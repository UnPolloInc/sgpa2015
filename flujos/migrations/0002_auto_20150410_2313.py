# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flujos',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2015, 4, 10), auto_now_add=True, help_text=b'Fecha de creacion del Flujo', null=True),
            preserve_default=True,
        ),
    ]
