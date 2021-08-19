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
    base_de_dados = pd.read_csv(conf.BASES_DE_DADOS[ano], low_memory=False, delimiter=';')

    # Altera os cabeçalhos do DataFrame para maiúsculas
    base_de_dados.columns = map(str.upper, base_de_dados.columns)

    # lê o arquivo com os novos rótulos da base de dados
    df_novos_rotulos = pd.read_excel(conf.ARQUIVO_ROTULOS_A_CONSIDERAR)

    lista_novos_rotulos = df_novos_rotulos['NOVAS_' + ano].to_list()

    lista_novos_rotulos = [item for item in lista_novos_rotulos if not (pd.isnull(item)) == True]

    base_de_dados.columns = lista_novos_rotulos

    # Altera os valores da base 2017, variável PESSOA_CONCLUINTE (concluinte de 1 para 0)
    if (ano == '2017'):
        base_de_dados[conf.VAR_PESSOA_CONCLUINTE] = base_de_dados[conf.VAR_PESSOA_CONCLUINTE].replace([0, 1], [1, 0])

    return base_de_dados


def presenca_ok(df, lista):
    for atributo in lista:
        df = df[df[atributo] == 555]
    return df


def cursos_de_interesse(df, ano):
    '''
    Retorna um DataFrame com as provas referentes aos cursos de interesse
    '''
    df = df.loc[df[conf.VAR_CURSO_GRUPO].isin(conf.LISTA_CURSO_GRUPO)]
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
    # tipo especial marcado como privada, por não ser predominantemente pública
    df[conf.VAR_IES_CATEGORIA] = df[conf.VAR_IES_CATEGORIA].replace(conf.LISTA_CATEGORIA_ESPECIAL, 4)
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
    df_base_de_dados = cursos_de_interesse(df_base_de_dados, ano)

    # Padroniza o intervalo da categoria da IES
    df_base_de_dados = padronizar_interv_cat_ies(df_base_de_dados)

    # Retorna as provas dos estudantes concluintes
    df_base_de_dados = df_base_de_dados.loc[df_base_de_dados[conf.VAR_PESSOA_CONCLUINTE] == 0]

    # Padroniza a variável renda
    df_base_de_dados = padronizar_renda(ano, df_base_de_dados)

    # Padroniza a variável SITUACAO_TRABALHO
    df_base_de_dados = padronizar_sit_trabalho(ano, df_base_de_dados)

    # Padroniza a variável ENSINO_MEDIO
    df_base_de_dados = padronizar_ens_medio(ano, df_base_de_dados)

    # Padroniza a variável TIPO_EM
    df_base_de_dados = padronizar_tipo_ens_medio(ano, df_base_de_dados)

    # Padroniza a variável HORAS_ESTUDO
    df_base_de_dados = padronizar_horas_estudo(ano, df_base_de_dados)

    # Retorna as variáveis de interesse
    df_base_de_dados = df_base_de_dados[conf.LISTA_VAR_INTERESSE]

    df_base_de_dados = padronizar_sexo(df_base_de_dados)

    df_base_de_dados = padronizar_notas(df_base_de_dados)

    return df_base_de_dados


def padronizar_notas(df):
    colunas_a_tratar = ['PROVA_FG_OBJETIVAS_NOTABRUTA', 'PROVA_FG_DISCURSIVAS_NOTABRUTA',
                        'PROVA_FG_NOTABRUTA', 'PROVA_FE_OBJETIVAS_NOTABRUTA', 'PROVA_FE_DISCURSIVAS_NOTABRUTA',
                        'PROVA_FE_NOTABRUTA', 'PROVA_NOTABRUTA']

    notas_strings = 0
    notas_not_float = 0
    for index, row in df.iterrows():
        for coluna in colunas_a_tratar:
            if type(row[coluna]) is str:
                v = float(row[coluna].replace(',', '.'))
                df.loc[index, coluna] = v
                notas_strings += 1
            elif type(row[coluna]) is not float:
                v = float(row[coluna])
                df.loc[index, coluna] = v
                notas_not_float += 1
    if notas_strings != 0 or notas_not_float != 0:
        print('--> notas_strings: ', notas_strings)
        print('--> notas_not_float: ', notas_not_float)
    return df


