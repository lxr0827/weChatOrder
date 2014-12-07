# -*- coding: utf-8 -*-
__author__ = 'lxr0827'
import pymysql,requests,json
import datetime
#定时运行该脚本获取accesstoken，记录到accesstoken module里

#test
appid = "wx243dd553e7ab9da7"
secret = "57f109fd1cce0913a76a1700f94c4e2d"

AccessTokenURL = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + secret

r = requests.get(AccessTokenURL)
if (r.status_code == requests.codes.ok):  # @UndefinedVariable
    res = json.loads(r.text)
    if res.get('errcode') == None:
        accessToken = res['access_token']
        conn = pymysql.connect(host='localhost', user='root', passwd='5817802', db='wechatorderdb', port=3306, charset='utf8')
        cur = conn.cursor()
        nowTime = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
        count = cur.execute("select * from WeInterc_accesstoken limit 0,1")
        if count == 0:
            insertStr = "insert into WeInterc_accesstoken values(1,'%s','%s')" % (accessToken,nowTime)
            print(insertStr)
            cur.execute(insertStr)
            conn.commit()
            cur.close()
            conn.close()
        else:
            result = cur.fetchone()
            updateStr = "update WeInterc_accesstoken set accessToken = '%s',getTokenTime = '%s'where id = 1" % (accessToken, nowTime)
            print(updateStr)
            cur.execute(updateStr)
            conn.commit()
            cur.close()
            conn.close()
