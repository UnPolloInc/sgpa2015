from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


from django.db import models
from django.utils.datetime_safe import date
from clientes.models import Cliente
from usuarios.models import Usuario
#from sprint.models import Sprint
from proyectos.models import Proyecto
from django.core.exceptions import ValidationError


class Estado(models.Model):
    estado = models.CharField(max_length=25)

    def __unicode__(self):
        return self.estado



class Sprint(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    proyecto = models.ForeignKey(Proyecto,help_text='Nombre del proyecto', max_length=100)
    descripcion = models.TextField(max_length=140, help_text='Introduzca una breve resenha del sprint', null=True)
    duracion_dias = models.IntegerField(default=0, help_text='Duracion en dias', max_length=2)
    observaciones = models.TextField(max_length=140, null=True, default='No hay observaciones')
    estado = models.ForeignKey(Estado, null=True, blank=True)
    capacidadTotal = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return self.nombre





