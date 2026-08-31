#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validador métrico da fala-simples.

Mede um roteiro de vídeo contra o spec numérico destilado de um corpus real
(28 roteiros de resposta direta, 6.310 palavras faladas) e devolve um diff
alvo a alvo, com as frases ofensoras nomeadas.

Uso:
    python3 validar.py roteiro.txt
    python3 validar.py roteiro.txt --lexico fitness
    cat roteiro.txt | python3 validar.py -
    python3 validar.py roteiro.txt --json

Saída: relatório legível + exit code 1 se algum alvo bloqueante falhar.
"""
import sys, os, re, json, argparse, statistics, unicodedata, collections

DIR = os.path.dirname(os.path.abspath(__file__))
LEXDIR = os.path.join(os.path.dirname(DIR), 'lexicos')

# ---------------------------------------------------------------- utilidades

def normaliza(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower())
                   if unicodedata.category(c) != 'Mn')

def palavras(t):
    return re.findall(r"[0-9A-Za-zÀ-ÿ]+", t)

def frases(t):
    t = re.sub(r'\s+', ' ', t).strip()
    bruto = re.split(r'(?<=[.!?…])\s+', t)
    return [f.strip() for f in bruto if len(palavras(f)) >= 1]

def pc(n, d):
    return 0.0 if not d else 100.0 * n / d

# ---------------------------------------------------------------- léxico

def carrega_lexico(nome):
    p = os.path.join(LEXDIR, f'{nome}.json')
    if not os.path.exists(p):
        disp = sorted(f[:-5] for f in os.listdir(LEXDIR) if f.endswith('.json'))
        sys.exit(f"léxico '{nome}' não existe. Disponíveis: {', '.join(disp)}")
    return json.load(open(p, encoding='utf-8'))

# ---------------------------------------------------------------- medidas

SUBORD = r'\b(que|porque|quando|se|onde|embora|enquanto|cujo|cuja|qual|caso|pois|conforme|ainda que|apesar de)\b'
# Estes dois rodam no texto COM acento (minúsculo), não na versão normalizada:
# o acento é justamente o que torna o futuro sintético inconfundível, e sem ele
# "-erá" viraria "-era", que colide com considera, espera, prospera.
ABERTURA_FALA = r'^(e|mas|então|aí|ah|olha|pô|sabe|cara|mano|pois é|agora|e aí|só que|aliás)\b'
FUT_SINTETICO = r'\b\w{2,}(ará|erá|irá|arão|erão|irão|aremos|eremos|iremos)\b'
# Substantivos que terminam nas mesmas sílabas do futuro sintético sem serem
# verbos. "quarteirão" termina em "irão" e era acusado como futuro. A lista é
# curta de propósito: "serão" e "verão" ficam de fora porque são futuro de ser
# e de ver, e o falso positivo deles é preferível ao falso negativo.
NAO_FUTURO = {'quarteirão', 'furacão', 'escadão'}
PERIFRASE = r'\b(vai|vão|vou|vamos)\s+\w+(ar|er|ir)\b'
# Apêndice de fala: a muleta colada no fim da oração ("né?", "sabe?", "viu?").
# Casa o USO, não a palavra: "do jeito certo." e "pra quem não sabe," ficam de fora.
APENDICE = (r'(?<![0-9a-zà-ÿ])(?<!não )(?<!nao )(né|viu|sabe|tá|entendeu|hein|certo|beleza|ok)\s*\?'
            r'|,\s*(né|viu|sabe|tá)\s*,'
            r'|(?<![0-9a-zà-ÿ])ó(?![0-9a-zà-ÿ])')   # "ó" solto: ruído, não marcador

# --- scanners das 12 Diretrizes: listam ocorrências, não reprovam ---
# Nenhum vira alvo binário porque os três erram muito sozinhos: "complemente" é
# verbo e não advérbio, "o treino é personalizado" é adjetivo e não voz passiva,
# e "você pode ter um corpo como esse" é o hook do corpus, não hesitação.
D12_FRACO = r'\b(pode|poderia|talvez|quase|geralmente|mais ou menos|aproximadamente|às vezes|em média|possivelmente|provavelmente)\b'
D8_ADV    = r'\b\w+mente\b'
D2_PASSIVA = r'\b(foi|foram|era|eram|será|serão)\s+\w+[ai]d[oa]s?\s+(por|pelo|pela|pelos|pelas)\b'

def mede(texto, lex):
    F = frases(texto)
    W = palavras(texto)
    n_frases, n_pal = len(F), len(W)
    if n_frases == 0 or n_pal == 0:
        sys.exit("texto vazio.")
    tam = [len(palavras(f)) for f in F]
    low = normaliza(texto)          # sem acento: só para a checagem de subordinação
    acc = texto.lower()             # com acento: léxico, futuro sintético, abertura, apêndice

    imperativos = lex['imperativos']
    orais = lex['marcadores_orais']
    concretos = lex['concretos']
    abstratos = lex['abstratos']

    def conta_termos(lista):
        # Casa COM acento, contra o texto acentuado. Sem isso, "ó" (interjeição)
        # vira "o" e casa com todo artigo definido do roteiro, inflando a contagem
        # de marcadores em quase 3x. Foi o bug que fez o alvo nascer alto demais.
        tot, achados = 0, []
        for termo in lista:
            n = len(re.findall(r'(?<![0-9a-zà-ÿ])' + re.escape(termo.lower()) + r'(?![0-9a-zà-ÿ])', acc))
            if n:
                tot += n
                achados.append((termo, n))
        return tot, sorted(achados, key=lambda x: -x[1])

    n_imp, l_imp = conta_termos(imperativos)
    n_oral, l_oral = conta_termos(orais)
    n_conc, l_conc = conta_termos(concretos)
    n_abst, l_abst = conta_termos(abstratos)

    curtas = [f for f, t in zip(F, tam) if t <= 10]
    sem_sub = [f for f in F if not re.search(SUBORD, normaliza(f))]
    abre_fala = [f for f in F if re.match(ABERTURA_FALA, f.lower().lstrip('"“‘ '))]
    longas4 = [w for w in W if len(w) <= 4]
    compridas = [w for w in W if len(w) >= 13]
    fut_s = [m.group(0) for m in re.finditer(FUT_SINTETICO, acc)
             if m.group(0) not in NAO_FUTURO]
    peri = re.findall(PERIFRASE, acc)
    apend = [m.group(0).strip() for m in re.finditer(APENDICE, acc)]

    # Legibilidade (D2, D3, D6 das 12 Diretrizes). Só entram as fórmulas que o
    # corpus real cumpre; ver reference/08-diretrizes.md para as rejeitadas.
    def silabas(w): return max(1, len(re.findall(r'[aeiouáéíóúâêôãõàü]+', w)))
    n_letras = sum(len(w) for w in W)
    n_sil = sum(silabas(w) for w in W)
    ppf = n_pal / n_frases
    spw = n_sil / n_pal
    lpw = n_letras / n_pal
    gulpease = 89 + (300 * n_frases - 10 * n_letras) / n_pal
    flesch = 248.835 - 1.015 * ppf - 84.6 * spw
    ari = 4.71 * lpw + 0.5 * ppf - 21.43
    perguntas = 100.0 * sum(1 for f in F if f.strip().endswith('?')) / n_frases
    sc_fraco = [m.group(0) for m in re.finditer(D12_FRACO, acc)]
    sc_adv = [m.group(0) for m in re.finditer(D8_ADV, acc)]
    sc_pass = [m.group(0) for m in re.finditer(D2_PASSIVA, acc)]

    # Densidade de subordinação e empilhamento nominal. É aqui que texto escrito
    # se disfarça de falado: passa em tamanho de frase e ainda soa complicado.
    n_que = len(re.findall(r'\bque\b', acc))
    n_de = len(re.findall(r'\bde\b', acc))
    n_doispontos = texto.count(':')
    pct_longas21 = 100.0 * sum(1 for t in tam if t >= 21) / n_frases

    return dict(
        n_frases=n_frases, n_pal=n_pal, F=F, tam=tam,
        media=statistics.mean(tam),
        desvio=statistics.pstdev(tam) if n_frases > 1 else 0.0,
        pct_curtas=pc(len(curtas), n_frases),
        pct_sem_sub=pc(len(sem_sub), n_frases),
        pct_abre_fala=pc(len(abre_fala), n_frases),
        pct_ate4=pc(len(longas4), n_pal),
        pct_13mais=pc(len(compridas), n_pal),
        compridas=sorted(set(compridas)),
        fut_sintetico=len(fut_s), perifrase=len(peri),
        n_apendice=len(apend), l_apendice=collections.Counter(apend).most_common(6),
        gulpease=gulpease, flesch=flesch, ari=ari, perguntas=perguntas,
        que_por_100=100.0*n_que/n_pal, de_por_100=100.0*n_de/n_pal,
        n_doispontos=n_doispontos, pct_longas21=pct_longas21,
        sc_fraco=collections.Counter(sc_fraco).most_common(8),
        sc_adv=collections.Counter(sc_adv).most_common(8),
        sc_pass=collections.Counter(sc_pass).most_common(5),
        imp_por_100=100.0 * n_imp / n_pal, n_imp=n_imp, l_imp=l_imp[:8],
        oral_por_100=100.0 * n_oral / n_pal, n_oral=n_oral, l_oral=l_oral[:8],
        n_conc=n_conc, n_abst=n_abst, l_abst=l_abst[:8],
        razao_conc=(n_conc / n_abst) if n_abst else (float('inf') if n_conc else 0.0),
        primeira=F[0], ultima=F[-1],
        tam_primeira=tam[0], tam_ultima=tam[-1],
        tam_penultima=tam[-2] if n_frases > 1 else 0,
    )

# ---------------------------------------------------------------- alvos

def alvos(m, lex, produto=None):
    """Cada alvo: (chave, rótulo, valor medido, texto do alvo, passou?, bloqueante?)

    Calibração: rodei estas medidas nos 26 roteiros falados do corpus de origem e olhei
    a distribuição por roteiro, não a média agregada. Os alvos BLOQUEANTES são as métricas
    que o corpus cumpre em praticamente todos os roteiros (a assinatura do estilo). As
    métricas dispersas viram AVISO, com a faixa observada no rótulo, porque reprovar por
    elas reprovaria os próprios originais.
    """
    A = []
    add = lambda *a: A.append(a)

    # --- assinatura (bloqueante): o corpus cumpre em ~todos os roteiros ---
    add('ate4', 'Palavras de até 4 letras', f"{m['pct_ate4']:.1f}%", '>= 50%', m['pct_ate4'] >= 50, True)
    add('longas', 'Palavras com 13+ letras', f"{m['pct_13mais']:.1f}%", '<= 2,5%', m['pct_13mais'] <= 2.5, True)
    add('futuro', 'Futuro sintético (fará, terá)', f"{m['fut_sintetico']} ocorrência(s)", '0', m['fut_sintetico'] == 0, True)
    r = m['razao_conc']
    add('concreto', 'Concreto por abstração', ('sem abstração' if r == float('inf') else f"{r:.1f} : 1"),
        '>= 10 : 1', r >= 10, True)
    # Apêndice de fala é regra da casa, mais estrita que o corpus (que tem 17 em 26
    # roteiros). O usuário não quer a muleta, e ela é a forma mais barata de simular
    # oralidade sem escrever falado de verdade.
    add('apendice', 'Muletas de fala: né? sabe? ó (casa)', f"{m['n_apendice']}", '0', m['n_apendice'] == 0, True)
    # D3 e D2 das 12 Diretrizes. Adotadas porque o corpus real cumpre as duas
    # em 25 dos 26 roteiros. As outras fórmulas do documento foram rejeitadas:
    # ver reference/08-diretrizes.md.
    add('gulpease', 'Gulpease, leitura fácil (D3)', f"{m['gulpease']:.0f}", '>= 55', m['gulpease'] >= 55, True)
    add('flesch', 'Flesch adaptado ao PT (D2)', f"{m['flesch']:.0f}", '>= 50', m['flesch'] >= 50, True)
    # Piso recalibrado: o antigo (>= 2,5) nasceu da contagem inflada pelo bug do "ó"
    # e reprovava 12 dos 26 originais. >= 1,0 é atingido por 22 dos 26.
    add('oral', 'Marcadores orais por 100 palavras', f"{m['oral_por_100']:.2f}", '>= 1,0', m['oral_por_100'] >= 1.0, True)
    add('imper', 'Imperativos por 100 palavras', f"{m['imp_por_100']:.2f}", '>= 1,0', m['imp_por_100'] >= 1.0, True)
    # Subordinação: o corpus fica em 2,18 "que" por 100 palavras (p75 = 3,21).
    # Texto escrito passa fácil no tamanho de frase e trava aqui.
    add('que', 'Densidade de "que" (casa)', f"{m['que_por_100']:.2f}", '<= 3,2', m['que_por_100'] <= 3.2, True)
    # Dois-pontos: regra da casa. A evidência do corpus é fraca (a pontuação da
    # transcrição é do Whisper, não do apresentador), mas o princípio é sólido:
    # quem fala não produz dois-pontos, produz pausa e frase nova.
    add('doispontos', 'Dois-pontos (casa)', f"{m['n_doispontos']}", '0', m['n_doispontos'] == 0, True)
    add('media', 'Tamanho médio da frase', f"{m['media']:.1f} palavras", '13 a 20', 13 <= m['media'] <= 20, True)
    add('desvio', 'Desvio do tamanho (alternância)', f"{m['desvio']:.1f}", '>= 5,5', m['desvio'] >= 5.5, True)

    # --- faixa (aviso): o corpus varia muito, o alvo é orientação ---
    add('curtas', 'Frases de até 10 palavras', f"{m['pct_curtas']:.1f}%", '20% a 50%', 20 <= m['pct_curtas'] <= 50, False)
    add('semsub', 'Frases sem oração encaixada', f"{m['pct_sem_sub']:.1f}%", '>= 28%', m['pct_sem_sub'] >= 28, False)
    add('abrefala', 'Frases abrindo com E/Mas/Então/Aí/Ah', f"{m['pct_abre_fala']:.1f}%", '>= 10%', m['pct_abre_fala'] >= 10, False)
    add('hook', 'Primeira frase (o hook)', f"{m['tam_primeira']} palavras", '<= 30', m['tam_primeira'] <= 30, False)
    add('fecho', 'Última frase (o tapa)', f"{m['tam_ultima']} palavras", '<= 5', m['tam_ultima'] <= 5, False)
    add('cta', 'Penúltima frase (o CTA)', f"{m['tam_penultima']} palavras", '6 a 45',
        6 <= m['tam_penultima'] <= 45, False)
    add('ari', 'ARI, leiturabilidade (D6)', f"{m['ari']:.1f}", '< 10', m['ari'] < 10, False)
    add('perg', 'Frases interrogativas (D7)', f"{m['perguntas']:.0f}%", '<= 35%', m['perguntas'] <= 35, False)
    add('de', 'Densidade de "de" por 100 pal.', f"{m['de_por_100']:.2f}", '<= 3,6', m['de_por_100'] <= 3.6, False)
    add('longas21', 'Frases com 21+ palavras', f"{m['pct_longas21']:.0f}%", '<= 35%', m['pct_longas21'] <= 35, False)
    if produto:
        nomeia = normaliza(produto) in normaliza(m['primeira'])
        add('hooknome', 'Hook não nomeia o produto', 'nomeia' if nomeia else 'não nomeia', 'não nomeia', not nomeia, False)
    tem_preco = bool(re.search(r'r\$|\d+,\d{2}|\breais\b', normaliza(m['primeira'])))
    add('hookpreco', 'Hook não cita preço', 'cita' if tem_preco else 'não cita', 'não cita', not tem_preco, False)
    return A

TIER1 = ["outrossim", "vale ressaltar", "e importante destacar", "e importante notar", "em suma",
         "dessa forma", "consequentemente", "em conclusao", "ademais", "posteriormente",
         "adicionalmente", "alem disso", "portanto", "no entanto", "furthermore", "moreover",
         "clique aqui", "saiba mais", "comece sua jornada", "garanta seu acesso", "adquira agora",
         "descubra agora", "transforme sua vida", "aproveite essa oportunidade",
         "voce sabia que", "e se eu te dissesse", "nos dias de hoje", "voce ja se perguntou",
         "a verdade que ninguem te conta"]
TIER2 = ["jornada", "mergulhar", "alavancar", "empoderar", "fomentar", "transformador",
         "holistico", "robusto", "abrangente", "ecossistema", "paradigma", "sinergia",
         "catalisador", "potencializar", "capacitar", "revolucionar"]

# "Saiba mais" e "clique aqui" são CTAs fracas quando o roteiro as usa como a própria
# chamada. Quando vêm precedidas de "em/no/botão", estão NOMEANDO o botão da plataforma
# ("toca em Saiba Mais"), que é obrigatório em anúncio de Meta e não é escolha de copy.
NOME_DE_BOTAO = r'(?:\bem|\bno|\bbot[ãa]o|\bbotao)\s+(?:o\s+)?$'

def blocklist(texto):
    low = normaliza(texto)
    achados = []
    if '—' in texto or '--' in texto:
        achados.append(('em-dash', texto.count('—') + texto.count('--')))
    for p in re.finditer(r'\bnao e [^.,;!?]{2,40},? e \b', low):
        achados.append(('fórmula "não é X, é Y"', 1))
    for t in TIER1 + TIER2:
        rx = r'(?<![0-9a-zà-ÿ])' + re.escape(t) + r'(?![0-9a-zà-ÿ])'
        n = 0
        for mt in re.finditer(rx, low):
            if t in ('saiba mais', 'clique aqui') and re.search(NOME_DE_BOTAO, low[:mt.start()]):
                continue                       # está nomeando o botão, não sendo a CTA
            n += 1
        if n:
            achados.append((t, n))
    return achados

# ---------------------------------------------------------------- relatório

def relatorio(m, A, bl, lex_nome, mostrar_frases=True):
    L = []
    ok = sum(1 for a in A if a[4])
    L.append("=" * 74)
    L.append(f"  VALIDAÇÃO fala-simples   léxico: {lex_nome}   "
             f"{m['n_pal']} palavras / {m['n_frases']} frases")
    L.append("=" * 74)
    L.append(f"{'':2}{'ALVO':<38}{'MEDIDO':<18}{'ESPERADO':<14}")
    L.append("-" * 74)
    for chave, rotulo, medido, alvo, passou, bloq in A:
        marca = ' ok ' if passou else ('FALHA' if bloq else 'aviso')
        L.append(f"{marca:<2}{rotulo:<38}{medido:<18}{alvo:<14}")
    L.append("-" * 74)
    L.append(f"  {ok}/{len(A)} alvos atingidos")
    L.append("  (casa) = regra da casa, mais estrita que o corpus. Ver reference/02-spec.md")

    falhas = [a for a in A if not a[4] and a[5]]
    avisos = [a for a in A if not a[4] and not a[5]]

    if bl:
        L.append("")
        L.append("  BLOCKLIST (bloqueante):")
        for termo, n in bl:
            L.append(f"    - {termo} ({n}x)")

    if mostrar_frases:
        chaves = {a[0] for a in falhas}
        if 'desvio' in chaves or 'curtas' in chaves:
            L.append("")
            L.append("  Diagnóstico de ritmo (as 6 frases mais longas):")
            piores = sorted(zip(m['F'], m['tam']), key=lambda x: -x[1])[:6]
            for f, t in piores:
                L.append(f"    {t:>3}p  {f[:96]}")
            L.append("    Ação: quebre uma dessas em duas e ponha uma virada de 3 a 6 palavras entre elas.")
        if 'que' in chaves or 'de' in chaves:
            L.append("")
            L.append("  Frases mais carregadas de subordinação:")
            car = sorted(((len(re.findall(r'\b(que|de)\b', f.lower())), f) for f in m['F']), reverse=True)[:5]
            for n, f in car:
                L.append(f"    [{n}] {f[:96]}")
            L.append("    Ação: quebre em duas frases. Cada 'que' relativo vira ponto final.")
        if 'doispontos' in chaves:
            L.append("")
            L.append("  Frases com dois-pontos (troque por ponto final):")
            for f in m['F']:
                if ':' in f:
                    L.append(f"    {f[:96]}")
        if 'semsub' in chaves:
            L.append("")
            L.append("  Frases com oração encaixada (candidatas a virar duas frases):")
            for f in [x for x in m['F'] if re.search(SUBORD, normaliza(x))][:6]:
                L.append(f"    - {f[:96]}")
        if 'longas' in chaves and m['compridas']:
            L.append("")
            L.append(f"  Palavras compridas: {', '.join(m['compridas'][:12])}")
        if 'concreto' in chaves and m['l_abst']:
            L.append("")
            L.append(f"  Abstrações encontradas: {', '.join(f'{w} ({n}x)' for w, n in m['l_abst'])}")
            L.append("    Ação: troque cada uma por uma coisa que se vê, se toca ou se mede.")
        if 'apendice' in chaves:
            L.append("")
            L.append(f"  Apêndices encontrados: {', '.join(f'{w} ({n}x)' for w, n in m['l_apendice'])}")
            L.append("    Ação: apague. Eles simulam fala sem escrever falado, e a frase")
            L.append("    quase sempre fica melhor sem. Se faltar oralidade depois de tirar,")
            L.append("    ganhe com interjeição (pô, cara, mano) ou abertura (olha, se liga, aí).")
        if 'oral' in chaves:
            L.append("")
            L.append(f"  Marcadores orais presentes: {', '.join(f'{w} ({n}x)' for w, n in m['l_oral']) or 'nenhum'}")
            L.append(f"    Ação: precisa de ~{max(0, int(round(m['n_pal']*0.010)) - m['n_oral'])} marcador(es) a mais.")
            L.append("    Use interjeição ou abertura de atenção, nunca apêndice de fim de frase.")
        if 'imper' in chaves:
            L.append("")
            L.append(f"    Ação: precisa de ~{max(0, int(round(m['n_pal']*0.014)) - m['n_imp'])} imperativo(s) a mais.")
        if 'fecho' in chaves:
            L.append("")
            L.append(f"  Última frase tem {m['tam_ultima']} palavras: \"{m['ultima'][:80]}\"")
            L.append("    Ação: mova o conteúdo para a frase anterior e feche com 1 a 3 palavras.")
        if 'hook' in chaves:
            L.append("")
            L.append(f"  Hook tem {m['tam_primeira']} palavras: \"{m['primeira'][:90]}\"")

    scan = [('Baixa convicção (D12): pode, talvez, quase', m.get('sc_fraco')),
            ('Advérbios em -mente (D8)', m.get('sc_adv')),
            ('Voz passiva com agente (D2)', m.get('sc_pass'))]
    scan = [(rot, itens) for rot, itens in scan if itens]
    if scan:
        L.append("")
        L.append("  REVISAR (scanners das 12 Diretrizes: apontam, não reprovam)")
        for rot, itens in scan:
            L.append(f"    {rot}: {', '.join(f'{w} ({n}x)' for w, n in itens)}")
        L.append("    Julgue caso a caso. \"você pode ter um corpo como esse\" é promessa")
        L.append("    calibrada; \"o método pode te ajudar\" é hesitação. Só a segunda sai.")

    L.append("")
    if falhas or bl:
        L.append(f"  RESULTADO: REPROVADO ({len(falhas)} alvo(s) bloqueante(s)"
                 + (f" + {len(bl)} item(ns) de blocklist" if bl else "") + ")")
    elif avisos:
        L.append(f"  RESULTADO: APROVADO com {len(avisos)} aviso(s)")
    else:
        L.append("  RESULTADO: APROVADO")
    L.append("=" * 74)
    return '\n'.join(L), (not falhas and not bl)

# ---------------------------------------------------------------- cli

def main():
    ap = argparse.ArgumentParser(description="Valida um roteiro contra o spec da fala-simples.")
    ap.add_argument('arquivo', help="caminho do .txt/.md, ou '-' para stdin")
    ap.add_argument('--lexico', default='fitness', help="nome do léxico em lexicos/ (default: fitness)")
    ap.add_argument('--produto', default=None, help="nome do produto, para checar se o hook o nomeia")
    ap.add_argument('--json', action='store_true', help="saída em JSON")
    ap.add_argument('--quieto', action='store_true', help="só a tabela, sem diagnóstico")
    a = ap.parse_args()

    texto = sys.stdin.read() if a.arquivo == '-' else open(a.arquivo, encoding='utf-8').read()
    texto = re.sub(r'^\s*#.*$', '', texto, flags=re.M)          # tira headings de markdown
    texto = re.sub(r'\[[^\]]*\]', '', texto)                     # tira [marcações de cena]
    texto = re.sub(r'\*\*|__|\*', '', texto)

    lex = carrega_lexico(a.lexico)
    m = mede(texto, lex)
    A = alvos(m, lex, a.produto)
    bl = blocklist(texto)

    if a.json:
        print(json.dumps({
            'lexico': a.lexico, 'palavras': m['n_pal'], 'frases': m['n_frases'],
            'alvos': [{'chave': c, 'rotulo': r, 'medido': md, 'esperado': al,
                       'passou': p, 'bloqueante': b} for c, r, md, al, p, b in A],
            'blocklist': [{'termo': t, 'n': n} for t, n in bl],
            'aprovado': not [x for x in A if not x[4] and x[5]] and not bl,
        }, ensure_ascii=False, indent=1))
        sys.exit(0 if not [x for x in A if not x[4] and x[5]] and not bl else 1)

    txt, aprovado = relatorio(m, A, bl, a.lexico, mostrar_frases=not a.quieto)
    print(txt)
    sys.exit(0 if aprovado else 1)

if __name__ == '__main__':
    main()
