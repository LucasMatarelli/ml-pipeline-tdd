# Decisões de Design — normalize_batch

Função escolhida: normalização de lote (batch normalization) usando min-max scaling, que transforma qualquer lista de números para o intervalo `[0.0, 1.0]`. É uma etapa essencial em pipelines de ML antes de treinar modelos sensíveis à escala das features (ex.: KNN, redes neurais, regressão com regularização).

Fórmula: `(x - min) / (max - min)`

## Casos-limite e decisões tomadas

| Caso | Decisão | Justificativa |
| :--- | :--- | :--- |
| Lista vazia (`[]`) | Levanta `ValueError` | Não existe min/max de uma lista vazia. A validação explícita evita que o erro genérico de `min()`/`max()` propague sem contexto. |
| `NaN` em qualquer posição | Levanta `ValueError` | `NaN` quebra comparações lógicas (`NaN < x` retorna `False`), tornando min/max indefinidos. Fail-fast para não corromper o pipeline. |
| `inf` / `-inf` em qualquer posição | Levanta `ValueError` | Valores infinitos quebram a escala relativa. Tratado como entrada inválida. |
| Todos os valores iguais (`max == min`, ex.: `[5, 5, 5]`) | Retorna `0.0` para todos | Evita divisão por zero. Sem variação amostral, a convenção padrão é zerar o vetor. |
| Empates que não são o máximo/mínimo global (ex.: `[1, 5, 5, 9]`) | Comportamento natural da fórmula | Valores de entrada idênticos geram saídas normalizadas idênticas pela própria aritmética da fórmula. |
| Lista com 1 elemento (ex.: `[7]`) | Trata como `max == min` (retorna `[0.0]`) | Elemento unitário não possui variabilidade relativa. |
| Tipos de entrada (`int` vs `float`) | Aceita ambos | Coerção implícita nativa do Python nas operações aritméticas. |

## Por que teste de propriedade (Hypothesis) e não apenas testes de exemplo?

Testes pontuais de exemplo (`assert normalize_batch([10, 20, 30]) == [...]`) validam somente caminhos pré-determinados. Eles não asseguram o comportamento diante de entradas aleatórias, vetores de grande escala, negativos ou empates arbitrários.

O Hypothesis gera automaticamente centenas de combinações de dados para validar invariantes fundamentais:
1. Toda saída deve estar contida rigorosamente no intervalo `[0.0, 1.0]`.
2. Para qualquer lista com variação, o menor valor mapeia para `0.0` e o maior para `1.0`.

Esse mecanismo identificou e comprovou a falha de divisão por zero presente em `src/normalize_buggy.py`, evidenciando a necessidade de testes baseados em propriedades para validação de software robusto.
