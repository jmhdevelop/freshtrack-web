---
# Documento interno: Jekyll no lo publica en la web (sin esto, GitHub Pages serviría el .md tal
# cual, igual que sirve README.md con 200).
published: false
---

# FreshTrack: guía alemana «gekochtes Essen im Kühlschrank» + siguiente tanda · 2026-11-24

**Hecho por:** `growth-marketing`, en el Mac mini M4. **Alcance:** solo texto. No hay HTML, ni sitemap,
ni `<head>`, ni nada publicado o empujado a la web. `web-dev` maqueta; `seo-indexing` pone `hreflang`,
sitemap y enlaces internos; publicar es desplegar y lo aprueba el dueño.
**Encargo:** aprobado por el dueño el 2026-11-24 (guías nuevas, sin publicidad de pago y sin prensa).
Es la acción A3 (3) de `docs/plan-difusion-2026-11-03.md`, prevista para el 05-12.
**Entrada:** `docs/plan-difusion-2026-11-03.md`, `docs/seo-estado-2026-11-03.md`,
`docs/guias-it-texto-2026-11-03.md` (y las dos guías italianas publicadas), `guias/etiquetas-nfc-tuppers.html`,
`knowledge/marketing.md` (2026-11-22) y `knowledge/seo.md`.

> **El alemán no lo ha revisado un nativo.** Lo ha escrito un agente. Las citas de las fuentes son
> literales (las fuentes están en alemán, así que no hay traducción en las citas), pero el resto del
> texto puede sonar a traducido. Las frases que más necesitan una lectura nativa llevan ⚑ y un número;
> la lista con el motivo está en §1.4.

---

## 0. Titular y línea base

**Titular:** en alemán la web no tiene nada que responder: solo portada, soporte y privacidad, cero
guías. Y la gente que llega desde Alemania llega sobre todo por enlaces: en octubre, 5 primeras descargas
en Alemania vinieron de la app de ChatGPT (`com.openai.chat`), y dos de cada tres descargas del último mes
no vinieron de la búsqueda de la App Store. Sin páginas en alemán que citar, ni Google ni un asistente
tienen de dónde sacar «FreshTrack NFC» cuando alguien pregunta en alemán.

| Magnitud | Valor | Periodo | Fuente |
|---|---|---|---|
| Primeras descargas | 63 (2,1/día) | 22-10 → 20-11-2026 | ASC, lectura de `data-analyst` (`knowledge/marketing.md`, 2026-11-22) |
| … por búsqueda en la tienda / enlaces web / otras apps | 19 / 21 / 19 | ídem | ídem |
| ChatGPT como origen | 5 primeras descargas en **Alemania** (`com.openai.chat`) | octubre de 2026 | ídem |
| Tiendas que convierten desde la búsqueda | IT, FR, DE, AT, CH (≈290 impresiones/mes entre todas); en inglés, 455 impresiones → 1 descarga | 22-10 → 20-11 | ídem |
| Google (toda la web) | 261 impresiones, 8 clics; la guía ES de comida cocinada sale en «cuanto aguanta la comida cocinada en la nevera» (0/11) y «cuanto dura la verdura cocinada en la nevera» (0/4) | 31-08 → 31-10 | Search Console, leído el 03-11 (`plan-difusion-2026-11-03.md` §2). **Ninguna consulta en alemán** |
| Indexación | **21 de 25** URL inspeccionadas, indexadas. Fuera: `en/privacy.html` y `guias/cuanto-dura-comida-congelador.html` (rastreadas, sin indexar), `en/guides/` (descubierta, sin indexar) y `en/guides/how-long-leftovers-last.html` («Google no reconoce esta URL») | caché del panel con `revisado: 2026-11-24` | M2, `ajustes.indexacion_freshtrack.softapp.tech` (solo lectura). El sitemap tiene 31 URL: **no sé si las 3 italianas están entre las 25 inspeccionadas** |
| Enlaces externos que cuentan | 0 | a 03-11 | `seo-estado-2026-11-03.md` §4. El correo a Shop NFC sigue sin enviar (previsto 25-11) |
| Visitas a la web | 103 visitas en 30 días | hasta el 03-11 | contador `b.js`. **No lo he releído hoy**, y el contador **no guarda la página** (ver §5) |
| Ficha DE/AT/CH | Publicada, `resultCount` 1 en las tres, «FreshTrack: MHD & NFC», 1.3 del 01-11, gratis, 0 valoraciones | 24-11 | `itunes.apple.com/lookup?id=6791699550&country=de|at|ch` |

---

## 1. La guía alemana

### 1.1 Cómo se ha hecho y qué tiene que saber `web-dev`

**Mismo esqueleto que la guía italiana de comida cocinada** (`it/guide/quanto-dura-cibo-cotto-in-frigo.html`):
migas, kicker, `h1`, `p.lead`, `p.byline`, índice, secciones `h2 id=`, tabla `.table-wrap > table.wrapcells`
con `caption` y `th scope`, notas en `p.fine`, bloque `.cta` con insignia, descargo en `p.fine`, pie con
enlaces a las otras versiones. Novedad respecto a la italiana: **un bloque final de preguntas y respuestas
cortas** (`#fragen`), con `h3` por pregunta y un `p` de una a tres frases por respuesta, en HTML visible.
Sobre el marcado de ese bloque, ver §4 (no hace falta `FAQPage`).

| Campo | Propuesta |
|---|---|
| Ruta | `de/ratgeber/gekochtes-essen-kuehlschrank.html` + `de/ratgeber/index.html` (ficha al final). La carpeta la decide `web-dev`; «Ratgeber» es como se llaman en alemán estas guías de consumo ⚑1 |
| `hreflang` | `de` → esta; `it` → `/it/guide/quanto-dura-cibo-cotto-in-frigo.html`; `es` → `/guias/cuanto-dura-comida-cocinada-nevera.html`; `en` → `/en/guides/how-long-leftovers-last.html`; `x-default` → la inglesa. **Recíproco en las otras tres** y en el sitemap (`seo-indexing`) |
| Enlace a la tienda (CTA) | `https://apps.apple.com/app/id6791699550?ct=web-de-guia-gekocht&mt=8`, y `pt=<pt>` delante del `ct` cuando el dueño lo saque. **Sin `/de/` en la ruta**, a diferencia de las italianas: esta guía la leerán también en Austria y Suiza, que convierten. La App Store del iPhone abre la ficha en la tienda de la cuenta del usuario (sin probar con una cuenta AT/CH) |
| Insignia | `img/app-store/de-black.svg` / `de-white.svg` (existen), `alt`: «Laden im App Store» |
| Nombre | «FreshTrack NFC» en el texto (plan §7). En la tienda alemana la ficha se llama «FreshTrack: MHD & NFC» (lookup 24-11) |
| JSON-LD | `Article` (`headline` = el `<title>` sin marca, `inLanguage: "de-DE"`, `datePublished`/`dateModified` = día de publicación, `author`/`publisher` = SOFTAPP SOLUTIONS LLC, `citation` con las URL de §1.2) + `BreadcrumbList` (FreshTrack › Ratgeber › Gekochtes Essen im Kühlschrank). Nada más (§4) |
| Enlace interno | Desde `de/index.html`, en el cuerpo, una frase que enlace a esta guía (`seo-indexing`). Hoy la portada DE solo enlaza guías en inglés |

### 1.2 Fuentes, leídas hoy (2026-11-24) en directo

Todas respondieron 200 a `curl` y se ha leído el texto. Ninguna cifra viene de medios ni de memoria.

