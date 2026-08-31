# Índice dos Bancos de Prompts

Bancos de exemplos reais usados pela skill `forja-oferta`. Todo case documentado foi extraído de material real (eBook 7P, Materiais Pré-Oferta, Livros, Arma, etc.), nunca fabricado.

## Bancos disponíveis

| Banco | Função | Quando consultar |
|---|---|---|
| `filtro-anti-ai-slop.md` | **Camada obrigatória** que valida todo output | Antes de qualquer entrega ao usuário |
| `banco-mecanismos-saude.md` | Cases reais de mecanismos em saúde, emagrecimento, beleza, diabetes | Playbooks 03, 05, 06, 07 |
| `banco-mecanismos-renda.md` | Cases reais de mecanismos em renda extra, MMO, investimentos | Playbooks 03, 05, 06, 07 |
| `banco-acoes-acreditaveis.md` | Ações Acreditáveis reais por nicho | Playbooks 06, 09 |
| `banco-nomes-chicletes.md` | Nomes reais documentados (Diabetox, Truque da Banana, Pilates Asiático, etc.) | Playbook 08, 06 (sexy cause) |
| `banco-metaforas-visuais.md` | Metáforas reais documentadas | Playbook 06 |
| `banco-provas-cientificas.md` | Autoridades, universidades, estudos reais | Playbooks 06, 07 |
| `banco-inimigos-comuns.md` | Vilões reais por nicho | Playbooks 02, 06 |
| `banco-authority-hooks.md` | Authority hooks reais com 8 formatos | Playbook 07 |
| `banco-transicoes-e-swipe.md` | Frases-cola e estruturas testadas | Playbooks 10, 11 |

## Regras de uso

1. **Toda sugestão sai de um banco.** Nunca invente um exemplo. Adapte de case real.
2. **Toda entrega passa pelo filtro.** Antes de mostrar ao usuário, rode `filtro-anti-ai-slop.md` mentalmente.
3. **Filtragem por nicho:** ao consultar um banco, filtre por nicho específico do usuário (saúde, renda, beleza) antes de propor opções.
4. **Cite o case que inspirou:** ao propor uma sugestão, sempre diga qual case real do banco virou a base ("estilo Diabetox", "estilo Fórmula Amazon").
5. **Quando não houver case exato:** mostre o case mais próximo e adapte junto com o usuário.

## Tabela cruzada playbook → banco

Para detalhes de qual banco usar em cada campo de cada playbook, ver `comportamentos-por-playbook.md` na raiz da skill.
