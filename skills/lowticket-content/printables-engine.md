# Printables Engine: gerar entregáveis imprimíveis por código

Use quando o entregável é um artefato **visual/imprimível** (fichas de atividade, flashcards, certificados, planners, pôsteres), e não texto corrido. Gere por **código** para sair exato, com variação infinita (por semente), 100% próprio e reproduzível a **0 tokens por mudança**. É o mesmo princípio do conversor Markdown→app: quem gera o dado é o código, não a IA.

## Motor (sem bibliotecas externas)

- Monte cada página como **HTML + SVG inline** e renderize para PDF com **Chrome headless**. Caminho no macOS:
  ```bash
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
    --no-pdf-header-footer --print-to-pdf="saida.pdf" "pagina.html"
  ```
- Uma página A4 = um `div.page` com `@page{size:A4;margin:0}`, largura 210mm, altura 297mm.
- **Anatomia fixa** de cada ficha: cabeçalho (marca + badge da categoria + código único), título, **uma** instrução curta, corpo, caixa "dica" (voz de especialista ajudando quem aplica, nunca recado para a IA), rodapé (nome/data + código).
- Varie por `seed` (`random.Random(seed)`): infinitas fichas únicas de um gerador só.
- Estrutura sugerida: `base.py` (template + render + catálogo), `icones.py` (biblioteca SVG própria), `comum.py` (geradores compartilhados), `build_<categoria>.py` (um por grupo) chamando um `run_category(...)` comum.

**Refinos do motor (entregável com foto / marca):**
- **Fontes embutidas em base64** (`@font-face` com `data:font/woff2;base64,…`): baixe do Google Fonts **uma
  vez**, converta cada `url()` para base64, cacheie o `fonts.css`. Depois o build é offline e o render é
  idêntico sempre (não depende da rede).
- **Foto WebP → JPEG leve antes de embutir** (`sips -s format jpeg -s formatOptions 72 --resampleWidth 1000`):
  o Chrome embute o JPEG via DCT direto e o PDF cai de ~18 MB → ~5 MB (embutir WebP fica bem mais pesado).
  Flags que importam: `--headless=new --no-pdf-header-footer --allow-file-access-from-files
  --run-all-compositor-stages-before-draw --virtual-time-budget=20000`.
- **Tema de impressão CLARO mesmo se o app for dark:** o PDF é baixado e impresso → tema "papel" (fundo claro,
  tinta escura, acento da marca) seguindo o design system, não o tema escuro do app (queima tinta). Fundo claro
  de ponta a ponta: `@page{margin:…}` + camada `position:fixed; inset:0` na cor do papel + `print-color-adjust: exact`.

## Biblioteca de ativos própria (fuja da armadilha de licença)

- Grátis não é licença comercial. Pegar "printable grátis" de Pinterest/TPT e revender é violação. Fontes seguras: CC0/domínio público, packs de licença comercial, ou PLR/MRR (feitos para revender). Mais seguro e consistente: **desenhe sua própria biblioteca de ícones SVG** uma vez (contorno arredondado, fofo) e reutilize: sem risco jurídico, um só estilo de casa, escalável, P&B perfeito.
- Guarde cada ícone como SVG interno num viewBox 0..100; um wrapper aplica traço/preenchimento/tamanho. Curador ~20 a 40 (animais, objetos, formas, carinhas de emoção).

## Checklist de impressão (rode antes de entregar)

- A4 (ou Carta), **uma atividade por página**, muito espaço em branco, elementos grandes.
- P&B para economizar tinta (ou cor, se o produto é "colorido"). **Evite emoji**: renderiza como emoji colorido e quebra o P&B. Use unicode geométrico ou SVG desenhado.
- **Verifique a contagem de páginas**: toda ficha individual deve ter exatamente 1 página (pega overflow).
- Fontes com acento correto (norma culta). Confirme que o acento realmente renderizou.
- **Decodifique entidades HTML** antes de gravar no catálogo/JSON (nada de `&ccedil;` vazando).

