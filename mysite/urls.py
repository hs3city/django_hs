from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'templa/', include('templa.urls')),
    url(r'form/', include('form.urls')),
    url(r'', include('hello.urls')),
    url(r'^todo/', include('todo.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns