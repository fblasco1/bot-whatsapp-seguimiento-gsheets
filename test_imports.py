#!/usr/bin/env python3
"""
Script de prueba para verificar importaciones
"""

print("🧪 Probando importaciones...")

try:
    from webhook_handler import app, PORT, HOST
    print(f"✅ webhook_handler: OK - {HOST}:{PORT}")
except Exception as e:
    print(f"❌ webhook_handler: {e}")

try:
    from config import WHATSAPP_VERIFY_TOKEN
    print("✅ config: OK")
except Exception as e:
    print(f"❌ config: {e}")

try:
    from sheets_manager import get_gspread_client
    print("✅ sheets_manager: OK")
except Exception as e:
    print(f"❌ sheets_manager: {e}")

try:
    from whatsapp_api import enviar_confirmacion_consentimiento
    print("✅ whatsapp_api: OK")
except Exception as e:
    print(f"❌ whatsapp_api: {e}")

print("\n🎯 Prueba completada!")

