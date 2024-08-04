"""
Django settings for rdv_project project.

Generated by 'django-admin startproject' using Django 4.2.14.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-f)0^frr8*#8%zengxp8*6&+^6$y9fe4n(++e6@dw97&ajina1@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
SITE = 1

# Ajoutez ces imports en haut du fichier
import os
from django.utils.translation import gettext_lazy as _

# Ajoutez 'appointment' à INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appointment',  # Ajoutez cette ligne
    'django_q',  # Nécessaire pour les tâches en arrière-plan
    # Tiers applications...
    'crispy_forms',
    'crispy_bootstrap5',
    # Vos autres applications...
    'customer',  # mes clients
    'rendezvous2',  # ou 'rendezvous2' selon le nom de votre application
    'rest_framework',
]


# Application definition


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = "rdv_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'rendezvous2'),
            os.path.join(BASE_DIR, 'templates', 'customer'),
            ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "rdv_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Configurez le backend d'e-mail (exemple avec console backend pour le développement)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Ajoutez ces imports en haut du fichier


# Configurez le backend d'e-mail (exemple avec console backend pour le développement)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuration de django-q pour les tâches en arrière-plan
Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default',
}

# Configurations spécifiques à django-appointment
APPOINTMENT_WEBSITE_NAME = 'Votre Nom de Site'
APPOINTMENT_SLOT_DURATION = 30  # durée du créneau en minutes
APPOINTMENT_CONFIRMATION_REQUIRED = True
APPOINTMENT_ALLOW_OVERLAPPING = False
APPOINTMENT_REMINDER_DAYS = 1  # envoyer un rappel 1 jour avant le rendez-vous

# Configuration des langues
LANGUAGES = [
    ('en', _('English')),
    ('fr', _('French')),
    # Ajoutez d'autres langues si nécessaire
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

# Assurez-vous que ces middlewares sont présents

# Configuration des fichiers statiques et media
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Utilisez le modèle utilisateur par défaut de Django
AUTH_USER_MODEL = 'auth.User'

## Crispy Form
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # ou 'bootstrap5' si vous utilisez Bootstrap 5
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"