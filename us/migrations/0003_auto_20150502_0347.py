# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sprint', '__first__'),
        ('flujos', '0012_auto_20150502_0347'),
        ('us', '0002_us_duracion_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='flujo',
            field=models.ForeignKey(to='flujos.Flujos', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='us',
            name='sprint',
            field=models.ForeignKey(to='sprint.Sprint', null=True),
            preserve_default=True,
        ),
    ]
