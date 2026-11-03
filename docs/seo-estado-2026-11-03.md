---
# Documento interno: Jekyll no lo publica en la web (sin esto, GitHub Pages serviría el .md tal
# cual, igual que sirve README.md con 200).
published: false
---

# FreshTrack web: estado en Google a 2026-11-03

**Dominio:** `freshtrack.softapp.tech` · **Repo:** `jmhdevelop/freshtrack-web` (`master`, `550845b`, igual que `origin/master`)
**Hecho por:** `seo-indexing`, en el Mac mini M4. **Alcance:** solo lectura. No se ha tocado ninguna página, ni el sitemap, ni `robots.txt`, y no se ha publicado nada.
**Lo leerá:** `growth-marketing`. Las cifras llevan su fuente; donde no hay dato lo digo, y no lo relleno con estimaciones.

---

## 0. Lo que salió mal: hoy tampoco hay cifras de Search Console

**Este documento no trae impresiones, clics, consultas, países, posición ni indexación inspeccionada
de los últimos 90 días.** No es falta de permiso en la propiedad, que es del dueño (`siteOwner`,
`knowledge/seo.md`, 2026-09-10). Lo que falla es que **el panel no tiene token de Google**:

| Vía (la de la casa) | Resultado, 2026-11-03 08:16 UTC |
|---|---|
| `GET https://softmetrics.softapp.tech/api/metrics` con el Bearer del panel (sacado con `SoftMetrics secreto`, sin imprimirlo) | **200**. Primer intento 502 de Cloudflare, transitorio; el segundo, bien |
| `sources.google` en esa respuesta | **`{"on": false, "need": "búsquedas en Google"}`** |
| Qué significa | `Recopilador.swift:512`: `on: !c.googleToken.isEmpty`. El panel no tiene token de acceso a Google, así que no consulta Search Console (ni rendimiento, ni sitemaps, ni inspección). En la respuesta no hay ni un campo de búsqueda |
| Caché de indexación del panel (`ajustes`, `indexacion_freshtrack.softapp.tech`) | No se puede leer: el M2 (`192.168.50.102`) no responde desde el M4 (`ping` y `ssh`: *No route to host*). Además, el 2026-10-02 el clasificador ya denegó esa lectura por `ssh` |
| `gcloud` / API directa | `gcloud` no está instalado. Sin token, la API responde 401 (verificado el 2026-09-27) |

Pasa lo mismo que el 2026-09-30 (`knowledge/seo.md`, «El panel da indexación "de hoy" que es de hace
días»): el token de Google del panel caduca o lo revocan, y nadie lo reconecta. **Hasta que alguien
lo reconecte, nadie en la casa ve Search Console por API.**

**Rangos que hay que pedir cuando haya acceso.** Search Console va con 2-3 días de retraso, así que
el último día fiable hoy es el **2026-10-31**:

- Últimos 90 días: **2026-08-03 → 2026-10-31** (por día, consulta, página y país).
- Septiembre: **2026-09-01 → 2026-09-30**.
- Octubre: **2026-10-01 → 2026-10-31**, para comparar los dos meses con el mismo criterio.
- Desde la publicación de las guías: **2026-10-01 → 2026-10-31**. Se sirven desde el build de Pages del **2026-09-30 17:02 UTC** (`5855390`).

---

## 1. Titular

**Diagnóstico sin cambios desde septiembre, y no es técnico:** los 28 URL del sitemap se sirven
bien y los fundamentos están correctos en todas. El cuello de botella sigue siendo de **autoridad**
(ningún enlace entrante externo que cuente) y de **marca ocupada** (el nombre está más disputado que
en septiembre). Si hay impresiones o no, y en qué consultas, **no se puede afirmar** sin Search
Console (§0).

---

## 2. Indexación

**Hoy: sin inspeccionar.** Último dato real conocido, sacado de `knowledge/seo.md` y
`~/Projects/FreshTrack/docs/seo-2026-09-16.md`:

