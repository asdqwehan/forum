# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bbs',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField()),
                ('author', models.ForeignKey(to='users.Bbs_user')),
            ],
        ),
        migrations.CreateModel(
            name='Catepory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nama', models.CharField(unique=True, max_length=32)),
                ('administrator', models.ForeignKey(to='users.Bbs_user')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to='users.Bbs_user')),
                ('topic', models.ForeignKey(to='myforum.Bbs')),
            ],
        ),
    ]
