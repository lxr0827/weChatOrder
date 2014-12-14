# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeInterc', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=41, verbose_name='菜单名')),
                ('location', models.IntegerField(choices=[(1, '位置一'), (2, '位置二'), (3, '位置三')], verbose_name='一级菜单位置')),
                ('sublocation', models.IntegerField(choices=[(-1, '无二级菜单'), (0, '有二级菜单'), (1, '位置一'), (2, '位置二'), (3, '位置三'), (4, '位置四'), (5, '位置五')], verbose_name='二级菜单位置')),
                ('type', models.CharField(max_length=63, choices=[('click', 'click'), ('view', 'view')], verbose_name='菜单点击类型')),
                ('key', models.CharField(max_length=257, verbose_name='菜单key值：如果type=view则填入url地址')),
            ],
            options={
                'verbose_name_plural': '自定义菜单',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='menu',
            unique_together=set([('location', 'sublocation')]),
        ),
    ]
