from django.test import TestCase
from clientes.models import Cliente
from flujos.models import Flujos
from miembros.models import Miembro
from proyectos.models import Proyecto
from sprint.models import Sprint
from us.models import us
from django.utils import timezone
from django.core.urlresolvers import reverse
from us.forms import usForm
import datetime

# models test
from usuarios.models import Usuario


class Test_us(TestCase):

    def create_us(self, nombre, valor_de_negocio, prioridad, valor_tecnico, historial, duracion_horas, sprint , flujo, responsable, proyecto):
        return us.objects.create(nombre=nombre, valor_de_negocio =valor_de_negocio, prioridad = prioridad, valor_tecnico=valor_tecnico, historial = historial, duracion_horas = duracion_horas,sprint=sprint,flujo=flujo,responsable=responsable,proyecto=proyecto)

    def crear_usuario(self, username='alforro', first_name= 'alvaro', last_name='test', cedula='4617510', email='alfa.alvaro.rodriguez@gmail.com',password='alforro', is_superuser=False):
            return Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password, is_superuser=is_superuser)

    def crear_cliente(self, username='cliente', first_name= 'mengano', last_name='test', cedula='4617', email='alfa.alvaro.rodriguez@gmail.com',password='alforro'):
            return Cliente.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email,password= password)

    def crear_miembro(self, proyecto, usuario):
        return Miembro.objects.create(proyecto=proyecto, usuario=usuario, horas_por_dia=5)

    def test_us_creation(self):
        cliente = self.crear_cliente()
        lider = self.crear_usuario()
        proyecto= Proyecto.objects.create(nombre='ProyectoPrueba', lider_proyecto=lider, cliente=cliente, descripcion='Descripcion del proyecto de prueba' , fecha_creacion= datetime.date.today(), fecha_inicio=datetime.date.today(), fecha_fin=datetime.date.today(), estado='PEN', observaciones='esta es la observacion del test')
        proyecto.save()
        responsable = self.crear_miembro(proyecto, lider)
        sprint= Sprint.objects.create(nombre="PruebaTestSprint", proyecto=proyecto, descripcion="Pequenha descripcion para el test de Sprint", duracion_dias=12, observaciones= "no hay observaciones")
        flujo = Flujos.objects.create(nombre='Flujo de Prueba', descripcion='No existen comentarios', fecha_hora_creacion= datetime.date.today(), proyecto=proyecto)
        u = self.create_us(nombre="us2", valor_tecnico=2,valor_de_negocio=1, prioridad=3,historial='hacer lalala', duracion_horas=25,sprint=sprint,flujo=flujo,responsable=responsable,proyecto=proyecto)
        self.assertTrue(isinstance(u, us))
        self.assertEqual(u.__unicode__(), u.nombre)