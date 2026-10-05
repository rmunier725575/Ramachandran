# Projet Clustering PDB

## 3. Configuration de Git

> À faire une seule fois sur chaque machine.

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "ton@email.com"
```

Vérifier la configuration :

```bash
git config --list
```

> **Important :** utilise le même email que ton compte GitHub/GitLab pour que tes commits te soient bien attribués.

---

## 4. Initialiser ou cloner un dépôt

**Nouveau projet local :**

```bash
git init
git remote add origin <url-du-repo>
```

**Cloner un projet existant :**

```bash
git clone <url-du-repo>
```

**Lier la branche locale à la branche distante :**

```bash
git branch --set-upstream-to=origin/Projetstage Projetstage
```

---

## 5. Workflow quotidien

> Répète ces étapes chaque fois que tu travailles sur le projet.

```
git pull  →  ... travail ...  →  git add .  →  git commit -m "..."  →  git push
```

### 1 — Récupérer les modifications distantes (toujours commencer par là)

```bash
git pull
```

### 2 — Ajouter les fichiers modifiés

```bash
git add .               # Ajoute tous les fichiers modifiés
git add mon_fichier.py  # Ajoute un fichier précis
```

### 3 — Committer avec un message clair

```bash
git commit -m "Description courte de ce que tu as fait"
```

> **Bonne pratique :** le message de commit doit expliquer le *pourquoi*, pas juste le *quoi*.  
> Ex: `"Ajout validation formulaire login"` plutôt que `"modif"`.

### 4 — Envoyer vers le dépôt distant

```bash
git push
```

---

## 6. Gestion des branches

> Les branches permettent de travailler sur une fonctionnalité sans toucher au code principal.

**Créer une branche :**

```bash
git checkout -b ma_branche
```

**Changer de branche :**

```bash
git checkout ma_branche
```

**Envoyer une nouvelle branche sur le dépôt distant :**

```bash
git push -u origin ma_branche
```

**Voir toutes les branches :**

```bash
git branch -a
```

> **Convention :** une branche par fonctionnalité ou par ticket.  
> Ex: `feature/ajout-login`, `fix/bug-calcul`

---


## Organisation des branches

Chaque groupe travaille sur une branche dédiée.

| Branche   | Travail                      |
| --------- | ---------------------------- |
| `main`    | Branche principale du projet |
| `group-1` | Atom / Amino Acid            |
| `group-2` | PDB Structure                |
| `group-3` | Point                        |

Les branches `group-*` seront créées au début du projet.

## Travail de chaque groupe

### Group 1 — Atom / Amino Acid

Branche :

```text
group-1
```

Ce groupe travaille sur la représentation des données au niveau des atomes et/ou des acides aminés.

Il devra notamment mettre en place :

* la récupération des données ;
* la préparation des données ;
* les features utilisées ;
* K-Means ;
* DBSCAN ;
* les résultats et visualisations.

### Group 2 — PDB Structure

Branche :

```text
group-2
```

Ce groupe travaille sur la représentation d'une structure PDB dans son ensemble.

Il devra notamment mettre en place :

* la récupération des données ;
* la préparation des données ;
* les features utilisées ;
* K-Means ;
* DBSCAN ;
* les résultats et visualisations.

### Group 3 — Point

Branche :

```text
group-3
```

Ce groupe travaille sur la représentation des données sous forme de points.

Il devra notamment mettre en place :

* la préparation des points ;
* les features utilisées ;
* K-Means ;
* DBSCAN ;
* les résultats et visualisations.

## Git

Chaque groupe travaille uniquement sur sa branche.

Pour récupérer le projet :

```bash
git clone <repository>
```

Pour se placer sur sa branche :

```bash
git checkout group-1
```

Remplacer `group-1` par la branche de son groupe.

Les modifications doivent être commit sur la branche du groupe :

```bash
git add .
git commit -m "Description de la modification"
git push
```

La branche `main` ne doit pas être modifiée directement.

Une fois le travail terminé, une Pull Request / Merge Request pourra être créée afin d'intégrer le travail dans `main`.

## Organisation finale

```text
main
│
├── group-1
│   └── Atom / Amino Acid
│
├── group-2
│   └── PDB Structure
│
└── group-3
    └── Point
```

Les noms des branches et la répartition des groupes pourront être modifiés lorsque les groupes seront définitivement définis.
