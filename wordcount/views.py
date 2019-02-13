import operator
from django.http import HttpResponse
from django.shortcuts import render
from . import functions

def homepage(request):
    return render(request, 'homepage.html')


def count(request):
    fulltext = request.GET['fulltext'].lower()
    occ_dict = functions.get_occurrence_dict(fulltext.split())
    sorted_tuple = sorted(occ_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': fulltext, 'sorted_tuple': sorted_tuple})


def about(request):
    return render(request, 'about.html')
