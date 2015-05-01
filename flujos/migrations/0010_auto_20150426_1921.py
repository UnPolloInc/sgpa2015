# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0009_auto_20150426_1921'),
        ('flujos', '0009_auto_20150425_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujos',
            name='proyecto',
            field=models.ForeignKey(default=1, to='proyectos.Proyecto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flujos',
            name='fecha_hora_creacion',
            field=models.DateTimeField(default=datetime.date(2015, 4, 26), auto_now_add=True, help_text=b'Hora de creacion del Flujo', null=True),
            preserve_default=True,
        ),
    ]
