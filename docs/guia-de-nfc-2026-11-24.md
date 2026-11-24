---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía DE · NFC-Etiketten für Dosen (adaptación de la guía NFC) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. **El dueño ha decidido publicarla sin
revisión nativa**: las frases con más riesgo llevan ⚑ (lista en §4).

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `de/ratgeber/nfc-etiketten-dosen.html` (junto a `de/ratgeber/gekochtes-essen-kuehlschrank.html`) |
| `hreflang` | `de` → esta · `es` → `/guias/etiquetas-nfc-tuppers.html` · `en` → `/en/guides/nfc-labels-food-containers.html` · `it` → `/it/guide/etichette-nfc-contenitori.html` · `fr` → `/fr/guides/etiquettes-nfc-boites.html` (guía FR de hoy) · `x-default` → la inglesa. Recíproco en todas |
| Enlace a la tienda | `https://apps.apple.com/de/app/id6791699550?pt=126402967&ct=web-de-guia-nfc&mt=8` (mismo formato que la guía DE publicada) |
| `<title>` (66) | `NFC-Etiketten für Dosen: NTAG213 oder NTAG215, Gefrierfach, iPhone` |
| `meta description` (153) | `Welches NFC-Etikett du für Frischhaltedosen kaufst, ob es Gefrierfach und Spülmaschine aushält und wie das iPhone es liest, ohne App zu öffnen. Mit Quellen.` |
| `og:title` | `NFC-Etiketten für Dosen und Gefrierschrank` |
| JSON-LD | `Article` (`inLanguage: "de-DE"`, `citation`: las URL de §1.1) + `BreadcrumbList` (FreshTrack › Ratgeber › NFC-Etiketten für Dosen). Ni `FAQPage` ni `HowTo` (motivo en `guia-de-cocido-nevera-2026-11-24.md` §4) |
| Enlaces internos | Las tres anclas de `de/index.html` que hoy van a la guía inglesa (`de/index.html:625`, `:707`, `:748`) y la URL dentro del texto de la FAQ JSON-LD (`:103`) deberían apuntar a esta. Y desde la guía DE de comida cocinada (`#beschriften`), que hoy enlaza la inglesa |
| Ficha para `de/ratgeber/index.html` | `h2`: NFC-Etiketten für Dosen · `p.q`: Welches Etikett, wohin damit, hält es das Gefrierfach aus? · `p.fact`: NTAG213 reicht (144 Byte); ab iPhone XS liest das iPhone sie im Hintergrund. |

### 1.1 Fuentes, comprobadas hoy (2026-11-24)

| # | Fuente | Qué da |
|---|---|---|
| A1 | Apple Developer, «Adding Support for Background Tag Reading» — `https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading` (leída por su JSON) | «iPhone XS and later support background tag reading»; solo con el iPhone «in use»; cinco casos sin lectura (nunca desbloqueado, sesión Core NFC, Wallet/Apple Pay, cámara, modo avión); busca el primer registro URI; enlace universal → abre la app, sin app → Safari; si está bloqueado, pide desbloquear antes de pasar los datos |
| A2 | Apple Support (DE), «Modelle mit Unterstützung für NFC-Tag-Leser» — `https://support.apple.com/de-de/guide/iphone/aside/asd-nfc-reader/15.0/ios` | Automático: iPhone SE (2. Generation und neuere), XR, XS, XS Max, 11 y posteriores. En el Kontrollzentrum: iPhone 7, 7 Plus, 8, 8 Plus, X. Solo modelos de iPhone |
| A3 | NXP, ficha técnica NTAG213/215/216, Rev. 3.2 (02-06-2015). **La URL oficial `nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf` da 404 hoy**; leída en una copia del mismo PDF (`datasheet.chipsmall.com/NT2H1311TTDUDZ/368586.pdf`, 26 páginas) | 144 / 504 / 888 bytes de memoria de usuario; «Data retention time of 10 years», «Write endurance 100.000 cycles», ambos **a Tamb = 22 °C**. **No da rango de temperatura de uso** en las páginas disponibles |
| A4 | Ficha DE de la App Store (lookup 24-11) | «Klebe ein wiederbeschreibbares NFC-Etikett auf den Deckel…», «Ist die Dose leer, wird das Etikett einfach neu beschrieben», «NFC-Etiketten lesen und beschreiben geht nur mit einem iPhone», gratis, sin anuncios, sin compras, sin cuenta |
| A5 | Código de la 1.3 publicada (tag `testflight-1.3-37`) | La etiqueta guarda `https://freshtrack.softapp.tech/t/#<id>`, el id en el fragmento, que no llega al servidor (`Services/EnlaceDeTupper.swift:8-11`); las etiquetas viejas de la 1.1/1.2 llevan `freshtrack://` y se siguen leyendo. Las Dosen se pueden crear sin etiqueta (`Models.swift:202`, `tagWritten = false` por defecto). Quien no tiene la app ve `freshtrack.softapp.tech/t/` (200, con texto en alemán) |

