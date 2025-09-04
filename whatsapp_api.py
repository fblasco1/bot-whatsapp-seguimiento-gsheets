
import requests
import re
import json
from config import WHATSAPP_API_TOKEN, WHATSAPP_BUSINESS_PHONE_NUMBER_ID, CONSENT_TEMPLATES, TELEFONO_ABOGADO, WHATSAPP_TEMPLATE_LANGUAGE

WHATSAPP_API_URL = f"https://graph.facebook.com/v23.0/{WHATSAPP_BUSINESS_PHONE_NUMBER_ID}/messages"

# Normaliza un número de teléfono al formato +549XXXXXXXXXX (Argentina)
def normalizar_numero(telefono):
    """
    Normaliza un número de teléfono al formato +549XXXXXXXXXX.
    Elimina espacios, guiones, paréntesis y el '15' si está presente.
    """
    phone_number_str = str(telefono)
    cleaned_number = re.sub(r'[^\d+]', '', phone_number_str)

    # Eliminar el '+' inicial si ya está presente
    if cleaned_number.startswith('+'):
        cleaned_number = cleaned_number[1:]

    # Si el número empieza con "549", ya casi está bien
    if cleaned_number.startswith('549'):
        if len(cleaned_number) == 12:
            return "+" + cleaned_number
        if len(cleaned_number) == 13 and cleaned_number[3:5] == '15':
            return "+549" + cleaned_number[5:]
        if len(cleaned_number) > 10:
            return "+549" + cleaned_number[-10:]

    # Eliminar el "0" inicial si existe
    if cleaned_number.startswith('0'):
        cleaned_number = cleaned_number[1:]

    # Eliminar el "15" si existe
    if cleaned_number.startswith('15'):
        cleaned_number = cleaned_number[2:]

    # Si quedan 10 dígitos, añadir +549
    if len(cleaned_number) == 10:
        return "+549" + cleaned_number

    print(f"Advertencia: Número '{phone_number_str}' no pudo ser normalizado. Resulta: '{cleaned_number}'")
    return None

# Enviar mensaje de texto por WhatsApp (DESHABILITADO: solo se permiten plantillas)
def enviar_mensaje_whatsapp(telefono, mensaje):
    raise RuntimeError("El envío de texto libre está deshabilitado. Use plantillas de WhatsApp.")

# Enviar mensaje de plantilla por WhatsApp (soporta parámetros/components)
def enviar_mensaje_template(telefono, template_id, language_code=None, components=None):
    if language_code is None:
        language_code = WHATSAPP_TEMPLATE_LANGUAGE
    telefono_normalizado = normalizar_numero(telefono)
    if not telefono_normalizado:
        print(f"No se envía template: número '{telefono}' no es válido para WhatsApp.")
        return False

    def _build_components(components_input):
        if not components_input:
            return None
        # Si es una lista simple, se asume parámetros del body como texto
        if isinstance(components_input, list):
            params = [{"type": "text", "text": str(v)} for v in components_input]
            return [{"type": "body", "parameters": params}]
        # Si es dict, permitir keys: body, header, buttons (ya formateados)
        if isinstance(components_input, dict):
            comp_list = []
            if 'header' in components_input and components_input['header'] is not None:
                header_vals = components_input['header']
                if isinstance(header_vals, list):
                    header_params = [{"type": "text", "text": str(v)} for v in header_vals]
                else:
                    header_params = [{"type": "text", "text": str(header_vals)}]
                comp_list.append({"type": "header", "parameters": header_params})
            if 'body' in components_input and components_input['body'] is not None:
                body_vals = components_input['body']
                body_params = [{"type": "text", "text": str(v)} for v in (body_vals if isinstance(body_vals, list) else [body_vals])]
                comp_list.append({"type": "body", "parameters": body_params})
            if 'buttons' in components_input and components_input['buttons']:
                # Se espera una lista de botones ya formateados según API
                comp_list.extend([b for b in components_input['buttons'] if b])
            return comp_list or None
        return None

    headers = {
        'Authorization': f'Bearer {WHATSAPP_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    template_payload = {
        'name': template_id,
        'language': {'code': language_code}
    }
    built_components = _build_components(components)
    if built_components:
        template_payload['components'] = built_components

    data = {
        'messaging_product': 'whatsapp',
        'to': telefono_normalizado,
        'type': 'template',
        'template': template_payload
    }

    try:
        print(f"Enviando template='{template_id}' language='{language_code}' to='{telefono_normalizado}'")
        response = requests.post(WHATSAPP_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            print(f"Template {template_id} enviado a {telefono_normalizado}")
            return True
        else:
            print(f"Error enviando template {template_id} a {telefono_normalizado}: {response.text}")
            return False
    except Exception as e:
        print(f"Excepción enviando template {template_id} a {telefono_normalizado}: {str(e)}")
        return False

# Enviar mensaje de consentimiento inicial (template)
def enviar_consentimiento_inicial(telefono, nombre_cliente):
    template_name = CONSENT_TEMPLATES.get("consentimiento_inicial")
    return enviar_mensaje_template(telefono, template_name, components=[nombre_cliente])

# Enviar mensaje de confirmación de consentimiento (template)
def enviar_confirmacion_consentimiento(telefono, nombre_cliente):
    template_name = CONSENT_TEMPLATES.get("consentimiento_confirmado")
    return enviar_mensaje_template(telefono, template_name, components=[nombre_cliente])

# Enviar mensaje de derivación a humano (template)
def enviar_derivacion_humano(telefono, nombre_cliente):
    template_name = CONSENT_TEMPLATES.get("derivacion_humano")
    return enviar_mensaje_template(telefono, template_name, components=[nombre_cliente])

# Enviar notificación de derivación al abogado (template)
def notificar_derivacion_abogado(telefono_cliente, nombre_cliente, mensaje_cliente):
    """
    Envía notificación al abogado cuando un cliente solicita derivación
    """
    template_name = CONSENT_TEMPLATES.get("notificacion_derivacion_abogado")
    return enviar_mensaje_template(TELEFONO_ABOGADO, template_name, components=[nombre_cliente, telefono_cliente, mensaje_cliente])

# Enviar mensaje de rechazo de consentimiento (template)
def enviar_rechazo_consentimiento(telefono, nombre_cliente):
    template_name = CONSENT_TEMPLATES.get("consentimiento_rechazado")
    return enviar_mensaje_template(telefono, template_name, components=[nombre_cliente])

# Verificar si un mensaje es una respuesta de consentimiento
def es_respuesta_consentimiento(mensaje):
    mensaje_lower = mensaje.lower().strip()
    respuestas_si = ['si', 'sí', 'yes', 'ok', 'okay', 'acepto', 'autorizo', '✅', '1']
    respuestas_no = ['no', 'not', 'rechazo', 'no autorizo', '❌', '0']
    
    if mensaje_lower in respuestas_si:
        return 'SI'
    elif mensaje_lower in respuestas_no:
        return 'NO'
    else:
        return None

# Verificar si un mensaje solicita derivación a humano
def solicita_derivacion_humano(mensaje):
    mensaje_lower = mensaje.lower().strip()
    palabras_clave = ['consulta', 'pregunta', 'duda', 'ayuda', 'hablar', 'humano', 'abogado', 'urgente']
    
    return any(palabra in mensaje_lower for palabra in palabras_clave)

# Verificar si un mensaje solicita reactivar notificaciones
def solicita_reactivacion(mensaje):
    mensaje_lower = mensaje.lower().strip()
    return 'reactivar' in mensaje_lower or 'activar' in mensaje_lower
