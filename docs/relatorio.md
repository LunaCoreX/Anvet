# Relatório da revisão (22/10/2026)

## Medições de desempenho

**Como foi medido:** Lighthouse 12.8.2, executado localmente em Chromium headless, 3 rodadas por cenário (celular e desktop), valor mediano. As duas versões foram servidas pelo mesmo servidor local, com `cache-control: max-age=600` como no GitHub Pages. Na versão anterior, a folha do Google Fonts foi servida por um servidor de outra origem, para manter o custo real de uma conexão externa que bloqueia a renderização.

São medições de laboratório. Elas não reproduzem a rede e o CDN reais do GitHub Pages, então os números podem diferir do PageSpeed Insights. Depois da publicação, rode o [PageSpeed Insights](https://pagespeed.web.dev/) no endereço real e compare com o diagnóstico de 22/10 (celular 86, desktop 99).

| Cenário (mediana de 3) | Nota | FCP | LCP | TBT | CLS | Transferido |
|---|---|---|---|---|---|---|
| Celular, antes | 90 (90, 89, 90) | 1,69 s | 3,53 s | 0 ms | 0,000 | 452 KB |
| **Celular, depois** | **99** (98, 99, 99) | **1,06 s** | **2,18 s** | 65 ms | 0,000 | **211 KB** |
| Desktop, antes | 100 (100, 100, 100) | 0,48 s | 0,64 s | 0 ms | 0,000 | 340 KB |
| **Desktop, depois** | **100** (100, 100, 100) | **0,38 s** | **0,48 s** | 0 ms | 0,003 | **204 KB** |

Metas pedidas: celular ≥ 90 (medido 99), desktop ≥ 95 (100), LCP ≤ 2,5 s (2,18 s no celular), CLS ≤ 0,1 (0,003).

**INP não foi medido.** INP depende de interações de visitantes reais (dados de campo do Chrome UX Report), que um site com pouco tráfego pode nem ter. O TBT acima é uma métrica de laboratório e não substitui o INP.

Na mesma ferramenta, as categorias Acessibilidade, Boas práticas e SEO ficaram em 100 na página inicial, na política e nos termos.

### De onde veio o ganho

- **Fontes:** o Google Fonts (CSS externo que bloqueava a renderização e mais três conexões) foi trocado por três arquivos WOFF2 locais (40 KB no total) com subconjunto para português e `font-display: swap`.
- **Foto principal:** passou a usar AVIF com alternativa WebP, `srcset` por largura e um recorte horizontal no celular. A versão de 720 px caiu de 129 KB (WebP) para 47 KB (AVIF horizontal). Ela continua com `fetchpriority="high"` e sem `loading="lazy"`.
- **Imagens abaixo da dobra:** `loading="lazy"`, `decoding="async"`, AVIF/WebP e `width`/`height` iguais aos arquivos reais.
- **Vídeos:** `preload="none"` e capa WebP leve (4 a 10 KB). Nenhum `.mp4` é baixado ao abrir a página.
- **CSS e JS:** um arquivo de cada, compartilhado por todas as páginas, sem bibliotecas.

## Validação funcional e visual

Testes automatizados (Playwright) e capturas em 360, 390, 768, 1280 e 1440 px, nos temas claro e escuro:

| Verificação | Resultado |
|---|---|
| Rolagem horizontal | Nenhuma, nas 4 páginas e 5 larguras |
| Imagens quebradas | Nenhuma |
| Âncoras internas sem destino | Nenhuma |
| Um único `h1` por página | Sim |
| 404 | O servidor de teste responde com status 404, como o GitHub Pages |
| Teclado | O primeiro Tab leva a “Pular para o conteúdo”; o foco é visível (contorno de 3 px); o botão de vídeo funciona com Enter e Espaço; “Ver mais fotos e vídeos” abre com Enter |
| Menu no celular | Abre, leva o foco ao primeiro link, fecha com Esc e devolve o foco ao botão |
| Formulário | O envio vazio marca os 3 campos obrigatórios e foca o primeiro; o envio válido mostra a prévia e o link do WhatsApp, com o aviso “Mensagem pronta, ainda não enviada” |
| Vídeo no celular (toque) | Não toca sozinho; toca ao tocar no botão; só nesse momento o arquivo é baixado |
| Vídeo no desktop | Toca sozinho quando aparece na tela (ponteiro fino); pausa fora da tela e com a aba oculta |
| Um vídeo por vez | Ao iniciar outro, o anterior pausa |
| Movimento reduzido | Nenhum vídeo toca sozinho; zero animações na página |

### Verificações das skills de design

- **taste-skill, `lint.mjs`:** 0 FAIL, 0 WARN. Quatro exceções estão justificadas no CSS: a linha da barra fixa, o menu sobreposto, o contorno do selo e o anel de foco.
- **taste-skill, `inspect.mjs`:** 1 FAIL e 0 WARN. O FAIL `still-page` (“nada se move ao rolar”) foi mantido de propósito: o pedido era reduzir as animações de entrada e mostrar o conteúdo essencial de imediato. Os avisos de quantidade de tamanhos de fonte e de título sem contexto no celular foram corrigidos.
- **impeccable, `detect`:** 0 problemas nas páginas renderizadas, depois de ajustar a largura das linhas nos documentos.

## O que mudou

**Identidade e visual**

- Logotipo oficial no cabeçalho.
- Títulos com peso menor e escala refinada.
- Espaçamento entre seções reduzido para `clamp(64px, 7vw, 112px)`.
- Nenhuma animação de entrada.

**Serviços**

- “Do check-up à cirurgia” virou a seção de destaque: oito cartões com ícone (consultas e cirurgia em evidência) e a lista completa em “Ver todos os serviços”.
- Instagram no cabeçalho (ícone no desktop, botão no celular e item no menu).

**Fotos e galeria**

- Fotos sem repetição.
- A galeria mostra 6 itens (3 vídeos e 3 fotos); os outros ficam em “Ver mais fotos e vídeos”.

**Equipe**

- Retratos padronizados em 4:5, com o mesmo enquadramento e sem filtros.
- O quadro de vídeo da Dra. Adriana foi recortado sem a legenda.
- Textos institucionais: nome, função e atuação confirmada.
- Foram retiradas as menções a frequência em vídeos, datas de posts e composição presumida da equipe.

**Afirmações**

- Foram mantidas as que vêm de fontes da própria clínica (25+ anos, preço popular, Petlove, silvestres com agendamento).
- Ficaram na lista de pendências para confirmação.

**Contato**

- A contagem regressiva foi trocada por uma informação tranquila de horário, no fuso de São Paulo, com aviso sobre feriados.
- O formulário explica em 3 passos o que acontece e nunca diz que a mensagem foi enviada.

**Vídeos**

- Capa leve, botão Reproduzir/Pausar acessível e um vídeo por vez.
- Pausa fora da tela e com a aba oculta.
- Respeita movimento reduzido e economia de dados.
- No celular, só toca quando o visitante toca.

**Arquivos**

- Pastas novas: `assets/images`, `videos`, `posters`, `icons`, `fonts`, `css` e `js`.
- Nomes descritivos e sem duplicatas.
- Os originais em alta resolução ficam fora do repositório.

**Páginas novas e arquivos técnicos**

- Política de Privacidade e Termos de Uso, linkadas em todos os rodapés e perto do formulário.
- 404, `llms.txt`, `site.webmanifest`, `sitemap.xml`, `robots.txt`, `_headers`, `.gitignore` e `_config.yml`.

**Metadados**

- Título, descrição, canonical, Open Graph com imagem de 1200×630, ícones e tema por esquema de cor.
- JSON-LD `VeterinaryCare` só com dados visíveis no site. Ficaram de fora faixa de preço, avaliações e credenciais.

## Ativo e preparado

Veja `docs/hospedagem-e-cabecalhos.md`. Em resumo:

- **Ativos no GitHub Pages:** páginas, 404, manifesto, sitemap, `llms.txt`.
- **Preparados, sem efeito hoje:**
  - `robots.txt`, porque não está na raiz do host.
  - `_headers`, porque o GitHub Pages ignora o arquivo; o cache longo e a CSP não estão ativos.
