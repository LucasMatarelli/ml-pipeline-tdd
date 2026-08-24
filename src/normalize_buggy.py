def normalize_batch_buggy(values):
    """
    Implementação ingênua sem validação de max == min.
    Utilizada para demonstrar falha por ZeroDivisionError em testes de propriedade.
    """
    minimo = min(values)
    maximo = max(values)
    return [(v - minimo) / (maximo - minimo) for v in values]
