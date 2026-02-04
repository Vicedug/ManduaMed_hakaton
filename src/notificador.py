import tkinter as tk
from tkinter import messagebox
import threading
import requests

def mostrar_popup(titulo, mensaje):
    """
    Muestra una ventana emergente (popup) nativa del sistema.
    
    Se ejecuta en un hilo separado para evitar bloquear el flujo principal de la aplicación.
    Utiliza tkinter para generar la interfaz gráfica mínima.

    Argumentos:
        titulo (str): Título de la ventana.
        mensaje (str): Contenido del mensaje.
    """
    def _show():
        # Crear ventana oculta raíz
        root = tk.Tk()
        root.withdraw()
        # Asegurar que la ventana aparezca encima de todo
        root.attributes('-topmost', True)
        
        # Sonido de alerta nativo
        root.bell()
        
        # Mostrar mensaje
        messagebox.showinfo(titulo, mensaje)
        
        root.destroy()

    threading.Thread(target=_show).start()

def enviar_telegram(token, chat_id, mensaje):
    """
    Envía un mensaje de texto a través de la API de Telegram.

    Argumentos:
        token (str): Token del Bot de Telegram.
        chat_id (str): ID del chat o usuario destino.
        mensaje (str): Texto a enviar (soporta Markdown).
    """
    if not token or not chat_id:
        print("Aviso: Telegram no configurado (Falta Token o Chat ID).")
        return

    print(f"--- Enviando notificación a Telegram ({chat_id}) ---")
    try:
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": mensaje,
            "parse_mode": "Markdown"
        }
        # Timeout corto para no bloquear si hay problemas de red
        response = requests.post(url, data=data, timeout=10)
        
        if response.status_code == 200:
            print("Telegram enviado correctamente.")
        else:
            print(f"Fallo al enviar a Telegram: {response.text}")
    except Exception as e:
        print(f"Error de conexión con Telegram: {e}")

if __name__ == "__main__":
    print("Módulo Notificador - Pruebas")

