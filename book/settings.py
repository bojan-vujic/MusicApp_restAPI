"""
Django settings for book project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ad@0!2$j%f-3m3dye&w45vv2xf$s-xao7(0ecyy*cmt%4&&(_p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = [
#   'localhost',
#   '127.0.0.1',
#   #'111.222.333.444',
#   #'mywebsite.example'
# ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_extensions',
    'bootstrap5',
    'widget_tweaks',
    'formtags',
    'main',
    'updates',
    'youtube',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    #'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8000',
    'http://localhost:35241',
    'http://localhost:4200'
)

ROOT_URLCONF = 'book.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, STATIC_DIR, MEDIA_DIR,],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries' : {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'book.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': os.path.join(BASE_DIR, 'oldDB.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    #'django.contrib.auth.hashers.BcryptSHA256PasswordHasher',
    #'django.contrib.auth.hashers.BcryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]

MIN_PASSWORD_LENGHT = 8

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS' : {
            'user_attributes' : ('username', 'email',),
            'max_similarity': 1,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': MIN_PASSWORD_LENGHT,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Stockholm'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# DATETIME_INPUT_FORMATS = [
#     '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
#     '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
#     '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
#     '%Y-%m-%d',              # '2006-10-25'
#     '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
#     '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
#     '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
#     '%m/%d/%Y',              # '10/25/2006'
#     '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
#     '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
#     '%m/%d/%y %H:%M',        # '10/25/06 14:30'
#     '%m/%d/%y',              # '10/25/06'
# ]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_DIR
LOGIN_URL = 'login/'

if os.getcwd() == '/home/bojan':
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')


#YOUTUBE_SEARCH_API_KEY = 'AIzaSyCFI6phHEEG2XmbHDPtwI_Ku1zr8qi6epI'
YOUTUBE_SEARCH_API_KEY = ''

# create key with admin powershell
# mkcert -cert-file cert.pem -key-file key.pem localhost 127.0.0.1

# Run with
# python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
