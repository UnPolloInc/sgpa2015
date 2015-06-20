from django.forms import models, DateTimeField

__author__ = 'chelox'

#from django.db import models
from django.contrib.auth.models import User, Group, Permission
from usuarios.models import Usuario
from proyectos.models import Proyecto
from sprint.models import Estado
from clientes.models import Cliente
from sprint.models import Sprint
from django.utils.datetime_safe import date
from flujos.models import Flujos
from miembros.models import Miembro
#from django.contrib.auth.models import User
from django.utils.datetime_safe import date
from us.models import us, registroTrabajoUs
from flujos.models import Actividad
from roles.models import Rol
Usuario.objects.all().delete()
#Tipo_Item.objects.all().delete()
#Fase.objects.all().delete()
Proyecto.objects.all().delete()

#username='alforro'
#first_name= 'alvaro'
#last_name='test'
#cedula='4617510'
#email='alfa.alvaro.rodriguez@gmail.com'
#password='alforro'
#is_superuser=False
#Usuario.objects.create(username=username ,first_name= first_name, last_name=last_name, cedula=cedula, email=email, password= password, is_superuser=is_superuser)

#created_datetime = models.DateTimeField(2015,6,8,22,30,39,0)

pendiente = Estado(estado='Pendiente')
pendiente.save()

en_ejecucion = Estado(estado= 'En ejecucion')
en_ejecucion.save()

finalizado = Estado(estado='Finalizado')
finalizado.save()

##Permisos #####################################################################
permiso=Permission.objects.get(name='Can add us')
permiso2=Permission.objects.get(name='Can add sprint')
permiso3=Permission.objects.get(name='Can change actividad')
permiso4=Permission.objects.get(name='Can add actividad')

permiso.save()
permiso2.save()
permiso3.save()
permiso4.save()

#USUARIOS ##############################################################################################

usuario1 = Usuario.objects.create_user(username='alvaro_user', first_name='Alvaro', last_name='Rodriguez',telefono='0961940704',
                                       cedula='4617510',direccion='Calle Rio Negro esq. Rio Jejui 315',
                                       email='alfa.alvaro.rodriguez@gmail.com', password='alvaro_user')
usuario1.save()
usuario2 = Usuario.objects.create_user(username='homero', first_name='Homero', last_name='Simpson',telefono='0961940704',
                                       direccion='Calle Rio Negro esq. Rio Jejui 315',
                                       cedula='123467',email='amantedelacomida53@aol.com', password='homero')
usuario2.save()
usuario3 = Usuario.objects.create_user(username='walter', first_name='Walter', last_name='White',telefono='0961940704',
                                       cedula='8910111', email='walter@gmail.com',direccion='San Lorenzo',
                                       password='walter')
usuario3.save()
usuario4 = Usuario.objects.create_user(username='john', first_name='John', last_name='Snow',telefono='0961940704',
                                       direccion='Fernando',
                                       cedula='2131415', email='john@gmail.com',
                                       password='john')

#usuario4.save()
#password='bruce'
usuario5 = Usuario.objects.create_user(username='bruce', first_name='Bruce', last_name='Banner',telefono='0961940704',
                                       direccion='Capiata',
                                       cedula='1617181', email='banner@gmail.com',
                                       password='1234')

#usuario5.set_password(password)
usuario5.save()


# CLIENTES ################################################################################

cliente1=Cliente.objects.create_user(username= 'Marcelo', first_name='Marcelo', last_name= 'Vera', cedula=4593718,
                                     direccion='Capiata',email='cheloxtreme@gmail.com',
                                     password='1234')

cliente2=Cliente.objects.create_user(username= 'Gabriel', first_name='Gabriel', last_name= 'Duarte', cedula=4778963, email='chelo.vera@gmail.com',
                                    direccion='San Lorenzo',
                                    password='1234')

cliente3=Cliente.objects.create_user(username= 'Hugo', first_name='Hugo', last_name= 'Bolanhos', cedula=4794123, email='hugo@gmail.com',
                                     direccion='San Lorenzo', password='1234')
cliente1.save()
cliente2.save()
cliente3.save()

