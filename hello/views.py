from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from hello.models import User, Job
from hello.forms import JobForm


def index(request):
    items = User.objects.all()
    return render(request, 'hello/test.html', context={'items': items})


def hello_show(request):
    return render(request, 'hello/show.html', {})


def hello_json(request):
    return JsonResponse({'hello': 'world'})


class UsersList(ListView):
    model = User
    template_name = 'hello/users.html'


class AddJob(CreateView):
    model = Job
    fields = ['jobtitle']

    def get_success_url(self):
        return '/'


class UsersList2(ListView):
    model = User
    template_name = 'hello/users2.html'
    queryset = User.objects.select_related('job', 'section__department')

# class UserEdit()
