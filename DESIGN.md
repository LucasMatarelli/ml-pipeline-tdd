# Decisões de Design — `normalize_batch`

Função escolhida: **normalização de lote (batch normalization)** usando
min-max scaling, que transforma qualquer lista de números para o
intervalo `[0.0, 1.0]`. É uma etapa muito comum em pipelines de ML antes
de treinar modelos sensíveis à escala das features (ex.: KNN, redes
neurais, regressão com regularização).

Fórmula: `(x - min) / (max - min)`

## Casos-limite e decisões tomadas

| Caso | Decisão | Justificativa |
|---|---|---|
| Lista vazia (`[]`) | Levanta `ValueError` | Não existe min/max de uma lista vazia; deixar o `min()`/`max()` do Python estourar `ValueError` genérico esconderia a causa real. Preferi validar explicitamente e dar uma mensagem clara. |
| `NaN` em qualquer posição | Levanta `ValueError` | `NaN` "contamina" comparações (`NaN < x` é sempre `False`), então min/max ficam indefinidos e o resultado seria silenciosamente incorreto. Melhor falhar alto e cedo (fail-fast) do que propagar `NaN` pro pipeline adiante. |
| `inf` / `-inf` em qualquer posição | Levanta `ValueError` | Um valor infinito quebra a escala inteira (tudo tenderia a 0 ou fica indefinido). Tratado como entrada inválida, igual ao `NaN`. |
| Todos os valores iguais (`max == min`, ex.: `[5, 5, 5]`) | Retorna `0.0` para todos | Dividir por zero não pode acontecer. Como não há variação nos dados, não existe uma "posição relativa" a calcular — `0.0` é a convenção escolhida (poderia ser `0.5` também; documentei a escolha para não ser ambígua). |
| Empates que **não** são o máximo/mínimo global (ex.: `[1, 5, 5, 9]`) | Comportamento natural da fórmula (ambos os `5` viram o mesmo valor normalizado) | Não é um caso especial: dois valores iguais na entrada devem gerar dois valores iguais na saída. A fórmula já garante isso sem tratamento extra. |
| Lista com 1 elemento (ex.: `[7]`) | Cai no caso `max == min` → retorna `[0.0]` | Um único valor não tem variação relativa; mesma lógica do empate total. |
| Tipos de entrada (`int` vs `float`) | Aceita ambos, mistura livre | Python já promove `int`/`float` automaticamente nas operações aritméticas usadas. |

## Por que teste de propriedade (Hypothesis) e não só exemplos?

Testes de exemplo (`assert normalize_batch([10,20,30]) == [...]`) só
provam que a função funciona *para aquele input específico*. Eles não
dizem nada sobre milhares de outras combinações possíveis (listas
grandes, valores negativos, um único elemento, muitos elementos iguais
etc.).

O Hypothesis gera automaticamente centenas de listas variadas — incluindo
casos extremos que um humano dificilmente pensaria em testar manualmente,
como `[0.0]` — e verifica se a invariante **"todo valor de saída está
entre 0.0 e 1.0"** continua verdadeira para qualquer uma delas. Foi
exatamente esse mecanismo que expôs o bug de divisão por zero na versão
`normalize_batch_buggy`, provando o valor prático de testes baseados em
propriedade além dos testes de exemplo.
