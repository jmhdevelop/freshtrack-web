#!/usr/bin/env python3
"""Avisa por IndexNow (Bing, Yandex, Seznam, Naver, Yep) de las URL del sitemap PUBLICADO.

Cuándo: después de cada publicación en master, cuando `curl` ya devuelve el cambio servido
(GitHub Pages tarda un par de minutos). Avisar antes de que esté servido hace que Bing
rastree la versión vieja.

    python3 _scripts/indexnow.py            # todas las URL del sitemap servido
    python3 _scripts/indexnow.py URL [URL…] # solo esas (deben ser del dominio)
    python3 _scripts/indexnow.py --seco     # enseña lo que enviaría, sin enviar

La clave es pública por diseño (va servida en la raíz como <clave>.txt) y vive en
.indexnow-key. Antes de enviar se comprueba que el fichero servido coincide; si no, no se
envía (IndexNow respondería 403 y Bing dejaría de fiarse de la clave).
Respuestas: 200 = recibido; 202 = recibido, clave pendiente de validar; 4xx = error.
Reenviar URL sin cambios no da nada y repetirlo mucho puede contar como abuso: se envía
tras publicar, no en bucle. Documentación: https://www.indexnow.org/documentation
"""
import json, pathlib, re, sys, urllib.request, urllib.error

HOST = "freshtrack.softapp.tech"
ROOT = pathlib.Path(__file__).resolve().parent.parent
KEY = (ROOT / ".indexnow-key").read_text().strip()
KEY_URL = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"
UA = {"User-Agent": "softapp-indexnow/1.0"}


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode("utf-8")


def main(args):
    seco = "--seco" in args
    urls = [a for a in args if not a.startswith("--")]
    if not urls:
        urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", get(f"https://{HOST}/sitemap.xml"))
    ajenas = [u for u in urls if not u.startswith(f"https://{HOST}/")]
    if ajenas:
        sys.exit(f"URL fuera de {HOST}: {ajenas}")
    if get(KEY_URL).strip() != KEY:
        sys.exit(f"{KEY_URL} no sirve la clave de .indexnow-key: no se envía nada")
    print(f"{len(urls)} URL de {HOST}")
    if seco:
        print("\n".join(urls))
        return
    body = json.dumps({"host": HOST, "key": KEY, "keyLocation": KEY_URL,
                       "urlList": urls}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST",
                                 headers={**UA, "Content-Type": "application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status}")
    except urllib.error.HTTPError as e:
        sys.exit(f"IndexNow: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")


if __name__ == "__main__":
    main(sys.argv[1:])
