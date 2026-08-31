# Exemplos de referência

A skill-padrão-ouro de copy gerada neste padrão é a **copy-ads**:

```
(corpus local do autor, nao incluso no repo)
```

Quando precisar de um modelo concreto de skill bem feita, leia a copy-ads. Ela tem:

- Roteador fino com gates de preflight declarados (`COPADS_PREFLIGHT`)
- 9 fases especialistas (intake, disguise, retrieval, craft, hook, variants, critique, audit, polish)
- Restrições absolutas (a DNA aplicada)
- Few-shot BAD/GOOD de calibração de voz
- Formato de saída padronizado com metadata
- Banco de swipe consumido por path absoluto

**O que a forja-skill melhora em relação à copy-ads:**

- A DNA entra como duas camadas formais (card sempre ativo + completa sob demanda + sync), não embutida à mão.
- O `description` é corrigido para conter só gatilhos (a copy-ads ainda resume o workflow no campo).
- Toda skill nasce com o test-harness RED-GREEN-REFACTOR, que a copy-ads não tem.

Para um exemplo de skill de ingestão (não de geração), veja a **swipe-builder**, que mostra o padrão de gates de preflight aplicado a uma skill que só cataloga.
