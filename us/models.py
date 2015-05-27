#encoding:utf-8
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.datetime_safe import date
from django.utils import timezone
from flujos.models import Flujos, Actividad
from sprint.models import Sprint
from usuarios.models import Usuario
from miembros.models import Miembro
from proyectos.models import Proyecto

# Create your models here.


class us(models.Model):
    opciones_estado = (
        ('TODO', 'To Do'),
        ('DOING', 'Doing'),
        ('DONE', 'Done'),
    )

    nombre = models.CharField(max_length=100, unique=True)
    valor_de_negocio = models.IntegerField(max_length=2, help_text='Introduzca un valor de negocio (1 al 10)', null = False)
    prioridad = models.IntegerField(max_length=3, help_text= 'Introduzca alguna prioridad para el User Stories', null=False, validators=[MinValueValidator(1), MaxValueValidator(100)])
    valor_tecnico = models.IntegerField(max_length=2, help_text='Introduzca un valor técnico al User Stories', null = False)
    historial = models.TextField(max_length=500, help_text= 'Introduzca la descripción del historial', null = True)
    duracion_horas = models.IntegerField(max_length=4, help_text='Introduzca la duración en horas estimadas del User Stories', null=False)
    duracion_horas_en_sprint = models.IntegerField(max_length=4, help_text='duracion de horas en el sprint', null=True, blank=True)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)
    flujo = models.ForeignKey(Flujos, null=True, blank=True)
    responsable = models.ForeignKey(Miembro, null=True, blank=True, on_delete=models.PROTECT)
    proyecto = models.ForeignKey(Proyecto, null=False)
    actividad = models.ForeignKey(Actividad, null=True)
    estado = models.CharField(max_length=5, choices=opciones_estado, default='TODO', help_text='Estado del user story')


    def __unicode__(self):
        return self.nombre

    def __unicode__(self):
        return self.nombre


class registroTrabajoUs(models.Model):
    us=models.ForeignKey(us, null=False)
    descripcion=models.TextField(max_length=200,unique=False, help_text='Introduzca una descricpion del trabajo realizado')
    horas_dedicadas = models.IntegerField(max_length=2, help_text='Introduzca las horas dedicadas')
    fecha_hora_creacion = models.DateTimeField(default=date.today(), auto_now_add=True, help_text='Hora de envio del mensaje', null=True)
    #archivo_adjunto= models.BinaryFi`eld()
    archivo_adjunto = models.FileField(null=True)

    def __unicode__(self):
        return self.nombre
