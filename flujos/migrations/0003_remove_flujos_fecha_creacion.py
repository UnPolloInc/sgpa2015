# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0002_auto_20150410_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flujos',
            name='fecha_creacion',
        ),
    ]
