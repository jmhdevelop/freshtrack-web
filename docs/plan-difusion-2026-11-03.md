---
# Documento interno: Jekyll no lo publica en la web (sin esto, GitHub Pages serviría el .md tal
# cual, igual que sirve README.md con 200).
published: false
---

# FreshTrack: plan de difusión para la web (enlaces, menciones y tráfico de referencia) · 2026-11-03

**Hecho por:** `growth-marketing`, en el Mac mini M4. **Alcance:** solo redacción. No se ha enviado,
publicado ni creado nada, y no se ha tocado ninguna página. Todo lo que lleva texto está listo para que
lo envíe o lo publique **el dueño**, y solo él.
**Entrada:** `docs/seo-estado-2026-11-03.md` (`seo-indexing`, hoy), `~/Projects/FreshTrack/docs/impresiones-store-2026-11-01.md`,
`~/Projects/FreshTrack/docs/aso-capturas-busqueda-2026-11-03.md`, `~/Projects/FreshTrack/docs/difusion-2026-09-16.md`
y `knowledge/seo.md` y `knowledge/marketing.md`.

---

## 0. Antes de leer: dos cosas que condicionan el plan

1. **La prensa sigue congelada por decisión tuya del 2026-09-16** (`FreshTrack/docs/difusion-2026-09-16.md`,
   «AVISO», punto 1: «No se vuelve a proponer un envío a prensa sin que el dueño lo reabra expresamente»).
   No he encontrado en `docs/` nada que lo reabra. Por eso **no propongo ningún correo a medios**, aunque
   es la fuente de enlaces con más autoridad que existe para este nicho (§6). Si quieres reabrirla, es
   una decisión tuya y va en «Para el dueño».
2. **Nada de publicidad de pago.** La app es gratis y sin compras: no hay coste por descarga que «salga
   a cuenta», y con unas 1,3 descargas al día una prueba pequeña no distingue señal de ruido. Las
   condiciones para reabrirlo siguen en `FreshTrack/docs/difusion-2026-09-16.md` §13.3. No lo justifico
   hoy porque no se cumplen.

---

## 1. Titular

**No llega gente a la web porque nadie de fuera la enlaza ni la nombra: 0 enlaces externos que cuenten
y 0 menciones de terceros (`seo-estado-2026-11-03.md` §4), y Google ya la enseña (261 impresiones en dos
meses, posición media 14,5) pero en la segunda página, donde casi no se hace clic (8 clics).** Y cuando
alguien busca la marca, «FreshTrack» le lleva a otros: 5 impresiones de «freshtrack», 3 de
«freshtrackcrm crm company», 3 de «freshtrak app», todas sin clic.

Esto no lo arregla tocar las páginas (la técnica está bien en las 28 URL). Lo arreglan **los primeros
enlaces de sitios del tema** y **contenido en el idioma de la tienda que ya descarga**.

---

## 2. Línea base (con fecha y fuente)

| Magnitud | Valor | Periodo | Fuente |
|---|---|---|---|
| Clics desde Google | **8** | 31-08 → 31-10-2026 | Search Console, propiedad `sc-domain:freshtrack.softapp.tech`, **leído por la sesión principal el 2026-11-03** |
| Impresiones en Google | **261** (CTR 3,1 %, posición media 14,5) | ídem | ídem |
| Consultas distintas | **16** | ídem | ídem |
| Consultas principales (clics/impresiones) | «rfid & nfc tags for food market» 0/15 · «cuanto aguanta la comida cocinada en la nevera» 0/11 · «freshtrack» 0/5 · «cuanto dura la verdura cocinada en la nevera» 0/4 · «freshtrak app» 0/3 · «nfc cosmetic bottle tags» 0/3 · «freshtrackcrm crm company» 0/3 · «freshrack» 0/2 · «mobile app» 1/1 | ídem | ídem |
| Enlaces externos que cuentan | **0** | a 2026-11-03 | `seo-estado-2026-11-03.md` §4 (HTML servido y búsqueda web). El informe «Enlaces» de Search Console **no se ha leído**: hay que mirarlo en la interfaz |
| Visitas a la web | **103** visitas, 121 páginas vistas | 30 días hasta el 03-11 | contador propio `b.js` (no guarda ni ruta ni referente) |
| Primeras descargas | **43** (≈1,3 al día) | 28-09 → 30-10 (32 días) | `impresiones-store-2026-11-01.md` §1 (Analytics Reports API) |
| … de ellas, por «Enlaces web» | **5** (11 vistas de ficha) | ídem | ídem |
| … por «Apps de referencia» | **21** (34 vistas); qué apps, lo suprime Apple | ídem | ídem |
| … por búsqueda en la tienda | **12** | ídem | ídem |
| Tienda que más descarga | **Italia, 15** (y la única cuya búsqueda acaba en visitas); Alemania, 10 | ídem | ídem §2 y §4 |
| Valoraciones | **0** en es, us, it, de, fr y br | 2026-11-03 | `itunes.apple.com/lookup?id=6791699550&country=…` (hoy, versión 1.3 del 01-11, ficha localizada en las seis tiendas) |
| Enlaces de la web a la tienda con `ct`/`pt` | **0** de 10 en la portada ES | 2026-11-03 | `grep` en `index.html` |

