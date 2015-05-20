from django.db import models
from roles.models import Rol
from usuarios.models import Usuario
from proyectos.models import Proyecto
# Create your models here.



class Miembro(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    usuario = models.ForeignKey(Usuario)
    horas_por_dia = models.IntegerField(default=0, help_text= 'Horas diarias a trabajar')
    rol = models.ForeignKey(Rol)

    def __unicode__(self):
        return self.usuario.username+self.proyecto.nombre
