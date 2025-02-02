import numpy as np
from scipy.optimize import minimize_scalar

def calcular_demanda(preco_proprio, preco_medio_concorrentes, demanda_base, elasticidade):
    """
    Calcula a demanda com base no preço próprio e preço médio dos concorrentes.
    """
    variacao = elasticidade * ((preco_proprio - preco_medio_concorrentes) / preco_medio_concorrentes)
    return max(demanda_base * (1 + variacao), 0)

def encontrar_equilibrio_nash(precos_iniciais, custos_marginais, elasticidade, demanda_base, iteracoes=100):
    """
    Encontra o equilíbrio de Nash para múltiplos concorrentes.
    """
    precos = np.array(precos_iniciais)
    n_jogadores = len(precos)
    
    for _ in range(iteracoes):
        for i in range(n_jogadores):
            funcao = lambda p: -((p - custos_marginais[i]) * calcular_demanda(
                p, np.mean(np.delete(precos, i)), demanda_base, elasticidade))
            
            resultado = minimize_scalar(funcao, bounds=(70000, 150000), method='bounded')
            precos[i] = resultado.x
    
    return precos