| # | Fuente | Fecha que declara | Qué da | Qué NO da |
|---|---|---|---|---|
| F1 | **BfR**, «Vorkochen für mehrere Tage: Was ist zu beachten?» (FAQ) — `https://www.bfr.bund.de/fragen-und-antworten/thema/vorkochen-fuer-mehrere-tage/` | 08.07.2025 | «erhitzte Mahlzeiten innerhalb von 2-3 Tagen zu verbrauchen oder einzufrieren»; con componentes crudos, «spätestens einen Tag»; nevera «maximal 7 °C, besser wären 5 °C»; zona baja junto a la pared del fondo, la más fría; recipientes herméticos con el símbolo vaso-tenedor, una ración por recipiente; congelar frío, por raciones, con poco aire; rotular «Bezeichnung» y «Datum der Einlagerung»; tiempos a −18 °C por tipo de alimento; recalentar «mindestens 2 Minuten über 70 °C»; descongelar en la nevera; el olfato no basta; grupos sensibles | cifra por plato |
| F2 | **BfR**, «Korrektes Kühlen von Lebensmitteln im Privathaushalt» (FAQ, PDF) — `https://www.bfr.bund.de/cm/343/korrektes-kuehlen-von-lebensmitteln-im-privathaushalt.pdf` | 13.02.2023 | restos: «innerhalb von zwei bis drei Tagen verbraucht», antes enfriados «innerhalb weniger Stunden auf unter + 7 °C», en varias fuentes planas; encuesta BfR 2020: media de 5,5 °C en neveras alemanas y solo la mitad con termómetro; a −18 °C las bacterias no crecen (la congelación es cuestión de calidad); comida cocinada «angetaut» tras un apagón se puede volver a congelar | — |
| F3 | **BfR**, «Verbrauchertipps: Schutz vor lebensmittelbedingten Erkrankungen durch bakterielle Toxine» (PDF) — `https://www.bfr.bund.de/cm/350/verbrauchertipps-schutz-vor-lebensmittelbedingten-erkrankungen-durch-bakterielle-toxine.pdf` | «Aktualisierte Fassung, Berlin 2020» | *Bacillus cereus*: esporas que sobreviven a la cocción, típico en «stärkehaltige, gekochte Lebensmittel wie Reis oder Nudeln»; el cereulide resiste el calor; enfriar «schnell auf unter 7 Grad Celsius», en fuentes planas; recalentar a 70 °C 2 minutos; remover en el microondas | horas o días para el arroz |
| F4 | **Verbraucherzentrale NRW**, «Mikrowelle richtig nutzen…» — `https://www.verbraucherzentrale.nrw/aufwaermen` | Stand 22.12.2025 | arroz: «innerhalb von 24 Stunden verbrauchen», recalentar a 70 °C; setas: máx. 4 °C y 24 horas; espinacas: recalentar una vez, no a bebés | — |
| F5 | **Verbraucherzentrale NRW**, «Kalt gemacht – Wie du Lebensmittel richtig einfrierst» — `https://www.verbraucherzentrale.nrw/unsere-lebensmittel/richtig-einfrieren` | Stand 22.12.2025 | rotular con la fecha de congelación, lista en la puerta; descongelar en la nevera; sopas sin patata ni pasta dentro; huevos cocidos en la lista de lo que no se congela | meses para platos cocinados |
| F6 | **Verbraucherzentrale Niedersachsen**, «Tipps und Tricks beim Einfrieren und Auftauen» — `https://www.verbraucherzentrale-niedersachsen.de/wissen/lebensmittel/gesund-ernaehren/tipps-und-tricks-beim-einfrieren-und-auftauen-120371` | Stand 26.09.2025 | tabla a −18 °C: **«Selbstgekochtes: 1 - 3 Monate»**; más grasa, menos tiempo; lista «auf Papier oder in einer App» con contenido, cantidad/raciones y fecha; lo nuevo abajo, lo viejo arriba; enfriar antes de congelar; postres con gelatina se aguan | cifra por plato |
| F7 | **BZfE**, «Richtig lagern» — `https://www.bzfe.de/kueche-und-alltag/kochen/lebensmittel-richtig-lagern` | sin fecha visible | comida preparada en los estantes por encima del más bajo; puerta, lo más cálido; congelador «für einige Monate»; rotular «mit Inhalt, Menge und Einfrierdatum»; huevos duros: «etwa zwei bis vier Wochen» | días para cocinados |
| F8 | **Zu gut für die Tonne!** (iniciativa del ministerio federal de agricultura), «Richtig lagern» — `https://www.zugutfuerdietonne.de/tipps-fuer-zu-hause/richtig-lagern` | Stand 20.02.2026 | «Nudelreste sollten Sie im obersten Kühlschrankfach aufbewahren. Dort halten sie ein bis zwei Tage.»; carne cruda en el estante más bajo, sobre un plato | — |
| F9 | **EFSA**, Safe2Eat, «Richtiger Umgang mit Lebensmitteln» (alemán) — `https://www.efsa.europa.eu/de/safe2eat/proper-food-handling` | — | «nicht länger als 2 Stunden bei Raumtemperatur»; nevera «möglichst unter 5 °C»; sopas a 70 °C | días |
| F10 | **AGES** (Austria), «Sicher kochen» — `https://www.ages.at/mensch/ernaehrung-lebensmittel/ernaehrungsempfehlungen/sicher-kochen` | — | nevera entre 1 y 5 °C; enfriar en raciones y al baño de agua fría; a −18 °C «fast alle Lebensmittel … ca. 10 Monate»; lo descongelado no se vuelve a congelar (lo «angetaut», microbiológicamente sí) | días para cocinados |
| F11 | **BLV** (Suiza), «Hygiene im Umgang mit Lebensmitteln» — `https://www.blv.admin.ch/de/hygiene-im-umgang-mit-lebensmitteln` | — | recalentar a 70 °C; lo descongelado no se vuelve a congelar; restos, en frío | días |

**Lo que no he encontrado** en ninguna de estas páginas: una cifra propia para patatas cocidas, boloñesa,
pollo cocinado o sopa (se aplica la regla general del BfR, y la guía lo dice), ni una tabla oficial alemana
de meses de congelador **por plato** cocinado. Busqué páginas de la AGES y del BLV con días para restos y
no las hay en lo que devuelve la búsqueda; por eso de Austria y Suiza solo uso temperatura, enfriado y
descongelación.

### 1.3 Consultas objetivo (autocompletado de Google, `hl=de`, `gl=de/at/ch`, 2026-11-24)

| Consulta | Lo que sugiere Google | Dónde se atiende |
|---|---|---|
| wie lange ist gekochtes essen im kühlschrank haltbar | «…frisch gekochtes…», «…fertig gekochtes…» (igual en DE, AT y CH) | `title`, `h1`, `#kurz`, pregunta 1 |
| gekochtes essen im kühlschrank | «…lagern», «…abdecken», «…nicht im kühlschrank», «…2 / 3 / 4 / 5 tage im kühlschrank» | `#kurz`, `#abkuehlen`, `#wo`, preguntas 1 y 8 |
| wie lange hält gekochter reis (im kühlschrank) | «…bei zimmertemperatur», «…ungekühlt», «…im gefrierschrank», «…mit gemüse / mit hähnchen» | `#reis`, pregunta 2 |
| wie lange hält gekochtes hähnchen im kühlschrank | «…7 tage» | pregunta 6 |
| wie lange hält suppe / eintopf im kühlschrank | «…selbstgemachte», «…gemüseeintopf», «…hackfleisch eintopf» | tabla, pregunta 4 |
| wie lange hält bolognese im kühlschrank | «…soße», «…aufgetaute bolognese» | tabla, pregunta 5 |
| gekochte kartoffeln im kühlschrank | «…wie lange haltbar», «…abdecken», «…weiß geworden», «…giftig» | pregunta 7 |
| meal prep wie lange haltbar | «…reis», «…hähnchen», «…einfrieren» | pregunta 13 |
| wie lange kann man gekochtes essen einfrieren | «…selbst gekochtes…», «…fertig gekochtes…» | `#einfrieren`, pregunta 9 |
| gefrierschrank beschriften | «…schubladen», «…fächer» | `#beschriften`, pregunta 11 |

Sin sugerencias (no se promete que nadie lo busque): «wie lange halten gekochte nudeln im kühlschrank»,
«essen einfrieren beschriften».

### 1.4 Frases que tiene que leer un nativo

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «Ratgeber» como nombre de la sección y kicker | La portada DE dice «Leitfaden» (`de/index.html:103`). «Ratgeber» es lo habitual en guías de consumo; decidir uno y usarlo en todo el sitio |
| ⚑2 | «Dose» para el recipiente | Es la palabra de la app y de la ficha («Dosen mit NFC-Etikett»). Para restos de comida quizá suena más natural «Frischhaltedose» o «Behälter». Lo he mezclado: «Dose» cuando hablo de la app, «Behälter» en lo general |
| ⚑3 | «Kreppband und ein wasserfester Stift» | Registro y si «Kreppband» es la palabra de uso común (en Austria y Suiza también) |
| ⚑4 | «Die Uhr läuft ab dem Kochtag» | Modismo traducido; alternativa: «Gezählt wird ab dem Tag, an dem du gekocht hast» |
| ⚑5 | «Wir haben FreshTrack NFC gebaut, weil …» y «sie ist von uns» | Traducción de «la hicimos porque…» y «es nuestra»; puede sonar raro. Alternativa: «Wir haben sie selbst entwickelt» |
| ⚑6 | Tuteo («du») en todo el texto | Igual que la ficha, la portada DE y la Verbraucherzentrale NRW; el BZfE y el BfR usan «Sie». Confirmar que «du» es lo adecuado para una guía de seguridad alimentaria |
| ⚑7 | «Unsere Lesart» / «Unser Rat» para marcar lo que es criterio nuestro y no de la fuente | Que se entienda que no es una cita |

---

### 1.5 Ficha para el `<head>` (la monta `web-dev`, la revisa `seo-indexing`)

| Campo | Texto | Caracteres |
|---|---|---|
| `<title>` | `Wie lange ist gekochtes Essen im Kühlschrank haltbar? Gericht für Gericht` | 73 |
| `<title>` alternativo con marca | `Gekochtes Essen im Kühlschrank: wie lange haltbar? – FreshTrack NFC` | 67 |
| `<meta name="description">` y `og:description` | `Reis 24 Stunden, Nudeln 1–2 Tage, die meisten Gerichte 2–3 Tage: was BfR, Verbraucherzentrale und BZfE zu Resten in Kühl- und Gefrierschrank sagen.` | 147 |
| `og:title` | `Wie lange ist gekochtes Essen im Kühlschrank haltbar?` | 53 |
| `og:locale` | `de_DE` | — |
| JSON-LD `headline` | igual que el `<title>` | 73 |
| `citation` | las URL de F1 a F11 | — |
| Fechas | `datePublished`/`dateModified`: el día que el dueño apruebe publicar. Fuentes geprüft am 24. November 2026 | — |

Recuentos con `len()` de Python sobre la cadena exacta.

---

### 1.6 TEXTO DE LA PÁGINA (alemán)

> **Migas:** FreshTrack › Ratgeber › Gekochtes Essen im Kühlschrank
> **Kicker:** Ratgeber ⚑1

# Wie lange ist gekochtes Essen im Kühlschrank haltbar? Gericht für Gericht, nach den offiziellen Quellen

