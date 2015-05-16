# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.core.mail import send_mail
from django.db import models
#from usuarios.models import Usuario


def notificar(usuarios,subj,mensaje):
    """
        notificar(usuarios,subj,mensaje)
        Notificar
        =========

        Función encargada de realizar las notificaciones a los usuarios mediante el envió de mensajes
        a los correos electronicos de cada uno de los afectados.
        @param usuarios: lista de usuarios al que se le notificará algún cambio.
        @param subj: Subjeto del mensaje.
        @param mensaje: Mensaje explicativo.
    """
    try:
        for u in usuarios:
            mail= u.email
            send_mail(subj, mensaje, 'sgpa2015q06@gmail.com',[mail], fail_silently=False)
    except:
        try:
            mail= usuarios.email
            send_mail(subj, mensaje, 'sgpa2015q06@gmail.com',[mail], fail_silently=False)
        except:
            mail=usuarios
            send_mail(subj, mensaje, 'sgpa2015q06@gmail.com',[mail], fail_silently=False)


def notificar_creacion_usuario(usuarios):
    #Usuario= models.ForeignKey()
    mensaje = u'Hola %s. Se ha creado su usuario éxitosamente.Su username es %s '%(usuarios.first_name,usuarios.username)
    subj = u'Creación de cuenta sgpa2015'
    notificar(usuarios,subj,mensaje)


def notificar_mod_usuario(usuario):
    """
        notificar_mod_usuario(usuario)
        Notificar modificación
        ======================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique la modificación de un Usuario dentro del sistema.
        @param usuario: Usuario al que se notificará.

    """
    mensaje = u'Se han modificado uno o más campos de su cuenta. Por favor consulte la proxima vez que inicie sesión'
    subj = u'Modificacón de cuenta sgpa2015'
    notificar(usuario,subj,mensaje)


def notificar_elim_usuario(usuario):
    """
        notificar_elim_usuario(usuario)
        Notificar Eliminación
        =====================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique la eliminación de un Usuario dentro del sistema.
        @param usuario: Usuario al que se notificará.

    """
    mensaje = u'Se ha eliminado su cuenta. Consulte con el administrador'
    subj = u'Eliminación de cuenta sgpa2015'
    notificar(usuario,subj,mensaje)

def notificar_asignacion_proyecto(usuarios,proyecto):
    """
        notificar_asignacion_proyecto(usuarios,proyecto)
        Notificar Asignación
        ====================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique a uno o varios usuarios la asignación al equipo de un Proyecto.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto al que se le asignó un equipo.

    """
    mensaje = u'Se le ha agregado al equipo del sgte Proyecto %s.' %(proyecto)
    subj = u'Asignación Proyecto SGPA2015'
    notificar(usuarios,subj,mensaje)

def notificar_mod_proyecto(usuarios,proyecto):
    """
        notificar_mod_proyecto(usuarios,proyecto)
        Notificar Modificación
        ======================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique al equipo de un Proyecto la modificación del mismo.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto que se modificó.

    """
    mensaje = u'Se han realizado cambios en los campos del sgte Proyecto %s que tiene asignado.' %(proyecto)
    subj = u'Modificación Proyecto SGPA2015'
    notificar(usuarios,subj,mensaje)

def notificar_creacion_proyecto(usuarios,proyecto):
    """
        notificar_mod_proyecto(usuarios,proyecto)
        Notificar Modificación
        ======================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique al equipo de un Proyecto la modificación del mismo.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto que se modificó.

    """
    mensaje = u'Se ha creado satisfactoriamente el proyecto %s.' %(proyecto)
    subj = u'Creacion Proyecto en SGPA2015'
    notificar(usuarios,subj,mensaje)

def notificar_asignacion_us(usuarios,proyecto):
    """
        notificar_mod_proyecto(usuarios,proyecto)
        Notificar Modificación
        ======================

        Función que prepara los datos para L{Notificar<IS2_R09.apps.Notificaciones.views.notificar>}
        para que notifique al equipo de un Proyecto la modificación del mismo.
        @param usuarios: Lista de usuarios asignados al Proyecto.
        @param proyecto: Proyecto que se modificó.

    """
    mensaje = u'Se le ha asignado satisfactoriamente un us en el proyecto %s.' %(proyecto)
    subj = u'Asignacion de us en SGPA2015'
    notificar(usuarios,subj,mensaje)