**Lo que no tiene fuente y la guía dice que no la tiene:** ni NXP ni Apple dan un dato para −18 °C ni para el
lavavajillas en pegatinas normales. **Aviso para `seo-indexing`/`web-dev`:** las guías NFC publicadas en ES,
EN e IT dicen que el chip funciona «entre −25 °C y +70 °C». Ese dato **no lo he podido confirmar** en la
ficha de NXP (ni la guía italiana pudo, `guias-it-texto-2026-11-03.md` §C). Recomiendo quitarlo o
sustituirlo por la frase de esta guía hasta que alguien lo encuentre en la ficha completa.

**Cálculo propio** (no es de una fuente, se dice como tal en el texto): lo que graba FreshTrack es un registro
NDEF URI de unos **71 bytes** (prefijo `https://` comprimido en 1 byte + `freshtrack.softapp.tech/t/#` + un UUID
de 36 caracteres + cabeceras). Cabe en un NTAG213 (144).

### 1.2 Consultas (autocompletado Google, `hl=de&gl=de`, 24-11)

«nfc sticker iphone», «nfc sticker programmieren iphone», «nfc sticker einrichten iphone», «nfc sticker scannen
iphone»; «nfc tag iphone lesen / auslesen / programmieren / beispiele»; «nfc tag automatisch lesen iphone»;
«ntag213 oder ntag215»; «nfc etiketten», «zwilling nfc etiketten». Sin sugerencias: «nfc tag gefrierschrank».

---

## 2. TEXTO DE LA PÁGINA (alemán)

> **Migas:** FreshTrack › Ratgeber › NFC-Etiketten für Dosen · **Kicker:** Ratgeber

# NFC-Etiketten für Dosen und Gefrierschrank: welches kaufen, wohin kleben, wie das iPhone sie liest

**Lead:** Welches NFC-Etikett du brauchst (NTAG213 oder NTAG215), was es im Gefrierfach und in der Spülmaschine aushält, wie du es mit dem iPhone beschreibst und warum neuere iPhones es lesen, ohne dass du eine App öffnest. Das meiste geht ganz ohne unsere App.

**Byline:** Veröffentlicht am [Datum] von SOFTAPP SOLUTIONS LLC · Quellen geprüft am 24. November 2026

**Inhaltsverzeichnis:** 1. Kurz gesagt (`#kurz`) · 2. Was ist ein NFC-Etikett? (`#was`) · 3. NTAG213 oder NTAG215? (`#kaufen`) · 4. Gefrierfach und Spülmaschine (`#kaelte`) · 5. Wohin kleben (`#wohin`) · 6. Mit dem iPhone beschreiben (`#beschreiben`) · 7. Lesen, ohne eine App zu öffnen (`#hintergrund`) · 8. Von Hand oder mit FreshTrack NFC (`#freshtrack`) · 9. Häufige Fragen (`#fragen`)

## Kurz gesagt  `#kurz`

- **Kauf ein wiederbeschreibbares Etikett mit NTAG213.** Laut Datenblatt des Herstellers NXP hat es 144 Byte Speicher; für einen Link oder eine kurze Notiz reicht das. NTAG215 (504 Byte) brauchst du nur für lange Texte.
- **Ab iPhone XS liest das iPhone das Etikett im Hintergrund:** Du hältst es an den Deckel, es erscheint eine Mitteilung, du tippst darauf. Dafür muss auf dem Etikett ein **Link** stehen, kein reiner Text (Apple).
- **Für das Gefrierfach und die Spülmaschine** gibt weder NXP noch Apple eine Angabe für normale Aufkleber. Was hält, hängt vom Aufkleber ab, nicht vom Chip: Achte auf die Angaben des Verkäufers.
- **Das iPad liest keine NFC-Etiketten**; Apple führt nur iPhone-Modelle auf.

## Was ist ein NFC-Etikett?  `#was`

