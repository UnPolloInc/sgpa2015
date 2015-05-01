from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


from django.db import models
from django.utils.datetime_safe import date
from clientes.models import Cliente
from usuarios.models import Usuario
#from sprint.models import Sprint
from proyectos.models import Proyecto

class Sprint(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    #lider_proyecto = models.ForeignKey(Usuario, related_name='Lider')
    #cliente = models.ForeignKey(Cliente, related_name='Cliente')
    #proyecto = models.ForeignKey(Proyecto, related_name= 'Proyecto', null=True)
    proyecto = models.ForeignKey(Proyecto,help_text='Nombre del proyecto', max_length=100)
    descripcion = models.TextField(max_length=140, help_text='Introduzca una breve resenha del sprint', null=True)
    duracion_dias = models.IntegerField(default=0, help_text='Duracion en dias', max_length=2)
    #fecha_creacion = models.DateField(default=date.today(),auto_now_add=True, help_text='Fecha de creacion del Proyecto', null=True)
    #fecha_inicio = models.DateField(help_text='Fecha de inicio del Proyecto', null=True)
    #fecha_fin = models.DateField(help_text='Fecha estimada de finalizacion', null=True)
    #estado = models.CharField(max_length=3, choices=opciones_estado, default='PEN', help_text='Estado del proyecto')
    observaciones = models.TextField(max_length=140, null=True, default='No hay observaciones')


    def __unicode__(self):
        return self.nombre
