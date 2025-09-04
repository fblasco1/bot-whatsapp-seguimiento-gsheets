# Estructura de Base de Datos - Bot WhatsApp Seguimiento Clientes

## 📊 Estructura de Google Sheets

### Hoja Principal: "Clientes"

| Col | Nombre | Descripción | Formato | Ejemplo | Actualización |
|-----|--------|-------------|---------|---------|---------------|
| **A** | **Nombre** | Nombre completo del cliente | Texto | Juan Pérez | Manual |
| **B** | **Teléfono** | Número de teléfono | Texto | 1123456789 | Manual |
| **C** | **Fecha Ingreso** | Fecha de ingreso del caso | DD/MM/YYYY | 01/01/2024 | Manual |
| **D** | **Tipo Cliente** | Categoría del cliente | ART/TRANSITO | TRANSITO | Manual |
| **E** | **Estado** | Estado actual del cliente | Texto | ACTIVO | Automático |
| **F** | **Consentimiento** | Consentimiento otorgado | SI/NO | SI | Automático |
| **G** | **Historial Mensajes** | Registro de mensajes enviados | Texto | Ver formato abajo | Automático |
| **H** | **Última Derivación** | Fecha de última derivación a humano | DD/MM/YYYY | 15/01/2024 | Automático |
| **I** | **Estado Derivación** | Estado de la derivación | PENDIENTE/RESUELTO | PENDIENTE | Automático |
| **J** | **Notas Abogado** | Comentarios del abogado | Texto | Cliente consultó sobre... | Manual |
| **K** | **Próxima Audiencia** | Fecha de próxima audiencia | DD/MM/YYYY | 15/02/2024 | Manual |
| **L** | **Prioridad** | Nivel de prioridad del caso | ALTA/MEDIA/BAJA | MEDIA | Manual |

### Hoja de Seguimiento: "Seguimiento"

| Col | Nombre | Descripción | Formato | Ejemplo |
|-----|--------|-------------|---------|---------|
| **A** | **ID Cliente** | Referencia al cliente | Texto | Cliente_001 |
| **B** | **Nombre** | Nombre del cliente | Texto | Juan Pérez |
| **C** | **Teléfono** | Número de teléfono | Texto | 1123456789 |
| **D** | **Día 2** | Mensaje día 2 enviado | SI/NO/FECHA | 03/01/2024 10:00 |
| **E** | **Día 10** | Mensaje día 10 enviado | SI/NO/FECHA | 11/01/2024 10:00 |
| **F** | **Día 20** | Mensaje día 20 enviado | SI/NO/FECHA | 21/01/2024 10:00 |
| **G** | **Día 30** | Mensaje día 30 enviado | SI/NO/FECHA | 31/01/2024 10:00 |
| **H** | **Día 40** | Mensaje día 40 enviado | SI/NO/FECHA | 10/02/2024 10:00 |
| **I** | **Día 50** | Mensaje día 50 enviado | SI/NO/FECHA | 20/02/2024 10:00 |
| **J** | **Día 60** | Mensaje día 60 enviado | SI/NO/FECHA | 02/03/2024 10:00 |

### Hoja de Derivaciones: "Derivaciones"

| Col | Nombre | Descripción | Formato | Ejemplo |
|-----|--------|-------------|---------|---------|
| **A** | **ID Derivación** | Identificador único | Texto | DER_001 |
| **B** | **Fecha** | Fecha de la derivación | DD/MM/YYYY HH:MM | 15/01/2024 14:30 |
| **C** | **Cliente** | Nombre del cliente | Texto | Juan Pérez |
| **D** | **Teléfono** | Teléfono del cliente | Texto | 1123456789 |
| **E** | **Mensaje Cliente** | Mensaje que generó derivación | Texto | Necesito hablar con un abogado |
| **F** | **Estado** | Estado de la derivación | PENDIENTE/RESUELTO | PENDIENTE |
| **G** | **Abogado Asignado** | Abogado responsable | Texto | Dr. Guiggi |
| **H** | **Fecha Resolución** | Fecha de resolución | DD/MM/YYYY | 16/01/2024 |
| **I** | **Notas Resolución** | Comentarios de resolución | Texto | Cliente contactado, consulta resuelta |

### Hoja de Logs: "Logs"

| Col | Nombre | Descripción | Formato | Ejemplo |
|-----|--------|-------------|---------|---------|
| **A** | **Timestamp** | Fecha y hora del evento | DD/MM/YYYY HH:MM:SS | 15/01/2024 14:30:25 |
| **B** | **Tipo Evento** | Tipo de evento | Texto | MENSAJE_ENVIADO |
| **C** | **Cliente** | Cliente afectado | Texto | Juan Pérez |
| **D** | **Teléfono** | Teléfono del cliente | Texto | 1123456789 |
| **E** | **Descripción** | Descripción del evento | Texto | Template día 10 enviado |
| **F** | **Estado** | Estado del evento | EXITOSO/ERROR | EXITOSO |
| **G** | **Detalles** | Detalles adicionales | Texto | WhatsApp API: 200 OK |

## 🔄 Flujo de Estados del Cliente

### Estados Principales (Columna E)
- **PENDIENTE_CONSENTIMIENTO**: Cliente nuevo, esperando respuesta
- **CONSENTIMIENTO_OTORGADO**: Cliente aceptó, listo para seguimiento
- **ACTIVO**: Cliente activo en seguimiento automático
- **CONSENTIMIENTO_RECHAZADO**: Cliente rechazó notificaciones
- **INACTIVO**: Cliente inactivo por otras razones

### Estados de Derivación (Columna I)
- **PENDIENTE**: Derivación solicitada, esperando resolución
- **RESUELTO**: Derivación resuelta por abogado
- **EN_PROCESO**: Abogado en contacto con cliente

## 📱 Formato del Historial de Mensajes (Columna G)

```
2024-01-01 10:00: consentimiento_inicial_enviado
2024-01-01 15:30: consentimiento_aceptado
2024-01-03 10:00: template_2dias_enviado
2024-01-11 10:00: template_10dias_enviado
2024-01-15 14:30: derivacion_humano_solicitada
2024-01-21 10:00: template_20dias_enviado
```

## 🚀 Configuración Inicial

### 1. Crear las hojas en Google Sheets
- **Clientes**: Hoja principal con datos de clientes
- **Seguimiento**: Seguimiento de mensajes por día
- **Derivaciones**: Registro de derivaciones a humano
- **Logs**: Logs del sistema

### 2. Configurar encabezados
- Primera fila de cada hoja debe contener los nombres de las columnas
- El bot lee desde la fila 2 en adelante

### 3. Permisos
- Asegurar que el Service Account tenga permisos de lectura/escritura
- Compartir la hoja con la cuenta de servicio

## 📊 Ventajas de la Nueva Estructura

1. **Separación de Responsabilidades**: Cada hoja tiene un propósito específico
2. **Trazabilidad Completa**: Seguimiento detallado de cada cliente
3. **Gestión de Derivaciones**: Control de derivaciones sin cortar flujo
4. **Logs Detallados**: Auditoría completa de todas las operaciones
5. **Escalabilidad**: Fácil agregar nuevas funcionalidades
6. **Mantenimiento**: Estructura clara y organizada

## 🔧 Migración desde Estructura Anterior

Si ya tienes datos en la estructura anterior:

1. **Crear nuevas hojas** con la estructura descrita
2. **Migrar datos existentes** de la hoja "Clientes"
3. **Ejecutar bot** para poblar automáticamente las nuevas hojas
4. **Verificar funcionamiento** antes de eliminar estructura anterior
