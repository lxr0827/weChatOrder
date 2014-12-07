from django.conf.urls import patterns, include, url
from django.contrib import admin

from weChatOrder.WeInterc.views import handleRequest


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weChatOrder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^wechat/', handleRequest),
    url(r'^admin/', include(admin.site.urls)),
)
