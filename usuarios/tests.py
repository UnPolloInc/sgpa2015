from django.test import TestCase

# Create your tests here.


from usuarios.models import Usuario
from django.core.urlresolvers import reverse

class TestUsuarioView(TestCase):

    def crear_usuario(self, username='alforro', first_name= 'alvaro', last_name='test', cedula='4617510', email='alfa.alvaro.rodriguez@gmail.com',password='alforro', is_superuser=False):
        return Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password, is_superuser=is_superuser)

    def test_crear_usuario(self):
        u = self.crear_usuario()
        #u = "hola"
        self.assertTrue(isinstance(u,Usuario))
        self.assertEqual(u.__unicode__(), u.username)
        print('ejecutando test crear usuario')

    def test_crear_superusuario(self):
        u = Usuario.objects.create_superuser('alforro','alfa.alvaro.rodriguez@gmail.com','alforro')
        self.assertTrue(isinstance(u,Usuario))
        self.assertTrue(u.is_superuser,True)
        self.assertEqual(u.__unicode__(), u.username)
        print('ejecutando test crear superusuario')