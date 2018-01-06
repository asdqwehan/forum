# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myforum', '0002_auto_20180105_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bbs',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
