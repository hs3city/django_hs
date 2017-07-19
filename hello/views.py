from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from hello.models import User


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


class UsersList2(ListView):
    model = User
    template_name = 'hello/users2.html'
    queryset = User.objects.select_related('job', 'section__department')