**Lectura de los números de Search Console:**

- **El contenido ya funciona a medias.** La guía de comida cocinada en español asoma en dos consultas de
  cola larga («cuanto aguanta…», «…la verdura cocinada…») a una posición media de ~15: indexada y
  relevante, pero en la segunda página. Es justo lo que pasa en un dominio sin autoridad: **un enlace
  externo de verdad mueve más esa página que otro retoque**.
- **La guía NFC en inglés atrae búsquedas de industria** («rfid & nfc tags for food market», «nfc cosmetic
  bottle tags»). Es gente del sector NFC, no quien busca una app para su nevera. Eso no trae descargas,
  pero dice algo útil: **para Google, la web ya es relevante en el tema NFC**, y los sitios del sector NFC
  son el sitio natural para el primer enlace (acción 1).
- **La marca a secas no se gana.** Las tres variantes con error de tecleo y la del CRM son gente buscando
  otro FreshTrack.

---

## 3. A quién le duele, y dónde está ya

- **Quien congela comida en tuppers y no sabe qué hay dentro ni desde cuándo.** El dolor exacto ya lo
  publicaron Directo al Paladar y El Español en feb-2025, resolviéndolo con hardware de pago
  (`knowledge/marketing.md`). Está en comunidades de cocina por tandas y de organización de casa
  (Reddit: inaccesible desde aquí, §5).
- **Quien ya compra pegatinas NFC y busca para qué usarlas en casa.** Está en las tiendas de etiquetas NFC
  y en sus guías («etichette nfc programmabili», «étiquette nfc iphone», «nfc tags examples» salen en el
  autocompletado de Google de hoy). Es el público más cercano al diferencial de FreshTrack y el que nadie
  más le habla.
- **En Italia y Alemania**, que son las tiendas que descargan (15 y 10 de 43). En la web no hay ni una guía
  en italiano ni en alemán.

---

## 4. Las tres acciones, por lo que traen dividido entre lo que cuestan

Antes de las tres, una condición previa de cinco minutos sin la cual ninguna se podrá medir bien.

### A0 · Condición previa: enlaces de campaña y un solo nombre fuera — **dueño 5 min + `seo-indexing`**

**Qué:** el `pt` (provider token) de la cuenta de App Store Connect. No se deduce ni se inventa: sale en
App Store Connect → Analytics → Acquisition → Campaigns → «+» (`FreshTrack/docs/promocion-app-store-herramientas-2026-10-06.md` §2.5).
Pendiente desde el 16-09.

Con él, cada enlace que se reparta en este plan lleva su campaña (máximo 30 caracteres):

| Acción | Enlace que se reparte |
|---|---|
| A1 Shop NFC | `https://apps.apple.com/it/app/id6791699550?pt=<pt>&ct=shopnfc-it&mt=8` |
| A1 Seritag | `https://apps.apple.com/app/id6791699550?pt=<pt>&ct=seritag-en&mt=8` |
| A2 Show HN | `https://apps.apple.com/app/id6791699550?pt=<pt>&ct=hn-show&mt=8` |
| Web (portadas y guías) | `ct` por página, lo pone `seo-indexing` (`web-es-guia-cocinada`, `web-it-portada`…) |

**El nombre de fuera, siempre igual: «FreshTrack NFC»**, enlazado, y con «de SOFTAPP» cuando haya sitio.
Va en todos los textos de este plan. Motivo: los otros FreshTrack ocupan la marca a secas (10 apps en la
tienda española, el B2B australiano en Google), y el texto del enlace que pone un tercero es lo que le
enseña a Google qué es «FreshTrack NFC». Más en §7.

