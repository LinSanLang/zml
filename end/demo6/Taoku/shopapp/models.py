from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 用户类
class User(AbstractUser):
    telephone = models.CharField(max_length=11,verbose_name='手机号')

class Bigcategory(models.Model):
    name = models.CharField(max_length=20, verbose_name="种类名")
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20,verbose_name="分类名")
    bigcategory = models.ForeignKey(Bigcategory, on_delete=models.CASCADE, verbose_name="种类", related_name='category')
    def __str__(self):
        return self.name

class Good(models.Model):
    name = models.CharField(max_length=20,verbose_name="商品名字")
    num = models.IntegerField(verbose_name="商品库存")
    numout = models.IntegerField(verbose_name="商品销量")
    img1 = models.ImageField(upload_to='img1', verbose_name='商品展示图1')
    img2 = models.ImageField(upload_to='img2', verbose_name='商品展示图2')
    desc = models.CharField(max_length=100,null=True,blank=True,verbose_name="商品描述")
    # 在序列化关联模型时一定要声明related_name
    # 一找多 related_name 没有定义 cl.good_ste.all() related_name定义了 cl.goods.all()
    price = models.FloatField(verbose_name="商品价格")
    price1 = models.FloatField(verbose_name="商品原价格")
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类",related_name='goods')

    def __str__(self):
        return self.name

class GoodImgs(models.Model):
    img = models.ImageField(upload_to='goodimg',verbose_name='商品展示图')
    good = models.ForeignKey(Good,on_delete=models.CASCADE,verbose_name='商品',related_name='imgs')

    def __str__(self):
        return self.good

class Order(models.Model):
    """
    简单模拟 订单只有商品
    """
    num = models.IntegerField(verbose_name="数量")
    price = models.FloatField(verbose_name="总价")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    good = models.ManyToManyField(Good,verbose_name='商品')

    def __str__(self):
        return self.user.username + '的订单'

# 限时抢购
class Flash(models.Model):
    names = models.CharField(max_length=100,verbose_name="名字")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品', related_name='flashs')

    def __str__(self):
        return self.names

# 今日秒杀
class Kill(models.Model):
    names = models.CharField(max_length=100, verbose_name="名字")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品', related_name='kills')

    def __str__(self):
        return self.names

class Internation(models.Model):
    names = models.CharField(max_length=100, verbose_name="名字")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品', related_name='internations')

    def __str__(self):
        return self.names

class Taokushop(models.Model):
    names = models.CharField(max_length=100, verbose_name="名字")
    good = models.ForeignKey(Good, on_delete=models.CASCADE, verbose_name='商品', related_name='taokushops')

    def __str__(self):
        return self.names