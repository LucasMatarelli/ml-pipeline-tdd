def normalize_batch_buggy(values):
    """
    Versão BUGADA de propósito: não trata o caso em que todos os valores
    são iguais (max == min). Nesse caso ocorre ZeroDivisionError,
    algo que um teste de exemplo pontual (com dados "normais") jamais
    encontraria sozinho, mas que o teste de propriedade encontra
    imediatamente porque o Hypothesis gera esse caso-limite sozinho.
    """
    minimo = min(values)
    maximo = max(values)
    return [(v - minimo) / (maximo - minimo) for v in values]  # bug: sem guarda para maximo == minimo
