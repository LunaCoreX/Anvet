# Hospedagem, cabeçalhos e arquivos técnicos

O site está no **GitHub Pages**, como site de projeto, em `https://lunacorex.github.io/Anvet/`. Este documento separa o que **está ativo** do que está apenas **preparado** para outra hospedagem ou para um domínio próprio.

## Cabeçalhos medidos no ar (22/10/2026)

Resposta de `https://lunacorex.github.io/Anvet/` (versão anterior do site), lida no navegador:

| Cabeçalho | Valor recebido |
|---|---|
| `cache-control` | `max-age=600` (o mesmo para HTML, imagens e vídeos) |
| `strict-transport-security` | `max-age=31556952` |
| `content-encoding` | `gzip` |
| `server` / `via` | `GitHub.com` / Fastly (varnish) |
| `content-security-policy` | **ausente** |

O GitHub Pages não permite configurar cabeçalhos. Por isso:

- o cache longo para CSS, JS e fontes **não está ativo**: todos os arquivos expiram em 10 minutos e são revalidados;
- a política de segurança de conteúdo (CSP) **não está ativa**;
- não foram adicionadas metatags `http-equiv` para imitar cabeçalhos: elas não substituem cabeçalhos HTTP de verdade (a CSP via meta não suporta `frame-ancestors`, por exemplo) e dariam falsa sensação de proteção.

## Situação de cada arquivo técnico

| Arquivo | Situação no GitHub Pages | Observação |
|---|---|---|
| `404.html` | **Ativo** | O GitHub Pages serve este arquivo com status 404 para endereços inexistentes dentro de `/Anvet/`. Usa caminhos absolutos (`/Anvet/...`) porque pode ser exibido em qualquer profundidade de URL. |
| `site.webmanifest` | **Ativo** | `start_url` e `scope` em `/Anvet/`. `display: browser`: o site não tenta se passar por aplicativo e não há service worker. |
| `sitemap.xml` | **Ativo**, mas precisa ser informado | Lista só as três páginas indexáveis. Como o `robots.txt` deste projeto não fica na raiz, envie o sitemap pelo Google Search Console (propriedade de prefixo de URL `https://lunacorex.github.io/Anvet/`). |
| `llms.txt` | **Ativo** como arquivo | Segue o formato de llmstxt.org. Não há garantia de que ferramentas de IA o leiam, nem efeito em posicionamento. |
| `robots.txt` | **Preparado, não lido** | Robôs só leem `robots.txt` na raiz do host. Veja abaixo. |
| `_headers` | **Preparado, ignorado** | Formato de Netlify e Cloudflare Pages. O GitHub Pages ignora. |
| `_config.yml` | **Ativo** | Diz ao GitHub Pages (Jekyll) para não publicar `docs/`, `build/` e `README.md`. Eles continuam visíveis no repositório público. |
| `.gitignore` | Ferramenta de trabalho | Evita subir originais e arquivos locais. Não remove nada já publicado e não é proteção. |

## robots.txt e a raiz do host

As regras de `robots.txt` só valem quando o arquivo está em `https://HOST/robots.txt` ([documentação do Google](https://developers.google.com/crawling/docs/robots-txt/create-robots-txt)). Hoje, `https://lunacorex.github.io/robots.txt` retorna 404, ou seja, não há restrição e tudo pode ser rastreado. O arquivo `/Anvet/robots.txt` deste projeto **não é lido**.

Se a conta `lunacorex` quiser um `robots.txt` na raiz, ele precisa ficar no repositório `lunacorex.github.io` e deve **preservar as regras de outros projetos** da conta. Modelo:

```
# https://lunacorex.github.io/robots.txt
# Mantenha aqui as regras dos outros projetos publicados nesta conta.

User-agent: *
Allow: /

Sitemap: https://lunacorex.github.io/Anvet/sitemap.xml
```

`robots.txt` não é mecanismo de privacidade: ele pede aos robôs que não rastreiem, mas o conteúdo continua público e acessível por link.

Com domínio próprio (por exemplo `anvet.com.br`), o arquivo deste projeto passa a ficar na raiz e começa a valer. Nesse caso, atualize `SITE` em `build/common.py` (ou os endereços absolutos nas páginas), o `sitemap.xml`, o `llms.txt`, o `robots.txt` e o `site.webmanifest`.

## `_headers` preparado

Se o site for publicado no Netlify ou no Cloudflare Pages (não faz parte desta entrega), o arquivo `_headers` passa a valer e define:

- HTML sempre revalidado (`max-age=0, must-revalidate`), nunca cache imutável;
- cache de 1 ano com `immutable` **só** para arquivos com versão no nome (`site.v1.css`, `site.v1.js`) e fontes;
- 7 dias para imagens, vídeos e ícones, que não têm versão no nome;
- CSP restrita a `'self'`. O site foi preparado para ela: não há scripts nem estilos inline executáveis (o bloco JSON-LD é dado, não script executado) e nenhum recurso de terceiros é carregado na abertura da página.

Depois de publicar em outra plataforma, **confira os cabeçalhos recebidos** (DevTools, aba Rede) antes de afirmar que estão ativos.

## Regra de versionamento

Ao alterar `assets/css/site.v1.css` ou `assets/js/site.v1.js`, crie `site.v2.css` / `site.v2.js` e atualize as referências em todas as páginas. No GitHub Pages isso não muda o cache (10 minutos para tudo), mas evita erro se o site for para uma plataforma com cache longo.
