import sys, os, re
sys.path.insert(0, os.path.dirname(__file__))
from common import *

UPDATED = '22 de outubro de 2026'
UPDATED_ISO = '2026-10-22'

def slug(t):
    import unicodedata
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', t).strip('-')

def doc_page(fname, title, h1, desc, kicker, summary, sections):
    toc = '\n'.join(f'        <li><a href="#{slug(h)}">{h}</a></li>' for h, _ in sections)
    body = '\n'.join(f'''      <section id="{slug(h)}" aria-labelledby="{slug(h)}-t">
        <h2 id="{slug(h)}-t">{i}. {h}</h2>
{c}
      </section>''' for i, (h, c) in enumerate(sections, 1))
    summ = '\n'.join(f'        <li>{s}</li>' for s in summary)
    html = head(title, desc, fname) + header() + f'''<main id="conteudo">
  <div class="wrap">
    <div class="doc-hero">
      <h1>{h1}</h1>
      <p class="meta">Última atualização: <time datetime="{UPDATED_ISO}">{UPDATED}</time></p>
      <div class="doc-summary">
        <h2>Em resumo</h2>
        <ul>
{summ}
        </ul>
      </div>
    </div>
    <div class="doc-layout">
      <nav class="toc" aria-labelledby="toc-t">
        <h2 id="toc-t">Nesta página</h2>
        <ol>
{toc}
        </ol>
      </nav>
      <article class="doc">
{body}
      </article>
    </div>
  </div>
</main>
''' + footer()
    open(os.path.join(ROOT, fname), 'w').write(html)
    print(fname, len(html))

P = lambda *ps: '\n'.join(f'        <p>{p}</p>' for p in ps)
UL = lambda *xs: '        <ul>\n' + '\n'.join(f'          <li>{x}</li>' for x in xs) + '\n        </ul>'

CONTROLADOR = P(
 'Este site é da <strong>Clínica Veterinária Anvet</strong>, Av. Dona Belmira Marin, 1801, Parque Brasil, São Paulo, SP, CEP 04846-010. Para os fins da Lei Geral de Proteção de Dados (Lei nº 13.709/2018, LGPD), a clínica é a controladora dos dados pessoais tratados a partir deste site e das conversas iniciadas por ele.',
 'Contato para assuntos de privacidade: WhatsApp <a class="link" href="https://wa.me/5511992999988" target="_blank" rel="noopener">(11) 99299-9988</a>, telefone <a class="link" href="tel:+551159398706">(11) 5939-8706</a> ou presencialmente na recepção.')

