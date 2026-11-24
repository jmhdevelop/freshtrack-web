---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía FR · Étiquettes NFC pour boîtes (adaptación de la guía NFC) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. **Se publicará sin revisión nativa
por decisión del dueño**: las frases de más riesgo llevan ⚑ (§4). Es la **primera guía en francés**: crea la
carpeta `fr/guides/` (propuesta; en francés «guides» es la palabra normal y coincide con `en/guides/`).

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `fr/guides/etiquettes-nfc-boites.html` + `fr/guides/index.html` (ficha al final) |
| `hreflang` | `fr` → esta · `de` → `/de/ratgeber/nfc-etiketten-dosen.html` · `es` → `/guias/etiquetas-nfc-tuppers.html` · `en` → `/en/guides/nfc-labels-food-containers.html` · `it` → `/it/guide/etichette-nfc-contenitori.html` · `x-default` → la inglesa |
| Enlace a la tienda | `https://apps.apple.com/fr/app/id6791699550?pt=126402967&ct=web-fr-guide-nfc&mt=8` |
| `<title>` (67) | `Étiquette NFC pour boîtes : NTAG213 ou NTAG215, congélateur, iPhone` |
| `meta description` (158) | `Quelle étiquette NFC acheter pour tes boîtes, si elle tient au congélateur et au lave-vaisselle, et comment l'iPhone la lit sans ouvrir d'app. Sources citées.` |
| `og:title` | `Étiquettes NFC pour boîtes et congélateur` |
| JSON-LD | `Article` (`inLanguage: "fr-FR"`, `citation`: URL de §1.1) + `BreadcrumbList` (FreshTrack › Guides › Étiquettes NFC pour boîtes). Ni `FAQPage` ni `HowTo` |
| Enlaces internos | `fr/index.html:568`, `:752` (anclas) y el texto de la FAQ JSON-LD `:103`, que hoy van a la guía inglesa, deberían apuntar a esta. (`pt/index.html` sigue con la inglesa: no hay guía pt) |
| Ficha para `fr/guides/index.html` | `h2`: Étiquettes NFC pour boîtes · `p.q`: Quelle étiquette, où la coller, tient-elle au congélateur ? · `p.fact`: Une NTAG213 suffit (144 octets) ; dès l'iPhone XS, l'iPhone la lit en arrière-plan. |

### 1.1 Fuentes, comprobadas hoy (2026-11-24)

| # | Fuente | Qué da |
|---|---|---|
| A1 | Apple Developer, «Adding Support for Background Tag Reading» — `https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading` | XS y posteriores; iPhone «in use»; cinco casos sin lectura; primer registro URI; enlace universal → app, sin app → Safari; desbloqueo antes de pasar datos |
| A2 | Apple Assistance (FR), «Modèles prenant en charge le lecteur d'étiquette NFC» — `https://support.apple.com/fr-fr/guide/iphone/aside/asd-nfc-reader/15.0/ios` | Automático: SE (2e génération et modèles ultérieurs), XR, XS, XS Max, 11 y posteriores. «activez « Lecteur d'étiquette NFC » dans le Centre de contrôle» en 7, 7 Plus, 8, 8 Plus, X |
| A3 | NXP, ficha NTAG213/215/216 Rev. 3.2 (02-06-2015); la URL oficial da 404 hoy, leída en copia (`datasheet.chipsmall.com/NT2H1311TTDUDZ/368586.pdf`) | 144/504/888 octetos; 10 años y 100 000 ciclos **a 22 °C**; sin rango de temperatura en lo disponible |
| A4 | Ficha FR de la App Store (lookup 24-11, «FreshTrack: anti-gaspi & NFC», 1.3) | «Colle une étiquette NFC réinscriptible sur le couvercle…», «l'étiquette se réutilise», «Lire et écrire les étiquettes NFC nécessite un iPhone», «Gratuit, sans pub, sans achat intégré, sans créer de compte» |
| A5 | Código de la 1.3 (`testflight-1.3-37`) | Enlace `https://freshtrack.softapp.tech/t/#<id>`, id en el fragmento (`Services/EnlaceDeTupper.swift:8-11`); boîtes sin etiqueta posibles (`Models.swift:202`); `freshtrack.softapp.tech/t/` (200) tiene texto en francés para quien no tiene la app |