## Proyecto Numero 1 "ALPHA" ESTADO PENDIENTE ##############################################################################


proyecto1 = Proyecto(nombre='alpha project', descripcion='este proyecto corresponde a Alvaro Rodriguez',
                     fecha_inicio= '2015-7-10', fecha_fin='2015-8-10', fecha_creacion=date.today(),
                     lider_proyecto=usuario1, cliente=cliente1, estado='PEN')
proyecto1.save()

flujo11 = Flujos(nombre= 'primer flujo del proyecto alpha', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto1)
flujo11.save()

acti1=Actividad(nombre='Analisis.',orden=1,flujo=flujo11)
acti1.save()
acti2=Actividad(nombre='Disenho.',orden=2,flujo=flujo11)
acti2.save()
acti3=Actividad(nombre='Desarrollo.',orden=3,flujo=flujo11)
acti3.save()

sprint1 = Sprint(nombre='primer sprint del proyecto alpha', proyecto=proyecto1, descripcion='sprint correspondiente al proyecto 1',
                 duracion_dias= 7, observaciones='Ninguna', estado=en_ejecucion)
sprint1.save()

sprint11 = Sprint(nombre='segundo sprint del proyecto alpha', proyecto=proyecto1, descripcion='sprint correspondiente al proyecto 1',
                 duracion_dias= 7, observaciones='Ninguna', estado=en_ejecucion)
sprint11.save()

desarrollador = Rol(name='desarrollador', proyecto=proyecto1,)
desarrollador.save()
desarrollador.permissions.add(permiso)
desarrollador.permissions.add(permiso2)
desarrollador.permissions.add(permiso3)
desarrollador.permissions.add(permiso4)
desarrollador.save()

miembro1 = Miembro(rol=desarrollador,proyecto=proyecto1,usuario=usuario2,horas_por_dia=6)
miembro1.save()
miembro2 = Miembro(rol=desarrollador,proyecto=proyecto1,usuario=usuario3,horas_por_dia=5)
miembro2.save()
miembro3 = Miembro(rol=desarrollador, proyecto=proyecto1,usuario=usuario4,horas_por_dia=4)
miembro3.save()

us1p1 = us(nombre='US1 para el proyecto 1',valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,sprint=sprint1,flujo=flujo11, responsable=miembro1, proyecto=proyecto1,
         estado='TODO', actividad=acti1,estado_de_aprobacion='OK')
us1p1.save()

us2p1 = us(nombre='US2 para el proyecto 1',valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10, sprint=sprint1,flujo=flujo11, responsable=miembro2,
         proyecto=proyecto1, estado='TODO', actividad=acti1,estado_de_aprobacion='OK')
us2p1.save()

us3p1 = us(nombre='US3 para el proyecto 1', proyecto=proyecto1,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='TODO',sprint=sprint1,flujo=flujo11, responsable=miembro3,
         estado_de_aprobacion='OK',actividad=acti1)
us3p1.save()

## Proyecto Numero 2 "Betha" ESTADO INICIADO ##############################################################################

## Este proyecto tiene dos sprint, dos flujos.


proyecto2 = Proyecto(nombre='beta project', descripcion='este proyecto corresponde a Homero Simpson', cliente=cliente2,
                     fecha_inicio= '2015-5-20', fecha_fin='2015-6-20', fecha_creacion=date.today(),
                     lider_proyecto=usuario2,estado='INI' )
proyecto2.save()
sprint2 = Sprint(nombre='segundo sprint del proyecto betha', proyecto=proyecto2, descripcion='2do sprint correspondiente al proyecto 2',
                 duracion_dias= 20, observaciones='Ninguna', estado=en_ejecucion)
sprint2.save()

sprint3 = Sprint(nombre='tercer sprint del proyecto betha', proyecto=proyecto2, descripcion='sprint 3 correspondiente al proyecto 2',
                 duracion_dias= 15, observaciones='Ninguna', estado=en_ejecucion)
sprint3.save()




flujo1 = Flujos(nombre= 'primer flujo del proyecto2', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto2)
flujo1.save()

