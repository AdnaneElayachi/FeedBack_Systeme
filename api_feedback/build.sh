#!/usr/bin/env bash
set -o errexit  # Arrêter le script en cas d'erreur

# Collecte des fichiers statiques
python manage.py collectstatic --noinput

# Exécution des migrations
python manage.py migrate
