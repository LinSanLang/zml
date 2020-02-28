from rest_framework import viewsets
from .models import *
from .serializers import *

from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
def category(request):
    print(request,type(request))
    if request.method == 'GET':
        print('获取到GET请求参数',request.query_params)
        queryset = Category.objects.all()
        # instance为需要序列化的对象，来源于数据库
        seria = CategorySerizlizer(instance=queryset,many=True,status=status.HTTP_200_OK)
        return Response(seria.data)
        # return HttpResponse('获取列表成功')
    elif request.method == 'POST':
        print('获取到POST请求参数',request.data)
        # data 也是序列化对象 来源于从请求中提取的数据
        seria = CategorySerizlizer(data=request.data)
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_201_CREATED)
        else:
            return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def categoryDetail(request,cid):
    model = get_object_or_404(Category,pk=cid)
    if request.method == 'GET':
        print('获取到GET请求参数',request.query_params)
        seria = CategorySerizlizer(model)
        return Response(seria.data,status=status.HTTP_200_OK)
        # return HttpResponse('获取单个成功')
    elif request.method == 'PUT' or request.method == 'PATCH':
        print('获取到PUT/PATCH请求参数',request.data)
        # 更新就是从请求中提取数据 替换掉数据库中的数据
        seria = CategorySerizlizer(instance=model,data=request.data)
        # 验证是否合法
        if seria.is_valid():
            seria.save()
            return Response(seria.data,status=status.HTTP_200_OK)
        else:
            return Response(seria.errors,status=status.HTTP_400_BAD_REQUEST)
        # return HttpResponse('修改成功')
    elif request.method == 'DELETE':
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse('删除成功')
    else:
        return HttpResponse('当前路由不允许'+request.method+'操作7')

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet之后拥有GET POST PUT PATCH DELETE　等HTTＰ动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerizlizer