from django.db import models
from usuarios.models import Usuario
from proyectos.models import Proyecto
# Create your models here.



class Miembro(models.Model):
    proyecto = models.ForeignKey(Proyecto, null=True)
    usuario = models.ForeignKey(Usuario, null=True)


    def __unicode__(self):
       return self.usuario.username