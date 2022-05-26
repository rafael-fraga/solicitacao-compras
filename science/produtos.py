import pandas as pd
import requests
from time import sleep


def post_rota_produtos():

    # ## Apurar lista generalizada de produtos
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
    produtos = pd.DataFrame(produtos[:50])

    # Apurar databaset completo de produtos
    produtos_completos = list()
    for id in produtos['id']:
        data = {
            'formato': 'json',
            'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
            'id': id
        }
        try:
            produtos_completos += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.php', data=data).json()['retorno']['produto']]
        except:
            sleep(60)
            produtos_completos += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.php', data=data).json()['retorno']['produto']]
    produtos_completos = pd.DataFrame(produtos_completos)

    # Filtragem de dados
    produtos_filtrados = produtos_completos[pd.DataFrame([produtos_completos['categoria'] == x for x in ['Bovinos', 'Suínos', 'Aves', 'Especiais']]).any()]
    produtos_filtrados = produtos_filtrados[produtos_filtrados['slug'] != '']

    # Limpeza de dados
    produtos_formatados = produtos_filtrados.drop(['preco', 'marca', 'preco_promocional', 'ncm', 'origem', 'gtin', 'gtin_embalagem', 'localizacao', 'peso_liquido', 'peso_bruto', 'estoque_maximo', 'id_fornecedor', 'codigo_fornecedor', 'codigo_pelo_fornecedor', 'unidade_por_caixa', 'preco_custo', 'preco_custo_medio', 'situacao', 'tipo', 'classe_ipi', 'valor_ipi_fixo', 'cod_lista_servicos', 'descricao_complementar', 'garantia', 'cest', 'obs', 'tipoVariacao', 'variacoes', 'idProdutoPai', 'sob_encomenda', 'dias_preparacao', 'tipoEmbalagem', 'alturaEmbalagem', 'comprimentoEmbalagem', 'larguraEmbalagem', 'diametroEmbalagem', 'categoria', 'anexos', 'imagens_externas', 'classe_produto', 'seo_title', 'seo_keywords', 'link_video', 'seo_description', 'kit'], axis=1)

    # unidade
    produtos_formatados['unidade'] = produtos_formatados['unidade'].str.casefold()
    produtos_formatados['unidade'] = ['un' if x != 'kg' else 'kg' for x in produtos_formatados['unidade']]

    # POST /produtos
    produtos_estoque = produtos_formatados
    estoque = list()
    for id in produtos_estoque['id']:
        data = {
            'formato': 'json',
            'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
            'id': id
        }
        try:
            estoque += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.estoque.php', data=data).json()['retorno']['produto']['saldo']]
        except:
            sleep(60)
            estoque += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.estoque.php', data=data).json()['retorno']['produto']]
    produtos_estoque['estoque'] = estoque
    produtos_estoque.drop(['codigo', 'unidade', 'estoque_minimo', 'slug'], axis=1, inplace=True)

    # POST /produtos
    return produtos_estoque.to_dict(orient='records')


