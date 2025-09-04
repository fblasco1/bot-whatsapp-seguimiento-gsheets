import logging
from datetime import datetime, timedelta
from sheets_manager import (
    get_clientes_pendientes_consentimiento,
    get_clientes_activos,
    actualizar_estado_cliente,
    actualizar_consentimiento_cliente,
    registrar_mensaje_enviado
)
from whatsapp_api import enviar_consentimiento_inicial
from config import ESTADOS_CLIENTE

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ConsentManager:
    """
    Gestiona el sistema de consentimiento y envío de mensajes iniciales
    """
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def enviar_consentimientos_pendientes(self):
        """
        Envía mensajes de consentimiento a clientes que aún no han respondido
        """
        try:
            clientes_pendientes = get_clientes_pendientes_consentimiento()
            self.logger.info(f"Encontrados {len(clientes_pendientes)} clientes pendientes de consentimiento")
            
            for cliente_data, row in clientes_pendientes:
                if len(cliente_data) >= 4:
                    nombre = cliente_data[0] if cliente_data[0] else "Cliente"
                    telefono = cliente_data[1]
                    
                    # Verificar si ya se envió consentimiento recientemente (últimas 24h)
                    if not self._consentimiento_enviado_recientemente(row):
                        # Enviar mensaje de consentimiento
                        if enviar_consentimiento_inicial(telefono, nombre):
                            # Actualizar estado y registrar envío
                            actualizar_estado_cliente(row, ESTADOS_CLIENTE["PENDIENTE_CONSENTIMIENTO"])
                            registrar_mensaje_enviado(row, "consentimiento_inicial_enviado")
                            self.logger.info(f"Consentimiento enviado a {nombre} ({telefono})")
                        else:
                            self.logger.error(f"Error enviando consentimiento a {nombre} ({telefono})")
                    else:
                        self.logger.info(f"Consentimiento ya enviado recientemente a {nombre} ({telefono})")
            
            return len(clientes_pendientes)
        
        except Exception as e:
            self.logger.error(f"Error enviando consentimientos pendientes: {str(e)}")
            return 0
    
    def _consentimiento_enviado_recientemente(self, row):
        """
        Verifica si se envió consentimiento en las últimas 24 horas
        """
        try:
            from sheets_manager import verificar_mensaje_enviado
            return verificar_mensaje_enviado(row, "consentimiento_inicial_enviado")
        except:
            return False
    
    def procesar_clientes_nuevos(self):
        """
        Procesa clientes nuevos y les envía consentimiento inicial
        """
        try:
            # Obtener todos los clientes
            from sheets_manager import get_clientes
            clientes = get_clientes()
            
            nuevos_enviados = 0
            
            for idx, cliente in enumerate(clientes, start=2):
                if len(cliente) >= 6:
                    nombre = cliente[0] if cliente[0] else "Cliente"
                    telefono = cliente[1]
                    estado = cliente[4] if len(cliente) > 4 else ""
                    consentimiento = cliente[5] if len(cliente) > 5 else ""
                    
                    # Si no hay estado ni consentimiento, es un cliente nuevo
                    if not estado and not consentimiento:
                        # Enviar consentimiento inicial
                        if enviar_consentimiento_inicial(telefono, nombre):
                            actualizar_estado_cliente(idx, ESTADOS_CLIENTE["PENDIENTE_CONSENTIMIENTO"])
                            registrar_mensaje_enviado(idx, "consentimiento_inicial_enviado")
                            nuevos_enviados += 1
                            self.logger.info(f"Cliente nuevo procesado: {nombre} ({telefono})")
            
            self.logger.info(f"Procesados {nuevos_enviados} clientes nuevos")
            return nuevos_enviados
        
        except Exception as e:
            self.logger.error(f"Error procesando clientes nuevos: {str(e)}")
            return 0
    
    def limpiar_estados_antiguos(self):
        """
        Limpia estados antiguos y resetea clientes que no respondieron
        """
        try:
            from sheets_manager import get_gspread_client, SHEET_NAME
            gc = get_gspread_client()
            sh = gc.open_by_key(os.getenv('GOOGLE_SHEET_ID'))
            worksheet = sh.worksheet(SHEET_NAME)
            
            # Obtener todas las filas
            all_values = worksheet.get_all_values()
            reseteados = 0
            
            for idx, row in enumerate(all_values[1:], start=2):
                if len(row) >= 6:
                    estado = row[4] if len(row) > 4 else ""
                    consentimiento = row[5] if len(row) > 5 else ""
                    
                    # Si está pendiente de consentimiento por más de 7 días, resetear
                    if (estado == ESTADOS_CLIENTE["PENDIENTE_CONSENTIMIENTO"] and 
                        not consentimiento):
                        # Verificar fecha del último mensaje
                        if self._debe_resetear_estado(idx):
                            actualizar_estado_cliente(idx, "")
                            actualizar_consentimiento_cliente(idx, "")
                            reseteados += 1
                            self.logger.info(f"Estado reseteado para fila {idx}")
            
            self.logger.info(f"Estados reseteados: {reseteados}")
            return reseteados
        
        except Exception as e:
            self.logger.error(f"Error limpiando estados antiguos: {str(e)}")
            return 0
    
    def _debe_resetear_estado(self, row):
        """
        Determina si se debe resetear el estado basado en la fecha del último mensaje
        """
        try:
            from sheets_manager import get_gspread_client, SHEET_NAME
            gc = get_gspread_client()
            sh = gc.open_by_key(os.getenv('GOOGLE_SHEET_ID'))
            worksheet = sh.worksheet(SHEET_NAME)
            
            # Obtener historial de mensajes
            historial = worksheet.acell(f'G{row}').value or ""
            
            if "consentimiento_inicial_enviado" in historial:
                # Buscar la fecha del último envío
                import re
                fecha_match = re.search(r'(\d{4}-\d{2}-\d{2})', historial)
                if fecha_match:
                    fecha_envio = datetime.strptime(fecha_match.group(1), '%Y-%m-%d')
                    dias_desde_envio = (datetime.now() - fecha_envio).days
                    return dias_desde_envio > 7
            
            return False
        
        except:
            return False

def main():
    """
    Función principal para ejecutar el gestor de consentimiento
    """
    manager = ConsentManager()
    
    logger.info("=== Iniciando Gestor de Consentimiento ===")
    
    # Procesar clientes nuevos
    nuevos = manager.procesar_clientes_nuevos()
    logger.info(f"Clientes nuevos procesados: {nuevos}")
    
    # Enviar consentimientos pendientes
    pendientes = manager.enviar_consentimientos_pendientes()
    logger.info(f"Consentimientos pendientes enviados: {pendientes}")
    
    # Limpiar estados antiguos
    reseteados = manager.limpiar_estados_antiguos()
    logger.info(f"Estados reseteados: {reseteados}")
    
    logger.info("=== Gestor de Consentimiento Completado ===")

if __name__ == "__main__":
    import os
    main()
