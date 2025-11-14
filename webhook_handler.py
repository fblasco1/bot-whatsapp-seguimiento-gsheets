import json
import logging
import threading
from datetime import datetime
from flask import Flask, request, jsonify
from config import WHATSAPP_VERIFY_TOKEN, ESTADOS_CLIENTE, HOST, PORT, TASK_SECRET
from sheets_manager import (
    get_cliente_por_telefono, 
    actualizar_estado_cliente, 
    actualizar_consentimiento_cliente,
    registrar_mensaje_enviado,
    registrar_derivacion_humano,
    registrar_log
)
from whatsapp_api import (
    enviar_confirmacion_consentimiento,
    enviar_rechazo_consentimiento,
    enviar_derivacion_humano,
    es_respuesta_consentimiento,
    solicita_derivacion_humano,
    solicita_reactivacion,
    notificar_derivacion_abogado
)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def _require_task_token(req):
    """Valida cabecera X-Task-Token para endpoints de tareas programadas."""
    if not TASK_SECRET:
        return False
    token = req.headers.get('X-Task-Token') or req.args.get('token')
    return token == TASK_SECRET

def procesar_mensaje_entrante(telefono, mensaje, nombre_cliente=None):
    """
    Procesa un mensaje entrante y determina la acción a tomar
    """
    logger.info(f"Procesando mensaje de {telefono}: {mensaje}")
    
    # Buscar cliente en la base de datos
    cliente_data, row = get_cliente_por_telefono(telefono)
    
    if not cliente_data:
        logger.warning(f"Cliente no encontrado para teléfono: {telefono}")
        return False
    
    if len(cliente_data) < 4:
        logger.error(f"Datos insuficientes para cliente: {cliente_data}")
        return False
    
    nombre = cliente_data[0] if cliente_data[0] else "Cliente"
    estado_actual = cliente_data[4] if len(cliente_data) > 4 else ""
    consentimiento = cliente_data[5] if len(cliente_data) > 5 else ""
    
    # Procesar según el estado actual del cliente
    if not consentimiento or estado_actual == ESTADOS_CLIENTE["PENDIENTE_CONSENTIMIENTO"]:
        return procesar_consentimiento(telefono, mensaje, nombre, row)
    
    elif consentimiento == "SI" and estado_actual in [ESTADOS_CLIENTE["CONSENTIMIENTO_OTORGADO"], ESTADOS_CLIENTE["ACTIVO"]]:
        return procesar_cliente_activo(telefono, mensaje, nombre, row)
    
    elif consentimiento == "NO":
        return procesar_cliente_inactivo(telefono, mensaje, nombre, row)
    
    return False

def procesar_consentimiento(telefono, mensaje, nombre, row):
    """
    Procesa respuesta de consentimiento del cliente
    """
    respuesta = es_respuesta_consentimiento(mensaje)
    
    if respuesta == "SI":
        # Cliente acepta consentimiento
        actualizar_consentimiento_cliente(row, "SI")
        actualizar_estado_cliente(row, ESTADOS_CLIENTE["ACTIVO"])
        registrar_mensaje_enviado(row, "consentimiento_aceptado")
        
        # Enviar confirmación de bienvenida
        if enviar_confirmacion_consentimiento(telefono, nombre):
            logger.info(f"Mensaje de bienvenida enviado a {nombre} ({telefono})")
        else:
            logger.error(f"Error enviando mensaje de bienvenida a {nombre} ({telefono})")
        logger.info(f"Consentimiento aceptado para {nombre} ({telefono}) - Cliente activado")
        return True
    
    elif respuesta == "NO":
        # Cliente rechaza consentimiento
        actualizar_consentimiento_cliente(row, "NO")
        actualizar_estado_cliente(row, ESTADOS_CLIENTE["CONSENTIMIENTO_RECHAZADO"])
        registrar_mensaje_enviado(row, "consentimiento_rechazado")
        
        # Enviar mensaje de rechazo
        enviar_rechazo_consentimiento(telefono, nombre)
        logger.info(f"Consentimiento rechazado para {nombre} ({telefono})")
        return True
    
    else:
        # Respuesta no reconocida
        logger.info(f"Respuesta no reconocida de {nombre} ({telefono}): {mensaje}")
        return False

