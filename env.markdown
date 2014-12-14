# 环境依赖

依赖库 | 版本 | 安装
------|------|-----
django | 1.71 | pip install Django==1.7.1
PyMySQL | 0.6.3 | pip install PyMySQL
requests | 2.5.0 | pip install requests
django-cms | 3.0.7 | pip install django-cms
djangocms_text_ckeditor | djangocms插件 | pip install djangocms_text_ckeditor
djangocms_file | djangocms插件 | pip install djangocms_file
djangocms_flash | djangocms插件 | pip install djangocms_flash
djangocms_inherit | djangocms插件 | pip install djangocms_inherit
djangocms_picture | djangocms插件 | pip install djangocms_picture
djangocms_video | djangocms插件 | pip install djangocms_video
djangocms_link | djangocms插件 | pip install djangocms_link


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
创建修改自定义菜单 | 支持click、view类型的主子菜单形式

# notes

 * 初始化数据库时，先把cms相关的app注释掉，先migrate django自己的app和custom app，成功后uncomment cms app，再执行一次 migrate。原因是django 1.7提供了自己的migrate组件，而不是之前版本使用south，存在兼容问题。[该issue地址](https://github.com/divio/django-cms/issues/3436)