# ---------------- Política de Privacidade ----------------
priv = [
 ('Quem é responsável pelos dados', CONTROLADOR),
 ('Quais dados o site trata', P(
   'O site é uma página informativa. Ele não tem área de cadastro, não exige login e não grava o que você digita. Os dados envolvidos são estes:') + '\n' + '''        <table>
          <thead><tr><th scope="col">Situação</th><th scope="col">Dados</th><th scope="col">Onde ficam</th></tr></thead>
          <tbody>
            <tr><td data-label="Situação">Formulário “Monte sua mensagem”</td><td data-label="Dados">Seu nome, nome e espécie do animal, assunto, período preferido e o texto livre que você escrever.</td><td data-label="Onde ficam">Só no seu navegador, enquanto a página está aberta. O site não envia esses dados para nenhum servidor.</td></tr>
            <tr><td data-label="Situação">Ao tocar em “Abrir no WhatsApp”</td><td data-label="Dados">O texto montado e o seu número de WhatsApp.</td><td data-label="Onde ficam">No WhatsApp (Meta) e no WhatsApp da clínica, depois que você enviar a mensagem.</td></tr>
            <tr><td data-label="Situação">Acesso a qualquer página</td><td data-label="Dados">Endereço IP, data e hora, página pedida, navegador e sistema (registros técnicos de acesso).</td><td data-label="Onde ficam">Nos servidores do GitHub Pages, que hospeda o site.</td></tr>
          </tbody>
        </table>''' + '\n' + P(
   'Para que o atendimento aconteça, você pode contar ao WhatsApp da clínica informações sobre a saúde do seu animal. Evite enviar dados de saúde de pessoas, documentos pessoais ou dados de pagamento por mensagem.')),
 ('Como o formulário funciona', P(
   'O formulário apenas organiza um texto. Quando você toca em “Montar mensagem”, o próprio navegador junta as respostas e mostra uma prévia. Nada é enviado nesse momento.',
   'Se você tocar em “Abrir no WhatsApp”, o texto é colocado em um link do WhatsApp. A mensagem só chega à clínica se você enviá-la no aplicativo. Montar a mensagem não confirma consulta, horário nem serviço: a equipe responde pelo WhatsApp no horário de atendimento.',
   'Se você fechar ou recarregar a página, as respostas se perdem. O site não usa armazenamento local do navegador para guardá-las.')),
 ('Para que os dados são usados', UL(
   'Responder dúvidas e pedidos enviados pelo WhatsApp ou telefone.',
   'Combinar consultas, exames, terapias e o táxi dog.',
   'Manter o site disponível e seguro (registros técnicos de acesso, tratados pela hospedagem).')),
 ('Bases legais', P('As bases legais previstas na LGPD (art. 7º) que se aplicam a cada finalidade, sujeitas à validação jurídica da clínica, são:') + '\n' + UL(
   '<strong>Procedimentos preliminares a um contrato</strong>, a pedido do titular (art. 7º, V): responder ao contato que você iniciou e combinar um atendimento.',
   '<strong>Legítimo interesse</strong> (art. 7º, IX): manter o site funcionando e protegido contra abuso, por meio dos registros técnicos da hospedagem.',
   '<strong>Cumprimento de obrigação legal ou regulatória</strong> (art. 7º, II), quando houver registros que a clínica precise manter por lei.')),
 ('Com quem os dados são compartilhados', UL(
   '<strong>GitHub, Inc.</strong> hospeda o site e registra o endereço IP de quem o acessa, por motivos de segurança, conforme a <a class="link" href="https://docs.github.com/pt/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">Declaração de Privacidade do GitHub</a>. A empresa fica nos Estados Unidos, o que pode envolver transferência internacional de dados.',
   '<strong>WhatsApp (Meta)</strong> trata as mensagens que você decidir enviar, conforme a política de privacidade do próprio aplicativo.',
   '<strong>Google Maps e Waze</strong> só recebem dados se você tocar nos botões de rota, que abrem esses serviços fora do site.',
   '<strong>Instagram</strong> só é acessado se você seguir o link para o perfil da clínica.') + '\n' + P('A clínica não vende dados pessoais.')),
 ('Cookies, fontes e medição de audiência', P(
   'O site não cria cookies, não usa ferramentas de análise de audiência, pixels de anúncios nem armazenamento local do navegador. As fontes, imagens e vídeos são servidos pelo próprio site, sem chamadas a serviços de terceiros ao carregar a página.',
   'Por isso não há aviso de cookies. Se algum desses recursos for adicionado no futuro, esta política será atualizada antes.')),
 ('Por quanto tempo os dados ficam guardados', UL(
   'Formulário: os dados ficam apenas na página aberta e são descartados ao fechá-la.',
   'Conversas no WhatsApp e registros de atendimento: pelo tempo necessário para o atendimento e para cumprir obrigações legais e regulatórias da clínica.',
   'Registros técnicos de acesso: pelo prazo definido pelo GitHub em sua política de privacidade.')),
 ('Seus direitos', P('Pela LGPD (art. 18), você pode pedir à clínica:') + '\n' + UL(
   'confirmação de que tratamos seus dados e acesso a eles;',
   'correção de dados incompletos, inexatos ou desatualizados;',
   'anonimização, bloqueio ou eliminação de dados desnecessários ou tratados em desacordo com a lei;',
   'portabilidade, informação sobre com quem os dados foram compartilhados e revisão de decisões automatizadas, quando aplicável;',
   'eliminação dos dados tratados com base no consentimento e revogação desse consentimento, quando for o caso.') + '\n' + P(
   'Faça o pedido pelos canais da seção 1. A clínica pode pedir informações para confirmar sua identidade antes de atender. Você também pode apresentar reclamação à <a class="link" href="https://www.gov.br/anpd/pt-br" target="_blank" rel="noopener">Autoridade Nacional de Proteção de Dados (ANPD)</a>.')),
 ('Segurança', P(
   'O site é servido por conexão criptografada (HTTPS). Como o formulário não envia dados a servidores, não há banco de dados do site a proteger. Mesmo assim, nenhum sistema na internet é totalmente imune a falhas; por isso pedimos que você não envie pelo site ou pelo WhatsApp informações além das necessárias para o atendimento.')),
 ('Crianças e adolescentes', P(
   'O site não se destina à coleta de dados de crianças. Se um menor de idade precisar de atendimento para seu animal, pedimos que o contato seja feito por um responsável.')),
 ('Mudanças nesta política', P(
   'Esta política pode mudar quando o site ou os canais de atendimento mudarem. A data no topo indica a versão em vigor. Mudanças relevantes serão destacadas nesta página.')),
]
doc_page('politica-de-privacidade.html',
  'Política de Privacidade | Clínica Veterinária Anvet',
  'Política de Privacidade',
  'Como o site da Clínica Veterinária Anvet trata dados pessoais: formulário que só monta a mensagem no navegador, WhatsApp, hospedagem e seus direitos pela LGPD.',
  'Privacidade',
  ['O formulário só monta um texto no seu navegador. O site não envia nem guarda o que você digita.',
   'A mensagem só chega à clínica se você enviá-la pelo WhatsApp. Enviar não confirma consulta ou horário.',
   'A hospedagem (GitHub Pages) registra o endereço IP de quem acessa o site, por segurança.',
   'O site não usa cookies, análise de audiência nem fontes de terceiros.',
   'Você pode exercer seus direitos da LGPD pelo WhatsApp, telefone ou na recepção.'],
  priv)

