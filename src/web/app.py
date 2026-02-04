from flask import Flask, render_template, request, redirect, url_for, jsonify
from .. import gestor
import os

app = Flask(__name__)

@app.after_request
def agregar_encabezados_sin_cache(response):
    """Evita el caché del navegador."""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def pagina_inicio():
    """Sirve la aplicación React principal."""
    return render_template('index.html')

@app.route('/api/recetas', methods=['GET'])
def api_get_recetas():
    """Retorna todas las recetas agrupadas por ID."""
    recetas_flat = gestor.cargar_recetas()
    recetas_agrupadas = {}
    
    for r in recetas_flat:
        nombre = r['nombre']
        dosis = r['dosis']
        clave = f"{nombre}|||{dosis}"
        
        if clave not in recetas_agrupadas:
            recetas_agrupadas[clave] = {
                "id": clave,
                "name": nombre,
                "dose": dosis,
                "pending": 0,
                "timestamp": r.get('timestamp', ''),
                "doses": []
            }
        recetas_agrupadas[clave]["pending"] += 1
        recetas_agrupadas[clave]["doses"].append(r)

    lista = sorted(recetas_agrupadas.values(), key=lambda x: x['timestamp'])
    return jsonify(lista)

@app.route('/api/recetas', methods=['POST'])
def api_add_receta():
    """Genera nuevas recetas basadas en los datos recibidos."""
    data = request.json
    gestor.generar_dosis(
        data.get('name'),
        data.get('dose'),
        data.get('startTime'),
        data.get('frequency'),
        data.get('duration'),
        data.get('notes')
    )
    return jsonify({"status": "success"})

@app.route('/api/recetas/<path:id>', methods=['DELETE'])
def api_delete_receta(id):
    """Elimina un grupo de recetas por su ID."""
    try:
        nombre, dosis = id.split('|||')
        gestor.eliminar_grupo(nombre, dosis)
        return jsonify({"status": "success"})
    except ValueError:
         return jsonify({"status": "error", "message": "Formato de ID inválido"}), 400

@app.route('/configurar', methods=['POST'])
def configurar():
    """Guarda la configuración de Telegram."""
    gestor.guardar_configuracion({
        "telegram_token": request.form.get('telegram_token'),
        "telegram_chat_id": request.form.get('telegram_chat_id')
    })
    return redirect(url_for('pagina_inicio'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

