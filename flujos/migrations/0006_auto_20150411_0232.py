# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0005_flujos_hora_creacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flujos',
            old_name='hora_creacion',
            new_name='fecha_hora_creacion',
        ),
        migrations.RemoveField(
            model_name='flujos',
            name='fecha_creacion',
        ),
    ]
