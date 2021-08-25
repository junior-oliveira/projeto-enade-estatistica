# ref: https://rpubs.com/melinatarituba/356739
library(MVN)
microdados_enade <- read.csv("/Volumes/GoogleDrive/Meu Drive/Doutorado/Disciplinas/Estatística/Projeto/projeto-enade-estatistica-1/bases_de_dados_filtradas/base_completa.csv")


dados <- as.data.frame(t(as.matrix(microdados_enade$PROVA_NOTABRUTA)))



dados <- na.omit(dados) # remove linhas com valoes nulos
mvn(microdados_enade$PROVA_FE_NOTABRUTA, multivariatePlot = 'histogram')
library(dplyr)

res <- dplyr::filter(microdados_enade, grepl(3, CURSO_REGIAO))
a <- res %>%
  select(PROVA_FE_NOTABRUTA, PROVA_NOTABRUTA)
#a <- a[1:4000,]

mvn(a, mvnTest= 'dh', univariatePlot = 'histogram', univariateTest = "AD")


source('filtros.R')


df <- microdados_enade
lista_var <- c("IES_CATEGORIA", "ANO")
lista_valores <- c(1, 2005)
b <- filtrar_por_variaveis(microdados_enade, c('IES_CATEGORIA', 'ANO'), c(1, 2005))

# Gera um histograma a partir dos dados de uma coluna do dataframe
histograma <- function(coluna_df, main='Histograma', xlab = "Nota", ylab= "Densidades", cex=1.0){
  
  # Plota o histograma
  hist(coluna_df, xlab = xlab, ylab= ylab, main = main, prob= TRUE, cex=cex)
  
  # Calcula a distribuição normal com média e desvio padrão iguais aos dados plotados no histograma
  points(seq(min(coluna_df), max(coluna_df)), dnorm(seq(min(coluna_df), max(coluna_df)), mean(coluna_df), sd(coluna_df)), type="l", col="red")
  
  #ref: https://randyzwitch.com/overlay-histogram-in-r/
}

qq_plot <- function(df_coluna, main='Q-Q Plot', xlab= "Quantis teóricos", ylab="Quantis amostrais", cex = 1.0){
  qqnorm(df_coluna, main=main, xlab=xlab, ylab=ylab, cex=cex)
  qqline(df_coluna, col = 2,lwd=2,lty=2)
}

# plota os gráficos para a variável PROVA_NOTABRUTA

par(mfrow=c(1,5), cex=0.5, oma = c(0, 0, 2, 0)) 
histograma(microdados_enade$PROVA_NOTABRUTA)
qq_plot(microdados_enade$PROVA_NOTABRUTA)
mtext(expression(bold("Nota Geral da Prova (Enade)")), outer = TRUE, cex = 1.0)

histogramas <- function(df, lista_rotulos, lista_var, lista_valores, main="Nota Geral da Prova (Enade)" ){
  # remover mar = rep(2, 4) para aparecer os rótulos dos eixos. Adiciona cex=0.5 para rodar
  par(mfrow=c(2,5), mar = rep(2, 4), oma = c(0, 0, 2, 0)) 
  
  for (i in 1:length(lista_var)){
    df_filtrado <- df %>% filter(!!as.symbol(lista_var[i]) == lista_valores[i])
    histograma(df_filtrado$PROVA_NOTABRUTA, main = lista_rotulos[i], cex=1.5)
  }
  for (i in 1:length(lista_var)){
    df_filtrado <- df %>% filter(!!as.symbol(lista_var[i]) == lista_valores[i])
    qq_plot(df_filtrado$PROVA_NOTABRUTA, main = lista_rotulos[i], cex=1.5)
  }
  mtext(expression(bold('Nota geral por região')), outer = TRUE, cex = 1.5)
}
png(file="mygraphic.png",width=3000,height=1500, res=300)
par(mfrow=c(1,2), cex=0.8, oma = c(0, 0, 2, 0)) 
histograma(microdados_enade$PROVA_NOTABRUTA)
qq_plot(microdados_enade$PROVA_NOTABRUTA)
mtext(expression(bold("Nota Geral da Prova (Enade)")), outer = TRUE, cex = 1.0)
dev.off()
# histograma das notas por região
png(file="mygraphic.png",width=3000,height=1500, res=300)
histogramas(microdados_enade, c('Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'), 
            c('CURSO_REGIAO', 'CURSO_REGIAO', 'CURSO_REGIAO',
              'CURSO_REGIAO','CURSO_REGIAO'), c(1, 2, 3, 4, 5), main="Nota geral por região" )
dev.off()