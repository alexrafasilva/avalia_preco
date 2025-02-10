def formatar_preco(texto: str) -> float:
    """
    Converte uma string de preço para float.
    
    Args:
        texto (str): Preço no formato "R$ 145.990,00"
        
    Returns:
        float: Preço convertido (ex: 145990.0)
    """
    return float(texto.replace('R$', '').replace('.', '').replace(',', '.').strip())