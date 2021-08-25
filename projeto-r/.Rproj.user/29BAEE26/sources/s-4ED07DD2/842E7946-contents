source('utils.R')
source('filtros.R')
source('conf.R')
# Passo 1: Carregar os pacotes que serão usados

if(!require(dplyr)) install.packages("dplyr")
library(dplyr)                                
if(!require(rstatix)) install.packages("rstatix") 
library(rstatix) 
if(!require(reshape)) install.packages("reshape") 
library(reshape) 
if(!require(PMCMRplus)) install.packages("PMCMRplus") 
library(PMCMRplus)   
if(!require(ggplot2)) install.packages("ggplot2") 
library("writexl")
library(ggplot2)    
library(xtable)

# Função que converte a idade em intervalos
idade_para_intervalo <- function(df){
  df['PESSOA_IDADE'] = replace(df['PESSOA_IDADE'],df['PESSOA_IDADE'] >= 30, 'D')
  df['PESSOA_IDADE'] = replace(df['PESSOA_IDADE'],df['PESSOA_IDADE'] >= 16.0 & df['PESSOA_IDADE'] <= 20.0, 'A')
  df['PESSOA_IDADE'] = replace(df['PESSOA_IDADE'],df['PESSOA_IDADE'] >= 21.0 & df['PESSOA_IDADE'] <= 24.0, 'B')
  df['PESSOA_IDADE'] = replace(df['PESSOA_IDADE'],df['PESSOA_IDADE'] >= 25.0 & df['PESSOA_IDADE'] <= 30.0, 'C')
  return(df)
}

# Carrega o banco de dados
dados <- get_base_de_dados()


# Mostra o tipo das variáveis
glimpse(dados_juntos)


# Cálculo do teste de Kruskal Wallis


# Verifica se exite '.' nas variáveis
unique(dados$EST_CIVIL)

# Remove '.' presente em algumas variáveis
df2<-dados[!(dados["EST_CIVIL"]=="."),]
EST_CIVIL
# Aplica o teste de Kruskal Wallis
k <- kruskal.test(PROVA_NOTABRUTA ~ CURSO_GRUPO, data = df2)
signif(k$p.value, 3)
k


# Preparando para o teste de Dunn
df2 <- idade_para_intervalo(df2)

# Altera os códigos das variáveis pelos nomes correspondentes

  var_interesse = "CURSO_GRUPO"
  valores = DF_VAR_VALOR_NOME[DF_VAR_VALOR_NOME[, "VARIAVEL"] == var_interesse,"VALOR"]
  for(valor in valores){
    nome <- DF_VAR_VALOR_NOME[DF_VAR_VALOR_NOME[, "VARIAVEL"] == var_interesse & DF_VAR_VALOR_NOME[,"VALOR"]==valor,"NOME"]
    #df2[var_interesse] <- nome
    df2[var_interesse] = replace(df2[var_interesse],df2[var_interesse] == valor, nome)
  }

  unique(df2$EST_CIVIL)
# Aplica o pós-teste de Dunn

summary(df2$PESSOA_IDADE)


res_dunn <- dunn_test(PROVA_NOTABRUTA ~ CURSO_GRUPO, data = df2, p.adjust.method = "bonferroni")
res_dunn$p.adj <- as.character(signif(res_dunn$p.adj, 3))
res_dunn$p <- as.character(signif(res_dunn$p, 3))
res_dunn$statistic <- signif(res_dunn$statistic, 2)

# Salva os resultados 
write_xlsx(res_dunn, "tabelas/teste_dunn_ajustado.xlsx")

# Altera os nomes das colunas após aplicação do método dunn

colnames(res_dunn) = c("Variável", "Grupo 1", "Grupo 2", "n1", "n2", "Estatística", "p", "p ajustado", "Significância" )

# Selecionar as colunas que serão imppressas no código latex

vars <- c("Grupo 1", "Grupo 2", "n1", "n2", "Estatística", "p", "p ajustado")

res_dunn <- select(res_dunn, !!vars)
print(xtable(res_dunn), include.rownames=FALSE)


# Teste de Mann-Whitney

# Pessoas do sexo masculino casadas
df2<-dados[!(dados["EST_CIVIL"]=="."),]
df2<-df2[!(df2["EST_CIVIL"]=="C"),]
df2<-df2[!(df2["EST_CIVIL"]=="D"),]
df2<-df2[!(df2["EST_CIVIL"]=="E"),]
df2 <- dados
#df_est_civil_sexo <- filtrar_por_variaveis(df2, c('EST_CIVIL'), c('A'))
df_est_civil_sexo <- filtrar_por_variaveis(df2, c('PESSOA_SEXO'), c(2))


if(!require(dplyr)) install.packages("dplyr") # Instalação do pacote caso não esteja instalado
library(dplyr)                                # Carregamento do pacote
if(!require(dplyr)) install.packages("rstatix") # Instalação do pacote caso não esteja instalado
library(rstatix)    

df_est_civil_sexo<-df_est_civil_sexo[!(df_est_civil_sexo["PESSOA_SEXO"]==3),]
unique(df_est_civil_sexo$PESSOA_SEXO)
w <- wilcox.test(PROVA_NOTABRUTA ~ EST_CIVIL, data = df_est_civil_sexo)
w$p.value
w


