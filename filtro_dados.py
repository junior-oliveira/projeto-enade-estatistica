import pandas as pd
import filtro_dados as fd

def remover_atributos(df, lista):
    resultado = df.drop(lista, axis=1, errors='ignore')
    return resultado

