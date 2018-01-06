# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myforum', '0003_auto_20180106_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catepory',
            old_name='nama',
            new_name='name',
        ),
    ]
