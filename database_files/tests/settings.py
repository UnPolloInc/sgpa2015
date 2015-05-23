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

ROOT_URLCONF = 'database_files.urls'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'database_files',
    'database_files.tests',
]
DEFAULT_FILE_STORAGE = 'database_files.storage.DatabaseStorage'


