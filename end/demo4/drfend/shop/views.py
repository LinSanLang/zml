from rest_framework import viewsets
from .models import *
from .serializers import *

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