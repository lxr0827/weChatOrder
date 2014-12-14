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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('accessToken', models.CharField(editable=False, max_length=256, verbose_name='accessToken')),
                ('getTokenTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'ACCESSTOKEN',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=41, verbose_name='菜单名')),
                ('location', models.IntegerField(choices=[(1, '位置一'), (2, '位置二'), (3, '位置三')], verbose_name='一级菜单位置')),
                ('sublocation', models.IntegerField(choices=[(-1, '无二级菜单'), (0, '有二级菜单'), (1, '位置一'), (2, '位置二'), (3, '位置三'), (4, '位置四'), (5, '位置五')], verbose_name='二级菜单位置')),
                ('type', models.CharField(choices=[('click', 'click'), ('view', 'view')], max_length=63, verbose_name='菜单点击类型')),
                ('key', models.CharField(max_length=257, verbose_name='菜单key值：如果type=view则填入url地址')),
            ],
            options={
                'verbose_name_plural': '自定义菜单',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('openid', models.CharField(editable=False, serialize=False, max_length=128, primary_key=True)),
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
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('location', 'sublocation')]),
        ),
    ]
