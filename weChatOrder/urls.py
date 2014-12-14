from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin

from weChatOrder.WeInterc.views import handleRequest


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weChatOrder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^wechat/', handleRequest),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

urlpatterns += i18n_patterns('',
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)