# ---------------- Termos ----------------
terms = [
 ('Quem mantém o site', CONTROLADOR.replace('Para os fins da Lei Geral de Proteção de Dados (Lei nº 13.709/2018, LGPD), a clínica é a controladora dos dados pessoais tratados a partir deste site e das conversas iniciadas por ele.', 'A clínica é responsável pelo conteúdo publicado aqui.').replace('Contato para assuntos de privacidade', 'Contato')),
 ('Para que serve o site', P(
   'O site apresenta a clínica, seus serviços, horários, endereço e canais de contato. Ele é informativo: não vende produtos, não recebe pagamentos e não faz agendamentos automáticos.',
   'Ao usar o site, você concorda com estes termos. Se não concordar, use diretamente o telefone ou a recepção da clínica.')),
 ('Uso dos canais de contato', P('Os canais de WhatsApp e telefone existem para tutores falarem com a equipe. Pedimos que você:') + '\n' + UL(
   'use os canais para dúvidas, pedidos de atendimento e assuntos ligados à clínica;',
   'informe dados verdadeiros sobre você e o seu animal;',
   'não envie conteúdo ofensivo, propaganda, correntes ou arquivos sem relação com o atendimento;',
   'não envie dados de saúde de pessoas, documentos pessoais ou dados de pagamento sem que a equipe peça.')),
 ('Como funcionam os pedidos', P(
   'O formulário do site monta uma mensagem pronta e abre o WhatsApp. A mensagem só é enviada se você a enviar no aplicativo.',
   'Enviar um pedido <strong>não é</strong> o mesmo que ter um atendimento confirmado. Consulta, horário, exame, terapia ou táxi dog só estão confirmados quando a equipe da clínica confirmar diretamente com você. As respostas acontecem no horário de funcionamento, de segunda a sábado, das 9h às 18h; em feriados, o horário pode mudar.',
   'Valores, formas de pagamento e condições de planos como o Petlove são informados pela equipe no contato e podem mudar.')),
 ('Emergências e limites das informações', P(
   'As informações do site são gerais. Elas não substituem a avaliação de um médico veterinário, que é necessária para diagnóstico, prescrição e tratamento do seu animal.',
   'Fora do horário de atendimento, ou em situações graves, procure imediatamente um serviço veterinário de emergência. Não espere a resposta de uma mensagem.')),
 ('Links para outros serviços', P(
   'O site tem links para WhatsApp, Instagram, Google Maps e Waze. Esses serviços têm seus próprios termos e políticas, e a clínica não controla seu funcionamento nem seu conteúdo.')),
 ('Fotos, vídeos e marca', P(
   'Os textos, fotos, vídeos e o logotipo publicados no site são do acervo da Clínica Veterinária Anvet ou usados com autorização. Não é permitido copiá-los, alterá-los ou usá-los em outros sites ou materiais sem autorização prévia da clínica.',
   'As fontes tipográficas Gabarito e Onest são usadas sob a SIL Open Font License.')),
 ('Privacidade', P(
   'O tratamento de dados pessoais está descrito na <a class="link" href="politica-de-privacidade.html">Política de Privacidade</a>.')),
 ('Mudanças nestes termos', P(
   'Estes termos podem ser atualizados quando o site ou os serviços mudarem. A data no topo indica a versão em vigor.')),
 ('Lei aplicável e contato', P(
   'Estes termos seguem as leis brasileiras. Nada aqui limita direitos garantidos pelo Código de Defesa do Consumidor ou por outras leis.',
   'Dúvidas sobre estes termos podem ser enviadas pelos canais da seção 1.')),
]
doc_page('termos-e-condicoes.html',
  'Termos e Condições de Uso | Clínica Veterinária Anvet',
  'Termos e Condições de Uso',
  'Regras de uso do site da Clínica Veterinária Anvet: finalidade informativa, canais de contato, como funcionam os pedidos e limites das informações.',
  'Termos de uso',
  ['O site é informativo. Ele não vende, não cobra e não agenda automaticamente.',
   'Um pedido enviado pelo WhatsApp só vira atendimento quando a equipe confirmar.',
   'As informações do site não substituem a avaliação de um médico veterinário.',
   'Em emergências fora do horário, procure um serviço veterinário de emergência.',
   'Fotos, vídeos e logotipo pertencem à clínica e não podem ser reutilizados sem autorização.'],
  terms)

# ---------------- 404 ----------------
PRE = '/Anvet/'
nf = head('Página não encontrada | Clínica Veterinária Anvet',
          'Esta página não existe no site da Clínica Veterinária Anvet.',
          '404.html', prefix=PRE, robots='noindex', og=False) + header(PRE) + f'''<main id="conteudo">
  <div class="wrap notfound">
    <div>
      <h1>Esta página não existe.</h1>
      <p class="lead">Erro 404: o endereço pode ter mudado ou ter sido digitado com algum erro. As informações da clínica continuam na página inicial.</p>
      <div class="actions">
        <a class="btn" href="{PRE}">Ir para a página inicial</a>
        <a class="btn btn--quiet" href="https://wa.me/5511992999988" target="_blank" rel="noopener">Falar no WhatsApp</a>
      </div>
    </div>
    <figure>
      {pic('fachada-clinica', [480, 800], '(max-width: 760px) 360px, 40vw', 'Fachada da Clínica Veterinária Anvet na Av. Dona Belmira Marin.', prefix=PRE)}
    </figure>
  </div>
</main>
''' + footer(PRE)
open(os.path.join(ROOT, '404.html'), 'w').write(nf)
print('404.html', len(nf))
