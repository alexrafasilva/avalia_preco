import numpy as np
from scipy.optimize import minimize_scalar
from .demand import calcular_lucro

def encontrar_equilibrio_nash(precos_iniciais: list, custos_marginais: list, elasticidade: float, demanda_base: int, iteracoes: int = 100) -> list:
    """
    Encontra o equilíbrio de Nash para múltiplos concorrentes.
    
    Args:
        precos_iniciais (list): Preços iniciais dos concorrentes
        custos_marginais (list): Custos marginais dos concorrentes
        elasticidade (float): Elasticidade-preço da demanda
        demanda_base (int): Demanda base
        iteracoes (int): Número de iterações para convergência
        
    Returns:
        list: Preços de equilíbrio de Nash
    """
    precos = np.array(precos_iniciais)
    n_jogadores = len(precos)
    
    for _ in range(iteracoes):
        for i in range(n_jogadores):
            funcao = lambda p: -calcular_lucro(p, custos_marginais[i], np.mean(np.delete(precos, i)), demanda_base, elasticidade)
            resultado = minimize_scalar(funcao, bounds=(50000, 200000), method='bounded')
            precos[i] = resultado.x
    
    return precos.tolist()