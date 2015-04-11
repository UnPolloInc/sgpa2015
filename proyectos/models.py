#encoding:utf-8

from django.db import models
from django.utils.datetime_safe import date
from clientes.models import Cliente
from usuarios.models import Usuario
# Create your models here.
class Proyecto(models.Model):
    opciones_estado = (
        ('PEN', 'Pendiente'),
        ('ANU', 'Anulado'),
        ('INI', 'Iniciado'),
        ('FIN', 'Finalizado'), )
    nombre = models.CharField(max_length=100, unique=True)
    lider_proyecto = models.ForeignKey(Usuario, related_name='Lider')
    cliente = models.ForeignKey(Cliente, related_name='Cliente')
    descripcion = models.TextField(max_length=140, help_text='Introduzca una breve reseña del proyecto', null=True)
    fecha_creacion = models.DateField(default=date.today(),auto_now_add=True, help_text='Fecha de creacion del Proyecto', null=True)
    fecha_inicio = models.DateField(help_text='Fecha de inicio del Proyecto', null=True)
    fecha_fin = models.DateField(help_text='Fecha estimada de finalizacion', null=True)
    estado = models.CharField(max_length=3, choices=opciones_estado, default='PEN', help_text='Estado del proyecto')
    observaciones = models.TextField(max_length=140, null=True, default='No hay observaciones')

    def __unicode__(self):
        return self.nombre
"""
    class Meta:
        permissions = (
            ('consultar_Proyecto', 'Puede consultar proyecto'),
            ('consultar_Usuarios_Vinculados', 'Puede consultar usuarios vinculados'),
        )
"""

