# Manual Archipelago pour Super Street Fighter II

## Bienvenue !
Bienvenue dans le dépôt de l'intégration Manual Archipelago pour **Super Street Fighter II**.
Ce projet communautaire relie les objectifs et les objets de progression de SSF2 au réseau multiworld Archipelago.

Le manual cible actuellement la version SNES de **Super Street Fighter II**. D'autres versions pourront être étudiées plus tard, car certains modes et certains checks peuvent changer selon les versions.

## Statut du projet
Le projet passe en **Version 1.0.0** avec la base actuelle de Manual Archipelago.
Les données de jeu restent centrées sur SSF2, tandis que la structure du package, le client, les hooks, la gestion des tokens, le template YAML et la documentation ont été remis à jour pour la release.

## Fonctionnalités actuelles
- **Super Battle Mode - ALL CLEARS**
  Terminer le mode Super Battle avec tous les personnages.
- **Time Challenge Mode - ALL CLEARS**
  Vaincre tous les adversaires en mode Time Challenge.
- **Street Fighter Token**
  Collecter les Shadaloo Emblems comme objectif token.
- **ALL CLEARS + TOKENS**
  Terminer tous les objectifs de clear et récupérer les Shadaloo Emblems requis.

---

## Notes de version

### Version 1.0.0 - Release Update

**Mise à jour de la base Manual**
- Synchronisation du package source avec la base stable récente de Manual Archipelago (`manual_stable_20260319`).
- Mise à jour des fichiers coeur de Manual pour le chargement des données, la création des items, les règles, les régions, les options, la validation, les helpers et le client.
- Ajout de `container.py` pour le support moderne des fichiers `.apmanual` en conteneur zip.
- Sauvegarde et relecture de `categories.json` dans les fichiers `.apmanual`, avec un fallback pour les anciens fichiers qui ne contiennent pas encore les catégories.
- Ajout de `data/events.json` vide pour préparer le projet au système d'events actuel de Manual.
- Ajout du package de tests stable dans `manual_ssf2_narusnake/test/`.
- Mise à jour de la base du client Manual avec le support tracker récent, les options client, le tri des items/locations, le rafraîchissement de recherche, l'interface DeathLink et la lecture moderne des `.apmanual`.

**Hooks et logique de génération SSF2**
- Ajout de la logique spécifique SSF2 pour le token `Shadaloo Emblem`.
- Les objectifs token ajoutent maintenant les Shadaloo Emblems au pool ; les objectifs sans token les retirent du pool.
- Ajout du réglage `shadaloo_emblems_required` pour choisir le nombre de tokens requis.
- Ajout du réglage `shadaloo_emblems_available_percentage` pour choisir le pourcentage de tokens disponibles.
- Les Shadaloo Emblems en trop par rapport au nombre requis sont classés en `useful` plutôt qu'en progression.
- Ajout d'un hook de catégorie `Filler`. Quand les vrais fillers seront ajoutés, le world pourra choisir dans cette catégorie ; en attendant, il retombe sur le filler défini par le jeu.
- Ajout et traduction en anglais des items actuellement présents dans la catégorie `Filler`.
- Ajout du forçage automatique des options nécessaires selon l'objectif choisi.
- Support du forçage de `Super_Battle`, `CPU_Time_Challenge` et `Token` quand l'objectif sélectionné en dépend.
- Ajout de `sort-key` stables via `hooks/Data.py` pour conserver l'ordre voulu des locations dans le client Manual.

**Options, catégories et YAML**
- Ajout des options `Super_Battle` et `CPU_Time_Challenge`.
- Retrait du toggle YAML public `Token` et conservation d'une logique de placement des tokens geree par les besoins en `Shadaloo Emblem`.
- Clarification du comportement de `Special_Moves` : d?sactiver cette option retire les items de coups sp?ciaux du pool, mais les checks de coups sp?ciaux restent disponibles car les coups peuvent ?tre utilis?s librement sans restriction d'item.
- Ajout des r?glages d'objectif `shadaloo_emblems_required` et `shadaloo_emblems_available_percentage`.
- Ajout d'aliases d'objectifs pour rendre le YAML plus propre.
- Branchement des catégories pour les checks Super Battle, les checks Time Challenge, les items CPU Time Challenge, les Special Moves, la Difficulty, les Tokens et les futurs fillers.
- Harmonisation des noms de personnages dans les items, locations, catégories et `requires` avec l'écriture canonique des items : `E.Honda`, `M.Bison`, `T.Hawk` et `Chun-Li`.
- Réécriture de `Manual_SSF2_NaruSnake.yaml` dans le style du template Tekken 2.
- Mise à jour du template YAML pour Archipelago `0.6.7`.
- Ajout de `random`, `random-low`, `random-high` et `random-range-*` pour les options numériques.
- Ajout de `plando_items` au template YAML.

**Documentation**
- Mise à jour du README pour la release 1.0.0.
- Ajout de cette version française dans `manual_ssf2_narusnake/docs/README_FR.md`.
- Ajout d'un guide YAML anglais dans `manual_ssf2_narusnake/docs/guide.md`.
- Ajout d'un guide YAML français dans `manual_ssf2_narusnake/docs/guide_fr.md`.
- Les guides expliquent les poids YAML, les valeurs random, les checks, les modes de jeu, les goals, les réglages de tokens Shadaloo Emblem, les noms exacts d'items/locations et des presets d'exemple.

