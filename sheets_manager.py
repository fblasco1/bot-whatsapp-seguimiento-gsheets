import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from config import (
    SHEET_NAME, SHEET_RANGE, SHEET_SEGUIMIENTO, 
    SHEET_DERIVACIONES, SHEET_LOGS, ESTADOS_CLIENTE, ESTADOS_DERIVACION
)
from datetime import datetime

load_dotenv()
GOOGLE_SHEET_ID = os.getenv('GOOGLE_SHEET_ID')
GOOGLE_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'bot-seguimiento-clientes-24318d7ece5d.json')

# Autenticación Google Sheets
def get_gspread_client():
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    credentials = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=scopes)
    return gspread.authorize(credentials)

# Leer clientes de Google Sheets
def get_clientes():
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    return worksheet.get(SHEET_RANGE)

# Obtener cliente por número de teléfono
def get_cliente_por_telefono(telefono):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    # Buscar en la columna B (teléfono)
    try:
        cell = worksheet.find(str(telefono))
        if cell:
            row = cell.row
            cliente_data = worksheet.row_values(row)
            return cliente_data, row
    except gspread.exceptions.CellNotFound:
        return None, None
    return None, None

# Actualizar estado del cliente
def actualizar_estado_cliente(row, estado):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    # Columna E para estado
    worksheet.update_cell(row, 5, estado)
    print(f"Estado actualizado para fila {row}: {estado}")

# Actualizar consentimiento del cliente
def actualizar_consentimiento_cliente(row, consentimiento):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    # Columna F para consentimiento
    worksheet.update_cell(row, 6, consentimiento)
    print(f"Consentimiento actualizado para fila {row}: {consentimiento}")

# Registrar mensaje enviado
def registrar_mensaje_enviado(row, template_id, fecha_envio=None):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    if fecha_envio is None:
        fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Columna G para historial de mensajes
    historial_actual = worksheet.acell(f'G{row}').value or ""
    nuevo_mensaje = f"{fecha_envio}: {template_id}"
    
    if historial_actual:
        historial_actual += f"; {nuevo_mensaje}"
    else:
        historial_actual = nuevo_mensaje
    
    worksheet.update_cell(row, 7, historial_actual)
    print(f"Mensaje registrado para fila {row}: {template_id}")

# Verificar si el cliente ya recibió un mensaje específico
def verificar_mensaje_enviado(row, template_id):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    historial = worksheet.acell(f'G{row}').value or ""
    return template_id in historial

# Obtener clientes pendientes de consentimiento
def get_clientes_pendientes_consentimiento():
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    # Obtener todas las filas
    all_values = worksheet.get_all_values()
    pendientes = []
    
    for idx, row in enumerate(all_values[1:], start=2):  # Saltar header
        if len(row) >= 6:
            estado = row[4] if len(row) > 4 else ""
            consentimiento = row[5] if len(row) > 5 else ""
            
            if estado == ESTADOS_CLIENTE["PENDIENTE_CONSENTIMIENTO"] or not consentimiento:
                pendientes.append((row, idx))
    
    return pendientes

# Obtener clientes activos (con consentimiento otorgado)
def get_clientes_activos():
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    
    all_values = worksheet.get_all_values()
    activos = []
    
    for idx, row in enumerate(all_values[1:], start=2):
        if len(row) >= 6:
            estado = row[4] if len(row) > 4 else ""
            consentimiento = row[5] if len(row) > 5 else ""
            
            if (estado == ESTADOS_CLIENTE["CONSENTIMIENTO_OTORGADO"] or 
                estado == ESTADOS_CLIENTE["ACTIVO"] or
                consentimiento == "SI"):
                activos.append((row, idx))
    
    return activos

# ===== NUEVAS FUNCIONES PARA ESTRUCTURA MEJORADA =====

