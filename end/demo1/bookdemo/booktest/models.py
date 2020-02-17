from django.db import models

# Create your models here.

#  在此编写应用的数据模型类
#  每一张表就是一个模型类

# 有了模型之后模型类如何与数据库交互
# 1注册模型
# 2生成迁移文件 python manage.py makemigrations
# 3，同步迁移执行ORM语句生成数据表 python manage.py migrate
# 模型类更改后需要再次执行2，3部

class Book(models.Model):
    """
    book继承了Model类 因为Model类拥有操作数据库的功能
    """
    title=models.CharField(max_length=20)
    price=models.FloatField(default=0)
    pub_date=models.DateField(default="1983-06-01")

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    Hero继承了Model类 因为Model类拥有操作数据库的功能
    """
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=6,choices=(('male','男'),('female','女')),default='male')
    content=models.CharField(max_length=100)
    # book 是一对多章的外键 on_delete代表删除主表数据时如何做
    book=models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# django orm关联查询
# 多方Hero   一方Book
# 1多找一， 多方对象.关系字段    exp: h1.book
# 2一找多， 一方对象.小写多方类名_set.all()   exp:  b1.hero_set.all()

class UserManager(models.Manager):
    """
    自定义模型管理类 改模型不存在objects对象
    """

    def deleteByTelePhone(self,tele):
        # django默认的objects 是Manages类型 *.objects.get()
        user = self.get(telephone=tele)
        user.delete()

    def createUser(self,tele):
        # self.model 可以获取模型类构造函数
        user = self.model()
        # user = User()
        user.telephone = tele
        user.save()

class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True,verbose_name='手机号')
    # 自定义过管理字段后不存在objects 自定义了一个新的 起名objects
    objects = UserManager()
    def __str__(self):
        return self.telephone

    class Meta:
        # 表名
        db_table = "用户类"
        # 排序依据
        ordering = ["id"]
        # admin 页面进入模型类显示的名字
        verbose_name = "用户模型类a"
        # admin 页面在应用下方显示的名字
        verbose_name_plural = "用户模型类"

class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    passward = models.CharField(max_length=20,verbose_name="密码")
    regist_data = models.DateField(auto_now_add=True,verbose_name="注册日期")
    # 这里以为Concact还没创建 所以需要引起来
    # concact = models.OneToOneField('Concact',on_delete=models.CASCADE)

class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="2927361944@qq.com")
    account = models.OneToOneField(Account,on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=20,verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")

class Tag(models.Model):
    name = models.CharField(max_length=10,verbose_name="标签名")
    articles = models.ManyToManyField(Article,related_name='tags')

# 一对多 一方Book 实例b 多方Hero 实例h 关系字段定义在多方
# 一找多 b.hero_set.all()   如果定义过related_name = 'heros' 则使用b.heros.all()
# 多找一 h.book

# 一对一 一方Account 实例a   一方Concact 实例c  关系字段定义在任意一方
# a找c a.concant
# c找a c.account

# 多对多  多方Article  实例a    多方Tag 实例t   关系字段可以定义在任意一方
# 添加关系   t.articles.add(a)    移除关系  t.articles.remove(a)
# a 找 所有的 t   a.tag_set.all()   如果定义过related_name='tags' 则使用 a.tags.all()
# t 找 所有的 a   t.articles.all()