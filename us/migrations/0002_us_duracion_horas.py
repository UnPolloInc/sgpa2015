# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='duracion_horas',
            field=models.CharField(help_text=b'Introduzca la duraci\xc3\xb3n en horas del User Stories', max_length=4, null=True),
            preserve_default=True,
        ),
    ]