**Si el `pt` no llega:** las acciones se hacen igual con el enlace desnudo. App Analytics ya separa por
dominio los toques desde Safari («Web Referrer»: `shopnfc.com`, `news.ycombinator.com`); lo que se pierde
es el desglose por enlace y lo que llega desde Chrome, que cae en «App Referrer».

---

### A1 · Pedir la mención a dos tiendas de etiquetas NFC que ya enlazan apps de iPhone — **la mejor relación**

**Dónde (verificado hoy):**

1. **Shop NFC** (`shopnfc.com`, Sinfotech.it S.r.l., Merate, Italia; versiones it, en, es, fr y de).
   Su página **«NFC e iPhone»** (`https://shopnfc.com/it/content/20-nfc-iphone`, 200) y la de
   «Come scrivere i tag NFC» (`/it/content/8-come-scrivere-i-tag-nfc`) **ya enlazan apps de terceros**:
   NFC Tools, Smart NFC, NFC TagWriter y NFC TagInfo de NXP. Esos enlaces salen con
   `rel="noreferrer noopener"`, **sin `nofollow`** (comprobado en el HTML de hoy). Venden NTAG213 y
   NTAG215 (`/it/30-ntag213`), que son las que recomienda nuestra guía.
   Contacto publicado en `https://shopnfc.com/it/contattaci`: **`info@shopnfc.com`** (y formulario).
2. **Seritag** (`seritag.com`, Reino Unido). Tiene una sección «Learn» con guías de uso
   (`/learn/using-nfc/…`: compartir wifi, contacto, ropa, iglesias) y `/learn/tech/how-to-encode-nfc-tags-with-an-iphone`.
   Contacto publicado en la portada: **`mail@seritag.com`**. **No he comprobado** que enlacen apps de
   terceros desde «Learn»: es la segunda opción por eso.

**Por qué esta y no otra:** es el único sitio que he encontrado que (a) tiene autoridad en el tema que
Google ya nos asocia (NFC), (b) **ya tiene la costumbre de enlazar apps de iPhone de terceros**, así que no
pedimos nada raro, (c) le interesa: un caso de uso doméstico vende pegatinas, y (d) es italiano, que es la
tienda que más descarga. No es prensa: es un correo a una empresa del sector. **No se ofrece nada a cambio**
(ni enlace recíproco ni dinero): pedir un intercambio de enlaces es justo lo que no se hace.

**Idioma:** italiano para Shop NFC (su sede y su versión principal), inglés para Seritag.
**Esfuerzo:** redactado (abajo). Al dueño, 10 minutos para enviar los dos. Un único recordatorio a los 10
días si no contestan; después, se da por perdido.
**Qué esperar:** lo más probable es que no contesten. Si uno dice que sí, es **el primer enlace externo que
cuenta** de la web, y en una página que leen justo los que compran pegatinas NFC. No prometo ni el sí ni
la posición.
**Cuándo:** Shop NFC el **martes 04-11**; Seritag el **miércoles 05-11**. Recordatorio único: 14-11 y 17-11.

#### Correo 1 · Shop NFC · para `info@shopnfc.com` · italiano

> **Revisión de idioma:** escrito por un agente, sin revisión de un nativo. Es corto y llano a propósito.
> Si el dueño tiene a alguien que lea italiano, mejor.

**Oggetto:** Un uso domestico per gli sticker NTAG213: i contenitori del congelatore

```
Buongiorno,

sono [NOME], sviluppatore indipendente (SOFTAPP SOLUTIONS LLC). Vi scrivo perché nella vostra
pagina «NFC e iPhone» (https://shopnfc.com/it/content/20-nfc-iphone) segnalate alcune app per
leggere e scrivere i tag con l'iPhone, e io ho sviluppato un'app che usa gli sticker NTAG213 e
NTAG215 per un caso d'uso domestico che lì ancora non c'è: i contenitori del frigo e del
congelatore.

L'app è mia e si chiama FreshTrack NFC (in App Store «FreshTrack: scadenze e NFC»). Si attacca
uno sticker NFC sul coperchio, l'app ci scrive cosa c'è dentro e quando scade, e avvicinando
l'iPhone si vede il contenuto senza aprire il contenitore, anche con l'app chiusa (lettura dei
tag in background). Quando il contenitore si svuota, il tag si riscrive con il cibo successivo.
È gratuita, senza pubblicità, senza acquisti in-app e senza account.

Vi chiedo solo se vi sembra utile citarla tra le app di quella pagina, o dove lo ritenete più
adatto. Non vi chiedo nulla in cambio e non c'è alcun accordo commerciale. Se vi servono
screenshot o un breve testo descrittivo, ve li mando.

App Store: https://apps.apple.com/it/app/id6791699550?pt=<pt>&ct=shopnfc-it&mt=8
Sito (in italiano): https://freshtrack.softapp.tech/it/

Grazie e buona giornata,
[NOME]
SOFTAPP SOLUTIONS LLC
```

