from flask import *
import os
import science.produtos, science.produtos

app = Flask(__name__)

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'


# INICIALIZAÇÃO

# estoque (grid)
@app.route('/estoque', methods=['GET'])
def estoque():
    return json.dumps(science.produtos.get_estoque())










# FINALIZAÇÃOs

# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
def pedido():
    
    science.pedidos.analise(json.loads(request.get_data()))
    return 'Análise concluída.'








## VARIÁVEIS DA ANÁLISE

# prazos
@app.route('/prazos', methods=['GET'])
def prazos():
    return open(cdir + 'prazos.json', 'r').read()


@app.route('/relatorio', methods=['POST'])
def relatorio():
    return request.get_data()


if __name__ == '__main__':
    app.run()