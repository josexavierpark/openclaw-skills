# Fase 7: Audit

Dois níveis: o que a máquina mede e o que só o julgamento pega.

## Nível 1: o validador (binário)

```bash
python3 ~/.claude/skills/fala-simples/scripts/validar.py rascunho.txt --lexico <nicho> --produto "<nome>"
```

Salve o rascunho num arquivo antes de rodar. Exit 0 aprova, exit 1 reprova.

O relatório traz, para cada falha, as frases ofensoras e a ação corretiva. **Corrija o texto, nunca o alvo.** Se você achar que um alvo está errado, a correção é recalibrar contra corpus real (ver [02-spec.md](02-spec.md)), não afrouxar o número para o rascunho passar.

Rode de novo depois de corrigir. Repita até passar ou até você conseguir justificar a exceção por escrito na entrega.

## Nível 2: os scans que a máquina não faz

Cada item é sim ou não. Um "não" manda de volta pro craft.

### Voz

1. Dá para ler o roteiro inteiro em voz alta sem tropeçar? Se você travou em alguma frase, ela ainda é escrita.
2. Os marcadores orais caem onde a fala pediria ênfase, ou foram salpicados para bater a métrica?
3. Tem alguma frase que você não diria para um amigo num áudio? Reescreva.
4. O vocabulário é do nicho certo, ou vazou do corpus de origem?

### Estrutura

5. O mecanismo do problema existe, e vem depois de uma frase-freio curta?
6. A falsa conclusão do espectador ("então é só fazer X") está escrita em voz alta antes de ser derrubada?
7. Tem uma anáfora, e só uma?
8. O hook foi escrito depois do corpo?
9. O CTA pede uma ação menor que a compra?

### Honestidade

10. Toda prova tem nome, número ou prazo vindo do usuário? Zero "muitos alunos", zero número inventado.
11. Toda escassez é verdadeira, ou pelo menos não é verificável como falsa?
12. Alguma afirmação é claim regulado (saúde, emagrecimento, renda) sem respaldo? Sinalize na entrega, não resolva sozinho.

### Anti-caricatura

13. Leia só os marcadores orais em sequência. Se a lista soa como imitação de humorista, você passou do ponto: corte um terço.
14. O roteiro seria distinguível de outro roteiro seu do mesmo nicho? Se todos ficam iguais, o motor virou molde.

## Formato de entrega

```
ROTEIRO
<o texto, uma frase por linha>

---
VALIDAÇÃO
<tabela do validar.py>

EXCEÇÕES
<alvo, motivo> ou "nenhuma"

SINALIZADO
<claims a conferir, provas a pedir> ou "nada"
```

Entregue sempre com a validação anexa. É ela que separa esta skill de um prompt de estilo.
