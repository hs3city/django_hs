from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, DetailView, TemplateView, FormView, DeleteView
from django.shortcuts import render, redirect
from todo.models import ToDo, Category
from todo.forms import ToDoForm, CategoryForm, ChangeStatusForm
from django.db.models import When, Count, Case, CharField


def hello_show(request):
    """ Welcome message page (django view can be function view or class based view)"""
    return render(request, 'todo/start.html', {})


class TodoListView(ListView):
    """ List display all user task """
    form_class = ChangeStatusForm
    model = ToDo
    template_name = 'todo/todo_list.html'

    def post(self, request, *args, **kwargs):
        """ If user clikg 'Gotowe!' button change task status to DONE and save """
        if request.POST.get('gotowe'):
            task_pk = request.POST.get('gotowe')
            task = self.model.objects.get(pk=task_pk)
            task.status = self.model.DONE
            task.save()

        return redirect('todo:todo_list')


class ToDoAddView(CreateView):
    """ User can add new taks to todolist """
    form_class = ToDoForm
    model = ToDo
    template_name = 'todo/todo_add.html'
    success_url = reverse_lazy('todo:todo_list')

class CategoriesView(FormView):
    """ Add new category page """
    model = Category
    form_class = CategoryForm
    context_object_name = 'category_list'
    template_name = 'todo/categories.html'
    success_url = reverse_lazy('todo:categories')

    def get_context_data(self, **kwargs):
        """
        you can pass to context everything you want display in django template
        :return dictionary
        """
        context = super().get_context_data(**kwargs)
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

    def form_invalid(self, form):
        print('invaliddd')
        return super().form_invalid(form)


class ToDoCategoryDeleteView(DeleteView):
    """ Delete item on click delete button in CategoriesView """
    success_url = reverse_lazy('todo:categories')
    model = Category
    template_name = 'todo/category_delete.html'