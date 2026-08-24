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
    Mesma invariante de antes, agora aplicada à versão BUGADA.
    Esperado: esse teste FALHA (ZeroDivisionError) assim que o Hypothesis
    gerar uma lista com todos os valores iguais — provando que a
    propriedade realmente pegaria esse bug em produção.
    """
    resultado = normalize_batch_buggy(valores)
    for r in resultado:
        assert 0.0 <= r <= 1.0
