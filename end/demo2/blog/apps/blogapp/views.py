from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Django自带的分页与分页器
from django.core.paginator import Paginator,Page
# 一个Page中有  object_list代表当前页的所有对象
# has_next 是不是有下一页
# has_previous 是否有上一页
# next_page_number 下一页的编号
# previous_page_number 上一页的编号
# self.number 当前页的编号
# self.paginator 当前页的分页器

# 一个Paginator中的object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number): 从分页器中取第几页
# page_range(self): 返回分页列表


from .forms import *
from .models import *
# Create your views here.


def index(resquest):
    ads = Ads.objects.all()
    typepage = resquest.GET.get('type')
    year = None
    month = None
    category_id = None
    if typepage == 'date':
        year = resquest.GET.get('year')
        month = resquest.GET.get('month')
        articles = Article.objects.filter(create_time__year = year,create_time__month = month)
    elif typepage == "category":
        category_id = resquest.GET.get('category_id')
        try:
            category = Categroy.objects.get(id=category_id)
            articles = category.article_set.all()
        except Ellipsis as e:
            print(e)
            return HttpResponse("不合法")
    elif typepage == 'tag':
        tag_id = resquest.GET.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
            articles = tag.article_set.all()
        except Ellipsis as e:
            print(e)
            return HttpResponse("不合法")
    else:
        articles = Article.objects.all().order_by('-create_time')
    paginator = Paginator(articles,2)
    print(articles)
    # 获取get请求中的页码，默认为1
    num = resquest.GET.get('pagenum',1)
    page = paginator.get_page(num)
    return render(resquest,'index.html',locals())

    # return render(resquest,'index.html',{'ads':ads,'page':page,'type':typepage,'year':year,'month':month,'category_id':category_id})
    # return HttpResponse("首页")

def detail(resquest,articleid):
    if resquest.method == "GET":
        try:
            article = Article.objects.get(id=articleid)
            cf = CommmentForm()
            return render(resquest,'single.html',locals())
        except Exception as e:
            print(e)
            return HttpResponse("出错了")
        # return render(resquest,'single.html')
        # return HttpResponse("详情页")
    elif resquest.method == "POST":
        cf = CommmentForm(resquest.POST)
        if cf.is_valid():
            comment = cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse('blogapp:detail',args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommmentForm()
            errors = "输入信息有误"
            return render(resquest, 'single.html', locals())


def contact(resquest):
    return render(resquest,'contact.html')
    # return HttpResponse("首页")

def favicon(request):
    # 如果获取logo返回
    return redirect(to="/static/favicon.ico")