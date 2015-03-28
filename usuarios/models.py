from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Usuario(User):
    telefono = models.PositiveIntegerField(default=0, blank=True)
    cedula = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=50, null=False, blank=True)

    def __unicode__(self):
        return self.nombre+str(self.codigo)

    def get_absolute_url(self):
        return reverse('editar_usuario', kwargs={'pk': self.pk})