from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "问题表"
        verbose_name_plural = verbose_name

class Option(models.Model):
    one = models.CharField(max_length=50,null=True)
    onenum = models.IntegerField(max_length=8,null=True)
    two = models.CharField(max_length=50, null=True)
    twonum = models.IntegerField(max_length=8, null=True)
    three = models.CharField(max_length=50, null=True)
    threenum = models.IntegerField(max_length=8, null=True)
    four = models.CharField(max_length=50, null=True)
    fournum = models.IntegerField(max_length=8, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Option2(models.Model):
    name = models.CharField(max_length=50,null=True)
    num = models.IntegerField(max_length=8,null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "投票表"
        verbose_name_plural = verbose_name
