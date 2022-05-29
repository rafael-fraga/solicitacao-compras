import time
from flask import *
import os
import science.produtos
from datetime import date, datetime

## fiz a funcao do temporizador, agora voce precisa arrumar as linhas (15-16) e (18-19)
def checkLastUpdate():
    today = date.today()
    with open('./science/cache/lastupdate', 'r') as lastupdate:
        lines = lastupdate.readlines()
    lastSave = datetime.strptime(lines[0], "%Y-%m-%d").date()
    dif = str(today - lastSave).split()
    if int(dif[0]) < 6:
        # produtos_f recebe o json salvo
        print('leia o json salvo em cache e responde ele no get')
    else:
        # produtos_f = json.dumps(science.produtos.post_rota_produtos())
        print('salve um json novo em cache e responde ele no get')
    time.sleep(60 * 60 * 24 * 3)
    checkLastUpdate()

# produtos_f = ''
# checkLastUpdate()

## temporizador de uma semana
produtos_f = json.dumps(science.produtos.post_rota_produtos())

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
    science.pedidos.analise(json.loads(request.get_data()))
    return 'Análise concluída.'


## VARIÁVEIS DA ANÁLISE
# prazos
@app.route('/prazos', methods=['GET'])
def prazos():
    return open(cdir + 'prazos.json', 'r').read()


@app.route('/relatorio', methods=['GET'])
def relatorio():
    return request.get_data()


if __name__ == '__main__':
    app.run()