'''
Implementar logica de bucle revise a que hora se tiene que ejecutar que cosa, para development cada minuto
para poder ver los cambios, para produccion considerar distintos parametros para ahorrar recursos
'''

import time
import datetime
import gestor
import notificador

def chequear_recetas_demo():
    """
    Verifica las recetas programadas y envía alertas si coincide la hora actual.
    
    MODO DEMO:
    Revisa la coincidencia exacta de segundos para permitir pruebas rápidas.
    Si encuentra una coincidencia:
    1. Imprime en consola.
    2. Muestra popup visual.
    3. Envía notificación a Telegram.
    """
    ahora_dt = datetime.datetime.now()
    target_time_str = ahora_dt.strftime("%H:%M:%S")
    
    recetas = gestor.cargar_recetas()
    config = gestor.cargar_configuracion()
    
    for receta in recetas:
        if receta.get('hora') == target_time_str:
            mensaje = f"🚀 *DEMO ManduadorMed*: Momento de tomar *{receta['nombre']}*!"
            
            print(f"ALERTA ACTIVADA! {target_time_str} - {receta['nombre']}")
            notificador.mostrar_popup("RECORDATORIO", f"Momento de usar: {receta['nombre']}")
            
            token = config.get("telegram_token")
            chat_id = config.get("telegram_chat_id")
            notificador.enviar_telegram(token, chat_id, mensaje)

def iniciar_scheduler_demo():
    """
    Inicia el bucle principal de automatización.
    
    Revisa cada segundo si hay recetas programadas para la hora actual.
    Diseñado para ser ejecutado en un hilo o proceso separado.
    """
    print("--- MOTOR DE AUTOMATIZACIÓN INICIADO (Modo Demo) ---")
    last_second = ""
    
    while True:
        ahora = datetime.datetime.now()
        current_second = ahora.strftime("%H:%M:%S")
        
        if current_second != last_second:
            chequear_recetas_demo()
            last_second = current_second
        
        # Pausa breve para evitar alto consumo de CPU, pero suficiente para no perder segundos
        time.sleep(0.5)

if __name__ == "__main__":
    iniciar_scheduler_demo()