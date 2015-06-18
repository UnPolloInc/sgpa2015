# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(help_text=b'Introduzca una breve rese\xc3\xb1a del proyecto', max_length=140, null=True)),
                ('fecha_creacion', models.DateField(default=datetime.date(2015, 6, 16), help_text=b'Fecha de creacion del Proyecto', null=True)),
                ('fecha_inicio', models.DateField(help_text=b'Fecha de inicio del Proyecto', null=True)),
                ('fecha_fin', models.DateField(help_text=b'Fecha estimada de finalizacion', null=True)),
                ('estado', models.CharField(default=b'PEN', help_text=b'Estado del proyecto', max_length=3, choices=[(b'PEN', b'Pendiente'), (b'ANU', b'Anulado'), (b'INI', b'Iniciado'), (b'FIN', b'Finalizado')])),
                ('observaciones', models.TextField(default=b'No hay observaciones', max_length=140, null=True)),
                ('cliente', models.ForeignKey(related_name=b'Cliente', to='clientes.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
