from django.conf.urls import url

from todo.views import TodoList

app_name = 'todo'
urlpatterns = [
    url(r'', TodoList.as_view(), name='todo'),
]
