# Manutenção do site

## Estrutura

```
index.html                    página inicial
politica-de-privacidade.html  minuta para validação jurídica
termos-e-condicoes.html       minuta para validação jurídica
404.html                      página de erro (caminhos absolutos /Anvet/)
assets/css/site.v1.css        estilos de todas as páginas
assets/js/site.v1.js          menu, horário, vídeos, formulário, pastilhas
assets/images|videos|posters|icons|fonts
site.webmanifest  sitemap.xml  robots.txt  llms.txt  _headers
_config.yml                   impede o GitHub Pages de publicar docs/, build/ e README
build/                        scripts que geram as páginas (Python 3 + Pillow)
docs/                         esta documentação (não é publicada)
```

## Editar textos

O jeito mais simples é editar o HTML direto. Se preferir gerar de novo pelos scripts (mantém cabeçalho e rodapé iguais em todas as páginas):

```sh
pip install pillow
python3 build/index.py    # página inicial
python3 build/legal.py    # política, termos e 404
```

Cabeçalho, rodapé e metadados ficam em `build/common.py`. Os scripts leem as dimensões reais das imagens, então `width` e `height` ficam sempre certos.

## Itens que mudam com frequência

| O quê | Onde |
|---|---|
| Horário de funcionamento | `index.html` (texto e JSON-LD), `assets/js/site.v1.js` (`updateStatus`: 540 = 9h, 1080 = 18h), rodapé em `build/common.py`, `llms.txt`, termos (seção 4) |
| WhatsApp | `WA` em `site.v1.js`, links `wa.me` em todas as páginas |
| Telefone | `index.html`, JSON-LD, política e termos (seção 1), `llms.txt` |
| Datas das páginas legais | `UPDATED` em `build/legal.py` e `lastmod` em `sitemap.xml` |

Depois de mudar a política ou os termos, atualize a data “Última atualização” e o `lastmod` do sitemap.

## Fotos e vídeos

Veja `docs/midias.md` (origem, proporções e como exportar).

## CSS e JS

Ao mudar `site.v1.css` ou `site.v1.js` de forma relevante, renomeie para `v2` e atualize as referências em `build/common.py` (e gere as páginas de novo). Isso evita versões antigas presas em cache se o site mudar de hospedagem.

## Antes de publicar

1. Abra as páginas no celular e no computador, no tema claro e no escuro.
2. Teste o formulário e o botão do WhatsApp.
3. Depois de publicar, rode o PageSpeed Insights no endereço real.
4. Se algo novo coletar dados (análise de audiência, chat, formulário com envio), atualize a Política de Privacidade **antes** de publicar.
