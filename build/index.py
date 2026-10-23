import sys; sys.path.insert(0,'/home/claude/site/build')
from common import *
title='Clínica Veterinária Anvet | Veterinária no Grajaú, São Paulo'
desc='Clínica veterinária no Parque Brasil, região do Grajaú (São Paulo). Consultas para cães e gatos sem agendamento, de segunda a sábado, das 9h às 18h. Exames, raio-X, ultrassom, cirurgias, fisioterapia e acupuntura.'
ld='''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VeterinaryCare",
  "@id": "https://lunacorex.github.io/Anvet/#clinica",
  "name": "Clínica Veterinária Anvet",
  "url": "https://lunacorex.github.io/Anvet/",
  "logo": "https://lunacorex.github.io/Anvet/assets/icons/icone-512.png",
  "image": "https://lunacorex.github.io/Anvet/assets/images/compartilhamento-anvet-1200x630.jpg",
  "description": "Clínica veterinária no Parque Brasil, região do Grajaú, em São Paulo. Consultas para cães e gatos sem agendamento.",
  "telephone": "+55-11-5939-8706",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Av. Dona Belmira Marin, 1801 - Parque Brasil",
    "addressLocality": "São Paulo",
    "addressRegion": "SP",
    "postalCode": "04846-010",
    "addressCountry": "BR"
  },
  "openingHoursSpecification": [{
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
    "opens": "09:00",
    "closes": "18:00"
  }],
  "sameAs": ["https://www.instagram.com/_anvet/"]
}
</script>'''
hero_sizes_m='calc(100vw - 32px)'
heroimg=f'''<picture>
            <source media="(max-width: 760px)" type="image/avif" srcset="assets/images/recepcao-balcao-pastilhas-horizontal-480.avif 480w, assets/images/recepcao-balcao-pastilhas-horizontal-720.avif 720w, assets/images/recepcao-balcao-pastilhas-horizontal-960.avif 960w" sizes="{hero_sizes_m}" width="720" height="540">
            <source media="(max-width: 760px)" type="image/webp" srcset="assets/images/recepcao-balcao-pastilhas-horizontal-480.webp 480w, assets/images/recepcao-balcao-pastilhas-horizontal-720.webp 720w, assets/images/recepcao-balcao-pastilhas-horizontal-960.webp 960w" sizes="{hero_sizes_m}" width="720" height="540">
            <source type="image/avif" srcset="assets/images/recepcao-balcao-pastilhas-480.avif 480w, assets/images/recepcao-balcao-pastilhas-720.avif 720w, assets/images/recepcao-balcao-pastilhas-960.avif 960w, assets/images/recepcao-balcao-pastilhas-1200.avif 1200w" sizes="(max-width: 1240px) 38vw, 470px">
            <img src="assets/images/recepcao-balcao-pastilhas-720.webp" srcset="assets/images/recepcao-balcao-pastilhas-480.webp 480w, assets/images/recepcao-balcao-pastilhas-720.webp 720w, assets/images/recepcao-balcao-pastilhas-960.webp 960w, assets/images/recepcao-balcao-pastilhas-1200.webp 1200w" sizes="(max-width: 1240px) 38vw, 470px" width="720" height="899" alt="Médica veterinária da Anvet, de uniforme azul, agachada com um cachorro branco no colo, em frente ao balcão de pastilhas verdes da recepção." fetchpriority="high">
          </picture>'''
