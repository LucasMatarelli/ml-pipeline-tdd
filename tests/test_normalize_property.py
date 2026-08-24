import math
from hypothesis import given, strategies as st

from src.normalize import normalize_batch

lista_de_floats_finitos = st.lists(
    st.floats(allow_nan=False, allow_infinity=False, width=32),
    min_size=1,
    max_size=50,
)


@given(lista_de_floats_finitos)
def test_propriedade_saida_sempre_entre_zero_e_um(valores):
    """Invariante: todos os elementos normalizados devem pertencer a [0.0, 1.0]."""
    resultado = normalize_batch(valores)

    assert len(resultado) == len(valores)
    for r in resultado:
        assert not math.isnan(r)
        assert not math.isinf(r)
        assert 0.0 <= r <= 1.0


@given(
    st.lists(
        st.floats(allow_nan=False, allow_infinity=False, width=32),
        min_size=2,
        max_size=50,
    )
)
def test_propriedade_minimo_vira_zero_e_maximo_vira_um_quando_ha_variacao(valores):
    """Invariante: com variabilidade nos dados, min -> 0.0 e max -> 1.0."""
    if min(valores) == max(valores):
        return

    resultado = normalize_batch(valores)
    assert min(resultado) == 0.0
    assert max(resultado) == 1.0
