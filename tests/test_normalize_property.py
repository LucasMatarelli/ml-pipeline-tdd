import math
from hypothesis import given, strategies as st

from src.normalize import normalize_batch

# Estratégia: listas de floats finitos (sem NaN/inf), com pelo menos 1 item.
lista_de_floats_finitos = st.lists(
    st.floats(allow_nan=False, allow_infinity=False, width=32),
    min_size=1,
    max_size=50,
)


@given(lista_de_floats_finitos)
def test_propriedade_saida_sempre_entre_zero_e_um(valores):
    """
    Invariante: para QUALQUER lista finita e não vazia de números,
    todo valor normalizado deve estar dentro do intervalo [0.0, 1.0].
    Isso vale independentemente de quantos itens, sinais, ou repetições existam.
    """
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
    """
    Invariante: se existe alguma variação nos dados (min != max),
    o menor valor original deve virar exatamente 0.0 e o maior
    valor original deve virar exatamente 1.0 após a normalização.
    """
    if min(valores) == max(valores):
        return  # não se aplica quando não há variação (caso coberto em outro teste)

    resultado = normalize_batch(valores)
    assert min(resultado) == 0.0
    assert max(resultado) == 1.0
