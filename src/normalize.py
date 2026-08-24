def normalize_batch(values):
    minimo = min(values)
    maximo = max(values)
    return [(v - minimo) / (maximo - minimo) for v in values]
