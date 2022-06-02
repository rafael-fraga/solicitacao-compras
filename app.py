from flask import Flask, jsonify, request
import os
import produtos, science.analise
from flask_cors import CORS, cross_origin
## temporizador de uma semana
produtos_f = produtos.produtos_static

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://brazas-simulador-compras.herokuapp.com/"}})

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'


# INICIALIZAÇÃO
# produtos
@app.route('/produtos', methods=['GET'])
def produtos():
    response = jsonify(produtos_f)
    response.headers.add("Access-Control-Allow-Origin", "http://brazas-simulador-compras.herokuapp.com/")
    return response


# FINALIZAÇÃOs
# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
@cross_origin(origin='*')
def pedido():
    response = jsonify({'status': 'success', 'retorno': science.analise.rota_pedido(request.get_json())})
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


if __name__ == '__main__':
    app.run()