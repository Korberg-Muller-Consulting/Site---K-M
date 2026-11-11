
(function(){
  // Endereço que recebe as mensagens do formulário. Troque pelo e-mail oficial da consultoria.
  var CONTACT_EMAIL = "contato@seudominio.com.br";

  try { document.getElementById("ano").textContent = new Date().getFullYear(); } catch(e){}

  // Menu mobile
  var btn = document.querySelector(".menu-btn"), nav = document.getElementById("menu");
  btn.addEventListener("click", function(){
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    btn.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
  });
  nav.addEventListener("click", function(e){
    if (e.target.tagName === "A") { nav.classList.remove("open"); btn.setAttribute("aria-expanded","false"); btn.setAttribute("aria-label","Abrir menu"); }
  });

  // Animação do hero: sinal ruidoso que se organiza em curva de crescimento
  var line = document.getElementById("signal-line"), area = document.getElementById("signal-area"), dot = document.getElementById("signal-dot");
  var W = 560, H = 420, N = 56, noisy = [], clean = [];
  var seed = 7; function rnd(){ seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  for (var i = 0; i < N; i++){
    var t = i / (N - 1);
    clean.push(360 - 300 * Math.pow(t, 1.8));
    noisy.push(220 + (rnd() - .5) * 230 * (1 - t * .3));
  }
  function render(k){
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
  }
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) { render(1); }
  else {
    render(0);
    var start = null, delay = 500, dur = 2600;
    function ease(x){ return x < .5 ? 4*x*x*x : 1 - Math.pow(-2*x + 2, 3) / 2; }
    function step(ts){
      if (start === null) start = ts;
      var p = Math.min(1, Math.max(0, (ts - start - delay) / dur));
      render(ease(p));
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  // Formulário: sem servidor e sem chaves; abre o e-mail do visitante com a mensagem pronta
  var form = document.getElementById("form-contato"), status = document.getElementById("form-status");
  form.addEventListener("submit", function(e){
    e.preventDefault();
    var nome = form.nome.value.trim(), email = form.email.value.trim(), msg = form.mensagem.value.trim();
    if (!nome || !msg || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      status.textContent = "Para continuar, preencha o nome, um e-mail válido e a mensagem.";
      (!nome ? form.nome : (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) ? form.email : form.mensagem).focus();
      return;
    }
    var assunto = "Contato pelo site: " + form.interesse.value;
    var corpo = "Nome: " + nome + "\nEmpresa: " + form.empresa.value.trim() + "\nE-mail: " + email + "\nInteresse: " + form.interesse.value + "\n\n" + msg;
    window.location.href = "mailto:" + CONTACT_EMAIL + "?subject=" + encodeURIComponent(assunto) + "&body=" + encodeURIComponent(corpo);
    status.textContent = "Abrimos seu aplicativo de e-mail com a mensagem pronta. Se ele não abrir, escreva para " + CONTACT_EMAIL + ".";
  });
})();
