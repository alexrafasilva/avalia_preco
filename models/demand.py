import numpy as np

def calcular_demanda_ajustada(
    preco: float, 
    preco_medio_concorrentes: float, 
    demanda_base: int, 
    elasticidade: float
) -> float:
    """
    Calcula a demanda ajustada com base na elasticidade-preço.
    
    Args:
        preco (float): Preço do produto
        preco_medio_concorrentes (float): Preço médio dos concorrentes
        demanda_base (int): Demanda quando preço = preço médio
        elasticidade (float): Elasticidade-preço da demanda
        
    Returns:
        float: Demanda ajustada (não negativa)
    """
    if preco <= 0 or preco_medio_concorrentes <= 0:
        raise ValueError("Preços devem ser positivos")
        
    demanda = demanda_base * (preco / preco_medio_concorrentes) ** elasticidade
    return max(demanda, 0)  # Garante demanda não negativa

def calcular_lucro(
    preco: float, 
    custo_marginal: float, 
    preco_medio_concorrentes: float, 
    demanda_base: int, 
    elasticidade: float
) -> float:
    """
    Calcula o lucro com base na demanda ajustada.
    
    Args:
        preco (float): Preço do produto
        custo_marginal (float): Custo por unidade
        preco_medio_concorrentes (float): Preço médio dos concorrentes
        demanda_base (int): Demanda base
        elasticidade (float): Elasticidade-preço
        
    Returns:
        float: Lucro total
    """
    demanda = calcular_demanda_ajustada(preco, preco_medio_concorrentes, demanda_base, elasticidade)
    return (preco - custo_marginal) * demanda