def procesar_cliente_activo(telefono, mensaje, nombre, row):
    """
    Procesa mensaje de cliente con consentimiento otorgado
    """
    if solicita_derivacion_humano(mensaje):
        # Cliente solicita hablar con humano
        # NO cambiar el estado principal, solo marcar como derivado temporalmente
        actualizar_estado_cliente(row, ESTADOS_CLIENTE["ACTIVO"])  # Mantener activo
        registrar_mensaje_enviado(row, "derivacion_humano_solicitada")
        
        # Registrar derivación en la hoja de Derivaciones
        id_derivacion = registrar_derivacion_humano(telefono, nombre, mensaje)
        
        # Registrar log del evento
        registrar_log(
            "DERIVACION_HUMANO", 
            nombre, 
            telefono, 
            f"Cliente solicitó derivación a humano - ID: {id_derivacion}",
            "EXITOSO"
        )
        
        # Enviar confirmación de derivación al cliente
        enviar_derivacion_humano(telefono, nombre)
        
        # Enviar notificación al abogado
        notificar_derivacion_abogado(telefono, nombre, mensaje)
        
        logger.info(f"Cliente {nombre} ({telefono}) derivado a humano - FLUJO MANTENIDO")
        return True
    
    elif solicita_reactivacion(mensaje):
        # Cliente solicita reactivar notificaciones
        actualizar_estado_cliente(row, ESTADOS_CLIENTE["ACTIVO"])
        registrar_mensaje_enviado(row, "notificaciones_reactivadas")
        
        # Registrar log del evento
        registrar_log(
            "REACTIVACION", 
            nombre, 
            telefono, 
            "Cliente reactivó notificaciones",
            "EXITOSO"
        )
        
        # Enviar confirmación de reactivación
        enviar_confirmacion_consentimiento(telefono, nombre)
        logger.info(f"Notificaciones reactivadas para {nombre} ({telefono})")
        return True
    
    else:
        # Mensaje no reconocido, registrar para análisis
        registrar_mensaje_enviado(row, f"mensaje_entrante: {mensaje[:50]}")
        
        # Registrar log del evento
        registrar_log(
            "MENSAJE_NO_RECONOCIDO", 
            nombre, 
            telefono, 
            f"Mensaje no reconocido: {mensaje[:50]}",
            "INFO"
        )
        
        logger.info(f"Mensaje no reconocido de {nombre} ({telefono}): {mensaje}")
        return False

