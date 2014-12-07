# 环境依赖

依赖库 | 版本 | 安装
------|------|-----
django | 1.71 | pip install Django==1.7.1
PyMySQL | 0.6.3 | pip install PyMySQL
requests | 2.5.0 | pip install requests


# 开发环境环境配置

* 配置数据库 weichatorderdb
* python manage.py migrate

# django 开发常用指令

* 新建model,增加migration manage.py makemigrations

# 已有功能

功能                |                描述
--------------------|---------------------
checkSignature | 配置校验签名
accesstoken定时获取 | access_token
接收解析微信平台post的消息 | 包括文本、图像、时间等
处理关注者信息  | 包括关注、取消关注事件的处理