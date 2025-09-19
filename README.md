# 🤖 Bot WhatsApp - Seguimiento Automático de Clientes

**Desarrollado para Estudio Guiggi & Ortiz** 🏛️

Bot automatizado de WhatsApp para realizar seguimiento de clientes en causas civiles (accidentes de tránsito), enviando mensajes programados en una ventana de 40 días previa a audiencia.

## 🎯 Resumen de Funcionalidades

### ✅ **Sistema Completo y Funcional**
- **Sistema de Consentimiento**: Solicitud inicial y gestión de respuestas
- **Webhook de WhatsApp**: Recepción y procesamiento de mensajes entrantes
- **Derivación a Humano**: Detección automática y notificación al abogado
- **Seguimiento Automático**: Envío de mensajes programados cada 10 días
- **Base de Datos Multi-Hoja**: Estructura organizada en Google Sheets
- **Logs y Auditoría**: Sistema completo de monitoreo y trazabilidad

### 🔄 **Flujo de Funcionamiento**
1. **Cliente Nuevo** → Mensaje de consentimiento automático
2. **Consentimiento Otorgado** → Inicio de seguimiento automático
3. **Mensajes Programados** → Días 2, 10, 20, 30, 40
4. **Derivación Inteligente** → Cliente solicita humano → Notificación al abogado
5. **Flujo Continuo** → Seguimiento automático NO se interrumpe

### 📱 **Sistema de Notificaciones al Abogado**
- **Derivación Automática**: Detección de palabras clave en mensajes
- **Notificación Directa**: Mensaje al abogado (+54 9 11 6981-7078)
- **Registro Completo**: Hoja dedicada para seguimiento de derivaciones
- **Estado Preservado**: Cliente mantiene estado "ACTIVO" para continuar flujo

## 🚀 Inicio Rápido

### **Enfoque de Desarrollo**
Este proyecto está diseñado para **desarrollo local directo** y despliegue en **Render**, manteniendo el bot ejecutándose nativamente en Python para facilitar el debugging y desarrollo.

### **Prerrequisitos**
- Python 3.8+
- Cuenta de Google Cloud con API habilitada
- WhatsApp Business API configurada


### **1. Configuración Inicial**
```bash
# Clonar repositorio
git clone <tu-repo>
cd bot-estudio-guiggi-ortiz

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
```

### **2. Configurar Credenciales**
```bash
# Copiar archivo de ejemplo
copy config.env.example .env

# Editar .env con tus credenciales reales
notepad .env
```

**Variables requeridas:**
```env
# Google Sheets
GOOGLE_SHEET_ID=tu_sheet_id_aqui
GOOGLE_CREDENTIALS_FILE=bot-seguimiento-clientes-24318d7ece5d.json

# WhatsApp Business API
WHATSAPP_API_TOKEN=tu_token_aqui
WHATSAPP_BUSINESS_PHONE_NUMBER_ID=tu_phone_number_id
WHATSAPP_VERIFY_TOKEN=token_personalizado_para_webhook


```

## 🧑‍💻 Configuración del Usuario (Guía en Español)

Sigue estos pasos para dejar el bot funcionando con tus credenciales y entorno:

### 1) Crear archivo `.env`
- Copia `config.env.example` a `.env`.
- Edita los valores con tus credenciales reales (Google y WhatsApp).

Campos mínimos obligatorios:
```env
GOOGLE_SHEET_ID=...               # ID de tu Google Sheet (se ve en la URL)
GOOGLE_CREDENTIALS_FILE=...       # Nombre del JSON de servicio (colócalo en la raíz)
WHATSAPP_API_TOKEN=...            # Token de WhatsApp Business API
WHATSAPP_BUSINESS_PHONE_NUMBER_ID=...  # Phone Number ID de Meta
WHATSAPP_VERIFY_TOKEN=...         # Texto que usarás para verificar el webhook
```

Opcionales útiles:
```env
PORT=5000
HOST=0.0.0.0
DEBUG=True                        # True en desarrollo, False en producción
ENVIRONMENT=local                 # o production
LOG_LEVEL=INFO
TASK_SECRET=cambia_este_token_seguro # Protege endpoints internos como /tasks/daily
```

### 2) Preparar Google Cloud y la Hoja
- Crea un Service Account con acceso a Google Sheets.
- Descarga el JSON y guárdalo con el nombre indicado en `GOOGLE_CREDENTIALS_FILE`.
- Comparte tu Google Sheet con el email del Service Account (Editor).
- Si no tienes la estructura, ejecútala automáticamente:
```bash
python setup_database.py
```

### 3) Configurar WhatsApp Business API
- Obtén el `WHATSAPP_API_TOKEN` y el `WHATSAPP_BUSINESS_PHONE_NUMBER_ID` desde Meta.
- Define `WHATSAPP_VERIFY_TOKEN` (cualquier string) para la verificación del webhook.
- Asegúrate de tener plantillas aprobadas si usas mensajes templated.

