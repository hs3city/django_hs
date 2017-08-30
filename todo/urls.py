from django.conf.urls import url

from todo.views import TodoList, ToDoAdd

app_name = 'todo'
urlpatterns = [
    url(r'^$', TodoList.as_view(), name='todo'),
    url(r'^todoformadd/$', ToDoAdd.as_view(), name='todoformadd')
]
