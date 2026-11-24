---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía DE · Gefrierschrank-Inventarliste (B1 de la tanda) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. Se publicará sin revisión nativa:
frases de riesgo con ⚑ (§4). Adapta `guias/inventario-congelador.html` y `en/guides/freezer-inventory.html`,
pero **todas las cifras son de fuentes alemanas o austriacas** (las ES/EN se apoyaban en la FSA británica).

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `de/ratgeber/gefrierschrank-inventarliste.html` |
| `hreflang` | `de` → esta · `es` → `/guias/inventario-congelador.html` · `en` → `/en/guides/freezer-inventory.html` · `fr` → `/fr/guides/inventaire-congelateur.html` (B3 de hoy) · `x-default` → la inglesa |
| Enlace a la tienda | `https://apps.apple.com/de/app/id6791699550?pt=126402967&ct=web-de-guia-inventar&mt=8` |
| `<title>` (67) | `Gefrierschrank-Inventarliste: kostenlos zum Ausdrucken oder als App` |
| `meta description` (148) | `Was auf eine Gefrierschrank-Inventarliste gehört, wie lange Eingefrorenes laut Verbraucherzentrale hält, und eine kostenlose Vorlage zum Ausdrucken.` |
| `og:title` | `Gefrierschrank-Inventarliste zum Ausdrucken` |
| JSON-LD | `Article` (`de-DE`, `citation` §1.1) + `BreadcrumbList` (FreshTrack › Ratgeber › Gefrierschrank-Inventarliste). Nada más |
| Plantilla imprimible | La tabla de `#vorlage` en HTML con CSS de impresión (`@media print`: solo la tabla, A4 apaisado, 20 filas vacías). Opcional para `web-dev`: un PDF en `de/ratgeber/gefrierschrank-inventarliste.pdf`. Sin pedir correo ni nada a cambio |
| Ficha para `de/ratgeber/index.html` | `h2`: Gefrierschrank-Inventarliste · `p.q`: Was liegt eigentlich im Gefrierschrank, und seit wann? · `p.fact`: Selbstgekochtes 1–3 Monate, Gemüse 6–12 Monate (Verbraucherzentrale Niedersachsen). |

### 1.1 Fuentes, leídas hoy (2026-11-24)

| # | Fuente | Qué da |
|---|---|---|
| F6 | Verbraucherzentrale Niedersachsen, «Tipps und Tricks beim Einfrieren und Auftauen» (Stand 26.09.2025) — `https://www.verbraucherzentrale-niedersachsen.de/wissen/lebensmittel/gesund-ernaehren/tipps-und-tricks-beim-einfrieren-und-auftauen-120371` | Lista «auf Papier oder in einer App»: Inhalt, Menge bzw. Portionen, Einfrierdatum, también en los recipientes; ordenar por grupos en cajones; lo nuevo abajo, lo viejo arriba. Tabla a −18 °C: Gemüse 6–12, Kräuter 3–4, Obst 9–12, Fleisch/Fisch 1–12, Wurst 1–6, Backwaren 1–3, Milchprodukte 2–6, Selbstgekochtes 1–3 meses; Schwein bis 8, Rind bis 12; más grasa, menos tiempo |
| F7 | BZfE, «Richtig lagern» — `https://www.bzfe.de/kueche-und-alltag/kochen/lebensmittel-richtig-lagern` | Beschriften «mit Inhalt, Menge und Einfrierdatum»; abtauen «ein- bis zweimal im Jahr», y entonces «eine kleine Inventur» |
| F5 | Verbraucherzentrale NRW, «Kalt gemacht» (Stand 22.12.2025) — `https://www.verbraucherzentrale.nrw/unsere-lebensmittel/richtig-einfrieren` | Fecha de congelación en todo, «ein Verzeichnis an die Tür des Gefrierschranks»; −18 °C o menos, constante; un congelador lleno gasta menos |
| F1 | BfR, «Vorkochen für mehrere Tage» (08.07.2025) — `https://www.bfr.bund.de/fragen-und-antworten/thema/vorkochen-fuer-mehrere-tage/` | Bezeichnung + Datum der Einlagerung, «denn nicht alle Lebensmittel können gleich lange tiefgekühlt aufbewahrt werden»; Rind/Schwein 3–6, Geflügel 3, Fisch 6, Gemüse 6–12 (gegart bis 12) meses |
| F2 | BfR, «Korrektes Kühlen» (FAQ 13.02.2023) — `https://www.bfr.bund.de/cm/343/korrektes-kuehlen-von-lebensmitteln-im-privathaushalt.pdf` | Apagón: un congelador «mit reichlich Gefriergut» mantiene el frío «über viele Stunden» si no se abre; a −18 °C los meses son de calidad |
| F10 | AGES, «Sicher kochen» — `https://www.ages.at/mensch/ernaehrung-lebensmittel/ernaehrungsempfehlungen/sicher-kochen` | −18 °C o menos: «fast alle Lebensmittel in entsprechender Verpackung ca. 10 Monate» |
| A4 | Ficha DE de la App Store (lookup 24-11) | Lo que se dice de la app (§2, `#freshtrack`) |

