
from django.views.generic import ListView, CreateView
from todo.models import ToDo
from todo.forms import ToDoForm


class TodoList(ListView):
    model = ToDo
    template_name = 'todo.html'
    # queryset = ToDo.objects.select_related('category')


class ToDoAdd(CreateView):
    form_class = ToDoForm
    model = ToDo
    template_name = 'todoform.html'
