from flask import Flask, jsonify, request, response
import os
import produtos, science.analise

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
    response = jsonify(produtos_f)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# FINALIZAÇÃOs
# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
def pedido():
    response = jsonify(request.form.to_dict())
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response, 'ok'


if __name__ == '__main__':
    app.run()