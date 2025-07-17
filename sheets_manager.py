import os
import gspread
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
from config import SHEET_NAME, SHEET_RANGE

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

# Actualizar estado de mensaje (opcional, si tienes una columna para esto)
def actualizar_estado_cliente(row, estado):
    gc = get_gspread_client()
    sh = gc.open_by_key(GOOGLE_SHEET_ID)
    worksheet = sh.worksheet(SHEET_NAME)
    worksheet.update_cell(row, 'D', estado)
