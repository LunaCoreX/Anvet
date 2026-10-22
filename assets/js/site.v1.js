/* Clínica Veterinária Anvet — script compartilhado. Sem dependências. */
(function () {
  "use strict";
  var WA = "5511992999988";
  var mq = function (q) { return window.matchMedia ? window.matchMedia(q).matches : false; };
  var reduce = mq("(prefers-reduced-motion: reduce)");
  var saveData = !!(navigator.connection && navigator.connection.saveData);

  /* Cabeçalho: linha discreta ao rolar */
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () { header.classList.toggle("scrolled", window.scrollY > 8); };
    window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
  }

  /* Menu no celular */
  var mb = document.getElementById("menu-btn"), nav = document.getElementById("nav");
  if (mb && nav) {
    var closeMenu = function () { nav.classList.remove("open"); mb.setAttribute("aria-expanded", "false"); mb.textContent = "Menu"; };
    mb.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      mb.setAttribute("aria-expanded", open ? "true" : "false");
      mb.textContent = open ? "Fechar" : "Menu";
      if (open) { var first = nav.querySelector("a"); if (first) first.focus(); }
    });
    nav.addEventListener("click", function (e) { if (e.target.closest("a")) closeMenu(); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) { closeMenu(); mb.focus(); } });
    document.addEventListener("click", function (e) { if (nav.classList.contains("open") && !e.target.closest(".site-header")) closeMenu(); });
  }

  /* Horário: informação tranquila, no fuso de São Paulo */
  var status = document.getElementById("status");
  function spNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-US", { timeZone: "America/Sao_Paulo", weekday: "short", hour: "numeric", minute: "numeric", hour12: false }).formatToParts(new Date());
      var o = {}; parts.forEach(function (p) { o[p.type] = p.value; });
      var days = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 };
      return { day: days[o.weekday], mins: (parseInt(o.hour, 10) % 24) * 60 + parseInt(o.minute, 10) };
    } catch (e) { return null; }
  }
  function updateStatus() {
    if (!status) return;
    var t = spNow(); if (!t) return;
    var workday = t.day >= 1 && t.day <= 6, open = workday && t.mins >= 540 && t.mins < 1080, txt;
    if (open) txt = "Aberto agora, atende até as 18h";
    else if (workday && t.mins < 540) txt = "Abre hoje às 9h";
    else if (t.day >= 1 && t.day <= 5) txt = "Abre amanhã às 9h";
    else txt = "Abre na segunda-feira às 9h";
    status.dataset.open = open ? "true" : "false";
    status.querySelector("[data-status-text]").textContent = txt;
  }
  updateStatus(); setInterval(updateStatus, 60000);

  /* Vídeos: capa leve, um por vez, controle acessível */
  var boxes = [].slice.call(document.querySelectorAll("[data-video]"));
  var canAuto = !reduce && !saveData && mq("(hover: hover) and (pointer: fine)");
  function setBtn(box, playing) {
    var b = box.querySelector(".vplay"); if (!b) return;
    b.setAttribute("aria-pressed", playing ? "true" : "false");
    b.querySelector("[data-label]").textContent = playing ? "Pausar" : "Reproduzir";
  }
  function pauseAll(except) {
    boxes.forEach(function (box) { var v = box.querySelector("video"); if (v !== except && !v.paused) v.pause(); });
  }
  boxes.forEach(function (box) {
    var v = box.querySelector("video"), b = box.querySelector(".vplay");
    v.addEventListener("play", function () { pauseAll(v); setBtn(box, true); });
    v.addEventListener("pause", function () { setBtn(box, false); });
    b.addEventListener("click", function () {
      if (v.paused) { box.dataset.user = "play"; v.play().catch(function () {}); }
      else { box.dataset.user = "pause"; v.pause(); }
    });
  });
  if ("IntersectionObserver" in window && boxes.length) {
    var vio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        var box = en.target, v = box.querySelector("video");
        if (!en.isIntersecting) { if (!v.paused) v.pause(); return; }
        if (canAuto && en.intersectionRatio >= 0.6 && box.dataset.user !== "pause") {
          var playing = boxes.some(function (b) { var x = b.querySelector("video"); return x !== v && !x.paused; });
          if (!playing) v.play().catch(function () {});
        }
      });
    }, { threshold: [0, 0.6] });
    boxes.forEach(function (box) { vio.observe(box); });
  }
  document.addEventListener("visibilitychange", function () { if (document.hidden) pauseAll(null); });

  /* Copiar */
  function copyText(text, btn, target) {
    var label = btn.textContent;
    var done = function (msg) { btn.textContent = msg; setTimeout(function () { btn.textContent = label; }, 1800); };
    var fallback = function () {
      if (!target) return;
      var r = document.createRange(); r.selectNodeContents(target);
      var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); done("Texto selecionado");
    };
    try { navigator.clipboard.writeText(text).then(function () { done("Copiado"); }, fallback); } catch (e) { fallback(); }
  }
  [].forEach.call(document.querySelectorAll("[data-copy]"), function (b) {
    b.addEventListener("click", function () { copyText(b.dataset.copy, b, b.parentElement.querySelector("strong")); });
  });

  /* Formulário: monta a mensagem no navegador; nada é enviado pelo site */
  var form = document.getElementById("form");
  if (form) {
    var result = document.getElementById("result"), preview = document.getElementById("preview"), wa = document.getElementById("wa-link");
    var assuntos = {
      consulta: "tirar uma dúvida sobre consulta", valores: "saber os valores", vacina: "saber sobre vacinas", imagem: "saber sobre raio-X ou ultrassom",
      lab: "saber sobre exames laboratoriais", cirurgia: "saber sobre cirurgia ou castração", fisio: "pedir uma avaliação de fisioterapia",
      acupuntura: "pedir uma avaliação de acupuntura", silvestre: "agendar uma consulta para animal silvestre", taxi: "pedir o táxi dog",
      petlove: "saber como usar o Petlove na clínica", outro: "tirar uma dúvida"
    };
    var rules = {
      "f-nome": function (v) { return v.trim().length >= 2 ? "" : "Escreva seu nome para a equipe saber com quem está falando."; },
      "f-especie": function (v) { return v ? "" : "Escolha a espécie do seu animal."; },
      "f-motivo": function (v) { return v ? "" : "Escolha o assunto da mensagem."; }
    };
    var check = function (id) {
      var el = document.getElementById(id), msg = rules[id](el.value), err = document.getElementById("e-" + id.slice(2));
      el.setAttribute("aria-invalid", msg ? "true" : "false");
      err.textContent = msg; err.hidden = !msg;
      return !msg;
    };
    Object.keys(rules).forEach(function (id) {
      var el = document.getElementById(id);
      el.addEventListener("blur", function () { if (el.value || el.getAttribute("aria-invalid") === "true") check(id); });
      ["input", "change"].forEach(function (ev) { el.addEventListener(ev, function () { if (el.getAttribute("aria-invalid") === "true") check(id); }); });
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var first = null;
      Object.keys(rules).forEach(function (id) { if (!check(id) && !first) first = document.getElementById(id); });
      if (first) { first.focus(); result.hidden = true; return; }
      var d = new FormData(form);
      var nome = String(d.get("nome")).trim(), pet = String(d.get("pet") || "").trim(), esp = d.get("especie"), mot = d.get("motivo"), per = d.get("periodo"), msg = String(d.get("mensagem") || "").trim();
      var espTxt = { "Cão": "cão", "Gato": "gato", "Animal silvestre": "animal silvestre", "Outro animal": "outro animal" }[esp] || esp;
      var linhas = ["Olá, Anvet! Meu nome é " + nome + "."];
      linhas.push(pet ? "Meu animal se chama " + pet + " (" + espTxt + ")." : "Tenho um " + espTxt + ".");
      linhas.push("Gostaria de " + assuntos[mot] + ".");
      if (per) linhas.push("Melhor período para mim: " + String(per).toLowerCase() + ".");
      if (msg) linhas.push(msg);
      var texto = linhas.join("\n");
      preview.textContent = texto;
      wa.href = "https://wa.me/" + WA + "?text=" + encodeURIComponent(texto);
      result.hidden = false;
      result.focus();
    });
    var cm = document.getElementById("copy-msg");
    if (cm) cm.addEventListener("click", function () { copyText(preview.textContent, cm, preview); });
  }

  /* Pastilhas do balcão da recepção, desenhadas no fundo da seção de visita */
  var cv = document.getElementById("tiles");
  function drawTiles() {
    if (!cv) return;
    var rect = cv.getBoundingClientRect(), dpr = Math.min(window.devicePixelRatio || 1, 2);
    if (!rect.width) return;
    cv.width = Math.round(rect.width * dpr); cv.height = Math.round(rect.height * dpr);
    var ctx = cv.getContext("2d"), cs = getComputedStyle(document.documentElement);
    var cols = ["--tile-1", "--tile-2", "--tile-3", "--tile-3", "--tile-4", "--tile-2", "--tile-5"].map(function (k) { return cs.getPropertyValue(k).trim(); });
    var size = (rect.width < 600 ? 22 : 30) * dpr, gap = Math.max(2, Math.round(2.5 * dpr));
    ctx.fillStyle = cs.getPropertyValue("--grout").trim(); ctx.fillRect(0, 0, cv.width, cv.height);
    var seed = 1801;
    var rnd = function () { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; };
    for (var y = 0; y < cv.height; y += size) for (var x = 0; x < cv.width; x += size) {
      ctx.fillStyle = cols[Math.floor(rnd() * cols.length)];
      ctx.fillRect(x + gap / 2, y + gap / 2, size - gap, size - gap);
    }
  }
  if (cv) {
    var drawWhenVisible = function () {
      if ("IntersectionObserver" in window) {
        var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { drawTiles(); io.disconnect(); } }, { rootMargin: "400px" });
        io.observe(cv);
      } else drawTiles();
    };
    drawWhenVisible();
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(drawTiles, 150); });
    if (window.matchMedia) { var dm = window.matchMedia("(prefers-color-scheme: dark)"); if (dm.addEventListener) dm.addEventListener("change", drawTiles); }
  }

  var y = document.getElementById("year"); if (y) y.textContent = String(new Date().getFullYear());
})();