**Autocompletado (24-11, `gl=de`):** «gefrierschrank inventarliste», «…inventarliste kostenlos», «…inventar
app», «…inventarliste app»; «gefrierschrank beschriften», «…schubladen beschriften», «…fächer beschriften».
**Reseñas alemanas de apps del sector** (206, 24-11): «Überblick» es lo más repetido (26).

---

## 2. TEXTO DE LA PÁGINA (alemán)

> **Migas:** FreshTrack › Ratgeber › Gefrierschrank-Inventarliste · **Kicker:** Ratgeber

# Gefrierschrank-Inventarliste: wissen, was drin ist, ohne alles auszuräumen

**Lead:** Was auf eine Inventarliste gehört, damit sie nach drei Wochen noch stimmt, wie lange Eingefrorenes laut Verbraucherzentrale hält, und eine kostenlose Vorlage zum Ausdrucken. Eine App ist optional.

**Byline:** Veröffentlicht am [Datum] von SOFTAPP SOLUTIONS LLC · Quellen geprüft am 24. November 2026

**Inhaltsverzeichnis:** 1. Kurz gesagt (`#kurz`) · 2. Was auf die Liste gehört (`#inhalt`) · 3. Wie lange hält Eingefrorenes? (`#haltbarkeit`) · 4. Vier Arten, die Liste zu führen (`#methoden`) · 5. An einem Nachmittag eingerichtet (`#einrichten`) · 6. Die eine Regel, die die Liste am Leben hält (`#regel`) · 7. Vorlage zum Ausdrucken (`#vorlage`) · 8. Mit FreshTrack NFC (`#freshtrack`) · 9. Häufige Fragen (`#fragen`)

## Kurz gesagt  `#kurz`

Eine Inventarliste für den Gefrierschrank braucht pro Eintrag vier Dinge: **was es ist, wie viel, wann es eingefroren wurde und wo es liegt.** Die ersten drei empfiehlt die Verbraucherzentrale Niedersachsen wörtlich: eine Liste «auf Papier oder in einer App» mit Inhalt, Menge bzw. Portionen und Einfrierdatum, dieselben Angaben auch auf dem Behälter. Das Fach ist unsere Ergänzung ⚑1: Damit findest du es, ohne zu suchen.

