from flask import Flask, jsonify, request
import os
import science.produtos, science.analise
import produtos

## temporizador de uma semana
produtos_f = produtos.produtos_static

app = Flask(__name__)

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'


# INICIALIZAÇÃO
# produtos
@app.route('/produtos', methods=['GET'])
def produtos():
    return jsonify(produtos_f)


# FINALIZAÇÃOs
# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
def pedido():
    resultado = science.analise.rota_pedido(request.get_data())
    return jsonify(resultado)


if __name__ == '__main__':
    app.run()