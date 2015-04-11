# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0004_flujos_fecha_creacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujos',
            name='hora_creacion',
            field=models.DateTimeField(default=datetime.date(2015, 4, 11), auto_now_add=True, help_text=b'Hora de creacion del Flujo', null=True),
            preserve_default=True,
        ),
    ]
