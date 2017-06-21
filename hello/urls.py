from django.conf.urls import url
from . import views
from hello.views import UsersList

app_name='hello'

urlpatterns = [
    url(r'^test/$', views.index, name='index'),
    url(r'^json/$', views.hello_json, name="hello_json"),
    url(r'^$', views.hello_show, name="hello_show"),
    url(r'^users/$', UsersList.as_view()),
]