flujo2 = Flujos(nombre= 'segundo flujo del proyecto2', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto2)
flujo2.save()

developer = Rol(name='developer', proyecto=proyecto2,)
developer.save()
developer.permissions.add(permiso)
developer.permissions.add(permiso2)
developer.permissions.add(permiso3)
developer.permissions.add(permiso4)
developer.save()

miembro4 =Miembro(rol=developer, proyecto=proyecto2,usuario=usuario5,horas_por_dia=4)
miembro4.save()
miembro22 = Miembro(rol=developer,proyecto=proyecto2,usuario=usuario3,horas_por_dia=5)
miembro22.save()
miembro33 = Miembro(rol=developer, proyecto=proyecto2,usuario=usuario4,horas_por_dia=4)
miembro33.save()

actividad11=Actividad(nombre='Analisiss',orden=1,flujo=flujo1)
actividad11.save()
actividad22=Actividad(nombre='Diseno',orden=2,flujo=flujo1)
actividad22.save()
actividad333=Actividad(nombre='Desarrolo',orden=3,flujo=flujo2)
actividad333.save()


us1p2 = us(nombre='US1 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=50,actividad=actividad11,sprint=sprint2,flujo=flujo1,responsable=miembro4,
         estado_de_aprobacion='OK',estado='TODO')
us1p2.save()
us2p2 = us(nombre='US2 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=50,actividad=actividad22,sprint=sprint3,flujo=flujo1, responsable=miembro33,
         estado_de_aprobacion='OK',estado='TODO')
us2p2.save()

us3p2 = us(nombre='US3 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=40, actividad=actividad11,sprint=sprint2,flujo=flujo1, responsable=miembro22,
         estado_de_aprobacion='OK',estado='TODO')
us3p2.save()

us4p2 = us(nombre='US4 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10, actividad=actividad333,sprint=sprint2,flujo=flujo2,responsable=miembro4,
         estado_de_aprobacion='OK',estado='TODO')
us4p2.save()
us5p2 = us(nombre='US5 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10, actividad=actividad333,sprint=sprint2,flujo=flujo2,responsable=miembro22,
         estado_de_aprobacion='OK',estado='TODO')
us5p2.save()
us6p2 = us(nombre='US6 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10, actividad=actividad333,sprint=sprint2,flujo=flujo2,responsable=miembro33,
         estado_de_aprobacion='OK',estado='TODO')
us6p2.save()
us7p2 = us(nombre='US7 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10, actividad=actividad333,sprint=sprint2,flujo=flujo2,responsable=miembro33,
         estado_de_aprobacion='OK',estado='TODO')
us7p2.save()


