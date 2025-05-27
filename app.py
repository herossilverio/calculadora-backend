from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.calculos import calcular_resina

app = Flask(__name__)
CORS(app)  # Permite conexões externas (como do frontend no Vercel)

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()  # Pega o corpo da requisição JSON
    resultado = calcular_resina(dados)
    return jsonify(resultado)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render define essa variável automaticamente
    app.run(host='0.0.0.0', port=port)
