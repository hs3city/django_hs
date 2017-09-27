from django.conf.urls import url
import todo.views as todo


app_name = 'todo'
urlpatterns = [
    url(r'^$', todo.hello_show, name="hello_show"),
    url(r'^list/$', todo.TodoList.as_view(), name='todo'),
    url(r'^todoformadd/$', todo.ToDoAdd.as_view(), name='todoformadd')
]
