import math
from hypothesis import given, strategies as st

from src.normalize_buggy import normalize_batch_buggy


@given(
    st.lists(
        st.floats(allow_nan=False, allow_infinity=False, width=32),
        min_size=1,
        max_size=50,
    )
)
def test_propriedade_pega_bug_real_na_versao_buggy(valores):
    """
    Valida a invariante [0.0, 1.0] contra a versão buggy.
    Deve falhar com ZeroDivisionError quando min == max.
    """
    resultado = normalize_batch_buggy(valores)
    for r in resultado:
        assert 0.0 <= r <= 1.0
