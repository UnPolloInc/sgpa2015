#encoding:utf-8
from django.db import models
from django.utils.datetime_safe import date
from django.utils import timezone
from proyectos.models import Proyecto
from usuarios.models import Usuario
# Create your models here.

class Flujos(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=140, help_text='Introduzca alguna descripción adicional acerca del flujo', null=True)
    fecha_hora_creacion = models.DateTimeField(default=date.today(), auto_now_add=True, help_text='Hora de creacion del Flujo', null=True)
    proyecto = models.ForeignKey(Proyecto)


    def __unicode__(self):
        return self.nombre

class Actividad(models.Model):
    """
    opciones_estado = (
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done'),
    )
        estado = models.CharField(max_length=3, choices=opciones_estado, default='PEN', help_text='Estado del flujo')
    """

    nombre = models.CharField(max_length=100, unique=True)
    orden = models.PositiveIntegerField(help_text='Introduzca el orden correspondiente de la actividad')
    flujo = models.ForeignKey(Flujos)