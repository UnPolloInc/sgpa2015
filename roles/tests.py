from django.test import TestCase
from django.contrib.auth.models import User,Group

# Create your tests here.
class test_content(TestCase):
    def setUp(self):
        # se inicializa un Group de django

        g1= Group.objects.create(name="Rol1")


    def test_rol_nombre(self):
        grp = Group.objects.get(name = "Rol1")
        print "Test 1. Imprimiendo nombre del Rol --> %s" %(grp.name)
