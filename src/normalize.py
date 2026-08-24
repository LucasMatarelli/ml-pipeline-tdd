import math


def normalize_batch(values):
    """
    Normaliza uma lista de números para o intervalo [0.0, 1.0] usando
    min-max scaling: (x - min) / (max - min).

    Decisões de design (ver DESIGN.md para detalhes):
      - Lista vazia -> ValueError.
      - Qualquer valor NaN ou infinito na entrada -> ValueError.
      - Se todos os valores forem iguais (max == min, "empate total"),
        não dividimos por zero: retornamos 0.0 para todos os itens,
        pois não existe variação a ser normalizada.

    Args:
        values: lista de int/float.

    Returns:
        Lista de float, mesmo tamanho de `values`, com valores em [0, 1].

    Raises:
        ValueError: se a lista for vazia ou contiver NaN/inf.
    """
    if len(values) == 0:
        raise ValueError("normalize_batch: a lista de entrada não pode ser vazia.")

    for v in values:
        if math.isnan(v) or math.isinf(v):
            raise ValueError(
                f"normalize_batch: valor não-finito encontrado ({v}). "
                "NaN e infinito não são suportados."
            )

    minimo = min(values)
    maximo = max(values)

    if maximo == minimo:
        # Todos os valores são iguais: não há variação para normalizar.
        return [0.0 for _ in values]

    return [(v - minimo) / (maximo - minimo) for v in values]
