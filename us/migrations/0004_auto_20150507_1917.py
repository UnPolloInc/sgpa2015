# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0003_auto_20150502_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='us',
            name='flujo',
            field=models.ForeignKey(to='flujos.Flujos', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='us',
            name='prioridad',
            field=models.IntegerField(help_text=b'Introduzca alguna prioridad para el User Stories', max_length=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
            preserve_default=True,
        ),
    ]
