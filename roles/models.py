from django.contrib.auth.models import Group
from django.db import models
# Create your models here.
from proyectos.models import Proyecto


class Rol(Group):
    proyecto = models.ForeignKey(Proyecto)