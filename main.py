# Código executado atraves do Google Collab

''' Primeiramente importamos as libs do py que utilizaremos, nesse caso:'''
import numpy as np  # lib numpy biblioteca usada para realizar operações em arrays multidimensionais.
import pandas as pd # lib pandas é comumente utilizada para trabalhar com datasets.


""" Agora importo (utilizando pandas) o arquivo que desejo analisar: """
dataframe = pd.read_csv("agricultural_raw_material.csv") # read_csv por se tratar de um arquivo .csv


""" Começo buscando valores nulos e os somando:"""
dataframe.isnull().sum() # isnull() checa se é nulo, caso positivo ele irá somar utilizando o sum()


""" Agora, tratarei os valores nulos conforme minha necessidade (me baseando no arquivo)"""
dataframe = dataframe.replace("%", "", regex=True)
dataframe = dataframe.replace(",", "", regex=True)
dataframe = dataframe.replace("-", "", regex=True)
dataframe = dataframe.replace("", np.nan)
dataframe = dataframe.replace("MAY90", np.nan)
dataframe = dataframe.dropna() # removendo os nulos.


""" Convertendo alguns campos para float:"""
lista = ["Coarse wool Price", "Coarse wool price % Change", "Copra Price", "Copra price % Change", "Cotton price % Change","Fine wool Price", "Fine wool price % Change", "Hard log price % Change", "Hard sawnwood price % Change", "Hide price % change", "Plywood price % Change", "Rubber price % Change", "Softlog price % Change", "Soft sawnwood price % Change", "Wood pulp price % Change"]
dataframe[lista] = dataframe[lista].astype("float")


''' Retornando as 5 primeiras linhas do dataframe:'''
dataframe.head()


''' Conversão da coluna month para o modelo datetime: '''
dataframe.Month = pd.to_datetime(dataframe.Month.str.upper(), format="%b%y", yearfirst=False)
dataframe = dataframe.set_index("Month")

########################################

""" Agora iniciaremos a Analise Exploratoria e Visualização com Matplotlib e Seaborn"""
import seaborn as sns # type: ignore 
import matplotlib
import matplotlib.pyplot as plt # type: ignore




