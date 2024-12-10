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

# Função que retorna o IV em cada categoria e IV total da variável

def IV(dataframe, variavel, target):
    # dataframe é um pandas dataframe
    # variavel é o nome da variável para calcularmos o IV -- string (nesse caso a variável deve ser categórica)
    # target é o nome da variável target -- string
    
    # Eventos de interesse / bads
    qtd_bads = dataframe[dataframe[target] == 1].shape[0]
    df_bads = pd.DataFrame(dataframe[variavel][dataframe[target] == 1].value_counts()/qtd_bads).reset_index().sort_values(by=variavel)
    df_bads.columns = [variavel, 'Perc_bads']
    # df_bads
    
    # Eventos de não interesse / bons
    qtd_bons = dataframe[dataframe[target] == 0].shape[0]
    df_bons = pd.DataFrame(dataframe[variavel][dataframe[target] == 0].value_counts()/qtd_bons).reset_index().sort_values(by=variavel)
    df_bons.columns = [variavel, 'Perc_bons']
    # df_bons
    
    df_result = df_bads.merge(df_bons, on = variavel, how = 'left')
    df_result['Odds'] = df_result['Perc_bons']/df_result['Perc_bads']
    df_result['Woe'] = np.log(df_result['Odds'])
    df_result['IV_parcial'] = (df_result['Perc_bons']-df_result['Perc_bads'])*df_result['Woe']
    df_result['IV'] = sum(df_result['IV_parcial'])

    return(df_result)


# Função que retorna uma lista de IVs das variáveis

def IV_lista_variaveis(dados, var_target, lista_variaveis = ['object', 'category']):
    # lista_variaveis = ['object', 'category']
    # var_target = ['Attrition_Flag']
    
    # var_target é o nome da coluna da variável target -- string
    # dados é um pandas dataframe
    
    aux1 = dados.select_dtypes(include=lista_variaveis)
    aux2 = dados[var_target]
    
    aux = pd.concat([aux1, aux2], axis = 1)
    
    del [aux1, aux2]
    
    lista_for = aux.columns
    resp_IVS = []
    
    for i in range(0,len(lista_for)-1):
        # print(lista_for[i])
        # resp_IVS.append(IV(aux, lista_for[i], lista_for[4])['IV'][0])
        resp_IVS.append(IV(aux, lista_for[i], lista_for[len(lista_for)-1])['IV'][0])
    
    aux1 = pd.DataFrame({'Variaveis': lista_for})
    # aux1 = aux1.drop(index = 4)
    aux1 = aux1.drop(index = max(aux1.index))
    aux2 = pd.DataFrame({'IV': resp_IVS})
    
    output = pd.concat([aux1, aux2], axis = 1)
    
    del [aux1, aux2, lista_for, resp_IVS]
    
    output = output.sort_values(by = 'IV', ascending = False)

    return(output)