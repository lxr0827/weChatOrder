__author__ = 'lxr0827'
from django.db import models
from django.contrib import admin

class AccessToken(models.Model):
    accessToken = models.CharField(max_length = 256,editable=False,verbose_name=u'accessToken')
    getTokenTime = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.accessToken

    class Meta:
        verbose_name_plural = 'ACCESSTOKEN'

class AccessTokenAdmin(admin.ModelAdmin):
    readonly_fields=('accessToken',)
    def has_add_permission(self, request):
        return False