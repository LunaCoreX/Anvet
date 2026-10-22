# Clínica Veterinária Anvet — site institucional

Site estático de uma página (HTML, CSS e JavaScript puros, sem build).

## Estrutura

```
index.html   página completa (estilos e scripts embutidos)
img/         fotos, vídeos curtos e logotipo
```

## Publicar no GitHub Pages

1. Crie um repositório e envie estes arquivos para a branch `main`.
2. Em **Settings → Pages**, escolha *Deploy from a branch*, branch `main`, pasta `/ (root)`.
3. O site fica em `https://<usuario>.github.io/<repositorio>/`.

Para testar localmente: `python3 -m http.server` na pasta e abra `http://localhost:8000`.

## Conteúdo e fontes

- Informações e fotos vêm do Instagram oficial [@_anvet](https://www.instagram.com/_anvet/), com autorização da clínica.
- Fontes: Gabarito e Onest (Google Fonts).
- O formulário não envia dados: ele monta uma mensagem e abre o WhatsApp da clínica.

## Pendências antes de publicar oficialmente

- Logotipo em vetor (o selo atual é a imagem de 150 px do Instagram).
- Nomes completos e CRMV da equipe e do responsável técnico.
- Confirmar o telefone fixo (11) 5939-8706.
- Valores e área atendida pelo táxi dog.
- Vídeos do tour em resolução maior (os atuais têm 360 px de largura).
