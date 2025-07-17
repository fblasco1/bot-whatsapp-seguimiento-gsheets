
import requests
import re
from config import WHATSAPP_API_TOKEN, WHATSAPP_BUSINESS_PHONE_NUMBER_ID

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

# Enviar mensaje de texto por WhatsApp
def enviar_mensaje_whatsapp(telefono, mensaje):
    telefono_normalizado = normalizar_numero(telefono)
    if not telefono_normalizado:
        print(f"No se envía mensaje: número '{telefono}' no es válido para WhatsApp.")
        return
    headers = {
        'Authorization': f'Bearer {WHATSAPP_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'to': telefono_normalizado,
        'type': 'text',
        'text': {'body': mensaje}
    }
    response = requests.post(WHATSAPP_API_URL, json=data, headers=headers)
    if response.status_code != 200:
        print(f"Error enviando mensaje a {telefono_normalizado}: {response.text}")
    else:
        print(f"Mensaje enviado a {telefono_normalizado}")

# Enviar mensaje de plantilla por WhatsApp
def enviar_mensaje_template(telefono, template_id, language_code='es'):
    telefono_normalizado = normalizar_numero(telefono)
    if not telefono_normalizado:
        print(f"No se envía template: número '{telefono}' no es válido para WhatsApp.")
        return
    headers = {
        'Authorization': f'Bearer {WHATSAPP_API_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'to': telefono_normalizado,
        'type': 'template',
        'template': {
            'name': template_id,
            'language': {'code': language_code}
        }
    }
    response = requests.post(WHATSAPP_API_URL, json=data, headers=headers)
    if response.status_code != 200:
        print(f"Error enviando template {template_id} a {telefono_normalizado}: {response.text}")
    else:
        print(f"Template {template_id} enviado a {telefono_normalizado}")
