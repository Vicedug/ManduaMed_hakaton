import json
import os
from datetime import datetime, timedelta

# Configuración de archivos
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'recetas.json')
CONFIG_FILE = os.path.join(BASE_DIR, 'data', 'config.json')

def cargar_recetas():
    """Lee el archivo JSON de recetas."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def guardar_recetas(recetas):
    """Guarda la lista de recetas en el JSON."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(recetas, f, indent=4, ensure_ascii=False)

def cargar_configuracion():
    """Lee la configuración del sistema."""
    if not os.path.exists(CONFIG_FILE):
        return {"telegram_token": "", "telegram_chat_id": ""}
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def guardar_configuracion(nuevos_datos):
    """Actualiza la configuración en el JSON."""
    config_actual = cargar_configuracion()
    config_actual.update(nuevos_datos)
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(config_actual, f, indent=4, ensure_ascii=False)

def generar_dosis(nombre, dosis, hora_inicio, frecuencia_horas, dias, notas=""):
    """
    Genera y guarda tomas de medicamentos.
    Nota: frecuencia_horas = segundos, dias = minutos (para demo).
    """
    recetas = cargar_recetas()
    nuevo_id = 1 if not recetas else max(r['id'] for r in recetas) + 1
    
    fecha_base = datetime.now().date()
    
    if len(hora_inicio) == 5:
        hora_inicio += ":00"
    
    try:
        hora_obj = datetime.strptime(hora_inicio, "%H:%M:%S").time()
    except ValueError:
        hora_obj = datetime.now().time()

    dt_actual = datetime.combine(fecha_base, hora_obj)
    limite = dt_actual + timedelta(minutes=int(dias))
    nuevas_recetas = []
    
    while dt_actual < limite:
        receta = {
            "id": nuevo_id,
            "nombre": nombre,
            "dosis": dosis,
            "hora": dt_actual.strftime("%H:%M:%S"),
            "fecha": dt_actual.strftime("%d-%m-%Y"),
            "timestamp": dt_actual.strftime("%Y-%m-%d %H:%M:%S"), 
            "notas": notas
        }
        recetas.append(receta)
        nuevas_recetas.append(receta)
        nuevo_id += 1
        dt_actual += timedelta(seconds=int(frecuencia_horas))
    
    recetas.sort(key=lambda x: x.get('timestamp', ''))
    guardar_recetas(recetas)
    return len(nuevas_recetas)

def eliminar_receta(id_receta):
    """Elimina una receta por ID."""
    recetas = cargar_recetas()
    recetas_filtradas = [r for r in recetas if r['id'] != int(id_receta)]
    if len(recetas) != len(recetas_filtradas):
        guardar_recetas(recetas_filtradas)
        return True
    return False

def eliminar_grupo(nombre, dosis):
    """Elimina todas las recetas de un grupo específico."""
    recetas = cargar_recetas()
    
    target_nombre = nombre.strip().lower() if nombre else ""
    target_dosis = dosis.strip().lower() if dosis else ""

    recetas_filtradas = [
        r for r in recetas 
        if not (r.get('nombre', '').strip().lower() == target_nombre and 
                r.get('dosis', '').strip().lower() == target_dosis)
    ]
    
    if len(recetas) != len(recetas_filtradas):
        guardar_recetas(recetas_filtradas)
        return True
    return False

if __name__ == "__main__":
    print("Gestor de Recetas - Prueba")
    print(f"Recetas cargadas: {len(cargar_recetas())}")
