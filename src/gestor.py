import json
import os

# Ruta al archivo de datos (basado en nuestra arquitectura)
DATA_PATH = os.path.join("data", "recetas.json")

def inicializar_base_datos():
    """Crea el archivo JSON si no existe."""
    if not os.path.exists("data"):
        os.makedirs("data")
    
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)
        print("Base de datos creada exitosamente.")

def guardar_medicamento(nombre, hora, dosis):
    """Guarda una nueva programación de medicina."""
    inicializar_base_datos()
    
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        datos = json.load(f)
    
    nueva_receta = {
        "id": len(datos) + 1,
        "nombre": nombre,
        "hora": hora, # Formato "HH:MM"
        "dosis": dosis,
        "estado": "pendiente"
    }
    
    datos.append(nueva_receta)
    
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4)
    
    return True

def obtener_recetas():
    """Lee todas las recetas guardadas."""
    inicializar_base_datos()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_por_hora(hora_actual):
    """Busca medicamentos programados para una hora específica."""
    recetas = obtener_recetas()
    # Retorna una lista de medicinas que coinciden con la hora
    return [r for r in recetas if r["hora"] == hora_actual]