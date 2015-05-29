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
from us.models import us
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
 
 
proyecto1 = Proyecto(nombre='alpha project', descripcion='este proyecto corresponde a Alvaro Rodriguez',
                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
                     lider_proyecto=usuario1, cliente=cliente1, estado='PEN')
proyecto2 = Proyecto(nombre='beta project', descripcion='este proyecto corresponde a Homero Simpson', cliente=cliente2,
                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
                     lider_proyecto=usuario2,estado='PEN' )
proyecto3 = Proyecto(nombre='gamma project', descripcion='este proyecto corresponde a Walter White',
                     fecha_inicio= date.today(),cliente=cliente3, fecha_fin=date.today(),
                     fecha_creacion=date.today(),lider_proyecto=usuario3,estado='PEN')
proyecto4 = Proyecto(nombre='delta project', descripcion='este proyecto corresponde a John Snow',
                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
                     lider_proyecto=usuario4, cliente=cliente3,estado='PEN')
proyecto5 = Proyecto(nombre='epsilon project', descripcion='este proyecto corresponde a Bruce Banner',
                     fecha_inicio= date.today(), fecha_fin=date.today(), fecha_creacion=date.today(),
                     lider_proyecto=usuario5, cliente=cliente2,estado='PEN')
 
proyecto1.save()
proyecto2.save()
proyecto3.save()
proyecto4.save()
proyecto5.save()

pendiente = Estado(estado='Pendiente')
pendiente.save()

en_ejecucion = Estado(estado= 'En ejecucion')
en_ejecucion.save()

finalizado = Estado(estado='Finalizado')
finalizado.save()

sprint1 = Sprint(nombre='SprintPro1', proyecto=proyecto1, descripcion='sprint correspondiente al proyecto 1',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint1.save()
 
sprint2 = Sprint(nombre='Sprint2Pro1', proyecto=proyecto1, descripcion='2do sprint correspondiente al proyecto 1',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint2.save()
 
sprint3 = Sprint(nombre='SprintPro2', proyecto=proyecto2, descripcion='sprint correspondiente al proyecto 2',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint3.save()
 
sprint4 = Sprint(nombre='2SprintPro2', proyecto=proyecto2, descripcion='2do sprint correspondiente al proyecto 2',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint4.save()
 
sprint5 = Sprint(nombre='SprintPro3', proyecto=proyecto3, descripcion='sprint correspondiente al proyecto 3',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint5.save()
 
sprint6 = Sprint(nombre='2Sprint2Pro3', proyecto=proyecto3, descripcion='2do sprint correspondiente al proyecto 3',
                 duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint6.save()
 
sprint7 = Sprint(nombre='SprintPro4', proyecto=proyecto4, descripcion='sprint correspondiente al proyecto 4', duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint7.save()
 
sprint8 = Sprint(nombre='2SprintPro4', proyecto=proyecto4, descripcion='2do sprint correspondiente al proyecto 4', duracion_dias= 15, observaciones='Ninguna', estado=pendiente)
sprint8.save()
 
flujo1 = Flujos(nombre= '1er flujo del proyecto1', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto1)
flujo1.save()
 
flujo2 = Flujos(nombre= '1er flujo del proyecto2', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto2)
flujo2.save()
 
 
flujo3 = Flujos(nombre= '1er flujo del proyecto3', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto3)
flujo3.save()
 
 
flujo4 = Flujos(nombre= '1er flujo del proyecto4', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto4)
flujo4.save()
 
flujo5 = Flujos(nombre= '1er flujo del proyecto5', descripcion='ninguna', fecha_hora_creacion=date.today(), proyecto=proyecto5)
flujo5.save()

rolMiembro = Rol(name='rolMiembroPro1', proyecto=proyecto1)
#rolMiembro.permissions=[can_add_rol,can_change_rol]
rolMiembro.save()
miembro1 = Miembro(rol=rolMiembro,proyecto=proyecto1,usuario=usuario2,horas_por_dia=6)
miembro1.save()
miembro2 = Miembro(rol=rolMiembro,proyecto=proyecto1,usuario=usuario3,horas_por_dia=5)
miembro2.save()
miembro3 = Miembro(rol=rolMiembro, proyecto=proyecto1,usuario=usuario4,horas_por_dia=4)
miembro3.save()
miembro4 =Miembro(rol=rolMiembro, proyecto=proyecto2,usuario=usuario5,horas_por_dia=4)
miembro4.save()
miembro5 =Miembro(rol=rolMiembro, proyecto=proyecto3,usuario=usuario1,horas_por_dia=4)
miembro5.save()
miembro22 = Miembro(rol=rolMiembro,proyecto=proyecto2,usuario=usuario3,horas_por_dia=5)
miembro22.save()
miembro33 = Miembro(rol=rolMiembro, proyecto=proyecto2,usuario=usuario4,horas_por_dia=4)
miembro33.save()
miembro222 = Miembro(rol=rolMiembro,proyecto=proyecto3,usuario=usuario3,horas_por_dia=5)
miembro222.save()
miembro333 = Miembro(rol=rolMiembro, proyecto=proyecto3,usuario=usuario4,horas_por_dia=4)
miembro333.save()

us1p1 = us(nombre='US1 para el proyecto 1', proyecto=proyecto1,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint1,flujo=flujo1, responsable=miembro1)
us1p1.save()
 
us2p1 = us(nombre='US2 para el proyecto 1', proyecto=proyecto1,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN', sprint=sprint2,flujo=flujo1, responsable=miembro2)
us2p1.save()

us3p1 = us(nombre='US3 para el proyecto 1', proyecto=proyecto1,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint2,flujo=flujo1, responsable=miembro3)
us3p1.save()




us1p2 = us(nombre='US1 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint2,flujo=flujo1,responsable=miembro4)
us1p2.save()
us2p2 = us(nombre='US2 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint3,flujo=flujo2, responsable=miembro33)
us2p2.save()

us3p2 = us(nombre='US3 para el proyecto 2', proyecto=proyecto2,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN', sprint=sprint2,flujo=flujo1, responsable=miembro22)
us3p2.save()


us1p3 = us(nombre='US1 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint2,flujo=flujo1, responsable=miembro333)
us1p3.save()

us2p3 = us(nombre='US2 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint2,flujo=flujo1,responsable=miembro5)
us2p3.save()
us3p3 = us(nombre='US3 para el proyecto 3', proyecto=proyecto3,valor_de_negocio= 5, prioridad= 5, valor_tecnico= 5, historial='vacio',
         duracion_horas=10, duracion_horas_en_sprint=10,estado='PEN',sprint=sprint3,flujo=flujo2, responsable=miembro222)
us3p3.save()



