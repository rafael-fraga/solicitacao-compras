import pandas as pd
import requests

#pylint input_file='./data/estoque.xlsx'

# rota '/estoque'
def rota_estoque(input_file):

    # importação da contagem de estoque
    estoque = pd.read_excel(input_file).T.set_index(
        0).dropna(axis=0, how='all').T
    estoque.drop(['ESTOQUE'], axis=1, inplace=True)
    estoque.columns = ['nome', 'estoque']
    estoque['estoque'] = pd.to_numeric(estoque['estoque'], errors='coerce')
    estoque.dropna(inplace=True)
    #pylint estoque

    # listagem de produtos tiny API
    produtos_id = list()

    data = {
        'formato': 'json',
        'token': '2b6fc7102240cedcc9166c43921ea73eea82b876',
        'pagina': 1
    }

    while True:
        try:
            produtos_id += [x['produto'] for x in requests.post(
                'https://api.tiny.com.br/api2/produtos.pesquisa.php', data).json()['retorno']['produtos']]
            data['pagina'] += 1
        except:
            break

    produtos_id = pd.DataFrame(produtos_id)
    produtos_id = produtos_id.T.reindex(['id', 'nome']).T
    produtos_id = estoque.merge(produtos_id)

    # requisição de dados completos do produto tiny API
    produtos_completos = [requests.post('https://api.tiny.com.br/api2/produto.obter.php', {
                                        'formato': 'json', 'token': '2b6fc7102240cedcc9166c43921ea73eea82b876', 'id': x}).json()['retorno']['produto'] for x in produtos_id['id']]
    produtos_completos = pd.DataFrame(produtos_completos).drop(['preco', 'preco_promocional', 'ncm', 'origem', 'gtin', 'gtin_embalagem', 'localizacao', 'peso_liquido', 'peso_bruto', 'estoque_maximo', 'id_fornecedor', 'codigo_fornecedor', 'codigo_pelo_fornecedor', 'unidade_por_caixa', 'preco_custo', 'preco_custo_medio', 'situacao', 'tipo', 'classe_ipi', 'valor_ipi_fixo', 'cod_lista_servicos',
                                                                'descricao_complementar', 'garantia', 'cest', 'obs', 'tipoVariacao', 'variacoes', 'idProdutoPai', 'sob_encomenda', 'dias_preparacao', 'tipoEmbalagem', 'alturaEmbalagem', 'comprimentoEmbalagem', 'larguraEmbalagem', 'diametroEmbalagem', 'categoria', 'anexos', 'imagens_externas', 'classe_produto', 'seo_title', 'seo_keywords', 'link_video', 'seo_description'], axis=1)

    # formatação final para /produtos
    produtos_formatados = produtos_completos
    produtos_formatados['unidade'] = produtos_formatados['unidade'].str.casefold()
    produtos_formatados['unidade'] = [
        'kg' if 'kg' in x else 'un' for x in produtos_formatados['unidade']]
    produtos_formatados['cotacao'] = 0
    produtos_formatados['disponivel'] = False
    produtos_formatados['quantidade'] = 0
    produtos_formatados['valorfinal'] = 0

    return produtos_formatados.to_dict(orient='records')
