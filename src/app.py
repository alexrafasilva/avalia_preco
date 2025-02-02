import sys
import os

# Adiciona o diretório raiz do projeto ao Python PATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Corrigido!

import streamlit as st
import numpy as np
from models.bertrand import otimizar_preco_bertrand  # Agora funcionará
from models.demand import calcular_lucro
from src.utils import plotar_grafico
from src.config import *

# Configuração da página
st.set_page_config(page_title="Otimizador de Preços", layout="wide")
st.title("📈 Otimização de Preços para SUVs - Teoria dos Jogos")

# Sidebar - Parâmetros
with st.sidebar:
    st.header("⚙️ Parâmetros de Entrada")
    
    # Modo de custo automático (58%) vs manual
    usar_custo_auto = st.toggle("Usar custo automático (58% do preço médio)", True)
    
    if usar_custo_auto:
        preco_medio = st.number_input("Preço médio de mercado (R$)", value=100000)
        custo_marginal = 0.58 * preco_medio
        st.info(f"Custo marginal calculado: R${custo_marginal:,.2f}")
    else:
        custo_marginal = st.number_input("Custo Marginal (R$)", value=CUSTO_MARGINAL_PADRAO)
    
    n_concorrentes = st.slider("Número de concorrentes", 1, 5, 3)
    precos_concorrentes = [st.number_input(f"Preço Concorrente {i+1} (R$)", value=100000) for i in range(n_concorrentes)]
    elasticidade = st.slider("Elasticidade-Preço", -2.0, 0.0, ELASTICIDADE, step=0.1)

# Cálculos
preco_medio_concorrentes = np.mean(precos_concorrentes)

# Seção principal
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Otimização de Preço")
    if st.button("Calcular Preço Ótimo", type="primary"):
        preco_otimo, lucro = otimizar_preco_bertrand(
            custo_marginal, 
            preco_medio_concorrentes,
            DEMANDA_BASE,
            elasticidade
        )
        st.success(f"**Preço Ótimo:** R${preco_otimo:,.2f}")
        st.metric("Lucro Anual Estimado", f"R${lucro:,.2f}")

with col2:
    st.subheader("🔍 Análise de Sensibilidade")
    precos_teste = np.linspace(70000, 150000, 50)
    lucros = [calcular_lucro(p, custo_marginal, preco_medio_concorrentes, DEMANDA_BASE, elasticidade) for p in precos_teste]
    st.pyplot(plotar_grafico(precos_teste, lucros))