Ein NFC-Etikett (auch NFC-Tag oder NFC-Sticker genannt) ist ein dünner Aufkleber mit einem winzigen Chip und einer aufgedruckten Antenne, ohne Batterie. Ab Werk steht nichts darauf. Du beschreibst es mit dem Handy und kannst es wieder überschreiben. Für Dosen ist genau das der Unterschied zu Kreppband oder Papieretiketten: Es nutzt sich nicht ab. Dose leer, spülen, und beim nächsten Mal überschreibst du dasselbe Etikett, ohne etwas abzuziehen oder neu zu kleben.

## NTAG213 oder NTAG215?  `#kaufen`

Die meisten günstigen NFC-Sticker haben einen Chip der Familie NTAG21x von NXP, fast immer NTAG213 oder NTAG215. Der eigentliche Unterschied steht im Datenblatt von NXP: **144 Byte** Nutzerspeicher beim NTAG213, **504 Byte** beim NTAG215 (NTAG216: 888 Byte).

Wie viel braucht man? Ein Beispiel aus unserer eigenen App: Der Link, den FreshTrack NFC auf ein Etikett schreibt, belegt nach unserer Rechnung etwa **71 Byte**. Ein NTAG213 reicht also mit Abstand; eine kurze Textnotiz («Linsen · eingefroren 6.9.») ebenso. NTAG215 lohnt sich nur für lange Notizen.

Bei der Haltbarkeit sind beide Chips gleich: NXP gibt **10 Jahre** Datenerhalt und **100.000 Schreibzyklen** an, gemessen bei 22 °C. Bei einem Neubeschreiben pro Woche ist der Chip damit nicht das, was zuerst aufgibt. ⚑1

Mit dem iPhone funktionieren beide ohne Zubehör: Apple nennt iPhone 7 und neuer als Modelle mit NFC-Tag-Leser.

*(`p.fine`)* In diesem Ratgeber gibt es absichtlich keine Kauflinks.

## Gefrierfach und Spülmaschine: was man weiß und was nicht  `#kaelte`

Ehrlich gesagt: **Eine Herstellerangabe für −18 °C oder für die Spülmaschine haben wir für normale NFC-Aufkleber nicht gefunden.** Die Werte im Datenblatt von NXP (10 Jahre, 100.000 Zyklen) gelten bei 22 °C; einen Temperaturbereich für den Betrieb nennt der Teil des Datenblatts, den wir lesen konnten, nicht.

Was wir daraus ableiten ⚑2:
- **Der Chip ist selten das Problem, eher der Aufkleber.** Kleber und bedruckte Schicht entscheiden, ob das Etikett im Gefrierfach hält. Kauf Etiketten, die der Verkäufer ausdrücklich für Kühl- oder Gefrierschrank angibt, am besten mit einer Schutzschicht (laminiert).
- **Spülmaschine nur, wenn der Verkäufer «spülmaschinenfest» angibt.** Sonst den Deckel von Hand spülen.
- **Kondenswasser:** Wenn du die Dose aus dem Gefrierfach nimmst, beschlägt der Deckel. Trockne ihn ab, bevor er zurückkommt, damit kein Wasser unter den Kleber zieht.

## Wohin kleben  `#wohin`

- **Auf den Deckel**, nicht an die Seite: So liest du es, ohne die Dose aus dem Stapel zu ziehen.
- **Auf eine flache Stelle, weg von Metall.** Metall stört das Feld der Antenne. Hat der Deckel einen Metallbügel, klebe das Etikett auf den Kunststoffteil, der am weitesten davon entfernt ist.
- **Nicht über ein Scharnier oder einen Verschluss, der sich biegt.** Die Antenne ist eine sehr dünne Leiterbahn; ständiges Knicken kann sie brechen. ⚑2

## Mit dem iPhone beschreiben  `#beschreiben`

Das geht mit jeder NFC-App aus dem App Store, die NDEF schreiben kann; es muss nicht unsere sein.

1. Öffne die App und wähle «Schreiben» (manchmal «Write»).
2. Wähle einen **Link (URL)** oder einen **Text**. Warum das wichtig ist, steht im nächsten Abschnitt.
3. Halte den **oberen Teil der Rückseite** des iPhones (bei der Kamera) an das Etikett, bis die App das Schreiben bestätigt.
4. Zum Wiederverwenden einfach neu schreiben; das überschreibt den alten Inhalt.

## Lesen, ohne eine App zu öffnen  `#hintergrund`

