#encoding:utf-8
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.datetime_safe import date
from django.utils import timezone
from flujos.models import Flujos
from sprint.models import Sprint
from usuarios.models import Usuario
# Create your models here.

class us(models.Model):

    nombre = models.CharField(max_length=100, unique=True)
    valor_de_negocio = models.IntegerField(max_length=2, help_text='Introduzca un valor de negocio (1 al 10)', null = False)
    prioridad = models.IntegerField(max_length=3, help_text= 'Introduzca alguna prioridad para el User Stories', null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    valor_tecnico = models.IntegerField(max_length=2, help_text='Introduzca un valor técnico al User Stories', null = False)
    historial = models.TextField(max_length=500, help_text= 'Introduzca la descripción del historial', null = False)
    duracion_horas = models.CharField(max_length=4, help_text='Introduzca la duración en horas del User Stories', null=True)
    sprint = models.ForeignKey(Sprint, null=True)
    flujo = models.ForeignKey(Flujos, null=True)

    def __unicode__(self):
        return self.nombre

"""
    class Meta:
        permissions = (
            ('consultar_Proyecto', 'Puede consultar proyecto'),
            ('consultar_Usuarios_Vinculados', 'Puede consultar usuarios vinculados'),
        )
"""
