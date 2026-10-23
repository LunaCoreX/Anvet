# Mídias do site

Todas as fotos e vídeos vêm do perfil oficial da clínica no Instagram ([@_anvet](https://www.instagram.com/_anvet/)), com uso autorizado pela clínica. Os originais em alta resolução **não** fazem parte deste repositório: ficam no pacote separado `anvet-originais.zip`, que deve ser guardado fora do GitHub.

Cada imagem tem versões AVIF (servida primeiro) e WebP (alternativa) nas larguras indicadas. O navegador escolhe a largura pelo `srcset`/`sizes`. As dimensões no HTML (`width`/`height`) são lidas dos arquivos reais na hora de gerar as páginas.

## Imagens (`assets/images/`)

| Arquivo base | Larguras | Proporção | Uso | Origem (post do Instagram) |
|---|---|---|---|---|
| `recepcao-balcao-pastilhas` | 480, 720, 960, 1200 | 4:5 | Foto principal (desktop e tablet), carregada com prioridade alta | Carrossel `DF_id0RssHG` |
| `recepcao-balcao-pastilhas-horizontal` | 480, 720, 960 | 4:3 | Foto principal no celular (recorte da mesma foto) | Carrossel `DF_id0RssHG` |
| `fachada-clinica` | 480, 800 | 4:5 | Seção “Como chegar” e página 404 | `DJIjtHTs1bX` |
| `taxi-dog-anvet` | 480, 800 | ≈1:1 | Galeria, serviço de táxi dog | `DM9DQVaMLo9` |
| `dra-laura-marques-gato` | 400, 800 | 3:4 | Galeria | `Dc65ylBFjEN` |
| `dra-laura-marques-pitoco` | 400, 800 | 3:4 | Galeria (área “Ver mais”) | `DdiQKvkFn8l` |
| `equipe-gato-preto` | 400, 800 | 4:5 | Galeria (área “Ver mais”) | `DGmJxjcsQ6j` |
| `equipe-corredor` | 480, 960 | 4:5 | Seção Equipe | `DMO8PLLMztA` |
| `fisioterapia-esteira` | 400, 720 | 4:5 | Galeria | quadro do reel `DeelZeSx7tj` |
| `retrato-dra-laura-marques` | 480 | 4:5 | Retrato padronizado, seção Equipe | recorte de `DesjttPsN5l` (com o Cabrito) |
| `retrato-dra-adriana` | 480 | 4:5 | Retrato padronizado, seção Equipe | quadro do reel `Demh2xzROPe`, sem legenda |
| `compartilhamento-anvet-1200x630.jpg` | 1200 | 1,91:1 | Imagem de compartilhamento (Open Graph) | `DF_id0RssHG` |

**Padrão dos retratos da equipe:** proporção 4:5, 480×600 px, olhos a cerca de 40% da altura, mesmo enquadramento de ombros, sem filtros que alterem a aparência. Um novo retrato deve seguir o mesmo padrão.

## Vídeos (`assets/videos/`) e capas (`assets/posters/`)

Todos são curtos, sem som (`muted`), em H.264. Cada vídeo tem uma capa WebP leve com o mesmo nome em `assets/posters/`; o vídeo só começa a baixar quando é reproduzido (`preload="none"`).

| Arquivo | Tamanho | Duração | Uso | Origem |
|---|---|---|---|---|
| `atendimento-consulta.mp4` | 400×500 | 9,4 s | Galeria | reel `Dex6UVIt7-V` |
| `centro-cirurgico.mp4` | 360×450 | 4 s | Galeria | tour, reel `DG1dU4ysK1N` |
| `sala-raio-x.mp4` | 360×450 | 4 s | Galeria | tour, reel `DG1dU4ysK1N` |
| `laboratorio.mp4` | 360×450 | 4 s | Galeria (área “Ver mais”) | tour, reel `DG1dU4ysK1N` |
| `farmacia.mp4` | 360×450 | 4 s | Galeria (área “Ver mais”) | tour, reel `DG1dU4ysK1N` |

Os trechos do tour foram recortados para remover a faixa de legenda do vídeo original. Como não têm fala, a alternativa em texto é a legenda visível abaixo de cada vídeo e o rótulo do botão de reprodução.

## Ícones (`assets/icons/`)

Gerados a partir do logotipo circular da clínica (foto de perfil do Instagram, 150 px). As versões acima de 150 px foram ampliadas; **substitua-as por uma exportação do arquivo vetorial original do logotipo** assim que a clínica fornecer.

| Arquivo | Uso |
|---|---|
| `favicon.ico`, `favicon-32.png` | Ícone da aba |
| `apple-touch-icon.png` (180) | Atalho no iPhone |
| `icone-192.png`, `icone-512.png`, `icone-maskable-512.png` | Manifesto (`site.webmanifest`) |
| `anvet-selo-96.png` | Logotipo no cabeçalho (exibido a 48 px) |
| `anvet-selo-150.png` | Logotipo no rodapé |

## Fontes (`assets/fonts/`)

| Arquivo | Família | Peso | Origem e licença |
|---|---|---|---|
| `gabarito-700-latin.woff2` | Gabarito | 700 (títulos) | Fontsource 5.3.0, SIL OFL 1.1 (`OFL-gabarito.txt`) |
| `onest-400-latin.woff2` | Onest | 400 (texto) | Fontsource 5.3.1, SIL OFL 1.1 (`OFL-onest.txt`) |
| `onest-600-latin.woff2` | Onest | 600 (destaques) | Fontsource 5.3.1, SIL OFL 1.1 |

Subconjunto Latin-1 com pontuação tipográfica (inclui á, ã, ç, é, ê, í, ó, õ, ú, travessão, aspas curvas e reticências). `font-display: swap`. Nenhuma fonte é pré-carregada.

## Como trocar ou acrescentar uma foto

1. Guarde o original em alta resolução no pacote de originais (fora do repositório).
2. Recorte na proporção da tabela acima.
3. Exporte as larguras indicadas em AVIF (qualidade ≈ 50) e WebP (qualidade ≈ 75), com nome em minúsculas, sem acentos, separado por hífen: `assunto-detalhe-LARGURA.avif`.
4. Atualize o `<picture>` correspondente no HTML: `srcset` das duas fontes, `src`, `width`, `height` (iguais aos do arquivo `src`) e `alt`.
5. Atualize esta tabela.

Exemplo com ferramentas de linha de comando:

```sh
magick original.jpg -resize 720x recepcao-720.png
avifenc -q 50 recepcao-720.png recepcao-720.avif
cwebp -q 75 recepcao-720.png -o recepcao-720.webp
```

Vídeo novo: até ~10 s, sem áudio, 360–400 px de largura, H.264 com `-crf 27 -movflags +faststart -an`, e uma capa WebP do primeiro quadro com o mesmo nome.
