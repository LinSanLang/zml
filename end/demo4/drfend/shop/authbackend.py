"""
实现自定义认证类（登录 内容）
"""
from .models import *
from django.contrib.auth import backends
from django.db.models import Q

class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        """

        :param request:
        :param kwargs:  认证参数
        :return:  如果认证成功 返回认证用户 否则返回None
        """
        print(kwargs)

        username = kwargs['username']
        password = kwargs['password']

        user = User.objects.filter(Q(username=username)|Q(email=username)|Q(telephone=username)).first()
        if user:
            b = user.check_password(password)
            if b:
                return user
        else:
            None