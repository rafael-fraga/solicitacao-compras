from flask import *
import json, time, os

app = Flask(__name__)

data_dir = os.path.dirname(os.getcwd()) + '\\data\\'

@app.route('/products', methods=['GET'])
def index():

    f = open(data_dir + 'produtos.json', 'r')
    produtos_json = f.read()

    return json.dumps(produtos_json)

if __name__ == '__main__':
    app.run()



