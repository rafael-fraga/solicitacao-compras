from flask import Flask, jsonify, request
import os
import science.produtos, science.analise

## temporizador de uma semana
produtos_f = science.produtos.rota_produtos()

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
    resultado = request.get_data()
    print(resultado)
    return jsonify(resultado)


if __name__ == '__main__':
    app.run()