from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Book,Hero
# Create your views here.

# MVT  中的V视图模块
# 在此处接受请求 处理数据 返回响应

from django.http import HttpResponse,HttpResponseRedirect

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

def deletebook(res,bookid):
    book=Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    # 删除之后仍然回到列表页
    # return HttpResponseRedirect(redirect_to='/')
    # return redirect(to='/')
    url = reverse('booktest:index')
    return redirect(to=url)

def deletehero(res,heroid):
    hero=Hero.objects.get(id=heroid)
    # 先获取在删除
    bookid = hero.book.id
    hero.delete()
    url = reverse('booktest:detail',args=(bookid,))
    return redirect(to=url)

def addhero(res,bookid):
    # 视图函数中可以同时存在get和post请求 默认为get
    if res.method == 'GET':
        return render(res,'addhero.html')
    elif res.method == 'POST':
        hero = Hero()
        hero.name = res.POST.get("heroname")
        hero.content = res.POST.get("herocontent")
        hero.gender = res.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)

def edithero(res,heroid):
    hero = Hero.objects.get(id=heroid)
    # 使用get方法进入英雄的编辑页面
    if res.method == "GET":
        return render(res,'edithero.html',{"hero":hero})
    elif res.method == "POST":
        hero.name = res.POST.get("heroname")
        hero.content = res.POST.get("herocontent")
        hero.gender = res.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(to=url)

def addbook(res):
    # 视图函数中可以同时存在get和post请求 默认为get
    if res.method == 'GET':
        return render(res,'addbook.html')
    elif res.method == "POST":
        book=Book()
        book.title = res.POST.get("booktitle")
        book.pub_date = res.POST.get("bookdate")
        book.price = res.POST.get("bookprice")
        book.save()
        return redirect(to='/')

def editbook(res,bookid):
    book = Book.objects.get(id=bookid)
    # 视图函数中可以同时存在get和post请求 默认为get
    if res.method == 'GET':
        return render(res,'editbook.html')
    elif res.method == "POST":
        book.title = res.POST.get("booktitle")
        book.pub_date = res.POST.get("bookdate")
        book.price = res.POST.get("bookprice")
        book.save()
        return redirect(to='/')





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

