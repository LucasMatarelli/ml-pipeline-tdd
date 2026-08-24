from src.normalize import normalize_batch


def test_normalize_batch_simple_range():
    """Teste unitário básico com range conhecido."""
    result = normalize_batch([10, 20, 30])
    assert result[0] == 0.0
    assert result[-1] == 1.0
    assert result[1] == 0.5