**Lead:** Reis, Nudeln, Suppe, Eintopf, Fleisch, Fisch, Gemüse und Soße: was das Bundesinstitut für Risikobewertung (BfR), die Verbraucherzentralen und das Bundeszentrum für Ernährung (BZfE) sagen, wo sie keine Zahl nennen – und wie du Reste so beschriftest, dass du nicht mehr raten musst.

**Byline:** Veröffentlicht am [Datum] von SOFTAPP SOLUTIONS LLC · Aktualisiert am [Datum] · Quellen geprüft am 24. November 2026

**Inhaltsverzeichnis «In diesem Ratgeber»:**
1. Kurz gesagt (`#kurz`)
2. Gericht für Gericht (`#tabelle`)
3. Sonderfall Reis (`#reis`)
4. Abkühlen: schnell und flach (`#abkuehlen`)
5. Wohin im Kühlschrank? (`#wo`)
6. Einfrieren: wie lange und wie (`#einfrieren`)
7. Beschriften: was auf den Behälter gehört (`#beschriften`)
8. Aufwärmen und Auftauen (`#aufwaermen`)
9. Warum der Geruchstest nicht reicht (`#geruch`)
10. Von Hand oder mit FreshTrack NFC (`#freshtrack`)
11. Häufige Fragen, kurz beantwortet (`#fragen`)

---

## Kurz gesagt  `#kurz`

Gekochtes Essen hält sich im Kühlschrank **2 bis 3 Tage**. So steht es beim Bundesinstitut für Risikobewertung: Es sei ratsam, «erhitzte Mahlzeiten innerhalb von 2-3 Tagen zu verbrauchen oder einzufrieren». Gerichte mit rohen Bestandteilen, etwa mit rohem Gemüse oder Salat, sollten «spätestens einen Tag nach der Zubereitung» gegessen werden.

Strenger sind zwei Fälle: **gekochter Reis** innerhalb von **24 Stunden** (Verbraucherzentrale NRW) und **Nudelreste**, die im obersten Kühlschrankfach **ein bis zwei Tage** halten (Zu gut für die Tonne!). Gekochte Pilze ebenfalls nur 24 Stunden, gut gekühlt (Verbraucherzentrale NRW).

Das gilt nur in einem kalten Kühlschrank: **höchstens 7 °C, besser 5 °C** (BfR). Und was du nicht rechtzeitig schaffst, kommt in den Gefrierschrank: Selbstgekochtes hält bei −18 °C etwa **1 bis 3 Monate** (Verbraucherzentrale Niedersachsen). Unser Rat ⚑7: lieber am ersten Tag einfrieren als am letzten.

## Gericht für Gericht  `#tabelle`

FreshTrack NFC kennt zehn Arten gekochter Speisen (dazu rohes Fleisch und roher Fisch, um die es hier nicht geht). Für jede: was die offiziellen Quellen sagen und welche Tage die App standardmäßig vorschlägt.

**Tabelle** (`caption`: «Haltbarkeit gekochter Speisen laut offiziellen Quellen und Standardwerte von FreshTrack NFC; Quellen geprüft am 24. November 2026»)

| Gericht | Kühlschrank laut offiziellen Quellen | Gefrierschrank (−18 °C) laut offiziellen Quellen | FreshTrack NFC Standard (Kühlschrank / Gefrierschrank) |
|---|---|---|---|
| Gekochter Reis | **24 Stunden** (Verbraucherzentrale NRW) | 1–3 Monate† | 2 Tage / 90 Tage |
| Gekochte Nudeln | **1–2 Tage**, im obersten Fach (Zu gut für die Tonne!) | 1–3 Monate† | 3 Tage / 60 Tage |
| Hülsenfrüchte / Eintopf | 2–3 Tage (BfR) | 1–3 Monate† | 3 Tage / 90 Tage |
| Suppe / Cremesuppe | 2–3 Tage (BfR) | 1–3 Monate†; Einlagen wie Nudeln oder Kartoffeln lieber nicht mit einfrieren (Verbraucherzentrale NRW) | 3 Tage / 90 Tage |
| Gekochtes Fleisch, Geflügel | 2–3 Tage (BfR) | 1–3 Monate† | 3 Tage / 90 Tage |
| Gekochter Fisch | 2–3 Tage (BfR) | 1–3 Monate† | 2 Tage / 60 Tage |
| Gekochtes Gemüse | 2–3 Tage (BfR); **Pilze 24 Stunden** (Verbraucherzentrale NRW) | gegart **bis zu 12 Monate** (BfR, für Gemüse) | 3 Tage / 60 Tage |
| Omelett / Ei | 2–3 Tage (BfR, allgemein); hartgekochte Eier etwa zwei bis vier Wochen (BZfE) | gekochte Eier besser nicht einfrieren: sie werden gummiartig (Verbraucherzentralen NRW und Niedersachsen) | 2 Tage / 30 Tage |
| Hausgemachte Soße (z. B. Bolognese) | 2–3 Tage (BfR) | 1–3 Monate† | 4 Tage / 90 Tage |
| Hausgemachtes Dessert | 2–3 Tage (BfR); mit rohen Zutaten höchstens 1 Tag (BfR) | Gelatinespeisen werden wässrig (Verbraucherzentrale Niedersachsen) | 3 Tage / 30 Tage |

