#!/usr/bin/env python3
"""
Servidor webhook para WhatsApp Bot
Ejecuta el servidor que recibe mensajes entrantes de WhatsApp
"""

import os
import sys
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Verificar variables requeridas
required_vars = [
    'WHATSAPP_API_TOKEN',
    'WHATSAPP_BUSINESS_PHONE_NUMBER_ID',
    'WHATSAPP_VERIFY_TOKEN',
    'GOOGLE_SHEET_ID',
    'GOOGLE_CREDENTIALS_FILE'
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    print(f"❌ Variables de entorno faltantes: {', '.join(missing_vars)}")
    print("Por favor, configura tu archivo .env")
    sys.exit(1)

print("✅ Variables de entorno configuradas correctamente")

# Importar y ejecutar el webhook
try:
    from webhook_handler import app, PORT, HOST
    
    print(f"🚀 Iniciando servidor webhook en {HOST}:{PORT}")
    print("📱 El bot está listo para recibir mensajes de WhatsApp")
    print("🔗 Webhook URL: https://tu-dominio.com/webhook")
    print("\n" + "="*50)
    
    app.run(host=HOST, port=PORT, debug=False)
    
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("Asegúrate de tener todas las dependencias instaladas")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error iniciando servidor: {e}")
    sys.exit(1)
