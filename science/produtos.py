import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import requests, os, json
from time import sleep

def get_estoque():
  # fazer requisição dos ids de produtos
  produtos = list()
  data = {'formato': 'json',
          'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
          'pesquisa': '',
          'pagina': 1}
  while True:
    session = requests.post(url='https://api.tiny.com.br/api2/produtos.pesquisa.php', data=data).json()
    data['pagina'] += 1
    try:
      produtos += [x['produto'] for x in session['retorno']['produtos']]
    except:
      break
  produtos = pd.DataFrame(produtos)
  produtos['estoque'] = ''
  produtos.set_index('id', inplace=True)
  produtos.drop(['codigo', 'preco', 'preco_promocional', 'gtin', 'tipoVariacao', 'localizacao', 'preco_custo', 'preco_custo_medio', 'situacao'], axis=1, inplace=True)

  # obter estoque para cada produto
  for id in produtos.index:
      data = {
          'formato': 'json',
          'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
          'id': id
      }
      session = requests.post('https://api.tiny.com.br/api2/produto.obter.estoque.php', data=data).json()['retorno']
      try:
          produtos['estoque'].loc[id] = session['produto']['saldo']
      except:
          break
  return produtos.to_dict(orient='records')