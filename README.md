# normalize_batch — Exercício de TDD + Property-Based Testing

## Como rodar
```
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

## Estrutura
- `src/normalize.py` — implementação final (correta), fruto do ciclo TDD.
- `src/normalize_buggy.py` — versão propositalmente bugada, usada só para provar
  que o teste de propriedade pega bugs reais.
- `tests/test_normalize.py` — teste de exemplo original (fase GREEN do TDD).
- `tests/test_normalize_edge_cases.py` — testes de exemplo para os casos-limite.
- `tests/test_normalize_property.py` — testes de propriedade (Hypothesis) contra a versão correta.
- `tests/test_prova_bug_real.py` — mesmo teste de propriedade rodado contra a versão bugada (deve falhar).
- `DESIGN.md` — decisões de design (NaN, inf, divisão por zero, empates).
- `evidencia_*.txt` — saídas reais do pytest em cada fase (red/green/refactor/prova do bug).

## Histórico de commits (ciclo TDD)
```
red      -> adiciona teste para normalize_batch (falha - função não existe)
green    -> implementação mínima de normalize_batch (min-max scaling)
refactor -> trata lista vazia, NaN/inf e empate (max==min); adiciona testes de propriedade
prova    -> versão bugada (sem tratar max==min) falha no teste de propriedade
```
Ver `git log` para os commits reais.