reg1= registroTrabajoUs(us=us1p2, descripcion='primer registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us1p2, descripcion='segundo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us1p2, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us1p2, descripcion='cuarto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg4.save()

reg5= registroTrabajoUs(us=us1p2, descripcion='quinto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us1p2, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us1p2, descripcion='septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us1p2, descripcion='octavo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us1p2, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us1p2, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us1p2, descripcion='decimo 1er registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us1p2, descripcion='decimo 2do registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-27 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us1p2, descripcion='decimo 3er registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-28 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us1p2, descripcion='decimo cuarto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-29 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us1p2, descripcion='decimo quinto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-30 16:30',archivo_adjunto=None)
reg15.save()
reg16= registroTrabajoUs(us=us1p2, descripcion='decimo sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-31 16:30',archivo_adjunto=None)
reg16.save()
reg17= registroTrabajoUs(us=us1p2, descripcion='decimo septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-6-1 16:30',archivo_adjunto=None)
reg17.save()
reg18= registroTrabajoUs(us=us1p2, descripcion='decimo octavo registro', horas_dedicadas=6, fecha_hora_creacion='2015-6-2 16:30',archivo_adjunto=None)
reg18.save()
reg19= registroTrabajoUs(us=us1p2, descripcion='decimo noveno registro', horas_dedicadas=6, fecha_hora_creacion='2015-6-3 16:30',archivo_adjunto=None)
reg19.save()
reg20= registroTrabajoUs(us=us1p2, descripcion='vigesimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-6-4 16:30',archivo_adjunto=None)
reg20.save()


reg1= registroTrabajoUs(us=us2p2, descripcion='primer registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us2p2, descripcion='segundo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us2p2, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us2p2, descripcion='cuarto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg4.save()

reg5= registroTrabajoUs(us=us2p2, descripcion='quinto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us2p2, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us2p2, descripcion='septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us2p2, descripcion='octavo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us2p2, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us2p2, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us2p2, descripcion='decimo 1er registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us2p2, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-27 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us2p2, descripcion='decimo 3er registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-28 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us2p2, descripcion='decimo cuarto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-29 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us2p2, descripcion='decimo quinto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-30 16:30',archivo_adjunto=None)
reg15.save()
reg16= registroTrabajoUs(us=us2p2, descripcion='decimo sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-31 16:30',archivo_adjunto=None)
reg16.save()
reg17= registroTrabajoUs(us=us2p2, descripcion='decimo septimo registro', horas_dedicadas=5, fecha_hora_creacion='2015-6-1 16:30',archivo_adjunto=None)
reg17.save()
reg18= registroTrabajoUs(us=us2p2, descripcion='decimo octavo registro', horas_dedicadas=3, fecha_hora_creacion='2015-6-2 16:30',archivo_adjunto=None)
reg18.save()
reg19= registroTrabajoUs(us=us2p2, descripcion='decimo noveno registro', horas_dedicadas=7, fecha_hora_creacion='2015-6-3 16:30',archivo_adjunto=None)
reg19.save()
reg20= registroTrabajoUs(us=us2p2, descripcion='vigesimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-6-4 16:30',archivo_adjunto=None)
reg20.save()

reg1= registroTrabajoUs(us=us3p2, descripcion='primer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us3p2, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us3p2, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us3p2, descripcion='cuarto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us3p2, descripcion='quinto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us3p2, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us3p2, descripcion='septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us3p2, descripcion='octavo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us3p2, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us3p2, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us3p2, descripcion='decimo 1er registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us3p2, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-27 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us3p2, descripcion='decimo 3er registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-28 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us3p2, descripcion='decimo cuarto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-29 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us3p2, descripcion='decimo quinto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-30 16:30',archivo_adjunto=None)
reg15.save()
reg16= registroTrabajoUs(us=us3p2, descripcion='decimo sexto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-31 16:30',archivo_adjunto=None)
reg16.save()
reg17= registroTrabajoUs(us=us3p2, descripcion='decimo septimo registro', horas_dedicadas=2, fecha_hora_creacion='2015-6-1 16:30',archivo_adjunto=None)
reg17.save()
reg18= registroTrabajoUs(us=us3p2, descripcion='decimo octavo registro', horas_dedicadas=5, fecha_hora_creacion='2015-6-2 16:30',archivo_adjunto=None)
reg18.save()
reg19= registroTrabajoUs(us=us3p2, descripcion='decimo noveno registro', horas_dedicadas=8, fecha_hora_creacion='2015-6-3 16:30',archivo_adjunto=None)
reg19.save()
reg20= registroTrabajoUs(us=us3p2, descripcion='vigesimo registro', horas_dedicadas=2, fecha_hora_creacion='2015-6-4 16:30',archivo_adjunto=None)
reg20.save()


## Proyecto Numero 3 'Gamma' ESTADO FINALIZADO ##############################################################################

proyecto3 = Proyecto(nombre='gamma project', descripcion='este proyecto corresponde a Walter White',
                     fecha_inicio= '2015-5-10',cliente=cliente3, fecha_fin='2015-6-15',
                     fecha_creacion=date.today(),lider_proyecto=usuario3,estado='FIN')
#proyecto4 = Proyecto(nombre='delta project', descripcion='este proyecto corresponde a John Snow',
#                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
#                     lider_proyecto=usuario4, cliente=cliente3,estado='INI')
#proyecto5 = Proyecto(nombre='epsilon project', descripcion='este proyecto corresponde a Bruce Banner',
#                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
#                     lider_proyecto=usuario5, cliente=cliente2,estado='FIN')



proyecto3.save()
#proyecto4.save()
#proyecto5.save()




#sprint4 = Sprint(nombre='segundo Sprint del proyecto betha', proyecto=proyecto2, descripcion='2do sprint correspondiente al proyecto 2',
#                 duracion_dias= 15, observaciones='Ninguna', estado=finalizado)
#sprint4.save()

sprint5 = Sprint(nombre='primer sprint del proyecto gamma', proyecto=proyecto3, descripcion='1er sprint correspondiente al proyecto 3',
                 duracion_dias= 15, observaciones='Ninguna', estado=finalizado)
sprint5.save()

sprint6 = Sprint(nombre='segundo sprint del proyecto gamma', proyecto=proyecto3, descripcion='2do sprint correspondiente al proyecto 3',
                 duracion_dias= 15, observaciones='Ninguna', estado=finalizado)
sprint6.save()

sprint7 = Sprint(nombre='tercer sprint del proyecto gamma', proyecto=proyecto3, descripcion='3er sprint correspondiente al proyecto 3',
                 duracion_dias= 4, observaciones='Ninguna', estado=finalizado)
sprint7.save()
#sprint7 = Sprint(nombre='3 Sprint Pro 4', proyecto=proyecto3, descripcion='3er sprint correspondiente al proyecto 3',
#                 duracion_dias= 15, observaciones='Ninguna', estado=finalizado)
#sprint7.save()

#sprint8 = Sprint(nombre='2SprintPro4', proyecto=proyecto3, descripcion='4to sprint correspondiente al proyecto 3',
#                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
#sprint8.save()



flujo3 = Flujos(nombre= '1er flujo del proyecto gamma', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto3)
flujo3.save()


flujo4 = Flujos(nombre= '2do flujo del proyecto gamma', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto3)
flujo4.save()

flujo5 = Flujos(nombre= '3er flujo del proyecto gamma', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto3)
flujo5.save()

#flujo5 = Flujos(nombre= '3er flujo del proyecto2', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto2)
#flujo5.save()


#desarrollador = Group(name='desarrollador')
#desarrollador.save()

#desarrollador.permissions.add(permiso)
#desarrollador.save()


develop = Rol(name='develop', proyecto=proyecto3,)
develop.save()
develop.permissions.add(permiso)
develop.permissions.add(permiso2)
develop.permissions.add(permiso3)
develop.permissions.add(permiso4)
develop.save()
#rolMiembro2 = Rol(proyecto=proyecto2, Group=desarrollador)
#rolMiembro3 = Rol(proyecto=proyecto3, Group=desarrollador)

#rolMiembro.permissions=[can_add_rol,can_change_rol]
#rolMiembro1.permissions=[Can add us,Can add miembro,Can add rol,Can change rol,Can add sprint, Can add flujo,Can change flujo, Can add actividad,
#                   Can change actividad, Can add registro trabajo us,]
#rolMiembro1.permissions=[]
#rolMiembro2.permissions=['Can add us','Can add miembro','Can add rol','Can change rol','Can add sprint', 'Can add flujo','Can change flujo', 'Can add actividad',
 #                    'Can change actividad', 'Can add registro trabajo us',]
#rolMiembro2.save()
#rolMiembro3.permissions=['Can add us','Can add miembro','Can add rol','Can change rol','Can add sprint', 'Can add flujo','Can change flujo', 'Can add actividad',
#                     'Can change actividad', 'Can add registro trabajo us',]
#rolMiembro3.save()




miembro5 =Miembro(rol=develop, proyecto=proyecto3,usuario=usuario1,horas_por_dia=4)
miembro5.save()
miembro222 = Miembro(rol=develop,proyecto=proyecto3,usuario=usuario3,horas_por_dia=5)
miembro222.save()
miembro333 = Miembro(rol=develop, proyecto=proyecto3,usuario=usuario4,horas_por_dia=4)
miembro333.save()

actividad1=Actividad(nombre='Analisis',orden=1,flujo=flujo3)
actividad1.save()
actividad2=Actividad(nombre='Disenho',orden=2,flujo=flujo3)
actividad2.save()
actividad3=Actividad(nombre='Desarrollo',orden=3,flujo=flujo3)
actividad3.save()
actividad4=Actividad(nombre='Mantenimiento',orden=1,flujo=flujo4)
actividad4.save()
actividad5=Actividad(nombre='Post-Desarrollo',orden=2,flujo=flujo4)
actividad5.save()

actividad6=Actividad(nombre='Mantenimiento.',orden=2,flujo=flujo5)
actividad6.save()

#us1 = us(nombre='US5 para el proyecto 2',valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
#         duracion_horas=10, duracion_horas_en_sprint=10,sprint=sprint4, responsable=miembro33, proyecto=proyecto2,
#         estado='TODO', actividad=actividad1,flujo=flujo2,estado_de_aprobacion='OK')
#us1.save()
#us2 = us(nombre='US6 para el proyecto 2',valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
#         duracion_horas=10, duracion_horas_en_sprint=10,sprint=sprint4, responsable=miembro22, proyecto=proyecto2,
#         estado='TODO', actividad=actividad4,flujo=flujo5,estado_de_aprobacion='OK')
#us2.save()


#US DEL PROYECTO GAMMA

us1p3 = us(nombre='US1 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=40,estado='DONE',actividad=actividad3,sprint=sprint5,flujo=flujo3, responsable=miembro333,
         estado_de_aprobacion='OK')
us1p3.save()

us2p3 = us(nombre='US2 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=60,estado='DONE',actividad=actividad5,sprint=sprint5,flujo=flujo4,responsable=miembro5,
         estado_de_aprobacion='OK')
us2p3.save()
us3p3 = us(nombre='US3 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=45,estado='DONE',actividad=actividad3,sprint=sprint5,flujo=flujo3, responsable=miembro222,
         estado_de_aprobacion='OK')
us3p3.save()


us4p3 = us(nombre='US4 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=35,estado='DONE',actividad=actividad5,sprint=sprint6,flujo=flujo4, responsable=miembro222,
         estado_de_aprobacion='OK')
us4p3.save()

us5p3 = us(nombre='US5 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=25,estado='DONE',actividad=actividad3,sprint=sprint5,flujo=flujo3,responsable=miembro333,
         estado_de_aprobacion='OK')
us5p3.save()
us6p3 = us(nombre='US6 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=28,estado='DONE',actividad=actividad5,sprint=sprint6,flujo=flujo4, responsable=miembro333,
         estado_de_aprobacion='OK')
us6p3.save()
us7p3 = us(nombre='US7 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=50,estado='DONE',actividad=actividad3,sprint=sprint5,flujo=flujo3, responsable=miembro5,
         estado_de_aprobacion='OK')
us7p3.save()

us8p3 = us(nombre='US8 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=30,estado='DONE',actividad=actividad5,sprint=sprint6,flujo=flujo4,responsable=miembro5,
         estado_de_aprobacion='OK')
us8p3.save()
us9p3 = us(nombre='US9 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=35,estado='DONE',actividad=actividad3,sprint=sprint5,flujo=flujo3, responsable=miembro333,
         estado_de_aprobacion='OK')
us9p3.save()

us10p3 = us(nombre='US10 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=60,estado='DONE',actividad=actividad5,sprint=sprint6,flujo=flujo4, responsable=miembro222,
         estado_de_aprobacion='OK')
us10p3.save()

reg1= registroTrabajoUs(us=us1p3, descripcion='primer registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us1p3, descripcion='segundo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us1p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us1p3, descripcion='cuarto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()

reg5= registroTrabajoUs(us=us1p3, descripcion='quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us1p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us1p3, descripcion='septimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us1p3, descripcion='octavo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us1p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us1p3, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us1p3, descripcion='decimo 1er registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us1p3, descripcion='decimo 2do registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us1p3, descripcion='decimo 3er registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us1p3, descripcion='decimo cuarto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us1p3, descripcion='decimo quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()



reg1= registroTrabajoUs(us=us2p3, descripcion='primer registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us2p3, descripcion='segundo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us2p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us2p3, descripcion='cuarto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us2p3, descripcion='quinto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us2p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us2p3, descripcion='septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us2p3, descripcion='octavo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us2p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us2p3, descripcion='decimo registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us2p3, descripcion='decimo 1er registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us2p3, descripcion='decimo 2do registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us2p3, descripcion='decimo 3er registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us2p3, descripcion='decimo cuarto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us2p3, descripcion='decimo quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()


reg1= registroTrabajoUs(us=us3p3, descripcion='primer registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us3p3, descripcion='segundo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us3p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us3p3, descripcion='cuarto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us3p3, descripcion='quinto registro', horas_dedicadas=7, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us3p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us3p3, descripcion='septimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us3p3, descripcion='octavo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us3p3, descripcion='noveno registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us3p3, descripcion='decimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us3p3, descripcion='decimo 1er registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us3p3, descripcion='decimo 2do registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us3p3, descripcion='decimo 3er registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us3p3, descripcion='decimo cuarto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us3p3, descripcion='decimo quinto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()


reg1= registroTrabajoUs(us=us4p3, descripcion='primer registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us4p3, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us4p3, descripcion='tercer registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us4p3, descripcion='cuarto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us4p3, descripcion='quinto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us4p3, descripcion='sexto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us4p3, descripcion='septimo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us4p3, descripcion='octavo registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us4p3, descripcion='noveno registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us4p3, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us4p3, descripcion='decimo 1er registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us4p3, descripcion='decimo 2do registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us4p3, descripcion='decimo 3er registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us4p3, descripcion='decimo cuarto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us4p3, descripcion='decimo quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us5p3, descripcion='primer registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us5p3, descripcion='segundo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us5p3, descripcion='tercer registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us5p3, descripcion='cuarto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us5p3, descripcion='quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us5p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us5p3, descripcion='septimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us5p3, descripcion='octavo registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us5p3, descripcion='noveno registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us5p3, descripcion='decimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us5p3, descripcion='decimo 1er registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us5p3, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us5p3, descripcion='decimo 3er registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us5p3, descripcion='decimo cuarto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us5p3, descripcion='decimo quinto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us6p3, descripcion='primer registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us6p3, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us6p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us6p3, descripcion='cuarto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us6p3, descripcion='quinto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us6p3, descripcion='sexto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us6p3, descripcion='septimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us6p3, descripcion='octavo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us6p3, descripcion='noveno registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us6p3, descripcion='decimo registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us6p3, descripcion='decimo 1er registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us6p3, descripcion='decimo 2do registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us6p3, descripcion='decimo 3er registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us6p3, descripcion='decimo cuarto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us6p3, descripcion='decimo quinto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us7p3, descripcion='primer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us7p3, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us7p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us7p3, descripcion='cuarto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us7p3, descripcion='quinto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us7p3, descripcion='sexto registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us7p3, descripcion='septimo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us7p3, descripcion='octavo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us7p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us7p3, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us7p3, descripcion='decimo 1er registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us7p3, descripcion='decimo 2do registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us7p3, descripcion='decimo 3er registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us7p3, descripcion='decimo cuarto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us7p3, descripcion='decimo quinto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us8p3, descripcion='primer registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us8p3, descripcion='segundo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us8p3, descripcion='tercer registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us8p3, descripcion='cuarto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us8p3, descripcion='quinto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us8p3, descripcion='sexto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us8p3, descripcion='septimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us8p3, descripcion='octavo registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us8p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us8p3, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us8p3, descripcion='decimo 1er registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us8p3, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us8p3, descripcion='decimo 3er registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us8p3, descripcion='decimo cuarto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us8p3, descripcion='decimo quinto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us9p3, descripcion='primer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us9p3, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us9p3, descripcion='tercer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us9p3, descripcion='cuarto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us9p3, descripcion='quinto registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us9p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us9p3, descripcion='septimo registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us9p3, descripcion='octavo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us9p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us9p3, descripcion='decimo registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us9p3, descripcion='decimo 1er registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us9p3, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us9p3, descripcion='decimo 3er registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us9p3, descripcion='decimo cuarto registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us9p3, descripcion='decimo quinto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()

reg1= registroTrabajoUs(us=us10p3, descripcion='primer registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us10p3, descripcion='segundo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us10p3, descripcion='tercer registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us10p3, descripcion='cuarto registro', horas_dedicadas=6, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()
reg5= registroTrabajoUs(us=us10p3, descripcion='quinto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-16 16:30',archivo_adjunto=None)
reg5.save()
reg6= registroTrabajoUs(us=us10p3, descripcion='sexto registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-17 16:30',archivo_adjunto=None)
reg6.save()
reg7= registroTrabajoUs(us=us10p3, descripcion='septimo registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-18 16:30',archivo_adjunto=None)
reg7.save()
reg8= registroTrabajoUs(us=us10p3, descripcion='octavo registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-19 16:30',archivo_adjunto=None)
reg8.save()
reg9= registroTrabajoUs(us=us10p3, descripcion='noveno registro', horas_dedicadas=5, fecha_hora_creacion='2015-5-20 16:30',archivo_adjunto=None)
reg9.save()
reg10= registroTrabajoUs(us=us10p3, descripcion='decimo registro', horas_dedicadas=1, fecha_hora_creacion='2015-5-21 16:30',archivo_adjunto=None)
reg10.save()
reg11= registroTrabajoUs(us=us10p3, descripcion='decimo 1er registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-22 16:30',archivo_adjunto=None)
reg11.save()
reg12= registroTrabajoUs(us=us10p3, descripcion='decimo 2do registro', horas_dedicadas=3, fecha_hora_creacion='2015-5-23 16:30',archivo_adjunto=None)
reg12.save()
reg13= registroTrabajoUs(us=us10p3, descripcion='decimo 3er registro', horas_dedicadas=7, fecha_hora_creacion='2015-5-24 16:30',archivo_adjunto=None)
reg13.save()
reg14= registroTrabajoUs(us=us10p3, descripcion='decimo cuarto registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-25 16:30',archivo_adjunto=None)
reg14.save()
reg15= registroTrabajoUs(us=us10p3, descripcion='decimo quinto registro', horas_dedicadas=2, fecha_hora_creacion='2015-5-26 16:30',archivo_adjunto=None)
reg15.save()


#miembro55 =Miembro(rol=develop, proyecto=proyecto3,usuario=usuario1,horas_por_dia=3)
#miembro55.save()
#miembro25 = Miembro(rol=develop,proyecto=proyecto3,usuario=usuario3,horas_por_dia=3)
#miembro25.save()

us11p3 = us(nombre='US11 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=12,actividad=actividad6,sprint=sprint7,flujo=flujo5,responsable=miembro5,
         estado_de_aprobacion='OK',estado='TODO')
us11p3.save()
us12p3 = us(nombre='US12 para el proyecto 4', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, descripcion='vacio',
         duracion_horas=10, duracion_horas_en_sprint=12,actividad=actividad6,sprint=sprint7,flujo=flujo5,responsable=miembro333,
         estado_de_aprobacion='OK',estado='TODO')

us12p3.save()

reg1= registroTrabajoUs(us=us11p3, descripcion='primer registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us11p3, descripcion='segundo registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us11p3, descripcion='tercer registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us11p3, descripcion='cuarto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()

reg1= registroTrabajoUs(us=us12p3, descripcion='primer registro', horas_dedicadas=8, fecha_hora_creacion='2015-5-10 16:30',archivo_adjunto=None)
reg1.save()
reg2= registroTrabajoUs(us=us12p3, descripcion='segundo registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-11 16:30',archivo_adjunto=None)
reg2.save()
reg3= registroTrabajoUs(us=us12p3, descripcion='tercer registro', horas_dedicadas=4, fecha_hora_creacion='2015-5-12 16:30',archivo_adjunto=None)
reg3.save()
reg4= registroTrabajoUs(us=us12p3, descripcion='cuarto registro', horas_dedicadas=0, fecha_hora_creacion='2015-5-13 16:30',archivo_adjunto=None)
reg4.save()