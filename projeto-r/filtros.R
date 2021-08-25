# há diferença estatística significativa entre as notas do Enade em diferentes regiões do país
# H0: a média das notas é igual
# H1: a média das notas é diferente

get_regiao <- function(df, codigo_regiao) {
  df = with(df, df[ (CURSO_REGIAO==codigo_regiao), ])
  df <- na.omit(df) # remove linhas com valoes nulos
  return(df)
}

filtrar_por_variaveis <- function (df, lista_var, lista_valores){
  for (i in 1:length(lista_var)){
    df <- df %>% filter(!!as.symbol(lista_var[i]) == lista_valores[i])
  }
  return(df)
}





