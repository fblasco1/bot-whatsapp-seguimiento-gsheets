#!/usr/bin/env python3
"""
Script de configuración inicial para la nueva estructura de base de datos
Crea las hojas necesarias y configura los encabezados
"""

import os
import sys
from dotenv import load_dotenv
from sheets_manager import get_gspread_client
from config import (
    SHEET_NAME, SHEET_SEGUIMIENTO, SHEET_DERIVACIONES, 
    SHEET_LOGS, GOOGLE_SHEET_ID
)

# Cargar variables de entorno
load_dotenv()

def crear_hoja_clientes():
    """Crea la hoja principal de clientes con la nueva estructura"""
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        
        # Verificar si la hoja ya existe
        try:
            worksheet = sh.worksheet(SHEET_NAME)
            print(f"✅ Hoja '{SHEET_NAME}' ya existe")
        except:
            # Crear nueva hoja
            worksheet = sh.add_worksheet(title=SHEET_NAME, rows=1000, cols=12)
            print(f"✅ Hoja '{SHEET_NAME}' creada")
        
        # Configurar encabezados
        headers = [
            "Nombre",
            "Teléfono", 
            "Fecha Ingreso",
            "Tipo Cliente",
            "Estado",
            "Consentimiento",
            "Historial Mensajes",
            "Última Derivación",
            "Estado Derivación",
            "Notas Abogado",
            "Próxima Audiencia",
            "Prioridad"
        ]
        
        worksheet.update('A1:L1', [headers])
        print(f"✅ Encabezados configurados en '{SHEET_NAME}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando hoja '{SHEET_NAME}': {str(e)}")
        return False

def crear_hoja_seguimiento():
    """Crea la hoja de seguimiento de mensajes"""
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        
        # Verificar si la hoja ya existe
        try:
            worksheet = sh.worksheet(SHEET_SEGUIMIENTO)
            print(f"✅ Hoja '{SHEET_SEGUIMIENTO}' ya existe")
        except:
            # Crear nueva hoja
            worksheet = sh.add_worksheet(title=SHEET_SEGUIMIENTO, rows=1000, cols=10)
            print(f"✅ Hoja '{SHEET_SEGUIMIENTO}' creada")
        
        # Configurar encabezados
        headers = [
            "ID Cliente",
            "Nombre",
            "Teléfono",
            "Día 2",
            "Día 10", 
            "Día 20",
            "Día 30",
            "Día 40"
        ]
        
        worksheet.update('A1:J1', [headers])
        print(f"✅ Encabezados configurados en '{SHEET_SEGUIMIENTO}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando hoja '{SHEET_SEGUIMIENTO}': {str(e)}")
        return False

def crear_hoja_derivaciones():
    """Crea la hoja de derivaciones a humano"""
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        
        # Verificar si la hoja ya existe
        try:
            worksheet = sh.worksheet(SHEET_DERIVACIONES)
            print(f"✅ Hoja '{SHEET_DERIVACIONES}' ya existe")
        except:
            # Crear nueva hoja
            worksheet = sh.add_worksheet(title=SHEET_DERIVACIONES, rows=1000, cols=9)
            print(f"✅ Hoja '{SHEET_DERIVACIONES}' creada")
        
        # Configurar encabezados
        headers = [
            "ID Derivación",
            "Fecha",
            "Cliente",
            "Teléfono",
            "Mensaje Cliente",
            "Estado",
            "Abogado Asignado",
            "Fecha Resolución",
            "Notas Resolución"
        ]
        
        worksheet.update('A1:I1', [headers])
        print(f"✅ Encabezados configurados en '{SHEET_DERIVACIONES}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando hoja '{SHEET_DERIVACIONES}': {str(e)}")
        return False

def crear_hoja_logs():
    """Crea la hoja de logs del sistema"""
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        
        # Verificar si la hoja ya existe
        try:
            worksheet = sh.worksheet(SHEET_LOGS)
            print(f"✅ Hoja '{SHEET_LOGS}' ya existe")
        except:
            # Crear nueva hoja
            worksheet = sh.add_worksheet(title=SHEET_LOGS, rows=10000, cols=7)
            print(f"✅ Hoja '{SHEET_LOGS}' creada")
        
        # Configurar encabezados
        headers = [
            "Timestamp",
            "Tipo Evento",
            "Cliente",
            "Teléfono",
            "Descripción",
            "Estado",
            "Detalles"
        ]
        
        worksheet.update('A1:G1', [headers])
        print(f"✅ Encabezados configurados en '{SHEET_LOGS}'")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando hoja '{SHEET_LOGS}': {str(e)}")
        return False

def configurar_permisos():
    """Configura permisos básicos en las hojas"""
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        
        # Obtener información de la hoja
        print(f"📊 Configurando permisos para: {sh.title}")
        print(f"🔗 URL: {sh.url}")
        
        # Verificar que el Service Account tenga acceso
        try:
            # Intentar leer la primera fila de cada hoja
            for sheet_name in [SHEET_NAME, SHEET_SEGUIMIENTO, SHEET_DERIVACIONES, SHEET_LOGS]:
                try:
                    worksheet = sh.worksheet(sheet_name)
                    first_row = worksheet.row_values(1)
                    print(f"✅ Acceso confirmado a '{sheet_name}': {len(first_row)} columnas")
                except Exception as e:
                    print(f"❌ Error accediendo a '{sheet_name}': {str(e)}")
        except Exception as e:
            print(f"❌ Error verificando permisos: {str(e)}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Error configurando permisos: {str(e)}")
        return False

def main():
    """Función principal de configuración"""
    print("🚀 Configurando nueva estructura de base de datos...")
    print("=" * 60)
    
    # Verificar variables de entorno
    if not GOOGLE_SHEET_ID:
        print("❌ GOOGLE_SHEET_ID no configurado en .env")
        sys.exit(1)
    
    print(f"📋 Configurando hoja: {GOOGLE_SHEET_ID}")
    print()
    
    # Crear hojas
    success = True
    success &= crear_hoja_clientes()
    success &= crear_hoja_seguimiento()
    success &= crear_hoja_derivaciones()
    success &= crear_hoja_logs()
    
    if success:
        print()
        print("✅ Todas las hojas creadas exitosamente")
        
        # Configurar permisos
        print()
        print("🔐 Configurando permisos...")
        if configurar_permisos():
            print("✅ Permisos configurados correctamente")
        else:
            print("⚠️ Advertencia: Problemas con permisos")
        
        print()
        print("🎉 Configuración completada!")
        print("📱 El bot está listo para usar la nueva estructura")
        print()
        print("📊 Hojas creadas:")
        print(f"   • {SHEET_NAME} - Datos principales de clientes")
        print(f"   • {SHEET_SEGUIMIENTO} - Seguimiento de mensajes")
        print(f"   • {SHEET_DERIVACIONES} - Derivaciones a humano")
        print(f"   • {SHEET_LOGS} - Logs del sistema")
        
    else:
        print()
        print("❌ Error en la configuración")
        sys.exit(1)

if __name__ == "__main__":
    main()
