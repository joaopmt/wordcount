from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    return render(request, 'count.html')
