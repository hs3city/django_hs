from django.http import JsonResponse
from django.shortcuts import render


def hello_show(request):
    return render(request, 'hello/show.html', {})


def hello_json(request):
    return JsonResponse({'hello': 'world'})