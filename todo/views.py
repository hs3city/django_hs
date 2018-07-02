from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, TemplateView, FormView
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

class ToDoCategoryAdd(FormView):
    """ Add new category page """
    model = Category
    form_class = CategoryForm
    context_object_name = 'category_list'
    template_name = 'categories.html'
    success_url = reverse_lazy('todo:categories')

    def get_context_data(self, **kwargs):
        """
        you can pass to context everything you want display in django template
        :return dictionary
        """
        context = super(ToDoCategoryAdd, self).get_context_data(**kwargs)
        context['categorys_list'] = Category.objects.all()
        return context

    def form_valid(self, form):
        """
        save ModelForm here and back to success url,
        instead this you can use django View or TemplateView base class
        and do this in post method.
        :param form:
        :return: HttpResponse
        """
        form.save()
        return super().form_valid(form)

