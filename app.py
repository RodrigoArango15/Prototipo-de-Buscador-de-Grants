# app.py
from flask import Flask, render_template, request, jsonify
from data import get_all_grants, toggle_save_grant

app = Flask(__name__)

@app.route('/')
def index():
    """Ruta principal que sirve la interfaz web (HTML)."""
    return render_template('index.html')

@app.route('/api/grants', methods=['GET'])
def api_grants():
    """API para obtener los grants, con soporte para filtrado."""
    grants = get_all_grants()
    
    # Obtener parámetros de búsqueda (query params)
    keyword = request.args.get('keyword', '').lower()
    region = request.args.get('region', '')
    g_type = request.args.get('type', '')
    status = request.args.get('status', '') # ej. 'saved' (guardados)
    
    filtered_grants = []
    
    for g in grants:
        match = True
        
        # Filtro por palabra clave en título o descripción
        if keyword and keyword not in g['title'].lower() and keyword not in g['description'].lower():
            match = False
            
        # Filtro por región
        if region and region != 'Todas' and region != g['region']:
            match = False
            
        # Filtro por tipo
        if g_type and g_type != 'Todos' and g_type != g['type']:
            match = False
            
        # Filtro por estado de guardado
        if status == 'saved' and not g['saved']:
            match = False

        if match:
            filtered_grants.append(g)
            
    return jsonify(filtered_grants)

@app.route('/api/grants/<int:grant_id>/toggle_save', methods=['POST'])
def api_toggle_save(grant_id):
    """API para guardar o desguardar un grant."""
    grant = toggle_save_grant(grant_id)
    if grant:
        return jsonify({"success": True, "saved": grant["saved"]})
    return jsonify({"success": False, "error": "Grant no encontrado"}), 404

if __name__ == '__main__':
    # Inicia el servidor en modo debug en el puerto 5000
    print("Iniciando Sistema de Buscador de Grants de LACCEI...")
    app.run(debug=True, port=5000)