Cada afirmación tiene fuente: NTAG213/215, lectura en segundo plano y reescritura, en la descripción
publicada de la ficha (lookup, 03-11) y en `guias/etiquetas-nfc-tuppers.html`; «gratis, sin anuncios, sin
compras y sin cuenta», en la descripción publicada.

#### Correo 2 · Seritag · para `mail@seritag.com` · inglés

**Subject:** A home use case for NTAG213 stickers: freezer containers + iPhone

```
Hello,

I'm [NAME], an independent developer (SOFTAPP SOLUTIONS LLC). I've been reading your Learn
section (https://seritag.com/learn/) and noticed the use-case guides: wifi, contact sharing,
garments. There's one I haven't seen covered that your customers might like: food containers.

I built an iPhone app for it, so to be clear up front, this is my own app. It's called
FreshTrack NFC. You stick an NTAG213 or NTAG215 sticker on a container lid, the app writes what's
inside and when it expires, and tapping the lid with an iPhone shows it without opening the box,
even with the app closed (background tag reading). When the container is empty, the tag is
rewritten. It's free, with no ads, no in-app purchases and no account.

If you ever write about NFC around the home, I'd be glad if you considered mentioning it. I'm not
asking for anything in return and there's no commercial arrangement. Happy to send screenshots
or answer technical questions about the tag format (an NDEF https URL record).

App Store: https://apps.apple.com/app/id6791699550?pt=<pt>&ct=seritag-en&mt=8
Guide: https://freshtrack.softapp.tech/en/guides/nfc-labels-food-containers.html

Thanks,
[NAME]
SOFTAPP SOLUTIONS LLC
```

«NDEF https URL record»: lo que se graba es `https://freshtrack.softapp.tech/t/#<id>`
(`FreshTrack/Services/EnlaceDeTupper.swift:9-11`); las etiquetas antiguas de la 1.1 y la 1.2 llevan el
esquema propio, pero el correo habla de lo que graba la app hoy.

---

### A2 · Show HN en Hacker News — **un solo tiro, 30 minutos y una tarde disponible**

**Dónde:** `https://news.ycombinator.com/submit`. **Normas leídas hoy** en `https://news.ycombinator.com/showhn.html`:

- Sí: «something you've made that other people can play with… things people can … hold in their hands».
  Una app gratis y sin registro encaja («ideally without barriers such as signups»).
- No: «blog posts, sign-up pages, newsletters, lists, and other reading material» y «Don't post
  landing pages». Por eso **el enlace es la ficha de la App Store, no la web ni una guía**.
- «Don't post quickly-generated one-offs» (no estaba en lo apuntado el 07-09 en `knowledge/marketing.md`).
  FreshTrack lleva dos meses y cuatro versiones publicadas: se cuenta cómo y por qué está hecha, que es lo
  que piden («Explain how and why»).