def padronizar_renda(ano, df):
    if ano == '2005':
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['C', 'D'], 'C')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('E', 'D')
    if ano == '2008':
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['C', 'D'], 'C')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('E', 'D')
    if (ano == '2011'):
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['A', 'B', 'C'], 'A')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['D', 'E', 'F'], 'B')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('G', 'C')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('H', 'D')
    if ano == '2014':
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['A', 'B'], 'A')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['C', 'D', 'E'], 'B')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('F', 'C')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('G', 'D')
    if ano == '2017':
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['A', 'B'], 'A')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace(['C', 'D', 'E'], 'B')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('F', 'C')
        df[conf.VAR_RENDA] = df[conf.VAR_RENDA].replace('G', 'D')
    return df


def padronizar_sexo(df):
    # 2005, 2008: 1 = Masculino 2 = Feminino
    # 2011, 2014: M = Masculino, F = Feminino, N = Não Informado
    # 2017: M = Masculino, F = Feminino

    # padronização: 1 = Masculino 2 = Feminino, 3 = NI
    df['PESSOA_SEXO'] = df['PESSOA_SEXO'].replace(['M', '1'], 1)
    df['PESSOA_SEXO'] = df['PESSOA_SEXO'].replace(['F', '2'], 2)
    df['PESSOA_SEXO'] = df['PESSOA_SEXO'].replace('N', 3)
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

def padronizar_sit_trabalho(ano, df):
    ''''
        Padroniza a variável SITUACAO_TRABALHO considerando se a pessoa tem algum tipo de renda, seja originária 
        de trabalho ou outra fonte.
        Intervalo considerado:
            A = Não tenho renda e meus gastos são financiados pela minha família ou por outras pessoas.
            B = Tenho renda, mas recebo ajuda da família ou de outras pessoas para financiar meus gastos.
            C = Tenho renda e me sustento totalmente.
            D = Tenho renda, me sustento e contribuo com o sustento da família.
            E = Tenho renda, me sustento e sou o principal responsável pelo sustento da família.
            . = Não respondeu, anulada ou ausente
    '''
    if ano == '2005' or ano == '2008':
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['*'], '.')
    if ano == '2014' or ano == '2017':
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['A'], '.') # A = Não tenho renda e meus gastos são financiados por programas governamentais.
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['B'], 'A')
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['C'], 'B')
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['D'], 'C')
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['E'], 'D')
        df['SITUACAO_TRABALHO'] = df['SITUACAO_TRABALHO'].replace(['F'], 'E')
    return df


def padronizar_ens_medio(ano, df):
    ''''
        Padroniza a variável ENSINO_MEDIO.
        Intervalo considerado:
            A = Todo em escola pública.
            B = Todo em escola privada (particular).
            C = A maior parte em escola pública.
            D = A maior parte em escola privada (particular).
            . = Intervalos que ocorrem apenas em algumas bases, nulos, outros.
    '''
    if ano == '2005' or ano == '2008' or ano == '2011':
        df['ENSINO_MEDIO'] = df['ENSINO_MEDIO'].replace(['E', '*'], '.')
    if ano == '2014' or ano == '2017':
        df['ENSINO_MEDIO'] = df['ENSINO_MEDIO'].replace(['C', 'F', '*'], '.') 
        df['ENSINO_MEDIO'] = df['ENSINO_MEDIO'].replace(['D'], 'C')
        df['ENSINO_MEDIO'] = df['ENSINO_MEDIO'].replace(['E'], 'D')        
    return df

def padronizar_tipo_ens_medio(ano, df):
    ''''
        Padroniza a variável TIPO_EM.
        Intervalo considerado:
            A = Ensino médio tradicional.
            B = Profissionalizante técnico (eletrônica, contabilidade, agrícola, outro).
            C = Profissionalizante magistério (Curso Normal).
            D = Educação de Jovens e Adultos (EJA) e/ou Supletivo, outros.
            . = nulos, outros.
    '''
    if ano == '2005' or ano == '2008' or ano == '2011' or ano == '2014' or ano == '2017':
        df['TIPO_EM'] = df['TIPO_EM'].replace(['E'], 'D')
        df['TIPO_EM'] = df['TIPO_EM'].replace(['*'], '.')      
    return df

def padronizar_horas_estudo(ano, df):
    ''''
        Padroniza a variável HORAS_ESTUDO.
        Intervalo considerado:
            A = Nenhuma, apenas assisto às aulas.
            B = Estuda pelo menos uma hora, excetuando aulas.
            . = nulos, outros.
    '''
    if ano == '2005' or ano == '2008' or ano == '2011' or ano == '2014' or ano == '2017':
        df['HORAS_ESTUDO'] = df['HORAS_ESTUDO'].replace(['C','D','E'], 'B')
        df['HORAS_ESTUDO'] = df['HORAS_ESTUDO'].replace(['*'], '.')      
    return df