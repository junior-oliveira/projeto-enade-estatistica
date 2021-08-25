# Arquivos e bibliotecas necessárias
library(dplyr)
source('filtros.R')
source('utils.R')
source("conf.R")
#library(MVN)
library(nortest)
library("writexl")
library(xtable)
#
microdados_enade <- get_base_de_dados()

estatisticas_descritivas <- function(dados_enade, variavel, valor, filtrar=TRUE){
 
  # Filtra os dados que serão considerados no cálculo das estatísticas
  if(filtrar){
    dados <- filtrar_por_variaveis(dados_enade, c(variavel), c(valor))
    dados <- dados$PROVA_NOTABRUTA
  }
  else{
    dados <- dados_enade$PROVA_NOTABRUTA
  }
  
  n <- length(dados)
  media <- round(mean(dados), 1)
  desvio_padrao <- round(sd(dados), 1)
  mediana <- round(median(dados),1)
  minimo <- round(min(dados),1)
  maximo <- round(max(dados),1)
  percentis <- quantile(dados, c(0.25, 0.75)) 
  # remove os nomes associados às variáveis
  percentis <- unname(percentis)
  percentil_25 = round(percentis[1],1)
  percentil_75 = round(percentis[2],1)
  
  # normalidade
  teste_normalidade = ad.test(dados) 
  p_value <- signif(teste_normalidade$p.value, 3)
  normalidade = "Sim"
  if(p_value < 0.05){
    normalidade = "Não"
  }
  
  # Traduz o código da variável para o valor correspondente (carregar source("conf.R") antes)
  if(filtrar){
    valor_traduzido <- DF_VAR_VALOR_NOME[DF_VAR_VALOR_NOME[, "VARIAVEL"]==variavel & DF_VAR_VALOR_NOME[,"VALOR"]==valor,"NOME"]
    descricao <- DF_VAR_VALOR_NOME[DF_VAR_VALOR_NOME[, "VARIAVEL"]==variavel & DF_VAR_VALOR_NOME[,"VALOR"]==valor,"DESCRICAO"]
  }
  else{
    descricao <- variavel
    valor_traduzido <- valor
  }
     
 
  linha <- c(descricao, valor_traduzido, n, media, desvio_padrao, mediana, minimo, maximo, p_value, normalidade)
  
  return(linha)
}


# Função de retorna a tabela com todas as estatísticas descritivas de cada variável considerada

tabela_estatisticas <- function(dados_enade, variaveis_interesse){
  # Utilizar se considerar os percentis
  #colunas <- c('Variável', 'Valor', 'n', 'media', 'desvio_padrao', 'mediana', 'minimo', 'maximo', 'percentil_25', 'percentil_50', 'p-valor', 'normalidade')
  colunas <- c('Variável', 'Valor', 'n', 'Med', 'DP', 'Medi', 'Min', 'Max', 'p-valor', 'Norm')
  df <- setNames(data.frame(matrix(ncol = length(colunas), nrow = 0)), colunas)
  
  linha <- estatisticas_descritivas(dados_enade, "Total", '', filtrar = FALSE)
  df[nrow(df) + 1, ] <- linha 
  for(var_interesse in variaveis_interesse){
    valores = DF_VAR_VALOR_NOME[DF_VAR_VALOR_NOME[, "VARIAVEL"] == var_interesse,"VALOR"]
    for(valor in valores){
      linha <- estatisticas_descritivas(dados_enade, var_interesse, valor)
      df[nrow(df) + 1, ] <- linha  
    }
  }
  return(df)
}

est_desc <- tabela_estatisticas(microdados_enade, c('CURSO_GRUPO'))
select(microdados_enade, starts_with("PROVA"))
vars <- c('Variável', 'Valor', 'n', 'Med', 'DP', 'Medi', 'Min', 'Max', 'p-valor', 'Norm' )

t = select(est_desc, !!vars)

print(xtable(est_desc), include.rownames=FALSE)


#write_xlsx(est_desc, "tabelas/analise_descritiva_e_normalidade.xlsx")

