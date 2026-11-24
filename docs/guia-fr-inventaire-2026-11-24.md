---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía FR · Inventaire congélateur à imprimer (B3 de la tanda) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. Se publicará sin revisión nativa:
frases de riesgo con ⚑ (§4). Adapta `guias/inventario-congelador.html` con fuentes francófonas: Santé publique
France y Anses (Francia) y la **FRC** (Fédération romande des consommateurs, Suiza), que es la única fuente
francófona leída hoy con una tabla de meses de congelación.

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `fr/guides/inventaire-congelateur.html` |
| `hreflang` | `fr` → esta · `es` → `/guias/inventario-congelador.html` · `en` → `/en/guides/freezer-inventory.html` · `de` → `/de/ratgeber/gefrierschrank-inventarliste.html` (B1 de hoy) · `x-default` → la inglesa |
| Enlace a la tienda | `https://apps.apple.com/fr/app/id6791699550?pt=126402967&ct=web-fr-guide-inventaire&mt=8` |
| `<title>` (60) | `Inventaire congélateur à imprimer gratuit : modèle et durées` |
| `meta description` (145) | `Un inventaire de congélateur gratuit à imprimer, ce qu'il doit contenir, et combien de mois se gardent les aliments congelés maison selon la FRC.` |
| `og:title` | `Inventaire congélateur à imprimer gratuit` |
| JSON-LD | `Article` (`fr-FR`, `citation` §1.1) + `BreadcrumbList` (FreshTrack › Guides › Inventaire congélateur) |
| Plantilla imprimible | La tabla de `#modele` en HTML con CSS de impresión (A4 apaisado, 20 filas vacías). Opcional: PDF en `fr/guides/inventaire-congelateur.pdf`. Sin pedir correo |
| Ficha para `fr/guides/index.html` | `h2`: Inventaire congélateur à imprimer · `p.q`: Qu'y a-t-il dans le congélateur, et depuis quand ? · `p.fact`: Restes et plats précuisinés : 2 à 3 mois ; légumes : 6 à 12 mois (FRC). |

### 1.1 Fuentes, leídas hoy (2026-11-24)

| # | Fuente | Qué da |
|---|---|---|
| R1 | **FRC**, «Fiche 6 · La congélation» (PDF, septiembre 2020) — `https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf` | Etiquetar contenido y fecha de congelación; «Les mêmes informations sur une liste ou sur des notes autocollantes fixées à l'extérieur permettent d'avoir une vue d'ensemble des réserves sans ouvrir le congélateur»; −18 a −22 °C; termómetro externo; descongelar con regularidad («une couche de 5 cm de glace double sa consommation»); lo nuevo, tras 24 h, detrás de lo antiguo; porciones; sin aire; no recongelar salvo si se ha cocinado entretanto. Tabla «Durées de conservation conseillées pour les aliments congelés "maison"» (fuente citada: Kantonales Labor Zürich): carne picada cruda 1-3 meses, cerdo crudo 2-4, ternera/cordero/ave crudos 4-5, buey crudo 6-10, pescado fresco 2-6, setas 4-6, verduras 6-12, frutas 8-12, hierbas picadas 6-10, pastel 2-4, pan 4-6, masa 3-4, helado casero 3-4, **plats précuisinés, restes (rôti ou sauce bolognaise) 2-3 mois** |
| S1 | **Santé publique France – Manger Bouger**, «Petit guide de la conservation des aliments» (21/04/2022) — `https://www.sante.fr/petit-guide-de-la-conservation-des-aliments-et-regles-dhygiene` | −18 °C; no sobrecargar, «le froid doit pouvoir circuler»; descongelar el congelador «au moins une fois par an»; no recongelar tras descongelar |
| S2 | **Anses**, «Comment bien conserver ses aliments…» (23/06/2022) — `https://www.anses.fr/fr/content/comment-bien-conserver-ses-aliments-et-ne-pas-interrompre-la-chaine-du-froid` (leída en la Wayback Machine, copia del 31-07-2026, porque anses.fr bloquea a clientes automáticos) | Congelar «dès l'achat ou la préparation et non en fin de date limite de consommation»; −18 °C para la multiplicación pero los microorganismos sobreviven; descongelado: «pas plus de trois jours», sin recongelar |
| A4 | Ficha FR de la App Store (lookup 24-11) | Todo lo que se dice de la app en `#freshtrack` |