- Prohibido pedir votos o comentarios a conocidos («That's not ok on HN»).
- «Foo 1.3.1 is out» no vale como Show HN: **es la primera vez que se presenta**, así que sí vale. No
  repetir con la 1.4.

**Idioma:** inglés. **Esfuerzo:** redactado (abajo); al dueño, 5 minutos para publicarlo y **3-4 horas
disponible** para contestar comentarios ese día, porque es lo que decide si sube.
**Cuándo:** **martes 11-11-2026 entre las 14:00 y las 16:00 (hora peninsular)**, que son las 8-10 de la
mañana en la costa este de EE. UU. Si ese día no puede estar delante, otro martes o miércoles a la misma
hora; nunca un viernes ni un fin de semana.
**Qué esperar:** lo normal en un Show HN es pasar sin pena ni gloria (unos pocos votos). Si sube a la
página «show», trae un pico de visitas de un día y, a veces, que alguien lo recoja en un boletín o un blog,
que es donde están los enlaces de verdad. **No prometo nada.** El público es sobre todo técnico y en
inglés, y la ficha en-US es la que peor convierte desde la búsqueda (1 vista de 169 impresiones); pero quien
llega desde HN entra directo a la ficha, que es otro embudo.
**Requisito que solo sabe el dueño:** una cuenta de HN. No sé si tiene; si es nueva el mismo día, el
envío puede verse menos (no está en las normas; **sin comprobar**).

**Título** (78 caracteres, el máximo de HN es 80):

```
Show HN: FreshTrack NFC – tap a freezer box with an iPhone to see what's in it
```

**URL:** `https://apps.apple.com/app/id6791699550?pt=<pt>&ct=hn-show&mt=8`

**Primer comentario, que publica el dueño nada más enviar:**

```
Hi HN, I'm the developer. This is my own app and I'm a one-person studio.

The problem: I freeze leftovers in identical containers and three weeks later I have no idea
what's in them or since when. Markers smudge, paper labels fall off in the freezer.

What FreshTrack does about it: you stick a cheap rewritable NFC sticker (NTAG213/215) on the lid.
The app writes an https URL to the tag, and the container's ID goes in the URL fragment, so it
never reaches a server. Because it's a Universal Link, iOS reads it in the background (iPhone
XS and later, screen on): hold the phone to the lid, tap the notification and the container
card opens, with no app launched first. If someone
without the app taps it, they get a small web page instead of nothing. When the box is empty
you rewrite the tag with the next meal.

The rest is an expiry tracker for pantry, fridge and freezer: barcode lookup via Open Food Facts
(only the barcode number is sent), Apple Intelligence reading dates and allergens off the
package on-device (needs a compatible iPhone), Siri and Shortcuts ("what's expiring?"), and
iCloud sync. Free, no ads, no in-app purchases, no account; data stays on the device and in your
private iCloud. Reading and writing tags needs an iPhone; the iPad app works without NFC.

Built with SwiftUI, SwiftData + CloudKit and Core NFC. In English, Spanish, German, French,
Italian and Portuguese.

Things I'd genuinely like feedback on: is NFC worth the extra step over a marker for you? And
for those who've done background tag reading: any tag or lid material that gave you trouble?
```

Fuentes de cada afirmación: descripción publicada (lookup es/us, 03-11) para funciones, precio, cuenta y
privacidad; `FreshTrack/Services/EnlaceDeTupper.swift:9-11` para la URL con el id en el fragmento;
`~/Projects/freshtrack-web/t/index.html` (200) para la página de quien no tiene la app;
`FreshTrack/FreshTrackApp.swift` y `Models/AppSchema.swift` para SwiftData y CloudKit; seis idiomas, lookup de
las seis tiendas (03-11) y `Localizable.xcstrings` (de, en, es, fr, it, pt-BR).

---

### A3 · Dos guías en italiano, y después una en alemán — **lo único que compone solo**

**Responde a la pregunta del encargo: sí merecen la pena, pero no las cuatro lenguas a la vez, y en este
orden.** Las hacen `web-dev` (página) y la traducción/adaptación quien decida la sesión principal; aquí
decido qué y por qué.

| Orden | Idioma | Guía | Consulta (autocompletado de Google, 03-11) | Por qué |
|---|---|---|---|---|
| 1 | **it** | Adaptar `guias/cuanto-dura-comida-cocinada-nevera.html` → «Quanto dura il cibo cotto in frigo, piatto per piatto» | «quanto dura il cibo cotto in frigo» (y «…sottovuoto in frigo»); «quanto si conserva in frigo» con cola larga por plato (sugo, insalata di riso, uovo sodo) | **Es la única guía con prueba de que funciona**: la versión ES ya sale a posición ~15 en dos consultas (Search Console). Italia es la tienda que más descarga (15 de 43) y la única donde la búsqueda acaba en visitas |
| 2 | **it** | Adaptar `guias/etiquetas-nfc-tuppers.html` → «Etichette NFC per contenitori del congelatore» | «etichette nfc», «etichette nfc programmabili», «etichette adesive nfc» | Es el **destino natural del enlace de Shop NFC** (A1) y del diferencial de la app; la portada `it/` ya habla de «etichette NFC» (13 menciones) pero no hay guía |
| 3 | **de** | Adaptar la de comida cocinada → «Wie lange ist gekochtes Essen im Kühlschrank haltbar» | «wie lange ist gekochtes essen im kühlschrank haltbar» y su cola por plato: Hähnchen, Hackfleisch, Gemüse, Reis | Alemania es la segunda tienda (10 descargas). La cola larga por plato es la más rica de los cuatro idiomas que he mirado |
| — | fr | Esperar | «combien de temps se conserve le riz au frigo», «étiquette nfc iphone» | Francia da 4 descargas y su ficha convierte poco (1 vista de 70). Se reabre si las guías 1-3 dan impresiones en 8 semanas |
| — | pt-BR | Esperar | «quanto tempo dura comida no freezer sem luz» | Demanda real, pero es tema de seguridad alimentaria donde Google prefiere organismos públicos (`seo-estado` §7.5), y Brasil da 2 descargas |

**Condiciones para que no sea humo:**

- **Adaptar, no traducir.** Los plazos se citan con la **fuente oficial del país** (para Italia, el
  Ministero della Salute; para Alemania, el BfR o el BZfE), no con la de la guía española. **No he
  comprobado** qué publican ni si se leen desde aquí; es lo primero que tiene que mirar quien la escriba
  (`knowledge/seo.md`, «Fuentes oficiales de conservación…», cuenta qué fuentes fallan).
- Mismo nivel que las guías actuales (≈2.000 palabras, tabla por plato, `Article` + `BreadcrumbList`),
  `hreflang` recíproco con es y en, y entrada en el sitemap. Eso es de `seo-indexing`.
- Enlaces a la tienda con `ct` (`web-it-guia-cocinato`, `web-it-guia-nfc`, `web-de-guia-gekocht`).
- **Publicar la web es desplegar: necesita tu OK** cuando esté hecha.

**Esfuerzo:** unas horas de agente por guía (adaptación y fuentes) más la maquetación; nada del dueño
salvo aprobar la publicación. **Cuándo:** las dos italianas publicadas antes del **viernes 21-11**; la
alemana, antes del **viernes 05-12**. **Qué esperar:** nada en las primeras 2-4 semanas (indexación);
impresiones en cola larga hacia las 6-8 semanas si sigue el patrón de la guía española. Sin enlaces, no
pasará de la segunda página en las consultas cortas.

**Y en español, sin página nueva:** la consulta «cuanto dura la verdura cocinada en la nevera» (0/4) ya la
cubre una fila de la tabla de la guía. Si `seo-indexing` lo ve razonable, una sección corta sobre verdura
cocinada (y la congelación de la verdura) dentro de la misma guía es más barato que una guía nueva.
Decisión suya.

---

## 5. El resto del mapa, con fecha y con el motivo de no ir primero

| # | Acción | Dónde (verificado) | Idioma | Esfuerzo | Cuándo | Por qué no va entre las tres |
|---|---|---|---|---|---|---|
| R1 | **Comunidades de Reddit**: r/NFC (caso de uso), r/MealPrepSunday (comentar donde alguien pregunta cómo etiquetar), r/iOSapps (presentar) | **Normas sin leer**: Reddit sigue dando **403** desde aquí (`/r/MealPrepSunday/about/rules.json`, 03-11, como en septiembre) | en | 1 h de redacción cuando haya normas; 15 min del dueño por publicación | Cuando el chat de escritorio con «Control Chrome» pegue las normas (§9, `SIGUIENTE`) | **Sin las normas no se propone entrar**: muchos subreddits prohíben la autopromoción o la limitan a un día. Con normas, se redacta con la afiliación declarada en la primera línea |
| R2 | **Product Hunt**, lanzado por el dueño con su cuenta personal | `https://www.producthunt.com/launch/how-product-hunt-works` (leído hoy): lo lanza el propio creador; «do not pay anyone to hunt or send traffic»; si se pagan votos, «the product will be removed»; **no se admiten cuentas de empresa o marca** | en | 2 h de preparación (textos, galería) + el día del lanzamiento del dueño | Después de la 1.4 (~12-11) y de las capturas nuevas (`aso-capturas-busqueda-2026-11-03.md`), no antes del 24-11 | Es un pico de un día que se gasta una vez: mejor con la galería nueva. No he comprobado si el enlace de la ficha de PH es `nofollow`: se cuenta como tráfico, no como autoridad |
| R3 | **Foro de Open Food Facts**, categoría «Introducing yourself» (presentarse como app que usa su base de datos) | `forum.openfoodfacts.org` (Discourse, 200). Normas (`/guidelines`): «Don't post spam»; no prohíben presentar una app. **Precedente**: «Hello from Italy: Catch, an iPhone grocery app built on Open Food Facts» (06-10-2026), bien recibido por un moderador | en | 20 min | Cuando `product-manager` confirme cómo atribuye la app los datos de OFF | Alcance mínimo: ese hilo tiene **39 vistas** en un mes. Y antes hay que confirmar la atribución ODbL: hoy la app solo enseña la fuente en el pie de alérgenos (`LabelInfoSections.swift:263-270`); un hilo en su foro invita a que lo miren |
| R4 | **AlternativeTo**, añadir la ficha y nada más | `alternativeto.net/faq` (leído el 07-09): el desarrollador puede añadirla; prohibido usar el perfil para promocionarse; cola de «at least a few months» | en | 10 min del dueño | Cualquier día con un rato | Tarda meses en salir; los 5 $ de revisión prioritaria **no** están autorizados |

---

## 6. Lo que descarto, y por qué

- **Correos a prensa (es, it, de, fr, br).** Congelados por el dueño desde el 16-09 (§0). Es la fuente de
  enlaces con más autoridad del nicho (Directo al Paladar trató el problema exacto en feb-2025), y los
  textos de entonces existen (`FreshTrack/docs/difusion-2026-09-16.md` §3 A2, §6), pero habría que
  actualizarlos a la 1.3: no se reescriben sin que lo reabra.
- **Pelear por la marca «FreshTrack» a secas.** Diez apps en la tienda española, el B2B australiano en el
  autocompletado y, en Search Console, 13 impresiones de variantes de marca sin un clic. Se gana
  «FreshTrack NFC» (§7), no «FreshTrack».
- **Directorios genéricos de apps y «envía tu app» masivos.** Sin autoridad propia y, a menudo, de pago
  encubierto (Applicantes cobra, `knowledge/marketing.md`). Una granja de directorios no es un enlace.
- **Hacker News con la guía o la web.** Las normas excluyen expresamente la lectura y las landing pages.
- **Intercambiar enlaces con las tiendas NFC.** En A1 no se ofrece nada a cambio a propósito.
- **Guías en francés y portugués ahora.** Pocas descargas en esas tiendas y, en pt-BR, un tema que se
  llevan los organismos públicos (§4, A3). Se reabren con datos.
- **Responder en hilos de Reddit o foros sin normas leídas.** Es mandar al dueño a que le baneen.
- **Publicidad de pago** (§0).

---

## 7. «FreshTrack NFC» frente a la marca ocupada

Lo que hay: Google y la tienda ya tienen «FreshTrack» repartido entre al menos 10 productos; nuestra ficha
sale primera buscando «freshtrack» en el App Store de España (`seo-estado` §6), pero en Google la marca
lleva al CRM y al B2B. Ninguna consulta de Search Console contiene «nfc» junto a la marca: **la combinación
está libre y nadie la busca todavía**. Se construye así, por orden de coste:

1. **Fuera (esto lo controla este plan):** en todo texto que vaya a un tercero, el nombre es
   «FreshTrack NFC» y el enlace lleva ese texto. Hecho en A1 y A2. Lo mismo en la bio o el perfil del
   dueño donde se presente (HN, Product Hunt).
2. **En la web (`seo-indexing` y `web-dev`, decisión suya):** propongo que las portadas empiecen el título
   por «FreshTrack NFC» (hoy terminan en «— FreshTrack») y que el JSON-LD `MobileApplication` y `WebSite`
   lleven `alternateName: "FreshTrack NFC"` (hoy no lo lleva ninguna portada, `grep` del 03-11). No lo
   toco: es `<head>` y es suyo.
3. **En la tienda (`aso-copywriter` y `product-manager`):** el nombre de la ficha ya dice «… y NFC»
   («scadenze e NFC», «MHD & NFC»), salvo la en-US («FreshTrack: Expiry Tracker»). Si deciden algo, es
   decisión suya: aquí solo dejo el dato de que la marca en inglés es la que más se confunde.
4. **Lo que no se hace:** cambiar de nombre. Sería otra conversación (de producto), no de difusión.

**Cómo se sabe si funciona:** que aparezca en Search Console una consulta con «freshtrack nfc» o
«freshtrack» + «nfc»/«tupper»/«scadenze» con clics. Hoy, 0.

---

## 8. Cómo se mide cada acción y cuándo se revisa

Línea base: §2. Todas las revisiones las hace `data-analyst` (App Store) y la sesión principal o
`seo-indexing` (Search Console, en la interfaz mientras el panel no tenga token de Google).

| Acción | Señal | Fuente | Revisión |
|---|---|---|---|
| A0 | Que existan campañas `ct` con datos (aunque estén bajo el umbral de 5) | ASC → Analytics → Campaigns | 21-11 |
| A1 | Respuesta (sí/no/nada) · página de Shop NFC o Seritag con nuestro enlace (`curl` de la página y `grep id6791699550` o `freshtrack.softapp.tech`) · visitas por «Web Referrer» de `shopnfc.com`/`seritag.com` · campaña `shopnfc-it`/`seritag-en` · Search Console → Enlaces: sitios externos > 0 | correo del dueño, `curl`, Analytics Reports API, Search Console | 14-11 (respuesta), 01-12 y 05-01-2027 (enlace y efecto) |
| A2 | Puntos y comentarios del hilo · si llega a la página «show» · descargas del día y de los 3 siguientes frente a ≈1,3/día · campaña `hn-show` · «Web Referrer» `news.ycombinator.com` · menciones que salgan después (búsqueda web de «FreshTrack NFC») | `news.ycombinator.com/item?id=…`, Analytics Reports API, búsqueda web | 12-11 (al día siguiente) y 26-11 (menciones) |
| A3 | Indexación de las URL nuevas · impresiones y consultas en it/de · posición media de esas páginas | Search Console (Páginas, Rendimiento filtrado por página) | 4 semanas tras publicar (indexación) y 8 semanas (impresiones): 19-12 y 16-01-2027 para las italianas |
| Marca | Consultas con «freshtrack nfc» o marca + calificador | Search Console | 05-01-2027 |

**Punto de parada escrito antes de empezar:** si a **05-01-2027** Search Console → Enlaces sigue con 0
sitios externos y A1 no ha dado ni una respuesta, el canal «tiendas NFC» se apunta como descartado en
`knowledge/marketing.md` con esos datos, y la siguiente apuesta de enlaces pasa a ser la prensa, si el dueño
la reabre.

**Agujero de medición que no tapo yo:** el contador `b.js` no guarda referente, así que una visita que llega
desde Shop NFC a la web (y no a la tienda) no se ve como tal. Decidir si se guarda el dominio de origen es
de privacidad y del panel (`legal-privacy` y `data-analyst`), no de marketing; aquí solo dejo que el
agujero existe.

---

## 9. Quién hace qué

**Lo prepara un agente (y ya está hecho o le toca a otro):**

| Qué | Quién | Estado |
|---|---|---|
| Correos A1 y post y comentario A2 | `growth-marketing` | Redactados en este documento |
| Leer las normas de r/NFC, r/MealPrepSunday y r/iOSapps (barra lateral «Rules» y wiki) y Search Console → Enlaces | chat de escritorio con «Control Chrome» (lo encarga la sesión principal) | Pendiente. Con las normas, `growth-marketing` redacta R1 |
| `ct` en los enlaces de la web; título y `alternateName` «FreshTrack NFC»; sección de verdura cocinada | `seo-indexing` (+ `web-dev` si hace falta maquetar) | Pendiente del `pt` (el `ct`) y de su criterio (lo demás) |
| Guías it (cocinato, NFC) y de (gekocht), con fuentes oficiales del país | `web-dev` + adaptación; `seo-indexing` para `hreflang` y sitemap | Pendiente |
| Atribución de Open Food Facts en la app (antes de R3) | `product-manager` | Pendiente |
| Revisiones de §8 | `data-analyst`, sesión principal | Fechas en §8 |

**Solo lo puede hacer el dueño:**

1. Sacar el `pt` de App Store Connect (5 min).
2. Enviar los correos de A1 desde su correo (martes 04-11 y miércoles 05-11) y, si no hay respuesta, un
   único recordatorio.
3. Publicar el Show HN con su cuenta de HN y estar 3-4 horas para contestar (martes 11-11).
4. Aprobar la publicación de las guías nuevas (es desplegar).
5. Decidir si reabre la prensa.
6. Más adelante: Product Hunt y AlternativeTo con su cuenta personal.

---

## 10. Lo que no he podido comprobar

- **Search Console → Enlaces**: no tiene API y no lo he visto. El 0 de §2 es lo que se ve desde fuera.
- **Normas de Reddit**: 403 desde aquí (03-11).
- **Si Seritag enlaza apps de terceros** desde «Learn» (sí lo he comprobado en Shop NFC).
- **Si el enlace de HN o de Product Hunt es `nofollow`**, y si una cuenta de HN nueva ve limitados sus Show HN.
- **Las fuentes oficiales italianas y alemanas** de conservación de alimentos que necesitan las guías de A3.
- **El italiano del correo 1** no lo ha revisado un nativo.
