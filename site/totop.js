/* Back to top (S76): a button fixed at the bottom right of the simulation page and the findings page, shown once the reader has scrolled
 * past the first screen. It moves focus to the page's first heading, so keyboard and screen-reader users land where sighted users do. */
(function () {
  'use strict';
  function init() {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'fx-top'; b.id = 'to-top'; b.hidden = true;
    b.setAttribute('aria-label', 'Back to the top of the page');
    b.innerHTML = '<span aria-hidden="true">&uarr;</span> Top';
    b.onclick = function () {
      var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({top: 0, behavior: reduce ? 'auto' : 'smooth'});
      var h = document.querySelector('h1');
      if (h) { if (!h.hasAttribute('tabindex')) h.setAttribute('tabindex', '-1'); h.focus({preventScroll: true}); }
    };
    document.body.appendChild(b);
    var tick = false;
    function update() { tick = false; b.hidden = window.scrollY < Math.max(600, window.innerHeight); }
    window.addEventListener('scroll', function () { if (!tick) { tick = true; window.requestAnimationFrame(update); } }, {passive: true});
    update();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
