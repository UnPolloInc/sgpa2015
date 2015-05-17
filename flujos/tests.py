from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from flujos.models import Flujos
from django.utils.datetime_safe import date
from proyectos.models import Proyecto
from usuarios.models import Usuario
from clientes.models import Cliente

class FlujosTest(TestCase):

    def crear_usuario(self, username='alforro', first_name= 'alvaro', last_name='test', cedula='4617510', email='alfa.alvaro.rodriguez@gmail.com',password='alforro', is_superuser=False):
            return Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password, is_superuser=is_superuser)

    def crear_cliente(self, username='cliente', first_name= 'mengano', last_name='test', cedula='4617', email='alfa.alvaro.rodriguez@gmail.com',password='alforro'):
            return Cliente.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password)



    def test_flujos_creation(self):
        cliente = self.crear_cliente()
        lider = self.crear_usuario()
        lider.save()
        proyecto= Proyecto.objects.create(nombre='ProyectoPrueba', lider_proyecto=lider, cliente=cliente, descripcion='Descripcion del proyecto de prueba' , fecha_creacion= date.today(), fecha_inicio=date.today(), fecha_fin=date.today(), estado='PEN', observaciones='esta es la observacion del test')


        f = Flujos.objects.create(nombre='Flujo de Prueba', descripcion='No existen comentarios', fecha_hora_creacion= date.today(), proyecto=proyecto)
        self.assertTrue(isinstance(f, Flujos))
        self.assertEqual((f.__unicode__()), f.nombre)
        print('Ejecutando test de FLujos')