**Hinweise unter der Tabelle (`p.fine`):**
Quellen: BfR, [Vorkochen für mehrere Tage: Was ist zu beachten?](https://www.bfr.bund.de/fragen-und-antworten/thema/vorkochen-fuer-mehrere-tage/) (08.07.2025); Verbraucherzentrale NRW, [Mikrowelle richtig nutzen](https://www.verbraucherzentrale.nrw/aufwaermen) und [Richtig einfrieren](https://www.verbraucherzentrale.nrw/unsere-lebensmittel/richtig-einfrieren) (Stand 22.12.2025); Verbraucherzentrale Niedersachsen, [Tipps und Tricks beim Einfrieren und Auftauen](https://www.verbraucherzentrale-niedersachsen.de/wissen/lebensmittel/gesund-ernaehren/tipps-und-tricks-beim-einfrieren-und-auftauen-120371) (Stand 26.09.2025); Zu gut für die Tonne!, [Richtig lagern](https://www.zugutfuerdietonne.de/tipps-fuer-zu-hause/richtig-lagern) (Stand 20.02.2026); BZfE, [Richtig lagern](https://www.bzfe.de/kueche-und-alltag/kochen/lebensmittel-richtig-lagern). Tage von FreshTrack NFC: Standardwerte der App.

**† Für dieses Gericht gibt es keine eigene Zahl.** Dort steht der allgemeine Wert der Verbraucherzentrale Niedersachsen für «Selbstgekochtes»: 1 bis 3 Monate bei −18 °C. Eine amtliche deutsche Tabelle mit Monaten pro gekochtem Gericht haben wir nicht gefunden, und eine Zahl, die die Quellen nicht nennen, schreiben wir nicht in die Tabelle.

Drei Dinge zum Lesen der Tabelle:
- **Die Werte von FreshTrack NFC sind nicht amtlich.** Es sind Startwerte der App, und du kannst sie ändern (siehe unten).
- **Bei drei Gerichten liegt die App über den Quellen**, und das sollst du wissen: Reis (2 Tage statt 24 Stunden), Nudeln (3 Tage statt 1–2) und Soße (4 Tage statt 2–3). Wer sich an die Quellen halten will, stellt Reis auf 1, Nudeln auf 2 und Soße auf 3 Tage.
- **Im Gefrierschrank liegt die App innerhalb der Quelle:** 30, 60 oder 90 Tage, also 1 bis 3 Monate, wie die Verbraucherzentrale Niedersachsen für Selbstgekochtes angibt.

Egal nach welcher Spalte du gehst: **Gezählt wird ab dem Kochtag**, nicht ab dem Tag, an dem du den Behälter zum ersten Mal öffnest. Das ist unsere Lesart ⚑7; die Quellen sprechen von «nach der Zubereitung» (BfR) und nennen keinen anderen Startpunkt.

## Sonderfall Reis  `#reis`

Reis ist der Fall, bei dem die Quellen am deutlichsten werden. Die Verbraucherzentrale NRW schreibt: «Reis direkt nach dem Kochen abkühlen lassen, im Kühlschrank aufbewahren, innerhalb von 24 Stunden verbrauchen und beim Aufwärmen auf mindestens 70 Grad erhitzen.»

Der Grund steht im Merkblatt des BfR zu bakteriellen Toxinen: Das Bakterium *Bacillus cereus* bildet Sporen, die normales Kochen überleben. Bleibt gekochter Reis zu lange warm, keimen sie aus, vermehren sich und können ein Gift bilden (Cereulid), das gegenüber Hitze «extrem widerstandsfähig» ist. Typisch betroffen sind laut BfR «stärkehaltige, gekochte Lebensmittel wie Reis oder Nudeln». Deshalb hilft gründliches Aufwärmen allein nicht, wenn der Reis vorher falsch gelagert wurde.

Was das praktisch heißt:
1. **Schnell abkühlen**, in flachen Portionen statt im großen Topf (BfR).
2. **Nicht stundenlang im Topf oder Reiskocher stehen lassen.** Das ist unsere Lesart der Regel «schnell abkühlen»; eine Stundenzahl für Reis nennen die deutschen Quellen nicht.
3. **In den Kühlschrank und innerhalb von 24 Stunden essen** (Verbraucherzentrale NRW).
4. **Beim Aufwärmen überall auf mindestens 70 °C** bringen, in der Mikrowelle zwischendurch umrühren (BfR, Verbraucherzentrale NRW).

Und Reis mit Gemüse oder mit Hähnchen? Unsere Lesart ⚑7: Es zählt die empfindlichste Zutat, also 24 Stunden.

## Abkühlen: schnell und flach  `#abkuehlen`

- **Höchstens zwei Stunden bei Raumtemperatur** (EFSA, [Safe2Eat](https://www.efsa.europa.eu/de/safe2eat/proper-food-handling)). Das BfR formuliert es so: Reste «innerhalb weniger Stunden auf unter + 7 °C» abkühlen.
- **Flach und in Portionen.** «Größere Speisemengen dafür in mehrere flache Schalen füllen» (BfR). Die österreichische AGES rät außerdem, die Portionen in ein kaltes Wasserbad zu stellen ([Sicher kochen](https://www.ages.at/mensch/ernaehrung-lebensmittel/ernaehrungsempfehlungen/sicher-kochen)).
- **Warum das so wichtig ist:** Keime vermehren sich laut BfR «zwischen 10 °C und 60 °C» besonders gut. Diesen Bereich soll Essen beim Abkühlen «möglichst schnell durchlaufen». Ein großer, heißer Topf braucht dafür lange, auch im Kühlschrank; kleine flache Portionen nicht.
- **Geschlossen lagern.** Das BfR empfiehlt luftdicht schließende Behälter mit dem Glas-Gabel-Symbol, gründlich gereinigt, und in jedem Behälter nur so viel, wie du auf einmal essen willst.

## Wohin im Kühlschrank?  `#wo`

- **Temperatur: höchstens 7 °C, besser unter 5 °C** (BfR). Die AGES nennt 1 bis 5 °C. Eine Umfrage des BfR von 2020 ergab im Schnitt 5,5 °C in deutschen Kühlschränken, aber nur die Hälfte der Befragten hatte überhaupt eine Temperaturanzeige oder ein Thermometer. Ein einfaches Kühlschrankthermometer lohnt sich also.
- **Am kältesten ist es unten an der Rückwand.** Für «eine mehrtägige Lagerung der vorbereiteten Mahlzeiten» eignet sich dieser Bereich laut BfR am besten.
- **Rohes ganz unten, Gekochtes geschlossen darüber.** Rohes Fleisch gehört auf einem Teller ins unterste Fach über dem Gemüsefach (Zu gut für die Tonne!), damit kein Fleischsaft auf anderes tropft; zubereitete Speisen halten sich laut BZfE auf den Ablagen darüber am besten.
- **Nicht in die Tür.** Dort ist es am wärmsten (BZfE).

## Einfrieren: wie lange und wie  `#einfrieren`

**Wie lange?** Hier gehen die Angaben auseinander, und das hat einen Grund.
- Verbraucherzentrale Niedersachsen: **Selbstgekochtes 1 bis 3 Monate** bei −18 °C. Je mehr Fett, desto kürzer.
- BfR, nach Lebensmittelart: Rind- und Schweinefleisch 3–6 Monate, Geflügel 3 Monate, Fisch 6 Monate, Gemüse 6–12 Monate, «wenn gegart oder blanchiert bis zu 12 Monaten».
- AGES: bei −18 °C oder kälter «fast alle Lebensmittel in entsprechender Verpackung ca. 10 Monate».

Warum so unterschiedlich? Weil es im Gefrierschrank vor allem um **Qualität** geht, nicht um Keimwachstum. Laut BfR stellen die meisten lebensmittelrelevanten Bakterien schon bei −5 bis −8 °C die Vermehrung ein. Selbst eine Tiefkühltemperatur von −12 °C statt −18 °C verkürze vor allem die Haltbarkeit und schade der Qualität, etwa durch Gefrierbrand: «Dies bedeutet aber keine gesundheitliche Gefährdung.» Die Monatsangaben sind also Qualitätsangaben. Abgetötet werden die Keime durch Kälte aber nicht (AGES, Verbraucherzentrale Niedersachsen): Nach dem Auftauen gilt wieder die Kühlschrank-Uhr.

**Wie?**
- **Erst abkühlen, dann einfrieren** (BfR, Verbraucherzentrale Niedersachsen).
- **Portionsweise und mit möglichst wenig Luft** im Behälter, sonst droht Gefrierbrand (BfR).
- **Suppe ohne Einlage** einfrieren, Nudeln oder Kartoffeln werden sonst matschig (Verbraucherzentrale NRW).
- **Nicht einfrieren:** gekochte Eier (werden gummiartig) und Gelatinespeisen (werden wässrig) (Verbraucherzentralen NRW und Niedersachsen).

## Beschriften: was auf den Behälter gehört  `#beschriften`

Alle Quellen sind sich einig, dass ein Datum auf den Behälter gehört:
- BfR: neben der Bezeichnung des Lebensmittels «das Datum der Einlagerung», «denn nicht alle Lebensmittel können gleich lange tiefgekühlt aufbewahrt werden».
- BZfE: beschriften «mit Inhalt, Menge und Einfrierdatum».
- Verbraucherzentrale Niedersachsen: zusätzlich eine Liste «auf Papier oder in einer App» mit Inhalt, Menge bzw. Portionen und Einfrierdatum; neues Gefriergut nach unten, älteres nach oben.

Was in den Quellen nicht steht und sich bei uns bewährt hat ⚑7:
- **Zwei Daten, wenn etwas erst in den Kühlschrank und dann in den Gefrierschrank geht:** «gekocht 24.11. · eingefroren 26.11.». Das Kochdatum zählt für den Kühlschrank, das Einfrierdatum für die Monate im Gefrierschrank.
- **Den Inhalt so genau, dass du nicht öffnen musst:** «Linseneintopf mit Wurst, 2 Portionen» statt «Eintopf».
- **Auf den Deckel**, nicht auf die Seite, wenn du Behälter stapelst; mit **Kreppband und einem wasserfesten Stift** ⚑3, die sich nach dem Spülen wieder abziehen lassen.
- Wer nicht schreiben will: ein **[NFC-Etikett auf dem Deckel](../../en/guides/nfc-labels-food-containers.html)** (Ratgeber bisher nur auf Englisch) leistet dasselbe ohne Tinte, und man kann es für den nächsten Inhalt neu beschreiben.

## Aufwärmen und Auftauen  `#aufwaermen`

- **Überall mindestens 70 °C, mindestens 2 Minuten** (BfR), auch innen. In der Mikrowelle zwischendurch umrühren (BfR, Verbraucherzentrale NRW). Das Schweizer BLV sagt dasselbe für bereits gekochte Speisen ([Hygiene im Umgang mit Lebensmitteln](https://www.blv.admin.ch/de/hygiene-im-umgang-mit-lebensmitteln)).
- **Nur so viel aufwärmen, wie du isst.** Das BfR empfiehlt Portionen pro Mahlzeit gerade deshalb, damit keine aufgewärmten Reste noch einmal gekühlt werden müssen. Für Spinat rät die Verbraucherzentrale NRW ausdrücklich: nur einmal erwärmen und sofort essen; Babys sollten keinen aufgewärmten Spinat bekommen.
- **Im Kühlschrank auftauen**, zum Beispiel über Nacht (BfR, Verbraucherzentrale NRW, AGES), nicht bei Raumtemperatur.
- **Wieder einfrieren?** Hier unterscheiden die Quellen. AGES und BLV: aufgetaute Lebensmittel nicht wieder einfrieren. Nur **angetaut** (außen weich, innen noch gefroren, etwa nach einem Stromausfall) ist es laut BfR bei gegarten Speisen möglich, laut AGES «aus mikrobiologischer Sicht kein Problem», aber mit Qualitätsverlust. Am einfachsten: nur auftauen, was du auch isst.

## Warum der Geruchstest nicht reicht  `#geruch`

«Riecht noch gut, also ist es gut?» Das BfR sagt dazu: Die Faustregel «sehen, riechen, schmecken» berücksichtigt keine Krankheitserreger wie Salmonellen oder Campylobacter, weil sie Geruch und Geschmack nicht verändern; verschiedene Keime «halten auch der Geruchsprobe stand». Und das Gift von *Bacillus cereus* im Reis (siehe oben) riecht man auch nicht.

Umgekehrt gilt: Schimmel oder kleine Gasbläschen bedeuten in jedem Fall wegwerfen (BfR).

Reste haben kein aufgedrucktes Datum. Das Datum bist du. Wenn du nicht mehr weißt, wann du gekocht hast: im Zweifel nicht mehr essen.

**Für wen besondere Vorsicht gilt:** Schwangere, ältere Menschen, Menschen mit Vorerkrankungen und Kinder unter fünf Jahren. Für sie ist Vorkochen für mehrere Tage laut BfR «weniger gut geeignet».

## Von Hand oder mit FreshTrack NFC  `#freshtrack`

**CTA, Satz in Fettdruck:** Das alles geht ohne App: mit der Tabelle oben, einem wasserfesten Stift und einem Streifen Kreppband.

Schreib das Kochdatum auf den Deckel und schau in die Tabelle, wenn du unsicher bist. Das reicht.

Wir haben FreshTrack NFC gebaut ⚑5, weil wir nicht jeden Sonntag neu rechnen wollten. Du klebst ein wiederbeschreibbares NFC-Etikett auf den Deckel der Dose ⚑2, trägst in der App ein, was drin ist, und wählst, ob sie in den Kühlschrank oder den Gefrierschrank kommt. Die App errechnet das Datum aus der Lebensmittelart und dem Lagerort, mit den Tagen aus der Tabelle oben, gezählt ab dem Tag, an dem du die Dose in der App befüllst. Hältst du später dein iPhone an den Deckel, siehst du Inhalt und Datum, ohne den Behälter zu öffnen. Auf dem Etikett steht nur ein Link; was drin ist, steht in der App. Ist die Dose leer, beschreibst du das Etikett für den nächsten Inhalt neu.

Die App erinnert dich einmal am Tag, standardmäßig zwei Tage vorher um 9:00 Uhr. Tage und Uhrzeit änderst du in den Einstellungen; unter **Einstellungen → Haltbarkeitszeiten** stellst du zum Beispiel Reis auf 1 Tag (Kühlschrank 1–30 Tage, Gefrierschrank 1–365 Tage). Die Änderung gilt für Dosen, die du danach befüllst.

FreshTrack NFC ist kostenlos, ohne Werbung, ohne In-App-Käufe und ohne Konto. Deine Daten bleiben auf deinem Gerät und in deinem privaten iCloud. NFC-Etiketten lesen und beschreiben geht nur mit einem iPhone; die App gibt es für iPhone und iPad. Und ja: Sie ist von uns ⚑5.

**[Insignia App Store `de-black.svg` / `de-white.svg`, `alt`: «Laden im App Store»]** → enlace de §1.1

**Haftungshinweis (`p.fine`, dentro del `.cta`; texto literal de la app, clave `the-dates-freshtrack-calculates-are-approximate-estimates` de `Localizable.xcstrings`, alemán):** Die von FreshTrack berechneten Daten sind grobe Schätzungen auf Basis allgemeiner Empfehlungen zur Aufbewahrung von Lebensmitteln (Richtlinien wie FoodKeeper des USDA und Empfehlungen zur Lebensmittelsicherheit). Sie ersetzen nicht das auf der Verpackung aufgedruckte Verbrauchsdatum oder Mindesthaltbarkeitsdatum, noch dein eigenes Urteil über Aussehen, Geruch oder Geschmack des Lebensmittels. Im Zweifel nicht mehr verzehren.

*(Igual que en la guía italiana: el descargo se copia de la app tal cual. Si `legal-privacy` o `appstore-qa` quieren que en la web cite las fuentes alemanas en vez de «FoodKeeper», es decisión suya.)*

## Häufige Fragen, kurz beantwortet  `#fragen`

### Wie lange ist gekochtes Essen im Kühlschrank haltbar?
2 bis 3 Tage. Das BfR rät, erhitzte Mahlzeiten innerhalb von 2–3 Tagen zu verbrauchen oder einzufrieren; Gerichte mit rohen Bestandteilen spätestens am Tag nach der Zubereitung.

### Wie lange hält gekochter Reis im Kühlschrank?
24 Stunden. Die Verbraucherzentrale NRW rät, Reis direkt nach dem Kochen abzukühlen, im Kühlschrank aufzubewahren, innerhalb von 24 Stunden zu verbrauchen und auf mindestens 70 °C aufzuwärmen.

### Wie lange halten gekochte Nudeln im Kühlschrank?
1 bis 2 Tage im obersten Kühlschrankfach, in einem geschlossenen Behälter (Zu gut für die Tonne!).

### Wie lange hält Suppe oder Eintopf im Kühlschrank?
2 bis 3 Tage, wie alle erhitzten Mahlzeiten (BfR). Eine eigene Zahl für Suppe oder Eintopf nennen die deutschen Quellen, die wir gelesen haben, nicht.

### Wie lange hält Bolognese im Kühlschrank?
2 bis 3 Tage (BfR, allgemeine Regel). Eine eigene Angabe für Bolognese haben wir in den amtlichen Quellen nicht gefunden.

### Hält gekochtes Hähnchen 7 Tage im Kühlschrank?
Keine der amtlichen Quellen, die wir gelesen haben, nennt 7 Tage. Für erhitzte Mahlzeiten, auch mit Geflügel, nennt das BfR 2–3 Tage.

### Wie lange halten gekochte Kartoffeln im Kühlschrank?
Eine eigene Zahl für gekochte Kartoffeln haben wir bei BfR, BZfE, Verbraucherzentralen und Zu gut für die Tonne! nicht gefunden. Es gilt die allgemeine Regel: 2–3 Tage (BfR).

### Darf warmes Essen in den Kühlschrank, und wie lange darf es draußen stehen?
Höchstens zwei Stunden bei Raumtemperatur (EFSA). Das BfR rät, Speisen schnell unter 7 °C abzukühlen und größere Mengen dafür auf mehrere flache Schalen zu verteilen.

### Wie lange kann man gekochtes Essen einfrieren?
1 bis 3 Monate bei −18 °C für Selbstgekochtes (Verbraucherzentrale Niedersachsen). Danach leidet vor allem die Qualität; Keime vermehren sich bei dieser Temperatur nicht (BfR).

### Wie oft darf man Essen aufwärmen?
Am besten nur einmal: Das BfR empfiehlt Portionen pro Mahlzeit, damit aufgewärmte Reste nicht erneut gekühlt werden müssen. Beim Aufwärmen überall mindestens 70 °C für 2 Minuten.

### Wie beschrifte ich eingefrorenes Essen?
Mit Inhalt, Menge und Einfrierdatum (BZfE, BfR). Geht etwas erst in den Kühlschrank und dann in den Gefrierschrank, schreib beide Daten auf.

### Kann ich am Geruch erkennen, ob Reste noch gut sind?
Nicht sicher. Laut BfR verändern Erreger wie Salmonellen Geruch und Geschmack nicht. Schimmel oder Gasbläschen bedeuten aber immer: wegwerfen.

### Wie lange ist Meal Prep haltbar?
Erhitzte Gerichte 2–3 Tage, Gerichte mit rohen Komponenten höchstens 1 Tag (BfR). Für Schwangere, ältere Menschen und kleine Kinder ist Meal Prep laut BfR weniger gut geeignet.

---

**Pie:** [Diesen Ratgeber auf Italienisch lesen](../../it/guide/quanto-dura-cibo-cotto-in-frigo.html) · [Leer en español](../../guias/cuanto-dura-comida-cocinada-nevera.html) · [Read this guide in English](../../en/guides/how-long-leftovers-last.html)

**Ficha para `de/ratgeber/index.html`** (tarjeta, como las de `it/guide/index.html`):
- `h2`: Wie lange ist gekochtes Essen im Kühlschrank haltbar?
- `p.q`: Kann ich das noch essen oder muss es weg?
- `p.fact`: Erhitzte Mahlzeiten 2–3 Tage laut BfR; gekochter Reis 24 Stunden laut Verbraucherzentrale NRW.

**Fuente de los datos de la app usados arriba** (para quien revise): los diez tipos y sus días, `FreshTrack/Services/SeedData.swift:12-25`, iguales en el tag `testflight-1.3-37` (la versión publicada es la 1.3); nombres alemanes, `Localizable.xcstrings` (`cooked-rice` = «Gekochter Reis»…); aviso a 2 días y 9:00, `Views/Settings/SettingsView.swift:7` y `:9`; topes 1–30 y 1–365, `Views/Settings/FoodTypeListView.swift:100-101`; «Haltbarkeitszeiten» = clave `expiration-times`; fecha = día de llenado + días del tipo, `Models/Models.swift:225-230`; gratis, sin anuncios ni compras ni cuenta, una notificación al día, iCloud privado, NFC solo en iPhone, «für iPhone und iPad»: descripción publicada de la ficha DE (lookup 24-11); la etiqueta lleva un enlace y no el contenido: corrección del 23-11 en `knowledge/marketing.md`.

---

## 2. Traducción al español (para que el dueño sepa qué se publica)

> Migas: FreshTrack › Guías › Comida cocinada en la nevera · Kicker: Guía

# ¿Cuánto dura la comida cocinada en la nevera? Plato a plato, según las fuentes oficiales

**Entradilla:** Arroz, pasta, sopa, guiso, carne, pescado, verdura y salsa: qué dicen el Instituto Federal de Evaluación de Riesgos (BfR), las centrales de consumidores (Verbraucherzentralen) y el Centro Federal de Nutrición (BZfE), dónde no dan una cifra, y cómo etiquetar las sobras para no tener que adivinar.

**Firma:** Publicada el [fecha] por SOFTAPP SOLUTIONS LLC · Actualizada el [fecha] · Fuentes comprobadas el 24 de noviembre de 2026

**Índice:** 1. En pocas palabras · 2. Plato a plato · 3. El caso del arroz · 4. Enfriar: rápido y en plano · 5. ¿Dónde en la nevera? · 6. Congelar: cuánto y cómo · 7. Etiquetar: qué va en el recipiente · 8. Recalentar y descongelar · 9. Por qué no basta con olerlo · 10. A mano o con FreshTrack NFC · 11. Preguntas frecuentes, en corto

## En pocas palabras
La comida cocinada aguanta en la nevera **2 a 3 días**. Lo dice el BfR: es aconsejable «consumir o congelar las comidas calentadas en 2-3 días». Los platos con ingredientes crudos, como verdura cruda o ensalada, «como muy tarde un día después de prepararlos».

Hay dos casos más estrictos: el **arroz cocido**, en **24 horas** (Verbraucherzentrale NRW), y las **sobras de pasta**, que en el estante más alto de la nevera aguantan **uno o dos días** (Zu gut für die Tonne!). Las setas cocinadas, también solo 24 horas y bien frías (Verbraucherzentrale NRW).

Todo esto vale solo con una nevera fría: **máximo 7 °C, mejor 5 °C** (BfR). Y lo que no te dé tiempo a comer va al congelador: lo cocinado en casa aguanta a −18 °C unos **1 a 3 meses** (Verbraucherzentrale Baja Sajonia). Nuestro consejo: mejor congelarlo el primer día que el último.

## Plato a plato
FreshTrack NFC trae diez tipos de comida cocinada (más carne y pescado crudos, que no son el tema). Para cada uno: qué dicen las fuentes oficiales y qué días propone la app por defecto.

| Plato | Nevera según las fuentes | Congelador (−18 °C) según las fuentes | FreshTrack NFC por defecto (nevera / congelador) |
|---|---|---|---|
| Arroz cocido | **24 horas** (VZ NRW) | 1–3 meses† | 2 días / 90 días |
| Pasta cocida | **1–2 días**, estante más alto (Zu gut für die Tonne!) | 1–3 meses† | 3 / 60 |
| Legumbres / guiso | 2–3 días (BfR) | 1–3 meses† | 3 / 90 |
| Sopa / crema | 2–3 días (BfR) | 1–3 meses†; mejor no congelar con pasta o patata dentro (VZ NRW) | 3 / 90 |
| Carne y ave cocinadas | 2–3 días (BfR) | 1–3 meses† | 3 / 90 |
| Pescado cocinado | 2–3 días (BfR) | 1–3 meses† | 2 / 60 |
| Verdura cocinada | 2–3 días (BfR); **setas 24 horas** (VZ NRW) | cocinada, **hasta 12 meses** (BfR, para verdura) | 3 / 60 |
| Tortilla / huevo | 2–3 días (BfR, general); huevos duros, unas dos a cuatro semanas (BZfE) | los huevos cocidos mejor no congelarlos: quedan gomosos (VZ NRW y Baja Sajonia) | 2 / 30 |
| Salsa casera (p. ej. boloñesa) | 2–3 días (BfR) | 1–3 meses† | 4 / 90 |
| Postre casero | 2–3 días (BfR); con ingredientes crudos, máximo 1 día (BfR) | los postres con gelatina se aguan (VZ Baja Sajonia) | 3 / 30 |

**† Para ese plato no hay cifra propia.** Se pone el valor general de la VZ Baja Sajonia para «lo cocinado en casa»: 1 a 3 meses a −18 °C. No hemos encontrado una tabla oficial alemana de meses por plato cocinado, y no ponemos una cifra que las fuentes no dan.

Tres cosas para leer la tabla: los valores de la app no son oficiales y se pueden cambiar; **en tres platos la app está por encima de las fuentes**, arroz (2 días frente a 24 horas), pasta (3 frente a 1–2) y salsa (4 frente a 2–3), y quien quiera atenerse a las fuentes pone el arroz en 1, la pasta en 2 y la salsa en 3; en el congelador la app está dentro de la fuente (30, 60 o 90 días: 1 a 3 meses). Se cuenta **desde el día en que cocinaste**, no desde que abres el recipiente (lectura nuestra; las fuentes dicen «tras la preparación»).

## El caso del arroz
La VZ NRW: «Dejar enfriar el arroz justo después de cocerlo, guardarlo en la nevera, consumirlo en 24 horas y recalentarlo a al menos 70 grados». El motivo, según la hoja del BfR sobre toxinas bacterianas: *Bacillus cereus* forma esporas que sobreviven a la cocción; si el arroz se queda templado, germinan, se multiplican y pueden formar una toxina (cereulida) «extremadamente resistente» al calor. Afecta típicamente a «alimentos cocinados ricos en almidón, como el arroz o la pasta». Por eso recalentar bien no basta si antes se guardó mal. En la práctica: enfriar rápido en porciones planas; no dejarlo horas en la olla o en la arrocera (lectura nuestra de «enfriar rápido»: las fuentes alemanas no dan horas para el arroz); nevera y 24 horas; recalentar a 70 °C en todo el plato, removiendo en el microondas. ¿Arroz con verdura o con pollo? Lectura nuestra: manda el ingrediente más delicado, 24 horas.

## Enfriar: rápido y en plano
Máximo dos horas a temperatura ambiente (EFSA); el BfR dice enfriar las sobras «en pocas horas por debajo de +7 °C». En plano y por raciones: «repartir las cantidades grandes en varias fuentes planas» (BfR); la AGES austriaca añade ponerlas al baño de agua fría. El porqué: según el BfR los gérmenes se multiplican sobre todo «entre 10 °C y 60 °C», y la comida debe atravesar ese rango «lo más rápido posible»; una olla grande y caliente tarda mucho, incluso en la nevera. Cerrado: recipientes herméticos con el símbolo del vaso y el tenedor, bien limpios, y en cada uno solo lo que vayas a comer de una vez (BfR).

## ¿Dónde en la nevera?
Máximo 7 °C, mejor por debajo de 5 °C (BfR); la AGES dice 1 a 5 °C. Una encuesta del BfR de 2020 dio una media de 5,5 °C en las neveras alemanas, pero solo la mitad de los encuestados tenía indicador de temperatura o termómetro. Lo más frío es abajo, junto a la pared del fondo, y según el BfR es la mejor zona para guardar varios días comidas preparadas. Lo crudo abajo del todo, sobre un plato, para que no gotee (Zu gut für die Tonne!); lo cocinado, cerrado, en los estantes de encima (BZfE). En la puerta no: es lo más cálido (BZfE).

## Congelar: cuánto y cómo
Las cifras no coinciden, y hay un motivo. VZ Baja Sajonia: lo cocinado en casa, 1 a 3 meses; cuanta más grasa, menos. BfR, por tipo de alimento: vacuno y cerdo 3–6 meses, ave 3, pescado 6, verdura 6–12 y «cocinada o escaldada, hasta 12 meses». AGES: a −18 °C «casi todos los alimentos, bien envasados, unos 10 meses». La diferencia es porque en el congelador lo que está en juego es sobre todo la **calidad**: según el BfR la mayoría de las bacterias dejan de multiplicarse ya a −5/−8 °C, e incluso congelar a −12 °C en vez de −18 °C acorta sobre todo la duración y daña la calidad (quemaduras de congelación): «Esto no supone, sin embargo, ningún riesgo para la salud». Los meses son, por tanto, de calidad. El frío no mata los gérmenes (AGES, VZ Baja Sajonia): al descongelar vuelve a contar el reloj de la nevera. Cómo: enfriar antes de congelar; por raciones y con el mínimo aire; la sopa sin pasta ni patata; no congelar huevos cocidos (gomosos) ni postres con gelatina (se aguan).

## Etiquetar: qué va en el recipiente
Todas las fuentes coinciden en poner la fecha: el BfR, nombre del alimento y «fecha de almacenamiento», «porque no todos los alimentos aguantan lo mismo congelados»; el BZfE, «contenido, cantidad y fecha de congelación»; la VZ Baja Sajonia, además una lista «en papel o en una app» con contenido, raciones y fecha, lo nuevo abajo y lo viejo arriba. Lo que no dicen las fuentes y nos funciona: **dos fechas** si algo pasa de la nevera al congelador («cocinado 24.11 · congelado 26.11»): la de cocinado cuenta para la nevera y la de congelado para los meses de congelador; el contenido tan concreto que no haga falta abrir («guiso de lentejas con salchicha, 2 raciones»); en la tapa si apilas, con cinta de carrocero y rotulador permanente, que se despegan al fregar. Quien no quiera escribir: una etiqueta NFC en la tapa (guía de momento solo en inglés) hace lo mismo sin tinta y se reescribe para el siguiente contenido.

## Recalentar y descongelar
Al menos 70 °C durante al menos 2 minutos en todo el plato (BfR), removiendo en el microondas; el BLV suizo dice lo mismo para lo ya cocinado. Calienta solo lo que vas a comer: el BfR recomienda raciones por comida precisamente para no tener que volver a enfriar sobras ya calentadas; para las espinacas, la VZ NRW dice calentar una sola vez y comer enseguida, y nunca a bebés. Descongelar en la nevera, por ejemplo de un día para otro (BfR, VZ NRW, AGES). ¿Volver a congelar? Las fuentes distinguen: AGES y BLV, lo descongelado no se recongela; lo solo **a medio descongelar** (blando por fuera, congelado por dentro, por ejemplo tras un apagón) es posible en platos cocinados según el BfR y «desde el punto de vista microbiológico, sin problema» según la AGES, pero pierde calidad. Lo más sencillo: descongela solo lo que vayas a comer.

## Por qué no basta con olerlo
El BfR: la regla «ver, oler, probar» no tiene en cuenta patógenos como la salmonela o el campylobacter, que no cambian olor ni sabor; hay gérmenes que «resisten la prueba del olfato». La toxina del arroz tampoco se huele. Al revés, moho o burbujitas de gas: a la basura siempre (BfR). Las sobras no traen fecha impresa: la fecha eres tú; si no recuerdas cuándo cocinaste, ante la duda no te lo comas. Precaución especial para embarazadas, mayores, personas con enfermedades previas y niños menores de cinco años: para ellos cocinar para varios días es «menos adecuado» (BfR).

## A mano o con FreshTrack NFC
**En negrita:** Todo esto se puede hacer sin app: con la tabla de arriba, un rotulador permanente y un trozo de cinta de carrocero. Escribe la fecha en la tapa y mira la tabla si dudas. Con eso basta.

Hicimos FreshTrack NFC porque no queríamos volver a hacer la cuenta cada domingo. Pegas una etiqueta NFC regrabable en la tapa, apuntas en la app qué hay dentro y eliges nevera o congelador. La app calcula la fecha con el tipo de comida y el sitio, con los días de la tabla, contando desde el día en que llenas el recipiente en la app. Al acercar luego el iPhone a la tapa ves qué hay y la fecha sin abrirlo. En la etiqueta solo hay un enlace; el contenido está en la app. Cuando se vacía, reescribes la etiqueta para lo siguiente. Avisa una vez al día, por defecto dos días antes a las 9:00. Días y hora se cambian en Ajustes; en **Ajustes → Tiempos de caducidad** pones, por ejemplo, el arroz a 1 día (nevera 1–30 días, congelador 1–365). El cambio vale para lo que llenes después. Es gratis, sin anuncios, sin compras y sin cuenta; los datos se quedan en tu aparato y en tu iCloud privado. Leer y escribir etiquetas NFC solo con iPhone; la app es para iPhone y iPad. Y sí: es nuestra.

[Insignia de la App Store] · Descargo: el texto de la app en alemán («Las fechas que calcula FreshTrack son estimaciones aproximadas basadas en recomendaciones generales de conservación… Ante la duda, no lo consumas»).

## Preguntas frecuentes, en corto
1. **¿Cuánto dura la comida cocinada en la nevera?** 2 a 3 días; con ingredientes crudos, al día siguiente como mucho (BfR).
2. **¿Y el arroz cocido?** 24 horas, enfriado enseguida y recalentado a 70 °C (VZ NRW).
3. **¿La pasta cocida?** 1 a 2 días en el estante más alto, cerrada (Zu gut für die Tonne!).
4. **¿Sopa o guiso?** 2 a 3 días; las fuentes no dan cifra propia (BfR).
5. **¿Boloñesa?** 2 a 3 días por la regla general; sin cifra propia en las fuentes oficiales.
6. **¿El pollo cocinado aguanta 7 días?** Ninguna fuente oficial que hemos leído dice 7 días; el BfR da 2–3 para comidas calentadas.
7. **¿Patatas cocidas?** Sin cifra propia en las fuentes; regla general, 2–3 días (BfR).
8. **¿Puede ir caliente a la nevera y cuánto puede estar fuera?** Máximo dos horas fuera (EFSA); enfriar rápido por debajo de 7 °C repartido en fuentes planas (BfR).
9. **¿Cuánto se puede congelar?** 1 a 3 meses a −18 °C lo cocinado en casa (VZ Baja Sajonia); luego sufre sobre todo la calidad (BfR).
10. **¿Cuántas veces se puede recalentar?** Mejor una: raciones por comida para no volver a enfriar (BfR); a 70 °C, 2 minutos.
11. **¿Cómo etiqueto lo congelado?** Contenido, cantidad y fecha de congelación (BZfE, BfR); si pasó antes por la nevera, las dos fechas.
12. **¿Se nota por el olor si está bien?** No con seguridad (BfR); moho o burbujas, siempre a la basura.
13. **¿Cuánto dura el meal prep?** Calentado, 2–3 días; con crudos, 1 día (BfR); poco adecuado para embarazadas, mayores y niños pequeños.

Pie: leer en italiano · en español · en inglés.

---

## 3. Siguiente tanda: como mucho 5 guías, por este orden

**Criterio:** solo idiomas cuyas tiendas convierten (IT, FR, DE, AT, CH; el inglés no: 455 impresiones → 1
descarga en 30 días). Demanda observada en el autocompletado de Google del 24-11 (mismo método que §1.3),
lo que dicen las reseñas del sector, y lo que ya existe y se puede adaptar en vez de escribir de cero.

**Reseñas del sector (leídas hoy):** las 206 reseñas más recientes en la App Store **alemana** de seis apps
de despensa y congelador (FoodShiner, Smantry, Haltbar Bis, MHD Butler, GefrierGut, Vorratskammer;
`itunes.apple.com/de/rss/customerreviews/…/sortBy=mostRecent/json`). Lo que más sale: **«Überblick»/inventario
(26)** y **suscripción, precio o anuncios (27)**; congelador 11; etiquetas/NFC/QR 4; restos/«Vorkocher» 3.
Dos citas que describen nuestro público: «Tiefkühltruhen Chaos ade. Habe eigene Etiketten für meine
Tupperware erstellt» y «perfekt für Vorkocher … Leute, die gerne selbst kochen und Selbstgekochtes
aufbewahren». Lectura: lo que se pide es **saber qué hay en el congelador**, y **«gratis y sin anuncios»
diferencia**.

| Orden | Idioma | Consulta objetivo | Demanda observada (autocompletado 24-11) | Por qué esta | Base para adaptar |
|---|---|---|---|---|---|
| 1 | **de** | «Gefrierschrank-Inventarliste» (kostenlos, zum Ausdrucken, App) | «gefrierschrank inventarliste», «…inventarliste kostenlos», «…inventar app», «…inventarliste app»; «gefrierschrank beschriften / schubladen beschriften» | Intención de producto, no de salud (no compite con el BfR). La Verbraucherzentrale Niedersachsen recomienda literalmente «eine Liste auf Papier oder in einer App». Es lo que más piden las reseñas alemanas («Überblick»). Las fuentes alemanas de congelación **ya están leídas hoy** (§1.2): es la más barata. Una lista imprimible gratis es útil sin instalar nada y es lo que otro sitio enlazaría | `guias/inventario-congelador.html`, `en/guides/freezer-inventory.html` |
| 2 | **fr** | «Combien de temps se conserve un plat cuisiné au frigo» | «…un plat préparé au frigo», «…un plat cuit au frigo», «combien de temps garder un plat fait maison au frigo»; cola: «le riz cuit (au frigo / au congélateur / à température ambiante)», «un oeuf dur au frigo»; «plat chaud frigo ou pas» | Francia convierte y no tiene ni una guía. **Mismo formato que ya funciona** (la ES saca impresiones; IT y DE lo replican), y sirve también a la Suiza francófona (autocompletado `gl=ch` idéntico). Hay que leer las fuentes francesas (ANSES, ministerio de Agricultura) antes de escribir: **no las he comprobado** | la guía alemana de hoy (estructura y método), la ES |
| 3 | **de** | «NFC-Sticker: Ideen und Anleitung fürs iPhone» (aplicado a recipientes) | «nfc sticker ideen», «nfc sticker iphone», «…programmieren», «…beschreiben», «…einrichten»; «nfc etiketten», «zwilling nfc etiketten» | Es el diferencial de la app y el **destino natural de un enlace de Shop NFC** (tiene versión alemana). Riesgo: ZWILLING ocupa «nfc etiketten» con su sistema FRESH & SAVE (`seo-estado` §7); por eso se apunta a «Ideen» e «iPhone», no a «Etiketten» | `guias/etiquetas-nfc-tuppers.html`, `it/guide/etichette-nfc-contenitori.html` |
| 4 | **fr** | «Inventaire congélateur à imprimer gratuit» | primera sugerencia: «inventaire congélateur à imprimer gratuit»; luego «…pdf», «…excel», «application inventaire congélateur», «fiche / tableau inventaire congélateur» | La demanda francesa es explícitamente de **lista imprimible**: material útil sin app, y la app como paso siguiente. Hacerla después de la 1 (misma plantilla, otro idioma) | la DE de la tanda (1) |
| 5 | **it** | «Quanto dura il cibo cotto in freezer» (ragù, carne cotta, brodo) | «quanto dura il cibo cotto in freezer», «quanto dura in freezer la carne cotta / il ragù / il brodo di carne»; la primera sugerencia de «quanto dura il cibo in freezer» es «…senza corrente» | Italia es la tienda que más descarga. **Va última a propósito**: la guía italiana del 03-11 no encontró ninguna fuente italiana con meses de congelador para cocinados (`guias-it-texto-2026-11-03.md` §0.2), y la variante del apagón es tema de seguridad donde Google prefiere organismos públicos. Antes de escribirla, ver si las dos italianas publicadas sacan impresiones (revisión 19-12) | `guias/cuanto-dura-comida-congelador.html` |

**Lo que descarto de esta tanda, y por qué:**
- **Cualquier guía en inglés.** No convierte (455 impresiones de búsqueda → 1 descarga). Además, la guía EN
  de comida cocinada sale en la caché del panel como «Google no reconoce esta URL»: eso es trabajo de
  `seo-indexing` (técnico), no de contenido nuevo.
- **Portugués (Brasil).** 2 descargas y tema de seguridad donde mandan los organismos (`plan-difusion` §4).
- **«Wie lange hält gekochter Reis» como guía aparte.** Tiene mucha cola, pero ya la cubre `#reis` de la
  guía de hoy; una segunda página competiría con la primera.
- **«Gekochte Kartoffeln im Kühlschrank giftig / weiß geworden».** Demanda real, pero no he encontrado
  fuente oficial que la conteste; sin fuente, no hay guía.
- **Más de una guía a la vez por idioma nuevo.** Primero ver que la primera se indexa.

---

## 4. Para que los asistentes de IA la encuentren y la citen

### 4.1 Lo que dice la documentación pública hoy (leída el 2026-11-24)

| Fuente | Lo que dice | Consecuencia |
|---|---|---|
| Google, «AI features and your website» — `https://developers.google.com/search/docs/appearance/ai-features` | «There are no additional requirements to appear in AI Overviews or AI Mode»; «There's also no special schema.org structured data that you need to add»; para salir como enlace de apoyo, la página tiene que estar indexada y poder mostrarse con fragmento | Lo que cuenta es **estar indexada** y ser la mejor respuesta. El marcado no es la palanca |
| Google, «AI optimization guide» (actualizada 2026-07-10) — `https://developers.google.com/search/docs/fundamentals/ai-optimization-guide` | Contenido «non-commodity» (punto de vista propio, no reciclar lo que ya dicen otros) es lo que más influye; llms.txt: «Google Search ignores them», ni ayuda ni perjudica; no hace falta «chunking»; los datos estructurados no son necesarios para la IA, pero sí para los resultados enriquecidos; medir con el informe **«Generative AI performance»** de Search Console | El ángulo de la guía (comparar fuentes, decir dónde no dan cifra y dónde la app se pasa) es justo lo que pide. llms.txt: no |
| Google, registro de cambios — `https://developers.google.com/search/updates` | 08-05-2026: el resultado enriquecido de FAQ deja de mostrarse desde el 07-05-2026; 15-06-2026: documentación de FAQ retirada. La de HowTo redirige a su retirada (2023). La galería de datos estructurados de hoy no incluye ni FAQ ni HowTo | `FAQPage` y `HowTo` no dan nada en Google. No hacen daño, pero no se añaden nuevos |
| Google, «Software app (SoftwareApplication)» (actualizada 2026-09-08) — `https://developers.google.com/search/docs/appearance/structured-data/software-app` | Requiere `name`, `offers.price` y **`aggregateRating` o `review`** | Con 0 valoraciones la app **no es elegible**. No se pone en la guía; y nunca se rellena con valoraciones inventadas |
| OpenAI, «Overview of OpenAI Crawlers» — `https://developers.openai.com/api/docs/bots` | `OAI-SearchBot` es el que decide si una web sale en las respuestas de búsqueda de ChatGPT; se recomienda permitirlo en `robots.txt` y permitir sus IP. `GPTBot` es solo entrenamiento, independiente. `ChatGPT-User` es el acceso a petición del usuario | Hay que dejar entrar a `OAI-SearchBot`. Hoy entra (abajo) |
| OpenAI, «Searching the web with ChatGPT» — `https://help.openai.com/en/articles/9237897` | Para ser elegible: permitir OAI-SearchBot y que el host o la CDN no bloqueen sus IP. ChatGPT «partners with other search providers», y cita la política de privacidad de **Microsoft** | Estar bien en **Bing** importa para ChatGPT, no solo Google |

**Comprobado hoy en el sitio:**
- `robots.txt` servido: `User-agent: * / Allow: / / Sitemap: …`. Permite a todos, incluidos `OAI-SearchBot`,
  `GPTBot`, `ClaudeBot`, `PerplexityBot` y `bingbot`.
- `freshtrack.softapp.tech` lo sirve **GitHub Pages directamente** (`server: GitHub.com`, `via: 1.1 varnish`),
  **sin Cloudflare delante**: no hay un WAF ni un «bloquear bots de IA» que pueda cortar a OpenAI.
  Una petición a la guía italiana con el user-agent de `OAI-SearchBot`, `GPTBot`, `ChatGPT-User`,
  `ClaudeBot`, `PerplexityBot` y `bingbot` da **200** en los seis (desde una IP que no es suya, así que
  solo prueba que no hay filtro por user-agent).
- Existe la clave de IndexNow en la raíz (`b6658d12….txt`, desde el 17-07, contenido = nombre).

### 4.2 Recomendación concreta

**Para `web-dev` (al maquetar la guía):**
1. `Article` + `BreadcrumbList`, como las italianas, con `inLanguage: "de-DE"`, fechas y `citation`. **Nada más.**
   Ni `FAQPage`, ni `HowTo`, ni `SoftwareApplication` en la guía.
2. El bloque `#fragen` en **HTML visible**: `h3` con la pregunta tal como la teclea la gente y un `p` corto
   que empieza por la respuesta («2 bis 3 Tage.») y lleva la fuente en la misma frase. Es lo que un
   asistente puede citar sin contexto; no depende de ningún marcado.
3. La tabla en `<table>` real con `caption` (no imagen), y la fecha «Quellen geprüft am …» visible en la firma.
4. Enlace de la CTA con `ct=web-de-guia-gekocht` (y `pt` cuando exista), sin `/de/` en la ruta.

**Para `seo-indexing`:**
1. `robots.txt`: **no tocar.** Ya permite todo, y no hay CDN que bloquee. Añadir una línea explícita para
   `OAI-SearchBot` no cambia nada. (Si algún día se quisiera cortar el entrenamiento con `GPTBot` o
   `Google-Extended`, eso es decisión del dueño, y no afecta a que la guía salga en la búsqueda de ChatGPT ni de Google.)
2. **No crear `llms.txt`.** Google dice por escrito que lo ignora; OpenAI no lo menciona entre lo que
   necesita `OAI-SearchBot`. Sería mantenimiento sin beneficio documentado.
3. **Bing:** comprobar que la web está verificada en Bing Webmaster Tools con el sitemap, y al publicar
   la guía, avisar por IndexNow con la clave que ya existe. Es lo único de esta lista con efecto probable
   en ChatGPT, porque su búsqueda se apoya en Microsoft. **Sin comprobar** si la web está dada de alta en Bing.
4. `hreflang` recíproco de/it/es/en + sitemap + enlace desde el cuerpo de `de/index.html`.
5. Las `FAQPage` que ya hay en portadas y soporte (16 páginas) se pueden dejar: no dan resultado enriquecido
   desde mayo de 2026, pero no estorban. Quitarlas no es urgente; decisión suya.
6. Tarea aparte, más importante que todo lo anterior para la guía inglesa: `en/guides/how-long-leftovers-last.html`
   sale como «Google no reconoce esta URL» en la caché del 24-11. Mirar por qué.

---

## 5. Cómo se mide y cuándo se revisa

**Primero, lo que no se puede medir hoy, para no prometerlo:**
- **Visitas por página en el contador propio: hoy no existe.** El `b.js` que se sirve hoy
  (`https://softmetrics.softapp.tech/b.js`, leído el 24-11) envía solo `{h: host, v: sesión nueva}`. Calcula
  `location.pathname` pero solo lo usa para detectar `/download`; **no lo envía**. Sin ese cambio, el contador
  dice cuántas visitas tiene la web entera, no cuántas tiene esta guía. Arreglo: mandar también la ruta. Es
  de `swift-dev` (SoftMetrics) y lo valida `legal-privacy` (la ruta no identifica a nadie, pero el texto de
  privacidad de la web es suyo). Va en `SIGUIENTE`.
- **Descargas con `ct=web-de-guia-gekocht`: sin `pt` no se atribuyen.** App Store Connect necesita el
  `pt` de la cuenta para contar una campaña (`knowledge/seo.md`, 2026-09-16), y está pendiente del dueño
  desde el 16-09 (`knowledge/marketing.md`, 22-11). Mientras tanto, lo único que da la tienda es el
  dominio de origen en «Web Referrer» (`freshtrack.softapp.tech`, solo desde Safari) y la app de origen en
  «App Referrer» (`com.openai.chat` para ChatGPT), por país.

| Señal | Fuente | Línea base | Revisión |
|---|---|---|---|
| La URL alemana, indexada | Caché del panel (M2, `indexacion_freshtrack…`), o Inspección de URL en Search Console | no existe aún | **4 semanas tras publicar** (si se publica el 01-12: **29-12-2026**) |
| Impresiones y consultas de la página DE, por país (DE, AT, CH) | Search Console → Rendimiento, filtro por página; y el informe «Generative AI performance» | 0 consultas en alemán (31-08 → 31-10) | **8 semanas tras publicar**: **26-01-2027** |
| Primeras descargas desde ChatGPT en DE, AT y CH | ASC → Fuentes → App Referrer `com.openai.chat`, por país (`data-analyst`) | 5 en DE en octubre | Lectura de diciembre el **05-01-2027** y de enero el **05-02-2027** |
| Descargas por «Web Referrer» `freshtrack.softapp.tech` en DE/AT/CH | ASC (`data-analyst`) | 21 por enlaces web en total, 22-10 → 20-11, sin desglose por dominio en lo que tengo | 05-01-2027 |
| Campaña `web-de-guia-gekocht` | ASC → Campaigns | — (no medible sin `pt`) | En cuanto exista el `pt` |
| Visitas a la página | `b.js` | — (no guarda la ruta) | En cuanto `swift-dev` lo cambie |

**Punto de parada escrito antes de empezar:** si el **26-01-2027** la página está indexada y Search Console
no le da **ni una impresión** en DE, AT o CH, no se escribe la siguiente guía alemana de la tanda (la 1 de §3
se mantiene solo si sus fuentes siguen leídas) y se apunta en `knowledge/marketing.md` como resultado, con
los números. Si no está indexada, el problema es técnico o de autoridad, no de contenido, y va a `seo-indexing`.

**Qué esperar, sin prometer:** nada en las primeras 2-4 semanas (indexación); impresiones en la cola larga
hacia las 6-8 semanas si sigue el patrón de la guía española, que a los dos meses asomaba en la cola larga
pero en la segunda página (posición media ~15). Sin enlaces externos, no hay motivo para esperar la primera página en la consulta corta.
Lo de ChatGPT no tiene precedente medido en la casa más allá de las 5 descargas de octubre: es una apuesta.
