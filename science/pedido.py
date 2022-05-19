# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

def dmy(date):
  return date.strftime('%d/%m/%Y')

def rdmy(date):
  return datetime.strptime(date, '%d/%m/%Y')

"""# Leitura Pedido
Requer compras.csv e prazos.csv

Compras
"""

compras = pd.read_csv('compras.csv')
compras['preco'] = compras['preco'].str.replace(',', '').astype(float)
compras = pd.pivot_table(compras, values='preco', index='fornecedor', aggfunc='sum')

"""Prazos"""

prazos = pd.read_csv('prazos.csv')
prazos.set_index('fornecedor', drop=True, inplace=True)
prazos = prazos[np.isin(prazos.index, compras.index)]

"""Datas"""

hoje = datetime.today()
last = hoje + timedelta(prazos.max().max())
sextas = [hoje + timedelta(hoje.weekday())]
while max(sextas) < last:
  sextas.append(max(sextas) + timedelta(7))

"""Pedido"""

pedido = pd.concat([compras, prazos[np.isin(prazos.index, compras.index)]], axis=1)

for fornecedor in pedido.index:
  for i, parcela in zip(['parcela 1', 'parcela 2', 'parcela 3'], pedido.loc[fornecedor, ['parcela 1', 'parcela 2', 'parcela 3']]):
    if pd.notna(parcela):
       pedido.loc[fornecedor, [i]] = hoje + timedelta(parcela)
  pedido.loc[fornecedor, ['n parcelas']] = pedido.loc[fornecedor, ['parcela 1', 'parcela 2', 'parcela 3']].notna().sum()
pedido['valor parcela'] = pedido['preco'] / pedido['n parcelas']

"""Agenda"""

agenda = pedido.drop(['preco', 'n parcelas'], axis=1)
agenda.reset_index(drop=False, inplace=True)
agenda = pd.melt(agenda, id_vars=['fornecedor', 'valor parcela'])
agenda.dropna(inplace=True)
agenda.columns = ['fornecedor', 'valor', 'parcela', 'data']
agenda['semana'] = [x.isocalendar()[1] for x in agenda['data']]

peso = pd.pivot_table(agenda, index='semana', values='valor', aggfunc='sum')

"""#Análise de Compras
Requer API Tiny
"""

token = ''

"""Vendas"""

vendas = list()
data = {'formato': 'json',
        'token': token,
        'dataInicial': dmy(hoje - timedelta(weeks=8)),
        'pagina': 1}
while True:
  session = requests.post(url='https://api.tiny.com.br/api2/pedidos.pesquisa.php', data=data).json()
  data['pagina'] += 1
  try:
    vendas += [x['pedido'] for x in session['retorno']['pedidos']]
  except:
    break
vendas = pd.DataFrame(vendas)
vendas.drop(['id', 'numero', 'numero_ecommerce', 'data_prevista', 'nome', 'id_vendedor', 'nome_vendedor', 'situacao',
       'codigo_rastreamento', 'url_rastreamento'], axis=1, inplace=True)
vendas['semana'] = [rdmy(x).isocalendar()[1] for x in vendas['data_pedido']]

"""Faturamento"""

faturamento = pd.pivot_table(vendas, values='valor', index='semana', aggfunc='sum')
faturamento = [faturamento['valor'][:-1].mean(), faturamento['valor'].std()]

"""Contas"""

contas = list()
data = {'formato': 'json',
        'token': token,
        'data_ini vencimento': dmy(hoje),
        'data_fim_vencimento': dmy(hoje + timedelta(agenda.index.max())),
        'pagina': 1}
while True:
  session = requests.post(url='https://api.tiny.com.br/api2/contas.pagar.pesquisa.php', data=data).json()
  data['pagina'] += 1
  try:
    contas += [x['conta'] for x in session['retorno']['contas']]
  except:
    break
contas = pd.DataFrame(contas)
contas.drop(['id', 'nome_cliente', 'historico', 'numero_doc', 'situacao', 'data_emissao', 'saldo'], axis=1, inplace=True)
contas['semana'] = [rdmy(x).isocalendar()[1] for x in contas['data_vencimento']]
contas['valor'] = pd.to_numeric(contas['valor'])
contas = pd.pivot_table(contas, values='valor', aggfunc='sum', index='semana')

"""Contas"""

analise = contas + peso
analise.columns = ['despesas']
analise['faturamento'] = faturamento[0] - faturamento[1]*0.85
analise['saldo'] = analise['faturamento'] - analise['despesas']
analise.dropna(inplace=True)

"""Negadas"""

negadas = analise[analise['saldo'] < 0].reset_index()
negadas = negadas.merge(agenda)
negadas.drop(['despesas', 'faturamento', 'saldo', 'parcela', 'saldo', 'semana'], axis=1, inplace=True)
negadas['data'] = [dmy(x) for x in negadas['data']]

print(analise)
print(negadas)
