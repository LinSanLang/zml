from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(resquest):
    return render(resquest,'index.html')
    # return HttpResponse("首页")

def detail(resquest,id):
    return render(resquest,'single.html')
    # return HttpResponse("详情页")

def contact(resquest):
    return render(resquest,'contact.html')
    # return HttpResponse("首页")