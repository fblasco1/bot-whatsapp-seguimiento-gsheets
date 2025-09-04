#!/usr/bin/env python3
"""
Script de validación de configuración
Verifica que todas las variables de entorno necesarias estén configuradas
"""

import os
import sys
from dotenv import load_dotenv

def validar_configuracion():
    """Valida que la configuración esté completa"""
    print("🔍 Validando configuración del bot...")
    print("=" * 50)
    
    # Cargar variables de entorno
    load_dotenv()
    
    # Variables requeridas
    variables_requeridas = {
        'GOOGLE_SHEET_ID': 'ID de la hoja de Google Sheets',
        'GOOGLE_CREDENTIALS_FILE': 'Archivo de credenciales de Google',
        'WHATSAPP_API_TOKEN': 'Token de la API de WhatsApp',
        'WHATSAPP_BUSINESS_PHONE_NUMBER_ID': 'ID del número de WhatsApp',
        'WHATSAPP_VERIFY_TOKEN': 'Token de verificación del webhook'
    }
    
    # Variables opcionales con valores por defecto
    variables_opcionales = {
        'PORT': '5000',
        'HOST': '0.0.0.0',
        'DEBUG': 'True',
        'ENVIRONMENT': 'local',
        'LOG_LEVEL': 'INFO',
        'MAX_MESSAGES_PER_HOUR': '100',
        'MAX_MESSAGES_PER_DAY': '1000',
        'WHATSAPP_API_TIMEOUT': '30',
        'GOOGLE_SHEETS_TIMEOUT': '30',
        'MAX_RETRIES': '3',
        'RETRY_DELAY': '5'
    }
    
    # Verificar variables requeridas
    print("📋 Variables requeridas:")
    faltantes = []
    for var, desc in variables_requeridas.items():
        valor = os.getenv(var)
        if valor:
            print(f"✅ {var}: {valor[:20]}{'...' if len(valor) > 20 else ''}")
        else:
            print(f"❌ {var}: FALTANTE - {desc}")
            faltantes.append(var)
    
    print()
    
    # Verificar variables opcionales
    print("🔧 Variables opcionales:")
    for var, default in variables_opcionales.items():
        valor = os.getenv(var, default)
        print(f"✅ {var}: {valor} {'(por defecto)' if valor == default else ''}")
    
    print()
    
    # Verificar archivo de credenciales
    archivo_credenciales = os.getenv('GOOGLE_CREDENTIALS_FILE', 'bot-seguimiento-clientes-24318d7ece5d.json')
    if os.path.exists(archivo_credenciales):
        print(f"✅ Archivo de credenciales: {archivo_credenciales}")
    else:
        print(f"❌ Archivo de credenciales no encontrado: {archivo_credenciales}")
        faltantes.append('ARCHIVO_CREDENCIALES')
    
    print()
    
    # Resultado final
    if faltantes:
        print("❌ Configuración incompleta!")
        print(f"Variables faltantes: {', '.join(faltantes)}")
        print("\n💡 Para configurar:")
        print("1. Copia config.env.example a .env")
        print("2. Edita .env con tus credenciales reales")
        print("3. Asegúrate de que el archivo de credenciales esté en la raíz del proyecto")
        return False
    else:
        print("🎉 ¡Configuración completa y válida!")
        print("\n✅ El bot está listo para ejecutarse")
        return True

def mostrar_configuracion_actual():
    """Muestra la configuración actual"""
    print("\n📊 Configuración actual:")
    print("=" * 30)
    
    # Importar config después de cargar .env
    try:
        from config import (
            GOOGLE_SHEET_ID, GOOGLE_CREDENTIALS_FILE, WHATSAPP_API_TOKEN,
            WHATSAPP_BUSINESS_PHONE_NUMBER_ID, WHATSAPP_VERIFY_TOKEN,
            PORT, HOST, DEBUG, ENVIRONMENT, LOG_LEVEL
        )
        
        config = {
            'Google Sheets ID': GOOGLE_SHEET_ID,
            'Credenciales': GOOGLE_CREDENTIALS_FILE,
            'WhatsApp Token': WHATSAPP_API_TOKEN[:20] + '...' if WHATSAPP_API_TOKEN else None,
            'Phone Number ID': WHATSAPP_BUSINESS_PHONE_NUMBER_ID,
            'Verify Token': WHATSAPP_VERIFY_TOKEN,
            'Puerto': PORT,
            'Host': HOST,
            'Debug': DEBUG,
            'Entorno': ENVIRONMENT,
            'Log Level': LOG_LEVEL
        }
        
        for key, value in config.items():
            if value is not None:
                print(f"  {key}: {value}")
            else:
                print(f"  {key}: No configurado")
                
    except ImportError as e:
        print(f"❌ Error importando configuración: {e}")
        print("💡 Asegúrate de que config.py esté en el mismo directorio")

def main():
    """Función principal"""
    print("🤖 Validador de Configuración - Bot WhatsApp")
    print("=" * 60)
    
    # Validar configuración
    config_valida = validar_configuracion()
    
    if config_valida:
        # Mostrar configuración actual
        mostrar_configuracion_actual()
        
        print("\n🚀 Próximos pasos:")
        print("1. Ejecutar: python setup_database.py")
        print("2. Ejecutar: python server.py")
        print("3. Desplegar en Render (usa render.yaml y gunicorn)")
        
    else:
        print("\n🛑 Corrige la configuración antes de continuar")
        sys.exit(1)

if __name__ == "__main__":
    main()
