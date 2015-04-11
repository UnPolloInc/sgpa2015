# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flujos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('descripcion', models.TextField(help_text=b'Introduzca alguna descripci\xc3\xb3n adicional acerca del flujo', max_length=140, null=True)),
                ('fecha_creacion', models.DateField(default=datetime.date(2015, 4, 10), auto_now_add=True, help_text=b'Fecha de creacion del Proyecto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
