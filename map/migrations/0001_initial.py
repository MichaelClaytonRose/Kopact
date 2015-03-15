# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_information', models.TextField()),
                ('location_latitude', models.DecimalField(max_digits=20, decimal_places=8)),
                ('location_longitude', models.DecimalField(max_digits=20, decimal_places=8)),
                ('location_type', models.TextField()),
                ('x', models.IntegerField(default=0)),
                ('z', models.IntegerField(default=0)),
                ('u', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
