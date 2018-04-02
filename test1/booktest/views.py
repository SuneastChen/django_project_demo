from django.shortcuts import render
from django.http import HttpResponse
from booktest.models import *
# Create your views here.
def index(request):

    # return HttpResponse('<h1>hello world</h1>')

    # pars_dict = {'title': '天狼集团', 'list': range(5)}
    # return render(request, 'booktest/index.html', pars_dict)

    context = {'books_list': BookInfo.objects.all()}
    return render(request, 'booktest/index2.html', context)

def detail(request, id):
    context = {'heros_list': BookInfo.objects.get(id=id).heroinfo_set.all()}
    return render(request, 'booktest/detail.html', context)

def bootstrap(request):
    return render(request, 'booktest/bootstrap_test.html')
