// Renders ```mermaid code fences (output by Zola as <code data-lang="mermaid">) into diagrams.
(function () {
  function renderMermaid() {
    var blocks = document.querySelectorAll('code[data-lang="mermaid"]');
    if (!blocks.length || !window.mermaid) return;

    var switched = document.documentElement.classList.contains('switch');
    var darkDefault = window.mermaidDarkDefault !== false;
    var isDark = darkDefault ? !switched : switched;

    mermaid.initialize({ startOnLoad: false, theme: isDark ? 'dark' : 'default' });

    blocks.forEach(function (code) {
      var pre = code.closest('pre');
      if (!pre) return;
      var div = document.createElement('div');
      div.className = 'mermaid';
      div.textContent = code.textContent;
      pre.replaceWith(div);
    });

    mermaid.run();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderMermaid);
  } else {
    renderMermaid();
  }
})();
