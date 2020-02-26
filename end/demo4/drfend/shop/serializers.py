from rest_framework import serializers
from .models import *

class CategorySerizlizer(serializers.ModelSerializer):
    """
    编写针对Category的序列化类
    本类指明lCategory的序列化细节
    需要继承ModelSerializer才可以针对模型序列化
    在Mate类中 model指明序列化的模型 fields指明序列化的字段
    """
    # goods 一定要和related_name的值一致
    # StringRelatedField() 可以显示关系模型中__str__返回值  many=True 代表多个对象
    goods = serializers.StringRelatedField(many=True)
    # 返回主键的值
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # 返回路由
    # goods = serializers.HyperlinkedIdentityField(view_name='good-detail',read_only=True,many=True)

    class Meta:
        model = Category
        fields = "__all__"

class GoodSerizlizer(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方 使用source=
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # __all__代表所有字段
        # fields = "__all__"
        fields = ('name','desc','category')