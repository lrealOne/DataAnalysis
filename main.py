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

''' Mapa de calor: '''

raw_data=['Coarse wool Price',  'Copra Price','Cotton Price', 'Fine wool Price',  'Hard log Price', 'Hard sawnwood Price',
 'Hide Price', 'Plywood Price', 'Rubber Price', 'Softlog Price', 'Soft sawnwood Price', 'Wood pulp Price']


# matriz correlata
corrmat = dataframe[raw_data].corr()


# tamanho grafico
fig = plt.figure(figsize = (12, 9))


# mascarando a parte de cima devido a simetria da matriz
mask = np.triu(np.ones_like(corrmat, dtype=bool))
sns.heatmap(corrmat, vmax = .8,mask=mask, square = True, annot = True)
plt.show()


''' Pequeno grafico evolutivo sobre a lã grossa e seu percentual de preço:'''
la_map=dataframe[["Coarse wool Price", "Coarse wool price % Change"]].plot(figsize=(11, 9), subplots=True, linewidth=1)


''' Variação do preço de cada item utilizando um for para percorrer a lista:'''
materials=['Copra price % Change','Softlog price % Change','Rubber price % Change','Cotton price % Change','Coarse wool price % Change','Fine wool price % Change','Hard log price % Change','Hard sawnwood price % Change','Hide price % change','Plywood price % Change','Soft sawnwood price % Change','Wood pulp price % Change']
for i in range(len(materials)):
    plt.figure(figsize=(12,12))
    dataframe[materials[i]].hist(figsize=(11, 9), linewidth=1)
    plt.xlabel('% Change')
    plt.ylabel('count')
    plt.legend(materials[i:],loc='upper center',bbox_to_anchor=(1.2,1))


''' Analise da materia prima com menor preço ao longo dos anos:'''
plt.figure(figsize=(10, 10))
materials_list=['Copra Price','Softlog Price','Rubber Price','Cotton Price','Coarse wool Price','Fine wool Price','Hard log Price','Hard sawnwood Price','Hide Price','Plywood Price','Soft sawnwood Price','Wood pulp Price']
for i in range(len(materials_list)):
    plt.subplot(4,3,i+1)
    plt.subplots_adjust( hspace=1 ,wspace=0.5)
    plt.title(materials_list[i])
    plt.plot(dataframe[materials_list[i]])
    plt.xticks(rotation=90)
plt.suptitle("Comparação de preço.")

