#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Slop Score para copy em PT-BR.

Porta o metodo do The Slop Index (theslopindex.com) para texto de venda em
portugues: mede a distancia entre uma copy e um corpus de copy humana que
vendeu, em quatro eixos mecanicos. Sem LLM julgando LLM.

Diferenca deliberada em relacao ao indice original: os dois eixos que o Opus 5
perde de verdade (concisao 31,6 e templating 58,4, os dois piores da tabela
dele) ganham peso, e templating so existe comparando ARQUIVOS DIFERENTES, de
tarefas nao relacionadas. Ninguem enxerga esqueleto reusado lendo um texto so.

Uso:
    slop_copy.py baseline <arquivos...> -o baseline.json
    slop_copy.py score <arquivos...> [--baseline baseline.json] [--json]
"""
import sys, os, re, json, math, argparse, statistics, unicodedata, collections
from itertools import combinations

PESOS = {'concisao': 0.35, 'templating': 0.30, 'ritmo': 0.20, 'tells': 0.15}

# ------------------------------------------------------------------ limpeza

def limpa(bruto):
    """Tira marcacao e anotacao de analise, deixa so a copy falada."""
    # imagem embutida em base64 dentro do .md vira 60 mil "palavras" porque o
    # +, o / e o = do base64 picotam o blob. Fora antes de qualquer medida.
    bruto = re.sub(r'data:[^;]+;base64,[A-Za-z0-9+/=\s]+', ' ', bruto)
    bruto = re.sub(r'[A-Za-z0-9+/]{60,}={0,2}', ' ', bruto)
    linhas = []
    for l in bruto.split('\n'):
        s = l.strip()
        if not s:
            linhas.append('')
            continue
        if s.startswith('#') or s.startswith('>') or s.startswith('|'):
            continue
        if s.startswith('---') or s.startswith('***'):
            continue
        if 'http://' in s or 'https://' in s or 'www.' in s:
            continue
        # metadado de arquivo de analise ("URL:", "Checkout:", "Plataforma:").
        # Sem isso o eixo tells acusa dois-pontos que ninguem escreveu na copy.
        mrot = re.match(r'^[\*\_]{0,2}([^:.!?]{1,40}):\s*\S', s)
        if mrot and len(palavras(mrot.group(1))) <= 5 and not re.search(r'[.!?]', s):
            continue
        # anotacao de bloco: [BLOCO 3], (nota: ...), **[LEAD]**
        if re.fullmatch(r'[\*\_\s]*\[[^\]]+\][\*\_\s]*', s):
            continue
        linhas.append(s)
    t = '\n'.join(linhas)
    t = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', t)   # links/imagens
    t = re.sub(r'[\*\_`~]+', '', t)                     # enfase
    t = re.sub(r'\\', '', t)
    t = re.sub(r'[ \t]+', ' ', t)
    return t

def paragrafos(t):
    return [p.strip() for p in re.split(r'\n\s*\n', t) if len(p.strip()) > 1]

def palavras(t):
    return re.findall(r"[0-9A-Za-zÀ-ÿ]+", t)

def frases(t):
    # em copy o corte de linha e uma pausa tao real quanto o ponto: cada linha
    # de VSL e uma batida. Quebrar so em [.!?] junta dez batidas numa frase de
    # 50 palavras e destroi a medida de ritmo.
    out = []
    for linha in t.split('\n'):
        linha = re.sub(r'[ \t]+', ' ', linha).strip()
        if not linha:
            continue
        for f in re.split(r'(?<=[.!?…])\s+', linha):
            f = f.strip()
            if len(palavras(f)) >= 1:
                out.append(f)
    return out

def norm(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower())
                   if unicodedata.category(c) != 'Mn')

# ------------------------------------------------------------------ lexico

# Vicios de IA em PT-BR. Fonte: anti-ia-blocklist.md deste projeto + os tells
# nomeados pelo proprio Slop Index traduzidos.
TELLS = [
    'mergulhar em','desbravar','alavancar','potencializar','revolucionar','fomentar',
    'nutrir','aproveitar ao maximo','desbloquear','desvendar','embarcar','desvelar',
    'elevar','otimizar','empoderar','navegar por','abracar','robusto','abrangente',
    'fluido','sem atrito','multifacetado','vibrante','intrincado','crucial','primordial',
    'matizado','profundo impacto','holistico','sinergia','paradigma','ecossistema',
    'jornada','panorama','tapecaria','no cenario atual','no mundo de hoje','vale ressaltar',
    'e importante notar','em suma','em resumo','por fim mas nao menos importante',
    'imagine so por um momento','vamos explorar','aqui estao','aqui esta','a verdade e que',
    'o segredo esta em','nao se trata apenas de','muito mais do que apenas',
    'seja voce','desde ate','tanto quanto','ou seja em outras palavras',
    'espero que este','fico a disposicao','qualquer duvida estou aqui',
    'em ultima analise','de forma eficaz','de maneira eficiente','significativamente',
    'consideravelmente','fundamentalmente','essencialmente','literalmente',
    'transformador','inovador','disruptivo','poderoso aliado','ferramenta poderosa',
    'passo a passo simples','de forma pratica','na pratica isso significa',
]
NAO_E_X_E_Y = re.compile(r'\bnao\s+(?:e|se\s+trata\s+de)\b[^.!?;]{2,60}?\b(?:e\s+sim|,\s*e)\b')
REGRA_DE_TRES = re.compile(r'\b[\wÀ-ÿ]+\s*,\s*[\wÀ-ÿ]+\s+e\s+[\wÀ-ÿ]+\b')
EMDASH = re.compile(r'[—–]')
DOISPONTOS = re.compile(r':(?!\d)')

STOP = set(norm(w) for w in (
    'a o e que de do da em um uma para com nao os as por mais como mas ao dos das se '
    'na no ou ele ela eu voce isso esse essa seu sua meu minha ja quando muito tem ser '
    'foi era vai vou tudo nada so entao ai porque pra pro ate sobre entre depois antes'
).split())

# ------------------------------------------------------------------ medidas

def medidas_doc(texto):
    P = paragrafos(texto)
    F = frases(texto)
    W = palavras(texto)
    n, nf = len(W), len(F)
    if n < 50 or nf < 5:
        return None
    nl = norm(texto)
    tam = [len(palavras(f)) for f in F]
    media = statistics.mean(tam)
    dp = statistics.pstdev(tam) if nf > 1 else 0.0

    # metronomo: maior sequencia de frases com tamanho dentro de +-25%
    corrida = maior = 1
    for a, b in zip(tam, tam[1:]):
        if a and abs(b - a) / a <= 0.25:
            corrida += 1
            maior = max(maior, corrida)
        else:
            corrida = 1

    tells_hits = collections.Counter()
    for t in TELLS:
        c = len(re.findall(r'(?<![a-z])' + re.escape(t) + r'(?![a-z])', nl))
        if c:
            tells_hits[t] = c

    marcadores = len(re.findall(r'\b(?:de|da|do|das|dos|que|para|com|nao|uma|um|em|no|na|os|as|e|o|a)\b', nl))
    m = {
        'pt_100': 100 * marcadores / n,
        'n_palavras': n, 'n_frases': nf, 'n_paragrafos': len(P),
        # concisao
        'wps': media,
        'que_100': 100 * len(re.findall(r'\bque\b', nl)) / n,
        'mente_100': 100 * len(re.findall(r'\b\w+mente\b', nl)) / n,
        'prep_100': 100 * len(re.findall(r'\b(?:de|da|do|das|dos)\b', nl)) / n,
        # ritmo (orientados: maior = mais humano, invertidos depois)
        'cv': dp / media if media else 0.0,
        'pct_curtas': 100 * sum(1 for t in tam if t <= 6) / nf,
        'metronomo': maior,
        # tells
        'tells_1000': 1000 * sum(tells_hits.values()) / n,
        'emdash_1000': 1000 * len(EMDASH.findall(texto)) / n,
        'doispontos_1000': 1000 * len(DOISPONTOS.findall(texto)) / n,
        'naoexey_1000': 1000 * len(NAO_E_X_E_Y.findall(nl)) / n,
        'tres_1000': 1000 * len(REGRA_DE_TRES.findall(nl)) / n,
        '_tells_hits': dict(tells_hits),
        '_tells_taxa': {t: 1000 * c / n for t, c in tells_hits.items()},
        '_aberturas': [' '.join(palavras(norm(p))[:3]) for p in P if len(palavras(p)) >= 4],
        '_shingles': shingles(nl),
    }
    return m

def shingles(nl, k=5):
    w = [x for x in palavras(nl)]
    return set(' '.join(w[i:i + k]) for i in range(len(w) - k + 1))

# templating precisa de mais de um documento
GRUPOS = {}

def carrega_grupos(caminhos):
    """grupos.json ao lado dos arquivos: {arquivo: grupo}. Par do mesmo grupo
    nao entra na conta. Copy da mesma serie reusa esqueleto de proposito."""
    g = {}
    for d in {os.path.dirname(os.path.abspath(c)) for c in caminhos}:
        f = os.path.join(d, 'grupos.json')
        if os.path.exists(f):
            g.update({k: v for k, v in json.load(open(f, encoding='utf-8')).items()
                      if not k.startswith('_')})
    return g

def mesmo_grupo(a, b):
    ga, gb = GRUPOS.get(a), GRUPOS.get(b)
    return ga is not None and ga == gb

def templating(docs):
    """docs: lista de (nome, medidas). Devolve dict nome -> (score_bruto, provas)."""
    out = {}
    if len(docs) < 2:
        # reuso interno NAO e templating. A regua (1,70% de media humana) foi
        # calibrada em reuso ENTRE arquivos; aplicar ela ao reuso dentro de um
        # texto so acusa qualquer copy que repita a propria abertura de
        # proposito, que e anafora e vende. Sem par, o eixo nao e medido.
        for nome, _ in docs:
            out[nome] = (float('nan'), {'aviso': 'sem par: templating nao medido. '
                                                 'Rode com --historico ou com outra copy junto.'})
        return out
    # media PAR A PAR, nao contra a uniao dos outros. Contra a uniao, o numero
    # cresce so por haver mais arquivos na mesa, e um lote de 7 fica sempre
    # "mais templatizado" que um lote de 3 sem escrever nada pior.
    for nome, m in docs:
        pares_ab, pares_sh, provas_ab, provas_sh = [], [], collections.Counter(), collections.Counter()
        piores = []
        for n2, m2 in docs:
            if n2 == nome or mesmo_grupo(nome, n2):
                continue
            ab2 = set(m2['_aberturas'])
            ab = m['_aberturas']
            rep = [a for a in ab if a in ab2]
            pares_ab.append(100 * len(rep) / max(1, len(ab)))
            provas_ab.update(rep)
            comuns = [x for x in (m['_shingles'] & m2['_shingles'])
                      if sum(1 for w in x.split() if w not in STOP) >= 3]
            pares_sh.append(100 * len(comuns) / max(1, len(m['_shingles'])))
            provas_sh.update(comuns)
            piores.append((0.6 * (100 * len(rep) / max(1, len(ab))) + 0.4 * min(100, 25 * 100 * len(comuns) / max(1, len(m['_shingles']))), n2))
        if not pares_ab:            # todo mundo do mesmo grupo: sem par valido
            out[nome] = (float('nan'), {'aviso': 'todos os pares sao do mesmo grupo'})
            continue
        pct_ab = statistics.mean(pares_ab)
        pct_sh = statistics.mean(pares_sh)
        # a metade das aberturas NAO e comparavel entre tamanhos: um anuncio de
        # 200 palavras tem 6 aberturas, e uma coincidencia sozinha ja vira 17%,
        # contra 1,7% de media num documento de 5 mil palavras. Abaixo de 15
        # paragrafos, so a metade dos esqueletos conta, que essa e estavel.
        curto = len(m['_aberturas']) < 15
        bruto_sh = min(100, pct_sh * 25)
        bruto = bruto_sh if curto else 0.6 * pct_ab + 0.4 * bruto_sh
        out[nome] = (bruto, {
            'curto': curto, 'n_aberturas': len(m['_aberturas']),
            'aberturas_repetidas': provas_ab.most_common(6),
            'esqueletos_repetidos': [x for x, _ in provas_sh.most_common(6)],
            'pct_aberturas': round(pct_ab, 1), 'pct_shingles': round(pct_sh, 3),
            'par_mais_parecido': max(piores) if piores else None,
        })
    return out

# ------------------------------------------------------------------ historico

def impressao(nome, m):
    """So o que templating precisa: aberturas e esqueletos com conteudo.
    A copy inteira nao vai para o disco."""
    return {'nome': nome, '_aberturas': m['_aberturas'],
            '_shingles': sorted(x for x in m['_shingles']
                                if sum(1 for w in x.split() if w not in STOP) >= 3)}

def carrega_historico(d):
    out = []
    if not d or not os.path.isdir(d):
        return out
    for f in sorted(os.listdir(d)):
        if not f.endswith('.json'):
            continue
        try:
            j = json.load(open(os.path.join(d, f), encoding='utf-8'))
        except Exception:
            continue
        out.append((j['nome'], {'_aberturas': j['_aberturas'], '_shingles': set(j['_shingles'])}))
    return out

def salva_historico(d, nome, m):
    os.makedirs(d, exist_ok=True)
    slug = re.sub(r'[^a-z0-9]+', '-', norm(nome)).strip('-')[:60] or 'copy'
    json.dump(impressao(nome, m), open(os.path.join(d, slug + '.json'), 'w', encoding='utf-8'),
              ensure_ascii=False)
    return slug

# ------------------------------------------------------------------ baseline

# (chave, orientacao) -> +1 = valor alto e mais slop, -1 = valor alto e mais humano
EIXOS = {
    'concisao': [('wps', +1), ('que_100', +1), ('mente_100', +1), ('prep_100', +1)],
    'ritmo':    [('cv', -1), ('pct_curtas', -1), ('metronomo', +1)],
    'tells':    [('tells_1000', +1), ('emdash_1000', +1), ('doispontos_1000', +1),
                 ('naoexey_1000', +1), ('tres_1000', +1)],
}
CHAVES = [k for eixo in EIXOS.values() for k, _ in eixo]

def piso_dp(dp, media):
    """Corpus pequeno gera desvio zero em metrica rara (o "nao e X, e Y" nao
    aparece nenhuma vez na copy humana). Sem piso, uma unica ocorrencia vira
    z de milhoes. O piso amarra o desvio a 20% da media, com um chao absoluto."""
    return max(dp, 0.20 * abs(media), 0.05)

def constroi_baseline(arquivos):
    ms = []
    for f in arquivos:
        m = medidas_doc(limpa(open(f, encoding='utf-8', errors='ignore').read()))
        if m:
            ms.append((os.path.basename(f), m))
    if len(ms) < 3:
        sys.exit('preciso de pelo menos 3 documentos humanos para o baseline')
    tpl = templating(ms)
    base = {'n_docs': len(ms), 'docs': [n for n, _ in ms], 'stats': {}}
    for k in CHAVES:
        v = [m[k] for _, m in ms]
        base['stats'][k] = {'media': statistics.mean(v), 'dp': piso_dp(statistics.pstdev(v), statistics.mean(v))}
    # taxa-base humana por termo. O metodo do Slop Index nao pune a palavra por
    # existir, pune por passar da taxa que o humano ja usava. "literalmente" e
    # "a verdade e que" aparecem 11 e 10 vezes na copy que vendeu: nao sao
    # vicio de IA em resposta direta brasileira, sao vocabulario do nicho.
    base_tells = collections.defaultdict(list)
    for _, m in ms:
        for t in TELLS:
            base_tells[t].append(m['_tells_taxa'].get(t, 0.0))
    base['tells_base'] = {t: round(statistics.mean(v), 4) for t, v in base_tells.items()}

    v = [tpl[n][0] for n, _ in ms if tpl[n][0] == tpl[n][0] and not tpl[n][1].get('curto')]
    base['stats']['templating'] = {'media': statistics.mean(v), 'dp': piso_dp(statistics.pstdev(v), statistics.mean(v))}
    vs = [min(100, tpl[n][1]['pct_shingles'] * 25) for n, _ in ms if 'pct_shingles' in tpl[n][1]]
    base['stats']['templating_curto'] = {'media': statistics.mean(vs), 'dp': piso_dp(statistics.pstdev(vs), statistics.mean(vs))}
    return base

def z(valor, st, orient):
    return orient * (valor - st['media']) / st['dp']

def escala(zmed):
    """baseline humano = 0 de slop; +2 desvios = 100."""
    return max(0.0, min(100.0, 50.0 * zmed))

def excesso_tells(m, base):
    """Devolve (acima_da_base, dentro_da_base). So o primeiro grupo e acusacao."""
    bt = base.get('tells_base', {})
    acima, dentro = [], []
    for t, taxa in sorted(m['_tells_taxa'].items(), key=lambda kv: -kv[1]):
        n = m['_tells_hits'].get(t, 0)
        alvo = bt.get(t, 0.0)
        (acima if taxa > max(alvo * 1.5, alvo + 0.15) else dentro).append((t, n, round(taxa, 2), alvo))
    return acima, dentro

def pontua(nome, m, tpl_bruto, base, curto=False):
    eixos, detalhe = {}, {}
    for eixo, campos in EIXOS.items():
        zs = {k: z(m[k], base['stats'][k], o) for k, o in campos}
        eixos[eixo] = escala(statistics.mean(zs.values()))
        detalhe[eixo] = {k: round(v, 2) for k, v in zs.items()}
    medido = tpl_bruto == tpl_bruto
    if medido:
        regua = 'templating_curto' if (curto and 'templating_curto' in base['stats']) else 'templating'
        zt = z(tpl_bruto, base['stats'][regua], +1)
        eixos['templating'] = escala(zt)
        detalhe['templating'] = {'z': round(zt, 2), 'bruto': round(tpl_bruto, 1), 'regua': regua}
    # sem par valido, o eixo sai da conta e os 30% se redistribuem. Melhor um
    # score de 3 eixos declarado do que um quarto eixo inventado.
    usados = {e: p for e, p in PESOS.items() if e != 'templating' or medido}
    soma = sum(usados.values())
    total = sum(p / soma * eixos[e] for e, p in usados.items())
    acima, dentro = excesso_tells(m, base)
    return {'arquivo': nome, 'slop_score': round(total, 1),
            'eixos': {e: round(v, 1) for e, v in eixos.items()},
            'z': detalhe, 'medidas': {k: round(m[k], 2) for k in CHAVES},
            'tells_acima_da_base': acima, 'tells_dentro_da_base': dentro}

# ------------------------------------------------------------------ relatorio

BARRA = lambda v: '#' * int(round(v / 5)) + '.' * (20 - int(round(v / 5)))

def relatorio(res, provas):
    for r in res:
        print('=' * 74)
        print(f"{r['arquivo']}")
        print(f"  SLOP SCORE  {r['slop_score']:>5.1f} / 100   (0 = escreve como a copy humana do baseline)")
        print()
        falta = 'templating' not in r['eixos']
        for e, p in PESOS.items():
            if e == 'templating' and falta:
                print(f"  {e:<11}    --  {'.' * 20}  não medido (sem par para comparar)")
                continue
            peso = p / (1 - PESOS['templating']) if falta else p
            print(f"  {e:<11} {r['eixos'][e]:>5.1f}  {BARRA(r['eixos'][e])}  peso {int(round(peso*100))}%")
        print()
        pior = max(r['eixos'], key=lambda e: PESOS[e] * r['eixos'][e])
        print(f"  perde principalmente em: {pior.upper()}" if r['eixos'][pior] > 0
              else "  nenhum eixo acima da copy humana")
        md = r['medidas']
        print(f"  frase media {md['wps']:.1f} palavras · cv do ritmo {md['cv']:.2f} · "
              f"curtas {md['pct_curtas']:.0f}% · metronomo {int(md['metronomo'])} frases seguidas")
        print(f"  que/100 {md['que_100']:.2f} · advérbio -mente/100 {md['mente_100']:.2f} · "
              f"de-da-do/100 {md['prep_100']:.2f}")
        print(f"  tells/1000 {md['tells_1000']:.1f} · em-dash/1000 {md['emdash_1000']:.1f} · "
              f"dois-pontos/1000 {md['doispontos_1000']:.1f} · regra-de-tres/1000 {md['tres_1000']:.1f}")
        if r['tells_acima_da_base']:
            print('  ACIMA da taxa humana: ' +
                  ', '.join(f'{t} ({n}x, {tx}/1000 vs base {b})' for t, n, tx, b in r['tells_acima_da_base']))
        if r['tells_dentro_da_base']:
            print('  dentro da taxa humana (não é acusação): ' +
                  ', '.join(f'{t} ({n}x)' for t, n, _, _ in r['tells_dentro_da_base']))
        if r['z'].get('templating', {}).get('regua') == 'templating_curto':
            print('  (texto curto: templating medido só por esqueleto, régua própria)')
        pv = provas.get(r['arquivo'], {})
        if pv.get('aberturas_repetidas'):
            print('  aberturas reusadas em outro arquivo: ' +
                  ' | '.join(f'"{a}..." {c}x' for a, c in pv['aberturas_repetidas']))
        pior_par = pv.get('par_mais_parecido')
        if pior_par and pior_par[0] >= 5:
            print(f'  par mais parecido: {pior_par[1]} ({pior_par[0]:.0f}% de reuso, '
                  f'contra 1,7% entre copies humanas sem relação)')
        if pv.get('esqueletos_repetidos'):
            print('  esqueletos reusados: ' + ' | '.join(f'"{s}"' for s in pv['esqueletos_repetidos'][:3]))
        print()

# ------------------------------------------------------------------ cli

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    b = sub.add_parser('baseline'); b.add_argument('arquivos', nargs='+'); b.add_argument('-o', required=True)
    s = sub.add_parser('score'); s.add_argument('arquivos', nargs='+')
    s.add_argument('--historico', help='pasta de impressoes de copies anteriores; '
                                       'templating passa a comparar contra elas')
    s.add_argument('--nao-salvar', action='store_true', help='nao gravar no historico')
    s.add_argument('--baseline', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'baseline.json'))
    s.add_argument('--json', action='store_true')
    a = ap.parse_args()

    global GRUPOS
    GRUPOS = carrega_grupos(a.arquivos)

    if a.cmd == 'baseline':
        base = constroi_baseline([f for f in a.arquivos if not f.endswith('grupos.json')])
        json.dump(base, open(a.o, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f"baseline gravado em {a.o} · {base['n_docs']} documentos humanos")
        for k, v in base['stats'].items():
            print(f"  {k:<16} media {v['media']:>7.2f}  dp {v['dp']:>6.2f}")
        return

    base = json.load(open(a.baseline, encoding='utf-8'))
    ms = []
    for f in a.arquivos:
        m = medidas_doc(limpa(open(f, encoding='utf-8', errors='ignore').read()))
        if not m:
            print(f'ignorado (curto demais): {f}', file=sys.stderr)
        elif m['pt_100'] < 12:
            # a regua inteira e de portugues: "que", "-mente", "de/da/do". Texto
            # em outro idioma zera essas medidas e passa como copy impecavel.
            print(f'ignorado (não parece PT-BR: {m["pt_100"]:.0f} marcadores/100 '
                  f'palavras, esperado 20+): {f}', file=sys.stderr)
        else:
            ms.append((os.path.basename(f), m))
    if not ms:
        sys.exit('nada para medir')
    hist = carrega_historico(getattr(a, 'historico', None))
    if hist:
        print(f'histórico: {len(hist)} copies anteriores na comparação de templating\n', file=sys.stderr)
    tpl = templating(ms + hist)
    res = [pontua(n, m, tpl[n][0], base, tpl[n][1].get('curto', False)) for n, m in ms]
    provas = {n: tpl[n][1] for n, _ in ms}
    if getattr(a, 'historico', None) and not a.nao_salvar:
        for n, m in ms:
            salva_historico(a.historico, n, m)
    if a.json:
        print(json.dumps({'resultados': res, 'provas': provas}, ensure_ascii=False, indent=1))
    else:
        relatorio(res, provas)

if __name__ == '__main__':
    main()
