import requests
import time
from datetime import datetime, timedelta

BASE_URL = "http://localhost:5000"

def agregar_receta_prueba(name, dosis, delay_seconds):
    # Calcular hora de inicio en el futuro cercano (para que el automatizador la capture pronto)
    start_time = (datetime.now() + timedelta(seconds=delay_seconds)).strftime("%H:%M:%S")
    
    data = {
        "nombre": name,
        "dosis": dosis,
        "hora_inicio": start_time,
        "frecuencia": "3600",
        "dias": "1", 
        "notas": "Test Auto Telegram"
    }
    print(f"Adding recipe: {name} at {start_time}")
    r = requests.post(f"{BASE_URL}/agregar", data=data)
    if r.status_code != 200:
        print(f"FAILED to add {name}: {r.status_code}")
    else:
        print(f"SUCCESS: Added {name}")

def probar_flujo_completo():
    # 1. Limpiar (borrar todo - opcional, pero mejor para test limpio)
    # Pero el usuario pidió "agregar", no necesariamente borrar. Lo dejaremos incremental.
    
    # 2. Agregar Receta 1 (Inicia en 10 segs)
    agregar_receta_prueba("TEST_MED_1", "500mg", 15)
    
    # 3. Agregar Receta 2 (Inicia en 30 segs)
    agregar_receta_prueba("TEST_MED_2", "10mg", 35)

    print("\nRecipes added via Browser API simulation.")
    print("Please check your Telegram for notifications in approx 15-40 seconds.")

if __name__ == "__main__":
    try:
        probar_flujo_completo()
    except Exception as e:
        print(f"Error: {e}")
