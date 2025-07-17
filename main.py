from datetime import datetime
from dateutil import parser
from sheets_manager import get_clientes
from whatsapp_api import enviar_mensaje_template
from config import TEMPLATES, SEGUIMIENTO_DIAS

# Lógica principal
def procesar_mensajes():
    clientes = get_clientes()
    hoy = datetime.now().date()
    for idx, cliente in enumerate(clientes, start=2):
        # Se espera: nombre, telefono, fecha_ingreso, tipo_cliente
        if len(cliente) < 4:
            print(f"Cliente sin tipo: {cliente}")
            continue
        nombre, telefono, fecha_ingreso, tipo_cliente = cliente[:4]
        tipo_cliente = tipo_cliente.strip().upper()
        try:
            fecha = parser.parse(fecha_ingreso, dayfirst=True).date()
        except Exception:
            print(f"Fecha inválida para {nombre}: {fecha_ingreso}")
            continue
        dias = (hoy - fecha).days
        for dia in SEGUIMIENTO_DIAS:
            if dias == dia and tipo_cliente in TEMPLATES and dia in TEMPLATES[tipo_cliente]:
                template_id = TEMPLATES[tipo_cliente][dia]
                enviar_mensaje_template(telefono, template_id)
                # sheets_manager.actualizar_estado_cliente(idx, f"Template {template_id} enviado")

if __name__ == "__main__":
    procesar_mensajes()