**Notes pour cette release**
- Des items dédiés sont actuellement présents dans la catégorie `Filler`. Le hook peut utiliser cette catégorie et retombe toujours sur le filler défini par le jeu si la catégorie redevient vide plus tard.
- Il faut reconstruire l'`.apworld` après modification des sources avant de distribuer une release.

---

### Version 0.8.0 - New Logic Update
- Certaines catégories sont de nouveau visibles dans le client via `categories.json`.
- Refonte de la logique pour permettre plusieurs challenges en mode Time Challenge.
- Les checks Time Challenge demandent maintenant le personnage CPU correspondant quand nécessaire.
- Modification de la syntaxe de tous les champs `requires`.
- Ajout de la catégorie de checks **Stage** et de ses checks associés.
- Ajout de checks **First Attack** pour chaque personnage.
- Ajout de sous-catégories pour les coups spéciaux dans `items.json`.
- Ajout de checks liés aux coups spéciaux.
- Les coups spéciaux sont maintenant des items de progression.
- Tous les coups spéciaux apparaissent dans la catégorie **Special Moves** dans le client.
- Ajout de checks supplémentaires dans la catégorie **Special Moves**.

---

### Version 0.7.1 - YAML Update
Changements depuis la 0.7.0 :
- Migration vers la base instable d'Archipelago Manual.
- Retrait de **Difficulty** de la configuration du pool d'items.
- Retrait de **Special Moves** de la configuration du pool d'items.

---

### Version 0.6.0
- Ajout des coups spéciaux au pool d'items.

---

### Version 0.5.1
- Correction de problèmes liés à la migration.

---

### Version 0.5.0
- Migration vers la nouvelle base Archipelago Manual.

---

### Version 0.4.1 - PopTracker Updates
- PopTracker : ajout d'items et de locations manquants.

---

### Version 0.4.0 - PopTracker Beta
- Introduction de PopTracker en beta avec support des items et locations.
- Début du travail sur l'intégration auto-tracker.

---

### Version 0.3.3
- Renommage des checks de combats de personnages pour des spoiler logs plus clairs et un pool d'items plus propre.
- Augmentation du nombre de tokens à 25.

---

### Version 0.3.2
- Réorganisation des noms de checks pour commencer par le nom du joueur.
- Ajout de trois checks bonus sans demander de perfect score.

---

### Version 0.3.1
**Suppressions**
- Suppression de trois anciens checks après la recatégorisation des personnages.

**Ajouts**
- Création d'une nouvelle catégorie **Special**.
- Ajout de trois checks de remplacement.

---

### Version 0.3.0
**Corrections**
- Correction du titre de catégorie **CPU Time Challenge**.

**Ajouts**
- Ajout de catégories YAML flexibles pour la création des seeds.
- Introduction d'une catégorie token dans `game.json` pour permettre la suppression des tokens.
- Mise en place de checks pour les combats de personnages, les stages bonus et des challenges inspirés du lore.

**Problèmes connus**
- Pas encore de tests multiworld ; certains cas limites peuvent rester.

---

### Version 0.2.0
**Ajouts**
- Ajout des checks **Beat Ryu with Ken** et **Beat Ken with Ryu**.
- Renommage de **Beat the Game** en **Super Battle Mode**.
- Renommage de **Get perfect** en **Get Perfect Round**.
- Ajout de checks pour trois stages bonus en Super Battle Mode.
- Introduction des catégories **Game Mode** et **CPU Time Challenge**.
- Renommage de plusieurs items de catégorie personnage.
- Renommage de **Fun** en **Challenge** et **Defeated** en **Defeated in Super Battle Mode**.
- Ajout des checks **Defeated in Time Challenge**.
- Mise à jour des objectifs vers **Super Battle Mode - ALL CLEARS**, **Time Challenge Mode - ALL CLEARS** et **ALL CLEARS + TOKENS**.
- Randomisation des items de départ pour Game Mode et CPU Time Challenge.
- Augmentation du nombre de tokens à 20.

**Bug connu**
- La génération des checks challenge était encore trop liée au Super Battle et nécessitait un meilleur support du Time Challenge.

---

### Version 0.1.0
- Suppression de l'ancien objectif **Character Battles**.
- Ajout de l'objectif et de l'item Street Fighter token.
- Changement du filler en **Bandage**.
- Ajout de plusieurs nouveaux checks.

---

### Version 0.0.1
- Première version alpha avec les fonctionnalités de base.

---

## Roadmap
- **Revue des items filler** : vérifier, remplacer ou compléter la liste d'items dédiée à la catégorie `Filler` si besoin.
- **Paramètres de difficulté** : continuer à affiner les restrictions de difficulté par seed.
- **Modes de jeu supplémentaires** : ajouter de nouveaux modes et leurs checks quand la version du jeu le permet.
- **Nouveaux objectifs** : diversifier les styles de jeu avec de nouvelles conditions de victoire.
- **Autres versions du jeu** : explorer SSF2 Turbo, les versions arcade et plus encore.

---

## Contribution
Les retours et contributions sont bienvenus.
- Signaler des bugs ou proposer des idées via les issues GitHub.
- Proposer des PR pour des corrections ou optimisations.
- Améliorer la documentation ou ajouter de nouveaux guides.

---

## Remerciements
Merci à toutes les personnes qui ont contribué jusqu'ici, en particulier les modérateurs Discord **Seafo**, **Garbo** et **RoobyRoo** pour l'aide au debug et les retours.

---

## Contact
Questions, streams ou bugs ? Passez par le Discord Archipelago ou ouvrez une issue sur GitHub.
