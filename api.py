from flask import *
import os

app = Flask(__name__)

cdir = os.getcwd() + '\\data\\'

@app.route('/', methods=['GET'])
def index():
    return 'index'

@app.route('/pedido', methods=['GET'])
def pedido():
    return open(cdir + 'pedido.json', 'r').read()

@app.route('/prazos', methods=['GET'])
def prazos():
    return open(cdir + 'prazos.json', 'r').read()

@app.route('/relatorio', methods=['POST'])
def relatorio():
    relatorio = request.data
    return relatorio

app.run()