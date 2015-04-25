# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('valor_de_negocio', models.IntegerField(help_text=b'Introduzca un valor de negocio (1 al 10)', max_length=2)),
                ('prioridad', models.IntegerField(help_text=b'Introduzca alguna prioridad para el User Stories', max_length=3)),
                ('valor_tecnico', models.IntegerField(help_text=b'Introduzca un valor t\xc3\xa9cnico al User Stories', max_length=2)),
                ('historial', models.TextField(help_text=b'Introduzca la descripci\xc3\xb3n del historial', max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
