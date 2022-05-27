import pandas as pd
import requests
from time import sleep


def post_rota_produtos():

    print('Importando produtos.')

    ### removido para a versão debug ###
    '''    # ## Apurar lista generalizada de produtos
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
    produtos = pd.DataFrame(produtos[:50])'''


    # variável temporária (remover antes do deploy)
    ids = ['623449734', '623449795', '623449782', '778208483', '646749750', '729652533', '638403161', '623449824', '623449837', '661843960', '649329262', '733149637', '659216777', '623449886', '623449902', '692081848', '623449926', '706381781', '623449932', '623449946', '794828451', '773934587', '770209199', '778208038', '791977192', '663063892', '623449970', '744114547', '767806291', '799895288', '664322273', '638432052', '623449997', '789712012', '623450013', '649329268', '785293008', '623450189', '623450199', '800868965', '623450046', '623450182', '623450205', '623450210', '623450220', '682500784', '623450215', '804981063', '794827835', '653960156', '634824164', '623450225', '623450236', '628882233', '804677691', '786903341', '638379143', '623450327', '766299129', '623450340', '630551037', '623450354', '737002822', '774269426', '623450374', '733415440', '637005194', '795400098', '777807737', '626302922', '723855204', '623450496', '794829708', '801868011', '768983512', '623450527', '797788298', '778208806', '623450540', '643787433', '769851535', '623450553', '777808809', '623450568', '687343884', '687345363', '623450585', '687338443', '647280665', '623450611', '623450624', '623450740', '623450753', '640758281', '623450765', '626670053', '692082492', '623585662', '638867885', '640758272', '623450791', '647280670', '769175229']

    # Apurar databaset completo de produtos
    produtos_completos = list()
    for id in ids:                                                   ## será removido antes do deploy
        data = {
            'formato': 'json',
            'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
            'id': id
        }
        try:
            produtos_completos += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.php', data=data).json()['retorno']['produto']]
        except:
            print('limite de requisições atingido.')
            sleep(60)
            print('Continuando.')
            produtos_completos += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.php', data=data).json()['retorno']['produto']]
    produtos_completos = pd.DataFrame(produtos_completos)

    # Filtragem de dados
    produtos_filtrados = produtos_completos[pd.DataFrame([produtos_completos['categoria'] == x for x in ['Bovinos', 'Suínos', 'Aves', 'Especiais']]).any()]
    produtos_filtrados = produtos_filtrados[produtos_filtrados['slug'] != '']

    # Limpeza de dados
    produtos_formatados = produtos_filtrados.drop(['preco', 'marca', 'preco_promocional', 'ncm', 'origem', 'gtin', 'gtin_embalagem', 'localizacao', 'peso_liquido', 'peso_bruto', 'estoque_maximo', 'id_fornecedor', 'codigo_fornecedor', 'codigo_pelo_fornecedor', 'unidade_por_caixa', 'preco_custo', 'preco_custo_medio', 'situacao', 'tipo', 'classe_ipi', 'valor_ipi_fixo', 'cod_lista_servicos', 'descricao_complementar', 'garantia', 'cest', 'obs', 'tipoVariacao', 'variacoes', 'idProdutoPai', 'sob_encomenda', 'dias_preparacao', 'tipoEmbalagem', 'alturaEmbalagem', 'comprimentoEmbalagem', 'larguraEmbalagem', 'diametroEmbalagem', 'categoria', 'anexos', 'imagens_externas', 'classe_produto', 'seo_title', 'seo_keywords', 'link_video', 'seo_description'], axis=1)
    produtos_formatados['unidade'] = produtos_formatados['unidade'].str.casefold()
    produtos_formatados['unidade'] = ['un' if x != 'kg' else 'kg' for x in produtos_formatados['unidade']]

    print('Importando estoque individual')

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
            print('limite de requisições atingido.')
            sleep(60)
            print('Continuando.')
            estoque += [requests.post(url='https://api.tiny.com.br/api2/produto.obter.estoque.php', data=data).json()['retorno']['produto']]
    produtos_estoque['estoque'] = estoque
    
    # POST /produtos
    return produtos_estoque.to_dict(orient='records')


