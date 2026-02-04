import json
import os
import requests

# Config path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, 'data', 'config.json')

def enviar_test_telegram():
    print("--- INICIANDO TEST DE TELEGRAM ---")
    
    # 1. Cargar Config
    if not os.path.exists(CONFIG_FILE):
        print("ERROR: No existe config.json")
        return

    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)
    
    token = config.get("telegram_token")
    chat_id = config.get("telegram_chat_id")
    
    print(f"Token: {token[:5]}... (oculto)")
    print(f"Chat ID: {chat_id}")
    
    if not token or not chat_id:
        print("ERROR: Faltan credenciales de Telegram.")
        return

    mensaje = "🤖 *Prueba de Telegram* \n✅ Si lees esto, ManduadorMed está conectado correctamente."

    print("Enviando mensaje HTTP...")
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": mensaje,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=data)
        
        if response.status_code == 200:
            print("✅ ¡ÉXITO! Mensaje enviado correctamente.")
            print("Revisa tu chat de Telegram.")
        else:
            print(f"❌ FALLO: {response.text}")
            
    except Exception as e:
        print(f"❌ ERROR DE CONEXIÓN: {e}")

if __name__ == "__main__":
    enviar_test_telegram()
