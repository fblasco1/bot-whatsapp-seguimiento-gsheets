# Configuración general del bot
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# =============================================================================
# CONFIGURACIÓN DE GOOGLE SHEETS
# =============================================================================
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'bot-seguimiento-clientes-24318d7ece5d.json')

# Nombres de las hojas
SHEET_NAME = "Clientes"
SHEET_SEGUIMIENTO = "Seguimiento"
SHEET_DERIVACIONES = "Derivaciones"
SHEET_LOGS = "Logs"
SHEET_RANGE = "A2:L"  # Expandido para incluir más columnas

# =============================================================================
# CONFIGURACIÓN DE WHATSAPP BUSINESS API
# =============================================================================
WHATSAPP_API_TOKEN = os.getenv('WHATSAPP_API_TOKEN')
WHATSAPP_BUSINESS_PHONE_NUMBER_ID = os.getenv('WHATSAPP_BUSINESS_PHONE_NUMBER_ID')
WHATSAPP_VERIFY_TOKEN = os.getenv('WHATSAPP_VERIFY_TOKEN', 'default_verify_token')
WHATSAPP_TEMPLATE_LANGUAGE = os.getenv('WHATSAPP_TEMPLATE_LANGUAGE', 'es_AR')

# Número del abogado para derivaciones
TELEFONO_ABOGADO = "+5491169817078"

# =============================================================================
# CONFIGURACIÓN DEL SERVIDOR
# =============================================================================
PORT = int(os.getenv('PORT', 5000))
HOST = os.getenv('HOST', '0.0.0.0')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
ENVIRONMENT = os.getenv('ENVIRONMENT', 'local')

# =============================================================================
# CONFIGURACIÓN DE TAREAS (ENDPOINTS PROTEGIDOS)
# =============================================================================
TASK_SECRET = os.getenv('TASK_SECRET')

# =============================================================================
# PARÁMETROS DE NEGOCIO
# =============================================================================
# Días de seguimiento (ajustado según README: 2, 10, 20, 30, 40)
SEGUIMIENTO_DIAS = [2, 10, 20, 30, 40]

# Templates por tipo de cliente y día
TEMPLATES = {
    "ART": {
        2: "art_template_2dias",
        10: "art_template_10dias",
        20: "art_template_20dias",
        30: "art_template_30dias",
        40: "art_template_40dias"
    },
    "TRANSITO": {
        2: "dia_2_accidente_transito",
        10: "accidente_transito_dia10",
        20: "accidente_transito_dia20",
        30: "dia_30_acccidente_transito",
        40: "accidente_transito_dia40"
    }
}

# Templates de consentimiento y derivación
CONSENT_TEMPLATES = {
    "consentimiento_inicial": "consentimiento_inicial_template",
    "consentimiento_confirmado": "consentimiento_confirmado_template",
    "consentimiento_rechazado": "consentimiento_rechazado_template",
    "derivacion_humano": "derivacion_humano_template",
    "notificacion_derivacion_abogado": "notificacion_derivacion_abogado_template"
}

# =============================================================================
# ESTADOS DEL SISTEMA
# =============================================================================
# Estados del cliente
ESTADOS_CLIENTE = {
    "PENDIENTE_CONSENTIMIENTO": "PENDIENTE_CONSENTIMIENTO",
    "CONSENTIMIENTO_OTORGADO": "CONSENTIMIENTO_OTORGADO",
    "CONSENTIMIENTO_RECHAZADO": "CONSENTIMIENTO_RECHAZADO",
    "DERIVADO_HUMANO": "DERIVADO_HUMANO",
    "ACTIVO": "ACTIVO",
    "INACTIVO": "INACTIVO"
}

# Estados de derivación
ESTADOS_DERIVACION = {
    "PENDIENTE": "PENDIENTE",
    "EN_PROCESO": "EN_PROCESO",
    "RESUELTO": "RESUELTO"
}

# =============================================================================
# VALIDACIÓN DE CONFIGURACIÓN
# =============================================================================
def validar_configuracion():
    """Valida que la configuración esté completa"""
    variables_requeridas = [
        'GOOGLE_SHEET_ID',
        'GOOGLE_CREDENTIALS_FILE',
        'WHATSAPP_API_TOKEN',
        'WHATSAPP_BUSINESS_PHONE_NUMBER_ID',
        'WHATSAPP_VERIFY_TOKEN'
    ]
    
    faltantes = []
    for var in variables_requeridas:
        if not globals().get(var):
            faltantes.append(var)
    
    if faltantes:
        raise ValueError(f"Variables de entorno faltantes: {', '.join(faltantes)}")
    
    return True

# =============================================================================
# CONFIGURACIÓN DE LOGS
# =============================================================================
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = os.path.join('logs', 'bot.log')

# =============================================================================
# CONFIGURACIÓN DE RATE LIMITING
# =============================================================================
# Límites para evitar spam
MAX_MESSAGES_PER_HOUR = int(os.getenv('MAX_MESSAGES_PER_HOUR', 100))
MAX_MESSAGES_PER_DAY = int(os.getenv('MAX_MESSAGES_PER_DAY', 1000))

# =============================================================================
# CONFIGURACIÓN DE TIMEOUTS
# =============================================================================
# Timeouts para APIs externas
WHATSAPP_API_TIMEOUT = int(os.getenv('WHATSAPP_API_TIMEOUT', 30))
GOOGLE_SHEETS_TIMEOUT = int(os.getenv('GOOGLE_SHEETS_TIMEOUT', 30))

# =============================================================================
# CONFIGURACIÓN DE RETRY
# =============================================================================
# Reintentos para operaciones fallidas
MAX_RETRIES = int(os.getenv('MAX_RETRIES', 3))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', 5))  # segundos