Wie lange es hält: Selbstgekochtes **1 bis 3 Monate**, Gemüse **6 bis 12 Monate** bei −18 °C (Verbraucherzentrale Niedersachsen). Eine Vorlage zum Ausdrucken findest du [weiter unten](#vorlage).

## Was auf die Liste gehört  `#inhalt`

- **Was es ist.** Das Gericht, nicht die Verpackung: «Linseneintopf mit Wurst», nicht «Dose 3».
- **Wie viel.** Portionen oder Gramm (Verbraucherzentrale Niedersachsen, BZfE).
- **Eingefroren am.** Das Datum, an dem es in den Gefrierschrank kam (BfR, BZfE, beide Verbraucherzentralen). Das BfR begründet es so: «denn nicht alle Lebensmittel können gleich lange tiefgekühlt aufbewahrt werden».
- **Verbrauchen bis.** Einfrierdatum plus die Monate aus der Tabelle unten. Das ist eine Qualitätsgrenze, keine Sicherheitsgrenze (siehe nächster Abschnitt) ⚑1.
- **Wo.** Schublade oder Fach. Die Verbraucherzentrale Niedersachsen rät, nach Warengruppen in die Schubladen zu sortieren.
- **Entnommen am.** Durchstreichen reicht; das Datum zeigt dir später, wie schnell du was verbrauchst.

## Wie lange hält Eingefrorenes?  `#haltbarkeit`

**Tabelle** (`caption`: «Ungefähre Haltbarkeit bei −18 °C laut Verbraucherzentrale Niedersachsen, Stand 26.09.2025»)

| Lebensmittel | Haltbarkeit bei −18 °C |
|---|---|
| Selbstgekochtes | 1–3 Monate |
| Backwaren | 1–3 Monate |
| Kräuter | 3–4 Monate |
| Milchprodukte | 2–6 Monate |
| Wurst | 1–6 Monate |
| Fleisch / Fisch | 1–12 Monate (Schweinefleisch bis 8, Rindfleisch bis 12) |
| Gemüse | 6–12 Monate |
| Obst | 9–12 Monate |

*(`p.fine`)* Quelle: Verbraucherzentrale Niedersachsen, [Tipps und Tricks beim Einfrieren und Auftauen](https://www.verbraucherzentrale-niedersachsen.de/wissen/lebensmittel/gesund-ernaehren/tipps-und-tricks-beim-einfrieren-und-auftauen-120371). Je mehr Fett ein Lebensmittel enthält, desto kürzer die Lagerdauer.

**Andere Quellen, andere Zahlen.** Das BfR nennt nach Lebensmittelart Rind- und Schweinefleisch 3–6 Monate, Geflügel 3 Monate, Fisch 6 Monate, Gemüse 6–12 Monate. Die österreichische AGES sagt allgemein: bei −18 °C «fast alle Lebensmittel in entsprechender Verpackung ca. 10 Monate». Der Grund für die Spanne: Bei −18 °C vermehren sich Bakterien nicht; die Monate sagen, wie lange **Geschmack und Konsistenz** gut bleiben (BfR). Für deine Liste heißt das: Nimm den kürzeren Wert, wenn du es gut essen willst.

## Vier Arten, die Liste zu führen  `#methoden`

Keine ist falsch. Jede bricht an einer anderen Stelle.

| Methode | Kostet | Wer sieht sie | Wann sie nicht mehr stimmt | Erinnert sie? |
|---|---|---|---|---|
| Papierliste an der Tür (die Verbraucherzentrale NRW rät zu einem «Verzeichnis an der Tür») | Papier und Stift | Wer vor dem Gefrierschrank steht | Wenn jemand etwas herausnimmt, ohne es durchzustreichen | Nein |
| Tabelle (z. B. in einer Tabellen-App) | meist nichts | Wer den Link hat, auch unterwegs | Wenn das Handy-Öffnen vor dem Gefrierschrank mühsamer ist als Nachschauen | Nur wenn du selbst eine Regel einrichtest |
| Etikett auf jedem Behälter (Stift, Papier oder NFC) | Kreppband bis NFC-Etiketten | Wer die Tür öffnet und den Deckel liest | Fast nie, die Angabe reist mit dem Behälter. Aber ohne Liste keine Übersicht | Nein, außer NFC mit einer App, die das kann |
| App | je nach App | Du, auf dem Handy, ohne die Tür zu öffnen | Wie alle anderen: wenn du beim Einfrieren nichts einträgst | Ja, wenn die App das Datum berechnet und erinnert |

Wie wählen, ohne lange zu überlegen ⚑1: Allein oder zu zweit mit kleinem Gefrierfach: Liste an der Tür. Große Truhe im Keller: Etikett auf jedem Behälter **plus** Liste, sonst läufst du für jede Frage nach unten. Mehrere Haushalte (Zweitwohnung, Eltern): Tabelle oder App.

## An einem Nachmittag eingerichtet  `#einrichten`

Das ist das einzige Mal, dass du alles ausräumst. Danach erspart dir die Liste genau das.

1. **Ein guter Moment ist das Abtauen.** Das BZfE rät, das Gefriergerät ein- bis zweimal im Jahr abzutauen, und «bei dieser Gelegenheit bietet sich eine kleine Inventur des Inhalts an».
2. **Kühlbox oder Taschen bereitstellen**, damit nichts antaut, während du sortierst.
3. **Alles herausnehmen, Unbeschriftetes zuerst.** Was du nicht erkennst und nicht datieren kannst: im Zweifel nicht mehr essen.
4. **Nach Warengruppen in die Schubladen** (Verbraucherzentrale Niedersachsen) und jede Schublade benennen («Gekochtes», «Gemüse», «Fleisch»).
5. **Alles mit Inhalt, Menge und Datum beschriften** (BZfE) und gleichzeitig in die Liste eintragen.
6. **Älteres nach oben, Neues nach unten** (Verbraucherzentrale Niedersachsen), damit du zuerst greifst, was zuerst weg muss.

## Die eine Regel, die die Liste am Leben hält  `#regel`

**Eintragen, wenn etwas hineinkommt. Streichen, wenn etwas herauskommt.** Sofort, nicht abends. ⚑2 Jede Liste stirbt an demselben Punkt: dem einen Mal, an dem man es «gleich» nachträgt. Deshalb hängt die Papierliste an der Tür und nicht in der Küchenschublade, und deshalb liegt der Stift daneben.

## Vorlage zum Ausdrucken  `#vorlage`

**Gefrierschrank von: ____________ · Letzte Inventur: ____________**

| Was | Portionen | Eingefroren am | Verbrauchen bis | Fach | Entnommen am |
|---|---|---|---|---|---|
| Linseneintopf mit Wurst | 2 | 03.11. | 03.01. | Schublade 1 | |
| Brokkoli, blanchiert | 500 g | 10.11. | 10.05. | Schublade 3 | |
| *(20 leere Zeilen)* | | | | | |

*(Debajo de la tabla, en pequeño, impreso:)* Selbstgekochtes 1–3 Monate · Gemüse 6–12 · Obst 9–12 · Fleisch/Fisch 1–12 · Backwaren 1–3 (Verbraucherzentrale Niedersachsen, −18 °C).

*(Los ejemplos: «verbrauchen bis» = congelado + 2 meses para el guiso y + 6 meses para la verdura, dentro de los rangos de la tabla.)*

## Mit FreshTrack NFC  `#freshtrack`

**CTA, Satz in Fettdruck:** Die Papierliste oben reicht vielen. Wer sie lieber auf dem iPhone hat:

Wir haben FreshTrack NFC gebaut, damit die Liste auf dem Handy ist und von selbst erinnert ⚑3. Produkte trägst du per Barcode-Scan ein, und Lagerort und Standardhaltbarkeit setzt die App automatisch. Für Selbstgekochtes klebst du ein wiederbeschreibbares NFC-Etikett auf den Deckel; die App errechnet das Datum aus Lebensmittelart und Lagerort, und wenn du dein iPhone an den Deckel hältst, siehst du Inhalt und Datum. Du kannst Siri fragen: «Was habe ich bei FreshTrack im Gefrierschrank?». Erinnerungen kommen einmal am Tag, gruppiert nach abgelaufen, heute und diese Woche, und ein Widget zeigt den Überblick, ohne die App zu öffnen. Für Ferienwohnung oder Eltern legst du eigene Haushalte an, über iCloud zwischen **deinen** Geräten synchronisiert. Kostenlos, ohne Werbung, ohne In-App-Käufe, ohne Konto; die Daten bleiben auf deinem Gerät und in deinem privaten iCloud. NFC-Etiketten lesen und beschreiben geht nur mit einem iPhone. Mehr zu den Etiketten im Ratgeber [NFC-Etiketten für Dosen](nfc-etiketten-dosen.html).

**[Insignia `de-black.svg`/`de-white.svg`]** → enlace de §1.

## Häufige Fragen  `#fragen`

### Was gehört auf eine Gefrierschrank-Inventarliste?
Inhalt, Menge bzw. Portionen und Einfrierdatum (Verbraucherzentrale Niedersachsen), dazu das Fach. Dieselben Angaben gehören auf den Behälter.

### Gibt es eine Gefrierschrank-Inventarliste kostenlos zum Ausdrucken?
Ja, auf dieser Seite, ohne Anmeldung: Spalten für Inhalt, Portionen, Einfrierdatum, «verbrauchen bis», Fach und Entnahme.

### Wie lange halten eingefrorene Lebensmittel?
Bei −18 °C laut Verbraucherzentrale Niedersachsen: Selbstgekochtes 1–3 Monate, Gemüse 6–12, Obst 9–12, Fleisch und Fisch 1–12 Monate. Danach leidet vor allem die Qualität (BfR).

### Wie beschriftet man Gefrierbeutel und Dosen?
Mit Inhalt, Menge und Einfrierdatum (BZfE), wasserfest. Neues nach unten, Älteres nach oben (Verbraucherzentrale Niedersachsen).

### Wie oft sollte man den Gefrierschrank aufräumen?
Beim Abtauen, ein- bis zweimal im Jahr, bietet sich laut BZfE eine kleine Inventur an. Die Liste selbst hält nur, wenn du jedes Mal einträgst und streichst.

### Welche Temperatur sollte der Gefrierschrank haben?
Konstant −18 °C oder kälter (Verbraucherzentrale NRW, AGES).

### Wie lange hält der Gefrierschrank bei Stromausfall?
Laut BfR viele Stunden, wenn er gut gefüllt ist und zumindest in den ersten Stunden nicht geöffnet wird. Eine feste Stundenzahl nennt das BfR nicht.

---

**Pie:** [Leer en español](../../guias/inventario-congelador.html) · [Read in English](../../en/guides/freezer-inventory.html) · [Lire en français](../../fr/guides/inventaire-congelateur.html)

---

## 3. Resumen fiel en español (para el dueño)

**«Lista de inventario del congelador: saber qué hay sin vaciarlo».** Qué debe llevar cada entrada (qué es,
cuánto, fecha de congelación, dónde; las tres primeras las recomienda literalmente la Verbraucherzentrale
Baja Sajonia, «en papel o en una app»; el cajón es añadido nuestro); tabla de meses a −18 °C de esa misma
fuente (cocinado en casa 1–3, verdura 6–12, fruta 9–12, carne/pescado 1–12…), con las cifras distintas del BfR
y la AGES y el porqué (son meses de calidad, no de seguridad); cuatro maneras de llevar la lista con su punto
débil (papel en la puerta, hoja de cálculo, etiqueta en cada recipiente, app); cómo montarlo en una tarde
aprovechando la descongelación que el BZfE recomienda una o dos veces al año; la regla que la mantiene viva
(apuntar al meter, tachar al sacar); **plantilla imprimible gratis** sin pedir nada; FreshTrack NFC como opción
(escaneo de código de barras, etiqueta NFC en tapers, pregunta a Siri, un aviso al día, widget, varias casas
sincronizadas entre **tus** aparatos por iCloud — no se dice que se comparta con otras personas porque la
ficha no lo dice), gratis, sin anuncios, sin compras, sin cuenta; 7 preguntas cortas, incluida la del apagón
(«muchas horas» si está lleno y cerrado; el BfR no da horas exactas y la guía lo dice).

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | Las frases «unsere Ergänzung», «Wie wählen, ohne lange zu überlegen», «Qualitätsgrenze» | Que se lea como criterio nuestro; naturalidad |
| ⚑2 | «Sofort, nicht abends.» y «dem einen Mal, an dem man es „gleich" nachträgt» | Giro idiomático |
| ⚑3 | «damit die Liste auf dem Handy ist und von selbst erinnert» | Construcción algo forzada; alternativa: «damit du die Liste auf dem Handy hast und rechtzeitig erinnert wirst» |
| — | «Truhe im Keller», «Kreppband», «Tabellen-App» | Léxico |