```bash
# Toda ficha individual = 1 pagina (cadernos multipagina sao esperados)
python3 - <<'PY'
import re,glob,os
for f in glob.glob("fichas/**/*.pdf",recursive=True):
    d=open(f,"rb").read(); c=[int(m.group(1)) for m in re.finditer(rb"/Count\s+(\d+)",d)]
    n=max(c) if c else 0; nm=os.path.basename(f)
    if "-00_" in nm: continue
    if n!=1: print("OVERFLOW",n,nm)
print("ok")
PY
```

## Auditoria funcional (além da anti-alucinação)

Texto se audita contra as fontes. Uma **atividade gerada** também precisa de auditoria de **lógica**:
- Labirinto: existe um único caminho que vai do início ao fim.
- Pareamento / "ache o par": existe exatamente uma resposta; distratores não casam por acidente.
- Contagem / "quantos tem": a resposta é inequívoca (nenhuma forma que se lê de dois jeitos).
- Sequência / padrão: a regra é real e a lacuna tem uma resposta só.
- Grade lógica (sudoku/latina): válida e as opções mostradas incluem a certa.

Renderize uma amostra de cada tipo e **leia de volta** (Read no PDF) antes de escalar. Bugs reais pegos assim: um "ache o par" insolúvel; uma contagem de formas ambígua (retângulos lidos como quadrados).

## Catálogo como fonte única da verdade

Um `catalogo.json` alimenta **o gerador e o app**: por item `{codigo,titulo,categoria,foco,tipo,grupo,idade,nivel,arquivo}` + `cadernos` (PDF "imprimir o caderno inteiro" por grupo) + `premium`. O app lê isso para progresso/gamificação. 0 tokens por mudança de conteúdo. Código no rodapé da ficha = a chave que liga ficha → catálogo → app.

## Um parser único alimenta app E livro PDF (não reimplemente)

Quando o produto também vira um **livro/apostila PDF** a partir de conteúdo de **prosa** (não fichas), **reuse
o mesmo parser** que gera o `data.js`/JSON do app — importe-o, não reescreva. Assim app e PDF saem com a
**mesma fidelidade, o mesmo `scrub` e a mesma resolução de xref**; parsers separados divergem (um limpa
bastidor, o outro não).

- Em Python: `importlib.util.spec_from_file_location` carrega o módulo do conversor; chame o `parse_file()`
  dele dentro do gerador de PDF.
- **Custo:** gerar o livro a partir do conteúdo já escrito é **mecânico → ~0 token**. Nunca peça à IA para
  "diagramar/formatar cada item" (≈30× mais caro e arrisca alterar o conteúdo) — quem diagrama é o template, e
  a regeneração após cada edição volta a custar 0.
- **Auditoria do PDF de prosa:** gere **uma** amostra (1 coleção/módulo), dê **Read no PDF** e aprove a cara
  (capa, sumário, um item, um guia) e cheque overflow/corte/página em branco — só então rode o lote. É a versão
  "para prosa" da auditoria funcional que este modo já faz para atividades.

## Camada premium colorida via IA de imagem (vitrine / upsell), com ressalvas duras

Para mockup da página de vendas, flipbook e um upsell colorido, gere versões bonitas com modelo de imagem (ex.: Magnific MCP, modelo `imagen-nano-banana-2` / Nano Banana Pro; ratio 3:4 para A4; 2k = 1792x2400, ~205 dpi; nesse modelo 2k custa o mesmo que 1k). Fluxo: `images_generate` → `creations_wait` → `curl` na url → conferir `sips -g pixelWidth -g pixelHeight` e dar Read na imagem.

- A IA acerta tipos **visuais** (achar/circular, contar, parear, sombra, ordenar por tamanho, cena, tabuleiro, cartas, certificado, carinhas, respiração, rotina).
- A IA **não é confiável** em lógica rígida (labirinto, liga-pontos numerado, grade lógica): fica bonito, não solucionável. Esses ficam só no código P&B.
- Ela **derruba acentos** às vezes e erra numeração de sequência. Verifique cada uma; reenvie no erro intermitente "invalid argument" e no falso positivo "NSFW".

## Handoff (produtos done-for-you)

Escreva um `HANDOFF.md`: resumo do produto, estado atual com contagens, mapa de pastas, como regenerar (comandos exatos + dependências), esquema de códigos, schema do catálogo, pipeline premium + ressalvas, as regras duras do projeto, próximos passos. Permite que outra pessoa ou IA assuma do zero.
