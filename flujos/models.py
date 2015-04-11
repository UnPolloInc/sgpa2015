#encoding:utf-8
from django.db import models
from django.utils.datetime_safe import date
from django.utils import timezone
from usuarios.models import Usuario
# Create your models here.

class Flujos(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=140, help_text='Introduzca alguna descripción adicional acerca del flujo', null=True)
    fecha_hora_creacion = models.DateTimeField(default=date.today(), auto_now_add=True, help_text='Hora de creacion del Flujo', null=True)



    def __unicode__(self):
        return self.nombre
"""
    class Meta:
        permissions = (
            ('consultar_Proyecto', 'Puede consultar proyecto'),
            ('consultar_Usuarios_Vinculados', 'Puede consultar usuarios vinculados'),
        )
"""

