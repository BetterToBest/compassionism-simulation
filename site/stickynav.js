/* The sticky section bar on the simulation page and the findings page (S77, from Duke's report of Nov 16, 2026).
 * 1. Release 1's controls (environment, years) float under the section links and show only while a release 1 section is under the bar; over
 *    release 2's sections (marked data-r2) they are hidden, so the bar never offers "v5.6 panel" switches beside release 2. They float
 *    (no change to the page's flow), so showing and hiding them never moves the page.
 * 2. Sections stop below the whole bar: their scroll margin is the bar's measured height (--fx-stick), not a fixed 120-130 px, which a phone's
 *    taller bar covered, so the reader saw the end of the section before the one clicked.
 * 3. A section link keeps its section in place while the content above it finishes drawing (charts and tables drawn when they come into view
 *    pushed the section down, so the page settled on the section before). The hold ends after two seconds or at the reader's first scroll. */
(function () {
  'use strict';
  var GAP = 12, HOLD = 2000;
  function init() {
    var nav = document.querySelector('.fx-nav'); if (!nav) return;
    var ctl = nav.querySelector('.fd-ctl, .fx-strip-bar'), root = document.documentElement;
    var space = null, ctlH = 0, navH = 0, tick = false;
    if (ctl) {
      ctl.classList.add('fx-ctl-float');
      space = document.createElement('div'); space.className = 'fx-ctl-space'; space.setAttribute('aria-hidden', 'true');
      nav.parentNode.insertBefore(space, nav.nextSibling);
    }
    function shown(el) { return !!(el && el.getClientRects().length); }
    function sections() { return Array.prototype.filter.call(document.querySelectorAll('.fx-sec'), shown); }
    /* the section under the bar's lower edge (the first one, above them all) */
    function current(line) { var s = sections(), cur = s[0] || null;
      for (var i = 0; i < s.length; i++) { if (s[i].getBoundingClientRect().top <= line + 1) cur = s[i]; else break; } return cur; }
    function measure() {
      /* a link to a section the open release does not have (an earlier release has no release 2 sections) is hidden */
      Array.prototype.forEach.call(nav.querySelectorAll('a[href^="#"]'), function (a) { var t = document.getElementById(a.getAttribute('href').slice(1));
        var gone = !!t && (t.hidden || !!(t.closest && t.closest('[hidden]'))); if (a.hidden !== gone) a.hidden = gone; });
      navH = nav.getBoundingClientRect().height; ctlH = ctl && ctl.children.length ? ctl.offsetHeight : 0;
      root.style.setProperty('--fx-stick', Math.round(navH + ctlH + GAP) + 'px'); root.style.setProperty('--fx-stick-r2', Math.round(navH + GAP) + 'px');  /* release 2's sections: no controls over them */
      /* when the first section is release 1's (an earlier release), reserve the controls' room under the unstuck bar so they cover nothing */
      if (space) { var first = sections()[0]; space.style.height = first && !first.hasAttribute('data-r2') && ctlH ? (ctlH + 1) + 'px' : '0px'; }
      update();
    }
    function update() {
      tick = false; if (!ctl) return;
      var cur = current(nav.getBoundingClientRect().top + navH + ctlH + GAP + 2);  /* the line where a clicked section stops */
      var off = !ctl.children.length || !cur || cur.hasAttribute('data-r2');
      if (ctl.classList.contains('fx-ctl-off') === off) return;
      ctl.classList.toggle('fx-ctl-off', off);
      if (off) { if (ctl.contains(document.activeElement)) document.activeElement.blur(); ctl.setAttribute('inert', ''); } else ctl.removeAttribute('inert');
    }
    function onScroll() { if (!tick) { tick = true; window.requestAnimationFrame(update); } }
    window.addEventListener('scroll', onScroll, {passive: true});
    window.addEventListener('resize', measure);
    if (window.ResizeObserver) { var ro = new ResizeObserver(measure); ro.observe(nav); if (ctl) ro.observe(ctl); }
    if (window.MutationObserver) new MutationObserver(measure).observe(document.body, {subtree: true, attributes: true, attributeFilter: ['hidden']});
    measure();

    /* 3: hold a section in place while what is above it draws */
    var holdT = null;
    function stopHold() { if (holdT !== null) { window.cancelAnimationFrame(holdT); holdT = null; } }
    ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) { window.addEventListener(ev, stopHold, {passive: true}); });
    function hold(t) {
      stopHold(); var end = Date.now() + HOLD;
      (function step() {
        var want = parseFloat(window.getComputedStyle(t).scrollMarginTop) || 0, d = t.getBoundingClientRect().top - want;
        if (Math.abs(d) > 2) window.scrollTo({top: window.scrollY + d, behavior: 'instant'});
        holdT = Date.now() < end ? window.requestAnimationFrame(step) : null;
      })();
    }
    nav.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]'); if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey) return;
      var t = document.getElementById(a.getAttribute('href').slice(1)); if (!shown(t)) return;
      e.preventDefault();
      if (window.history && history.pushState) history.pushState(null, '', a.getAttribute('href')); else location.hash = a.getAttribute('href');
      measure(); hold(t);
      if (!t.hasAttribute('tabindex')) t.setAttribute('tabindex', '-1'); t.focus({preventScroll: true});
    });
    /* an address that names a section: hold it while the page's data load and draw */
    var h = location.hash && document.getElementById(location.hash.slice(1));
    if (h && h.classList.contains('fx-sec')) window.addEventListener('load', function () { if (shown(h)) { var end = Date.now() + 4000;
      (function wait() { if (window.scrollY > 0 || Date.now() > end) hold(h); else window.setTimeout(wait, 100); })(); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
