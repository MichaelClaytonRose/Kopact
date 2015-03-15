# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_name',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='location_type',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
