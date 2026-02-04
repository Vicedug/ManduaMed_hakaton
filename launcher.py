import subprocess
import webbrowser
import time
import requests
import sys
import os

def iniciar_servidor_web():
    """Ejecuta el servidor web Flask en subproceso."""
    print("[Launcher] Iniciando Flask...")
    return subprocess.Popen(["python", "-m", "src.web.app"], shell=True)

def iniciar_motor_automatizacion():
    """Ejecuta el scheduler en subproceso."""
    print("[Launcher] Iniciando Motor...")
    return subprocess.Popen(["python", "src/automatizador.py"], shell=True)

def esperar_inicio_servidor(url, timeout=30):
    """Espera a que el servidor web responda (status 200)."""
    print(f"[Launcher] Conectando a {url}...")
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("[Launcher] ¡Conectado!")
                return True
        except requests.ConnectionError:
            pass
        time.sleep(1)
    return False

def ejecutar_lanzador():
    """Flujo principal: Verifica, inicia procesos y abre navegador."""
    print("--- ManduadorMed Launcher ---")
    
    if not os.path.exists("src/web/app.py"):
        print("Error: Ejecutar desde la raíz del proyecto.")
        sys.exit(1)

    server_process = iniciar_servidor_web()
    automation_process = iniciar_motor_automatizacion()
    
    SERVER_URL = "http://127.0.0.1:5000"
    
    if esperar_inicio_servidor(SERVER_URL):
        print(f"[Launcher] Abriendo {SERVER_URL}")
        webbrowser.open(SERVER_URL)
    else:
        print("[Launcher] Timeout esperando servidor.")
    
    print("\n[Launcher] Running. Ctrl+C para salir.")
    
    try:
        while True:
            time.sleep(1)
            if server_process.poll() is not None:
                print("[Launcher] Flask se detuvo.")
                break
            if automation_process.poll() is not None:
                print("[Launcher] Motor se detuvo.")
                break
    except KeyboardInterrupt:
        print("\n[Launcher] Deteniendo...")
    finally:
        server_process.terminate()
        automation_process.terminate()
        print("[Launcher] Fin.")

if __name__ == "__main__":
    ejecutar_lanzador()

