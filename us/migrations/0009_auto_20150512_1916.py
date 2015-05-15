# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0008_auto_20150512_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='us',
            name='flujo',
            field=models.ForeignKey(to='flujos.Flujos', null=True),
            preserve_default=True,
        ),
    ]
