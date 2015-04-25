from django.test import TestCase
from us.models import us
from django.utils import timezone
from django.core.urlresolvers import reverse
from us.forms import usForm
# models test

class Test_us(TestCase):

    def create_us(self, nombre="us2", valor_de_negocio =2, prioridad = 1, valor_tecnico=3, historial = 'hacer lalala', duracion_horas = "25"):
        return us.objects.create(nombre=nombre, valor_de_negocio =valor_de_negocio, prioridad = prioridad, valor_tecnico=valor_tecnico, historial = historial, duracion_horas = duracion_horas)

    def test_us_creation(self):
        u = self.create_us()
        self.assertTrue(isinstance(u, us))
        self.assertEqual(u.__unicode__(), u.nombre)