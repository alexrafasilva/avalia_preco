import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import numpy as np
import pandas as pd
import sqlite3
from models.bertrand import otimizar_preco
from src.database import criar_tabela, inserir_preco, obter_preco_medio
from src.config import DEMANDA_BASE, ELASTICIDADE_PADRAO

# Configuração inicial
criar_tabela()
st.set_page_config(page_title="Otimizador de Preços SUV", layout="wide")
st.title("🚙 Otimizador de Preços - Teoria dos Jogos")

# Sidebar - Controle de dados
with st.sidebar:
    st.header("📊 Gestão de Dados")
    
    # Modo de entrada
    modo_dados = st.radio("Fonte de dados:", ["Banco de Dados", "Manual"])
    
    if modo_dados == "Manual":
        n_concorrentes = st.slider("Número de concorrentes", 1, 5, 3)
        precos_concorrentes = [st.number_input(f"Preço concorrente {i+1} (R$)", value=100000) 
                              for i in range(n_concorrentes)]
        preco_medio = np.mean(precos_concorrentes)
    else:
        preco_medio = obter_preco_medio()
        st.info(f"Preço médio atual: R${preco_medio:,.2f}")

# Parâmetros principais
with st.sidebar:
    st.header("⚙️ Parâmetros")
    custo_marginal = st.number_input("Custo marginal (R$)", value=60000)
    elasticidade = st.slider("Elasticidade-preço", -2.0, 0.0, ELASTICIDADE_PADRAO, 0.1)

# Seção principal
col1, col2 = st.columns(2)

with col1:
    st.subheader("💡 Otimização de Preço")
    if st.button("Calcular preço ótimo", type="primary"):
        preco_otimo, lucro = otimizar_preco(custo_marginal, preco_medio, DEMANDA_BASE, elasticidade)
        st.success(f"**Preço recomendado:** R${preco_otimo:,.2f}")
        st.metric("Lucro projetado", f"R${lucro:,.2f}")

with col2:
    st.subheader("📈 Análise Competitiva")
    if modo_dados == "Banco de Dados":
        conn = sqlite3.connect('database/precos.db')
        dados = pd.read_sql("SELECT marca, modelo, preco FROM precos", conn)
        st.dataframe(dados.style.format({"preco": "R${:,.2f}"}))
    else:
        st.write("Preços inseridos manualmente:")
        for i, preco in enumerate(precos_concorrentes):
            st.write(f"- Concorrente {i+1}: R${preco:,.2f}")

# Administração do banco de dados
with st.expander("🔧 Adicionar dados ao banco"):
    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    preco = st.number_input("Preço (R$)", min_value=0)
    if st.button("Salvar registro"):
        inserir_preco(marca, modelo, preco)
        st.success("Dados salvos!")