| Fecha | URL en el sitemap entonces | Indexadas | Fuente |
|---|---|---|---|
| 2026-09-07 | 4 | 4/4 | inspección por URL |
| 2026-09-11 | 8 | guía NFC ES «Rastreada: actualmente sin indexar» | inspección por URL |
| antes del 2026-09-19 (fecha de `revisado` en la caché) | 8 | 6/8 | caché del panel, leída el 2026-09-30 |
| **2026-11-03** | **28** | **sin dato** | — |

Desde entonces han entrado al sitemap las portadas y el soporte en de/fr/it/pt (29-09), las
políticas de privacidad en 6 idiomas (24-09 y 29-09) y 8 URL de guías (30-09). De esas, **nunca
se ha inspeccionado ninguna** con datos posteriores al 19-09.

Lo que sí está comprobado hoy con `curl`: las 28 URL dan **200**, ninguna redirige, ninguna lleva
`x-robots-tag` y todas declaran `index, follow`. Con eso Google *puede* indexarlas. Si lo ha hecho, no
se sabe.

---

## 3. Búsqueda (90 días, comparado con septiembre)

| Métrica | Septiembre (2026-09-01 → 09-30) | Últimos 90 días (2026-08-03 → 10-31) |
|---|---|---|
| Impresiones | 0 en los 28 días hasta el 2026-09-07 (último dato medido); del 08-09 al 30-09, sin dato | sin dato |
| Clics | 0 (mismo periodo) | sin dato |
| Posición media | — | sin dato |
| Consultas | ninguna | sin dato |
| Países | ninguno | sin dato |

**Qué páginas reciben algo (guías incluidas): no se puede saber hoy por ninguna vía.**

- Search Console: sin acceso (§0).
- El contador propio (`b.js`) solo manda el host y si la sesión es nueva: no guarda ni la ruta ni el
  referente (`seo-2026-09-27.md` §2). Lo que da el panel para FreshTrack en **los últimos 30 días
  hasta el 2026-11-03**: **103 visitas y 121 páginas vistas**. No dice cuáles ni de dónde vienen, así
  que **no** sirve como prueba de tráfico orgánico. Y no se compara con Search Console: son fuentes
  distintas, con retrasos distintos.

---

## 4. Enlaces entrantes

**Los que Google conoce** salen del informe «Enlaces» de Search Console, que **no tiene API**: hay que
mirarlo en la interfaz. Sin dato hoy.

**Los que existen y se ven desde fuera** (comprobado hoy en el HTML servido):

| Origen | Enlaza a | `rel` | ¿Aporta autoridad? |
|---|---|---|---|
| `softapp.tech` | portada y guía NFC ES | normal | **No**: es el mismo dominio registrable (`softapp.tech`). Ayuda a rastrear, no da autoridad |
| `dibus.softapp.tech`, `devtoolbox.softapp.tech` | portada | normal | No, por lo mismo |
| Ficha de App Store `id6791699550` (web del desarrollador y privacidad) | portada y `privacidad.html` | `nofollow noopener noreferrer` | No: sirve para descubrir las páginas |
| `github.com/jmhdevelop/freshtrack-web`: README y campo `homepage` | portada y `/en/` | `nofollow` | No: sirve para descubrir las páginas. **Novedad:** el repo es **PUBLIC** (en septiembre era privado y Google no lo veía) |
| Terceros (medios, blogs, foros, directorios) | — | — | **Ninguno encontrado.** Una búsqueda web de `"freshtrack.softapp.tech"` no devuelve ni una página nuestra ni una mención; solo salen otros FreshTrack |

**Conclusión: 0 enlaces entrantes externos que cuenten.** Es lo mismo que en septiembre y, en un
dominio nuevo, la causa por defecto de que una web indexada no salga en los resultados.

---

## 5. ¿Hay algo técnico nuevo roto?

**No.** Comprobado hoy con `curl` y un análisis del HTML servido en las 28 URL del sitemap:

