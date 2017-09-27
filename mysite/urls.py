from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
import todo.views as todo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', todo.hello_show),
    url(r'todo/', include('todo.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
