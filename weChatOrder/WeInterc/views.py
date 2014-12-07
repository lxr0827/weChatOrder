# -*- coding: utf-8 -*-
from weChatOrder.WeInterc.user_info import UserInfo
from weChatOrder.WeInterc.user_info_admin import getUserInfo, unsubscribeUser

__author__ = 'lxr0827'
import hashlib

from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt

from weChatOrder.WeInterc.parser import parse_user_msg

TOKEN = "lxr0827"

#test
appid = "wx243dd553e7ab9da7"
secret = "57f109fd1cce0913a76a1700f94c4e2d"

message_types = ['subscribe', 'unsubscribe', 'click',   'event',
                     'text', 'image', 'link', 'location', 'voice']

@csrf_exempt
def handleRequest(request):
    if request.method == 'GET':
        response = HttpResponse(checkSignature(request),content_type="text/plain")
        print(response)
        return response
    elif request.method == 'POST':
        response = HttpResponse(responseMsg(request),content_type="application/xml")
        return response
    else:
        return None

def responseMsg(request):
    body = smart_str(request.body)
    # print body
    message = parse_user_msg(body)
    # print message.type
    if message.type == 'click':
        print(message.key)
        return
        # return procClickEvent(message.key,message)
    elif message.type == 'subscribe':
        return procSubEvent(message)
    elif message.type == 'unsubscribe':
        return procUnsubEvent(message)
    elif message.type == 'text':
        print(message.content)
        return
        # return procTextMessage(message)

def checkSignature(request):
    global TOKEN
    signature = request.GET.get("signature", None)
    timestamp = request.GET.get("timestamp", None)
    nonce = request.GET.get("nonce", None)
    echoStr = request.GET.get("echostr",None)

    token = TOKEN
    tmpList = [token,timestamp,nonce]
    tmpList.sort()
    tmpstr = "%s%s%s" % tuple(tmpList)
    tmpstr = hashlib.sha1(tmpstr.encode(encoding='utf-8')).hexdigest()

    if tmpstr == signature:
        return echoStr
    else:
        return None

def procSubEvent(message):
    getUserInfo(message.source)

def procUnsubEvent(message):
    unsubscribeUser(message.source)