from scipy.optimize import minimize_scalar
from .demand import calcular_lucro

def otimizar_preco(custo_marginal: float, preco_medio_concorrentes: float, demanda_base: int, elasticidade: float) -> tuple:
    """
    Encontra o preço ótimo usando o Modelo de Bertrand.
    
    Args:
        custo_marginal (float): Custo marginal de produção
        preco_medio_concorrentes (float): Preço médio dos concorrentes
        demanda_base (int): Demanda base
        elasticidade (float): Elasticidade-preço da demanda
        
    Returns:
        tuple: (preco_otimo, lucro_maximo)
    """
    funcao_objetivo = lambda p: -calcular_lucro(p, custo_marginal, preco_medio_concorrentes, demanda_base, elasticidade)
    resultado = minimize_scalar(funcao_objetivo, bounds=(50000, 200000), method='bounded')
    return resultado.x, -resultado.fun