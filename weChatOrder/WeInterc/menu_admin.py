# -*- coding: utf-8 -*-
import traceback
from django.contrib import admin
import json
from weChatOrder.WeInterc.access_token import AccessToken
from weChatOrder.WeInterc.views import postToWeiChat

__author__ = 'lxr0827'


class MenuAdmin(admin.ModelAdmin):
    def toWeChatJson(self, queryset):
        menu_name1 = ''
        menu_name2 = ''
        menu_name3 = ''
        menu1 = []
        menu2 = []
        menu3 = []
        submenu1 = []
        submenu2 = []
        submenu3 = []

        dicts = queryset.values()
        for dict in dicts:
            if dict['sublocation'] == -1:
                if dict['type'] == 'view':
                    dict['url'] = dict['key']
                    del dict['key']
                if dict['location'] == 1:
                    menu1 = dict
                elif dict['location'] == 2:
                    menu2 = dict
                elif dict['location'] == 3:
                    menu3 = dict
            elif dict['sublocation'] == 0:
                if dict['location'] == 1:
                    menu_name1 = dict['name']
                elif dict['location'] == 2:
                    menu_name2 = dict['name']
                elif dict['location'] == 3:
                    menu_name3 = dict['name']

        for dict in dicts:
            if dict['location'] == 1 and dict['sublocation'] > 0:
                submenu1.append(dict)
            elif dict['location'] == 2 and dict['sublocation'] > 0:
                submenu2.append(dict)
            elif dict['location'] == 3 and dict['sublocation'] > 0:
                submenu3.append(dict)

        menu_total = []
        if menu_name1 != '':
            menu_total.append({'name': menu_name1, 'sub_button': submenu1})
        else:
            menu_total.append(menu1)
        if menu_name2 != '':
            menu_total.append({'name': menu_name2, 'sub_button': submenu2})
        else:
            menu_total.append(menu2)
        if menu_name3 != '':
            menu_total.append({'name': menu_name3, 'sub_button': submenu3})
        else:
            menu_total.append(menu3)

        return json.dumps({"button": list(menu_total)}, ensure_ascii=False)

    def changeMenu(self, request, queryset):
        accToken = AccessToken.objects.get(id=1)
        postUrl = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=' + accToken.accessToken
        jsonStr = self.toWeChatJson(queryset)
        print(jsonStr)
        if (postToWeiChat(postUrl, jsonStr.encode('utf-8'))):
            self.message_user(request, "更改自定义菜单成功！")
        else:
            self.message_user(request, "更改自定义菜单失败")


    list_display = ['name', 'location', 'sublocation', 'type']
    search_fields = ['name', 'location', 'sublocation', 'type']
    ordering = ['location', 'sublocation']
    actions = ['changeMenu']
    radio_fields = {"location": admin.HORIZONTAL, "sublocation": admin.HORIZONTAL, "type": admin.HORIZONTAL}
    save_as = True

    changeMenu.short_description = '选择全部菜单发布给微信后台修改自定义菜单'