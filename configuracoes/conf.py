# Variáveis de interesse para serem utilizadas após filtragem 
# A variável 'CURSO_MODALIDADE' não foi considerada pois não existe nas bases 2005 e 2008
LISTA_VAR_INTERESSE = ['ANO', 'IES_COD_MEC', 'PESSOA_CURSO_ANO_ENTRADA', 'IES_CATEGORIA', 'IES_TIPO', 'CURSO_GRUPO', 'CURSO_REGIAO', 'CURSO_UF',
                        'PESSOA_IDADE', 'PESSOA_SEXO', 'PROVA_FG_OBJETIVAS_NOTABRUTA', 'PROVA_FG_DISCURSIVAS_NOTABRUTA', 
                        'PROVA_FG_NOTABRUTA', 'PROVA_FE_OBJETIVAS_NOTABRUTA', 'PROVA_FE_DISCURSIVAS_NOTABRUTA', 
                        'PROVA_FE_NOTABRUTA', 'PROVA_NOTABRUTA', 'QUESTIONARIO_PERCEPCAO_Q1', 'QUESTIONARIO_PERCEPCAO_Q2', 
                        'QUESTIONARIO_PERCEPCAO_Q3', 'QUESTIONARIO_PERCEPCAO_Q4', 'QUESTIONARIO_PERCEPCAO_Q5', 
                        'QUESTIONARIO_PERCEPCAO_Q6', 'QUESTIONARIO_PERCEPCAO_Q7', 'QUESTIONARIO_PERCEPCAO_Q8', 
                        'QUESTIONARIO_PERCEPCAO_Q9', 'EST_CIVIL', 
                        'RENDA', 'SITUACAO_TRABALHO', 'CH_TRABALHO', 'ENSINO_MEDIO', 'TIPO_EM', 'HORAS_ESTUDO']

# Variáveis de presença que devem ser consideradas como 555 em todas as bases de dados
# Para considerar outros tipos de variáveis, acrescente aqui
VAR_PRESENCA =  ['PROVA_DISCENTE_PRESENTE_ENADE', 'PROVA_DISCENTE_FEZ_PROVA', 
                'PROVA_FG_OBJETIVAS_DISCENTE_FEZ_PROVA', 'PROVA_FG_DISCURSIVAS_DISCENTE_FEZ_PROVA', 
                'PROVA_FE_OBJETIVAS_DISCENTE_FEZ_PROVA', 'PROVA_FE_DISCURSIVA_DISCENTE_FEZ_PROVA']

# Lista de variáveis a serem convertidas para variáveis categóricas
LISTA_VAR_CONVERT_CATEGORICO = ['QUESTIONARIO_PERCEPCAO_Q1', 'QUESTIONARIO_PERCEPCAO_Q2', 'QUESTIONARIO_PERCEPCAO_Q3', 
                                'QUESTIONARIO_PERCEPCAO_Q4', 'QUESTIONARIO_PERCEPCAO_Q5', 'QUESTIONARIO_PERCEPCAO_Q6', 
                                'QUESTIONARIO_PERCEPCAO_Q7', 'QUESTIONARIO_PERCEPCAO_Q8', 'QUESTIONARIO_PERCEPCAO_Q9', 
                                'RENDA', 'SITUACAO_TRABALHO', 'CH_TRABALHO', 'ENSINO_MEDIO', 'TIPO_EM', 'HORAS_ESTUDO', 
                                'EST_CIVIL']

# Lista de cursos a serem considerados no experimento
## ENADE 2005 ##
# 40 - Computação
# 72 = TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS
# 79 = TECNOLOGIA EM REDES DE COMPUTADORES
# 4003 = Engenharia Da Computação
# 4004 = COMPUTAÇÃO (BACHARELADO)
# 4005 = COMPUTAÇÃO (LICENCIATURA)
# 4006 = COMPUTAÇÃO (SISTEMAS DE INFORMAÇÃO)
# 4007 = COMPUTAÇÃO (ENGENHARIA DE COMPUTAÇÃO)
# 5809 = ENGENHARIA (GRUPO II) - ENGENHARIA DE COMPUTAÇÃO

# Não utilizado (verificar necessidade)
# 6409 = Tecnologia em Gestão da Tecnologia da Informação"

LISTA_CURSO_GRUPO = [72, 79, 4003, 4004, 4005, 4006]


# Variável que representa os cursos
VAR_CURSO_GRUPO = 'CURSO_GRUPO'

# Variável que representa se um aluno é concluinte
VAR_PESSOA_CONCLUINTE = 'PESSOA_CONCLUINTE'

# Variável que representa a renda de um aluno
VAR_RENDA = 'RENDA'

# Variável que representa a nota geral na prova do enade
PROVA_NOTABRUTA = 'PROVA_NOTABRUTA'

# Bases de dados
BASES_DE_DADOS = {'2005': 'base_de_dados/alter/AA/microdados_enade_2005_alt.csv', 
                    '2008': 'base_de_dados/alter/AA/microdados_enade_2008_alt.csv', 
                    '2011': 'base_de_dados/alter/AA/microdados_enade_2011_alt.csv', 
                    '2014': 'base_de_dados/alter/AA/microdados_enade_2014_alt.csv', 
                    '2017': 'base_de_dados/alter/AA/MICRODADOS_ENADE_2017.txt'}

# Arquivo com os rótulos novos a considerar
ARQUIVO_ROTULOS_A_CONSIDERAR = 'rotulos_colunas/rotulos_colunas_todas_bases.xlsx'

# Variável que representa a categoria da IES (publica, privada, especial)
VAR_IES_CATEGORIA = 'IES_CATEGORIA'

# Listas de categorias a substituir (padronização)
LISTA_CATEGORIA_FEDERAL = [93, 10002] 
LISTA_CATEGORIA_ESTADUAL = [10001]
LISTA_CATEGORIA_MUNICIPAL = [116, 10003]
LISTA_CATEGORIA_PRIVADA = [5, 118, 121, 10004, 10005, 10006, 10007, 10008, 10009]
LISTA_CATEGORIA_ESPECIAL = [7]