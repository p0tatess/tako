from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'page/base.html')


def categories(request, catid):
    if catid >= 20:
        return redirect('home')
    return HttpResponse(f'<h1>categories</h1><p>{catid}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')