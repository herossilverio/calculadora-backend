from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.calculos import calcular_resina

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.json
    resultado = calcular_resina(dados)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
