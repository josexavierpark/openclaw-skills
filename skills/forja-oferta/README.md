# Forja de Ofertas

Skill do Claude Code que conduz a construção de briefings completos de oferta e VSL em PT-BR, antes da primeira palavra de copy ser escrita. Cobre 14 playbooks (00A Pesquisa Operacional + 13 playbooks teóricos) organizados em 6 módulos: Pré-Campo, Pré-Briefing, Estratégia, Mecanismos, Linguagem, Oferta e Estrutura da VSL.

A skill funciona em dois modos:

- **Modo completo:** percorre tudo, do 00A ao 13, gerando briefing completo salvo em disco
- **Modo cirúrgico:** ativa peças isoladas (nome chiclete, mecanismo, USP, oferta, VSL) sem exigir briefing completo

Todas as sugestões saem de bancos com cases reais documentados (Diabetox, Truque da Banana, Pilates Asiático, Fórmula Amazon, etc.). Nenhum exemplo é fabricado. Todo output passa por um filtro Anti-AI-Slop antes de chegar ao usuário.

---

## Instalação

### Pré-requisito

Ter o [Claude Code](https://claude.com/claude-code) instalado e funcionando.

### Mac e Linux

1. Salve o arquivo `forja-oferta.zip` na pasta Downloads
2. Abra o Terminal e cole:

```bash
mkdir -p ~/.claude/skills
cd ~/.claude/skills
unzip ~/Downloads/forja-oferta.zip
```

3. Reinicie o Claude Code (ou abra uma nova conversa)

### Windows (via WSL ou Git Bash)

Mesmo processo, ajustando o caminho da pasta Downloads conforme seu sistema.

### Verificar instalação

Em uma conversa do Claude Code, digite:

```
/forja-oferta
```

Se a skill foi carregada corretamente, Claude vai responder com a abertura conversacional da Forja.

---

## Como usar

### Modo completo (briefing inteiro)

```
/forja-oferta
```

Claude conduz você do 00A ao 13, salvando cada resposta automaticamente em `~/Documents/Copywriting/Briefings/<nome-do-produto>/`. Pode pausar e retomar a qualquer momento.

### Modo cirúrgico (peça específica)

| Comando | Saída |
|---|---|
| `/forja-oferta pesquisa` | Dossiê de pesquisa operacional (5 frentes) |
| `/forja-oferta avatar` | Avatar real + nível de consciência + sofisticação |
| `/forja-oferta diagnostico` | Dores, desejos, inimigos, objeções, falsas soluções |
| `/forja-oferta tese` | Tese de marketing com gradualização |
| `/forja-oferta paradoxo` | Perguntas paradoxais |
| `/forja-oferta big-idea` | Big Idea + One Belief |
| `/forja-oferta mecanismo-problema` | Mecanismo do Problema + Ação Acreditável |
| `/forja-oferta mecanismo-solucao` | Mecanismo da Solução + Solução Acreditável |
| `/forja-oferta mecanismo` | Os dois mecanismos juntos |
| `/forja-oferta nome` | 10 nomes chicletes + critérios + teste seco |
| `/forja-oferta usp` | 3 versões de USP + Carta de 16 Palavras |
| `/forja-oferta oferta` | Big Offer (9 elementos) + 7 Perguntas |
| `/forja-oferta vsl` | Estrutura completa de lead/VSL (4 e 10 perguntas) |

### Modos especiais

| Comando | Função |
|---|---|
| `/forja-oferta exemplo` | Mostra o briefing-diabetox.md preenchido como referência |
| `/forja-oferta validar` | Roda checklist em briefing existente, mostra pendências |
| `/forja-oferta consolidar` | Gera `99-CONSOLIDADO.md` com tudo que foi preenchido |
| `/forja-oferta ajuda` | Lista todos os comandos disponíveis |

### Linguagem natural

Você também pode ativar sem digitar comando, basta descrever o que quer:

> "Quero criar um briefing de oferta nova"
>
> "Me ajuda a definir nome chiclete pra um suplemento de diabetes"
>
> "Construir oferta nova para curso de inglês com ticket R$497"

---

## Estrutura da skill

```
forja-oferta/
├── SKILL.md                          (orquestração principal)
├── README.md                         (este arquivo)
├── modos-cirurgicos.md               (detalhe dos argumentos de ativação)
├── comportamentos-por-playbook.md    (regras específicas por playbook)
├── playbooks/                        (00A + 13 playbooks teóricos)
│   ├── 00-INDICE-MESTRE.md
│   ├── 00A-Pesquisa-Operacional.md
│   ├── 01-Inteligencia-de-Mercado.md
│   ├── ... (até o 13)
├── prompts/
│   ├── INDEX.md                      (índice dos bancos)
│   ├── filtro-anti-ai-slop.md        (filtro obrigatório aplicado a todo output)
│   └── banco-*.md                    (9 bancos de cases reais)
├── templates/                        (briefing-vazio, status, consolidado)
└── examples/
    └── briefing-diabetox.md          (case real preenchido como referência)
```

---

## Convenções de estilo aplicadas

Todo output da skill respeita:

- PT-BR brasileiro com acentuação correta
- Zero em-dash (—). Uso de `:`, `.`, `,`, `()`, `;` ou "a" para ranges
- Zero fórmula "Não é X, é Y"
- Vocabulário sóbrio e funcional
- Sem citação de nomes de autores ou métodos batizados
- Filtro Anti-AI-Slop bloqueando palavras-vício de IA, fórmulas proibidas e padrões artificiais

---

## Onde os briefings ficam salvos

```
~/Documents/Copywriting/Briefings/<nome-do-produto>/
├── 00-CONTEXTO.md
├── 00-STATUS.md
├── 00A-Pesquisa-Operacional.md
├── 01-Inteligencia-de-Mercado.md
├── ... (um arquivo por playbook)
└── 99-CONSOLIDADO.md                 (gerado ao final pelo modo consolidar)
```

A pasta é criada automaticamente no primeiro briefing.

---

## Atualizações

Para atualizar para uma nova versão, basta reextrair o zip por cima da pasta existente. Os briefings em `~/Documents/Copywriting/Briefings/` não são afetados.

---

## Suporte

Em caso de dúvida, abra uma conversa no Claude Code e pergunte:

> "Como funciona a skill forja-oferta?"

Claude vai consultar o SKILL.md e te orientar.
