# -*- coding: utf-8 -*-
from weChatOrder.WeInterc.access_token import AccessToken, AccessTokenAdmin
from weChatOrder.WeInterc.menu import Menu
from weChatOrder.WeInterc.menu_admin import MenuAdmin
from weChatOrder.WeInterc.user_info import UserInfo
from weChatOrder.WeInterc.user_info_admin import UserInfoAdmin

__author__ = 'lxr0827'
from django.contrib import admin

admin.site.register(AccessToken,AccessTokenAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Menu,MenuAdmin)