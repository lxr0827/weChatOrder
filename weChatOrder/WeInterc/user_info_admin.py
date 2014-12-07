# -*- coding: utf-8 -*-
__author__ = 'lxr0827'
from django.utils.safestring import mark_safe
from weChatOrder.WeInterc.access_token import AccessToken
from django.contrib import admin
import requests,json
from django.core.exceptions import ObjectDoesNotExist

from .user_info import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    def showHeadImage(self, obj):
        if obj.headimgurl:
            return mark_safe('<img src="%s" />') % obj.headimgurl
        else:
            return u'图像不存在'

    def procUserList(self,userList):
        if userList.get('errcode') != None:
            return {}
        count = userList['count']
        if(0 == int(count)):
            return dict(finish = True)
        openids = userList['data']['openid']

        for openid in openids:
            try:
                UserInfo.objects.get(openid=openid)
            except ObjectDoesNotExist:
                getUserInfo(openid)

        return dict(total = userList['total'],count = userList['count'],next_openid = userList['next_openid'],finish = False)

    def getUserListFromWeiChat(self,getUrl):
        r = requests.get(getUrl)
        if (r.status_code == requests.codes.ok):  # @UndefinedVariable
            userList = json.loads(r.text)
            return self.procUserList(userList)
        return {}

    def getAllUserInfo(self, request, queryset):
        accToken = AccessToken.objects.get(id=1)
        firstGetUserListUrl = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='+ accToken.accessToken
        res = self.getUserListFromWeiChat(firstGetUserListUrl)
        if res == {}:
            self.message_user(request, "同步关注者信息失败")
        else:
            if res['total'] == res['count']:
                self.message_user(request, "同步关注者信息成功")
            else: #关注者超过10000
                nextOpenid = res['next_openid']
                while nextOpenid != u'':
                    nextGetUserListUrl = 'https://api.weixin.qq.com/cgi-bin/user/get?access_token='+accToken.accessToken + '&next_openid=' + nextOpenid
                    res = self.getUserListFromWeiChat(nextGetUserListUrl)
                    if res == {}:
                        self.message_user(request, "同步关注者信息部分失败")
                    else:
                        if res['finish'] == False:
                            nextOpenid = res['next_openid']
                        else:
                            nextOpenid = u''
                self.message_user(request, "同步关注者信息成功")


    def updateUserInfo(self, request, queryset):
        allSuccess = True
        for obj in queryset.iterator():
            if obj.is_subscribe == True:
                if not getUserInfo(obj.openid):
                    allSuccess = False
        if allSuccess:
            self.message_user(request, "更新关注者信息成功！")
        else:
            self.message_user(request, "更新关注者信息部分或全部失败！")

    readonly_fields=('openid',
                     'nickname',
                     'sex',
                     'city',
                     'openid',
                     'country',
                     'province',
                     'language',
                     'headimgurl',
                     'subscribe_time',
                     )
    list_display = ['showHeadImage', 'nickname', 'city', 'province', 'is_subscribe']
    search_fields= ['nickname', 'city','province','openid','sex','country']
    list_filter = ['is_subscribe']
    actions = ['getAllUserInfo','updateUserInfo']
    getAllUserInfo.short_description = u'全选以便同步所有的关注者信息'
    updateUserInfo.short_description = u'更新所选关注者信息'
    showHeadImage.short_description = u'头像'
    showHeadImage.allow_tags = True

    def has_add_permission(self, request):
        return False


def getUserInfo(openid):
    accToken = AccessToken.objects.get(id=1)
    getUserInfoUrl = 'https://api.weixin.qq.com/cgi-bin/user/info?access_token='+accToken.accessToken+'&openid='+openid
    r = requests.get(getUserInfoUrl)
    if (r.status_code == requests.codes.ok):  # @UndefinedVariable
        # weiIntercLogger.info("获取用户信息成功，用户信息为："+r.text)
        try:
            userInfo = json.loads(r.text)
        except:
            # weiIntercLogger.error("json解析用户信息失败，用户信息为："+r.text)
            return False
        if userInfo.get('errcode') != None:
            return False
        if userInfo['subscribe'] == 1:
            try:
                olduser = UserInfo.objects.get(openid=openid)
                olduser.is_subscribe = True
                olduser.nickname = userInfo['nickname']
                olduser.sex=getRealSex(userInfo['sex'])
                olduser.city=userInfo['city']
                olduser.country=userInfo['country']
                olduser.province=userInfo['province']
                olduser.language=userInfo['language']
                olduser.headimgurl=userInfo['headimgurl']
                olduser.subscribe_time=userInfo['subscribe_time']
                olduser.save()

            except ObjectDoesNotExist:
                newUser = UserInfo(openid=openid,
                               nickname=userInfo['nickname'],
                               sex=getRealSex(userInfo['sex']),
                               city=userInfo['city'],
                               country=userInfo['country'],
                               province=userInfo['province'],
                               language=userInfo['language'],
                               headimgurl=userInfo['headimgurl'],
                               subscribe_time=userInfo['subscribe_time']
                               )
                newUser.save()

            return True
    return False

def getRealSex(sexInt):
    if sexInt == 0:
        return '未知'
    elif sexInt == 1:
        return '男性'
    elif sexInt == 2:
        return '女性'
    else:
        return None

def unsubscribeUser(openid):
        try:
            user = UserInfo.objects.get(openid=openid)
            user.is_subscribe = False
            user.save()
            return True
        except ObjectDoesNotExist:
            return False