| Comprobación | Resultado |
|---|---|
| `robots.txt` | 200, `Allow: /`, declara el sitemap |
| `sitemap.xml` | 200, `application/xml`, `xmllint` sin errores, 28 `<loc>`, todos del dominio propio |
| Estado HTTP | 28/28 dan 200, sin redirecciones, sin `x-robots-tag` |
| Origen `jmhdevelop.github.io/freshtrack-web/` | 301 al dominio propio. `http://` hace 301 a `https://` |
| `canonical` | 28/28 absolutos y autorreferenciales |
| `hreflang` | recíproco en las 28, con `x-default`; 0 parejas rotas |
| `title` | 28 distintos |
| `h1` | uno por página |
| `meta description` | en las 28; sin escapes `\uXXXX` |
| JSON-LD | se lee bien en todas y sin claves repetidas (`MobileApplication`, `WebSite`, `FAQPage` en las portadas; `Article` y `BreadcrumbList` en las guías, más `HowTo` en dos) |
| Contenido | portadas entre 755 y 921 palabras; guías entre 1.956 y 2.271 |
| Enlaces internos a las guías | desde el cuerpo de las páginas, no solo desde el pie: 5-8 en ES, 5-20 en EN |
| `/t/` (página de las etiquetas NFC) | `noindex` y fuera del sitemap. Es a propósito, no es un fallo |
| Contador | `b.js` en las 28 |

**Una cosa menor, no es un fallo:** el `<lastmod>` de las 6 políticas de privacidad (2026-09-24 y
2026-09-30) es anterior a su último cambio (2026-10-30, `b88f285`…`550845b`). Google solo hace caso
de `lastmod` si suele coincidir con la realidad, así que conviene ponerlo al día la próxima vez que
se toque el sitemap. No lo he cambiado: este encargo es solo de diagnóstico.

---

## 6. Marca: está más ocupada que en septiembre

En septiembre había «al menos seis» productos FreshTrack. Hoy, al buscar `freshtrack` en el App
Store de España (iTunes Search API, 2026-11-03), salen **10**, y al menos **cuatro son del mismo
nicho** que el nuestro: `6759292627` «Freshtrack - Aviso caducidad», `6765562095` «FreshTrack -
Inventario Cocina», `6794076905` «FreshTrack: Food Tracker» y `6764229469` «FreshTrack: Food Saver».
La nuestra sale **primera** en esa búsqueda del App Store, pero el App Store no es Google.

En Google, el autocompletado de `freshtrack app` propone «freshtrack login app», que es del
FreshTrack B2B australiano (`freshtrack.com`). **La marca a secas no se puede ganar.** Lo que dice
`knowledge/seo.md` (2026-09-07) sigue en pie: marca + calificador.

---

## 7. Las 5 consultas o temas con más posibilidad realista

**Esto es una hipótesis con fundamento, no una medición.** Faltan las consultas reales de Search
Console (§0), y en cuanto estén disponibles mandan sobre esta lista. Lo que sí está medido es que
la gente teclea esas búsquedas, según el autocompletado de Google (`suggestqueries.google.com`,
2026-11-03, una consulta por idioma). La competencia se juzga por quién aparece en las búsquedas de
prueba. La lista va de más a menos probable, contando que el dominio no tiene autoridad.

Las guías solo existen en **es** y **en**. En **de, fr, it y pt-BR** solo hay portada, soporte y
privacidad.

