# -*- coding: utf-8 -*-
__author__ = 'lxr0827'
from django.db import models
#from unilever_weichat.settings import WeiInterc_appLabel

class UserInfo(models.Model):
    openid = models.CharField(primary_key=True,max_length = 128,editable=False)
    nickname = models.CharField(max_length = 128,editable=False,blank = True,verbose_name = '昵称')
    sex = models.CharField(max_length = 16,editable=False,blank = True,verbose_name = '性别')
    city = models.CharField(max_length = 64,editable=False,blank = True,verbose_name = '城市')
    country = models.CharField(max_length = 64,editable=False,blank = True,verbose_name = '国家')
    province = models.CharField(max_length = 64,editable=False,blank = True,verbose_name = '省份')
    language = models.CharField(max_length = 64,editable=False,blank = True,verbose_name = '语言')
    headimgurl = models.CharField(max_length = 1024,editable=False,blank = True,verbose_name = '头像链接')
    subscribe_time = models.IntegerField(editable=False,blank = True,verbose_name = '关注时间')
    is_subscribe = models.BooleanField(editable=False, blank=True, default=True, verbose_name = '正在关注')

    def __unicode__(self):
        return self.nickname

    class Meta:
        verbose_name_plural = u'关注者信息'
