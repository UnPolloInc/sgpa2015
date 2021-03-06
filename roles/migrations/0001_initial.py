# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('proyectos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('proyecto', models.ForeignKey(to='proyectos.Proyecto')),
            ],
            options={
            },
            bases=('auth.group',),
        ),
    ]
