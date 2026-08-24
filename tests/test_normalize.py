from src.normalize import normalize_batch


def test_normalize_batch_simple_range():
    """
    Teste de exemplo (pontual): para uma lista conhecida,
    o menor valor deve virar 0.0 e o maior deve virar 1.0.
    """
    result = normalize_batch([10, 20, 30])
    assert result[0] == 0.0
    assert result[-1] == 1.0
    assert result[1] == 0.5
