(function(){
  // Endereço que recebe as mensagens do formulário. Troque pelo e-mail oficial da consultoria.
  var CONTACT_EMAIL = "contato@seudominio.com.br";

  try { document.getElementById("ano").textContent = new Date().getFullYear(); } catch(e){}

  // Menu mobile
  var btn = document.querySelector(".menu-btn"), nav = document.getElementById("menu");
  if (btn && nav) {
    btn.addEventListener("click", function(){
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
      btn.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    });
    nav.addEventListener("click", function(e){
      if (e.target.tagName === "A") { nav.classList.remove("open"); btn.setAttribute("aria-expanded","false"); btn.setAttribute("aria-label","Abrir menu"); }
    });
  }

  // Animação do hero (só na página inicial): sinal ruidoso que se organiza em curva de crescimento
  var line = document.getElementById("signal-line"), area = document.getElementById("signal-area"), dot = document.getElementById("signal-dot");
  if (line && area && dot) {
    var W = 560, H = 420, N = 56, noisy = [], clean = [];
    var seed = 7; var rnd = function(){ seed = (seed * 9301 + 49297) % 233280; return seed / 233280; };
    for (var i = 0; i < N; i++){
      var t = i / (N - 1);
      clean.push(360 - 300 * Math.pow(t, 1.8));
      noisy.push(220 + (rnd() - .5) * 230 * (1 - t * .3));
    }
    var render = function(k){
      var d = "", pts = [];
      for (var i = 0; i < N; i++){
        var x = 10 + (W - 20) * i / (N - 1);
        var y = noisy[i] + (clean[i] - noisy[i]) * k;
        pts.push([x, y]); d += (i ? " L" : "M") + x.toFixed(1) + " " + y.toFixed(1);
      }
      line.setAttribute("d", d);
      area.setAttribute("d", d + " L" + pts[N-1][0] + " " + H + " L" + pts[0][0] + " " + H + " Z");
      area.style.opacity = k;
      dot.setAttribute("cx", pts[N-1][0]); dot.setAttribute("cy", pts[N-1][1]);
    };
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) { render(1); }
    else {
      render(0);
      var start = null, delay = 500, dur = 2600;
      var ease = function(x){ return x < .5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2; };
      var step = function(ts){
        if (start === null) start = ts;
        var p = Math.min(1, Math.max(0, (ts - start - delay) / dur));
        render(ease(p));
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    }
  }

  // Formulário (só na página inicial): sem servidor e sem chaves; abre o e-mail do visitante com a mensagem pronta
  var form = document.getElementById("form-contato"), status = document.getElementById("form-status");
  if (form && status) {
    var valid = function(v){ return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); };
    form.addEventListener("submit", function(e){
      e.preventDefault();
      var nome = form.nome.value.trim(), email = form.email.value.trim(), msg = form.mensagem.value.trim();
      if (!nome || !msg || !valid(email)) {
        status.textContent = "Para continuar, preencha o nome, um e-mail válido e a mensagem.";
        (!nome ? form.nome : !valid(email) ? form.email : form.mensagem).focus();
        return;
      }
      var assunto = "Contato pelo site: " + form.interesse.value;
      var corpo = "Nome: " + nome + "\nEmpresa: " + form.empresa.value.trim() + "\nE-mail: " + email + "\nInteresse: " + form.interesse.value + "\n\n" + msg;
      window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(assunto) + "&body=" + encodeURIComponent(corpo);
      status.textContent = "Abrimos seu aplicativo de e-mail com a mensagem pronta. Se ele não abrir, escreva para " + CONTACT_EMAIL + ".";
    });
  }

  // Ilustrações e seções: animam quando entram na tela
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var revealSel = ".sec-head, .manifesto .cols, .cap-grid, .cap-wide, .deliv, .fit, .steps, .faq, .lead-grid, .related, .contact .cols, .callout .cols, .group-title, .princ-grid, .post-list, .article-body";
  var targets = [].slice.call(document.querySelectorAll(".illo"));
  [].forEach.call(document.querySelectorAll(revealSel), function(el){ el.classList.add("reveal"); targets.push(el); });
  if (reduceMotion || !("IntersectionObserver" in window)) {
    targets.forEach(function(el){ el.classList.add("in-view"); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){ if (en.isIntersecting) { en.target.classList.add("in-view"); io.unobserve(en.target); } });
    }, { threshold: 0.15, rootMargin: "0px 0px -40px 0px" });
    targets.forEach(function(el){ io.observe(el); });
  }

  // Ilustrações reagem ao mouse (camadas se movem em profundidades diferentes)
  if (!reduceMotion) {
    [].forEach.call(document.querySelectorAll(".illo-wrap"), function(wrap){
      var svg = wrap.querySelector(".illo"); if (!svg) return;
      wrap.addEventListener("pointermove", function(e){
        var r = wrap.getBoundingClientRect();
        svg.style.setProperty("--mx", (((e.clientX - r.left) / r.width) - .5).toFixed(3));
        svg.style.setProperty("--my", (((e.clientY - r.top) / r.height) - .5).toFixed(3));
      });
      wrap.addEventListener("pointerleave", function(){ svg.style.setProperty("--mx", 0); svg.style.setProperty("--my", 0); });
    });
  }
})();
