# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0017_auto_20150512_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='flujo',
            field=models.ForeignKey(to='flujos.Flujos'),
            preserve_default=True,
        ),
    ]
