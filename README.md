# Travail académique

Ce projet a été réalisé dans le cadre du cours **B2 – UE19 : Gestion de la sécurité opérationnelle** à HELMo.
Responsable de cette UE : FORAMITTI Laurent
Laboratoire dispensé par : COLLIN Anne-Sophie

# Générateur d'UUID

Petite application en ligne de commande qui génère des UUID à l'aide de l'API publique [UUIDTools](https://uuidtools.com/). Elle utilise la bibliothèque Python `requests` pour envoyer les requêtes HTTP.

## Fonctionnalités

- Génération de 1 à 20 UUID par requête.
- Validation du nombre saisi.
- Possibilité d'effectuer plusieurs générations pendant la même session.
- Gestion des erreurs réseau et des réponses inattendues de l'API.

## Prérequis

- Python 3.10 ou supérieur.
- Une connexion Internet.

## Installation

Clonez le dépôt, puis installez la dépendance :

```bash
git clone https://github.com/Nathanael1109/ue19-lab-05.git
cd ue19-lab-05
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Sous Windows, activez l'environnement avec `.venv\Scripts\activate`.

## Lancement

```bash
python app.py
```

Saisissez un nombre de 1 à 20. Après l'affichage des UUID, répondez `o` pour en générer d'autres ou toute autre réponse pour quitter.

## Exécution avec Docker

Construisez l'image depuis le dossier du projet :

```bash
docker build -t ue19-lab-05 .
```

Lancez le conteneur en mode interactif pour pouvoir répondre aux invites :

```bash
docker run --rm -it ue19-lab-05
```

## API utilisée

L'application appelle l'endpoint `https://uuidtools.com/api/generate/v1/count/{nombre}`. Il ne nécessite pas de clé API. La requête utilise un délai maximal de 10 secondes ; en cas d'erreur, un message est affiché et l'application revient à la saisie.