# Registrar derivación a humano
def registrar_derivacion_humano(telefono, nombre, mensaje_cliente):
    """
    Registra una nueva derivación a humano en la hoja de Derivaciones
    """
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sh.worksheet(SHEET_DERIVACIONES)
        
        # Generar ID único para la derivación
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        id_derivacion = f"DER_{timestamp}"
        
        # Fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        # Datos de la derivación
        derivacion_data = [
            id_derivacion,           # ID Derivación
            fecha_actual,            # Fecha
            nombre,                  # Cliente
            telefono,                # Teléfono
            mensaje_cliente,         # Mensaje del cliente
            ESTADOS_DERIVACION["PENDIENTE"],  # Estado
            "",                      # Abogado asignado (vacío por ahora)
            "",                      # Fecha resolución
            ""                       # Notas resolución
        ]
        
        # Agregar nueva fila
        worksheet.append_row(derivacion_data)
        print(f"Derivación registrada: {id_derivacion} para {nombre}")
        
        return id_derivacion
        
    except Exception as e:
        print(f"Error registrando derivación: {str(e)}")
        return None

# Actualizar estado de derivación
def actualizar_estado_derivacion(id_derivacion, nuevo_estado, notas=""):
    """
    Actualiza el estado de una derivación
    """
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sh.worksheet(SHEET_DERIVACIONES)
        
        # Buscar la derivación por ID
        try:
            cell = worksheet.find(id_derivacion)
            if cell:
                row = cell.row
                # Actualizar estado (columna F)
                worksheet.update_cell(row, 6, nuevo_estado)
                
                # Si se resuelve, agregar fecha de resolución
                if nuevo_estado == ESTADOS_DERIVACION["RESUELTO"]:
                    fecha_resolucion = datetime.now().strftime("%Y-%m-%d")
                    worksheet.update_cell(row, 8, fecha_resolucion)
                
                # Actualizar notas si se proporcionan
                if notas:
                    worksheet.update_cell(row, 9, notas)
                
                print(f"Estado de derivación {id_derivacion} actualizado a: {nuevo_estado}")
                return True
        except gspread.exceptions.CellNotFound:
            print(f"Derivación {id_derivacion} no encontrada")
            return False
            
    except Exception as e:
        print(f"Error actualizando estado de derivación: {str(e)}")
        return False

# Registrar log del sistema
def registrar_log(tipo_evento, cliente, telefono, descripcion, estado="EXITOSO", detalles=""):
    """
    Registra un evento en la hoja de Logs
    """
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sh.worksheet(SHEET_LOGS)
        
        # Timestamp actual
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Datos del log
        log_data = [
            timestamp,      # Timestamp
            tipo_evento,    # Tipo de evento
            cliente,        # Cliente
            telefono,       # Teléfono
            descripcion,    # Descripción
            estado,         # Estado
            detalles        # Detalles
        ]
        
        # Agregar nueva fila
        worksheet.append_row(log_data)
        print(f"Log registrado: {tipo_evento} - {cliente}")
        
    except Exception as e:
        print(f"Error registrando log: {str(e)}")

# Actualizar seguimiento de mensajes por día
def actualizar_seguimiento_dia(cliente_id, dia, estado="ENVIADO"):
    """
    Actualiza el estado de un mensaje específico en la hoja de Seguimiento
    """
    try:
        gc = get_gspread_client()
        sh = gc.open_by_key(GOOGLE_SHEET_ID)
        worksheet = sh.worksheet(SHEET_SEGUIMIENTO)
        
        # Buscar el cliente por ID
        try:
            cell = worksheet.find(cliente_id)
            if cell:
                row = cell.row
                # Determinar columna según el día
                columna_dia = {
                    2: 4,   # Día 2 -> Columna D
                    10: 5,  # Día 10 -> Columna E
                    20: 6,  # Día 20 -> Columna F
                    30: 7,  # Día 30 -> Columna G
                    40: 8,  # Día 40 -> Columna H
                    50: 9,  # Día 50 -> Columna I
                    60: 10  # Día 60 -> Columna J
                }
                
                if dia in columna_dia:
                    col = columna_dia[dia]
                    fecha_envio = datetime.now().strftime("%Y-%m-%d %H:%M")
                    worksheet.update_cell(row, col, fecha_envio)
                    print(f"Seguimiento actualizado: Día {dia} para {cliente_id}")
                    return True
                    
        except gspread.exceptions.CellNotFound:
            print(f"Cliente {cliente_id} no encontrado en seguimiento")
            return False
            
    except Exception as e:
        print(f"Error actualizando seguimiento: {str(e)}")
        return False