**Autocompletado (24-11, `hl=fr&gl=fr`):** «inventaire congélateur à imprimer gratuit» (primera sugerencia),
«…à imprimer», «…pdf», «…excel», «application inventaire congélateur», «fiche / tableau / liste inventaire
congélateur»; «étiquette congélation (à imprimer, réutilisable, effaçable)».

---

## 2. TEXTO DE LA PÁGINA (francés)

> **Fil d'Ariane :** FreshTrack › Guides › Inventaire congélateur · **Kicker :** Guide

# Inventaire du congélateur à imprimer : savoir ce qu'il contient sans tout vider

**Chapô :** Un modèle gratuit à imprimer, ce que chaque ligne doit contenir pour que la liste reste juste, et combien de mois se gardent les aliments congelés à la maison. Une app, c'est en option.

**Signature :** Publié le [date] par SOFTAPP SOLUTIONS LLC · Sources vérifiées le 24 novembre 2026

**Sommaire :** 1. En bref (`#bref`) · 2. Ce que doit contenir l'inventaire (`#contenu`) · 3. Combien de temps au congélateur ? (`#durees`) · 4. Papier, tableur, étiquette ou app (`#methodes`) · 5. Le mettre en place en un après-midi (`#mise-en-place`) · 6. La seule règle qui le garde à jour (`#regle`) · 7. Modèle à imprimer (`#modele`) · 8. Avec FreshTrack NFC (`#freshtrack`) · 9. Questions fréquentes (`#questions`)

## En bref  `#bref`

Un inventaire de congélateur utile tient en quatre colonnes : **ce que c'est, combien, la date de congélation et où c'est rangé.** La Fédération romande des consommateurs (FRC) le dit ainsi : écrire « le contenu et la date de congélation » sur les sachets et récipients, et reporter « les mêmes informations sur une liste ou sur des notes autocollantes fixées à l'extérieur » permet « d'avoir une vue d'ensemble des réserves sans ouvrir le congélateur ». L'emplacement, c'est notre ajout ⚑1 : il évite de chercher.

