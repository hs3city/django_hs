from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^json/$', views.hello_json, name="hello_json"),
    url(r'^$', views.hello_show, name="hello_show"),
]
