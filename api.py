from flask import *
import os

app = Flask(__name__)

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'





# INICIALIZAÇÃO

# estoque (grid)
@app.route('/estoque', methods=['GET'])
def estoque():
    from science.feeding import estoque
    return estoque


# produtos/fornecedores (input)
@app.route('/produtos', methods=['GET'])
def produtos():
    from science.feeding import produtos, fornecedores
    return produtos, fornecedores








# FINALIZAÇÃOs

# pedido (output do front end)
@app.route('/pedido', methods=['POST'])
def pedido():
    import science.pedidos
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