from django.test import TestCase
from django.utils import timezone
import factory
from usuarios.models import Usuario
from django.test import TestCase

# Create your tests here.

def crear_usuario(self, username='alforro', first_name= 'alvaro', last_name='test', cedula='4617510', email='alfa.alvaro.rodriguez@gmail.com',password='alforro', is_superuser=False):
    return Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password, is_superuser=is_superuser)



class TestAutenticacionViewsMyLogin(TestCase):
    """
        Prueba para la vista autenticacion.views.myLogin.
    """

    un_admin = 'admin'
    pw_admin = 'admin'

    un_unknown_user = 'cualquiera'
    pw_unknown_user = 'cualquiera'

    def setUp(self):
        """
            Crea el usuario 'admin' con contrasena 'admin'
        """
        UsuarioFactory.create()

    def test_login_response(self):
        """
            Prueba de la respuesta de la vista '/login/'
        """

        resp = self.client.get('/login/')
        self.assertEqual(resp.status_code, 200)

    def test_root_response(self):
        """
            Prueba de la respuesta de la vista '' root
        """

        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_login_admin(self):
        """
            Prueba del Logeo del usuario 'admin'
        """

        login = self.client.login(username=self.un_admin, password=self.pw_admin)
        self.assertTrue(login)

    def test_login_unknown_user(self):
        """
            Prueba del Logeo de un usuario no registrado
        """

        login = self.client.login(username=self.un_unknown_user, password=self.pw_unknown_user)
        self.assertFalse(login)