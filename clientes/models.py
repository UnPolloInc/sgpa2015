from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Cliente(User):
    """
    *Modelo para cliente con campos extras:*
        + *telefono*: telefono del usuario
        + *cedula*: documento de identidad del usuario
        + *direccion*: direccion del usuario
    """
    telefono = models.PositiveIntegerField(default=0, blank=True)
    cedula = models.PositiveIntegerField(default=0)
    direccion = models.CharField(max_length=50, null=False, blank=True)

    def __unicode__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('editar_cliente', kwargs={'pk': self.pk})