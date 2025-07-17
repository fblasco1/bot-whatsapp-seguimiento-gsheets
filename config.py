# Configuración general del bot
import os

# Parámetros de negocio
SHEET_NAME = "Clientes"
SHEET_RANGE = "A2:D"  # Se espera columna tipo de cliente en D
SEGUIMIENTO_DIAS = [2, 10, 20, 30]

# Templates por tipo de cliente y día
TEMPLATES = {
    "ART": {
        2: "art_template_2dias",
        10: "art_template_10dias",
        20: "art_template_20dias",
        30: "art_template_30dias"
    },
    "TRANSITO": {
        2: "transito_template_2dias",
        10: "transito_template_10dias",
        20: "transito_template_20dias",
        30: "transito_template_30dias"
    }
}

# Acceso a variables sensibles desde el entorno
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE')
WHATSAPP_API_TOKEN = os.getenv('WHATSAPP_API_TOKEN')
WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv('WHATSAPP_BUSINESS_PHONE_NUMBER_ID')
