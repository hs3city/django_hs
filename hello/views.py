from django.http import JsonResponse
from django.shortcuts import render

from hello.models import ShoppingItem


def index(request):
    items = ShoppingItem.objects.all()
    return render(request, 'hello/test.html', context={'items': items})

def hello_show(request):
    return render(request, 'hello/show.html', {})


def hello_json(request):
    return JsonResponse({'hello': 'world'})
