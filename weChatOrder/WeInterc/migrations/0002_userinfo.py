# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeInterc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('openid', models.CharField(editable=False, primary_key=True, serialize=False, max_length=128)),
                ('nickname', models.CharField(editable=False, max_length=128, blank=True, verbose_name='昵称')),
                ('sex', models.CharField(editable=False, max_length=16, blank=True, verbose_name='性别')),
                ('city', models.CharField(editable=False, max_length=64, blank=True, verbose_name='城市')),
                ('country', models.CharField(editable=False, max_length=64, blank=True, verbose_name='国家')),
                ('province', models.CharField(editable=False, max_length=64, blank=True, verbose_name='省份')),
                ('language', models.CharField(editable=False, max_length=64, blank=True, verbose_name='语言')),
                ('headimgurl', models.CharField(editable=False, max_length=1024, blank=True, verbose_name='头像链接')),
                ('subscribe_time', models.IntegerField(editable=False, blank=True, verbose_name='关注时间')),
                ('is_subscribe', models.BooleanField(editable=False, default=True, verbose_name='正在关注')),
            ],
            options={
                'verbose_name_plural': '关注者信息',
            },
            bases=(models.Model,),
        ),
    ]