Combien de temps : restes et plats précuisinés **2 à 3 mois**, légumes **6 à 12 mois** (FRC). Le modèle à imprimer est [plus bas](#modele), gratuit et sans inscription.

## Ce que doit contenir l'inventaire  `#contenu`

- **Ce que c'est.** Le plat, pas la boîte : « lentilles aux saucisses », pas « boîte 3 ».
- **Combien.** Parts ou grammes : la FRC conseille de congeler en portions adaptées à l'usage (« de soupe pour remplir un bol »).
- **Congelé le.** La date d'entrée au congélateur (FRC).
- **À consommer avant.** Date de congélation plus les mois du tableau ci-dessous. C'est un repère de qualité, pas une date de sécurité (voir plus bas) ⚑1.
- **Où.** Tiroir ou étagère.
- **Sorti le.** Barrer suffit ; la date te montre ensuite à quel rythme tu consommes.

## Combien de temps au congélateur ?  `#durees`

**Tableau** (`caption` : « Durées de conservation conseillées pour les aliments congelés maison, selon la FRC (2020) »)

| Aliment | Durée conseillée |
|---|---|
| Plats précuisinés, restes (rôti, sauce bolognaise) | 2–3 mois |
| Viande hachée crue | 1–3 mois |
| Porc cru | 2–4 mois |
| Veau, agneau, volaille crus | 4–5 mois |
| Bœuf cru | 6–10 mois |
| Poisson frais | 2–6 mois |
| Champignons | 4–6 mois |
| Légumes | 6–12 mois |
| Fruits, baies | 8–12 mois |
| Fines herbes hachées | 6–10 mois |
| Pain | 4–6 mois |
| Gâteau | 2–4 mois |
| Pâte, pâton | 3–4 mois |
| Glace maison | 3–4 mois |

*(`p.fine`)* Source : FRC, [Fiche 6 · La congélation](https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf) (2020), d'après le laboratoire cantonal de Zurich. Les sources officielles françaises que nous avons lues (Santé publique France, Anses) ne publient pas de tableau en mois.

**Pourquoi ce sont des repères de qualité.** À −18 °C, la multiplication des bactéries s'arrête, mais « la plupart des microorganismes survivent à la congélation » (Anses) ; la FRC le dit aussi : la congélation « freine le développement de bactéries nocives mais ne les tue pas ». Au-delà des durées, c'est surtout le goût et la texture qui se dégradent : la FRC explique que l'oxygène fait rancir les graisses même au froid. D'où deux conseils : congeler tôt, « dès l'achat ou la préparation et non en fin de date limite de consommation » (Anses), et bien remplir les boîtes ou vider l'air des sachets (FRC).

## Papier, tableur, étiquette ou app  `#methodes`

Aucune méthode n'est mauvaise. Chacune lâche à un endroit différent.

| Méthode | Coût | Qui la voit | Quand elle n'est plus juste | Elle prévient ? |
|---|---|---|---|---|
| Liste papier ou notes collées sur la porte (ce que propose la FRC) | papier et stylo | qui passe devant le congélateur | quand quelqu'un sort quelque chose sans barrer | non |
| Tableur (Excel ou autre) | souvent rien | qui a le fichier ou le lien, même ailleurs | quand ouvrir le téléphone devant le congélateur demande plus d'effort que d'ouvrir la porte | seulement si tu crées toi-même une règle |
| Étiquette sur chaque boîte (feutre, papier ou NFC) | du ruban de masquage aux étiquettes NFC | qui ouvre la porte et lit le couvercle | presque jamais, l'information voyage avec la boîte ; mais sans liste, pas de vue d'ensemble | non, sauf NFC avec une app qui le fait |
| App | selon l'app | toi, sur ton téléphone, sans ouvrir la porte | comme les autres : quand on n'ajoute rien en congelant | oui, si l'app calcule la date et prévient |

Choisir sans y passer des heures ⚑1 : seul ou à deux avec un petit congélateur, la liste sur la porte suffit. Un grand coffre à la cave : étiquette sur chaque boîte **et** liste, sinon tu descends pour chaque question. Plusieurs logements (résidence secondaire, parents) : tableur ou app.

## Le mettre en place en un après-midi  `#mise-en-place`

C'est la seule fois où tu vides tout. Ensuite, la liste t'évite justement de le refaire.

1. **Profite du dégivrage.** Santé publique France conseille de dégivrer le congélateur au moins une fois par an ; la FRC rappelle qu'une couche de 5 cm de glace double sa consommation d'électricité.
2. **Prépare une glacière ou des sacs isothermes** pour que rien ne décongèle pendant le tri.
3. **Sors tout, ce qui n'est pas étiqueté d'abord.** Ce que tu ne reconnais pas et ne peux pas dater : dans le doute, ne le mange pas.
4. **Range par familles**, un tiroir par famille (« plats cuisinés », « légumes », « viande »).
5. **Étiquette chaque paquet** avec le contenu et la date (FRC) et note-le en même temps dans la liste.
6. **Les nouveaux derrière les anciens** (FRC), pour prendre d'abord ce qui doit partir en premier. Et sans trop remplir : le froid doit pouvoir circuler (Santé publique France).

## La seule règle qui le garde à jour  `#regle`

**On note en mettant, on barre en sortant.** Tout de suite, pas le soir ⚑2. Toutes les listes meurent au même endroit : la fois où l'on se dit « je le noterai tout à l'heure ». C'est pour ça que la liste se colle sur la porte et pas dans un tiroir de la cuisine, avec le stylo à côté.

## Modèle à imprimer  `#modele`

**Congélateur de : ____________ · Dernier inventaire : ____________**

| Quoi | Parts | Congelé le | À consommer avant | Où | Sorti le |
|---|---|---|---|---|---|
| Lentilles aux saucisses | 2 | 03/11 | 03/01 | Tiroir 1 | |
| Brocoli blanchi | 500 g | 10/11 | 10/05 | Tiroir 3 | |
| *(20 lignes vides)* | | | | | |

*(Sous le tableau, en petit, imprimé :)* Restes et plats précuisinés 2–3 mois · Légumes 6–12 · Fruits 8–12 · Bœuf cru 6–10 · Viande hachée crue 1–3 · Pain 4–6 (FRC).

*(Los ejemplos: guiso + 2 meses, verdura + 6 meses, dentro de la tabla.)*

## Avec FreshTrack NFC  `#freshtrack`

**CTA, phrase en gras :** La liste papier ci-dessus suffit à beaucoup de monde. Pour ceux qui la préfèrent sur l'iPhone :

Nous avons créé FreshTrack NFC pour avoir la liste dans le téléphone et être prévenus à temps ⚑3. Tu ajoutes tes produits en scannant le code-barres, et l'app remplit le type, l'emplacement et la durée de conservation standard. Pour les plats faits maison, tu colles une étiquette NFC réinscriptible sur le couvercle : l'app calcule la date selon le type d'aliment et l'endroit, et en posant ton iPhone sur le couvercle tu vois le contenu et la date. Tu peux demander à Siri : « Qu'ai-je dans le congélateur sur FreshTrack ? ». Une alerte par jour, groupée en périmé, aujourd'hui et cette semaine, et un widget pour voir ce qui périme sans ouvrir l'app. Pour la maison de vacances ou celle des parents, tu crées des foyers séparés, synchronisés via iCloud entre **tes** appareils. Gratuite, sans pub, sans achat intégré, sans créer de compte ; tout reste sur ton appareil et dans ton iCloud privé. Lire et écrire les étiquettes NFC nécessite un iPhone. Plus de détails sur les étiquettes dans le guide [Étiquettes NFC pour boîtes](etiquettes-nfc-boites.html).

**[Insignia `fr-black.svg`/`fr-white.svg`]** → enlace de §1.

## Questions fréquentes  `#questions`

### Où trouver un inventaire de congélateur à imprimer gratuit ?
Sur cette page, sans inscription : colonnes pour le contenu, les parts, la date de congélation, la date limite conseillée, l'emplacement et la sortie.

### Que noter sur un inventaire de congélateur ?
Le contenu et la date de congélation (FRC), plus la quantité et l'emplacement. Les mêmes informations vont sur le sachet ou la boîte.

### Combien de temps se gardent les restes au congélateur ?
2 à 3 mois pour les plats précuisinés et les restes (rôti, sauce bolognaise), selon la FRC.

### Combien de temps se gardent la viande et les légumes congelés ?
Selon la FRC : viande hachée crue 1–3 mois, porc cru 2–4, volaille crue 4–5, bœuf cru 6–10, légumes 6–12 mois.

### À quelle température régler le congélateur ?
−18 °C (Santé publique France) ; la FRC situe l'idéal entre −18 et −22 °C.

### Peut-on recongeler un aliment décongelé ?
Non (Santé publique France, Anses), sauf s'il a été cuisiné entre-temps (FRC). Un aliment décongelé se consomme dans les trois jours (Anses).

### Tous les combien faut-il faire l'inventaire ?
Au moins une fois par an, au moment du dégivrage (Santé publique France). Entre-temps, la liste ne reste juste que si l'on note et barre à chaque fois.

---

**Pied de page :** [Leer en español](../../guias/inventario-congelador.html) · [Read in English](../../en/guides/freezer-inventory.html) · [Auf Deutsch lesen](../../de/ratgeber/gefrierschrank-inventarliste.html)

---

## 3. Resumen fiel en español (para el dueño)

**«Inventario del congelador para imprimir: saber qué hay sin vaciarlo».** Mismo esquema que la guía alemana
B1, con fuentes francófonas: qué lleva cada línea (contenido y fecha según la FRC suiza, que además propone una
lista o notas pegadas fuera para ver las reservas sin abrir; cantidad y sitio, añadido nuestro); **tabla de meses
de la FRC** (restos y platos precocinados 2-3, verduras 6-12, buey crudo 6-10, carne picada 1-3…), diciendo que
las fuentes oficiales francesas no publican meses; por qué son meses de calidad (Anses, FRC); papel, hoja de
cálculo, etiqueta o app, con su punto débil; montarlo aprovechando la descongelación anual (Santé publique
France) — 5 cm de hielo duplican el consumo (FRC); la regla de anotar y tachar; **plantilla imprimible gratis**;
FreshTrack NFC como opción (escaneo, etiqueta NFC, Siri en francés, un aviso al día, widget, varios hogares
sincronizados entre tus aparatos), gratis, sin anuncios, sin compras, sin cuenta; 7 preguntas cortas.

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | «c'est notre ajout», «repère de qualité», «Choisir sans y passer des heures» | Que se lea como criterio nuestro; naturalidad |
| ⚑2 | «Tout de suite, pas le soir.» / «je le noterai tout à l'heure» | Giro |
| ⚑3 | «pour avoir la liste dans le téléphone et être prévenus à temps» | Concordancia («prévenus» plural por «nous») |
| — | «coffre à la cave», «pâton», «ruban de masquage» | Léxico de Francia frente a Suiza (la fuente es suiza: «congélateur-coffre», «bahut») |
