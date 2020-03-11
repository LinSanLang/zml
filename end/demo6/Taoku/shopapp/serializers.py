from rest_framework import serializers
from .models import *

class BigcategorySerializer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        instance = Bigcategory.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200,min_length=2,error_messages={
        "max_length":"最多200个字",
        "min_length":"最少2个字"
    })
    img1 = serializers.ImageField()
    img2 = serializers.ImageField()
    num = serializers.IntegerField()
    numout = serializers.IntegerField()
    price = serializers.FloatField()
    price1 = serializers.FloatField()
    desc = serializers.CharField()
    # category = CategorySerizlizer(label="分类")

    def validate_category(self, category):
        """
        处理category
        :param category:  处理的原始值
        :return: 返回新值
        """
        print("category原始值为",category)
        try:
            Category.objects.get(name = category["name"])
        except:
            raise serializers.ValidationError("输入的分类名不存在")

        return category

    def validate(self, attrs):
        print("收到的数据为",attrs)
        try:
            c = Category.objects.get(name=attrs["category"]["name"])
        except:
            c = Category.objects.create(name = attrs["category"]["name"])
        attrs["category"] = c
        print("更改之后的数据",attrs)

        return attrs

    def create(self, validated_data):
        print("创建good参数",validated_data)
        instance = Good.objects.create(**validated_data)  # name=    category=
        return instance

    def update(self, instance, validated_data):
        print("原始值",instance.name,instance.category)
        instance.name = validated_data.get("name",instance.name)
        instance.img1 = validated_data.get("img1", instance.img1)
        instance.img2 = validated_data.get("img2", instance.img2)
        instance.num = validated_data.get("num", instance.num)
        instance.numout = validated_data.get("numout", instance.numout)
        instance.price = validated_data.get("price", instance.price)
        instance.price1 = validated_data.get("price1", instance.price1)
        instance.desc = validated_data.get("desc", instance.desc)
        instance.category = validated_data.get("category",instance.category)
        instance.save()
        return instance

class CategorySerizlizer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })
    bigcategory = serializers.CharField(source='bigcategory.name')
    goods = GoodSerializer(many=True)

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        instance = Category.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    # def validate_good(self, data):
    #     print("原始值",data)
    #     try:
    #         g = Good.objects.get(name = data)
    #         print(g,type(g),"+++")
    #         return g
    #     except:
    #         raise serializers.ValidationError("输入的商品不存在")
    #     # return data

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = GoodImgs.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.img = validated_data.get("img",instance.img)
        instance.good = validated_data.get("good",instance.good)
        instance.save()
        return instance



class FlashSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=100,min_length=2,error_messages={
        "max_length":"最多100个字",
        "min_length":"最少2个字"
    })
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = Flash.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.names = validated_data.get("names",instance.names)
        instance.good = validated_data.get("good",instance.good)
        instance.save()
        return instance

class KillSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=100,min_length=2,error_messages={
        "max_length":"最多100个字",
        "min_length":"最少2个字"
    })
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = Kill.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.names = validated_data.get("names",instance.names)
        instance.good = validated_data.get("good",instance.good)
        instance.save()
        return instance

class InternationSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=100,min_length=2,error_messages={
        "max_length":"最多100个字",
        "min_length":"最少2个字"
    })
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = Internation.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.names = validated_data.get("names",instance.names)
        instance.good = validated_data.get("good",instance.good)
        instance.save()
        return instance

class TaokushopSerializer(serializers.Serializer):
    names = serializers.CharField(max_length=100,min_length=2,error_messages={
        "max_length":"最多100个字",
        "min_length":"最少2个字"
    })
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        print("原始值",attrs["good"]["name"])
        try:
            g = Good.objects.get(name = attrs["good"]["name"])
            print("修改商品",g)
            attrs["good"] = g
        except:
            raise serializers.ValidationError("商品不存在")
        return attrs

    def create(self, validated_data):
        print(validated_data)
        instance = Taokushop.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.names = validated_data.get("names",instance.names)
        instance.good = validated_data.get("good",instance.good)
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        # 设置显示的信息  __all__ 代表模型中的所有字段
        # fields = "__all__"
        # 设置不想显示的信息
        exclude = ['groups']

    def validate(self, attrs):
        from django.contrib.auth import hashers
        if attrs.get('password'):
            attrs['password'] = hashers.make_password(attrs['password'])
        return attrs

class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10,min_length=3)
    password = serializers.CharField(max_length=10,min_length=3)
    password2 = serializers.CharField(max_length=10,min_length=3,write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data['password']:
            raise serializers.ValidationError('密码不一致1')
        else:
            return data

    def validate(self, attrs):
        if attrs['password2'] != attrs['password']:
            raise serializers.ValidationError('密码不一致')

        del attrs['password2']
        return attrs

    def create(self, validated_data):
        # 此方法创建可以加密密码
        return User.objects.create_user(username=validated_data.get('username'),email=validated_data.get('email'),password=validated_data.get('password'))

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        # 设置显示的信息  __all__ 代表模型中的所有字段
        fields = "__all__"
