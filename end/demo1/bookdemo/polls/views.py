from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Question,Option,Option2

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect

def index2(res):
    # 视图函数中可以同时存在get和post请求 默认为get
    questions = Question.objects.all()
    return render(res,'index2.html',{'questions':questions})

def detail2(res,detaili2):
    question = Question.objects.get(id=detaili2)
    # 使用get方法进入英雄的编辑页面
    if res.method == "GET":
        return render(res,'detail2.html',{"question":question})
    elif res.method == 'POST':
        x = res.POST.get("question")
        option3 = Option2.objects.get(id=x)
        y = option3.num
        option3.num = y+1
        option3.save()

        url = reverse("polls:result",args=(detaili2,))
        return redirect(to=url)

def result(res,detaili2):
    question = Question.objects.get(id=detaili2)
    # 使用get方法进入英雄的编辑页面
    if res.method == "GET":
        return render(res,'result.html',{"question":question})




