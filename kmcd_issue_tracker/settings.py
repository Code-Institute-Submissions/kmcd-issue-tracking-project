"""
Django settings for kmcd_issue_tracker project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# import environment variables, if the file exists

if os.path.exists('env.py'):
    import env

# Import dj_database_url which was installed with "pip3 install dj-database-url"

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Lines added for kmcd-issue-tracking-project
# The C9_HOSTNAME wasn't working in settings.py as an ALLOWED_HOST. So, after a 
# chat with a tutor I set up AWSC9_HOST as an environment variable 
# in .bashrc and am using it in settings.py so that I have an environment variable
# rather than a hardcoded url

ALLOWED_HOSTS = [os.environ.get('AWSC9_HOST', 'kmcd-issue-tracker.herokuapp.com')]


# Lines added for kmcd-issue-tracking-project:
# 'django_forms_bootstrap', 'accounts'
# Notice that 'django_forms_bootstrap' has underscores, whereas you install it 
# with hyphens

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap', 
    'accounts',
    'app1_home',
    'app2_user_home',
    'app3_issue_logging',
    'app4_features',
    'app6_cart',
    'app7_checkout',
     'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kmcd_issue_tracker.urls'

# Line added to TEMPLATES for kmcd-issue-tracking-project:
# 'DIRS': [os.path.join(BASE_DIR, 'templates')], This is because there is more 
# than one 'templates' dir and this specifies that all of them could 
# potentially contain templates. This allows us to keep templates separate
# within each app.)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'app6_cart.contexts.cart_contents'
            ],
        },
    },
]

WSGI_APPLICATION = 'kmcd_issue_tracker.wsgi.application'


# Database - sqlite3
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# Database - postgres dj_database_url was installed with 
# "pip3 install dj-database-url" and is imported above
# Get postgres 'DATABASE_URL', if it exists, otherwise use sqlite3 db

if "DATABASE_URL" in os.environ:
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) 
}
else:
    print("Database URL not found. Using SQLite instead.")
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Lines added for kmcd-issue-tracking-project
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailAuth'
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATE_INPUT_FORMATS = [
    '%d/%m/%Y'           # '25/10/06'
    
    ]

DATE_FORMAT = 'j, N  Y'

# Let boto know that it can cach the static files
# Give an expiry date long into the future, our static files are not going to
# expire. Also, they're not age-sensitive.

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
    'CacheControl': 'max-age=94608000',
}

# Name of Storage Bucket we created in S3

AWS_STORAGE_BUCKET_NAME = 'kmcd-issue-tracker'

# S3 region (eu-west-1 = Ireland)

AWS_S3_REGION_NAME = 'eu-west-1'

# AWS Access Key and Secret Key, which will be defined in env.py

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Domain Name
# The domain that we are using - the bucket name will be injected into the '%s'
# i.e. 'kmcd-issue-tracker.s3.amazonaws.com'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME


# Static Files location and storage

# All files under 'static' are static files

STATICFILES_LOCATION = 'static'

# Tell s3 where to store the static files (s3/static)

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = '/static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]


# Media Files
# All files under 'media' are static files

MEDIAFILES_LOCATION = 'media'

# This tells s3 where to store the media files (s3/media)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'


# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
# (The following is what the video has, but it doesnt work. The above MEDIA_URL I found on slack, and it works!!)
MEDIA_URL = '/media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')

# Lines added for kmcd-issue-tracking-project

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# To send a real email:
# TLS = Form of email encryption which is used by gmail

EMAIL_USE_TLS = True

# smtp = Protocol used to send emails

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_PORT = 587

