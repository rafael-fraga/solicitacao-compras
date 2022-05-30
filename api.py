from flask import *
import os
import science.produtos, science.analise

## temporizador de uma semana
produtos_f = json.dumps(science.produtos.post_rota_produtos())
os.system('cls')

app = Flask(__name__)

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'


# INICIALIZAÇÃO
# produtos
@app.route('/produtos', methods=['GET'])
def produtos():
    return produtos_f


# FINALIZAÇÃOs
# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
def pedido():
    resultado = science.analise.rota_pedido('./science/pedido.json')
    return json.dumps(resultado)


if __name__ == '__main__':
    app.run()