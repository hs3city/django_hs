from django.conf.urls import url
import todo.views as todo

app_name = 'todo'

urlpatterns = [
    url(r'^$', todo.hello_show, name="hello_show"),
    url(r'^todo_list/$', todo.TodoList.as_view(), name='todo_list'),
    url(r'^todo_add/$', todo.ToDoAdd.as_view(), name='todo_add'),
    url(r'^categories/$', todo.ToDoCategoryAdd.as_view(), name='categories')
]
