# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('miembros', '__first__'),
        ('flujos', '0034_auto_20150516_0008'),
        ('sprint', '__first__'),
        ('proyectos', '0015_auto_20150516_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(unique=True, max_length=100)),
                ('valor_de_negocio', models.IntegerField(help_text=b'Introduzca un valor de negocio (1 al 10)', max_length=2)),
                ('prioridad', models.IntegerField(help_text=b'Introduzca alguna prioridad para el User Stories', max_length=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('valor_tecnico', models.IntegerField(help_text=b'Introduzca un valor t\xc3\xa9cnico al User Stories', max_length=2)),
                ('historial', models.TextField(help_text=b'Introduzca la descripci\xc3\xb3n del historial', max_length=500, null=True)),
                ('duracion_horas', models.IntegerField(help_text=b'Introduzca la duraci\xc3\xb3n en horas del User Stories', max_length=2)),
                ('flujo', models.ForeignKey(blank=True, to='flujos.Flujos', null=True)),
                ('proyecto', models.ForeignKey(to='proyectos.Proyecto')),
                ('responsable', models.ForeignKey(blank=True, to='miembros.Miembro', null=True)),
                ('sprint', models.ForeignKey(blank=True, to='sprint.Sprint', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