Das kennen die wenigsten: **Ab iPhone XS liest das iPhone NFC-Etiketten von selbst** («iPhone XS and later support background tag reading», Apple). Keine App muss offen sein. Du hältst das iPhone an das Etikett, oben erscheint eine Mitteilung, und wenn du darauf tippst, öffnet iOS die passende App oder, wenn keine passt, den Link in Safari. Ist das iPhone gesperrt, verlangt iOS erst das Entsperren, bevor es die Daten an die App gibt.

Laut Apple automatisch dabei: iPhone XR, XS, XS Max, iPhone SE ab der 2. Generation und alle ab iPhone 11. Beim **iPhone 7, 7 Plus, 8, 8 Plus und X** musst du den **NFC-Tag-Leser im Kontrollzentrum** einschalten.

**Wann es nicht klappt** (Apple): Der Bildschirm muss an sein, und auch dann nicht, wenn das iPhone seit dem Einschalten noch nie entsperrt wurde, eine App gerade selbst NFC scannt, Wallet mit Apple Pay benutzt wird, die Kamera läuft oder der Flugmodus an ist.

> **`.box` Das Wichtigste für Dosen:** Das iPhone sucht auf dem Etikett nach einem **Link** (einem URI-Eintrag) und nimmt den ersten. Ein reiner **Text** wie «Linsen · 6.9.» lässt **keine** Mitteilung erscheinen; du kannst ihn nur mit einer geöffneten NFC-App lesen. Wenn du die Dose antippen und sofort etwas sehen willst, muss ein Link auf dem Etikett stehen.

## Von Hand oder mit FreshTrack NFC  `#freshtrack`

**CTA, Satz in Fettdruck:** Alles oben geht mit jeder NFC-App aus dem App Store, ohne unsere.

Wir haben FreshTrack NFC gebaut, weil wir nicht jeden Sonntag Datum und Haltbarkeit von Hand ausrechnen wollten ⚑3. Du klebst ein wiederbeschreibbares Etikett auf den Deckel, trägst in der App ein, was drin ist und ob die Dose in den Kühl- oder Gefrierschrank kommt, und die App errechnet das Datum aus Lebensmittelart und Lagerort. Auf das Etikett schreibt sie **nur einen Link**, keinen Inhalt: Was drin ist, steht in der App. Deshalb erkennt ein iPhone ab XS das Etikett von selbst. Halte das iPhone an den Deckel, tippe auf die Mitteilung, und die Dose öffnet sich in der App. Wer die App nicht hat, sieht beim Antippen eine kleine Webseite, die erklärt, was das Etikett ist. Ist die Dose leer, beschreibst du das Etikett für den nächsten Inhalt neu.

Etiketten braucht die App nicht: Dosen kannst du auch ohne Etikett anlegen und bearbeiten. Es funktionieren wiederbeschreibbare NTAG213- und NTAG215-Etiketten. NFC lesen und beschreiben geht nur mit einem iPhone; die App gibt es für iPhone und iPad. Kostenlos, ohne Werbung, ohne In-App-Käufe, ohne Konto. Wie lange gekochte Reste halten, steht in unserem Ratgeber [Wie lange ist gekochtes Essen im Kühlschrank haltbar?](gekochtes-essen-kuehlschrank.html).

**[Insignia `de-black.svg`/`de-white.svg`, `alt` «Laden im App Store»]** → enlace de §1.

## Häufige Fragen  `#fragen`

### NTAG213 oder NTAG215 – welches NFC-Etikett für Dosen?
NTAG213 reicht. Laut NXP hat es 144 Byte Speicher; ein Link braucht etwa 70 Byte. NTAG215 (504 Byte) nur für lange Texte.

### Funktionieren NFC-Sticker mit dem iPhone?
Ja, ab iPhone 7, ohne Zubehör (Apple). Ab iPhone XS werden sie sogar ohne geöffnete App gelesen.

### Hält ein NFC-Etikett im Gefrierschrank?
Eine Herstellerangabe für −18 °C haben wir für normale Aufkleber nicht gefunden; die NXP-Werte gelten bei 22 °C. Entscheidend ist der Aufkleber: Kauf Etiketten, die ausdrücklich für den Gefrierschrank angegeben sind.

### Sind NFC-Sticker spülmaschinenfest?
Nur, wenn der Verkäufer das angibt. Eine allgemeine Angabe von NXP oder Apple gibt es nicht. Im Zweifel den Deckel von Hand spülen.

