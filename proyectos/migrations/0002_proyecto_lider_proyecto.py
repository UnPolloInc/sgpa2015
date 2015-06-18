# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='lider_proyecto',
            field=models.ForeignKey(related_name=b'Lider', to='usuarios.Usuario'),
            preserve_default=True,
        ),
    ]
