import sys
import os

# Add root to path to find src package
sys.path.append(os.getcwd())

import src.gestor as gestor

def reproduce():
    print("--- Reproduction Test (Direct Backend) ---")
    
    # Target: Amoxi, 1 pastilla
    nombre_target = "Amoxi"
    dosis_target = "1 pastilla" 
    
    print(f"Attempting to delete: '{nombre_target}' / '{dosis_target}'")
    
    # Check if exists first
    recetas = gestor.cargar_recetas()
    found = False
    for r in recetas:
        if r['nombre'] == nombre_target and r['dosis'] == dosis_target:
            found = True
            break
            
    if not found:
        print(f"Target '{nombre_target}' not found in DB initially. Cannot reproduce.")
        return

    print("Target found. Calling eliminar_grupo...")
    
    # Call the function
    result = gestor.eliminar_grupo(nombre_target, dosis_target)
    
    print(f"Function returned: {result}")
    
    # Verify
    recetas_after = gestor.cargar_recetas()
    for r in recetas_after:
        if r['nombre'] == nombre_target and r['dosis'] == dosis_target:
            print("FAILURE: Target still exists in DB!")
            return
             
    print("SUCCESS: Target deleted from DB.")

if __name__ == "__main__":
    reproduce()