def procesar_cliente_inactivo(telefono, mensaje, nombre, row):
    """
    Procesa mensaje de cliente que rechazó consentimiento
    """
    if solicita_reactivacion(mensaje):
        # Cliente solicita reactivar notificaciones
        actualizar_consentimiento_cliente(row, "SI")
        actualizar_estado_cliente(row, ESTADOS_CLIENTE["ACTIVO"])
        registrar_mensaje_enviado(row, "consentimiento_reactivado")
        
        # Enviar confirmación de reactivación
        enviar_confirmacion_consentimiento(telefono, nombre)
        logger.info(f"Consentimiento reactivado para {nombre} ({telefono})")
        return True
    
    else:
        # Registrar mensaje para análisis
        registrar_mensaje_enviado(row, f"mensaje_cliente_inactivo: {mensaje[:50]}")
        logger.info(f"Mensaje de cliente inactivo {nombre} ({telefono}): {mensaje}")
        return False

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """
    Verifica el webhook de WhatsApp
    """
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode and token:
        if mode == 'subscribe' and token == WHATSAPP_VERIFY_TOKEN:
            logger.info("Webhook verificado exitosamente")
            return challenge
        else:
            logger.error("Verificación de webhook fallida")
            return 'Forbidden', 403
    
    return 'Bad Request', 400

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    """
    Maneja los mensajes entrantes de WhatsApp
    Responde inmediatamente y procesa en background para evitar timeouts de Cloudflare
    """
    try:
        data = request.get_json()
        logger.info(f"Webhook recibido: {json.dumps(data, indent=2)}")
        
        # Verificar que sea un mensaje de WhatsApp
        if 'object' not in data or data['object'] != 'whatsapp_business_account':
            return jsonify({'status': 'ignored'}), 200
        
        # Procesar cada entrada en background para responder rápidamente
        def procesar_mensajes_background():
            try:
                for entry in data.get('entry', []):
                    for change in entry.get('changes', []):
                        if change.get('value', {}).get('messages'):
                            for message in change['value']['messages']:
                                mtype = message.get('type')
                                telefono = message.get('from')
                                logger.info(f"Mensaje entrante tipo={mtype} desde {telefono}")

                                if mtype == 'text':
                                    mensaje = message['text']['body']
                                    procesar_mensaje_entrante(telefono, mensaje)
                                elif mtype == 'button':
                                    # Respuesta a botones 'reply button'
                                    btn = message.get('button', {})
                                    # Preferir 'text'; fallback a 'payload' si existiera
                                    mensaje = btn.get('text') or btn.get('payload') or ''
                                    if mensaje:
                                        procesar_mensaje_entrante(telefono, mensaje)
                                elif mtype == 'interactive':
                                    inter = message.get('interactive', {})
                                    itype = inter.get('type')
                                    if itype == 'button_reply':
                                        btn = inter.get('button_reply', {})
                                        # Usar el título visible del botón
                                        mensaje = btn.get('title') or btn.get('id') or ''
                                        if mensaje:
                                            procesar_mensaje_entrante(telefono, mensaje)
                                    elif itype == 'list_reply':
                                        rep = inter.get('list_reply', {})
                                        mensaje = rep.get('title') or rep.get('id') or ''
                                        if mensaje:
                                            procesar_mensaje_entrante(telefono, mensaje)
                                else:
                                    logger.info(f"Tipo de mensaje no manejado: {mtype}")
            except Exception as e:
                logger.error(f"Error procesando mensajes en background: {str(e)}")
        
        # Iniciar procesamiento en background y responder inmediatamente
        threading.Thread(target=procesar_mensajes_background, daemon=True).start()
        
        # Responder inmediatamente para evitar timeouts de Cloudflare
        return jsonify({'status': 'accepted'}), 202
    
    except Exception as e:
        logger.error(f"Error procesando webhook: {str(e)}")
        # Aún así responder rápidamente con error
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint de verificación de salud del servicio
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'WhatsApp Bot Webhook'
    }), 200

if __name__ == '__main__':
    logger.info("Iniciando servidor webhook...")
    app.run(host=HOST, port=PORT, debug=False)

@app.route('/tasks/daily', methods=['POST'])
def run_daily_task():
    """
    Endpoint protegido para ejecutar el ciclo diario del bot.
    Requiere cabecera X-Task-Token = TASK_SECRET.
    Responde inmediatamente para evitar timeouts de Cloudflare Workers.
    """
    if not _require_task_token(request):
        logger.warning("Intento de acceso a /tasks/daily sin token válido")
        return jsonify({'status': 'forbidden'}), 403

    try:
        # Ejecutar en segundo plano para responder inmediatamente
        # Esto evita timeouts de Cloudflare (timeout de 100s en plan free)
        # Importante: responder rápido para evitar error 524
        from main import BotSeguimientoClientes

        def _run():
            try:
                logger.info("Iniciando tarea diaria en background")
                bot = BotSeguimientoClientes()
                bot.ejecutar_ciclo_completo()
                logger.info("Tarea diaria completada exitosamente")
            except Exception as e:
                logger.error(f"Error en tarea diaria: {str(e)}", exc_info=True)

        # Iniciar thread en background y responder inmediatamente
        thread = threading.Thread(target=_run, daemon=True)
        thread.start()
        
        logger.info("Tarea diaria iniciada en background, respondiendo 202")
        return jsonify({
            'status': 'started',
            'message': 'Tarea diaria iniciada en background'
        }), 202
    except Exception as e:
        logger.error(f"Error iniciando tarea diaria: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': str(e)}), 500
