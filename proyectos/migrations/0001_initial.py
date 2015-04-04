# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20150327_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(help_text=b'Introduzca una breve rese\xc3\xb1a del proyecto', max_length=140, null=True)),
                ('fecha_creacion', models.DateField(help_text=b'Fecha de creacion del Proyecto', auto_now_add=True, null=True)),
                ('fecha_inicio', models.DateField(help_text=b'Fecha de inicio del Proyecto', null=True)),
                ('fecha_fin', models.DateField(help_text=b'Fecha estimada de finalizacion', null=True)),
                ('estado', models.CharField(default=b'PEN', help_text=b'Estado del proyecto', max_length=3, choices=[(b'PEN', b'Pendiente'), (b'ANU', b'Anulado'), (b'INI', b'Iniciado'), (b'FIN', b'Finalizado')])),
                ('observaciones', models.TextField(default=b'No hay observaciones', max_length=140, null=True)),
                ('lider_proyecto', models.ForeignKey(related_name='Lider', to='usuarios.Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
