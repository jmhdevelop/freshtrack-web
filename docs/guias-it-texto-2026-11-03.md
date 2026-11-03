---
# Documento interno: Jekyll no lo publica en la web (sin esto, GitHub Pages serviría el .md tal
# cual, igual que sirve README.md con 200).
published: false
---

# FreshTrack: texto de las dos guías en italiano (acción A3 del plan de difusión) · 2026-11-03

**Hecho por:** `aso-copywriter`. **Alcance:** solo texto. No hay HTML, ni sitemap, ni nada publicado o empujado.
`web-dev` monta las páginas con este texto; publicar es desplegar y lo aprueba el dueño.
**Entrada:** `docs/plan-difusion-2026-11-03.md` (A3, A1 y §7), `docs/seo-estado-2026-11-03.md`,
`guias/cuanto-dura-comida-cocinada-nevera.html`, `guias/etiquetas-nfc-tuppers.html`, `guias/index.html`, `it/index.html`.

## 0. Lo que tiene que saber web-dev y quien revise

### 0.1 Cómo están hechas las guías existentes (para montarlas igual)

| Aspecto | Guía ES existente | Aquí |
|---|---|---|
| Tamaño | cocinada: 33 KB de HTML (unas 2.000 palabras de cuerpo); NFC: 32 KB | cocinada ≈ 2.600 palabras (con tablas); NFC ≈ 2.100 |
| Esqueleto | `nav` + migas (`crumbs`) + `kicker` «Guida» + `h1` + `p.lead` + `p.byline` + `nav.toc` + secciones `h2 id=` + bloque `.cta` con insignia App Store + `hr` + enlace a la versión en otro idioma | igual; los `id` de cada `h2` están en el índice de cada guía |
| Tabla | `.table-wrap` > `table.wrapcells` con `caption`, `th scope`, leyenda `†` en `p.fine` | la guía 1 lleva una tabla igual (5 columnas → 4) |
| Tarjetas / caja | NFC: `.cards` con `.card` y `p.fail`; `.box` para la conclusión práctica | igual en la guía 2 |
| JSON-LD | `Article` (headline, description, `inLanguage`, `datePublished`, `dateModified`, `author`/`publisher` = SOFTAPP SOLUTIONS LLC, `citation` con las fuentes) + `BreadcrumbList` | `inLanguage: "it-IT"`; las URL de `citation` están en cada guía, §A.1 y §B.1 |
| `hreflang` | `es`, `en`, `x-default` (→ en) en las dos | **las nuevas llevan `it`, `es`, `en` y `x-default`; y hay que añadir `hreflang="it"` recíproco en las páginas ES y EN** (si no, Google ignora el par). Es trabajo de `web-dev`/`seo-indexing`, no de texto |
| Barra de idioma | `#langbar` («This page is also available in English») | en italiano, el mensaje del `langbar` para quien llega con otro idioma lo decide `web-dev` |
| Pie de la guía | «Read this guide in English» | «Leggi questa guida in spagnolo / inglese» (ver la última línea de cada guía) |
| Descargo | `p.fine` dentro del `.cta` en la guía de cocinada | idéntico, traducido, en la guía 1 |

Rutas propuestas (decisión de `web-dev`; hoy `it/` solo tiene `index.html`, `privacy.html` y `supporto.html`):
`it/guide/quanto-dura-cibo-cotto-in-frigo.html`, `it/guide/etichette-nfc-contenitori.html` y un `it/guide/index.html`
(texto de las dos fichas del índice, al final de cada guía).

**Dos arreglos que salen de leer `it/index.html`** (no son texto de guía, los dejo dichos):
- `it/index.html:623`, `:705` y `:746` enlazan la guía NFC **en inglés** (`../en/guides/nfc-labels-food-containers.html`). Cuando exista la guía italiana, deberían apuntar a ella.
- La FAQ con JSON-LD de `it/index.html:101` también lleva esa URL inglesa en el texto.

**Enlace a la tienda (CTA).** El plan pide `ct=web-it-guia-cocinato` y `ct=web-it-guia-nfc`. Sin el `pt` (token del proveedor, A0, pendiente del dueño)
App Store Connect no atribuye la campaña. Enlace a poner, con `<pt>` cuando exista:
- Guía 1: `https://apps.apple.com/it/app/id6791699550?pt=<pt>&ct=web-it-guia-cocinato&mt=8`
- Guía 2: `https://apps.apple.com/it/app/id6791699550?pt=<pt>&ct=web-it-guia-nfc&mt=8`

Mientras no haya `pt`, el enlace normal `https://apps.apple.com/app/id6791699550` (como en las guías actuales) y la insignia `img/app-store/it-black.svg` / `it-white.svg` (existen).

**Nombre.** Las dos CTA dicen «FreshTrack NFC» (nombre de fuera de casa, plan §7). Ojo: en la tienda italiana la app aparece como
**«FreshTrack: scadenze e NFC»** (lookup iTunes, IT, 03-11). Quien busque «FreshTrack NFC» en el App Store la encuentra por «FreshTrack» + «NFC»; no hay desajuste
que rechace nada, pero el texto no promete un nombre exacto de la ficha. En pantalla de inicio sigue siendo «FreshTrack».

### 0.2 Cómo se ha hecho el texto de conservación (la parte que no se traduce)

La guía ES se apoya en FDA y FSA. **Aquí no se ha copiado ninguna cifra de ahí.** Lo que dicen las fuentes oficiales italianas y de la UE, leído el 03-11-2026:

| Fuente | Qué da | Qué NO da | Estado |
|---|---|---|---|
| **ISS** (Istituto Superiore di Sanità, proyecto SAC), nota de prensa «Gli avanzi delle Feste, dieci suggerimenti per conservarli in sicurezza riducendo gli sprechi», publicada 19-12-2025, editada 16-02-2026 | «Idealmente, non dovrebbero essere conservati per più di 2-3 giorni»; no más de dos horas fuera de la nevera; congelar en raciones pequeñas y en recipientes aptos; señales de deterioro | cifra por plato; meses de congelador; arroz | leída en directo (`curl`, 200) |
| **EFSA**, Safe2Eat, «Pratiche corrette» (revisada 31-03-2025) | no más de dos horas a temperatura ambiente; nevera por debajo de 5 °C; sopas y guisos a 70 °C al recalentar; «Evita di conservarli per troppo tempo, anche in frigorifero» | **ningún número de días** | leída en directo (200) |
| **Ministero della Salute**, «Etichette e igiene, ecco le regole per la sicurezza alimentare» (06-10-2022) | no preparar con demasiada antelación; guardar en nevera crudos, cocinados y listos para consumir por separado y en recipientes cerrados; recalentar a alta temperatura | **ningún número de días** | leída en directo (200) |
| **CREA/INRAN**, «Linee guida per una sana alimentazione», cap. 10 «La sicurezza dei tuoi cibi dipende anche da te» (reimpresión 2007) | nevera a 4-5 °C; nevera entre dos horas (una en verano); recalentar una sola vez; congelador a -18 °C «non conserva in eterno»; escribir la fecha | cifra de días para lo cocinado | leída en directo (PDF, 200). **Es de 2007**: se cita solo para reglas que no cambian, y se dice la fecha |
| **FSA** (Reino Unido), «Home food fact checker» | arroz: 24 horas en la nevera | — | leída en directo (200). **Es la única cifra no italiana ni de la UE y solo para el arroz**; la página lo dice |

