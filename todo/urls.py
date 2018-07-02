from django.conf.urls import url
import todo.views as todo

app_name = 'todo'

urlpatterns = [
    url(r'^$', todo.hello_show, name="hello_show"),
    url(r'^todo_list/$', todo.TodoListView.as_view(), name='todo_list'),
    url(r'^todo_add/$', todo.ToDoAddView.as_view(), name='todo_add'),
    url(r'^categories/$', todo.CategoriesView.as_view(), name='categories'),
    url(r'^categories/(?P<pk>[^/]+)/delete$', todo.ToDoCategoryDeleteView.as_view(), name='categories_delete')
]
