def calcular_demanda(preco: float, preco_medio_concorrentes: float, demanda_base: int, elasticidade: float) -> float:
    """
    Calcula a demanda ajustada usando elasticidade-preço.
    
    Args:
        preco (float): Preço do produto
        preco_medio_concorrentes (float): Preço médio dos concorrentes
        demanda_base (int): Demanda quando preço = preço médio
        elasticidade (float): Elasticidade-preço da demanda
        
    Returns:
        float: Demanda ajustada (não negativa)
    """
    if preco <= 0 or preco_medio_concorrentes <= 0:
        raise ValueError("Preços devem ser positivos.")
    return max(demanda_base * (preco / preco_medio_concorrentes) ** elasticidade, 0)

def calcular_lucro(preco: float, custo_marginal: float, preco_medio_concorrentes: float, demanda_base: int, elasticidade: float) -> float:
    """
    Calcula o lucro total.
    
    Args:
        preco (float): Preço do produto
        custo_marginal (float): Custo marginal de produção
        preco_medio_concorrentes (float): Preço médio dos concorrentes
        demanda_base (int): Demanda base
        elasticidade (float): Elasticidade-preço da demanda
        
    Returns:
        float: Lucro total
    """
    demanda = calcular_demanda(preco, preco_medio_concorrentes, demanda_base, elasticidade)
    return (preco - custo_marginal) * demanda