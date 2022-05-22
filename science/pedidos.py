import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import requests, os, json

 
def dmy(date):
  return date.strftime('%d/%m/%Y')

def rdmy(date):
  return datetime.strptime(date, '%d/%m/%Y')

def week(date):
  return datetime.strptime(date.split()[0], '%d/%m/%Y').isocalendar()[1]

def rweek(week):
  return dmy(date.fromisocalendar(datetime.today().year, week, day=1)) + ' à ' + dmy(datetime.today() + timedelta(4-datetime.today().weekday()))

 
dir = os.getcwd()

hoje = datetime.today()

   
# # Leitura Pedido

   
# Compras

 
compras = pd.DataFrame(requests.get('http://127.0.0.1:5000/pedido').json()).T
compras['preco'] = pd.to_numeric(compras['preco'].str.replace(',', ''))
compras = pd.pivot_table(compras, values='preco', index='fornecedor', aggfunc='sum')

   
# Prazos

 
prazos = pd.DataFrame(requests.get('http://127.0.0.1:5000/prazos').json()).T
prazos.index.name = 'fornecedor'
prazos = prazos[np.isin(prazos.index, compras.index)]
prazos = prazos.replace(0, np.nan)

   
# Pedido

 
pedido = pd.concat([compras, prazos[np.isin(prazos.index, compras.index)]], axis=1)
for fornecedor in pedido.index:
  for i, parcela in zip(['parcela 1', 'parcela 2', 'parcela 3'], pedido.loc[fornecedor, ['parcela 1', 'parcela 2', 'parcela 3']]):
    if pd.notna(parcela):
      pedido.loc[fornecedor, [i]] = hoje + timedelta(parcela)
      pedido.loc[fornecedor, ['n parcelas']] = pedido.loc[fornecedor, ['parcela 1', 'parcela 2', 'parcela 3']].notna().sum()

pedido['valor parcela'] = pedido['preco'] / pedido['n parcelas']

   
# Agenda

 
agenda = pd.melt(pedido, id_vars=['valor parcela', 'preco'], value_vars=['parcela 1', 'parcela 2', 'parcela 3'], ignore_index=False, var_name='parcela', value_name='data')
agenda.dropna(inplace=True)
agenda.reset_index(inplace=True)
agenda['semana'] = [x.isocalendar()[1] for x in agenda['data']]
agenda.sort_values('data', inplace=True)
agenda.set_index('fornecedor', inplace=True)

 
peso = pd.pivot_table(agenda, index='semana', values='valor parcela', aggfunc='sum')
peso.columns = ['valor']

   
# # Análise de Compras
# Requer API Tiny
# 
# 

 
token = str(input('token: '))

   
# Vendas

 
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

   
# Faturamento

 
faturamento = pd.pivot_table(vendas, values='valor', index='semana', aggfunc='sum')
faturamento = [faturamento['valor'][:-1].mean(), faturamento['valor'].std()]

   
# Contas

 

contas = list()
data = {'formato': 'json',
        'token': token,
        'data_ini vencimento': dmy(hoje),
        'data_fim_vencimento': dmy(agenda['data'].max()),
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

   
# Análise

 
analise = contas + peso
analise.columns = ['despesas']
analise['faturamento'] = faturamento[0] - faturamento[1]*0.85
analise['saldo'] = analise['faturamento'] - analise['despesas']
analise.dropna(inplace=True)
analise.index = [rweek(x) for x in analise.index]

   
# Negadas

 
negadas = analise[analise['saldo'] < 0]
negadas.index = [week(x) for x in negadas.index]
negadas.reset_index(inplace=True)
negadas.columns = ['semana', 'despesas', 'faturamento', 'saldo']
negadas = negadas.merge(agenda.reset_index())
negadas.set_index('fornecedor', inplace=True)
negadas.drop(['despesas', 'faturamento', 'saldo', 'parcela', 'semana'], axis=1, inplace=True)
negadas.sort_values('data', inplace=True)
negadas['data'] = [dmy(x) for x in negadas['data']]

   
# # Output

   
# Formatação do parâmetro de POST

 
data = {'analise': analise.to_dict(orient='index'),
        'negadas': negadas.to_dict(orient='index')
}
data = json.dumps(data)

 
print(requests.post('http://127.0.0.1:5000/relatorio', data=data).json())