gs='(max-width: 900px) 50vw, 400px'
html=head(title,desc,'',extra=ld)+header(home=True)+f'''
<main id="conteudo">
  <section class="hero" id="inicio" aria-labelledby="titulo">
    <div class="wrap hero-grid">
      <div class="hero-copy">
        <h1 id="titulo">Veterinária <span>no Grajaú</span></h1>
        <p class="lead">A Clínica Veterinária Anvet atende cães e gatos há mais de 25 anos, sem agendamento e com preço popular.</p>
        <div class="hero-cta">
          <a class="btn" href="https://wa.me/5511992999988" target="_blank" rel="noopener">{WA_SVG}Falar no WhatsApp</a>
          <p class="status" id="status" data-open="false"><strong><i aria-hidden="true"></i><span data-status-text>Segunda a sábado, das 9h às 18h</span></strong><small>Em feriados, o horário pode mudar. Os avisos saem no Instagram.</small></p>
        </div>
        <p class="hero-where"><span><span class="tile" aria-hidden="true"></span> Av. Dona Belmira Marin, 1801, Parque Brasil</span><a class="link" href="#visita">Ver como chegar</a></p>
      </div>
      <figure class="hero-photo">
        <div class="frame">
          {heroimg}
        </div>
        <figcaption>Recepção da Anvet, com o balcão de pastilhas verdes.</figcaption>
      </figure>
    </div>
  </section>

  <section class="how" id="atendimento" aria-labelledby="how-titulo">
    <div class="wrap">
      <div class="how-head">
        <h2 id="how-titulo">Como funciona o atendimento</h2>
        <p>Uma única unidade, de segunda a sábado, das 9h às 18h. Para a consulta, é só chegar. Alguns serviços são combinados antes.</p>
      </div>
      <ul class="rules">
        <li><span class="tile" aria-hidden="true"></span><h3>Consulta</h3><p>Sem hora marcada: chegue no horário de atendimento e a recepção encaminha seu animal.</p><span class="tag">Sem agendamento</span></li>
        <li><span class="tile" aria-hidden="true"></span><h3>Plano Petlove</h3><p>A clínica aceita o plano Petlove, com a mesma regra da consulta. Leve os dados do plano.</p><span class="tag">Sem agendamento</span></li>
        <li><span class="tile" aria-hidden="true"></span><h3>Táxi dog</h3><p>Leva o animal e o tutor juntos até a clínica. Peça pelo WhatsApp com antecedência e aguarde a confirmação do horário.</p><span class="tag">Com agendamento</span></li>
        <li><span class="tile" aria-hidden="true"></span><h3>Acupuntura e fisioterapia</h3><p>Começam por uma avaliação, marcada na recepção ou pelo WhatsApp.</p><span class="tag">Com agendamento</span></li>
      </ul>
    </div>
  </section>

  <section class="section svc-section" id="servicos" aria-labelledby="servicos-titulo">
    <div class="wrap">
      <div class="svc-top">
        <h2 id="servicos-titulo">Do check&#8209;up à cirurgia</h2>
        <p class="lead">Consulta, exames, cirurgia e reabilitação no mesmo endereço, sem levar seu animal a outro lugar.</p>
      </div>
      <ul class="svc-cards">
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M8 4v7a6 6 0 0 0 12 0V4"/><path d="M6 4h4M18 4h4"/><path d="M14 17v4a6 6 0 0 0 12 0v-2"/><circle cx="26" cy="16" r="3"/></svg></span><h3>Consultas</h3><p>Sem hora marcada</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 4l7 7"/><path d="M24.5 7.5 11 21l-4-4L20.5 3.5"/><path d="M15 9l3 3M12 12l3 3"/><path d="M9 19l-5 5M4 24l4 4"/></svg></span><h3>Vacinas</h3><p>Cães e gatos</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="24" height="17" rx="2.5"/><path d="M11 27h10M16 22v5"/><path d="M12 10a2 2 0 1 1 3 1.7v3.6a2 2 0 1 1-3 1.7M20 10a2 2 0 1 0-3 1.7v3.6a2 2 0 1 0 3 1.7"/></svg></span><h3>Raio-X e ultrassom</h3><p>Raio-X com laudo</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4h8M13 4v9L6.5 24.5A2.5 2.5 0 0 0 8.7 28h14.6a2.5 2.5 0 0 0 2.2-3.5L19 13V4"/><path d="M9.5 19h13"/></svg></span><h3>Exames laboratoriais</h3><p>Laboratório na clínica</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 27 21.5 10.5a3.5 3.5 0 0 1 5 5L10 27H5z"/><path d="M16 16l5 5"/><circle cx="8" cy="8" r="4"/><path d="M8 6v4M6 8h4"/></svg></span><h3>Cirurgia e castração</h3><p>Centro cirúrgico próprio</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17h6l3-7 5 14 3-7h9"/></svg></span><h3>Fisioterapia e acupuntura</h3><p>Começa com avaliação</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 20l2.5-7A3 3 0 0 1 10.3 11h11.4a3 3 0 0 1 2.8 2l2.5 7"/><rect x="3" y="20" width="26" height="5" rx="2"/><circle cx="9" cy="25" r="2.2"/><circle cx="23" cy="25" r="2.2"/></svg></span><h3>Táxi dog</h3><p>Leva o animal e o tutor</p></li>
        <li class="svc-card"><span class="svc-icon"><svg viewBox="0 0 32 32" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 9a4 4 0 0 0-8 0c0 3-4 5-6 8 4 0 7 1 9 4 2-3 3-5 3-8"/><path d="M20 9h5l-3 3"/><path d="M15 21v6M12 27h6"/><circle cx="16.5" cy="8.5" r=".6" fill="currentColor"/></svg></span><h3>Animais silvestres</h3><p>Com agendamento</p></li>
      </ul>
      <div class="svc-foot">
        <details class="svc-all">
          <summary>Ver todos os serviços</summary>
          <div class="svc-grid">
            <div class="svc"><h3>Consultas e prevenção</h3><ul><li>Consultas clínicas</li><li>Vacinas</li><li>Microchipagem</li><li>Orientação nutricional</li><li>Animais silvestres, com agendamento</li></ul></div>
            <div class="svc"><h3>Exames e imagem</h3><ul><li>Exames laboratoriais</li><li>Raio-X com laudo</li><li>Ultrassom</li><li>Ecocardiograma e eletrocardiograma</li><li>Endoscopia</li></ul></div>
            <div class="svc"><h3>Cirurgia e ortopedia</h3><ul><li>Cirurgias</li><li>Castração</li><li>Ortopedia</li></ul></div>
            <div class="svc"><h3>Terapias e farmácia</h3><ul><li>Fisioterapia</li><li>Acupuntura</li><li>Especialidades veterinárias</li><li>Farmácia veterinária</li></ul></div>
          </div>
        </details>
        <a class="link" href="#mensagem">Perguntar sobre valores ou preparo</a>
      </div>
    </div>
  </section>

  <section class="section" id="clinica" aria-labelledby="clinica-titulo">
    <div class="wrap">
      <div class="inside-head">
        <h2 id="clinica-titulo">Por dentro da Anvet</h2>
        <p class="lead">Sala de consulta, centro cirúrgico, raio-X, fisioterapia e o táxi dog da clínica.</p>
      </div>
      <div class="gallery">
        {video('atendimento-consulta','Duas profissionais da Anvet examinam um cachorro branco sobre a bancada da sala de consulta.','Atendimento na sala de consulta.')}
        {video('centro-cirurgico','Centro cirúrgico da Anvet, com foco cirúrgico, mesa de inox e aparelho de anestesia.','Centro cirúrgico.')}
        {video('sala-raio-x','Aparelho de raio-X da clínica.','Sala de raio-X.')}
        <figure class="shot"><div class="frame">{pic('dra-laura-marques-gato',[400,800],gs,'Dra. Laura Marques, de jaleco branco, segura um gato rajado no colo.')}</div><figcaption>Dra. Laura Marques e um paciente felino.</figcaption></figure>
        <figure class="shot"><div class="frame">{pic('taxi-dog-anvet',[480,800],gs,'Carro branco do táxi dog com a marca verde Anvet e o telefone da clínica, estacionado na entrada.')}</div><figcaption>Táxi dog: leva o animal e o tutor juntos.</figcaption></figure>
        <figure class="shot"><div class="frame">{pic('fisioterapia-esteira',[400,720],gs,'Cadela caramelo caminha na esteira de fisioterapia apoiada por duas profissionais.')}</div><figcaption>Fisioterapia na esteira.</figcaption></figure>
      </div>
      <details class="more">
        <summary>Ver mais fotos e vídeos</summary>
        <div class="gallery">
          {video('laboratorio','Profissional prepara uma amostra no analisador do laboratório da clínica.','Laboratório.')}
          {video('farmacia','Prateleiras da farmácia veterinária da clínica.','Farmácia veterinária.')}
          <figure class="shot"><div class="frame">{pic('equipe-gato-preto',[400,800],'(max-width: 900px) 50vw, 300px','Profissional da Anvet, de uniforme azul, abraça um gato preto.')}</div><figcaption>Paciente felino no colo da equipe.</figcaption></figure>
          <figure class="shot"><div class="frame">{pic('dra-laura-marques-pitoco',[400,800],'(max-width: 900px) 50vw, 300px','Dra. Laura Marques segura no colo um cachorro pequeno preto e marrom.')}</div><figcaption>Dra. Laura Marques em consulta.</figcaption></figure>
        </div>
      </details>
    </div>
  </section>

  <section class="section" id="equipe" aria-labelledby="equipe-titulo">
    <div class="wrap team-wrap">
      <div class="team-head">
        <h2 id="equipe-titulo">Quem atende</h2>
        <p>Médicas veterinárias e equipe de apoio que recebem os tutores, conduzem consultas, exames e terapias.</p>
        <figure class="team-photo">
          {pic('equipe-corredor',[480,960],'(max-width: 900px) min(100vw, 520px), 360px','Quatro profissionais da Anvet de jaleco e uniforme lado a lado no corredor da clínica.')}
          <figcaption>Profissionais da Anvet no corredor da clínica.</figcaption>
        </figure>
      </div>
      <div class="team">
        <figure class="person">
          {pic('retrato-dra-laura-marques',[480],'(max-width: 560px) 112px, 360px','Retrato da Dra. Laura Marques sorrindo, com um cachorro de pelo claro no colo.')}
          <figcaption>
            <h3>Dra. Laura Marques</h3>
            <p class="role">Médica veterinária</p>
            <p>Atende cães e gatos em consultas e acompanha pacientes durante exames na clínica.</p>
          </figcaption>
        </figure>
        <figure class="person">
          {pic('retrato-dra-adriana',[480],'(max-width: 560px) 112px, 360px','Retrato da Dra. Adriana, de óculos e jaleco branco.')}
          <figcaption>
            <h3>Dra. Adriana</h3>
            <p class="role">Médica veterinária · Acupuntura</p>
            <p>Responsável pelas avaliações e sessões de acupuntura veterinária da Anvet.</p>
          </figcaption>
        </figure>
      </div>
    </div>
  </section>

  <section class="section" id="duvidas" aria-labelledby="duvidas-titulo">
    <div class="wrap split">
      <div class="split-head">
        <h2 id="duvidas-titulo">Dúvidas frequentes</h2>
        <p class="muted">Não encontrou a resposta? A recepção responde pelo WhatsApp.</p>
        <a class="link" href="#mensagem">Mandar uma pergunta</a>
      </div>
      <div class="faq">
        <details><summary>Quanto custa uma consulta?</summary><div><p>A Anvet trabalha com preço popular. Os valores de consultas, vacinas e exames são informados na recepção ou pelo WhatsApp.</p></div></details>
        <details><summary>A clínica atende emergências ou 24 horas?</summary><div><p>Não. O atendimento é de segunda a sábado, das 9h às 18h. Fora desse horário, em caso de emergência, procure um hospital veterinário 24 horas.</p></div></details>
        <details><summary>Quais animais são atendidos?</summary><div><p>Cães e gatos, sem agendamento. A clínica também atende animais silvestres; nesse caso, agende a consulta pelo WhatsApp antes de vir.</p></div></details>
        <details><summary>Aceitam outros planos além do Petlove?</summary><div><p>A clínica divulga apenas o Petlove. Para outro plano, confirme pelo WhatsApp antes de vir.</p></div></details>
        <details><summary>Como peço o táxi dog?</summary><div><p>Envie pelo WhatsApp seu endereço, o nome do animal e o horário em que precisa. O pedido só vale depois que a equipe confirmar a disponibilidade.</p></div></details>
        <details><summary>A clínica abre nos feriados?</summary><div><p>Depende do feriado. Os avisos de horário são publicados no Instagram <a href="https://www.instagram.com/_anvet/" target="_blank" rel="noopener">@_anvet</a>.</p></div></details>
      </div>
    </div>
  </section>

  <section class="visit" id="visita" aria-labelledby="visita-titulo">
    <canvas id="tiles" aria-hidden="true"></canvas>
    <div class="wrap">
      <div class="card">
        <h2 id="visita-titulo">Como chegar</h2>
        <figure class="facade">{pic('fachada-clinica',[480,800],'(max-width: 1000px) calc(100vw - 80px), 420px','Fachada verde da clínica com o letreiro Anvet Clínica Veterinária e a garagem de entrada.')}<figcaption>Procure a fachada verde com o letreiro Anvet.</figcaption></figure>
        <p class="addr">Av. Dona Belmira Marin, 1801<br>Parque Brasil, região do Grajaú<br>São Paulo, SP · <span class="num">CEP 04846-010</span></p>
        <dl class="hours" aria-label="Horário de atendimento">
          <dt>Segunda a sexta</dt><dd>9h às 18h</dd>
          <dt>Sábado</dt><dd>9h às 18h</dd>
          <dt class="closed">Domingo</dt><dd class="closed">Fechado</dd>
        </dl>
        <div class="routes">
          <a class="btn btn--sm" href="https://www.google.com/maps/dir/?api=1&amp;destination=Av.+Dona+Belmira+Marin,+1801+-+Parque+Brasil,+S%C3%A3o+Paulo+-+SP,+04846-010" target="_blank" rel="noopener">Rota no Google Maps</a>
          <a class="btn btn--sm" href="https://waze.com/ul?q=Av.%20Dona%20Belmira%20Marin%2C%201801%2C%20S%C3%A3o%20Paulo&amp;navigate=yes" target="_blank" rel="noopener">Rota no Waze</a>
        </div>
        <div class="contacts">
          <div class="contact-row"><div><span>WhatsApp</span><strong>(11) 99299-9988</strong></div><a class="chip-btn" href="https://wa.me/5511992999988" target="_blank" rel="noopener">Abrir</a></div>
          <div class="contact-row"><div><span>Telefone</span><strong>(11) 5939-8706</strong></div><a class="chip-btn" href="tel:+551159398706">Ligar</a></div>
        </div>
      </div>

      <div class="card" id="mensagem">
        <h2 id="form-titulo">Mande sua pergunta</h2>
        <ol class="steps">
          <li>Preencha os campos abaixo.</li>
          <li>Toque em <b>Montar mensagem</b>: o texto aparece nesta página. Nada é enviado pelo site.</li>
          <li>Abra o WhatsApp, confira o texto e envie. A clínica responde por lá.</li>
        </ol>
        <p class="small muted">Pedidos de táxi dog e de avaliação só valem depois que a equipe confirmar o horário. Veja como os dados são tratados na <a href="politica-de-privacidade.html">Política de Privacidade</a>.</p>
        <form class="form" id="form" novalidate aria-labelledby="form-titulo">
          <div class="field">
            <label for="f-nome">Seu nome</label>
            <input id="f-nome" name="nome" autocomplete="name" required minlength="2" aria-describedby="e-nome">
            <p class="err" id="e-nome" hidden></p>
          </div>
          <div class="field">
            <label for="f-pet">Nome do animal <span class="opt">(opcional)</span></label>
            <input id="f-pet" name="pet" autocomplete="off">
          </div>
          <div class="field">
            <label for="f-especie">Espécie</label>
            <select id="f-especie" name="especie" required aria-describedby="e-especie">
              <option value="">Escolha</option>
              <option>Cão</option>
              <option>Gato</option>
              <option>Animal silvestre</option>
              <option>Outro animal</option>
            </select>
            <p class="err" id="e-especie" hidden></p>
          </div>
          <div class="field">
            <label for="f-motivo">Assunto</label>
            <select id="f-motivo" name="motivo" required aria-describedby="e-motivo">
              <option value="">Escolha</option>
              <option value="consulta">Dúvida sobre consulta</option>
              <option value="valores">Valores</option>
              <option value="vacina">Vacinas</option>
              <option value="imagem">Raio-X ou ultrassom</option>
              <option value="lab">Exames laboratoriais</option>
              <option value="cirurgia">Cirurgia ou castração</option>
              <option value="fisio">Avaliação de fisioterapia</option>
              <option value="acupuntura">Avaliação de acupuntura</option>
              <option value="silvestre">Consulta para animal silvestre</option>
              <option value="taxi">Pedir táxi dog</option>
              <option value="petlove">Atendimento pelo Petlove</option>
              <option value="outro">Outro assunto</option>
            </select>
            <p class="err" id="e-motivo" hidden></p>
          </div>
          <div class="field">
            <label for="f-periodo">Melhor período <span class="opt">(opcional)</span></label>
            <select id="f-periodo" name="periodo">
              <option value="">Sem preferência</option>
              <option>Manhã</option>
              <option>Tarde</option>
            </select>
          </div>
          <div class="field full">
            <label for="f-msg">Mensagem <span class="opt">(opcional)</span></label>
            <textarea id="f-msg" name="mensagem" maxlength="600" aria-describedby="h-msg"></textarea>
            <p class="hint" id="h-msg">Não inclua dados de saúde de pessoas nem documentos. Para táxi dog, informe o bairro e o horário desejado.</p>
          </div>
          <div class="form-foot">
            <button class="btn" type="submit">Montar mensagem</button>
          </div>
          <div class="result" id="result" hidden tabindex="-1" aria-live="polite">
            <p><strong>Mensagem pronta, ainda não enviada.</strong> Confira o texto abaixo. Ao tocar em Abrir no WhatsApp, o aplicativo abre com a mensagem preenchida, e o envio acontece quando você confirmar por lá.</p>
            <pre id="preview"></pre>
            <div class="row">
              <a class="btn" id="wa-link" href="https://wa.me/5511992999988" target="_blank" rel="noopener">Abrir no WhatsApp</a>
              <button class="chip-btn" type="button" id="copy-msg">Copiar texto</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</main>

'''+footer()
html='\n'.join(l for l in html.split('\n') if l.strip()!='' or True)
open(ROOT+'/index.html','w').write(html)
print(len(html))
