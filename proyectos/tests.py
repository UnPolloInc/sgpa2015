from django.test import TestCase

# Create your tests here.
import unittest
from django.test import Client
from django.utils.datetime_safe import date
from clientes.models import Cliente
from proyectos.forms import ProyectoForm
from proyectos.models import Proyecto
from usuarios.models import Usuario


class SimpleTest(unittest.TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_lista(self):
        # Issue a GET request.
        response = self.client.get('/proyectos/', follow=True)

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
