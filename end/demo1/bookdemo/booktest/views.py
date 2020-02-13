from django.shortcuts import render
from django.template import loader
from .models import Book,Hero
# Create your views here.

# MVT  中的V视图模块
# 在此处接受请求 处理数据 返回响应

from django.http import HttpResponse

def index(res):
    # # return HttpResponse("这里是首页2")
    # # 1 获取模板
    # template = loader.get_template("index.html")
    # # 2 渲染模板数据
    books= Book.objects.all()
    # context = {"books":books}
    # result = template.render(context)
    # # 3 将渲染结果使用httpresponse返回
    # return HttpResponse(result)

    # 把上面三部封装到一部
    return render(res,'index.html',{'books':books})

def list(res):
    return HttpResponse("这里是详情页2")

def detail(res,bookid):
    # return HttpResponse("这里是详情页"+bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'book':book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(res,'detail.html',{'book':book})
# 使用django模板
# MVT