Lo que **no** he podido leer: el dosier «Il mio frigo» del Ministero (la URL antigua `nsis.salute.gov.it` ya no existe y `salute.gov.it/portale/...` exige JavaScript y no devuelve texto),
ni ninguna tabla oficial italiana con meses de congelador para platos cocinados. Por eso la guía **dice** que las fuentes italianas dan una regla general y no una cifra por plato,
y no se inventa ninguna. La web española sí tenía cifras por plato porque FDA y FSA las publican.

### 0.3 Consultas objetivo (autocompletado de Google en italiano, `hl=it&gl=it`, 03-11-2026)

Cada consulta se ha lanzado al autocompletado con User-Agent de navegador genérico. Lo que devolvió, y dónde se atiende:

| Consulta | Sugerencias reales | Dónde |
|---|---|---|
| quanto dura il cibo cotto in frigo | «…sottovuoto in frigo», «…fuori dal frigo», «…in freezer», «…scongelato» | título, h1, §«La risposta breve»; sottovuoto/fuori/scongelato en §«Le domande più frequenti» |
| cibo cotto in frigo | «cibo cotto caldo in frigo», «conservare cibo cotto in frigo», «il cibo cotto va conservato in frigo» | §«Due ore» (caliente a la nevera) |
| quanto si conserva in frigo | «…l'insalata di riso», «…un uovo sodo», «…il sugo di pomodoro», «…il riso cotto» | §«Le domande più frequenti» |
| quanto dura il riso cotto in frigo | «…condito», «…sottovuoto», «…fuori frigo» | §«Il caso del riso» |
| quanto dura la pasta cotta in frigo | «…condita», «…al forno» | tabla + preguntas |
| quanto dura il sugo in frigo | «…sugo cotto», «…di pomodoro fatto in casa» | tabla + preguntas |
| quanto dura la verdura cotta in frigo | «…al vapore», «…scongelata» | tabla + preguntas (es la consulta de 4 impresiones en ES) |
| quanto dura il pollo / il pesce cotto in frigo | «…petto di pollo», «…pesce spada» | tabla + preguntas |
| quanto dura la minestra in frigo | «…di verdure», «…di fagioli», «…di legumi» | tabla + preguntas |
| quanto dura la frittata in frigo | «…frittata di patate», «…di zucchine» | tabla + preguntas |
| etichette nfc | «etichette nfc programmabili», «etichette adesive nfc», «etichette nfc cosa sono» | título, h1 y sección «Cos'è» de la guía 2 |
| tag nfc ntag213 | «tag nfc ntag213 215», «…adesivo» | §«Quale etichetta comprare» |
| tag nfc iphone | «…notifica», «…bloccato», «…iPhone 15» | §«Come scrivere…» y §«Leggerla senza aprire nessuna app» |
| come scrivere tag nfc | «come scrivere su tag nfc» | §«Come scrivere…» |
| tag nfc adesivi | «…personalizzati» | §«Cos'è» |
| etichette per congelatore | «etichette adesive per congelatore», «…per sacchetti congelatore» | §«Come si risolve oggi» (la alternativa competidora) |

Sin sugerencia (demanda mínima, como dice `seo-estado`): «etichette nfc per alimenti», «etichette nfc contenitori», «etichette nfc iphone», «etichette nfc congelatore».
Se usan igual en el cuerpo porque son lo que describe la página, pero no se promete que nadie las busque.

### 0.4 Marcas de revisión por un nativo

En el texto, ⚑ + número marca una frase que conviene que lea un nativo. La lista con el motivo está al final de cada guía. Ninguna es un error conocido: son decisiones de registro o de léxico donde un agente puede equivocarse.

---

---

# GUÍA 1 · Quanto dura il cibo cotto in frigo

## A.1 Ficha técnica (para el `<head>` y el JSON-LD)

| Campo | Texto | Caracteres |
|---|---|---|
| Ruta propuesta | `it/guide/quanto-dura-cibo-cotto-in-frigo.html` | — |
| `<title>` | `Quanto dura il cibo cotto in frigo, piatto per piatto — FreshTrack NFC` | 70 |
| `<title>` alternativo (más corto, sin marca) | `Quanto dura il cibo cotto in frigo, piatto per piatto` | 53 |
| `<meta name="description">` y `og:description` | `Riso, pasta, sugo, verdura, carne, pesce e frittata: quanti giorni durano in frigo secondo ISS ed EFSA, dove le fonti non danno un numero e cosa fare allora.` | 157 |
| `og:title` | `Quanto dura il cibo cotto in frigo, piatto per piatto` | 53 |
| `og:locale` | `it_IT` | — |
| JSON-LD `headline` | `Quanto dura il cibo cotto in frigo: piatto per piatto, secondo le fonti ufficiali` | 81 |
| JSON-LD `inLanguage` | `it-IT` | — |
| JSON-LD `BreadcrumbList` | FreshTrack › Guide › Cibo cotto in frigo | — |
| `citation` (URL) | `https://www.iss.it/en/-/gli-avanzi-delle-feste-dieci-suggerimenti-per-conservarli-in-sicurezza-riducendo-gli-sprechi` · `https://www.efsa.europa.eu/it/safe2eat/proper-food-handling` · `https://www.salute.gov.it/new/it/news-e-media/notizie/etichette-e-igiene-ecco-le-regole-la-sicurezza-alimentare/` · `https://www.crea.gov.it/documents/59764/0/lineeguida_10.pdf/7a499afb-5b1c-a2a7-cd66-d75f096f02e4?t=1551862640500` · `https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker` · `https://www.gov.uk/government/publications/cooking-your-food/cooking-your-food` | — |
| `hreflang` | `it` → esta; `es` → `/guias/cuanto-dura-comida-cocinada-nevera.html`; `en` → `/en/guides/how-long-leftovers-last.html`; `x-default` → la inglesa | — |
| Fechas | `datePublished` / `dateModified`: la del día que el dueño apruebe publicar. Fuentes consultadas: 3 novembre 2026 | — |

Los recuentos son de `len()` de Python sobre la cadena exacta.

## A.2 Texto de la página

