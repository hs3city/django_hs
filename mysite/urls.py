from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'templa/$', include('templa.urls')),
    url(r'form/$', include('form.urls')),
    url(r'', include('hello.urls')),
]
