# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20150306_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='location_color',
        ),
        migrations.AlterField(
            model_name='location',
            name='location_information',
            field=models.TextField(default=b'Sorry, we currently have no information about this company. Hopefully they will update their profile soon!'),
            preserve_default=True,
        ),
    ]