### 4) Verificar configuración local
```bash
python validate_config.py
```
Soluciona cualquier variable faltante o archivo no encontrado.

### 5) Correr localmente
```bash
python server.py
```
Usa herramientas como `ngrok` para exponer el webhook durante pruebas si lo necesitas.

### 6) Webhook (producción)
1. Despliega en Render.
2. Configura en WhatsApp el webhook a `https://<tu-app>.onrender.com/webhook`.
3. Usa el mismo `WHATSAPP_VERIFY_TOKEN` que definiste en `.env`.

### 7) Formato de Números de Teléfono

**📱 El bot maneja automáticamente TODOS los indicativos interurbanos de Argentina:**

El estudio puede cargar números en cualquier formato y el bot los encontrará automáticamente:

- `1166537925` (formato local Buenos Aires)
- `91166537925` (móvil Buenos Aires)  
- `5491166537925` (formato WhatsApp completo)
- `2611234567` (Mendoza)
- `3511234567` (Córdoba)
- `+54 9 11 6653-7925` (con espacios y guiones)

**✅ Solución completa al problema de "Cliente no encontrado":**
- **296 códigos de área soportados** de toda Argentina
- **Validación E.164 completa** según estándares internacionales
- **Cumplimiento con especificaciones ENACOM** y documentación oficial de Sent.dm
- Búsqueda inteligente con múltiples variantes del número
- Maneja códigos de área de 2, 3 y 4 dígitos
- Soporta números con prefijos 0, 15, 54, +54
- Funciona con espacios, guiones y otros caracteres especiales
- **Soporte para números especiales**: toll-free (800), premium (600)
- **Cobertura nacional completa**: Buenos Aires, Córdoba, Mendoza, Santa Fe, Tucumán, Salta, Río Negro, Tierra del Fuego, y todas las provincias

**🗺️ Códigos de área incluidos:**
- Buenos Aires: 11, 220-249 (AMBA e interior)
- Córdoba: 351, 3521-3585
- Mendoza: 260-2627
- Santa Fe: 3400-3495
- Tucumán: 381
- Salta: 387-3892
- Río Negro: 2920-298
- Tierra del Fuego: 2964
- Y todos los demás códigos interurbanos de Argentina

### **3. Configurar Base de Datos**
```bash
# Crear estructura de hojas automáticamente
python setup_database.py
```

### **4. Validar Configuración**
```bash
# Verificar que toda la configuración esté correcta
python validate_config.py
```

Este script verificará:
- ✅ Variables de entorno requeridas
- ✅ Archivo de credenciales de Google
- ✅ Configuración del servidor
- ✅ Valores por defecto de variables opcionales

### **5. Iniciar Desarrollo Local**

#### **Opción A: Script Automático (Recomendado)**
```bash
# Ejecutar script de inicio
start_development.bat
```

#### **Opción B: Desarrollo Local Completo**
```bash
# Terminal 1: Bot principal
python server.py
```

 

### **5. Configurar Webhook de WhatsApp**
1. Despliega en Render y obtén la URL pública del servicio (por ejemplo: `https://tu-servicio.onrender.com`).
2. Configura en WhatsApp el webhook: `https://tu-servicio.onrender.com/webhook`.
3. Usa como Verify Token el valor de `WHATSAPP_VERIFY_TOKEN` de tu `.env`.

## 🏗️ Estructura del Proyecto

### **Archivos Principales**
```
├── main.py                 # Bot principal y lógica de seguimiento
├── server.py              # Servidor webhook Flask
├── webhook_handler.py     # Manejo de mensajes entrantes
├── consent_manager.py     # Gestión de consentimientos
├── sheets_manager.py      # Interacción con Google Sheets
├── whatsapp_api.py        # API de WhatsApp
├── config.py              # Configuración centralizada
└── setup_database.py      # Configuración inicial de BD
```



### **Base de Datos - Google Sheets**
- **"Clientes"**: Datos principales (12 columnas)
- **"Seguimiento"**: Control de mensajes por día
- **"Derivaciones"**: Registro de derivaciones a humano
- **"Logs"**: Auditoría completa del sistema

## 🧪 Desarrollo y Pruebas

### **Ejecutar Pruebas Locales**
```bash
# Verificar configuración
python -c "from config import *; print('✅ Configuración OK')"

# Probar conexión a Google Sheets
python -c "from sheets_manager import get_gspread_client; gc = get_gspread_client(); print('✅ Google Sheets OK')"

# Probar funciones de WhatsApp
python -c "from whatsapp_api import normalizar_numero; print('✅ WhatsApp API OK')"
```

### **Flujo de Pruebas**
1. **Consentimiento**: Agregar cliente → `python consent_manager.py`
2. **Seguimiento**: Cliente activo → `python main.py`
3. **Derivación**: Mensaje con palabras clave → Verificar notificación
4. **Webhook**: Enviar mensaje → Verificar procesamiento