Igual que en la guía alemana: **sin dato de fabricante para −18 °C ni lavavajillas**, y el «−25/+70 °C» de las
guías ES/EN/IT publicadas **no está confirmado**. Cálculo propio: el enlace de FreshTrack ocupa ~71 octetos.

### 1.2 Consultas (autocompletado Google, `hl=fr&gl=fr`, 24-11)

«étiquette nfc iphone», «etiquette nfc iphone c'est quoi», «etiquette nfc detectee iphone», «lecteur étiquette
nfc iphone (c'est quoi)», «desactiver etiquette nfc iphone»; «étiquette nfc de site web», «…iphone», «…c'est
quoi», **«notification etiquette nfc de site web»**; «tag nfc iphone (notifica, xr, 11…17)»; «ntag213 ou
ntag215», «ntag213 ntag215 ou ntag216»; «autocollant nfc (c'est quoi)», «puce nfc iphone». La pregunta
«¿qué es esa notificación?» es la que más se repite y la guía la contesta en `#arriere-plan` y en la FAQ.

---

## 2. TEXTO DE LA PÁGINA (francés)

> **Fil d'Ariane :** FreshTrack › Guides › Étiquettes NFC pour boîtes · **Kicker :** Guide

# Étiquettes NFC pour boîtes et congélateur : laquelle acheter, où la coller, comment l'iPhone la lit

**Chapô :** Quelle étiquette NFC choisir (NTAG213 ou NTAG215), ce qu'elle supporte au congélateur et au lave-vaisselle, comment l'écrire avec l'iPhone, et pourquoi les iPhone récents la lisent sans ouvrir d'app. L'essentiel se fait sans notre app.

**Signature :** Publié le [date] par SOFTAPP SOLUTIONS LLC · Sources vérifiées le 24 novembre 2026

**Sommaire :** 1. En bref (`#bref`) · 2. Une étiquette NFC, c'est quoi ? (`#quoi`) · 3. NTAG213 ou NTAG215 ? (`#acheter`) · 4. Congélateur et lave-vaisselle (`#froid`) · 5. Où la coller (`#ou`) · 6. L'écrire avec l'iPhone (`#ecrire`) · 7. La lire sans ouvrir d'app (`#arriere-plan`) · 8. À la main ou avec FreshTrack NFC (`#freshtrack`) · 9. Questions fréquentes (`#questions`)

## En bref  `#bref`

- **Achète une étiquette réinscriptible NTAG213.** D'après la fiche technique du fabricant NXP, elle offre 144 octets de mémoire : assez pour un lien ou une note courte. La NTAG215 (504 octets) ne sert que pour des textes longs.
- **Dès l'iPhone XS, l'iPhone lit l'étiquette en arrière-plan** : tu l'approches du couvercle, une notification apparaît, tu la touches. Pour cela, l'étiquette doit contenir un **lien**, pas seulement du texte (Apple).
- **Pour le congélateur et le lave-vaisselle**, ni NXP ni Apple ne donnent d'indication pour les autocollants ordinaires. Ce qui tient dépend de l'autocollant, pas de la puce : regarde ce qu'annonce le vendeur.
- **L'iPad ne lit pas les étiquettes NFC** : Apple ne liste que des modèles d'iPhone.

## Une étiquette NFC, c'est quoi ?  `#quoi`

Une étiquette NFC (on dit aussi tag NFC, puce NFC ou autocollant NFC) est un autocollant fin qui contient une minuscule puce et une antenne imprimée, sans pile. Elle sort d'usine vierge : on l'écrit avec le téléphone, et on peut la réécrire. Pour les boîtes, c'est toute la différence avec le ruban de masquage ou l'étiquette papier : elle ne s'use pas. Boîte vide, lavée, et la fois suivante tu réécris la même étiquette, sans rien décoller ni recoller.

## NTAG213 ou NTAG215 ?  `#acheter`

La plupart des autocollants NFC bon marché utilisent une puce de la famille NTAG21x de NXP, presque toujours NTAG213 ou NTAG215. La vraie différence figure dans la fiche technique de NXP : **144 octets** de mémoire utilisateur pour la NTAG213, **504** pour la NTAG215 (888 pour la NTAG216).

De combien a-t-on besoin ? Exemple tiré de notre propre app : le lien que FreshTrack NFC écrit sur une étiquette occupe, selon notre calcul, environ **71 octets**. Une NTAG213 suffit largement, une note courte (« Lentilles · congelé le 6/9 ») aussi. La NTAG215 n'a d'intérêt que pour de longues notes.

Côté durée de vie, les deux puces sont identiques : NXP indique **10 ans** de conservation des données et **100 000 cycles d'écriture**, mesurés à 22 °C. À une réécriture par semaine, ce n'est pas la puce qui lâchera la première. ⚑1

Avec l'iPhone, les deux fonctionnent sans accessoire : Apple cite l'iPhone 7 et les modèles ultérieurs parmi ceux qui ont le lecteur d'étiquette NFC.

*(`p.fine`)* Ce guide ne contient volontairement aucun lien d'achat.

## Congélateur et lave-vaisselle : ce qu'on sait et ce qu'on ne sait pas  `#froid`

Pour être honnêtes : **nous n'avons trouvé aucune indication de fabricant pour −18 °C ni pour le lave-vaisselle concernant les autocollants NFC ordinaires.** Les valeurs de la fiche NXP (10 ans, 100 000 cycles) sont données à 22 °C, et la partie de la fiche que nous avons pu lire n'indique pas de plage de température de fonctionnement.

Ce que nous en déduisons ⚑2 :
- **Le point faible est l'autocollant plus que la puce.** La colle et la couche imprimée décident si l'étiquette tient au congélateur. Choisis des étiquettes que le vendeur annonce expressément pour le réfrigérateur ou le congélateur, idéalement avec une couche de protection (pelliculée).
- **Lave-vaisselle seulement si le vendeur l'indique.** Sinon, lave le couvercle à la main.
- **La condensation :** en sortant la boîte du congélateur, le couvercle se couvre de buée. Essuie-le avant de le remettre au froid, pour que l'eau ne passe pas sous la colle.

## Où la coller  `#ou`

- **Sur le couvercle**, pas sur le côté : tu la lis sans sortir la boîte de la pile.
- **Sur une zone plate, loin du métal.** Le métal perturbe le champ de l'antenne. Si le couvercle a une attache métallique, colle l'étiquette sur la partie en plastique la plus éloignée.
- **Pas sur une charnière ou un clip qui se plie.** L'antenne est une piste très fine ; la plier sans cesse peut la casser. ⚑2

## L'écrire avec l'iPhone  `#ecrire`

N'importe quelle app NFC de l'App Store capable d'écrire en NDEF fait l'affaire ; pas besoin que ce soit la nôtre.

1. Ouvre l'app et choisis « Écrire » (parfois « Write »).
2. Choisis un **lien (URL)** ou un **texte**. La section suivante explique pourquoi c'est important.
3. Approche le **haut du dos** de l'iPhone (près de l'appareil photo) de l'étiquette jusqu'à ce que l'app confirme l'écriture.
4. Pour réutiliser la boîte, écris à nouveau : cela remplace l'ancien contenu.

## La lire sans ouvrir d'app : la lecture en arrière-plan  `#arriere-plan`

Peu de gens le savent : **dès l'iPhone XS, l'iPhone lit seul les étiquettes NFC** (« iPhone XS and later support background tag reading », Apple). Aucune app n'a besoin d'être ouverte. Tu approches l'iPhone de l'étiquette, une notification apparaît en haut de l'écran, et si tu la touches, iOS ouvre l'app correspondante ou, s'il n'y en a pas, le lien dans Safari. Si l'iPhone est verrouillé, iOS demande d'abord de le déverrouiller avant de transmettre les données à l'app.

**C'est cette notification que beaucoup découvrent sans comprendre** ⚑3 : elle signifie simplement que l'iPhone vient de lire une étiquette NFC qui contient l'adresse d'un site web. Rien ne s'ouvre tant que tu ne la touches pas.

D'après Apple, c'est automatique sur l'iPhone XR, XS, XS Max, l'iPhone SE à partir de la 2e génération et tous les modèles depuis l'iPhone 11. Sur l'**iPhone 7, 7 Plus, 8, 8 Plus et X**, il faut activer le **« Lecteur d'étiquette NFC » dans le Centre de contrôle**.

**Quand ça ne marche pas** (Apple) : l'écran doit être allumé, et même allumé, la lecture en arrière-plan n'est pas disponible si l'iPhone n'a jamais été déverrouillé depuis son démarrage, si une app est déjà en train de lire du NFC, si Cartes (Wallet) avec Apple Pay est utilisé, si l'appareil photo est ouvert ou si le mode Avion est activé.

> **`.box` L'essentiel pour tes boîtes :** l'iPhone cherche sur l'étiquette un **lien** (un enregistrement URI) et prend le premier. Un simple **texte** comme « Lentilles · 6/9 » ne déclenche **aucune** notification : tu ne peux le lire qu'en ouvrant une app NFC. Si tu veux approcher le téléphone de la boîte et voir quelque chose tout de suite, l'étiquette doit contenir un lien.

## À la main ou avec FreshTrack NFC  `#freshtrack`

**CTA, phrase en gras :** Tout ce qui précède se fait avec n'importe quelle app NFC de l'App Store, sans la nôtre.

Nous avons créé FreshTrack NFC parce que nous ne voulions plus recalculer à la main chaque dimanche la date et la durée de conservation ⚑4. Tu colles une étiquette réinscriptible sur le couvercle, tu indiques dans l'app ce que contient la boîte et si elle va au frigo ou au congélateur, et l'app calcule la date selon le type d'aliment et l'endroit où il est rangé. Sur l'étiquette, elle n'écrit **qu'un lien**, pas le contenu : ce qu'il y a dedans est noté dans l'app. C'est pour cela qu'un iPhone XS ou plus récent reconnaît l'étiquette tout seul. Approche l'iPhone du couvercle, touche la notification, et la boîte s'ouvre dans l'app. Quelqu'un qui n'a pas l'app voit une petite page web qui explique ce qu'est l'étiquette. Une fois la boîte vidée, tu réécris l'étiquette pour le contenu suivant.

L'app n'exige pas d'étiquettes : tu peux aussi créer et modifier des boîtes sans étiquette. Les étiquettes réinscriptibles NTAG213 et NTAG215 fonctionnent. Lire et écrire les étiquettes NFC nécessite un iPhone ; l'app existe pour iPhone et iPad. Gratuite, sans pub, sans achat intégré, sans créer de compte.

**[Insignia `fr-black.svg`/`fr-white.svg`, `alt` «Télécharger dans l'App Store»]** → enlace de §1.

## Questions fréquentes  `#questions`

### NTAG213 ou NTAG215 : quelle étiquette NFC pour des boîtes ?
La NTAG213 suffit. Selon NXP, elle a 144 octets de mémoire ; un lien en demande environ 70. La NTAG215 (504 octets) seulement pour des textes longs.

### Que veut dire la notification « étiquette NFC » sur iPhone ?
Que l'iPhone a lu une étiquette NFC contenant un lien. Dès l'iPhone XS, il le fait sans ouvrir d'app ; rien ne s'ouvre tant que tu ne touches pas la notification (Apple).

### Les autocollants NFC fonctionnent-ils avec l'iPhone ?
Oui, dès l'iPhone 7, sans accessoire (Apple). Dès l'iPhone XS, ils sont lus même sans app ouverte.

### Une étiquette NFC tient-elle au congélateur ?
Nous n'avons pas trouvé d'indication de fabricant pour −18 °C sur les autocollants ordinaires ; les valeurs de NXP sont données à 22 °C. Ce qui compte, c'est l'autocollant : choisis-en un annoncé pour le congélateur.

### Les étiquettes NFC passent-elles au lave-vaisselle ?
Seulement si le vendeur l'indique. Ni NXP ni Apple ne donnent d'indication générale. Dans le doute, lave le couvercle à la main.

### Pourquoi aucune notification n'apparaît ?
L'étiquette ne contient que du texte au lieu d'un lien, l'iPhone est antérieur au XS, l'écran est éteint, ou l'appareil photo, Wallet ou le mode Avion sont actifs (Apple).

### L'iPad peut-il lire les étiquettes NFC ?
Non. Apple ne liste que des modèles d'iPhone pour le lecteur d'étiquette NFC.

### Combien de fois peut-on réécrire une étiquette NFC ?
100 000 fois selon NXP (à 22 °C), avec 10 ans de conservation des données.

---

**Pied de page :** [Leer en español](../../guias/etiquetas-nfc-tuppers.html) · [Read in English](../../en/guides/nfc-labels-food-containers.html) · [Auf Deutsch lesen](../../de/ratgeber/nfc-etiketten-dosen.html) · [Leggi in italiano](../../it/guide/etichette-nfc-contenitori.html)

---

## 3. Resumen fiel en español (para el dueño)

Mismo contenido y mismas fuentes que la guía alemana NFC (ver `guia-de-nfc-2026-11-24.md` §3), adaptado al
francés de Francia y con tuteo como la ficha FR. Diferencias: usa los nombres que Apple da en francés
(«Lecteur d'étiquette NFC», «Centre de contrôle»), y añade un párrafo y una pregunta sobre **qué significa la
notificación de «étiquette NFC» en el iPhone**, porque es lo que más se busca en francés («notification
etiquette nfc de site web»): la respuesta es que el iPhone ha leído una etiqueta con un enlace y no abre nada
hasta que la tocas (Apple). Sin enlaces de compra; sin dato de congelador ni lavavajillas porque no lo hay.
FreshTrack NFC: escribe solo un enlace, se abre la boîte al tocar la notificación, página para quien no tiene
la app, se reescribe, boîtes sin etiqueta posibles, NFC solo en iPhone, gratis, sin anuncios, sin compras,
sin cuenta. 8 preguntas cortas.

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «ce n'est pas la puce qui lâchera la première» | Giro coloquial; alternativa «la puce tiendra des années» |
| ⚑2 | Consejos «Ce que nous en déduisons» | Que se lea como criterio nuestro |
| ⚑3 | «C'est cette notification que beaucoup découvrent sans comprendre» | **No he visto el texto exacto que muestra iOS en francés**; por eso la guía no lo cita entre comillas salvo en la pregunta, con la forma genérica «étiquette NFC». Si alguien con un iPhone en francés lo ve, poner el literal |
| ⚑4 | «Nous avons créé FreshTrack NFC parce que…» | Registro |
| — | «Cartes (Wallet)» | En iOS francés la app se llama «Cartes»; Apple escribe «Apple Pay Wallet» en la doc inglesa. Confirmar |
| — | «pelliculée», «ruban de masquage» | Léxico de papelería en Francia |
