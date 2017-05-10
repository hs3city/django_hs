from django.conf.urls import include, url
from django.contrib import admin
from form import views

urlpatterns = [
    url(r'^$', views.post_form, name="post_form"),
]