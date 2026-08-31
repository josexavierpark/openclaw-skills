# raio-x-ad

Skill de Claude Code que faz o raio-x completo de um anúncio em vídeo, tudo de uma vez, num único relatório markdown.

Você aponta um vídeo (arquivo local ou URL). A skill assiste o vídeo de verdade: extrai frames inteligentes (troca de cena + hook denso + intervalo + fim) e transcreve o áudio via Groq Whisper com timestamps. Depois o Claude escreve o relatório.

## O relatório tem 5 seções

1. **Relatório visual:** formato, orientação, produção, personagens (com reconhecimento de celebridade local), hook em 4 camadas, provas visuais, texto na tela, símbolos carregados, pacote do editor.
2. **7 camadas + blueprint:** as 7 camadas macro do anúncio de resposta direta + os movimentos persuasivos.
3. **Transcrição:** verbatim no idioma original, com timestamps.
4. **Mapa de blocos:** 13 blocos canônicos com a primeira e a última fala de cada um.
5. **Tradução PT-BR:** quando a fonte está em outra língua.

## Requisitos

- `ffmpeg` e `ffprobe` (`brew install ffmpeg`)
- `python3`
- `yt-dlp` (só para URLs: `brew install yt-dlp`)
- Uma chave Whisper: `GROQ_API_KEY` (recomendado, gratuito em https://console.groq.com/keys) ou `OPENAI_API_KEY`. Coloque em `~/.config/raio-x-ad/.env`:
  ```
  GROQ_API_KEY=sua_chave_aqui
  ```
  Sem chave, a skill roda com `--no-transcribe` e entrega as seções 1 e 2.

Verifique tudo com: `bash scripts/check-deps.sh`

## Uso

Invoque a skill e aponte o vídeo:

```
/raio-x-ad /caminho/do/anuncio.mp4
/raio-x-ad https://... (país: Brasil, nicho: diabetes)
```

O relatório sai numa pasta `~/Documents/Copywriting/Analises-Ads/<AAAA-MM-DD>_<slug>/`, junto com os frames e a transcrição. O arquivo principal é nomeado por característica do ad: `<AAAA-MM-DD>_<subnicho>_<slug-do-ad>.md` (ex: `2026-07-08_confeitaria-lucrativa_brigadeiros-florais.md`), pra se identificar sozinho fora da pasta.

## Como funciona por dentro

- `scripts/extract.py`: download + frames + Groq Whisper + manifest.
- `scripts/whisper_lib.py`: módulo Groq/OpenAI (stdlib puro, timestamps por segmento).
- `reference/`: os bancos das 7 camadas, o catálogo de movimentos e blocos, as pistas visuais, a diretriz de reconhecimento facial, as regras de estilo e dois exemplos trabalhados.
- `output-template.md`: o formato do relatório final.

Não depende de nenhuma outra skill. Portável.
