import logging
from datetime import datetime
from dateutil import parser
from sheets_manager import (
    get_clientes, 
    get_clientes_activos,
    actualizar_estado_cliente,
    registrar_mensaje_enviado
)
from whatsapp_api import enviar_mensaje_template
from consent_manager import ConsentManager
from config import TEMPLATES, SEGUIMIENTO_DIAS, ESTADOS_CLIENTE

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BotSeguimientoClientes:
    """
    Bot principal para seguimiento automatizado de clientes
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.consent_manager = ConsentManager()
    
    def procesar_consentimientos(self):
        """
        Procesa el sistema de consentimiento para clientes nuevos
        """
        self.logger.info("=== Procesando Sistema de Consentimiento ===")
        
        try:
            # Procesar clientes nuevos
            nuevos = self.consent_manager.procesar_clientes_nuevos()
            self.logger.info(f"Clientes nuevos procesados: {nuevos}")
            
            # Enviar consentimientos pendientes
            pendientes = self.consent_manager.enviar_consentimientos_pendientes()
            self.logger.info(f"Consentimientos pendientes enviados: {pendientes}")
            
            # Limpiar estados antiguos
            reseteados = self.consent_manager.limpiar_estados_antiguos()
            self.logger.info(f"Estados reseteados: {reseteados}")
            
        except Exception as e:
            self.logger.error(f"Error en sistema de consentimiento: {str(e)}")
    
    def procesar_seguimiento_automatico(self):
        """
        Procesa el envío automático de mensajes de seguimiento
        """
        self.logger.info("=== Procesando Seguimiento Automático ===")
        
        try:
            # Solo procesar clientes activos (con consentimiento otorgado)
            clientes_activos = get_clientes_activos()
            self.logger.info(f"Clientes activos encontrados: {len(clientes_activos)}")
            
            hoy = datetime.now().date()
            mensajes_enviados = 0
            
            for cliente_data, row in clientes_activos:
                if len(cliente_data) < 4:
                    self.logger.warning(f"Cliente sin datos suficientes: {cliente_data}")
                    continue
                
                nombre, telefono, fecha_ingreso, tipo_cliente = cliente_data[:4]
                tipo_cliente = tipo_cliente.strip().upper()
                
                try:
                    fecha = parser.parse(fecha_ingreso, dayfirst=True).date()
                except Exception as e:
                    self.logger.error(f"Fecha inválida para {nombre}: {fecha_ingreso} - {str(e)}")
                    continue
                
                dias = (hoy - fecha).days
                
                # Verificar si corresponde enviar algún mensaje de seguimiento
                for dia in SEGUIMIENTO_DIAS:
                    if dias == dia and tipo_cliente in TEMPLATES and dia in TEMPLATES[tipo_cliente]:
                        template_id = TEMPLATES[tipo_cliente][dia]
                        
                        # Verificar si ya se envió este mensaje
                        if not self._mensaje_ya_enviado(row, template_id):
                            # Pasar el nombre del cliente como {{1}} si el template lo requiere
                            if enviar_mensaje_template(telefono, template_id, components=[nombre]):
                                registrar_mensaje_enviado(row, template_id)
                                mensajes_enviados += 1
                                self.logger.info(f"Mensaje {template_id} enviado a {nombre} ({telefono}) - Día {dia}")
                            else:
                                self.logger.error(f"Error enviando mensaje {template_id} a {nombre} ({telefono})")
                        else:
                            self.logger.info(f"Mensaje {template_id} ya enviado a {nombre} ({telefono})")
            
            self.logger.info(f"Total de mensajes de seguimiento enviados: {mensajes_enviados}")
            return mensajes_enviados
            
        except Exception as e:
            self.logger.error(f"Error en seguimiento automático: {str(e)}")
            return 0
    
    def _mensaje_ya_enviado(self, row, template_id):
        """
        Verifica si un mensaje específico ya fue enviado
        """
        try:
            from sheets_manager import verificar_mensaje_enviado
            return verificar_mensaje_enviado(row, template_id)
        except:
            return False
    
    def ejecutar_ciclo_completo(self):
        """
        Ejecuta el ciclo completo del bot
        """
        self.logger.info("=== INICIANDO CICLO COMPLETO DEL BOT ===")
        
        try:
            # 1. Procesar consentimientos
            self.procesar_consentimientos()
            
            # 2. Procesar seguimiento automático
            mensajes_seguimiento = self.procesar_seguimiento_automatico()
            
            # 3. Resumen final
            self.logger.info("=== RESUMEN DEL CICLO ===")
            self.logger.info(f"Mensajes de seguimiento enviados: {mensajes_seguimiento}")
            self.logger.info("=== CICLO COMPLETADO ===")
            
        except Exception as e:
            self.logger.error(f"Error en ciclo completo: {str(e)}")

def main():
    """
    Función principal del bot
    """
    try:
        bot = BotSeguimientoClientes()
        bot.ejecutar_ciclo_completo()
        
    except Exception as e:
        logger.error(f"Error crítico en main: {str(e)}")
        raise

if __name__ == "__main__":
    main()
