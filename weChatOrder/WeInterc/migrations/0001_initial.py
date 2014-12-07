# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('accessToken', models.CharField(verbose_name='accessToken', max_length=256, editable=False)),
                ('getTokenTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ACCESSTOKEN',
            },
            bases=(models.Model,),
        ),
    ]
