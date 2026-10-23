from PIL import Image
import os
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SITE='https://lunacorex.github.io/Anvet/'
def dims(path):
    with Image.open(os.path.join(ROOT,path)) as im: return im.size
def pic(name, widths, sizes, alt, cls='', lazy=True, prefix='', extra_img=''):
    srcs=lambda ext: ', '.join(f'{prefix}assets/images/{name}-{w}.{ext} {dims(f"assets/images/{name}-{w}.{ext}")[0]}w' for w in widths)
    fw=widths[min(1,len(widths)-1)]
    w,h=dims(f'assets/images/{name}-{fw}.webp')
    la=' loading="lazy" decoding="async"' if lazy else ''
    c=f' class="{cls}"' if cls else ''
    return (f'<picture><source type="image/avif" srcset="{srcs("avif")}" sizes="{sizes}">'
            f'<img{c} src="{prefix}assets/images/{name}-{fw}.webp" srcset="{srcs("webp")}" sizes="{sizes}" width="{w}" height="{h}" alt="{alt}"{la}{extra_img}></picture>')
WA_SVG='<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.66 15l-1.3 4.76 4.88-1.28A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.18-1.14l-.3-.18-2.9.76.78-2.83-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.14c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.55.12-.17.25-.64.8-.78.97-.14.16-.29.18-.53.06a6.7 6.7 0 0 1-3.32-2.9c-.25-.43.25-.4.72-1.33.08-.16.04-.3-.02-.43-.06-.12-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47a.9.9 0 0 0-.65.3 2.73 2.73 0 0 0-.85 2.03 4.74 4.74 0 0 0 1 2.52 10.86 10.86 0 0 0 4.16 3.68c1.55.67 2.16.73 2.93.61.47-.07 1.46-.6 1.66-1.17.2-.58.2-1.07.15-1.17-.06-.1-.22-.17-.47-.29Z"/></svg>'
PLAY='<svg class="i-play" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg><svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M7 5h4v14H7zM13 5h4v14h-4z"/></svg>'
def video(slug, label, caption, cls='shot'):
    w,h=dims(f'assets/posters/{slug}.webp')
    return (f'<figure class="{cls}"><div class="frame" data-video>'
            f'<video preload="none" poster="assets/posters/{slug}.webp" muted loop playsinline width="{w}" height="{h}" aria-label="{label}"><source src="assets/videos/{slug}.mp4" type="video/mp4"></video>'
            f'<button class="vplay" type="button" aria-pressed="false">{PLAY}<span data-label>Reproduzir</span><span class="sr"> vídeo: {caption}</span></button>'
            f'</div><figcaption>{caption}</figcaption></figure>')
def head(title, desc, path, extra='', prefix='', robots='index, follow', og=True):
    url=SITE+path
    canon=f'<link rel="canonical" href="{url}">' if robots.startswith('index') else ''
    ogt=(f'''<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Clínica Veterinária Anvet">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}assets/images/compartilhamento-anvet-1200x630.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Médica veterinária da Anvet com um cachorro branco em frente ao balcão de pastilhas verdes da recepção.">
<meta name="twitter:card" content="summary_large_image">''') if og else ''
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
{canon}
<meta name="theme-color" content="#f6f6f4" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f1a14" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<link rel="icon" href="{prefix}assets/icons/favicon.ico" sizes="48x48">
<link rel="icon" href="{prefix}assets/icons/favicon-32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="{prefix}assets/icons/apple-touch-icon.png">
<link rel="manifest" href="{prefix}site.webmanifest">
{ogt}
<link rel="stylesheet" href="{prefix}assets/css/site.v1.css">
{extra}
<script src="{prefix}assets/js/site.v1.js" defer></script>
</head>
<body>
'''
def header(prefix='', home=False):
    h='' if home else (prefix or './')
    return f'''<a class="skip" href="#conteudo">Pular para o conteúdo</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{prefix or './'}"><img src="{prefix}assets/icons/anvet-selo-96.png" width="48" height="48" alt=""><span><b>Anvet</b> <small>Clínica Veterinária</small></span></a>
    <nav class="nav" id="nav" aria-label="Principal">
      <a href="{h}#servicos">Serviços</a>
      <a href="{h}#clinica">A clínica</a>
      <a href="{h}#equipe">Equipe</a>
      <a href="{h}#duvidas">Dúvidas</a>
      <a href="{h}#visita">Como chegar</a>
      <a class="nav-ig" href="https://www.instagram.com/_anvet/" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg><span>Instagram</span></a>
      <a class="btn btn--sm" href="https://wa.me/5511992999988" target="_blank" rel="noopener">WhatsApp</a>
    </nav>
    <div class="header-actions">
      <a class="icon-btn" href="https://www.instagram.com/_anvet/" target="_blank" rel="noopener" aria-label="Instagram da Anvet (@_anvet)"><svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.9"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1" fill="currentColor" stroke="none"/></svg></a>
      <a class="btn btn--sm btn--quiet" href="https://wa.me/5511992999988" target="_blank" rel="noopener">WhatsApp</a>
      <button class="menu-btn" id="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    </div>
  </div>
</header>
'''
def footer(prefix='', after_visit=False):
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="seal">
        <img src="{prefix}assets/icons/anvet-selo-150.png" width="150" height="150" alt="Logotipo da Clínica Veterinária Anvet" loading="lazy">
        <p><strong>Clínica Veterinária Anvet</strong>Av. Dona Belmira Marin, 1801, Parque Brasil, São Paulo, SP. Segunda a sábado, das 9h às 18h.</p>
      </div>
      <ul class="foot-links">
        <li><a class="link" href="{prefix}politica-de-privacidade.html">Política de Privacidade</a></li>
        <li><a class="link" href="{prefix}termos-e-condicoes.html">Termos e Condições de Uso</a></li>
        <li><a class="link" href="https://www.instagram.com/_anvet/" target="_blank" rel="noopener">Instagram @_anvet</a></li>
      </ul>
    </div>
    <div class="foot-meta">
      <p>Este site não usa cookies nem ferramentas de análise de audiência.</p>
      <p>Fotos e vídeos: acervo da Clínica Veterinária Anvet. © <span id="year">2026</span> Clínica Veterinária Anvet.</p>
    </div>
  </div>
</footer>
</body>
</html>
'''
