# Fonte do site

Os arquivos HTML do site são gerados por `build.py` a partir de `content.py` (textos dos serviços),
`base.css` + `extra.css` (estilos) e `site.js` (comportamento).

Para regenerar, a partir da raiz do repositório:

    python3 _fonte/build.py prod .

Não há chaves nem dados sensíveis nesta pasta.
