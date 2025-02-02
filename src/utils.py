import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
def plotar_grafico(precos: list, lucros: list) -> plt.Figure:
    """
    Gera um gráfico profissional de preço vs lucro.
    
    Args:
        precos (list): Lista de preços testados
        lucros (list): Lista de lucros correspondentes
        
    Returns:
        plt.Figure: Objeto de figura do matplotlib
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(precos, lucros, 
            color='#2ecc71', 
            linewidth=2.5, 
            marker='o',
            markersize=6,
            markerfacecolor='#e74c3c')
    
    ax.set_title("Relação Preço vs Lucro", fontsize=14, pad=20)
    ax.set_xlabel("Preço (R$)", fontsize=12)
    ax.set_ylabel("Lucro (R$)", fontsize=12)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.tick_params(axis='both', which='major', labelsize=10)
    
    # Destacar ponto máximo
    max_idx = np.argmax(lucros)
    ax.annotate(f'Máximo: R${lucros[max_idx]:,.2f}',
                xy=(precos[max_idx], lucros[max_idx]),
                xytext=(precos[max_idx]+5000, lucros[max_idx]*0.9),
                arrowprops=dict(facecolor='black', shrink=0.05),
                fontsize=10)
    
    plt.tight_layout()
    return fig