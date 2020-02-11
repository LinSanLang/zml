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