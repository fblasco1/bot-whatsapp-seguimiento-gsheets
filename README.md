# 🤖 Bot WhatsApp - Seguimiento Automático de Clientes

**Desarrollado para Estudio Guiggi & Ortiz** 🏛️

Bot automatizado de WhatsApp para realizar seguimiento de clientes en causas civiles (accidentes de tránsito), enviando mensajes programados en una ventana de 60 días previa a audiencia.

## 🎯 Funcionalidades Core Implementadas

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
4. Configura la URL pública en WhatsApp: `https://tu-servicio.onrender.com/webhook`.

### ⏰ Tarea Programada (Cron) en Render

- Se incluye un cron job en `render.yaml` que ejecuta el ciclo del bot todos los días a las **10:00 AM (Argentina, UTC-3)**.
- Render programa tareas en **UTC**, por eso el cron está configurado a `0 13 * * *` (13:00 UTC = 10:00 AR).
- El comando ejecutado es: `python -u main.py`.

Si deseas cambiar el horario, ajusta la línea en `render.yaml`:

```
cronJobs:
  - name: whatsapp-bot-daily-10am-ar
    schedule: "0 13 * * *"  # 10:00 AM Argentina (UTC-3)
    startCommand: python -u main.py
```

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

- ✅ **Todas las funcionalidades core implementadas**
- ✅ **Sistema probado y funcionando**
- ✅ **Listo para uso en producción**
- ✅ **No requiere más desarrollo**

**El bot puede manejar automáticamente:**
- Seguimiento de clientes en causas civiles
- Envío de mensajes programados
- Derivación inteligente a abogados
- Gestión completa de consentimientos
- Auditoría y trazabilidad completa

---

**¡El proyecto está listo para usar! 🚀**

