from rest_framework import serializers
from .models import *

class CategorySerizlizer(serializers.Serializer):
    """
    序列化类 决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10,min_length=3,error_messages={
        'max_length':'最长十个字符',
        'min_length':'最短3个字符'
    })

    def create(self, validated_data):
        """
        通过重写create方法 来定义模型创建方式
        :param validated_data:
        :return:
        """
        print('重写构建方法',validated_data)
        instance = Category.objects.create(**validated_data)
        print('创建模型实例',instance)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改之前的实例
        :return: 返回的新实例
        """
        print('重写更新方法',validated_data,instance.name)
        instance.name = validated_data.get('name',instance.name)
        print(instance.name)
        instance.save()
        return instance

class GoodImgsSerizlizer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    # def validate_good(self, good):
    #     try:
    #         g = Good.objects.get(name=good)
    #         return g
    #     except:
    #         raise serializers.ValidationError('输入商品不存在')
    #     # return good

    def validate(self, attrs):
        try:
            g = Good.objects.get(name = attrs['good']['name'])
        except:
            raise serializers.ValidationError('输入商品不存在')
        attrs['good'] = g
        print('更改后的数据',attrs)
        return attrs

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        """
        通过重写update，来定义模型的更新方法
        :param instance: 更改之前的实例
        :param validated_data: 更改之前的实例
        :return: 返回的新实例
        """
        instance.img = validated_data.get('img',instance.img)
        instance.good = validated_data.get('name', instance.good)
        instance.save()
        return instance

class GoodSerizlizer(serializers.Serializer):
    name = serializers.CharField(max_length=20,min_length=2,error_messages={
        'max_length':'最长不超过20字符',
        'min_length':'最短两个字符'
    })
    category = CategorySerizlizer(label='分类')
    imgs = GoodImgsSerizlizer(label='图片',many=True,read_only=True)

    # 自定义处理字段 validate_+要处理的字段名 这里用来筛选category存在不存在
    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回新值
        """
        print('category原始值为',category)
        try:
            Category.objects.get(name = category['name'])
        except:
            raise serializers.ValidationError('输入的分类名不存在')
        return category

    def validate(self, attrs):
        print('收到的数据为',attrs)
        try:
            c = Category.objects.get(name = attrs['category']['name'])
        except:
            c = Category.objects.create(name = attrs['category']['name'])
        attrs['category'] = c
        print('更改后的数据',attrs)
        return attrs

    def create(self, validated_data):
        print('创建good参数',validated_data)
        instance = Good.objects.create(**validated_data)
        return instance

    # def update(self, instance, validated_data):
    #     """
    #     通过重写update，来定义模型的更新方法
    #     :param instance: 更改之前的实例
    #     :param validated_data: 更改之前的实例
    #     :return: 返回的新实例
    #     """
    #     instance.name = validated_data.get('img',instance.name)
    #     instance.save()
    #     return instance



class GoodSerizlizer1(serializers.ModelSerializer):
    # 在序列化时指定字段 在多方 使用source=
    category = serializers.CharField(source='category.name',read_only=True)
    class Meta:
        model = Good
        # __all__代表所有字段
        # fields = "__all__"
        fields = ('id','name','desc','category')

class CustomSerializer(serializers.RelatedField):
    """
    自定义序列化类
    value 序列化对象
    return 输出格式
    """
    def to_representation(self, value):
        return str(value.id)+'--'+value.name+'--'+value.desc


class CategorySerizlizer1(serializers.ModelSerializer):
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
    # 显示自定义字段值
    # goods = serializers.SlugRelatedField(slug_field='name',many=True,read_only=True)
    # 返回路由(资源RestFulApi)
    # goods = serializers.HyperlinkedRelatedField(view_name='good-detail',read_only=True,many=True)
    # 自定义序列化类
    # goods = CustomSerializer(many=True,read_only=True)
    # goods = GoodSerizlizer(many=True,read_only=True)


    class Meta:
        model = Category
        fields = "__all__"


