import numpy as np 
import pylab 
import scipy.stats as stats
import pandas as pd
import filtro_dados as fd
import statsmodels.api as sm
from matplotlib import pyplot as plt
df_dados_enade = pd.read_csv("base_de_dados/microdados_enade_2004.csv", delimiter=';')
df = fd.get_dados_filtrados(df_dados_enade)

# Gráfico QQ Plot para verificar a normalidade dos dados 
def qq_plot(lista):
    stats.probplot(lista, dist="norm", plot=pylab)
    pylab.show()

sm.qqplot(df.NT_GER, line="s")
plt.show()