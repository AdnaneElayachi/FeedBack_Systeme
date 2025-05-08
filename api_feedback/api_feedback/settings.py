
# import os
# from pathlib import Path
# from decouple import config


# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = config('DJANGO_SECRET_KEY', default='fallback-secret-key')

# # ALLOWED_HOSTS = ['127.0.0.1', 'localhost']  # Ajoutez vos domaines en production


# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
#     'https://feedback-systeme.onrender.com',
# ]


# DEBUG = False  # Changez à False en production



# INSTALLED_APPS = [
#     'admin_interface',
#     'colorfield', 
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'admin_tools.theming',
#     'admin_tools.menu',
#     'admin_tools.dashboard',
#     'api_feedback_apps',
#     'rest_framework',

    
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'corsheaders.middleware.CorsMiddleware',

#       'whitenoise.middleware.WhiteNoiseMiddleware',
# ]


# ROOT_URLCONF = 'api_feedback.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / "templates"],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'api_feedback.wsgi.application'












# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # import dj_database_url
# # from decouple import config


# # DATABASES = {
# #     'default': dj_database_url.config(
# #         default='DATABASE_URL=postgres://internal_db_4s4y_user:XCEPt1jj8aOGXbYIR0CRG8qjxnvZc5rK@dpg-d0dlc1juibrs73cu5n7g-a.oregon-postgres.render.com:5432/internal_db_4s4y',
# #         conn_max_age=600,
# #         ssl_require=True,
# #     )
# # }













# REST_FRAMEWORK = {
#     'DEFAULT_RENDERER_CLASSES': [
#         'rest_framework.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ],
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
#     {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = 'static/'
# # STATIC_ROOT = BASE_DIR / "staticfiles"
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CORS_ALLOW_ALL_ORIGINS = True

# MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE

# SWAGGER_USE_COMPAT_RENDERERS = False





import os
from pathlib import Path
from decouple import config
import dj_database_url

ROOT_URLCONF = 'api_feedback.urls'

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY', default='fallback-secret-key')

# DEBUG = config('DEBUG', default=False, cast=bool)
DEBUG = True


# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
#     'feedback-systeme.onrender.com',
# ]

import os

# Vérifier si la variable d'environnement est définie
django_production = os.environ.get('DJANGO_PRODUCTION', 'False')  # 'False' est la valeur par défaut



# if django_production == 'True':
#     ALLOWED_HOSTS = ['feedback-systeme.onrender.com']
# else:
#     ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# # Debug: Afficher la valeur de ALLOWED_HOSTS
# print("ALLOWED_HOSTS:", ALLOWED_HOSTS)



ALLOWED_HOSTS = [
    'feedback-systeme.onrender.com',
   '127.0.0.1'
]

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',

     'admin_tools', 
     'admin_tools.dashboard',
     'admin_tools.theming',
    'admin_tools.menu',
    

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

   
    'api_feedback_apps',

    'rest_framework',
    'corsheaders',
]




CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "https://feedback-systeme.onrender.com",
]







MIDDLEWARE = [
    'django.middleware.locale.LocaleMiddleware',  # Ajoutez ceci

    'corsheaders.middleware.CorsMiddleware',  # doit être en premier
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}





STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'






TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        # APP_DIRS ne doit PAS être présent quand on utilise loaders
        'OPTIONS': {
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


