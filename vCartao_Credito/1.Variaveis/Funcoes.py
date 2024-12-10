# Carrega pacotes necessários
import pandas as pd
import numpy as np

# Funções 


# Função para categorização de variáveis numéricas

def Categorizacao(dataframe, pontos_corte, variavel):
    # dataframe é um pandas dataframe
    # pontos_corte é a quantidade de categorias
    # variavel é o nome da coluna da variável numérica a ser categorizada -- string
    
    # nome_coluna = variavel + '_Cat'
    # dataframe[nome_coluna] = pd.qcut(dataframe[variavel], q = pontos_corte)
    categorias, bins = pd.qcut(dataframe[variavel], q = pontos_corte, retbins=True)
    return(categorias, bins)


# Função que retorna uma lista de variáveis correlacionadas

def Vars_Correl(dataframe, list_vars_num, limiar = 0.7, metodo = 'spearman'):
    # dataframe é um pandas dataframe
    # list_vars_num é uma lista das colunas do dataframe que são numéricas
    # limiar é o valor mínimo para o qual consideraremos a correlação. Valores superiores ao limiar serão considerados altamente correlacionados
    # metodo é o critério de correlação dos dados. Pode ser spearman ou pearson
    
    aux1 = dataframe[list_vars_num]
    matriz_correl = aux1.corr(method = metodo)
    
    linha = []
    coluna = []
    valor = []
    
    for i in matriz_correl.index:
        for j in matriz_correl.columns:
            if ((i != j) & (np.abs(matriz_correl[i][j]) >= limiar)):
                linha.append(i)
                coluna.append(j)
                valor.append(matriz_correl[i][j])
    
    Var1 = pd.DataFrame({'Var1': linha})
    Var2 = pd.DataFrame({'Var2': coluna})
    Valores = pd.DataFrame({'Valores': valor})
    Resultado_correl = pd.concat([Var1, Var2, Valores], axis = 1)
    Resultado_correl = Resultado_correl.drop_duplicates(subset=['Valores']).reset_index(drop = 'True')

    return(Resultado_correl)