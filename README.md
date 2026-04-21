# Portfolio

Application web de portfolio personnel développée avec Django.

Le projet présente plusieurs pages statiques pour mettre en avant un profil, des expériences, des compétences et d'autres rubriques personnelles.

## Aperçu

Ce projet contient actuellement :

- une application Django nommée `apps.core`
- un routage principal via `config`
- des pages HTML rendues côté serveur
- une base SQLite locale
- une configuration d'environnement via fichier `.env`

## Pages disponibles

Les routes actuellement exposées sont les suivantes :

- `/` : accueil
- `/a-propos/` : à propos
- `/experiences/` : expériences
- `/competences/` : compétences
- `/loisirs/` : loisirs
- `/hobbies/` : hobbies
- `/certificats/` : certificats
- `/formations/` : formations

## Stack technique

- Python
- Django 6.0.4
- SQLite
- `django-environ`
- Pillow

## Prérequis

Avant de lancer le projet, assurez-vous d'avoir :

- Python installé
- `pip` disponible
- un environnement virtuel recommandé

## Installation

### 1. Cloner le projet

```powershell et bash
git clone <url-du-depot>
cd Portfolio
```

### 2. Créer et activer un environnement virtuel

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

```bash
python -m venv venv
source .ven/bin/activate
```

### 3. Installer les dépendances

```powershell et bash
pip install -r requirements.txt
```

## Configuration

Le projet lit ses variables d'environnement depuis le fichier `portfolio/.env`.

Créez ce fichier si nécessaire avec au minimum :

```env
DJANGO_SECRET_KEY=votre-cle-secrete-django
```

## Lancer le projet en local

Depuis le dossier `portfolio/` :

```powershell et bash
cd portfolio
python manage.py migrate
python manage.py runserver
```

Puis ouvrez votre navigateur à l'adresse suivante :

```text
http://127.0.0.1:8000/
```

## Vérifications utiles

Contrôle de configuration Django :

```powershell
cd portfolio
python manage.py check
```

Lancer les tests :

```powershell
cd portfolio
python manage.py test
```

## Structure du projet

```text
Portfolio/
├── README.md
├── requirements.txt
└── portfolio/
	├── manage.py
	├── db.sqlite3
	├── apps/
	│   └── core/
	│       ├── models.py
	│       ├── urls.py
	│       ├── views.py
	│       ├── templates/
	│       │   └── core/
	│       └── tests/
	├── config/
	│   ├── urls.py
	│   └── settings/
	│       ├── base.py
	│       └── local.py
	├── static/
	├── media/
	└── templates/
		└── base.html
```

## État actuel du projet

- les vues existantes rendent principalement des pages statiques
- les modèles sont encore des structures de base à compléter
- la suite de tests est présente mais ne contient pas encore de cas de test exécutés
- les dossiers `static/css` et `static/images` sont prêts à recevoir les ressources front-end

## Auteur
Jacques-a Sidney
Portfolio personnel de présentation.
