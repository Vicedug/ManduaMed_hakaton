import requests
import sys

BASE_URL = "http://localhost:5000"

def verificar_eliminacion():
    print("--- Verifying Delete Functionality ---")
    
    # 1. Create a dummy recipe
    print("[1] Creating test recipe 'RECETA_TEST'...")
    data = {
        "nombre": "RECETA_TEST",
        "dosis": "500mg",
        "hora_inicio": "12:00",
        "frecuencia": "24",
        "dias": "1",
        "notas": "To be deleted"
    }
    try:
        r = requests.post(f"{BASE_URL}/agregar", data=data)
        if r.status_code != 200:
            print(f"Error creating recipe: {r.status_code}")
            return False
    except Exception as e:
        print(f"Server not reachable: {e}")
        return False

    # 2. Check it exists
    r = requests.get(BASE_URL)
    if "RECETA_TEST" not in r.text:
        print("Error: Recipe was not created.")
        return False
    print("[2] Recipe created successfully.")

    # 3. Try to delete it using the EXACT URL format the button uses
    # /eliminar_grupo?nombre=RECETA_TEST&dosis=500mg
    print("[3] Attempting deletion via URL...")
    params = {"nombre": "RECETA_TEST", "dosis": "500mg"}
    r = requests.get(f"{BASE_URL}/eliminar_grupo", params=params)
    
    # 4. Check if it's gone
    r = requests.get(BASE_URL)
    if "RECETA_TEST" in r.text:
        print("Error: Recipe STILL EXISTS after deletion!")
        return False
    
    print("[4] Recipe deleted successfully via backend.")
    return True

if __name__ == "__main__":
    if verificar_eliminacion():
        print("Backend logic is verified.")
        sys.exit(0)
    else:
        print("Backend verification FAILED.")
        sys.exit(1)
