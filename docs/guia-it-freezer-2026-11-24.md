---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía IT · Quanto dura il cibo cotto in freezer (B4 de la tanda) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. Se publicará sin revisión nativa:
frases de riesgo con ⚑ (§4).

**Lo primero, porque condiciona toda la guía:** como ya vio la guía italiana del 03-11, **ninguna fuente
oficial italiana que haya podido leer da meses de congelador para el cocinado.** Hoy he vuelto a buscar: la
prensa atribuye al Ministero della Salute «uno-due mesi» para los cocinados, pero **no he encontrado esa página
del Ministero** (ni en salute.gov.it ni en el dosier regional «Sicurezza alimentare nel frigorifero di casa», que
la reproduce y no da meses). No se usa. La guía lo dice abiertamente, da lo que sí dicen ISS, CREA y Ministero
(cómo congelar, descongelar, etiquetar, por qué no es eterno), y da como **referencias extranjeras declaradas**
la FRC suiza (2-3 meses para «piatti precotti, avanzi») y la FDA estadounidense (tabla por plato, «for quality
only»). Si el dueño prefiere no publicar una guía cuya respuesta principal es extranjera, es la que menos
pierde quedándose en borrador; pero la consulta tiene demanda y la honestidad es justo el ángulo.

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `it/guide/quanto-dura-cibo-cotto-in-freezer.html` |
| `hreflang` | Sin equivalente exacto: las guías `guias/cuanto-dura-comida-congelador.html` y `en/guides/how-long-food-lasts-in-freezer.html` tratan todo el congelador, no solo lo cocinado. Propongo **no** emparejarlas por `hreflang` (decisión de `seo-indexing`) y enlazarlas en el texto |
| Enlace a la tienda | `https://apps.apple.com/it/app/id6791699550?pt=126402967&ct=web-it-guia-freezer&mt=8` |
| `<title>` (65) | `Quanto dura il cibo cotto in freezer? Ragù, brodo, carne e avanzi` |
| `meta description` (155) | `Quanti mesi in freezer per ragù, brodo, carne cotta e avanzi: cosa dicono ISS e CREA, dove le fonti italiane non danno un numero e quali riferimenti usare.` |
| `og:title` | `Quanto dura il cibo cotto in freezer?` |
| JSON-LD | `Article` (`it-IT`, `citation` §1.1) + `BreadcrumbList` (FreshTrack › Guide › Cibo cotto in freezer) |
| Descargo (`p.fine` del CTA) | Literal de la app en italiano (`the-dates-freshtrack-calculates-are-approximate-estimates`): «Le date calcolate da FreshTrack sono stime orientative basate su standard generali di conservazione degli alimenti (linee guida come il FoodKeeper dell'USDA e raccomandazioni di sicurezza alimentare). Non sostituiscono la data di scadenza o il termine minimo di conservazione stampati sulla confezione, né il tuo giudizio sull'aspetto, l'odore o il sapore dell'alimento. In caso di dubbio, non consumarlo.» |
| Enlaces internos | Desde `it/guide/quanto-dura-cibo-cotto-in-frigo.html` (§«Quando congelare e quanto dura in freezer») hacia esta |
| Ficha para `it/guide/index.html` | `h2`: Quanto dura il cibo cotto in freezer? · `p.q`: Quel ragù congelato a settembre, lo mangio ancora? · `p.fact`: Le fonti italiane non danno mesi; la FRC svizzera indica 2-3 mesi per avanzi e piatti precotti. |

### 1.1 Fuentes, leídas hoy (2026-11-24)

| # | Fuente | Qué da |
|---|---|---|
| I1 | **ISS**, «Gli avanzi delle Feste, dieci suggerimenti…» — `https://www.iss.it/en/-/gli-avanzi-delle-feste-dieci-suggerimenti-per-conservarli-in-sicurezza-riducendo-gli-sprechi` | «Riponi gli avanzi in frigo o in congelatore entro poche ore dalla cottura»; no más de dos horas fuera; en el frigorífico «idealmente… non più di 2-3 giorni»; para congelar, «contenitori adatti al freezer» y «porzioni piccole da consumare in un'unica volta»; calentar solo la porción; señales de deterioro |
| I2 | **CREA**, «Linee guida per una sana alimentazione», cap. 10 (PDF, reimpresión 2007) — `https://www.crea.gov.it/documents/59764/0/lineeguida_10.pdf/7a499afb-5b1c-a2a7-cd66-d75f096f02e4?t=1551862640500` | Congelador a −18 °C (tres o cuatro estrellas) «non effettua un'azione di bonifica», bloquea el crecimiento; «i prodotti surgelati non sono eterni»; en casa, «piccole confezioni, scrivendoci sopra la data»; que no toquen lo ya congelado; compartimentos de −12 °C a pocos grados bajo cero no son congeladores: de 3 días (hielo) a un mes (dos estrellas); descongelar cocinando, en el frigorífico, en el microondas o en agua fría corriente si está bien cerrado, no a temperatura ambiente; recalentar una vez; lo comprado más reciente detrás o debajo. **Es de 2007**: se cita solo para reglas que no cambian |
| I3 | **Ministero della Salute**, dosier «Sicurezza alimentare nel frigorifero di casa» reproducido por la Regione Valle d'Aosta (PDF de 2014; el servidor de la región da 503 hoy, leído en la Wayback Machine, copia del 26-09-2014) — `https://www.regione.vda.it/allegato.aspx?pk=39581` | Congelador «a circa -18°C»; congelar en piezas pequeñas, en recipientes limpios «con l'etichetta che riporta il nome del cibo contenuto e la data di congelamento»; enfriar antes de congelar; descongelar en el frigorífico; lo descongelado no se recongela; el congelador no mata los microorganismos. **Fuente débil** (regional, 2014, vía archivo): solo para lo que repiten ISS o CREA |
| X1 | **FRC** (Suiza), «Fiche 6 · La congélation» (PDF, 2020) — `https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf` | Según el laboratorio cantonal de Zúrich: «plats précuisinés, restes (rôti ou sauce bolognaise) 2-3 mois»; verduras 6-12; carne picada cruda 1-3; pan 4-6… |
| X2 | **FDA** (EE. UU.), «Refrigerator & Freezer Storage Chart» (PDF) — `https://www.fda.gov/media/74435/download` | «freezing 0 °F (-18 °C) keeps food safe indefinitely, the following recommended storage times are for quality only»; sopas y guisos 2-3 meses; platos de carne cocinada 2-3; ave cocinada 4-6; pescado cocinado 4-6; huevo duro: «Don't freeze» |

**Autocompletado (24-11, `hl=it&gl=it`):** «quanto dura il cibo cotto in freezer»; «quanto dura in freezer la carne
cotta / il ragù / il brodo di carne / il pesto fatto in casa / la pasta fresca»; «quanto dura il cibo in freezer
senza corrente / dopo la scadenza / sottovuoto».

---

## 2. TEXTO DE LA PÁGINA (italiano)

> **Briciole:** FreshTrack › Guide › Cibo cotto in freezer · **Kicker:** Guida

# Quanto dura il cibo cotto in freezer? Ragù, brodo, carne e avanzi, e perché le fonti italiane non danno un numero

**Lead:** Cosa dicono l'Istituto Superiore di Sanità e il CREA su come congelare gli avanzi, perché nessuna delle fonti ufficiali italiane che abbiamo letto indica quanti mesi, e quali riferimenti stranieri usare per decidere.

**Byline:** Pubblicata il [data] da SOFTAPP SOLUTIONS LLC · Fonti consultate il 24 novembre 2026

**Indice:** 1. La risposta breve (`#breve`) · 2. Piatto per piatto (`#tabella`) · 3. Perché in freezer non è eterno, ma nemmeno pericoloso (`#qualita`) · 4. Come congelare gli avanzi (`#congelare`) · 5. Scrivere la data (`#data`) · 6. Come scongelare (`#scongelare`) · 7. A mano o con FreshTrack NFC (`#freshtrack`) · 8. Le domande più frequenti (`#domande`)

## La risposta breve  `#breve`

**Nessuna delle fonti ufficiali italiane che abbiamo letto indica per quanti mesi si conserva il cibo cotto in freezer.** L'ISS dice di mettere gli avanzi «in frigo o in congelatore entro poche ore dalla cottura», in porzioni piccole e in contenitori adatti al freezer; il CREA ricorda che il congelatore a −18 °C blocca la crescita dei microrganismi ma che i prodotti congelati «non sono eterni». Di mesi, però, non parlano.

I riferimenti che abbiamo trovato vengono dall'estero, e li indichiamo come tali:
- la Fédération romande des consommateurs (Svizzera), su dati del laboratorio cantonale di Zurigo: **2-3 mesi** per «piatti precotti e avanzi (arrosto o ragù alla bolognese)»;
- la FDA statunitense: **2-3 mesi** per zuppe, stufati e piatti di carne cotta, **4-6 mesi** per pollame e pesce cotti, e precisa che sono tempi «for quality only», cioè di qualità.

In pratica ⚑1: **2-3 mesi** per ragù, brodo, minestre, stufati e avanzi è un riferimento prudente. Oltre, il piatto peggiora di sapore e consistenza; non diventa per questo pericoloso, se il freezer è rimasto sempre a −18 °C.

## Piatto per piatto  `#tabella`

FreshTrack NFC ha già pronti dieci tipi di cibo cotto. Per ognuno: cosa dicono le fonti italiane, i riferimenti stranieri e quanti giorni propone l'app di base in freezer.

**Tabella** (`caption`: «Cibo cotto in freezer: fonti italiane, riferimenti stranieri e valori predefiniti di FreshTrack NFC; fonti consultate il 24 novembre 2026»)

| Piatto | Fonti ufficiali italiane | Riferimento straniero | FreshTrack NFC di base (freezer) |
|---|---|---|---|
| Ragù e sughi fatti in casa | nessuna cifra | 2-3 mesi (FRC, «sauce bolognaise») | 90 giorni |
| Brodo, minestra, zuppa | nessuna cifra | 2-3 mesi (FDA, zuppe e stufati) | 90 giorni |
| Legumi, stufato, spezzatino | nessuna cifra | 2-3 mesi (FDA, stufati) | 90 giorni |
| Carne cotta, arrosto | nessuna cifra | 2-3 mesi (FRC, «rôti»; FDA, piatti di carne cotta) | 90 giorni |
| Pollo cotto | nessuna cifra | 4-6 mesi (FDA) | 90 giorni (tipo «Carne cotta») |
| Pesce cotto | nessuna cifra | 4-6 mesi (FDA) | 60 giorni |
| Riso cotto | nessuna cifra | — | 90 giorni |
| Pasta cotta | nessuna cifra | — | 60 giorni |
| Verdura cotta | nessuna cifra | verdure 6-12 mesi (FRC; non distingue cotte e crude) | 60 giorni |
| Frittata / uovo | nessuna cifra | uovo sodo: «Don't freeze» (FDA) | 30 giorni |
| Dolce fatto in casa | nessuna cifra | torte 2-4 mesi (FRC) | 30 giorni |

*(`p.fine`)* Riferimenti stranieri: FRC, [Fiche 6 · La congélation](https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf) (in francese, 2020); FDA, [Refrigerator & Freezer Storage Chart](https://www.fda.gov/media/74435/download) (in inglese). Giorni di FreshTrack NFC: valori predefiniti dell'app, modificabili.

Tre cose per leggere la tabella:
- **La colonna italiana è vuota di proposito.** Non abbiamo messo numeri che le fonti italiane non danno.
- **I valori di FreshTrack NFC stanno dentro o sotto i riferimenti stranieri**: 90 giorni sono 3 mesi, il massimo di FRC e FDA per ragù, zuppe e carne. Per riso e pasta cotti non abbiamo trovato un riferimento specifico.
- **L'uovo sodo non va congelato** secondo la FDA (diventa gommoso); la frittata è un'altra cosa, ma nessuna fonte che abbiamo letto ne parla.

## Perché in freezer non è eterno, ma nemmeno pericoloso  `#qualita`

Il CREA lo dice con chiarezza: il congelatore «non effettua un'azione di bonifica, ma semplicemente blocca la crescita dei microrganismi, se la temperatura è mantenuta costante». Due conseguenze:
- **Finché resta a −18 °C, il problema non è la sicurezza ma la qualità.** La FDA lo scrive nella sua tabella: a −18 °C il cibo resta sicuro, e i tempi indicati sono «for quality only». Col tempo peggiorano sapore e consistenza.
- **Quando lo scongeli, i microrganismi ripartono da dove si erano fermati.** Per questo conta com'era il cibo quando l'hai congelato: l'ISS chiede di congelare gli avanzi «entro poche ore dalla cottura», non l'ultimo giorno in frigo.

**Attenzione allo scomparto del frigo.** Secondo il CREA, gli scomparti da −12 °C a pochi gradi sotto zero non sono congelatori: conservano i surgelati da 3 giorni (scomparto del ghiaccio) a un mese (due stelle). Per mesi serve un congelatore a tre o quattro stelle, a −18 °C.

## Come congelare gli avanzi  `#congelare`

- **Entro poche ore dalla cottura**, e mai più di due ore fuori dal frigo o dal congelatore (ISS).
- **Prima fallo raffreddare**, appena intiepidito e in porzioni piccole, perché si raffreddi in fretta fino al centro (CREA).
- **Contenitori adatti al freezer, in porzioni da consumare in una volta sola** (ISS). Così scongeli solo quello che mangi.
- **Che non tocchino ciò che è già congelato**, per non farlo scongelare in parte (CREA).

## Scrivere la data  `#data`

Il CREA: piccole confezioni, «scrivendoci sopra la data». Il dosier del Ministero della Salute aggiunge il nome del cibo: un'etichetta con il contenuto e la data di congelamento. Quello che le fonti non dicono e che a noi serve ⚑2:
- **Due date** se il piatto passa dal frigo al freezer: «cotto il 24/11 · congelato il 26/11».
- **Il contenuto per esteso**: «ragù di manzo, 2 porzioni», non «contenitore 3».
- **Il più recente dietro o sotto**, come consiglia il CREA per tutti gli alimenti in casa, così usi prima quello che è lì da più tempo.
- Sul coperchio, con nastro adesivo di carta e pennarello indelebile, oppure con un'[etichetta NFC](etichette-nfc-contenitori.html) riscrivibile.

## Come scongelare  `#scongelare`

Il metodo migliore, per il CREA, è **cuocerlo direttamente** (in acqua già bollente o in padella a fuoco alto). In alternativa, **in frigorifero** (la mattina per la sera o la sera per la mattina), nel microonde o, se la confezione è impermeabile, in acqua corrente fredda. **Mai a temperatura ambiente.** Una volta scongelato, il dosier del Ministero dice di non ricongelarlo; e il CREA sconsiglia di riscaldare un cibo più di una volta.

## A mano, o con FreshTrack NFC  `#freshtrack`

**CTA, frase in grassetto:** Si può fare tutto a mano: una data sul coperchio e la tabella qui sopra.

Noi abbiamo fatto FreshTrack NFC perché non volevamo più contare i mesi a memoria ⚑3. Quando riempi un contenitore scegli che cos'è (i tipi della tabella) e se va in frigo o in freezer; l'app calcola la data con quei giorni, contando dal giorno in cui lo riempi nell'app, ti dice quando scade e ti avvisa una volta al giorno: di base, due giorni prima e alle 9:00. Con un'etichetta NFC riscrivibile sul coperchio, avvicinando l'iPhone vedi cosa c'è dentro e quando scade, senza aprire il freezer a lungo. Nell'etichetta c'è solo un collegamento: il contenuto è nell'app. I giorni si cambiano in **Impostazioni → Tempi di scadenza** (freezer da 1 a 365 giorni); la modifica vale per i contenitori che riempirai dopo. Puoi anche chiedere a Siri cosa hai nel congelatore. È gratuita, senza pubblicità, senza acquisti e senza account. Leggere e scrivere le etichette NFC richiede un iPhone; l'app è per iPhone e iPad.

**[Insignia `it-black.svg`/`it-white.svg`, `alt` «Scarica dall'App Store»]** → enlace de §1 · **Descargo** (§1).

## Le domande più frequenti  `#domande`

### Quanto dura il cibo cotto in freezer?
Le fonti ufficiali italiane che abbiamo letto non danno un numero. Riferimenti stranieri: 2-3 mesi per avanzi e piatti precotti (FRC, Svizzera), 2-3 mesi per zuppe e stufati (FDA, Stati Uniti).

### Quanto dura il ragù in freezer?
Nessuna fonte italiana dà un numero. La FRC svizzera indica 2-3 mesi per la «sauce bolognaise» fatta in casa e congelata.

### Quanto dura il brodo di carne in freezer?
Nessuna fonte italiana dà un numero. La FDA indica 2-3 mesi per zuppe e stufati, come tempo di qualità.

### Quanto dura la carne cotta in freezer?
Riferimenti stranieri: 2-3 mesi per piatti di carne cotta (FDA) e per l'arrosto (FRC); 4-6 mesi per il pollo cotto (FDA).

### Il cibo congelato da più tempo è pericoloso?
Se il freezer è rimasto sempre a −18 °C, la FDA dice che resta sicuro e che i tempi indicati riguardano la qualità. Il CREA ricorda che il freddo blocca i microrganismi ma non li elimina: quando scongeli, ripartono.

### Si può ricongelare il cibo cotto scongelato?
No, secondo il dosier del Ministero della Salute. Scongela solo le porzioni che mangerai.

### Come si scongela il cibo cotto?
Cuocendolo direttamente, in frigorifero, nel microonde o in acqua fredda se ben chiuso. Mai a temperatura ambiente (CREA).

### Lo scomparto del frigo va bene per congelare?
No, se non è a −18 °C: secondo il CREA gli scomparti da −12 °C a pochi gradi sotto zero conservano i surgelati da 3 giorni a un mese.

---

**Pie:** Per il frigo: [Quanto dura il cibo cotto in frigo, piatto per piatto](quanto-dura-cibo-cotto-in-frigo.html). Per tutto il resto del freezer (carne, pesce e pane crudi): guida per ora in [spagnolo](../../guias/cuanto-dura-comida-congelador.html) e in [inglese](../../en/guides/how-long-food-lasts-in-freezer.html).

---

## 3. Resumen fiel en español (para el dueño)

**«¿Cuánto dura la comida cocinada en el congelador? Ragú, caldo, carne y sobras, y por qué las fuentes
italianas no dan una cifra».** Respuesta corta honesta: ninguna fuente oficial italiana leída da meses; el ISS
dice congelar las sobras en pocas horas, en raciones pequeñas y recipientes aptos; el CREA, que el congelador
bloquea pero no elimina los microbios y que lo congelado «no es eterno». Referencias extranjeras declaradas:
FRC suiza (2-3 meses para platos precocinados y sobras, «asado o boloñesa») y FDA (2-3 meses sopas, guisos y
carne cocinada; 4-6 ave y pescado cocinados; solo calidad). Tabla con los diez tipos de la app: columna italiana
vacía a propósito; los valores de la app (30-90 días) están dentro o por debajo de esas referencias; huevo duro,
no congelar (FDA). Por qué es calidad y no seguridad mientras esté a −18 °C; el compartimento del frigorífico
no es congelador (3 días a un mes según el CREA); cómo congelar, etiquetar (dos fechas, contenido, lo nuevo
detrás) y descongelar (cocinando, frigorífico, microondas o agua fría; nunca a temperatura ambiente; no
recongelar). FreshTrack NFC con las mismas afirmaciones que las otras guías («Impostazioni → Tempi di
scadenza»). 8 preguntas cortas. Se ha quitado la consulta «senza corrente» (cuánto aguanta sin luz) porque
no hay fuente italiana que la conteste.

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «In pratica: 2-3 mesi … è un riferimento prudente» | Criterio nuestro, no cita; que se lea así |
| ⚑2 | «Quello che le fonti non dicono e che a noi serve» | Registro |
| ⚑3 | «Noi abbiamo fatto FreshTrack NFC perché…» | En la guía italiana publicada se marcó «ed è nostra» como raro; aquí no se usa |
| — | «nastro adesivo di carta», «pennarello indelebile», «spezzatino» | Léxico |
