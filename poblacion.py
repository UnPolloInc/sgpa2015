__author__ = 'chelox'
from usuarios.models import Usuario
from django.contrib.auth.models import User

username='alforro'
first_name= 'alvaro'
last_name='test'
cedula='4617510'
email='alfa.alvaro.rodriguez@gmail.com'
password='alforro'
is_superuser=False
Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email, password= password, is_superuser=is_superuser)
