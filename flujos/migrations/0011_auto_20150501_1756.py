# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('flujos', '0010_auto_20150426_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('orden', models.PositiveIntegerField(help_text=b'Introduzca el orden correspondiente de la actividad')),
                ('flujo', models.ForeignKey(to='flujos.Flujos')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='flujos',
            name='fecha_hora_creacion',
            field=models.DateTimeField(default=datetime.date(2015, 5, 1), auto_now_add=True, help_text=b'Hora de creacion del Flujo', null=True),
            preserve_default=True,
        ),
    ]
