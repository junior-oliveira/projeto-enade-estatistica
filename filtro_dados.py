import pandas as pd
from configuracoes import conf

def remover_atributos(df, lista):
    resultado = df.drop(lista, axis=1, errors='ignore')
    return resultado



def renomearColunas(ano):
    '''
    ano - ano da base de dados
    '''

    # Obtém a base de dados de uma dado ano
    base_de_dados = pd.read_csv(conf.BASES_DE_DADOS[ano], delimiter=';')

    # Altera os cabeçalhos do DataFrame para maiúsculas
    base_de_dados.columns = map(str.upper, base_de_dados.columns)

    # lê o arquivo com os novos rótulos da base de dados
    df_novos_rotulos = pd.read_excel(conf.ARQUIVO_ROTULOS_A_CONSIDERAR)
    
    lista_novos_rotulos = df_novos_rotulos['NOVAS_'+ano].to_list()

    
    lista_novos_rotulos = [item for item in lista_novos_rotulos if not(pd.isnull(item)) == True]

    base_de_dados.columns = lista_novos_rotulos

    # Altera os valores da base 2017, variável PESSOA_CONCLUINTE (concluinte de 1 para 0)
    if(ano == '2017'):
       base_de_dados[conf.VAR_PESSOA_CONCLUINTE] = base_de_dados[conf.VAR_PESSOA_CONCLUINTE].replace([0,1], [1,0])

    return base_de_dados

def presenca_ok(df, lista):
    for atributo in lista:
        df = df[df[atributo] == 555]
    return df


def cursos_de_interesse(df):
    '''
    Retorna um DataFrame com as provas referentes aos cursos de interesse
    '''
    # Retorna apenas os cursos de interesse, contidos na lista LISTA_CO_GRUPO_2011
    df = df.loc[df[conf.VAR_CURSO_GRUPO]. isin(conf.LISTA_CURSO_GRUPO)]
    return df


def padronizar_interv_cat_ies(df):
    ''''
    Padroniza o intervalo IES_CATEGORIA nos valores:
        1 = Pública Federal
        2 = Pública Estadual
        3 = Pública Municipal
        4 = Privada 
        5 = Especial 
    '''
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_FEDERAL, 1)
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_ESTADUAL, 2)
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_MUNICIPAL, 3)
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_PRIVADA, 4)
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_ESPECIAL, 5)
    return df

def get_base_filtrada(ano):
    '''
    Retorna a base de dados com os dados prontos para uso
    '''
    print('processando base de dados ', ano, '...')
    # Renomeia as colunas com o formato padrão e altera o valor de concluinte da base 2017 para 0 em vez de 1
    df_base_de_dados = renomearColunas(ano)

    # Retorna apenas as provas dos estudantes com presença nos campos VAR_PRESENCA
    df_base_de_dados = presenca_ok(df_base_de_dados, conf.VAR_PRESENCA)

    # Retorna apenas os cursos de interesse (área de computação)
    df_base_de_dados = cursos_de_interesse(df_base_de_dados)
    
    # Padroniza o intervalo da categoria da IES
    df_base_de_dados = padronizar_interv_cat_ies(df_base_de_dados)

    # Retorna as provas dos estudantes concluintes
    df_base_de_dados = df_base_de_dados.loc[df_base_de_dados[conf.VAR_PESSOA_CONCLUINTE] == 0]

    # Padroniza a variável renda
    df_base_de_dados = padronizar_renda(ano, df_base_de_dados)
    
    # Retorna as variáveis de interesse
    df_base_de_dados = df_base_de_dados[conf.LISTA_VAR_INTERESSE]
    
    return df_base_de_dados

def padronizar_renda(ano, df):
    if ano == '2005':
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['C', 'D'], 'C')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('E', 'D')
    if ano == '2008':
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['C', 'D'], 'C')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('E', 'D')
    if(ano == '2011'):
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['A', 'B', 'C'], 'A')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['D', 'E', 'F'], 'B')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('G', 'C')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('H', 'D')
    if ano == '2014':
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['A', 'B'], 'A')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['C', 'D', 'E'], 'B')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('F', 'C')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('G', 'D')
    if ano == '2017':
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['A', 'B'], 'A')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace(['C', 'D', 'E'], 'B')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('F', 'C')
        df['QUESTIONARIO_SOCIO_RENDA'] = df['QUESTIONARIO_SOCIO_RENDA'].replace('G', 'D')
    return df
 
def get_base_completa():
    '''
    Retorna a base completa, concatenando todas as bases
    '''
    df_base_de_dados_2005 = get_base_filtrada('2005')
    df_base_de_dados_2008 = get_base_filtrada('2008')
    df_base_de_dados_2011 = get_base_filtrada('2011')
    df_base_de_dados_2014 = get_base_filtrada('2014')
    df_base_de_dados_2017 = get_base_filtrada('2017')

    base_completa = pd.concat([df_base_de_dados_2005, df_base_de_dados_2008, 
                            df_base_de_dados_2011, df_base_de_dados_2014, df_base_de_dados_2017],
                             ignore_index=True)

    return base_completa

def get_rotulos_base(df_base_dados):
    ''''
    Input:
        df_base_dados - dataframe que se quer pegar os cabeçalhos das colunas
    Output:
        dataframe com os rótulos das colunas
    '''
    lista_rotulos_colunas = list(df_base_dados)
    df_rotulos_colunas = pd.DataFrame(lista_rotulos_colunas)
    return df_rotulos_colunas