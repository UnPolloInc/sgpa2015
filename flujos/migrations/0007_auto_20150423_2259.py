# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0006_auto_20150411_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flujos',
            name='fecha_hora_creacion',
            field=models.DateTimeField(default=datetime.date(2015, 4, 23), auto_now_add=True, help_text=b'Hora de creacion del Flujo', null=True),
            preserve_default=True,
        ),
    ]
