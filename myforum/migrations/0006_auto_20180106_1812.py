# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myforum', '0005_bbs_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catepory',
            new_name='Category',
        ),
    ]