| # | Tema | Consultas por idioma | Página que la cubre | Por qué es realista | Riesgo |
|---|---|---|---|---|---|
| 1 | **Marca + calificador** | es: «FreshTrack caducidad y NFC», «FreshTrack NFC», «FreshTrack tuppers» · en: «FreshTrack NFC», «FreshTrack expiry tracker» · de/fr/it/pt: «FreshTrack NFC» | portadas (6 idiomas). El título ES ya dice «tuppers NFC»; el EN, «NFC containers» | Casi nadie más combina FreshTrack con NFC. Es lo que busca quien ya ha visto la app (ficha, boca a boca) | Poca demanda: el autocompletado no propone ninguna. Da pocas impresiones, pero de las primeras que llegarán |
| 2 | **Etiquetas NFC para tuppers** | es: «etiquetas NFC para tuppers», «etiquetas NFC comida» · en: «NFC labels for food containers» · de: «NFC Etiketten Lebensmittel» | `guias/etiquetas-nfc-tuppers.html`, `en/guides/nfc-labels-food-containers.html` (en de no hay guía) | Nicho con poquísima competencia. Las guías son largas y con datos (NXP, FDA) | Demanda mínima: el autocompletado no propone ni la consulta ES ni la EN. En alemán, «zwilling nfc etiketten» sale en el autocompletado: ZWILLING (FRESH & SAVE) ocupa ese hueco con una marca grande |
| 3 | **Inventario del congelador (app)** | es: «inventario congelador», «app inventario congelador» · en: «freezer inventory app», «… for iphone», «… free» · de: «Gefrierschrank Inventar App» | `guias/inventario-congelador.html`, `en/guides/freezer-inventory.html` (de: solo la portada) | Demanda confirmada en los tres idiomas y con intención de producto. Compite sobre todo con listados de apps, no con medios de salud | En «app para X», Google cita listicles (`knowledge/seo.md`, 2026-09-07). Se ganan antes las variantes («para iPhone», «sin vaciarlo») que la consulta corta |
| 4 | **Cuánto dura la comida cocinada en la nevera, plato a plato** | es: «cuánto dura la pasta cocinada en la nevera», «… el pollo cocinado…», «… comida cocinada descongelada…» · en: «how long do leftovers last in the fridge pasta / chicken / after cooking» · de: «wie lange ist gekochtes Essen im Kühlschrank haltbar» · fr: «combien de temps se conserve un plat cuisiné au frigo» · it: «quanto dura il cibo cotto in frigo» | `guias/cuanto-dura-comida-cocinada-nevera.html`, `en/guides/how-long-leftovers-last.html` (fr/de/it: sin guía) | Es la de más demanda de la lista, en todos los idiomas. La guía ya trata la pasta (7 menciones) | La consulta corta la dominan medios y organismos oficiales; sin enlaces, no hay sitio. Solo es realista en la cola larga por plato |
| 5 | **Cuánto dura la comida en el congelador si se va la luz** | es: «cuánto dura la comida en el congelador sin luz / si se va la luz» · en: «how long does food last in the freezer without power / during a power outage» · pt-BR: «quanto tempo dura comida no freezer sem luz» | `guias/cuanto-dura-comida-congelador.html` (5 menciones de apagón o luz), `en/guides/how-long-food-lasts-in-freezer.html` (6 de power) | Mucha demanda: el autocompletado propone primero la variante del apagón en es, en y pt-BR. Las guías ya lo tratan | Es un tema de seguridad alimentaria: Google prefiere USDA, FDA y organismos públicos. Lo pongo el último por eso, no porque no haya demanda |

**Lo que esto supone para `growth-marketing`:** con contenido propio se pueden ganar el 1 y el 2, y
en parte el 3. El 4 y el 5 tienen demanda real, pero sin enlaces entrantes de terceros (prensa,
blogs de cocina o de organización, foros) no van a salir. Cualquiera de los cinco llega antes con
**un solo enlace externo de verdad** que con otro retoque de la página. Las guías en de/fr/it/pt son
contenido nuevo y le tocan a `web-dev`/`growth-marketing`, no a SEO técnico.

---

## 8. Qué falta para cerrar este diagnóstico

1. **Que el panel vuelva a tener token de Google** (reconectar en `/conexiones` de SoftMetrics). Si
   cae otra vez a los 7 días, pasar la app OAuth de Testing a In production
   (`knowledge/seo.md`, 2026-09-30). En cuanto haya token, se piden los rangos de §0 y se inspeccionan
   las 28 URL una vez cada una, guardando el resultado.
2. **O bien**, más rápido: leer Search Console en la interfaz desde un chat de escritorio con «Control
   Chrome»: Rendimiento (rangos de §0, pestañas Consultas, Páginas y Países), Páginas (indexadas y no
   indexadas, con su motivo), Enlaces (sitios externos y páginas más enlazadas) y Sitemaps (estado de
   `sitemap.xml` y URL descubiertas).
3. Con eso se rehacen §2, §3, §4 y el orden de §7.
