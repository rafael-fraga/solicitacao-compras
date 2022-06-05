from flask import Flask, jsonify, request
import os
import science.produtos, science.analise
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'


# INICIALIZAÇÃO
# produtos
@app.route('/estoque', methods=['POST'])
def produtos():
    file = request.files
    file['0'].save('./uploads/teste.csv')
    response = jsonify({'status': 'success', 'retorno': 'json'})
    # response = jsonify({'status': 'success', 'mensagem': 'coluna 3 errada', 'retorno': 'json'})
    # response = jsonify({'status': 'error', 'mensagem': 'erro em tudo'})
    # response = jsonify(science.produtos.rota_produtos())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# FINALIZAÇÃOs
# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
@cross_origin(origin='*')
def pedido():
    response = jsonify({'status': 'success', 'retorno': science.analise.rota_pedido(request.get_json())})
    # response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response


if __name__ == '__main__':
    app.run()