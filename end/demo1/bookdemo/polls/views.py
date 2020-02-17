from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Question,Option,Option2

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,TemplateView,ListView,CreateView,DateDetailView,UpdateView,DetailView

def index2(res):
    # 视图函数中可以同时存在get和post请求 默认为get
    questions = Question.objects.all()
    return render(res,'index2.html',{'questions':questions})

class IndexView(ListView):
    # 方法二、继承ListView
    # template_name指明使用的模板
    template_name = "index2.html"
    # queryset 指明返回的结果列表
    questions = Question.objects.all()
    # context_object_name 指明返回字典参数的健
    context_object_name = "questions"

    # 方法一、继承的TemplateView
    # template_name = "polls/index.html"
    # def get_context_data(self, **kwargs):
    #     return {"questions":Question.objects.all()}


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

class Detail(View):
    def get(self,res,detaili2):
        question = Question.objects.get(id=detaili2)
        return render(res, 'detail2.html', {"question": question})
    def post(self,res,detaili2):
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


class ResultView(View):
    # 方法一 继承View
    def get(self,res,detaili2):
            question = Question.objects.get(id=detaili2)
            return render(res, 'result.html', {"question": question})


