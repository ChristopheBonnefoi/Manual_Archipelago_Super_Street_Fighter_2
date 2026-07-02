# Guide YAML pour Manual_SSF2_NaruSnake

Ce guide explique comment remplir `Manual_SSF2_NaruSnake.yaml` pour Super Street Fighter II.
Le YAML controle le type de seed qu'Archipelago va generer pour ton slot joueur.

## Regle de base

Garde ces champs en haut du fichier :

```yaml
name: Player{number}
description: Default Manual_SSF2_NaruSnake Template
game: Manual_SSF2_NaruSnake
requires:
  version: 0.6.7

Manual_SSF2_NaruSnake:
```

Toutes les options SSF2 doivent rester dans le bloc `Manual_SSF2_NaruSnake:`.
L'indentation est importante. Utilise deux espaces, pas de tabulation.

## Options avec poids

La plupart des options utilisent des poids. Archipelago choisit une entree selon les nombres indiques.

```yaml
Super_Battle:
  'false': 0
  'true': 50
```

Ici, `true` a un poids de 50 et `false` a un poids de 0, donc Super Battle sera toujours active.

```yaml
Super_Battle:
  'false': 25
  'true': 75
```

Ici, Super Battle a 75 chances sur 100 d'etre active.

Pour les options numeriques, le template accepte aussi :

```yaml
random: 0
random-low: 0
random-high: 0
random-range-1-100: 0
```

Utilise une valeur fixe si tu veux controler la seed. Utilise les entrees random si tu veux varier les seeds.

## Goals

L'option `goal` choisit la condition de victoire.

```yaml
goal:
  super battle mode -all clears-: 50
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 0
```

Goals disponibles :

- `super battle mode -all clears-` : finir le Super Battle avec tous les personnages. Force `Super_Battle`.
- `time challenge mode -all clears-` : battre tous les CPU du Time Challenge. Force `CPU_Time_Challenge`.
- `all clears + tokens` : faire les deux objectifs de clear et recuperer les Shadaloo Emblems requis. Force `Super_Battle` et `CPU_Time_Challenge`, et active automatiquement la logique token.
- `street fighter token` : recuperer les Shadaloo Emblems requis. Active automatiquement la logique token.

Une seule goal est choisie au moment de generer la seed.

## Modes de jeu

`Super_Battle` controle les items de progression et les checks lies au Super Battle.

```yaml
Super_Battle:
  'false': 0
  'true': 50
```

Quand cette option est active, le pool peut contenir l'item `Super Battle` et les checks du Super Battle, comme les combats par personnage, les bonus stages et les checks de defaite en Super Battle.

`CPU_Time_Challenge` controle les items CPU et les checks du Time Challenge.

```yaml
CPU_Time_Challenge:
  'false': 0
  'true': 50
```

Quand cette option est active, le pool peut contenir des items CPU comme `Ryu [CPU for Time Challenge]` et les checks de la categorie `Defeated in Time Challenge`.

Si la goal choisie a besoin d'un mode, le hook force ce mode pour que la seed reste finissable.

## Options de gameplay

`Difficulty` ajoute les items de difficulte au pool.

```yaml
Difficulty:
  'false': 0
  'true': 50
```

`Special_Moves` ajoute les coups speciaux au pool.

```yaml
Special_Moves:
  'false': 0
  'true': 50
```

Si `Special_Moves` est desactive, les items de coups speciaux sont retires du pool. Les checks bases sur les coups speciaux restent disponibles, car le joueur peut utiliser les techniques du personnage librement sans restriction d'item.

## Reglages de tokens

Il n'y a plus d'option YAML publique `Token`. Le placement des tokens est controle par le `goal` choisi.

Si la goal choisie demande des tokens, les items `Shadaloo Emblem` sont ajoutes au pool. Si la goal choisie ne demande pas de tokens, `Shadaloo Emblem` est retire du pool.

`shadaloo_emblems_required` definit le nombre de Shadaloo Emblems requis.

```yaml
shadaloo_emblems_required:
  100: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-1-100: 0
```

`shadaloo_emblems_available_percentage` controle combien de Shadaloo Emblems sont places par rapport au nombre requis.

