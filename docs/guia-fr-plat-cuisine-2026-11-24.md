---
# Documento interno: Jekyll no lo publica en la web.
published: false
---

# Guía FR · Combien de temps se conserve un plat cuisiné au frigo (B2 de la tanda) · 2026-11-24

**Hecho por:** `growth-marketing` (M4). Solo texto; lo maqueta `web-dev`. Se publicará sin revisión nativa:
frases de riesgo con ⚑ (§4). Mismo método que la guía alemana publicada: cifras solo de fuentes oficiales
francesas (o europeas), y donde no hay cifra, se dice.

## 1. Ficha para maquetar

| Campo | Propuesta |
|---|---|
| Ruta | `fr/guides/plat-cuisine-frigo.html` (carpeta `fr/guides/` creada con la guía NFC FR) |
| `hreflang` | `fr` → esta · `es` → `/guias/cuanto-dura-comida-cocinada-nevera.html` · `en` → `/en/guides/how-long-leftovers-last.html` · `it` → `/it/guide/quanto-dura-cibo-cotto-in-frigo.html` · `de` → `/de/ratgeber/gekochtes-essen-kuehlschrank.html` · `x-default` → la inglesa. Recíproco en las cuatro |
| Enlace a la tienda | `https://apps.apple.com/fr/app/id6791699550?pt=126402967&ct=web-fr-guide-plat-cuisine&mt=8` |
| `<title>` (69) | `Combien de temps se conserve un plat cuisiné au frigo ? Plat par plat` |
| `meta description` (155) | `Restes faits maison : 3 jours au frigo, jamais plus de 2 heures dehors. Ce que disent Santé publique France, l'Anses et l'EFSA, riz et congélation compris.` |
| `og:title` | `Combien de temps se conserve un plat cuisiné au frigo ?` |
| JSON-LD | `Article` (`fr-FR`, `citation` §1.1) + `BreadcrumbList` (FreshTrack › Guides › Plat cuisiné au frigo) |
| Descargo (`p.fine` del CTA) | Texto literal de la app en francés, clave `the-dates-freshtrack-calculates-are-approximate-estimates` (`Localizable.xcstrings`): «Les dates calculées par FreshTrack sont des estimations indicatives basées sur des normes générales de conservation des aliments (guides du type FoodKeeper de l'USDA et recommandations de sécurité alimentaire). Elles ne remplacent pas la DLC (date limite de consommation) ou la DDM (date de durabilité minimale) imprimée sur l'emballage, ni ton propre jugement sur l'apparence, l'odeur ou le goût de l'aliment. En cas de doute, ne le consomme pas.» |
| Ficha para `fr/guides/index.html` | `h2`: Combien de temps se conserve un plat cuisiné au frigo ? · `p.q`: Je le mange ou je le jette ? · `p.fact`: Restes faits maison : 3 jours au frigo selon Santé publique France ; jamais plus de 2 heures à température ambiante. |

### 1.1 Fuentes, leídas hoy (2026-11-24)

| # | Fuente | Fecha | Qué da | Qué no da |
|---|---|---|---|---|
| S1 | **Santé publique France – Manger Bouger**, «Petit guide de la conservation des aliments et règles d'hygiène», publicado en sante.fr — `https://www.sante.fr/petit-guide-de-la-conservation-des-aliments-et-regles-dhygiene` | 21/04/2022 | Restos caseros: «consommez le plus rapidement possible (dans les 3 jours)»; preparaciones con huevo crudo: «dans les 24h maximum»; «Ne pas laisser refroidir plus de 2h à température ambiante», repartir «en petites quantités peu épaisses»; zona fría ≤ 4 °C; congelador a −18 °C, descongelar el congelador al menos una vez al año; no recongelar lo descongelado; en la zona fría: «plats cuisinés»; en la parte media: «préparations maison… viandes et poissons cuits faits maison» | días por plato; meses de congelador; arroz |
| S2 | **Anses**, «Comment bien conserver ses aliments et ne pas interrompre la chaîne du froid ?» — `https://www.anses.fr/fr/content/comment-bien-conserver-ses-aliments-et-ne-pas-interrompre-la-chaine-du-froid` | 23/06/2022 | 4 °C en la zona más fría; «plats cuisinés dans la zone la plus froide»; a −18 °C la multiplicación se para pero «la plupart des microorganismes survivent»; congelar «dès l'achat ou la préparation et non en fin de date limite»; descongelar en la nevera, microondas o cocción; descongelado: «pas plus de trois jours» y no recongelar; huevo crudo: 24 h | días para restos caseros; meses |
| S3 | **Anses**, «Qu'est-ce que Bacillus cereus et comment s'en prémunir ?» — `https://www.anses.fr/fr/content/qu-est-ce-que-bacillus-cereus-et-comment-s-en-premunir` | 19/03/2026 | Principal causa de TIAC bacterianas en Francia (~¼; 462 focos en 2022); crece entre 4 °C y 55 °C; la cereulida resiste el calor, «reste active même après avoir (ré)chauffé»; pasta, arroz, sémola cocidos conservados a temperatura ambiente; «Refroidir rapidement… et les conserver au réfrigérateur dans les 2 heures» | horas o días para el arroz en la nevera |
| S4 | **Anses**, ficha «Hygiène domestique : 10 recommandations à retenir» (PDF) — `https://www.anses.fr/fr/system/files/ANSES-Ft-HygieneDomestique.pdf` | diciembre 2017 | Platos cocinados **comprados**: 3 días tras la compra; 0 a +4 °C en la zona fría; a la nevera «au plus tard 2 heures après leur préparation» | restos caseros |
| S5 | **DGCCRF**, «La chaîne du froid : adoptez les bons réflexes !», en sante.fr — `https://www.sante.fr/la-chaine-du-froid-adoptez-les-bons-reflexes` | 19/08/2019 | «plats cuisinés maison»: entre 0 °C y +4 °C; restos «dans des emballages fermés et consommez-les rapidement»; termómetro si la nevera no lleva indicador | días |
| S6 | **EFSA**, Safe2Eat (francés) — `https://www.efsa.europa.eu/fr/safe2eat/proper-food-handling` | — | «Ne pas laisser les aliments cuits à température ambiante plus de 2 heures»; nevera «de préférence en dessous de 5 °C»; sopas y guisos a 70 °C | días |
| S7 | **FSA** (Reino Unido), «Home food fact checker» — `https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker` (releída hoy) | — | arroz: en la nevera y en 24 horas | — |
| S8 | **FRC** (Fédération romande des consommateurs, Suiza), «Fiche 6 · La congélation» (PDF) — `https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf` | septiembre 2020 | «Plats précuisinés, restes (rôti ou sauce bolognaise) : 2-3 mois» (según el laboratorio cantonal de Zúrich); la congelación «freine le développement de bactéries nocives mais ne les tue pas»; no recongelar salvo si se ha cocinado entretanto | — |

**Cómo se han leído las de la Anses:** `anses.fr` responde a `curl` y a `WebFetch` con un desafío anti-bots
(CrowdSec). He leído las tres páginas en la Wayback Machine: S2 en la copia del 31-07-2026, S3 en la del
20-10-2026 (fecha de la página: 19/03/2026), S4 en la del 30-09-2023 (edición de 2017). En la guía se enlaza la
URL oficial. Si `web-dev` o `seo-indexing` pueden abrirlas con un navegador, que confirmen que siguen igual.

**Lo que no he encontrado en fuente oficial francesa:** días por plato; horas o días para el arroz en la
nevera (la prensa atribuye a la AFSCA belga «2 jours» para pasta y arroz, pero no he podido leerlo en su web:
no se usa); meses de congelador para platos cocinados; huevo duro. La guía lo dice.

**Autocompletado (24-11, `hl=fr`, `gl=fr` y `gl=ch`):** «combien de temps se conserve un plat cuisiné au frigo»,
«…un plat préparé au frigo», «…un plat cuit au frigo», «combien de temps garder un plat fait maison au frigo»;
«combien de temps se conserve le riz cuit (au frigo / au congélateur / à température ambiante)»; «plat chaud
frigo (ou pas)», «mettre plat chaud frigo», «plat chaud au frigo bactérie»; «combien de temps se conserve une
mousse au chocolat maison».

---

## 2. TEXTO DE LA PÁGINA (francés)

> **Fil d'Ariane :** FreshTrack › Guides › Plat cuisiné au frigo · **Kicker :** Guide

# Combien de temps se conserve un plat cuisiné au frigo ? Plat par plat, selon les sources officielles

**Chapô :** Riz, pâtes, soupe, plat mijoté, viande, poisson, légumes, sauce et dessert : ce que disent Santé publique France, l'Anses et l'EFSA, là où elles ne donnent pas de chiffre, et comment noter la date pour ne plus deviner.

**Signature :** Publié le [date] par SOFTAPP SOLUTIONS LLC · Sources vérifiées le 24 novembre 2026

**Sommaire :** 1. En bref (`#bref`) · 2. Plat par plat (`#tableau`) · 3. Le cas du riz (`#riz`) · 4. Plat chaud au frigo ? (`#refroidir`) · 5. Où le ranger dans le frigo (`#ou`) · 6. Congeler un plat cuisiné (`#congeler`) · 7. Noter la date (`#date`) · 8. L'odeur ne suffit pas (`#odeur`) · 9. À la main ou avec FreshTrack NFC (`#freshtrack`) · 10. Questions fréquentes (`#questions`)

## En bref  `#bref`

Les restes d'un plat fait maison se conservent au réfrigérateur **3 jours au maximum**. Santé publique France le formule ainsi : « Conservez au réfrigérateur et consommez le plus rapidement possible (dans les 3 jours) les restes des repas faits maison. »

Deux règles l'accompagnent. **Pas plus de 2 heures à température ambiante** avant de le mettre au frais (Santé publique France, Anses, EFSA). Et les préparations **à base d'œufs crus**, comme la mayonnaise ou la mousse au chocolat maison, **24 heures au maximum** (Santé publique France, Anses).

Pour le **riz**, aucune source officielle française que nous avons lue ne donne de durée propre ; l'agence britannique (FSA) dit 24 heures, et nous expliquons pourquoi plus bas.

Tout cela suppose un frigo froid : **4 °C au maximum dans la zone la plus froide** (Anses). Et si tu sais que tu ne le mangeras pas à temps, congèle-le tout de suite : l'Anses conseille de congeler « dès l'achat ou la préparation et non en fin de date limite ».

## Plat par plat  `#tableau`

FreshTrack NFC propose dix types de plats cuisinés (plus la viande et le poisson crus, hors sujet ici). Pour chacun : ce que disent les sources officielles et les jours que l'app propose par défaut.

**Tableau** (`caption` : « Conservation des plats cuisinés selon les sources officielles et valeurs par défaut de FreshTrack NFC ; sources vérifiées le 24 novembre 2026 »)

| Plat | Frigo selon les sources officielles | Congélateur selon les sources officielles | FreshTrack NFC par défaut (frigo / congélateur) |
|---|---|---|---|
| Riz cuit | pas de chiffre français ; **24 heures** selon la FSA (Royaume-Uni) ; règle générale : 3 jours | pas de chiffre† | 2 jours / 90 jours |
| Pâtes cuites | 3 jours* | pas de chiffre† | 3 jours / 60 jours |
| Légumineuses / plat mijoté | 3 jours* | pas de chiffre† | 3 jours / 90 jours |
| Soupe / velouté | 3 jours* | pas de chiffre† | 3 jours / 90 jours |
| Viande cuite | 3 jours* | pas de chiffre† | 3 jours / 90 jours |
| Poisson cuit | 3 jours* | pas de chiffre† | 2 jours / 60 jours |
| Légumes cuits | 3 jours* | pas de chiffre† | 3 jours / 60 jours |
| Omelette / œuf | 3 jours* | pas de chiffre† | 2 jours / 30 jours |
| Sauce faite maison | 3 jours* ; à base d'œufs crus (mayonnaise) : **24 heures** | pas de chiffre† | 4 jours / 90 jours |
| Dessert fait maison | 3 jours* ; à base d'œufs crus (mousse au chocolat) : **24 heures** | pas de chiffre† | 3 jours / 30 jours |

*(`p.fine`)* Sources : Santé publique France – Manger Bouger, [Petit guide de la conservation des aliments](https://www.sante.fr/petit-guide-de-la-conservation-des-aliments-et-regles-dhygiene) (21/04/2022) ; Anses, [Comment bien conserver ses aliments](https://www.anses.fr/fr/content/comment-bien-conserver-ses-aliments-et-ne-pas-interrompre-la-chaine-du-froid) (23/06/2022) ; FSA, [Home food fact checker](https://www.gov.uk/government/publications/home-food-fact-checker/home-food-fact-checker) (en anglais). Jours de FreshTrack NFC : valeurs par défaut de l'app.

**\* Pas de chiffre propre pour ce plat.** C'est la règle générale de Santé publique France pour les restes faits maison (« dans les 3 jours »). **† Pas de durée officielle française** en mois pour les plats cuisinés dans les pages que nous avons lues. Repère suisse : la Fédération romande des consommateurs (FRC) conseille [2 à 3 mois](https://www.frc.ch/wp-content/uploads/2020/09/FRC-GASPI-ALIM-F6-CONGELATION-LR-WEB.pdf) pour les plats précuisinés et les restes congelés à la maison.

Trois choses pour lire le tableau :
- **Les valeurs de FreshTrack NFC ne sont pas officielles.** Ce sont des valeurs de départ, modifiables (voir plus bas).
- **Là où l'app dépasse les sources, nous le disons** : la sauce (4 jours au lieu de 3) ; le riz (2 jours, alors que la FSA dit 24 heures) ; et tout dessert ou sauce à base d'œufs crus, que l'app ne distingue pas (3 ou 4 jours au lieu de 24 heures). Si tu veux t'en tenir aux sources, règle la sauce sur 3 jours et le riz sur 1, et compte toi-même 24 heures pour une mousse ou une mayonnaise.
- **Au congélateur**, l'app propose 30, 60 ou 90 jours, soit 1 à 3 mois : jamais au-delà des 2 à 3 mois de la FRC, parfois en dessous.

**Compte à partir du jour de la cuisson**, pas du jour où tu ouvres la boîte ⚑1. C'est notre lecture : les sources parlent de « restes » sans fixer d'autre point de départ.

## Le cas du riz  `#riz`

Le riz est le cas où il faut être le plus prudent, et l'Anses explique pourquoi. La bactérie *Bacillus cereus*, présente naturellement dans le riz, forme des spores qui résistent à la cuisson. Entre 4 °C et 55 °C, elle se multiplie et certaines souches produisent une toxine, la céréulide, « très stable et résistante à la chaleur » : elle « reste active même après avoir (ré)chauffé ou cuit l'aliment ». Selon l'Anses, *Bacillus cereus* est depuis plusieurs années la principale cause de toxi-infections alimentaires collectives d'origine bactérienne en France, environ un quart des cas.

Le conseil de l'Anses : **refroidir rapidement après cuisson et mettre au réfrigérateur dans les 2 heures.** Une durée de conservation au frigo pour le riz, en revanche, nous ne l'avons trouvée dans aucune source officielle française. La FSA britannique, elle, est nette : au réfrigérateur, et à consommer dans les **24 heures**. Faute de chiffre français, c'est le repère que nous retenons ⚑1.

En pratique : riz étalé en couche fine pour refroidir vite, au frigo dans les 2 heures, consommé dans les 24 heures, réchauffé jusqu'à être bien chaud partout. Riz aux légumes, riz au poulet : c'est l'ingrédient le plus délicat qui compte.

## Plat chaud au frigo ? Refroidir vite  `#refroidir`

- **Pas plus de 2 heures dehors.** « Ne pas laisser refroidir plus de 2h à température ambiante les restes de plats chauds » (Santé publique France) ; même limite pour l'EFSA et l'Anses.
- **En petites quantités peu épaisses.** Pour refroidir plus vite, Santé publique France conseille de répartir le plat « en petites quantités peu épaisses », si nécessaire dans plusieurs récipients. Une grande cocotte encore chaude met longtemps à refroidir, même au frigo ⚑1.
- **Fermé.** Boîtes hermétiques, film ou aluminium (Santé publique France), emballages fermés (DGCCRF).

## Où le ranger dans le frigo  `#ou`

- **Dans la zone la plus froide, à 4 °C au maximum** : c'est là que l'Anses et la DGCCRF placent les plats cuisinés (0 à +4 °C). Le guide de Santé publique France met les « préparations maison » dans la partie du milieu ; en cas de doute, la zone la plus froide est le choix le plus prudent ⚑1.
- **Trouver la zone froide** : selon le modèle, en haut ou en bas (Santé publique France). Si le frigo n'a pas d'indicateur, la DGCCRF conseille un thermomètre.
- **Ne pas surcharger** le frigo, pour que l'air circule (Anses).

## Congeler un plat cuisiné  `#congeler`

- **Le plus tôt possible.** L'Anses : congeler « dès l'achat ou la préparation et non en fin de date limite de consommation ».
- **−18 °C** (Santé publique France). Le froid arrête la multiplication des bactéries, mais « la plupart des microorganismes survivent à la congélation » (Anses).
- **Combien de mois ?** Les sources françaises que nous avons lues ne donnent pas de durée pour les plats cuisinés. Repère suisse : 2 à 3 mois pour les plats précuisinés et les restes (FRC). Plus de durées, aliment par aliment, dans notre [inventaire du congélateur à imprimer](inventaire-congelateur.html).
- **Décongeler au réfrigérateur**, au micro-ondes en position décongélation, ou directement en réchauffant (Anses). Une fois décongelé : **pas plus de trois jours**, et **ne pas recongeler** (Anses, Santé publique France).

## Noter la date  `#date`

Santé publique France conseille de noter au stylo la date d'ouverture des produits entamés ; pour les restes, le même réflexe vaut : la date de cuisson sur le couvercle. Ce qui ne figure pas dans les sources et qui nous est utile ⚑2 :
- **Deux dates** si le plat passe du frigo au congélateur : « cuit le 24/11 · congelé le 26/11 ».
- **Le contenu en clair** : « lentilles aux saucisses, 2 parts » plutôt que « boîte 3 ».
- **Sur le couvercle**, avec un ruban de masquage et un feutre indélébile. Ou une [étiquette NFC](etiquettes-nfc-boites.html), réinscriptible.

## L'odeur ne suffit pas  `#odeur`

La toxine du riz ne se sent pas, et elle résiste à la chaleur (Anses). Un plat qui sent bon n'est donc pas forcément sûr. Les restes n'ont pas de date imprimée : la date, c'est toi. Si tu ne sais plus quand tu as cuisiné, dans le doute, ne le mange pas.

**Prudence particulière** pour les personnes immunodéprimées, les personnes âgées et les jeunes enfants, en particulier les nourrissons : l'Anses les cite parmi les populations les plus à risque face à *Bacillus cereus*.

## À la main ou avec FreshTrack NFC  `#freshtrack`

**CTA, phrase en gras :** Tout cela se fait sans app : le tableau ci-dessus, un feutre indélébile et un bout de ruban de masquage.

Nous avons créé FreshTrack NFC parce que nous ne voulions plus refaire le calcul chaque dimanche ⚑3. Tu colles une étiquette NFC réinscriptible sur le couvercle, tu indiques dans l'app ce que contient la boîte et si elle va au frigo ou au congélateur, et l'app calcule la date selon le type d'aliment et l'endroit, avec les jours du tableau, comptés à partir du jour où tu remplis la boîte dans l'app. En posant ensuite ton iPhone sur le couvercle, tu vois le contenu et la date sans ouvrir la boîte. Sur l'étiquette, il n'y a qu'un lien ; le contenu est noté dans l'app. Une fois la boîte vidée, tu réécris l'étiquette pour le contenu suivant.

L'app te prévient une fois par jour, par défaut deux jours avant, à 9 h. Les jours et l'heure se changent dans les réglages : dans **Réglages → Durées de conservation**, tu peux par exemple régler le riz sur 1 jour (frigo de 1 à 30 jours, congélateur de 1 à 365). Le changement vaut pour les boîtes remplies ensuite.

Gratuite, sans pub, sans achat intégré, sans créer de compte ; les données restent sur ton appareil et dans ton iCloud privé. Lire et écrire les étiquettes NFC nécessite un iPhone ; l'app existe pour iPhone et iPad.

**[Insignia `fr-black.svg`/`fr-white.svg`]** → enlace de §1 · **Descargo** (§1).

## Questions fréquentes  `#questions`

### Combien de temps se conserve un plat cuisiné au frigo ?
3 jours au maximum pour les restes faits maison, selon Santé publique France. Les préparations à base d'œufs crus : 24 heures.

### Combien de temps se conserve le riz cuit au frigo ?
Aucune source officielle française que nous avons lue ne donne de durée. La FSA britannique dit 24 heures. L'Anses demande de le refroidir vite et de le mettre au frigo dans les 2 heures.

### Peut-on mettre un plat chaud au frigo ?
Il ne doit pas rester plus de 2 heures à température ambiante (Santé publique France, EFSA). Pour qu'il refroidisse vite, répartis-le en petites quantités peu épaisses.

### Combien de temps se conserve un plat fait maison au congélateur ?
Les sources françaises consultées ne donnent pas de durée en mois. La FRC (Suisse) conseille 2 à 3 mois pour les restes et plats précuisinés. L'Anses conseille de congeler dès la préparation, pas en fin de conservation.

### Combien de temps se conserve un plat décongelé ?
Pas plus de trois jours, au réfrigérateur, et sans le recongeler (Anses).

### Combien de temps se conserve une mousse au chocolat maison ?
24 heures au maximum au frais, car elle contient des œufs crus (Santé publique France, Anses).

### Où ranger les restes dans le frigo ?
Dans la zone la plus froide, entre 0 et 4 °C, dans un récipient fermé (Anses, DGCCRF).

### Un plat qui sent bon est-il sans danger ?
Pas forcément. La toxine de *Bacillus cereus* ne se sent pas et résiste à la chaleur (Anses).

---

**Pied de page :** [Leer en español](../../guias/cuanto-dura-comida-cocinada-nevera.html) · [Read in English](../../en/guides/how-long-leftovers-last.html) · [Leggi in italiano](../../it/guide/quanto-dura-cibo-cotto-in-frigo.html) · [Auf Deutsch lesen](../../de/ratgeber/gekochtes-essen-kuehlschrank.html)

---

## 3. Resumen fiel en español (para el dueño)

**«¿Cuánto se conserva un plato cocinado en la nevera? Plato a plato, según las fuentes oficiales».** Regla
general francesa: restos caseros **3 días** (Santé publique France); nunca más de **2 horas** fuera (SPF, Anses,
EFSA); lo hecho con **huevo crudo** (mayonesa, mousse de chocolate) **24 horas** (SPF, Anses); nevera a **4 °C**
como mucho en la zona fría (Anses). Tabla con los diez tipos de la app: Francia no da cifra por plato (se usa
la regla de 3 días y se dice); **arroz**: ninguna fuente francesa da horas, se cita la FSA británica (24 h) como
referencia extranjera y se explica con la Anses por qué (Bacillus cereus, primera causa de intoxicaciones
colectivas bacterianas en Francia, toxina que resiste el calor; enfriar y a la nevera en 2 horas). Congelador:
sin meses en fuentes francesas (referencia suiza de la FRC: 2-3 meses para restos); congelar pronto, descongelar en nevera,
descongelado máximo 3 días y sin recongelar (Anses). La guía dice dónde la app pone más días que las fuentes
(salsa, arroz, y postres o salsas con huevo crudo, que la app no distingue). Etiquetado (dos fechas, contenido
en claro, tapa, o etiqueta NFC), «el olor no basta», grupos de riesgo. FreshTrack NFC como forma de aplicarlo
(mismas afirmaciones que en la guía alemana, con la ruta «Réglages → Durées de conservation»). 8 preguntas
cortas.

## 4. Frases que más necesitan revisión nativa

| # | Frase | Duda |
|---|---|---|
| ⚑1 | Frases de criterio propio: «C'est notre lecture», «c'est le repère que nous retenons», «le choix le plus prudent», «Une grande cocotte… met longtemps à refroidir» | Que se lean como criterio nuestro, no como cita |
| ⚑2 | «Ce qui ne figure pas dans les sources et qui nous est utile» | Registro |
| ⚑3 | «Nous avons créé FreshTrack NFC parce que…» | Registro |
| — | «plat mijoté», «velouté», «ruban de masquage», «feutre indélébile» | Léxico (los dos primeros son los nombres de la app en francés) |
