/* Sahara Nova — canvas effects: hero sky/dunes + agent flow diagrams.
   Decorative only: all text stays in HTML. Pauses off-screen / hidden tab.
   prefers-reduced-motion → a single still frame. */
(function () {
  'use strict';
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var COARSE = window.matchMedia && matchMedia('(pointer: coarse)').matches;
  var FRAME = COARSE ? 1000 / 30 : 1000 / 60;
  var GOLD = '242,181,68', OCHRE = '200,121,30', CREAM = '244,241,234';

  function dprOf() { return Math.min(window.devicePixelRatio || 1, COARSE ? 1.5 : 2); }

  /* Shared loop driver: runs draw(t, dt) while visible */
  function Loop(el, draw) {
    var raf = 0, last = 0, acc = 0, visible = false, running = false, t = 0;
    function frame(now) {
      raf = requestAnimationFrame(frame);
      var dt = last ? Math.min(now - last, 100) : 16; last = now; acc += dt;
      if (acc < FRAME - 1) return;
      t += acc / 1000; draw(t, acc / 1000); acc = 0;
    }
    function start() { if (!running && visible && !document.hidden && !RM) { running = true; last = 0; raf = requestAnimationFrame(frame); } }
    function stop() { running = false; cancelAnimationFrame(raf); }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; visible ? start() : stop(); }, { rootMargin: '80px' }).observe(el);
    } else { visible = true; }
    document.addEventListener('visibilitychange', function () { document.hidden ? stop() : start(); });
    return { start: start, stop: stop, still: function () { draw(t || 3.2, 0); } };
  }

  function rnd(a, b) { return a + Math.random() * (b - a); }

  /* ---------------- HERO: night sky over the Sahara ---------------- */
  function Hero(hero) {
    var cv = document.createElement('canvas');
    cv.className = 'hero-fx'; cv.setAttribute('aria-hidden', 'true');
    hero.insertBefore(cv, hero.firstChild);
    hero.classList.add('fx-on');
    var ctx = cv.getContext('2d'), w, h, dpr, stars = [], sand = [], nova = null, nextNova = 3;
    var px = 0, py = 0, tx = 0, ty = 0;
    var LAYERS = [
      { base: .74, amp: .07, f1: 1.6, f2: 4.1, v: .018, fill: ['#242B55', '#1B2140'], rim: .18 },
      { base: .82, amp: .085, f1: 1.15, f2: 3.2, v: .028, fill: ['#2B2A50', '#1D2143'], rim: .32 },
      { base: .92, amp: .10, f1: .8, f2: 2.4, v: .04, fill: ['#352B45', '#20213F'], rim: .55 }
    ];
    LAYERS.forEach(function (L) { L.p1 = rnd(0, 6); L.p2 = rnd(0, 6); });

    function ridge(L, i, x, t) {
      var u = x / w, env = .45 + .9 * u;          // taller dunes to the right, clear of the text
      return h * L.base - h * L.amp * env * (.55 + .45 * Math.sin(u * L.f1 * 6.283 + L.p1 + t * L.v * 6.283))
             - h * L.amp * .28 * Math.sin(u * L.f2 * 6.283 + L.p2 - t * L.v * 8);
    }

    function resize() {
      dpr = dprOf(); w = hero.clientWidth; h = hero.clientHeight;
      cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = Math.min(240, Math.round(w * h / 4200));
      stars = [];
      for (var i = 0; i < n; i++) stars.push({ x: Math.random(), y: Math.pow(Math.random(), 1.4) * .72, r: Math.pow(Math.random(), 3) * 1.5 + .35, z: rnd(.2, 1), ph: rnd(0, 6.28), sp: rnd(.4, 1.6) });
      sand = [];
      var m = COARSE ? 36 : 70;
      for (var j = 0; j < m; j++) sand.push({ x: rnd(0, w), lift: rnd(0, 26), vx: rnd(18, 55), r: rnd(.5, 1.5), a: rnd(.25, .7), ph: rnd(0, 6.28) });
    }

    function draw(t, dt) {
      px += (tx - px) * .05; py += (ty - py) * .05;
      ctx.clearRect(0, 0, w, h);
      // halo behind the brand star
      var narrow = w < 700, sx = w * (narrow ? .9 : .82) + px * 10, sy = narrow ? 34 : h * .22 + py * 6, SR = narrow ? 13 : 34;
      var g = ctx.createRadialGradient(sx, sy, 0, sx, sy, Math.max(w, h) * .38);
      g.addColorStop(0, 'rgba(' + GOLD + ',' + (narrow ? .04 : .07) + ')'); g.addColorStop(1, 'rgba(' + GOLD + ',0)');
      ctx.fillStyle = g; ctx.fillRect(0, 0, w, h);
      // stars
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i], tw = Math.sin(t * s.sp + s.ph);
        ctx.globalAlpha = .25 + .55 * tw * tw;
        ctx.fillStyle = 'rgb(' + CREAM + ')';
        ctx.beginPath(); ctx.arc(s.x * w + px * 14 * s.z, s.y * h + py * 8 * s.z, s.r, 0, 6.283); ctx.fill();
      }
      ctx.globalAlpha = 1;
      // occasional nova flare
      if (!nova && t > nextNova) {
        var c = stars[(Math.random() * stars.length) | 0];
        nova = { s: c, t0: t }; nextNova = t + rnd(5, 9);
      }
      if (nova) {
        var p = (t - nova.t0) / 2.6;
        if (p >= 1) nova = null; else {
          var e = Math.sin(p * Math.PI), nx = nova.s.x * w + px * 14 * nova.s.z, ny = nova.s.y * h + py * 8 * nova.s.z;
          var rg = ctx.createRadialGradient(nx, ny, 0, nx, ny, 34 * e + 1);
          rg.addColorStop(0, 'rgba(' + GOLD + ',' + (.55 * e) + ')'); rg.addColorStop(1, 'rgba(' + GOLD + ',0)');
          ctx.fillStyle = rg; ctx.beginPath(); ctx.arc(nx, ny, 34 * e + 1, 0, 6.283); ctx.fill();
          ctx.fillStyle = 'rgba(' + CREAM + ',' + (.95 * e) + ')'; ctx.beginPath(); ctx.arc(nx, ny, 1.2 + 2.4 * e, 0, 6.283); ctx.fill();
          ctx.strokeStyle = 'rgba(' + GOLD + ',' + (.35 * (1 - p)) + ')'; ctx.lineWidth = 1;
          ctx.beginPath(); ctx.arc(nx, ny, 8 + 46 * p, 0, 6.283); ctx.stroke();
        }
      }
      // dunes, far to near
      var step = COARSE ? 10 : 6;
      for (var k = 0; k < LAYERS.length; k++) {
        var L = LAYERS[k], off = px * (k + 1) * 7;
        ctx.save(); ctx.translate(off, 0);
        ctx.beginPath(); ctx.moveTo(-40, h);
        for (var x = -40; x <= w + 40; x += step) ctx.lineTo(x, ridge(L, k, x, t));
        ctx.lineTo(w + 40, h); ctx.closePath();
        var top = h * (L.base - L.amp * 1.4), fg = ctx.createLinearGradient(0, top, 0, h);
        fg.addColorStop(0, L.fill[0]); fg.addColorStop(1, L.fill[1]);
        ctx.fillStyle = fg; ctx.fill();
        // moonlit ochre rim
        ctx.beginPath();
        for (var x2 = -40; x2 <= w + 40; x2 += step) ctx.lineTo(x2, ridge(L, k, x2, t));
        var rim = ctx.createLinearGradient(0, 0, w, 0);
        rim.addColorStop(0, 'rgba(' + OCHRE + ',0)'); rim.addColorStop(.55, 'rgba(' + OCHRE + ',' + L.rim * .6 + ')'); rim.addColorStop(1, 'rgba(' + GOLD + ',' + L.rim + ')');
        ctx.strokeStyle = rim; ctx.lineWidth = 1.2; ctx.stroke();
        ctx.restore();
      }
      // blowing sand over the nearest ridge
      var NL = LAYERS[2];
      for (var q = 0; q < sand.length; q++) {
        var d = sand[q];
        d.x += d.vx * dt; if (d.x > w + 20) { d.x = -20; d.lift = rnd(0, 26); }
        var yy = ridge(NL, 2, d.x, t) - d.lift - 6 * Math.sin(t * 2 + d.ph);
        ctx.fillStyle = 'rgba(' + (q % 3 ? OCHRE : GOLD) + ',' + d.a * Math.min(1, d.x / (w * .25)) + ')';
        ctx.fillRect(d.x + px * 21, yy, d.r * 1.8, d.r);
      }
    }

    resize();
    var loop = Loop(hero, draw);
    if (RM) loop.still(); else loop.start();
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { resize(); loop.still(); }, 150); });
    if (!COARSE && !RM) hero.addEventListener('pointermove', function (e) {
      var r = hero.getBoundingClientRect();
      tx = ((e.clientX - r.left) / r.width - .5) * 2; ty = ((e.clientY - r.top) / r.height - .5) * 2;
    });
  }

  /* ---------------- AGENT FLOW diagrams ---------------- */
  function Flow(fig) {
    var steps; try { steps = JSON.parse(fig.getAttribute('data-steps')); } catch (e) { return; }
    var agent = +fig.getAttribute('data-agent') || 1;
    var cv = fig.querySelector('canvas'), cap = fig.querySelector('.flow-caption');
    var ctx = cv.getContext('2d'), w, h, dpr, nodes = [], active = 0, hover = -1, seg = 0, segT = 0, pause = 0, done = 0, trail = [];
    var NW, NH = 58;

    var vert = false;
    function layout() {
      dpr = dprOf(); w = fig.clientWidth;
      var n = steps.length, gap, pad = 18;
      vert = w < 640;
      if (vert) {            // phones: one clear vertical column
        gap = 20; NW = Math.min(340, w - pad * 2); h = pad * 2 + n * NH + (n - 1) * gap;
        nodes = steps.map(function (s, i) { return { x: (w - NW) / 2, y: pad + i * (NH + gap) }; });
      } else {
        gap = 22; NW = Math.min(150, (w - pad * 2 - gap * (n - 1)) / n); h = 150;
        var x0 = (w - (n * NW + (n - 1) * gap)) / 2;
        nodes = steps.map(function (s, i) { return { x: x0 + i * (NW + gap), y: (h - NH) / 2 }; });
      }
      cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); cv.style.height = h + 'px';
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function pointOn(i, p) { // position along edge i -> i+1
      var a = nodes[i], b = nodes[i + 1];
      if (vert) { var y0 = a.y + NH, y1 = b.y; return { x: a.x + NW / 2, y: y0 + (y1 - y0) * p }; }
      var x0 = a.x + NW, x1 = b.x; return { x: x0 + (x1 - x0) * p, y: a.y + NH / 2 };
    }

    function rr(x, y, ww, hh, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + ww, y, x + ww, y + hh, r); ctx.arcTo(x + ww, y + hh, x, y + hh, r); ctx.arcTo(x, y + hh, x, y, r); ctx.arcTo(x, y, x + ww, y, r); ctx.closePath(); }

    function wrap(text, maxW) {
      var words = text.split(' '), lines = [''];
      words.forEach(function (wd) { var t = lines[lines.length - 1] ? lines[lines.length - 1] + ' ' + wd : wd;
        if (ctx.measureText(t).width > maxW && lines[lines.length - 1]) lines.push(wd); else lines[lines.length - 1] = t; });
      return lines.slice(0, 2);
    }

    function setCaption(i) {
      if (!cap) return;
      cap.innerHTML = '<b>Step ' + (i + 1) + ' · ' + steps[i][0] + '</b> ' + steps[i][1];
    }

    function draw(t, dt) {
      ctx.clearRect(0, 0, w, h);
      // dot grid
      ctx.fillStyle = 'rgba(255,255,255,.06)';
      for (var gx = 12; gx < w; gx += 22) for (var gy = 12; gy < h; gy += 22) ctx.fillRect(gx, gy, 1.2, 1.2);
      // advance packet
      if (!RM && dt) {
        if (pause > 0) { pause -= dt; }
        else if (seg < steps.length - 1) { segT += dt / .85; if (segT >= 1) { segT = 0; seg++; active = seg; pause = .45; trail = []; if (hover < 0) setCaption(active); } }
        else { done += dt; if (done > 1.6) { seg = 0; segT = 0; active = 0; done = 0; trail = []; if (hover < 0) setCaption(0); } }
      }
      // edges
      for (var i = 0; i < nodes.length - 1; i++) {
        var a = pointOn(i, 0), b = pointOn(i, 1), lit = RM || i < seg;
        ctx.strokeStyle = lit ? 'rgba(' + GOLD + ',.55)' : 'rgba(255,255,255,.16)';
        ctx.lineWidth = lit ? 1.6 : 1; ctx.setLineDash(lit ? [] : [4, 5]);
        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
      }
      ctx.setLineDash([]);
      // nodes
      ctx.textBaseline = 'middle';
      for (var j = 0; j < nodes.length; j++) {
        var n = nodes[j], isA = j === agent, on = RM || j <= seg || done > 0, cur = j === (hover >= 0 ? hover : active);
        if (cur) { var rg = ctx.createRadialGradient(n.x + NW / 2, n.y + NH / 2, 0, n.x + NW / 2, n.y + NH / 2, NW * .75);
          rg.addColorStop(0, 'rgba(' + GOLD + ',.22)'); rg.addColorStop(1, 'rgba(' + GOLD + ',0)'); ctx.fillStyle = rg;
          ctx.fillRect(n.x - NW * .3, n.y - NH, NW * 1.6, NH * 3); }
        rr(n.x, n.y, NW, NH, 10);
        ctx.fillStyle = isA ? 'rgba(' + OCHRE + ',.22)' : '#1F2650'; ctx.fill();
        ctx.lineWidth = cur ? 1.8 : 1;
        ctx.strokeStyle = cur ? 'rgb(' + GOLD + ')' : (on ? 'rgba(' + GOLD + ',.45)' : 'rgba(255,255,255,.18)'); ctx.stroke();
        ctx.font = '600 10px "JetBrains Mono", monospace'; ctx.fillStyle = 'rgba(' + GOLD + ',' + (on ? .9 : .45) + ')';
        ctx.textAlign = 'left'; ctx.fillText((j < 9 ? '0' : '') + (j + 1), n.x + 9, n.y + 11);
        if (isA) { var bx = n.x + NW - 18, by = n.y + 6, lift = RM ? 0 : Math.max(0, Math.sin(t * 3)) * 1.5; ctx.fillStyle = 'rgb(' + GOLD + ')'; ctx.beginPath(); ctx.moveTo(bx, by + 10 - lift); ctx.lineTo(bx + 9, by + 10 - lift); ctx.lineTo(bx + 9, by - lift); ctx.lineTo(bx, by + 6 - lift); ctx.closePath(); ctx.fill(); }
        ctx.font = '600 13px "Instrument Sans", system-ui, sans-serif'; ctx.textAlign = 'center';
        ctx.fillStyle = on ? 'rgb(' + CREAM + ')' : 'rgba(' + CREAM + ',.55)';
        var lines = wrap(steps[j][0], NW - 16), ly = n.y + NH / 2 + 5 - (lines.length - 1) * 8;
        lines.forEach(function (l, k) { ctx.fillText(l, n.x + NW / 2, ly + k * 16); });
      }
      // packet + trail
      if (!RM && seg < nodes.length - 1 && pause <= 0) {
        var pt = pointOn(seg, segT); trail.push(pt); if (trail.length > 14) trail.shift();
        for (var q = 0; q < trail.length; q++) { ctx.fillStyle = 'rgba(' + GOLD + ',' + (q / trail.length) * .5 + ')'; ctx.beginPath(); ctx.arc(trail[q].x, trail[q].y, 1 + q / trail.length * 2.5, 0, 6.283); ctx.fill(); }
        var pg = ctx.createRadialGradient(pt.x, pt.y, 0, pt.x, pt.y, 12); pg.addColorStop(0, 'rgba(' + GOLD + ',.9)'); pg.addColorStop(1, 'rgba(' + GOLD + ',0)');
        ctx.fillStyle = pg; ctx.beginPath(); ctx.arc(pt.x, pt.y, 12, 0, 6.283); ctx.fill();
        ctx.fillStyle = 'rgb(' + CREAM + ')'; ctx.beginPath(); ctx.arc(pt.x, pt.y, 3, 0, 6.283); ctx.fill();
      }
    }

    function hit(e) {
      var r = cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      for (var i = 0; i < nodes.length; i++) { var n = nodes[i]; if (x >= n.x && x <= n.x + NW && y >= n.y && y <= n.y + NH) return i; }
      return -1;
    }
    cv.addEventListener('pointermove', function (e) { var i = hit(e); if (i !== hover) { hover = i; cv.style.cursor = i >= 0 ? 'pointer' : ''; setCaption(i >= 0 ? i : active); if (RM) loop.still(); } });
    cv.addEventListener('pointerleave', function () { hover = -1; setCaption(active); if (RM) loop.still(); });
    cv.addEventListener('pointerdown', function (e) { var i = hit(e); if (i >= 0) { hover = i; setCaption(i); if (RM) loop.still(); } });

    layout(); setCaption(0);
    var loop = Loop(fig, draw);
    loop.still(); if (!RM) loop.start();
    var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { layout(); loop.still(); }, 150); });
  }

  /* ---------------- Count-up figures (text is already correct in HTML) ---------------- */
  function Count(el) {
    var target = parseFloat(el.getAttribute('data-count')), pre = el.getAttribute('data-prefix') || '', suf = el.getAttribute('data-suffix') || '', dec = +el.getAttribute('data-dec') || 0;
    if (RM || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (e) {
      if (!e[0].isIntersecting) return; io.disconnect();
      var t0 = performance.now(), D = 1600;
      (function tick(now) { var p = Math.min(1, (now - t0) / D), v = target * (1 - Math.pow(1 - p, 3));
        el.textContent = pre + v.toFixed(dec) + suf; if (p < 1) requestAnimationFrame(tick); })(t0);
    }, { threshold: .6 });
    io.observe(el);
  }

  function boot() {
    var go = function () {
      var hero = document.querySelector('.hero'); if (hero) Hero(hero);
      Array.prototype.forEach.call(document.querySelectorAll('.flow-viz[data-steps]'), Flow);
      Array.prototype.forEach.call(document.querySelectorAll('[data-count]'), Count);
    };
    (document.fonts && document.fonts.ready ? document.fonts.ready : Promise.resolve()).then(function () {
      'requestIdleCallback' in window ? requestIdleCallback(go, { timeout: 600 }) : setTimeout(go, 60);
    });
  }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
