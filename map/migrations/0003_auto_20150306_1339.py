# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150223_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_color',
            field=models.CharField(default=b'#000000', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='location_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
