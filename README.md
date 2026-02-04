# Manduador Med - Asistente Automatizado de Medicación

Un sistema híbrido (Web + Automatización de Escritorio) diseñado para ayudar a adultos mayores a gestionar su medicación de forma segura y autónoma, reduciendo errores de dosificación y mejorando la adherencia terapéutica.

## 🎯 Propósito del Proyecto

El envejecimiento poblacional trae consigo un aumento en enfermedades crónicas que requieren polifarmacia (múltiples medicamentos). **El problema:** los pacientes olvidan dosis, las confunden o las repiten, lo que causa hospitalizaciones evitables y deterioro en la calidad de vida.

**La solución:** Manduador Med propone:
- ✅ **Interfaz Web intuitiva** para que cuidadores y médicos gestionen recetas
- ✅ **Automatización de escritorio** que alerta al paciente SIN requerir interacción tecnológica
- ✅ **Accesibilidad cognitiva** mediante alertas de voz y ventanas emergentes claras
- ✅ **Reducción de errores** actuando como una memoria externa fiable

## 👥 Actores Beneficiados

### 👴 Paciente (Adulto Mayor)
- Independencia y dignidad en la gestión de su salud
- Sin necesidad de interactuar con tecnología compleja


### 👨‍👩‍👧 Cuidadores y Familiares
- Gestión centralizada de medicamentos
- Tranquilidad mental sabiendo que el sistema alerta automáticamente
- Modificación fácil de dosis tras cambios médicos

### 👨‍⚕️ Médicos y Profesionales
- Mejora en la eficacia terapéutica garantizando que los pacientes sigan el tratamiento
- Estandarización digital de prescripciones
- Reducción de ambigüedad en la medicación

## 📁 Estructura del Proyecto

```
Proyecto H5/
├── src/                      # Backend principal (Python)
│   ├── main.py              # Punto de entrada del sistema
│   ├── automatizador.py      # Lógica de automatización de alertas
│   ├── gestor.py            # Gestión de recetas y medicamentos
│   ├── notificador.py       # Sistema de notificaciones
│   └── web/
│       ├── app.py           # Aplicación web Flask/similar
│       ├── templates/       # Templates HTML
│       └── static/          # Assets compilados
├── frontend_src/            # Frontend React + TypeScript
│   ├── src/
│   │   ├── App.jsx          # Componente principal
│   │   ├── components/      # Componentes React
│   │   │   ├── Header.tsx
│   │   │   ├── MedicationCalendar.tsx
│   │   │   ├── NewRecipeForm.tsx
│   │   │   └── AlertConfig.tsx
│   │   └── main.tsx
│   ├── vite.config.ts       # Configuración Vite
│   ├── tailwind.config.js   # Configuración Tailwind CSS
│   └── package.json
├── data/                    # Archivos de configuración
│   ├── config.json          # Configuración del sistema
│   └── recetas.json         # Base de datos de recetas
├── docs/
│   └── fundamentacion_proyecto.md
└── requirements.txt         # Dependencias Python
```

## 🛠️ Tecnologías Utilizadas

### Backend
- **Python 3.x** - Lógica principal
- **Flask** - Framework web
- **Schedule** - Programación de tareas
- **Requests** - Cliente HTTP

### Frontend
- **React 18.2** - Framework de interfaz
- **TypeScript** - Tipado estático
- **Vite** - Bundler ultrarrápido
- **Tailwind CSS** - Estilos utility-first
- **Lucide React** - Iconografía

## 🚀 Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- Node.js 16+
- npm o yarn

### Setup del Backend

```bash
# 1. Navegar al directorio del proyecto
cd "Proyecto H5"

# 2. Crear entorno virtual (si no existe)
python -m venv .venv

# 3. Activar entorno virtual
# En Windows:
.venv\Scripts\activate
# En macOS/Linux:
source .venv/bin/activate

# 4. Instalar dependencias Python
pip install -r requirements.txt
```

### Setup del Frontend

```bash
# 1. Navegar al directorio frontend
cd frontend_src

# 2. Instalar dependencias Node.js
npm install

# 3. Ejecutar servidor de desarrollo
npm run dev

# 4. Para producción
npm run build
```

## 📊 Configuración del Sistema

### `data/config.json`
Define la configuración general del sistema:
```json
{
  "app_name": "Manduador Med",
  "language": "es",
  "timezone": "America/Argentina/Buenos_Aires",
  "patient_name": "Nombre del Paciente"
}
```

### `data/recetas.json`
Almacena las recetas de medicamentos:
```json
{
  "recetas": [
    {
      "id": "receta_001",
      "nombre_medicamento": "Medicamento X",
      "miligramos": 500,
      "horarios": ["08:00", "14:00", "20:00"],
      "observaciones": "Tomar con alimentos"
    }
  ]
}
```

## 🔧 Scripts Disponibles

| Script | Descripción |
|--------|-------------|
| `launcher.py` | Inicia la aplicación |
| `main.py` | Punto de entrada del sistema |
| `automatizador.py` | Gestiona alertas automáticas |
| `gestor.py` | Administra recetas y medicamentos |
| `notificador.py` | Envía notificaciones |
| `test_*.py` | Suite de pruebas |
| `reset_recetas.py` | Reinicia la base de datos de recetas |

## 🚀 Uso

### Iniciar el Sistema
```bash
python src/main.py
```

### Acceder a la Interfaz Web
La aplicación estará disponible en:
```
http://localhost:5000
```

### Principales Funcionalidades

1. **Crear Nueva Receta** - Agregar medicamentos con horarios
2. **Configurar Alertas** - Personalizar notificaciones
3. **Ver Calendario** - Visualizar medicación programada
4. **Generar Reportes** - Tracking de dosis tomadas

## 🔔 Sistema de Notificaciones

El sistema automatiza alertas mediante:
- 🪟 **Ventanas emergentes** en escritorio
- 📱 **Notificaciones** en la interfaz web



Crear un archivo `.env` en la raíz:
```env
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_PATH=data/recetas.json
CONFIG_PATH=data/config.json
```

## 🧪 Testing

Ejecutar pruebas:
```bash
python test_full_flow.py
```

Verificar funcionalidad de eliminación:
```bash
python verify_delete_again.py
```

## 📚 Documentación Adicional

Para más detalles sobre la fundamentación y propósito del proyecto:
```bash
cat docs/fundamentacion_proyecto.md
```

## 🐛 Solución de Problemas

### El sistema no inicia
1. Verificar que todas las dependencias estén instaladas: `pip install -r requirements.txt`
2. Revisar los permisos de lectura/escritura en `data/`
3. Asegurar que no hay otra instancia ejecutándose en el puerto 5000

### Las alertas no funcionan
1. Verificar que el servicio de notificaciones está activo
2. Revisar la configuración de `data/config.json`
3. Consultar los logs en la consola

### Problemas con el frontend
1. Limpiar cache: `rm -rf node_modules && npm install`
2. Reconstruir: `npm run build`
3. Verificar versión de Node.js: `node --version`

## 📄 Licencia

Este proyecto fue desarrollado como parte de un hackathon.

## 👨‍💻 Autor

Desarrollado por el equipo de HELLO WORLD

---

**Última actualización:** Febrero 2026
