from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.simple_templa, name="simple_templa"),
]