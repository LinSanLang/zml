from rest_framework import viewsets
from .models import *
from .serializers import *

from django.http import HttpResponse

# 通过api_view装饰器可以将基于函数的视图转换成APIView基于类的视图
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework import permissions

from django.shortcuts import get_object_or_404

from rest_framework import throttling

from . import permissions as mypermissions

from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# 引入django过滤类
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

from rest_framework_simplejwt.authentication import JWTAuthentication
@api_view(["GET"])
def getuserinfo(request):
    user = JWTAuthentication().authenticate(request)
    seria = UserSerializer(instance=user[0])
    return Response(seria.data,status=status.HTTP_200_OK)

class BigcategoryViewSets(viewsets.ModelViewSet):
    queryset = Bigcategory.objects.all()
    serializer_class = BigcategorySerializer

class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet之后拥有GET POST PUT PATCH DELETE　等HTTＰ动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer

    # 用户未登录不显示 分类列表 优先级高于全局配置
    # permission_classes = [permissions.IsAdminUser]

    # 授权的前提是认证 也就是登陆过才能权限判定

    # 超级管理员可以创建分类 普通用户可以查看分类
    def get_permissions(self):
        if self.action == "create" or self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            return [permissions.IsAdminUser()]
        else:
            return []

    # 局部过滤配置
    # filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    # filter_fields = ['name']
    # search_fields = ['name']
    # ordering_fields = ['id']

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerializer

class FlashViewSets(viewsets.ModelViewSet):
    queryset = Flash.objects.all()
    serializer_class = FlashSerializer

class KillViewSets(viewsets.ModelViewSet):
    queryset = Kill.objects.all()
    serializer_class = KillSerializer

class InternationViewSets(viewsets.ModelViewSet):
    queryset = Internation.objects.all()
    serializer_class = InternationSerializer

class TaokushopViewSets(viewsets.ModelViewSet):
    queryset = Taokushop.objects.all()
    serializer_class = TaokushopSerializer

class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    """
    声明用户资源类 用户操作：获取个人信息 更新个人信息 删除账户
    扩展action路由 用户操作：创建用户
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 使用action扩展资源的http方法
    # @action(methods=["POST"],detail=False)
    # def regist(self,request):
    #     seria = UserRegistSerializer(data=request.data)
    #     seria.is_valid()
    #     seria.save()
    #     return Response(seria.data,status=status.HTTP_201_CREATED)

    def get_serializer_class(self):
        print('action代表http方法',self.action)
        if self.action == 'create':
            return UserRegistSerializer
        return UserSerializer

class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [mypermissions.OrdersPermission]

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'retrieve' or self.action == 'destory':
            return [mypermissions.OrdersPermission()]
        else:
            return [permissions.IsAdminUser()]