
from django.views.generic import ListView
from todo.models import ToDo


class TodoList(ListView):
    model = ToDo
    template_name = 'todo.html'
    # queryset = ToDo.objects.select_related('category')
