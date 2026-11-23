---
# Documento interno: Jekyll no lo publica en la web (sin esto, GitHub Pages serviría el .md tal
# cual, igual que sirve README.md con 200).
published: false
---

# Correo a Shop NFC, listo para enviar · 2026-11-23

**Hecho por:** `growth-marketing`. Actualiza `docs/plan-difusion-2026-11-03.md` §A1, que no se llegó a
enviar (lo confirmó el dueño el 23-11). **Lo envía el dueño desde su correo; ningún agente lo envía.**

- **Para:** `info@shopnfc.com` (comprobado el 23-11 en `https://shopnfc.com/it/contattaci`, 200).
- **Cuándo:** martes 25-11-2026.
- **Adjuntos:** ninguno. Un primer correo sin adjuntos pasa mejor los filtros; las capturas se ofrecen
  en el texto.
- **Idioma:** italiano (Shop NFC es Sinfotech.it S.r.l., Merate). **Sin revisar por un nativo**:
  frases cortas y llanas a propósito.
- **Antes de enviar:** cambiar `[NOME]` por su nombre. Si tiene el `pt`, añadir `&pt=<pt>` al enlace
  de la App Store (ver «Enlace» abajo).

---

**Oggetto:** Un uso domestico per gli NTAG213: i contenitori del congelatore

```
Buongiorno,

sono [NOME], sviluppatore indipendente (SOFTAPP SOLUTIONS LLC). Nella vostra
pagina «NFC e iPhone» (https://shopnfc.com/it/content/20-nfc-iphone) segnalate
alcune app per leggere e scrivere tag con l'iPhone. Vi scrivo perché ho
sviluppato un'app che usa gli sticker NTAG213 e NTAG215 per un uso domestico
che lì non c'è ancora: i contenitori del frigo e del congelatore.

L'app è mia e si chiama FreshTrack NFC (in App Store «FreshTrack: scadenze e
NFC»). Si attacca uno sticker sul coperchio, lo si scrive dall'app e si annota
cosa c'è dentro e quando scade. Dall'iPhone XS in poi basta avvicinare l'iPhone
al coperchio e toccare la notifica: si apre la scheda del contenitore, senza
aprire prima l'app. Quando il contenitore si svuota, il tag si riscrive per il
cibo successivo. È gratuita, senza pubblicità, senza acquisti in-app e senza
account.

Vi chiedo solo se vi sembra utile citarla in quella pagina, o dove lo ritenete
più adatto. Non chiedo nulla in cambio e non c'è alcun accordo commerciale. Se
vi servono screenshot o un breve testo, ve li mando volentieri.

App Store: https://apps.apple.com/it/app/id6791699550?ct=shopnfc&mt=8
Guida in italiano (quale etichetta usare, se regge il freezer):
https://freshtrack.softapp.tech/it/guide/etichette-nfc-contenitori.html

Grazie e buona giornata,
[NOME]
SOFTAPP SOLUTIONS LLC
```

### Traducción al español (solo para el dueño; no se envía)

> **Asunto:** Un uso doméstico para las NTAG213: los tuppers del congelador
>
> Buenos días:
>
> Soy [NOMBRE], desarrollador independiente (SOFTAPP SOLUTIONS LLC). En vuestra página «NFC e iPhone»
> recomendáis algunas apps para leer y escribir etiquetas con el iPhone. Os escribo porque he
> desarrollado una app que usa las pegatinas NTAG213 y NTAG215 para un uso doméstico que ahí todavía
> no aparece: los tuppers de la nevera y del congelador.
>
> La app es mía y se llama FreshTrack NFC (en la App Store, «FreshTrack: scadenze e NFC»). Se pega una
> pegatina en la tapa, se graba desde la app y se apunta qué hay dentro y cuándo caduca. Desde el
> iPhone XS basta con acercar el iPhone a la tapa y tocar la notificación: se abre la ficha del tupper
> sin abrir antes la app. Cuando el tupper se vacía, la etiqueta se vuelve a grabar para la siguiente
> comida. Es gratis, sin anuncios, sin compras dentro de la app y sin cuenta.
>
> Solo os pregunto si os parece útil citarla en esa página, o donde mejor os parezca. No pido nada a
> cambio y no hay ningún acuerdo comercial. Si necesitáis capturas o un texto breve, os los mando.
>
> [enlace a la App Store] · [guía en italiano: qué etiqueta usar y si aguanta el congelador]
>
> Gracias y buen día.

### De dónde sale cada afirmación

| Afirmación | Fuente (comprobada el 23-11) |
|---|---|
| Su página enlaza NFC Tools, NFC TagWriter y Smart NFC | `https://shopnfc.com/it/content/20-nfc-iphone` (200), enlaces a `apps.apple.com` |
| Nombre en la tienda italiana | `itunes.apple.com/lookup?id=6791699550&country=it` → `trackName` |
| Gratis, sin anuncios, sin compras, sin cuenta; etiqueta reescribible | Descripción publicada de la 1.3 (lookup it) |
| NTAG213 y NTAG215 | `/it/guide/etichette-nfc-contenitori.html` («Quale etichetta comprare: NTAG213 o NTAG215») |
| Desde el iPhone XS, acercar y tocar la notificación, sin abrir antes la app | Lectura en segundo plano por Universal Link: `FreshTrack/Services/EnlaceDeTupper.swift` en `testflight-1.3-37` (la 1.3 publicada); la guía italiana, sección «Leggerla senza aprire nessuna app» |

No se menciona la 1.4 a propósito: no está publicada.

### Enlace

`https://apps.apple.com/it/app/id6791699550?ct=shopnfc&mt=8` (200 el 23-11). **Sin `pt`:** App Store
Connect no atribuye la campaña `shopnfc` sin el token del proveedor, así que solo se verá la visita
como «Web Referrer» `shopnfc.com` si llega desde Safari (desde Chrome cae en «App Referrer»). El `pt`
se saca en App Store Connect → Analytics → Campaigns → «+» (generador de enlaces); no está en ningún
fichero de la casa (`knowledge/seo.md`).

### Cómo se mide, y cuándo se para

| Fecha | Qué se mira | Quién |
|---|---|---|
| 25-11 | Enviado (lo confirma el dueño) | dueño |
| 05-12 | ¿Respuesta? Si no hay, **un único** recordatorio corto ese día, en el mismo hilo | dueño |
| 19-12 | `curl -s https://shopnfc.com/it/content/20-nfc-iphone \| grep -c id6791699550` (hoy 0) y también la versión `/en/` | `growth-marketing` |
| 19-12 y 09-01-2027 | Visitas y descargas con «Web Referrer» `shopnfc.com` (y campaña `shopnfc` si hubo `pt`); Search Console → Enlaces | `data-analyst`, chat de escritorio |

**Punto de parada:** si el **09-01-2027** no hay respuesta ni enlace, el canal «tiendas de etiquetas
NFC» se apunta como descartado en `~/Projects/claude-agents/knowledge/marketing.md` con estos datos,
y no se escribe a otras tiendas NFC (Seritag, NFC21) por la misma vía.
