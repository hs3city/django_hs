from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import render
from todo.models import ToDo, Category
from todo.forms import ToDoForm, CategoryForm, ChangeStatusForm


def hello_show(request):
    return render(request, 'start.html', {})


class TodoList(CreateView, ListView):
    #TODO Add action to "Gotowe!" button.
    form_class = ChangeStatusForm
    model = ToDo
    # context_object_name = 'todo_list'
    template_name = 'todo.html'
    # queryset = ToDo.objects.select_related('category')


class ToDoAdd(CreateView):
    form_class = ToDoForm
    model = ToDo
    template_name = 'todoform.html'

    def get_context_data(self, **kwargs):
        context = super(ToDoAdd, self).get_context_data(**kwargs)
        return context

class ToDoCategoryList(ListView):
    model = Category
    context_object_name =  'category_list'
    template_name = 'categorylist.html'

    def get_context_data(self, **kwargs):
        context = super(ToDoCategoryList, self).get_context_data(**kwargs)
        context['some_data'] = 'this is just some data'
        context['todo_list'] = ToDo.objects.all()
        return context

class ToDoCategoryAdd(CreateView, ListView):
    form_class = CategoryForm
    model = Category
    context_object_name = 'category_list'
    template_name = 'categoryadd.html'

    def get_context_data(self, **kwargs):
        self.context = super(ToDoCategoryAdd, self).get_context_data(**kwargs)
        return self.context

    def post(self, request, *args, **kwargs):
        stuff = request.POST.get('delete_category') #TODO add delete category action
        return render(request, self.template_name, {'stuff': stuff, 'q': 12 })