> **Migas:** FreshTrack › Guide › Cibo cotto in frigo
> **Kicker:** Guida

# Quanto dura il cibo cotto in frigo: piatto per piatto, secondo le fonti ufficiali

**Lead:** Riso, pasta, sugo, verdura, carne, pesce e frittata: cosa dicono l'Istituto Superiore di Sanità e l'EFSA, dove non danno un numero e quanti giorni propone FreshTrack NFC in ogni caso.

**Byline:** Pubblicata il [data] da SOFTAPP SOLUTIONS LLC · Aggiornata il [data] · Fonti consultate il 3 novembre 2026

**Indice «In questa guida»:**
1. La risposta breve (`#breve`)
2. Piatto per piatto (`#tabella`)
3. Il caso del riso (`#riso`)
4. Le domande più frequenti (`#domande`)
5. Perché le fonti non coincidono (`#perche`)
6. Da quando si contano i giorni (`#conto`)
7. La regola delle due ore e come raffreddare in fretta (`#due-ore`)
8. Quando congelare e quanto dura in freezer (`#freezer`)
9. Perché l'odore non basta (`#odore`)
10. A mano, o con FreshTrack NFC (`#freshtrack`)

---

## La risposta breve  `#breve`

Il cibo cotto si tiene in frigo **al massimo 2-3 giorni**. È il limite dell'Istituto Superiore di Sanità (ISS) per gli avanzi: «idealmente, non dovrebbero essere conservati per più di 2-3 giorni».

Né l'EFSA né il Ministero della Salute danno un numero di giorni. L'EFSA dice solo di non conservare il cibo cotto «per troppo tempo, anche in frigorifero». Nessuna delle fonti ufficiali che abbiamo letto dà un limite diverso per la pasta, per il sugo o per la minestra: per quasi tutto vale la regola generale.

L'eccezione è il riso. L'ente britannico per la sicurezza alimentare (FSA) indica **24 ore**; le fonti italiane non dicono niente di specifico, e ne parliamo più sotto.

