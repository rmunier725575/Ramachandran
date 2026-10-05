# Projet Clustering PDB

## 1. Organisation du projet

Le projet est organisé en trois groupes. Chaque groupe travaille sur une branche dédiée.

| Branche   | Travail                      |
| --------- | ---------------------------- |
| `main`    | Branche principale du projet |
| `group-1` | Atom / Amino Acid            |
| `group-2` | PDB Structure                |
| `group-3` | Point                        |

Les branches `group-1`, `group-2` et `group-3` seront créées au début du projet.

### Groupe 1 — Atom / Amino Acid

Branche :

```text
group-1
```

Ce groupe est responsable des classes et fonctionnalités liées aux atomes et aux acides aminés.

Travail à réaliser :

* récupération des données ;
* préparation des données ;
* représentation des atomes et des acides aminés ;
* features nécessaires ;
* intégration avec les autres parties du projet.

### Groupe 2 — PDB Structure

Branche :

```text
group-2
```

Ce groupe est responsable de la lecture et de la représentation des structures PDB.

Travail à réaliser :

* lecture des fichiers PDB ;
* préparation des données ;
* représentation d'une structure PDB ;
* calcul et gestion des données nécessaires au projet ;
* intégration avec les autres parties du projet.

### Groupe 3 — Point

Branche :

```text
group-3
```

Ce groupe est responsable de la représentation des données sous forme de points et de leur utilisation pour le clustering.

Travail à réaliser :

* préparation des points ;
* représentation des points ;
* K-Means ;
* DBSCAN ;
* résultats et visualisations.

## 2. Organisation des branches

Chaque groupe travaille uniquement sur sa branche.

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

La branche `main` contient la version principale du projet et ne doit pas être modifiée directement.

Lorsque le travail d'un groupe est terminé, une Pull Request / Merge Request peut être créée afin d'intégrer les modifications dans `main`.

---

# 3. Configuration de Git

Cette configuration est à faire une seule fois sur chaque machine.

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "ton@email.com"
```

Pour vérifier la configuration :

```bash
git config --list
```

**Important :** utiliser le même email que celui associé à votre compte GitHub/GitLab afin que vos commits soient correctement attribués.

---

# 4. Initialiser ou cloner le dépôt

### Nouveau projet local

```bash
git init
git remote add origin <url-du-repo>
```

### Cloner un projet existant

```bash
git clone <url-du-repo>
```

Après le clonage, entrer dans le dossier du projet :

```bash
cd <nom-du-projet>
```

### Lier une branche locale à une branche distante

Si nécessaire :

```bash
git branch --set-upstream-to=origin/Projetstage Projetstage
```

---

# 5. Choisir sa branche

Après avoir cloné le projet, chaque membre doit se placer sur la branche de son groupe.

### Groupe 1

```bash
git checkout group-1
```

### Groupe 2

```bash
git checkout group-2
```

### Groupe 3

```bash
git checkout group-3
```

Pour vérifier la branche actuelle :

```bash
git branch
```

La branche active est indiquée avec `*`.

---

# 6. Workflow quotidien

À chaque session de travail, suivre ce principe :

```text
git pull
   ↓
travail
   ↓
git add
   ↓
git commit
   ↓
git push
```

### 1. Récupérer les modifications

Toujours commencer par récupérer les dernières modifications de la branche :

```bash
git pull
```

### 2. Ajouter les fichiers modifiés

Pour ajouter tous les fichiers :

```bash
git add .
```

Pour ajouter un fichier précis :

```bash
git add mon_fichier.py
```

### 3. Créer un commit

```bash
git commit -m "Description de la modification"
```

Le message doit être court et suffisamment clair pour comprendre la modification.

Exemple :

```bash
git commit -m "Ajout du calcul des coordonnées"
```

Éviter les messages trop vagues comme :

```bash
git commit -m "modif"
```

### 4. Envoyer les modifications

```bash
git push
```

---

# 7. Gestion des branches

### Créer une branche

```bash
git checkout -b ma_branche
```

### Changer de branche

```bash
git checkout ma_branche
```

### Envoyer une nouvelle branche sur le dépôt distant

```bash
git push -u origin ma_branche
```

### Voir toutes les branches

```bash
git branch -a
```

**Convention :** une branche doit correspondre à une fonctionnalité ou à une partie clairement identifiée du projet.

Exemples :

```text
feature/calcul-angle
feature/lecture-pdb
fix/calcul-distance
```

---

# 8. Règles importantes

* Chaque groupe travaille sur sa propre branche.
* Ne pas travailler directement sur `main`.
* Faire un `git pull` avant de commencer à travailler.
* Faire des commits réguliers.
* Utiliser des messages de commit clairs.
* Faire un `git push` régulièrement pour sauvegarder son travail.
* Vérifier sa branche avant de modifier le projet.
* Une Pull Request / Merge Request doit être utilisée pour intégrer le travail dans `main`.

## Structure finale

```text
Projet Clustering PDB
│
├── main
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

Les noms des branches et la répartition des groupes pourront être modifiés si l'organisation du projet évolue.
