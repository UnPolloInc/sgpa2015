"""
WSGI config for sgap project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
#from sgpa import settings
#from django.core.wsgi import get_wsgi_application
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sgpa.settings")

sys.path.append('/home/chelox/PycharmProjects/sgpa2015')
#sys.path.append('/home/chelox/PycharmProjects/sgpa2015/sgpa')
#path = settings.PATH
#if path not in sys.path:
    #sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE']= 'sgpa.settings'
os.environ.setdefault('LANG', "en_US.UTF-8")
os.environ.setdefault("LC_ALL", "en_US.UTF-8")

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sgpa.settings")
#activate_this='/home/chelox/mysite/proyecto/bin/activate_this.py'
#execfile(activate_this, dict(__file__=activate_this))

#obtenemos la aplicacion
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
