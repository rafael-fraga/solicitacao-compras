from pprint import pprint
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, date
import requests, os, json

def analise(pedido):

    # datetime
    def dmy(date):
        return date.strftime('%d/%m/%Y')
    def rdmy(date):
        return datetime.strptime(date, '%d/%m/%Y')
    def week(date):
        return datetime.strptime(date.split()[0], '%d/%m/%Y').isocalendar()[1]
    def rweek(week):
        return dmy(date.fromisocalendar(datetime.today().year, week, day=1)) + ' à ' + dmy(date.fromisocalendar(datetime.today().year, week, day=1) + timedelta(4-datetime.today().weekday()))
    hoje = datetime.today()


    # Compras
    compras = pedido['produtos']
    compras = pd.DataFrame([x for x in compras])
    print(compras)
    compras = pd.pivot_table(compras, values='valor', index='fornecedor', aggfunc='sum')


    # Prazos
    prazos = requests.get('http://127.0.0.1:5000/prazos').json()
    prazos = json.dumps(prazos, ensure_ascii=False).replace('Ã£', 'ã')
    prazos = json.loads(prazos)['prazos']
    prazos = pd.DataFrame([x for x in prazos])
    prazos.set_index('fornecedor', inplace=True)
    prazos = prazos[np.isin(prazos.index, compras.index)]
    prazos = prazos.replace(0, np.nan)
    prazos['n parcelas'] = [len(parcela.dropna()) for parcela in [prazos.loc[x] for x in prazos.index]]
    prazos.fillna(0, inplace=True)
    prazos = pd.DataFrame(prazos.values.astype(int), index=prazos.index, columns=prazos.columns)


    # Agenda
    agenda = prazos.join(compras)
    agenda['valor'] /= agenda['n parcelas']
    agenda = agenda.reset_index().melt(id_vars=['valor', 'fornecedor', 'n parcelas'], var_name='parcela')
    agenda.set_index('fornecedor', inplace=True)
    agenda = agenda[agenda['value'] != 0]
    agenda['data'] = [hoje + timedelta(x) for x in agenda['value']]
    agenda.drop(['n parcelas', 'value'], axis=1, inplace=True)


    # Peso
    peso = pd.pivot_table(agenda, index='data', values='valor', aggfunc='sum')


    # Token Tiny ERP
    token = '2b6fc7102240cedcc9166c43921ea73eea82b876'


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
    contas['data'] = contas['data_vencimento']
    contas.set_index('data', inplace=True)
    contas.drop(['id', 'data_vencimento', 'nome_cliente', 'historico', 'numero_doc', 'situacao', 'data_emissao', 'saldo'], axis=1, inplace=True)
    contas['valor'] = pd.to_numeric(contas['valor'])
    contas = pd.pivot_table(contas, values='valor', aggfunc='sum', index='data')


    # Análise
    analise = contas.copy()
    analise.index = [rdmy(x) for x in contas.reset_index()['data']]
    analise = pd.concat([analise, peso]).sort_index()
    analise['semana'] = [x.isocalendar()[1] for x in analise.index]
    analise = pd.pivot_table(analise.reset_index(drop=False), 'valor', 'semana')
    analise.index = [rweek(x) for x in analise.index]
    analise.columns = ['despesas']
    analise['faturamento'] = [(faturamento[0] - faturamento[1]*1.6) for x in analise.index]
    analise['saldo'] = analise['faturamento'] - analise['despesas']
    analise.index.name = 'semana'


    # Negadas
    negadas = analise[analise['saldo'] <= 0]
    negadas['intervalo'] = [[rdmy(x.split(' à ')[0]), rdmy(x.split(' à ')[1])] for x in negadas.index]
    negadas.reset_index(inplace=True)
    negadas = negadas['intervalo'].values.tolist()
    temp = list()
    for fornecedor, valor, data in zip(agenda.index, agenda['valor'], agenda['data']):
        for segunda, sexta in negadas:
            if data > segunda and data < sexta:
                temp.append([fornecedor, dmy(data), valor])
    negadas = pd.DataFrame(temp)
    negadas.set_index(0, inplace=True)
    negadas.columns = ['data', 'valor']
    negadas.index.name = 'fornecedor'


    # POST Request
    data = {
        'relatorio': {
                'analise': analise.reset_index().to_dict(orient='records'),
                'negadas': negadas.reset_index().to_dict(orient='records')
        }
    }
    requests.post('http://127.0.0.1:5000/relatorio', data=json.dumps(data)).json()


    # Retorno terminal
    os.system('cls')
    print('ANÁLISE DE COMPRAS:\n', analise.to_string())
    print('\n\nPARCELAS NEGADAS:\n', negadas.to_string())


