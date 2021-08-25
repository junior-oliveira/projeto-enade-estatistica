
microdados_enade <- read.csv("/Volumes/GoogleDrive/Meu Drive/Doutorado/Disciplinas/Estatística/Projeto/projeto-enade-estatistica-1/bases_de_dados_filtradas/base_completa.csv")

#Remover valores ausentes
#microdados_enade <- na.omit(microdados_enade) # Method 1 - Remove NA

# QQ PLOT
qqnorm(microdados_enade$PROVA_NOTABRUTA)
qqline(microdados_enade$PROVA_NOTABRUTA, col = 2,lwd=2,lty=2)

# Histograma
hist(microdados_enade$PROVA_NOTABRUTA, main="Nota Geral", 
     xlab="Acertos", ylab = "Quantidade")
#curve(dnorm(x, mean=mean(microdados_enade$PROVA_NOTABRUTA), sd=sd(microdados_enade$PROVA_NOTABRUTA)), add=TRUE)

# Filtra os dados com base em condições
teste = with(microdados_enade, microdados_enade[ (ANO==2005 & IES_CATEGORIA == 1) | (ANO==2005 & IES_CATEGORIA == 1), ])

# Teste de normalidade
xb <- mean(microdados_enade$PROVA_NOTABRUTA) # mu
sx <- sd(microdados_enade$PROVA_NOTABRUTA) # sigma
ks.test(microdados_enade$PROVA_NOTABRUTA, "pnorm", xb, sx)
shapiro.test(teste$PROVA_NOTABRUTA)
hist(teste$PROVA_NOTABRUTA, main="Nota Geral", 
     xlab="Acertos", ylab = "Quantidade")

select(microdados_enade, starts_with("PROVA"))
vars <- c(var1 = "CURSO_REGIAO","PROVA_NOTABRUTA" )

select(microdados_enade, !!vars)

source("filtros.R")
df = get_regiao(microdados_enade, 1)
source("conf.R")
c <- LIST_VAR_NORM_TEST
d <- setNames(data.frame(matrix(ncol = length(c), nrow = 0)), c)
new_row <- c(1, 20.3, 0.004, 1, 20.3, 0.004, 1)
d[nrow(d) + 1, ] <- new_row  

c[2]


# Concatenar dois dataframes (foi usado na tentativa de usar o teste de friedman)
dados_juntos <- new <- rbind(dados_r1, dados_r2, dados_r3, dados_r4)

dados_juntos <- sort_df(dados_juntos, vars = 'ID')

# Reseta os índices nativos do dataframe
row.names(dados_juntos) <- NULL

# Criar uma variável ID com valores automáticos
dados_juntos$ID <- seq.int(nrow(dados_juntos))

# Transformando a variável X em fator
dados_juntos$ID <- factor(dados_juntos$ID)

# Ordena os dados com base na variável X
dados <- sort_df(dados, vars = 'X')

# Seleciona os dados com base nas variáveis
#df2<-dados[(dados[var_interesse]== 1 |  dados[var_interesse] == 2 | dados[var_interesse]== 3 | dados[var_interesse]== 4 ),]
