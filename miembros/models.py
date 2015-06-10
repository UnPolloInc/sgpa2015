from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from roles.models import Rol
from usuarios.models import Usuario
from proyectos.models import Proyecto



# Create your models here.



class Miembro(models.Model):
    proyecto = models.ForeignKey(Proyecto)
    usuario = models.ForeignKey(Usuario)
    horas_por_dia = models.IntegerField(max_length=2, default=1, help_text= 'Horas diarias a trabajar', validators=[MinValueValidator(1), MaxValueValidator(12)])

    rol = models.ForeignKey(Rol)

    def __unicode__(self):
        return self.usuario.username

