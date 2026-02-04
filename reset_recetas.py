import json
import datetime
import os

# Define paths
BASE_DIR = r"c:\Users\viced\Desktop\Proyecto H5"
DATA_FILE = os.path.join(BASE_DIR, 'data', 'recetas.json')

def reiniciar_y_generar_recetas():
    print("Resetting recipes...")
    
    # Calculate times
    now = datetime.datetime.now()
    time1 = now + datetime.timedelta(seconds=20)
    time2 = now + datetime.timedelta(seconds=50)

    # Create new recipes
    new_recipes = [
        {
            "id": 1,
            "nombre": "Prueba Demo 1",
            "dosis": "1 prueba",
            "hora": time1.strftime("%H:%M:%S"),
            "fecha": time1.strftime("%d-%m-%Y"),
            "timestamp": time1.strftime("%Y-%m-%d %H:%M:%S"),
            "notas": "Esta es la primera prueba generada automáticamente."
        },
        {
            "id": 2,
            "nombre": "Prueba Demo 2",
            "dosis": "1 prueba",
            "hora": time2.strftime("%H:%M:%S"),
            "fecha": time2.strftime("%d-%m-%Y"),
            "timestamp": time2.strftime("%Y-%m-%d %H:%M:%S"),
            "notas": "Esta es la segunda prueba generada automáticamente."
        }
    ]

    # Write to file
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(new_recipes, f, indent=4, ensure_ascii=False)
    
    print(f"Generated 2 recipes:")
    print(f"1. {new_recipes[0]['nombre']} at {new_recipes[0]['hora']}")
    print(f"2. {new_recipes[1]['nombre']} at {new_recipes[1]['hora']}")

if __name__ == "__main__":
    reiniciar_y_generar_recetas()