### Warum erscheint beim Antippen keine Mitteilung?
Entweder steht auf dem Etikett nur Text statt eines Links, das iPhone ist älter als XS, der Bildschirm ist aus, oder Kamera, Wallet oder Flugmodus sind aktiv (Apple).

### Kann das iPad NFC-Etiketten lesen?
Nein. Apple führt für den NFC-Tag-Leser nur iPhone-Modelle auf.

### Wie oft kann man ein NFC-Etikett neu beschreiben?
Laut NXP 100.000 Mal (bei 22 °C), bei 10 Jahren Datenerhalt.

### Wo klebt man das NFC-Etikett auf die Dose?
Auf eine flache Stelle des Deckels, weg von Metall und nicht über ein Scharnier.

---

**Pie:** [Leer en español](../../guias/etiquetas-nfc-tuppers.html) · [Read in English](../../en/guides/nfc-labels-food-containers.html) · [Leggi in italiano](../../it/guide/etichette-nfc-contenitori.html) · [Lire en français](../../fr/guides/etiquettes-nfc-boites.html)

---

## 3. Resumen fiel en español (para el dueño)

**Título:** «Etiquetas NFC para recipientes y congelador: cuál comprar, dónde pegarla, cómo la lee el iPhone».
- **En corto:** comprar NTAG213 (144 bytes según NXP; basta para un enlace o una nota corta; NTAG215, 504, solo para textos largos). Desde el iPhone XS, el iPhone lee la etiqueta en segundo plano: acercas, sale una notificación, la tocas; para eso la etiqueta tiene que llevar un **enlace**, no texto (Apple). Para congelador y lavavajillas **ni NXP ni Apple dan dato** para pegatinas normales: depende de la pegatina, mira lo que dice el vendedor. El iPad no lee NFC.
- **Qué es:** pegatina fina con chip y antena, sin batería, regrabable; no se gasta como la cinta o el papel.
- **NTAG213 o 215:** diferencia de memoria (144/504/888); el enlace de FreshTrack ocupa unos 71 bytes por cálculo nuestro; 10 años y 100.000 escrituras a 22 °C según NXP; iPhone 7 o posterior sin accesorios. Sin enlaces de compra.
- **Congelador y lavavajillas:** se dice claramente que no hay dato del fabricante; consejos nuestros marcados como tales: pegatina indicada para congelador y plastificada, lavavajillas solo si el vendedor lo garantiza, secar la tapa antes de volver a congelar.
- **Dónde pegar:** tapa, zona plana, lejos del metal y de bisagras.
- **Grabar:** con cualquier app NFC que escriba NDEF; enlace o texto; parte alta trasera del iPhone; reescribir sobrescribe.
- **Leer sin abrir app:** XS y posteriores (lista de Apple: XR, XS, XS Max, SE 2.ª gen., 11 en adelante); 7/8/X con el lector del Centro de control; casos en que no funciona (pantalla apagada, nunca desbloqueado, otra app escaneando, Wallet, cámara, modo avión). Recuadro: un texto no hace salir la notificación; un enlace, sí.
- **FreshTrack NFC:** escribe solo un enlace (el contenido está en la app); al acercar y tocar la notificación se abre la Dose; quien no tiene la app ve una página que lo explica; se reescribe al vaciar; se pueden crear Dosen sin etiqueta; NTAG213/215; NFC solo en iPhone, app para iPhone y iPad; gratis, sin anuncios, sin compras, sin cuenta. Enlace a la guía de comida cocinada.
- **8 preguntas cortas:** cuál comprar, si va con iPhone, congelador, lavavajillas, por qué no sale la notificación, iPad, cuántas reescrituras, dónde pegarla.

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «ist der Chip damit nicht das, was zuerst aufgibt» | Giro propio; alternativa neutra: «reicht das für viele Jahre» |
| ⚑2 | Los consejos marcados como «Was wir daraus ableiten» | Que se lea como criterio nuestro, no como dato |
| ⚑3 | «Wir haben FreshTrack NFC gebaut, weil …» | Traducción de «la hicimos porque»; alternativa «Wir haben FreshTrack NFC entwickelt, weil …» |
| — | «Mitteilung» por la notificación de iOS; «Lesen im Hintergrund» | Apple usa «Mitteilungen» en iOS alemán; el nombre que Apple da en alemán a *background tag reading* no lo he comprobado. «NFC-Tag-Leser» y «Kontrollzentrum» sí salen literales en la página de Apple (A2) |
