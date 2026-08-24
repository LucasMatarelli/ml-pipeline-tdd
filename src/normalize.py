import math


def normalize_batch(values):
    """
    Normaliza uma lista de números para o intervalo [0.0, 1.0] via min-max scaling.

    Args:
        values: Lista de int ou float.

    Returns:
        Lista normalizada no intervalo [0.0, 1.0].

    Raises:
        ValueError: Caso a lista esteja vazia ou contenha NaN/inf.
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
        return [0.0 for _ in values]

    return [(v - minimo) / (maximo - minimo) for v in values]
