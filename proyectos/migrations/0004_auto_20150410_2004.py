# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('proyectos', '0003_auto_20150409_1913'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(related_name='Cliente', default=None, to='clientes.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date(2015, 4, 10), auto_now_add=True, help_text=b'Fecha de creacion del Proyecto', null=True),
            preserve_default=True,
        ),
    ]
