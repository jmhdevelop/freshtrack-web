#!/usr/bin/env python3
"""Etiqueta los enlaces a la App Store de cada página con ct= (y pt= si hay) y pone el
Smart App Banner (solo app-id) en las páginas de la tabla. Idempotente: se puede relanzar.

UN SOLO SITIO PARA EL PROVIDER TOKEN: la constante PT de abajo. Está vacía porque el
token (App Store Connect → Analytics → Campañas) lo tiene el dueño. Cuando lo haya:
poner PT = "<token>", ejecutar `python3 _scripts/appstore-enlaces.py` y commitear.

Nombre del ct: web-<idioma>-<portada|soporte|guia-<clave>>[-<hueco>] (máx. 40 car.).
El hueco es nav, hero, faq, cta, pie. En las guías el botón grande (cta) va sin sufijo,
como ya hacían las guías italianas (web-it-guia-nfc, web-it-guia-cocinato).
No toca el JSON-LD (sus URL son la ficha limpia) ni /t/ (ct=tupper).
"""
import re, sys, pathlib

PT = "126402967"  # Provider Token (ASC > Analytics > Campañas). Vacío = enlaces solo con ct.
APP = "6791699550"
ROOT = pathlib.Path(__file__).resolve().parent.parent
PAIS = {"es": "es", "en": "us", "de": "de", "fr": "fr", "it": "it", "pt": "br"}

# ruta: (idioma, tipo de página, con Smart App Banner)
PAGES = {
    "index.html": ("es", "portada", True),
    "guias/index.html": ("es", "guia-indice", True),
    "guias/cuanto-dura-comida-cocinada-nevera.html": ("es", "guia-cocinado", True),
    "guias/cuanto-dura-comida-congelador.html": ("es", "guia-congelador", True),
    "guias/etiquetas-nfc-tuppers.html": ("es", "guia-nfc", True),
    "guias/inventario-congelador.html": ("es", "guia-inventario", True),
    "soporte.html": ("es", "soporte", False),
    "en/index.html": ("en", "portada", True),
    "en/guides/index.html": ("en", "guia-indice", True),
    "en/guides/how-long-leftovers-last.html": ("en", "guia-cocinado", True),
    "en/guides/how-long-food-lasts-in-freezer.html": ("en", "guia-congelador", True),
    "en/guides/nfc-labels-food-containers.html": ("en", "guia-nfc", True),
    "en/guides/freezer-inventory.html": ("en", "guia-inventario", True),
    "en/support.html": ("en", "soporte", False),
    "de/index.html": ("de", "portada", True),
    "de/support.html": ("de", "soporte", False),
    "fr/index.html": ("fr", "portada", True),
    "fr/assistance.html": ("fr", "soporte", False),
    "it/index.html": ("it", "portada", True),
    "it/guide/index.html": ("it", "guia-indice", True),
    "it/guide/quanto-dura-cibo-cotto-in-frigo.html": ("it", "guia-cocinato", True),
    "it/guide/etichette-nfc-contenitori.html": ("it", "guia-nfc", True),
    "it/supporto.html": ("it", "soporte", False),
    "de/ratgeber/index.html": ("de", "guia-indice", True),
    "de/ratgeber/gekochtes-essen-kuehlschrank.html": ("de", "guia-gekocht", True),
    "pt/index.html": ("pt", "portada", True),
    "pt/suporte.html": ("pt", "soporte", False),
}

TOKENS = re.compile(
    r'(?P<nav><nav\b)|(?P<navend></nav>)|(?P<hero><header id="hero")|(?P<faq>id="faq")'
    r'|(?P<cta><div class="cta\b)|(?P<pie><footer\b)'
    r'|(?P<a><a\b[^>]*?href="(?P<href>https://apps\.apple\.com/(?:[a-z]{2}/)?app/id' + APP + r'[^"]*)"[^>]*>)')
BANNER = re.compile(r'<meta name="apple-itunes-app" content="[^"]*">')


def ct_name(lang, tipo, slot, tag):
    base = f"web-{lang}-{tipo}"
    if slot is None:
        slot = "cta" if 'class="appstore"' in tag else "cuerpo"
    if tipo.startswith("guia-") and slot == "cta":
        return base
    return f"{base}-{slot}"


def process(rel, lang, tipo, banner):
    p = ROOT / rel
    html = p.read_text(encoding="utf-8")
    state = {"slot": None}

    def sub(m):
        for k in ("nav", "hero", "faq", "cta", "pie"):
            if m.group(k):
                state["slot"] = k
                return m.group(0)
        if m.group("navend"):
            state["slot"] = None
            return m.group(0)
        ct = ct_name(lang, tipo, state["slot"], m.group("a"))
        assert len(ct) <= 40, ct
        q = (f"pt={PT}&amp;" if PT else "") + f"ct={ct}&amp;mt=8"
        new = f"https://apps.apple.com/{PAIS[lang]}/app/id{APP}?{q}"
        return m.group("a").replace(m.group("href"), new)

    out = TOKENS.sub(sub, html)
    if banner:
        content = f"app-id={APP}"
        # Banner solo con app-id: la doc de Apple (Promoting Apps with Smart App Banners) solo
        # define app-id y app-argument; el formato de pt/ct en el banner no figura en fuente
        # oficial, así que no se escribe.
        tag = f'<meta name="apple-itunes-app" content="{content}">'
        if BANNER.search(out):
            out = BANNER.sub(tag, out)
        else:
            ico = re.search(r'<link rel="apple-touch-icon"[^>]*>\n', out)
            assert ico, rel
            out = out[:ico.end()] + tag + "\n" + out[ico.end():]
    if out != html:
        p.write_text(out, encoding="utf-8")
        print("actualizado", rel)


def process_t():
    """/t/ (página de la etiqueta NFC) conserva su ct=tupper; solo se le añade el pt."""
    p = ROOT / "t/index.html"
    html = p.read_text(encoding="utf-8")
    q = (f"pt={PT}&amp;" if PT else "") + "ct=tupper"
    out = re.sub(r'(apps\.apple\.com/app/id' + APP + r')\?(?:pt=\d+&amp;)?ct=tupper"', r'\1?' + q + '"', html)
    if out != html:
        p.write_text(out, encoding="utf-8")
        print("actualizado t/index.html")


if __name__ == "__main__":
    process_t()
    for rel, (lang, tipo, banner) in PAGES.items():
        process(rel, lang, tipo, banner)
