# -*- coding: utf-8 -*-
from django.db import models

__author__ = 'lxr0827'

class Menu(models.Model) :

    LOCATION_CHOICES = (
        (1, '位置一'),
        (2, '位置二'),
        (3, '位置三'),
    )
    SUBLOCATION_CHOICES = (
        (-1, u'无二级菜单'),
        (0, '有二级菜单'),
        (1, '位置一'),
        (2, '位置二'),
        (3, '位置三'),
        (4, '位置四'),
        (5, '位置五'),
    )

    TYPE_CHOICES = (
        ('click', 'click'),
        ('view', 'view'),
    )

    name = models.CharField(max_length=41, verbose_name= '菜单名')
    location = models.IntegerField(choices=LOCATION_CHOICES,verbose_name= '一级菜单位置')
    sublocation = models.IntegerField(choices=SUBLOCATION_CHOICES, verbose_name='二级菜单位置')
    type = models.CharField(max_length=63, choices=TYPE_CHOICES, verbose_name='菜单点击类型')
    key = models.CharField(max_length=257, verbose_name='菜单key值：如果type=view则填入url地址')

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = (("location", "sublocation"),)
        verbose_name_plural = '自定义菜单'