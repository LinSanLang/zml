from rest_framework import serializers
from .models import *

class CategorySerizlizer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        "max_length":"最多10个字",
        "min_length":"最少3个字"
    })



    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print("重写创建方法",validated_data)
        instance = Category.objects.create(**validated_data)
        print("创建模型实例",instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改参数
        :return: 返回的新实例
        """
        print("重写更新方法", validated_data, instance.name)
        instance.name = validated_data.get("name", instance.name)
        print(instance.name)
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

class GoodSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        "max_length":"最多20个字",
        "min_length":"最少2个字"
    })
    category = CategorySerizlizer(label="分类")
    imgs = GoodImgsSerializer(label="图片",many=True,read_only=True)

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
        instance.category = validated_data.get("category",instance.category)
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