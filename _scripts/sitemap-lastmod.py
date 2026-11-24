#!/usr/bin/env python3
"""Pone en sitemap.xml el <lastmod> de cada URL con la fecha del último commit de su fichero.

Así lastmod no depende de acordarse de cambiarlo a mano (el 2026-11-24 había 21 de 33
atrasados: portadas y soportes cambiados ese día seguían con fechas de septiembre).
Bing lo usa para decidir qué recoger antes; Google lo usa si es fiable.

Cuándo: después de commitear los cambios de páginas y antes de publicar. Luego se commitea
sitemap.xml y, ya publicado, se avisa con `python3 _scripts/indexnow.py`.

    python3 _scripts/sitemap-lastmod.py           # reescribe los lastmod
    python3 _scripts/sitemap-lastmod.py --check   # sale 1 si alguno está atrasado

Un fichero con cambios sin commitear no cuenta hasta que se commitea.
"""
import pathlib, re, subprocess, sys

HOST = "https://freshtrack.softapp.tech/"
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITEMAP = ROOT / "sitemap.xml"


def fichero(loc):
    rel = loc[len(HOST):]
    return rel + "index.html" if rel == "" or rel.endswith("/") else rel


def fecha(rel):
    out = subprocess.run(["git", "log", "-1", "--format=%cd", "--date=short", "--", rel],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    if not out:
        sys.exit(f"{rel}: sin historial en git (¿la URL del sitemap no tiene fichero?)")
    return out


def main(check):
    xml = SITEMAP.read_text(encoding="utf-8")
    atrasados = []

    def poner(m):
        loc, actual = m.group(2), m.group(4)
        nueva = fecha(fichero(loc))
        if nueva != actual:
            atrasados.append(f"{actual} -> {nueva}  {loc}")
        return f"{m.group(1)}{loc}{m.group(3)}{nueva}{m.group(5)}"

    nuevo = re.sub(r"(<loc>)([^<]+)(</loc>\s*<lastmod>)([^<]+)(</lastmod>)", poner, xml)
    print("\n".join(atrasados) or "lastmod al día")
    if check:
        sys.exit(1 if atrasados else 0)
    if nuevo != xml:
        SITEMAP.write_text(nuevo, encoding="utf-8")


if __name__ == "__main__":
    main("--check" in sys.argv[1:])
