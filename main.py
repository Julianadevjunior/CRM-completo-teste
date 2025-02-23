import streamlit as st
import requests
import pandas as pd


url = st.secrets["my_secrets"]["url"]
response = requests.get(url)

tabela = {}

#Transformar o response em um dicionário tabela
for i, item in enumerate(response.json()):
    if i == 0:
        for nome in item:
             tabela[nome] = []

    else:
        for i, nome in enumerate(item):
            tabela[list(tabela.keys())[i]].append(nome)

df = pd.DataFrame(tabela)

def dados_cliente(idx):
    keys = ['cod',
            'nome',
            'telefone',
            'bairro',
            'valor',
            'descricao',
            'data_entrada',
            'data_old_update',
            'data_new_update']

    lista_dados = []

    for item in keys:
        lista_dados.append(df[item][idx])

    return lista_dados
st.write(dados_cliente(2))