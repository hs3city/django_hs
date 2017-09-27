from django.conf.urls import include, url
from . import views
from hello.views import UsersList, UsersList2, AddJob


app_name='hello'

urlpatterns = [
    url(r'^test/$', views.index, name='index'),
    url(r'^json/$', views.hello_json, name="hello_json"),
    url(r'^$', views.hello_show, name="hello_show"),
    url(r'^users/$', UsersList.as_view(), name='user_list'),
    url(r'^add_job/$', AddJob.as_view(), name='add_job'),
    url(r'^users2/$', UsersList2.as_view(), name='user_list2'),

]