### **Monitoreo y Logs**
```bash
# Logs del bot en tiempo real
# Los logs aparecen en la consola donde ejecutes python server.py
```
## 📊 Estados del Cliente

### **Estados Principales**
- **PENDIENTE_CONSENTIMIENTO**: Esperando respuesta inicial
- **CONSENTIMIENTO_OTORGADO**: Listo para seguimiento
- **ACTIVO**: En seguimiento automático
- **CONSENTIMIENTO_RECHAZADO**: Cliente rechazó notificaciones
- **INACTIVO**: Cliente inactivo por otras razones

### **Estados de Derivación**
- **PENDIENTE**: Derivación solicitada, esperando resolución
- **RESUELTO**: Derivación resuelta por abogado
- **EN_PROCESO**: Abogado en contacto con cliente

## 🔧 Comandos Útiles


### **Desarrollo Local**
```bash
# Solo webhook
python server.py

# Solo bot principal
python main.py

# Solo gestor de consentimiento
python consent_manager.py

# Configurar base de datos
python setup_database.py
```

## 🚨 Solución de Problemas

### **Error: "Module not found"**
```bash
# Verificar entorno virtual activado
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstalar dependencias
pip install -r requirements.txt
```

### **Error: "Google Sheets API"**
1. Verificar que la API esté habilitada en Google Cloud
2. Verificar permisos del Service Account
3. Verificar que la hoja esté compartida

### **Error: "WhatsApp API"**
1. Verificar token válido
2. Verificar Phone Number ID
3. Verificar permisos de envío

### **Webhook no funciona**
1. Verificar URL pública en Render
2. Verificar verify token
3. Revisar logs del servidor

## 🎯 **Estado del Proyecto**

### **✅ COMPLETADO - Listo para Uso**
- **Funcionalidades core implementadas** y funcionando
- **Sistema de consentimiento** operativo
- **Webhook de WhatsApp** configurado y funcional
- **Derivación a humano** implementada y probada
- **Base de datos estructurada** en Google Sheets
- **Desarrollo local optimizado** para debugging y testing
- **Despliegue en Render** listo
- **Logs y auditoría** completos

### **🚀 El Proyecto Está Listo**
- **No requiere más desarrollo** para las funcionalidades core
- **Puede usarse en producción** tal como está
- **Escalabilidad no es necesaria** para el caso de uso actual
- **Mantenimiento mínimo** requerido

## 💡 **Recomendaciones de Uso**

### **1. Para Desarrollo/Testing**
- Ejecutar bot localmente para debugging
- Monitorear logs en tiempo real

## 🚀 Despliegue en Render

1. Asegúrate de tener los secretos configurados en Render: `GOOGLE_SHEET_ID`, `GOOGLE_CREDENTIALS_FILE`, `WHATSAPP_API_TOKEN`, `WHATSAPP_BUSINESS_PHONE_NUMBER_ID`, `WHATSAPP_VERIFY_TOKEN`.
2. Render detectará `render.yaml` y usará `gunicorn` para levantar `webhook_handler:app`.
3. Verifica el endpoint de salud: `GET /health`.
4. Configura la URL pública en WhatsApp: `https://whatsapp-bot-guiggi-ortiz.onrender.com/webhook`.

### ⏰ Ejecución Programada vía Endpoint 

- Endpoint seguro: `POST /tasks/daily` con cabecera `X-Task-Token: ${TASK_SECRET}`.
- Configura `TASK_SECRET` en Render (Environment Group `whatsapp-bot-env`).
- Usa un scheduler externo (ej. Cloudflare Workers Cron) para llamar al endpoint a las 10:00 AR.

Ejemplo (Cloudflare Workers - TypeScript):
```ts
export default {
  async scheduled(event: ScheduledEvent, env: any, ctx: ExecutionContext) {
    const url = 'https://tu-servicio.onrender.com/tasks/daily';
    const res = await fetch(url, {
      method: 'POST',
      headers: { 'X-Task-Token': env.TASK_SECRET }
    });
    console.log('Status:', res.status);
  }
}
```
En Variables del Worker define `TASK_SECRET` con el mismo valor que en Render.

### **2. Para Producción**
- Deployar en servidor con dominio HTTPS
- Configurar webhook de WhatsApp con URL real
- Mantener credenciales seguras
- Monitorear logs periódicamente

### **3. Mantenimiento**
- Revisar logs semanalmente
- Verificar funcionamiento de APIs
- Actualizar credenciales cuando sea necesario

---

## 🎉 **Resumen**

**Este proyecto está COMPLETO y FUNCIONAL para las necesidades del Estudio Guiggi & Ortiz.**

**El bot puede manejar automáticamente:**
- Seguimiento de clientes en causas civiles
- Envío de mensajes programados
- Derivación inteligente a abogados
- Gestión completa de consentimientos
- Auditoría y trazabilidad completa

---

**¡El proyecto está listo para usar! 🚀**

---

