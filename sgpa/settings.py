"""
Django settings for sgap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


DEFAULT_FILE_STORAGE = 'db_file_storage.storage.DatabaseFileStorage'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0mq2*pxruqx=2mb7fztd7lf+nicenx1$uyij!p&uf@n#&hw+tv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'autenticacion',
    'usuarios',
    'proyectos',
    'clientes',
    'flujos',
    'sprint',
    'us',
    'miembros',
    'roles',
    'mensajes',
    'Notificaciones',
    'database_files',
    'djangobower',
    'django_nvd3',
    'db_file_storage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'sgpa.urls'

WSGI_APPLICATION = 'sgpa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sgpa',                      # Or path to database file if using sqlite3.
            # The following settings are not used with sqlite3:
            'USER': 'sgpa',
            'PASSWORD': 'sgpa',
            'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
            'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-PY'

TIME_ZONE = 'America/Asuncion'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT=[os.path.join(BASE_DIR, 'static')]
#STATIC_ROOT='/home/jorge/PycharmProjects/sgpa2015/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)
#para que django pueda encontrar los templates.
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
#BOWER_COMPONENTS_ROOT = '/home/chelox/PycharmProjects/sgpa2015/components'
BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'components')
#BOWER_COMPONENTS_ROOT = str([os.path.join(BASE_DIR, 'components')])
BOWER_INSTALLED_APPS = (
    'd3',
    'nvd3',
)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(
        os.path.dirname(__file__),
        'static/',
    ),
)

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'django.contrib.auth.views.login'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


# Configuracion de mail
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'sgpa2015q06@gmail.com'
EMAIL_HOST_PASSWORD = 'sgpa2015'
EMAIL_PORT = 587

# Para los archivos

MEDIA_ROOT = os.path.join(BASE_DIR, 'userfiles')
MEDIA_URL = '/files/'  # Note they don't have to be identical names
WKHTMLTOPDF_CMD = '/usr/bin/wkhtmltopdf.sh'
WKHTMLTOPDF_CMD_OPTIONS = {
   'quiet':True,
}

# Formato para fechas
DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)