ISS, EFSA e CREA concordano su due cose: il cibo cotto va in frigo **entro due ore** e il frigo deve essere freddo (sotto i 5 °C per l'EFSA; intorno ai 4-5 °C per il CREA). Se sai che non riuscirai a mangiarlo in tempo, **congelalo subito**, non l'ultimo giorno.

## Piatto per piatto  `#tabella`

FreshTrack NFC ha già pronti dieci tipi di cibo cotto (più due crudi, carne e pesce, che non sono l'oggetto di questa guida). Per ognuno: cosa dicono le fonti ufficiali e quanti giorni propone l'app di base.

**Tabella** (`caption`: «Giorni in frigo del cibo cotto secondo le fonti ufficiali e valori predefiniti di FreshTrack NFC; fonti consultate il 3 novembre 2026»)

| Piatto | Frigo secondo le fonti ufficiali | Freezer secondo le fonti ufficiali | FreshTrack NFC di base (frigo / freezer) |
|---|---|---|---|
| Riso cotto | **24 ore** (FSA, Regno Unito); ISS: 2-3 giorni come regola generale | nessuna cifra | 2 giorni / 90 giorni |
| Pasta cotta | 2-3 giorni† | nessuna cifra | 3 giorni / 60 giorni |
| Legumi / stufato | 2-3 giorni† | nessuna cifra | 3 giorni / 90 giorni |
| Zuppa / crema (minestra, passato) | 2-3 giorni† | nessuna cifra | 3 giorni / 90 giorni |
| Carne cotta | 2-3 giorni† | nessuna cifra | 3 giorni / 90 giorni |
| Pesce cotto | 2-3 giorni† | nessuna cifra | 2 giorni / 60 giorni |
| Verdura cotta | 2-3 giorni† | nessuna cifra | 3 giorni / 60 giorni |
| Frittata / uovo | 2-3 giorni† | nessuna cifra | 2 giorni / 30 giorni |
| Sugo e salse fatte in casa | 2-3 giorni† (l'ISS segnala le salse e le creme come preparazioni «particolarmente deperibili») | nessuna cifra | 4 giorni / 90 giorni |
| Dessert fatto in casa | 2-3 giorni† (creme comprese: «particolarmente deperibili») | nessuna cifra | 3 giorni / 30 giorni |

**Note sotto la tabella (`p.fine`):**
Fonti: ISS, [Gli avanzi delle Feste, dieci suggerimenti per conservarli in sicurezza riducendo gli sprechi](https://www.iss.it/en/-/gli-avanzi-delle-feste-dieci-suggerimenti-per-conservarli-in-sicurezza-riducendo-gli-sprechi) (19 dicembre 2025, modificata il 16 febbraio 2026); FSA, [Home food fact checker](https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker) (in inglese). Giorni di FreshTrack NFC: valori predefiniti dell'app.

**† Per questo piatto non c'è una cifra propria.** In quelle caselle abbiamo messo la regola generale degli avanzi dell'ISS («idealmente non più di 2-3 giorni»). Non abbiamo riempito nessuna casella con un numero che le fonti non danno. Nemmeno sul freezer: l'ISS, l'EFSA e il Ministero non pubblicano, almeno nelle pagine che abbiamo letto, una tabella di mesi per i piatti cotti. L'FDA statunitense sì ([tabella in inglese](https://www.fda.gov/media/74435/download)); la citiamo come riferimento straniero, non come regola italiana.

Tre cose per leggere la tabella:
- **Le cifre di FreshTrack NFC non sono ufficiali.** Sono valori di partenza dell'app, e puoi cambiarli (vedi più sotto). Quelli del freezer, in particolare, sono suoi: nessuna fonte italiana li dà.
- **Sugo, salse e creme sono il punto debole.** L'ISS dice di tenere «ben refrigerate» le preparazioni avanzate, con particolare attenzione a creme e salse. Il valore di base dell'app per il sugo, 4 giorni, è **più** di quanto indica l'ISS (2-3). Lo diciamo perché lo sappiate: se preferisci stare nella regola dell'ISS, abbassalo a 2 o 3.
- **Riso e frittata:** 2 giorni, dentro il limite dell'ISS. Ma per il riso la FSA è più severa, e te lo spieghiamo adesso.

Qualunque colonna segua, **conta i giorni dal momento in cui hai cucinato** e scrivilo sul coperchio. Se vuoi tenere il conto di tutto quello che hai in freezer, non solo di ogni contenitore, serve un'altra guida, che per ora abbiamo solo in [spagnolo](../../guias/inventario-congelador.html) e in [inglese](../../en/guides/freezer-inventory.html). ⚑1

## Il caso del riso  `#riso`

Nessuna delle fonti italiane o europee che abbiamo letto parla del riso cotto. L'ISS, l'EFSA e il Ministero non lo nominano (il CREA lo cita solo crudo, in dispensa). Per questo ricorriamo alla FSA britannica, che invece è chiarissima: «il riso si può mangiare freddo se si raffredda in fretta; mettilo in frigo e consumalo entro 24 ore». ⚑2

Il motivo, secondo la FSA: il riso crudo può contenere spore di *Bacillus cereus*, e **le spore sopravvivono alla cottura**. Più a lungo il riso cotto resta a temperatura ambiente, più è probabile che il batterio o le sue tossine lo rendano non sicuro. E la FSA precisa: **non è il riscaldamento a causare il problema, ma il modo in cui il riso è stato conservato prima.**

Qui non c'è un numero italiano da contrapporre. Se devi scegliere, scegli la prudenza: 24 ore. Quello che vale comunque:

1. **Raffreddalo il prima possibile**, idealmente entro un'ora (FSA).
2. **Dividilo in porzioni piccole**: si raffredda prima. Lo stesso consiglio lo danno il CREA e l'ISS per tutti gli avanzi.
3. **Non lasciarlo nella pentola, nella vaporiera o nel cuociriso** a raffreddarsi.
4. **Riscaldalo una volta sola**, finché non è fumante anche all'interno.

E l'insalata di riso? Nessuna fonte ufficiale dà un numero. Contiene riso: ricordati del caso del riso.

## Le domande più frequenti  `#domande`

Risposte brevi, con la fonte. Quando le fonti ufficiali non danno un numero, lo diciamo.

### Quanto dura la pasta cotta in frigo?
Nessuna fonte ufficiale dà un numero solo per la pasta. Vale la regola generale dell'ISS: 2-3 giorni. Condita o in bianco, in contenitore chiuso. Se è al forno (lasagne, pasticci) vale lo stesso: è un piatto cotto.

### Quanto dura il sugo in frigo?
Nessuna fonte ufficiale dà un numero per il sugo di pomodoro. L'ISS include salse e creme tra le preparazioni «particolarmente deperibili» da tenere ben refrigerate. Regola generale: 2-3 giorni. Non è lo stesso del sugo in barattolo: una volta aperto, vale quello che dice l'etichetta del produttore.

### Quanto dura la verdura cotta in frigo?
Nessuna fonte ufficiale dà un numero per la verdura cotta. Regola generale dell'ISS: 2-3 giorni. Vale anche per la verdura cotta al vapore.

### Quanto dura il pollo cotto in frigo? E il pesce?
Nessuna fonte ufficiale che abbiamo letto distingue tra carne, pollo e pesce una volta cotti: per tutti, idealmente non più di 2-3 giorni.

### Quanto dura la minestra o il minestrone in frigo?
Stessa regola: 2-3 giorni. Quando la riscaldi, l'EFSA dice di usare un termometro per portare minestre e stufati a 70 °C e di riscaldare bene le pietanze; il CREA, di farle diventare «molto calde anche all'interno».

### Quanto dura la frittata, e l'uovo sodo?
Nessuna fonte ufficiale italiana dà un numero per la frittata o per l'uovo sodo. Vale la regola generale: 2-3 giorni.

### E il cibo cotto sottovuoto?
Qui non ti possiamo dare un numero: nelle fonti ufficiali italiane che abbiamo letto non c'è una regola per il cibo cotto in casa e messo sottovuoto. Se invece è un prodotto confezionato e integro, vale la durata scritta dal produttore sulla confezione (lo dice il CREA), e una volta aperto, qualche giorno.

### Quanto può stare fuori dal frigo?
Al massimo **due ore** (ISS, EFSA, CREA). Il CREA aggiunge: **un'ora** in estate. Dopo, non vale la pena rischiare.

### E il cibo cotto scongelato?
Scongela in frigo, dove la temperatura è più sicura (EFSA, ISS, CREA); non a temperatura ambiente. Le fonti italiane che abbiamo letto non indicano per quanto tempo si può tenere dopo lo scongelamento, e un numero che non abbiamo non te lo diamo.

## Perché le fonti non coincidono  `#perche`

In realtà quasi coincidono: il limite generale è 2-3 giorni nell'ISS, e nell'EFSA e nel Ministero della Salute non c'è un numero. Ciò che cambia è il riso, dove la FSA scende a 24 ore, e la FSA in generale: per gli avanzi dà 48 ore.

Nessuna delle fonti spiega, nelle pagine per i consumatori che abbiamo letto, perché ha scelto proprio quei numeri, e non ne inventiamo una ragione.

**E FreshTrack NFC, dove si colloca?** Non sempre dalla parte prudente, ed è giusto saperlo:
- **Riso cotto: 2 giorni.** La FSA dice 24 ore. L'app dà il doppio.
- **Pasta, legumi, zuppa, carne, verdura, dolci: 3 giorni.** È il limite alto dell'ISS (2-3 giorni). Per la FSA sarebbero 48 ore.
- **Sugo e salse: 4 giorni.** Oltre il limite dell'ISS. È il valore che consigliamo di abbassare.
- **Pesce cotto e frittata: 2 giorni.** Il limite basso dell'ISS.

Se preferisci essere più prudente, si cambia: **Impostazioni → Tempi di scadenza**, tocchi il tipo (per esempio «Riso cotto») e abbassi «Frigo» a 1 giorno. Il frigo ammette da 1 a 30 giorni e il freezer da 1 a 365. ⚑3 La modifica vale per i contenitori che riempirai dopo; quelli già pieni mantengono la loro data.

## Da quando si contano i giorni  `#conto`

Né l'ISS né le altre fonti definiscono un «giorno uno» più preciso di «avanzi». La lettura prudente, e quella che usiamo, è contare **dal giorno in cui hai cucinato**, non dal giorno in cui apri il contenitore.

- **Riscaldare non azzera il conto.** Né l'ISS né il CREA dicono che lo azzeri; dicono di riscaldare solo la porzione che mangerai e di non farlo più di una volta: ripetere i cambi di temperatura aumenta il rischio.
- **In FreshTrack NFC il giorno uno è il giorno in cui riempi il contenitore nell'app.** Se cucini la domenica e lo registri il lunedì, l'app ti dà un giorno in più. Registralo quando lo metti via.
- **Se lo sposti dal frigo al freezer**, l'app ricalcola la data con la regola del tipo di cibo, **contata dal giorno in cui hai riempito il contenitore**, non da quello in cui l'hai congelato. Uno stufato registrato il lunedì e congelato il mercoledì scade 90 giorni dopo il lunedì.

## La regola delle due ore e come raffreddare in fretta  `#due-ore`

- **Due ore al massimo** tra la cottura e il frigo o il freezer (ISS, EFSA, CREA). In estate, **un'ora** (CREA).
- **Porzioni piccole, e non il cibo bollente ancora nella pentola.** Il CREA consiglia di metterlo in frigo appena si è intiepidito, in porzioni piccole, perché si raffreddi in fretta fino al centro. L'ISS: travasalo in recipienti puliti e chiusi, non lasciarlo nella pentola.
- **Chiuso, e sui ripiani alti.** L'ISS: le preparazioni già cotte vanno sui ripiani alti, separate dagli alimenti crudi, e non vanno messe più preparazioni diverse nello stesso contenitore. Il Ministero: crudi, cotti e pronti da mangiare, separati e in contenitori chiusi.
- **Frigo sotto i 5 °C** (EFSA), intorno ai 4-5 °C (CREA). Controllalo con un termometro.

## Quando congelare e quanto dura in freezer  `#freezer`

**Congela quando decidi di farlo, non quando manca un giorno.** L'ISS: gli avanzi vanno in frigo *o in congelatore* entro poche ore dalla cottura.

- **Contenitori adatti al freezer, in porzioni piccole**, da consumare in una volta sola (ISS).
- **Il freezer a -18 °C blocca la crescita dei batteri, ma non li elimina** (CREA), e i prodotti surgelati «non sono eterni». Scrivi la data sul contenitore e non far toccare quelli già congelati con quelli nuovi.
- **Scongela in frigo** (EFSA, ISS). Se non puoi, il CREA ammette il microonde; mai a temperatura ambiente.
- **Quanti mesi?** Le fonti italiane che abbiamo letto non danno mesi per i piatti cotti. I valori di FreshTrack NFC (30, 60 o 90 giorni secondo il tipo) sono di partenza dell'app e li puoi cambiare. Se vuoi un riferimento esterno, l'FDA statunitense ha una [tabella in inglese](https://www.fda.gov/media/74435/download).

## Perché l'odore non basta  `#odore`

«Ha un buon odore, lo mangio?». Qui le fonti dicono due cose, e vanno tenute insieme.

L'ISS elenca i segni di deterioramento da non mangiare: muffa, odori acidi o rancidi, colore alterato, consistenza diversa. Il CREA aggiunge che un cattivo odore o un sapore rancido sono segno sicuro di non salubrità. Ma **il contrario non vale**: sempre per il CREA, gli alimenti contaminati possono mantenere colore, odore e sapore di sempre, e «un bell'aspetto non è una garanzia di cibo sano».

Gli avanzi non hanno una data stampata: la data sei tu. Se non ricordi quando li hai cucinati, **nel dubbio, buttali.**

## A mano, o con FreshTrack NFC  `#freshtrack`

**CTA, frase in grassetto:** Si può fare tutto a mano, con la tabella qui sopra, un pennarello e un pezzo di nastro adesivo.

Scrivi sul coperchio il giorno in cui hai cucinato e guarda la tabella quando serve. Se preferisci non scrivere a mano, un'[etichetta NFC sul coperchio](etichette-nfc-contenitori.html) fa lo stesso senza inchiostro.

Noi abbiamo fatto FreshTrack NFC perché non volevamo rifare il conto ogni domenica. Quando riempi un contenitore scegli che cos'è (i tipi della tabella) e se va in frigo o in freezer; l'app calcola la data con quei giorni, ti dice quando scade e ti avvisa una volta al giorno: di base, due giorni prima e alle 9:00. I giorni e l'ora si cambiano in Impostazioni, quindi se per il riso preferisci il limite della FSA, lo lasci a 1 giorno. È gratuita, senza pubblicità, senza acquisti e senza account, ed è nostra. ⚑4

**[Insignia App Store `it-black.svg` / `it-white.svg`, `alt`: «Scarica dall'App Store»]** → enlace de la guía 1 (§0.1)

**Descargo (`p.fine`, dentro del `.cta`):** Le date calcolate da FreshTrack NFC sono stime indicative basate su standard generali di conservazione degli alimenti (linee guida di tipo FoodKeeper dell'USDA e raccomandazioni di sicurezza alimentare). Non sostituiscono la data di scadenza o il termine minimo di conservazione stampati sulla confezione, né il tuo giudizio su aspetto, odore o sapore dell'alimento. Nel dubbio, non consumarlo.

*(Es la traducción del descargo de la guía ES, que está publicado así. Ojo: ahí dice «guías tipo FoodKeeper del USDA»; el descargo hay que mantenerlo igual que el de la ficha de la tienda. `appstore-qa` o `legal-privacy` deciden si en la web italiana se cambia por las fuentes que citamos aquí; yo no lo he tocado.)*

---

**Pie:** [Leggi questa guida in spagnolo](../../guias/cuanto-dura-comida-cocinada-nevera.html) · [Read this guide in English](../../en/guides/how-long-leftovers-last.html)

**Ficha para `it/guide/index.html`** (tarjeta, como las de `guias/index.html`):
- `h2`: Quanto dura il cibo cotto in frigo, piatto per piatto
- `p.q`: Mangio questo contenitore o lo butto?
- `p.fact`: Avanzi: idealmente non più di 2-3 giorni secondo l'ISS; il riso, 24 ore secondo la FSA britannica.

## A.3 Frases que conviene que revise un nativo (guía 1)

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «serve un'altra guida, che per ora abbiamo solo in spagnolo e in inglese» | Registro y naturalidad al enviar al lector a otro idioma; alternativa: omitir el enlace hasta que exista la guía italiana del congelador |
| ⚑2 | «il riso si può mangiare freddo se si raffredda in fretta; mettilo in frigo e consumalo entro 24 ore» | Es traducción de una cita de la FSA (inglés). Comprobar que no suena a traducción y que «cuociriso» (más abajo) se usa en lugar de «pentola per il riso» |
| ⚑3 | «Il frigo ammette da 1 a 30 giorni e il freezer da 1 a 365» | Léxico: «ammette»; alternativa «puoi impostare da 1 a 30 giorni» |
| ⚑4 | «ed è nostra» | Traducción literal de «es nuestra». En italiano suena raro; alternativa: «e l'abbiamo fatta noi» |

Además, para una revisión rápida: «cuociriso» (en la lista de recipientes), «nastro adesivo» (cinta), «pennarello» (rotulador), «contenitore» (tupper: no se usa «tupper» en italiano) y «Frigo / Freezer» frente a «frigorifero / congelatore» (he usado las formas coloquiales en el cuerpo, que son las de las consultas, y «congelatore» solo en frases de las fuentes).

---

---

# GUÍA 2 · Etichette NFC per contenitori del cibo e del congelatore

## B.1 Ficha técnica (para el `<head>` y el JSON-LD)

| Campo | Texto | Caracteres |
|---|---|---|
| Ruta propuesta | `it/guide/etichette-nfc-contenitori.html` | — |
| `<title>` | `Etichette NFC per contenitori del cibo e del congelatore — FreshTrack NFC` | 73 |
| `<title>` alternativo (sin marca) | `Etichette NFC per contenitori del cibo e del congelatore` | 56 |
| `<meta name="description">` y `og:description` | `Quale etichetta NFC programmabile comprare (NTAG213 o NTAG215), dove applicarla, come scriverla con l'iPhone e se resiste al freezer. Guida senza link di acquisto.` | 163 |
| `<meta name="description">` alternativa | `Quale etichetta NFC comprare (NTAG213 o NTAG215), dove applicarla, come scriverla con l'iPhone e se resiste al freezer. Senza link di acquisto.` | 143 |
| `og:title` | `Etichette NFC per contenitori del cibo e del congelatore` | 56 |
| JSON-LD `headline` | `Etichette NFC per contenitori del cibo e del congelatore: guida completa` | 72 |
| `inLanguage` / `og:locale` | `it-IT` / `it_IT` | — |
| `BreadcrumbList` | FreshTrack › Guide › Etichette NFC per contenitori | — |
| `citation` (URL) | `https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading` · `https://support.apple.com/it-it/guide/iphone/aside/asd-nfc-reader/15.0/ios` · `https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf` | — |
| `hreflang` | `it` → esta; `es` → `/guias/etiquetas-nfc-tuppers.html`; `en` → `/en/guides/nfc-labels-food-containers.html`; `x-default` → la inglesa | — |
| Enlaces a la tienda | ver §0.1, `ct=web-it-guia-nfc` | — |

**Elección entre las dos descripciones:** la primera (163) pasa de los ~155-160 caracteres que Google suele mostrar completos; recomiendo la alternativa de 143. Ambas contadas en VERIFICADO CON.

## B.2 Texto de la página

> **Migas:** FreshTrack › Guide › Etichette NFC per contenitori
> **Kicker:** Guida

# Etichette NFC per contenitori del cibo e del congelatore: guida completa

**Lead:** Quale etichetta NFC comprare, dove applicarla, come scriverla e leggerla con l'iPhone e se regge davvero il freezer. Si può fare tutto senza installare niente.

**Byline:** Pubblicata il [data] da SOFTAPP SOLUTIONS LLC · Aggiornata il [data]

**Indice «In questa guida»:**
1. Il blocco opaco di tre settimane (`#problema`)
2. Come si risolve oggi (`#oggi`)
3. Cos'è un'etichetta NFC (`#cose`)
4. Quale etichetta comprare: NTAG213 o NTAG215 (`#comprare`)
5. Dove applicarla (`#applicarla`)
6. Come scrivere un tag NFC con l'iPhone (`#scrivere`)
7. Leggerla senza aprire nessuna app (`#senza-app`)
8. Regge il freezer? (`#freezer`)
9. Quanto dura il cibo congelato (`#durata`)
10. A mano, o con FreshTrack NFC (`#freshtrack`)

---

## Il blocco opaco di tre settimane  `#problema`

Domenica congeli sei contenitori. Tre settimane dopo apri il freezer e trovi sei blocchi di plastica bianca che potrebbero essere lenticchie, potrebbero essere ragù o potrebbero essere lì dall'estate scorsa. Non c'è una foto, il pennarello si è sbavato con la brina e aprire ogni contenitore per controllare interrompe la catena del freddo di tutti gli altri. È un problema piccolo, ma si ripete ogni settimana. ⚑1

Questa guida parla dell'etichetta di ogni contenitore. Se invece vuoi tenere il conto del freezer intero, c'è la guida all'[inventario del congelatore](../../guias/inventario-congelador.html) (per ora solo in spagnolo; in [inglese](../../en/guides/freezer-inventory.html)).

## Come si risolve oggi, e cosa non funziona in ogni caso  `#oggi`

Prima di arrivare all'NFC, conviene essere onesti su quello che esiste già. Nessuna di queste tre soluzioni è sbagliata; ognuna cede in un punto diverso. Se cerchi «etichette per congelatore», le trovi soprattutto così.

**Cards:**

1. **Pennarello e nastro adesivo di carta**
   Gratis, ce l'hai già nel cassetto, non devi comprare niente.
   **Cede:** il nastro si stacca con l'umidità del freezer e il pennarello si sbava o si cancella quando scongeli. Bisogna riscrivere ogni volta.
2. **Etichetta adesiva di carta**
   Si legge meglio del pennarello e si può scrivere o stampare con più ordine.
   **Cede:** è monouso. Quando svuoti il contenitore bisogna staccarla (spesso lascia la colla) e attaccarne una nuova la volta dopo.
3. **Etichettatrice termica**
   Etichette leggibili e resistenti, senza scrivere a mano.
   **Cede:** devi comprare l'apparecchio e ricomprare i rotoli. Per due o tre contenitori a settimana è una spesa che non tutti vogliono fare.

## Cos'è un'etichetta NFC, e perché è diversa  `#cose`

Un'etichetta NFC (si chiama anche tag NFC, o adesivo NFC) è un adesivo sottile con dentro un chip minuscolo e un'antenna stampata, senza batteria e senza elettronica a vista. Dalla fabbrica non porta scritto niente: si scrive dal telefono, e poiché non è inchiostro né stampa, si può riscrivere migliaia di volte. Rispetto alle tre soluzioni qui sopra, la differenza non è che sia più bella: è che **non si consuma**. Svuoti il contenitore, lo lavi, e la volta dopo scrivi sopra la stessa etichetta senza staccare né attaccare niente.

In pratica, quando cerchi «etichette NFC programmabili» o «tag NFC adesivi» cerchi questo: adesivi con chip riscrivibili.

## Quale etichetta comprare: NTAG213 o NTAG215  `#comprare`

Quasi tutte le etichette NFC riscrivibili economiche che troverai montano un chip della famiglia NXP NTAG21x, quasi sempre NTAG213 o NTAG215. Sono compatibili con l'iPhone (dall'iPhone 7) senza nessun accessorio. La differenza vera tra i due, secondo la scheda tecnica del produttore, è la memoria disponibile: l'NTAG213 ha 144 byte di memoria utente e l'NTAG215 ne ha 504.

Per quello che ti serve qui (un testo breve, tipo «Lenticchie · Congelato 6 set»), bastano circa 30-40 byte: l'NTAG213 avanza e di solito costa meno. L'NTAG215 conviene solo se vuoi scrivere note lunghe (ingredienti, allergeni) o unire testo e collegamento.

Quanto alla resistenza, i due chip sono uguali: il produttore indica una conservazione dei dati di 10 anni e 100.000 cicli di riscrittura per entrambi. Riscrivendo un'etichetta a settimana, 100.000 volte bastano per secoli di contenitori. ⚑2

Quello che fa la differenza al momento dell'acquisto è l'adesivo, non il chip: cerca etichette indicate espressamente per frigorifero o congelatore, con uno strato protettivo (plastificato) sopra la parte stampata. Un adesivo di carta senza protezione si può inumidire e staccare; uno plastificato regge molto meglio.

*(`p.fine`)* In questa guida non ci sono link di acquisto, di proposito: non vogliamo che sia pubblicità, vogliamo che sia utile.

## Dove applicarla  `#applicarla`

- **Sul coperchio, non sul corpo del contenitore**, così la leggi senza aprirlo né toglierlo dalla pila del freezer.
- **In una zona piana e lontana dalle parti metalliche.** Il metallo blocca il campo dell'antenna e il telefono non riesce a leggere il chip. Se il coperchio ha una chiusura o un rinforzo metallico, applica l'etichetta nella parte di plastica più lontana.
- **Lontano da una cerniera o da una chiusura che si piega** ogni volta che apri il contenitore: l'antenna è una pista stampata molto sottile e la piega ripetuta può spezzarla.

## Come scrivere un tag NFC con l'iPhone  `#scrivere`

Funziona allo stesso modo con qualunque app NFC compatibile con NDEF che hai installato: non serve che sia FreshTrack NFC.

1. Apri l'app e cerca l'opzione per **scrivere** un'etichetta (a volte compare come «Write» o «Scrivi tag»).
2. Scegli un record di **testo** (o un **URL**, se preferisci rimandare a qualcosa invece di scrivere una nota).
3. Scrivi quello che vuoi ricordare: il contenuto e, se ti serve, la data o quando scade.
4. Avvicina la parte **alta del retro** dell'iPhone (dove c'è l'antenna NFC, vicino alla fotocamera) all'etichetta e tienilo fermo un paio di secondi, finché l'app non conferma la scrittura.
5. Per riusare il contenitore, ripeti il procedimento: scrivere sovrascrive il contenuto precedente, non devi cancellare niente prima.

*(`p.fine`)* Serve un iPhone 7 o successivo: è il minimo con cui Apple permette di leggere e scrivere etichette NFC dalle app di terze parti. L'iPad non legge né scrive etichette NFC.

*(Fuente de «l'iPad non…»: la descripción de la ficha italiana, «Leggere e scrivere le etichette NFC richiede un iPhone», lookup 03-11.)*

## Leggerla senza aprire nessuna app: la lettura in background  `#senza-app`

C'è una cosa che quasi nessuno sa e che cambia l'uso di tutti i giorni: dall'**iPhone XS** in poi, il sistema legge le etichette NFC **senza che tu apra niente**. Non serve che l'app sia aperta, e nemmeno in esecuzione. Avvicini il telefono all'etichetta, compare un avviso sullo schermo e, se lo tocchi, iOS apre l'app giusta e le consegna quello che c'era scritto. Apple la chiama *background tag reading*, e nella sua documentazione dice: «iPhone XS and later support background tag reading».

Nel manuale dell'iPhone, i modelli che ce l'hanno attiva di serie sono l'iPhone XR, l'XS, l'XS Max, l'SE (2ª generazione) e tutti i successivi. Apple non indica la versione di iOS in quella pagina; ciò che è datato è la parte dell'API che consegna all'app il contenuto di un'etichetta letta così, disponibile **da iOS 12.0**.

### Cosa serve perché compaia l'avviso

La condizione generale è che l'iPhone sia **in uso**, cioè con lo schermo acceso. Non serve che sia sbloccato perché l'avviso compaia: se è bloccato, il sistema chiede di sbloccarlo prima di passare i dati all'app. E anche con lo schermo acceso, Apple elenca cinque situazioni in cui la lettura in background **non** è disponibile:
- L'iPhone **non è mai stato sbloccato** da quando è stato acceso.
- C'è una **sessione di lettura NFC di un'app** in corso: se stai già scansionando da un'app, il sistema non interviene.
- È in uso **Wallet con Apple Pay**.
- È in uso la **fotocamera**.
- È attiva la **modalità aereo**.

### Cosa deve esserci scritto nell'etichetta

Qui c'è il dettaglio che cambia cosa conviene scrivere. Il sistema non guarda tutto il contenuto dell'etichetta: cerca nel messaggio NDEF un **record URI** (quello di tipo «U») e, se ce n'è più di uno, prende il primo. Quell'URI deve essere un **collegamento universale** di un'app o uno degli schemi che Apple ammette: indirizzi web https, mailto, sms, tel, FaceTime e FaceTime Audio, Mappe di Apple e configurazione degli accessori HomeKit. Gli schemi personalizzati di un'app non vanno bene.

> **`.box`: La conseguenza pratica per questa guida.** Un record di **testo** (quello consigliato qui sopra per scrivere «Lenticchie · Congelato 6 set») **non** fa comparire l'avviso. L'etichetta si legge benissimo, ma aprendo un'app NFC. Se vuoi avvicinare il telefono al contenitore e vederlo comparire da solo, l'etichetta deve contenere un **URL**, non una nota di testo.

Quando tocchi l'avviso succede una di due cose: se l'URL è un collegamento universale di un'app che hai installata, iOS apre quell'app (o la porta in primo piano) e le consegna il messaggio dell'etichetta; se nessuna app installata è associata a quel collegamento, lo apre in Safari.

### Dove non funziona

L'iPhone 7, il 7 Plus, l'8, l'8 Plus e l'iPhone X **non** hanno la lettura in background. Leggono e scrivono le etichette altrettanto bene, ma bisogna chiederlo: o da un'app, o attivando il **lettore di tag NFC** nel centro di controllo. Per questo uso preciso, è questa la differenza reale tra un iPhone del 2017 e uno dal 2018 in poi.

*(`p.fine`)* Fonti: Apple, [Adding Support for Background Tag Reading](https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading) (documentazione Core NFC, in inglese) e [Modelli compatibili con il lettore di tag NFC](https://support.apple.com/it-it/guide/iphone/aside/asd-nfc-reader/15.0/ios) (manuale dell'iPhone).

## Regge il freezer? Freddo e umidità  `#freezer`

Il chip, secondo le specifiche del produttore, funziona tra -25 °C e +70 °C: quindi regge i -18 °C di un freezer domestico. L'elettronica non è il problema. ⚑3

Quello che può cedere è l'adesivo e lo strato stampato, se l'etichetta non è pensata per questo: da qui il consiglio di comprarla già indicata per frigorifero o congelatore e con plastificazione protettiva. E l'altro punto critico non è il freddo ma la **condensa** quando tiri fuori il contenitore: un'etichetta plastificata sopporta bene quelle gocce in superficie senza che la lettura ne risenta; quello che può rovinarla col tempo è l'acqua che si infila sotto l'adesivo e lo stacca, quindi conviene asciugare il coperchio prima di rimetterlo in freezer se è rimasto molto umido.

## Quanto dura il cibo congelato  `#durata`

Questo non dipende dall'etichetta, ma è la domanda che viene subito dopo aver organizzato il freezer. Il CREA ricorda che il freezer a -18 °C non elimina i batteri ma ne blocca la crescita, e che i prodotti surgelati «non sono eterni». Quanto a mesi, le fonti ufficiali italiane che abbiamo letto non pubblicano una tabella per i piatti cotti. Cosa dicono ISS, EFSA e Ministero su frigo, due ore e riscaldamento è in [Quanto dura il cibo cotto in frigo, piatto per piatto](quanto-dura-cibo-cotto-in-frigo.html), con la sezione sul freezer. ⚑4

Per carne, pesce o pane **crudi**, e per tutto quello che compri e non cucini tu, i tempi sono altri: la guida ce l'abbiamo per ora solo in [spagnolo](../../guias/cuanto-dura-comida-congelador.html) e in [inglese](../../en/guides/how-long-food-lasts-in-freezer.html).

## A mano, o con FreshTrack NFC  `#freshtrack`

**CTA, frase in grassetto:** Si può fare tutto a mano con qualunque app NFC dell'App Store, come spiegato qui sopra.

Noi abbiamo fatto FreshTrack NFC perché non volevamo scrivere la data e calcolare la scadenza a mano ogni domenica. L'app scrive l'etichetta, calcola quanto dura secondo il tipo di cibo e dove lo conservi, e ti avvisa prima che scada. Scrive nell'etichetta un indirizzo web (un collegamento universale) e non un testo: per questo l'iPhone la riconosce da solo, senza aprire l'app, come abbiamo spiegato sopra. E se in casa qualcuno non ha l'app, avvicinando il telefono si apre una pagina che spiega cos'è l'etichetta. Per usare l'app non servono etichette: i contenitori si possono creare e modificare anche a mano, e l'etichetta aggiunge solo la possibilità di avvicinare l'iPhone per vedere cosa c'è dentro e quando scade. Funzionano le etichette riscrivibili NTAG213 e NTAG215. È gratuita, senza pubblicità, senza acquisti e senza account. ⚑5

**[Insignia App Store `it-black.svg` / `it-white.svg`, `alt`: «Scarica dall'App Store»]** → enlace de la guía 2 (§0.1)

---

**Pie:** [Leggi questa guida in spagnolo](../../guias/etiquetas-nfc-tuppers.html) · [Read this guide in English](../../en/guides/nfc-labels-food-containers.html)

**Ficha para `it/guide/index.html`:**
- `h2`: Etichette NFC per contenitori del cibo e del congelatore
- `p.q`: Quale etichetta compro, dove la applico, regge il freezer?
- `p.fact`: NTAG213 o NTAG215 (144 o 504 byte) e la lettura in background dell'iPhone, che parte da XS.

## B.3 Frases que conviene que revise un nativo (guía 2)

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «Domenica congeli sei contenitori… potrebbero essere lì dall'estate scorsa» | Adaptación libre de la apertura ES (lentejas / salsa de tomate). Registro coloquial de segunda persona; confirmar que «ragù», «blocchi di plastica bianca» y «sbavato con la brina» suenan naturales |
| ⚑2 | «100.000 cicli… bastano per secoli di contenitori» | Hipérbole humorística heredada de la guía ES; un nativo decide si se queda |
| ⚑3 | «funziona tra -25 °C e +70 °C: quindi regge i -18 °C» | Dato heredado de la guía ES y no reconfirmado (ver §C); un nativo revisa solo la frase |
| ⚑4 | «la guida ce l'abbiamo per ora solo in spagnolo e in inglese» | Mismo asunto que ⚑1 de la guía 1: se puede suprimir el enlace |
| ⚑5 | «Scrive nell'etichetta un indirizzo web (un collegamento universale)» | Términos: «collegamento universale» es el que usa Apple en italiano; confirmar |

Léxico para revisión rápida: «tag NFC / etichetta NFC / adesivo NFC» usados como sinónimos a propósito (las tres se buscan: «tag nfc adesivi», «etichette nfc programmabili»); «plastificato» (laminado); «nastro adesivo di carta» (cinta de carrocero); «lettura in background» (lo que Apple llama así en italiano: confirmar en iOS en italiano); «lettore di tag NFC» (nombre del control en el centro de control: confirmar con un iPhone en italiano; **no lo he podido comprobar**).

---

# C. Lo que he comprobado y lo que no (resumen para quien lea solo esto)

**Comprobado en directo el 03-11-2026** (`curl`/`WebFetch` con User-Agent de navegador genérico, sin ninguna cabecera con el correo del dueño):
- ISS, nota «Gli avanzi delle Feste…»: 2-3 días, 2 horas, congelar en raciones, signos de deterioro. 200.
- EFSA Safe2Eat «Pratiche corrette»: 2 horas, <5 °C, 70 °C, sin cifra de días. 200.
- Ministero della Salute, nota del 06-10-2022: sin cifra de días. 200.
- CREA/INRAN, cap. 10 (PDF, reimpresión 2007): 4-5 °C, 2 h / 1 h en verano, recalentar una vez, -18 °C. 200.
- FSA «Home food fact checker»: arroz 24 horas. 200.
- Apple Soporte en italiano (modelos con lector de etiquetas) y documentación de Core NFC: 200.
- Ficha de la tienda IT (lookup iTunes): nombre, gratis, sin anuncios/compras/cuenta, iPhone para NFC, iOS 17.
- Código de la app: 12 tipos de fábrica con sus días (`FreshTrack/Services/SeedData.swift:12-23`); aviso por defecto 2 días antes y a las 9:00 (`Views/Settings/SettingsView.swift:7-9`); rangos 1-30 y 1-365 (`Views/Settings/FoodTypeListView.swift:100-101`); la etiqueta lleva una URL web (`Services/EnlaceDeTupper.swift:9-11`); nombres de tipo y de menús en italiano de `Localizable.xcstrings`.

**Heredado de la guía ES publicada, sin releer el código:** que mover del frigo al congelador recalcula la fecha desde el día de relleno; que el cambio de días solo afecta a los contenedores nuevos; el descargo.
**No comprobado:** ficha técnica de NXP (144/504 bytes, 10 años, 100.000 ciclos, -25 a +70 °C): el PDF no se deja leer por `curl` ni `WebFetch`; los 144/504 bytes y los 10 años/100.000 ciclos los confirma una búsqueda dirigida a nxp.com; el rango de temperatura **no** lo he podido confirmar y es el que ya publicamos en ES y EN. Tampoco he comprobado en un iPhone en italiano cómo se llaman «lettore di tag NFC» y «lettura in background».