```yaml
shadaloo_emblems_available_percentage:
  100: 50
  random: 0
  random-low: 0
  random-high: 0
  random-range-100-400: 0
```

Exemples :

- Requis `25`, disponible `100` : 25 Shadaloo Emblems sont places.
- Requis `25`, disponible `200` : 50 Shadaloo Emblems sont places.
- Le total final est limite a 100 Shadaloo Emblems.

## Checks

Dans Archipelago Manual, les checks sont des locations. Quand tu fais l'objectif en jeu, tu coches la location dans le client.

Ce manual contient 470 checks, surtout groupes par personnage et par mode.

Groupes de checks principaux :

- Checks de personnage : combats, bonus stages, first attack, stun, perfect round, victoire avec coup special et challenges propres aux personnages.
- `Defeated in Super Battle Mode` : battre chaque personnage en Super Battle.
- `Defeated in Time Challenge` : battre chaque CPU en Time Challenge.
- `Stage` : checks lies aux stages ou aux elements de decor.
- `Special` : challenges speciaux ou multi-personnages.
- `Goal` : locations finales de victoire.

Certains checks peuvent se faire en Super Battle ou en Time Challenge. Leur logique ressemble souvent a ca :

```text
|Character [Player]| and |Super Battle| or (|Time Challenge| and |CPU [CPU for Time Challenge]|)
```

Ca veut dire que le check est valide si tu as le personnage jouable et Super Battle, ou si Time Challenge est actif avec le CPU correspondant.

## Les noms exacts comptent

Quand tu mets des noms d'items ou de locations dans le YAML, il faut utiliser exactement la meme ecriture que dans les fichiers data.

Ecriture canonique des personnages :

- `E.Honda`
- `M.Bison`
- `T.Hawk`
- `Chun-Li`

Exemples de noms d'items utiles :

```yaml
start_inventory:
  "Ryu [Player]": 1
  "Super Battle": 1
```

```yaml
start_inventory_from_pool:
  "Time Challenge": 1
```

Mets des guillemets autour des noms avec crochets, apostrophes ou ponctuation.

## Champs YAML utiles

`local_items` garde les items listes dans ton monde.

```yaml
local_items:
  - "Super Battle"
```

`non_local_items` force les items listes a partir dans les mondes des autres joueurs.

```yaml
non_local_items:
  - "Shadaloo Emblem"
```

`start_hints` donne des hints d'items au depart.

```yaml
start_hints:
  - "Shadaloo Emblem"
```

`start_location_hints` donne des hints de locations au depart.

```yaml
start_location_hints:
  - "Street Fighter Token"
```

`exclude_locations` evite de mettre des items importants sur les locations listees.

```yaml
exclude_locations:
  - "Ryu - Get Perfect Round"
```

`priority_locations` essaie de mettre des items importants sur les locations listees.

```yaml
priority_locations:
  - "Street Fighter Token"
```

`plando_items` est disponible pour placer des items manuellement si ta configuration Archipelago autorise le plando.

## Exemples de presets

Preset Super Battle :

```yaml
goal:
  super battle mode -all clears-: 50
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 0
Super_Battle:
  'false': 0
  'true': 50
CPU_Time_Challenge:
  'false': 50
  'true': 0
```

Preset Time Challenge :

```yaml
goal:
  super battle mode -all clears-: 0
  time challenge mode -all clears-: 50
  all clears + tokens: 0
  street fighter token: 0
Super_Battle:
  'false': 50
  'true': 0
CPU_Time_Challenge:
  'false': 0
  'true': 50
```

Preset chasse aux tokens :

```yaml
goal:
  super battle mode -all clears-: 0
  time challenge mode -all clears-: 0
  all clears + tokens: 0
  street fighter token: 50
shadaloo_emblems_required:
  25: 50
shadaloo_emblems_available_percentage:
  200: 50
```

## Verification

Avant de generer une seed :

- Verifie l'indentation.
- Garde `game: Manual_SSF2_NaruSnake`.
- Garde toutes les options SSF2 sous `Manual_SSF2_NaruSnake:`.
- Utilise les noms exacts d'items et de locations.
- Valide le YAML avec un verificateur YAML ou la page de verification Archipelago.

