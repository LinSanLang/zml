"""
Django settings for drfend project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9e%urg=i5i(9s$qov=1w5%+sr3dl^brhdh&-+zlion0i53joak'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'rest_framework',
    'rest_framework_jwt',
    'django_filters',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drfend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drfend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIAFILES_DIRS = [os.path.join(BASE_DIR,'media')]


# 此处可以对DjangoRestFramwork重新配置
REST_FRAMEWORK = {
    # Schema
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.AutoSchema',

    # 默认权限配置 每一个http方法都可以有对应的权限配置
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.AllowAny'
    ],

    # 全局认证 优先级高于视图类中的认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 已经不维护了
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',

        'rest_framework_simplejwt.authentication.JWTAuthentication',

        # 默认首先使用session认证
        # 'rest_framework.authentication.SessionAuthentication',
        # cookie与session cookie是储存再浏览器的非敏感数据
        # session为储存再服务器上的敏感数据 但是session离不开cookie 因为session的sessionid储存再浏览器中
        # 发起请求时 需要在Cookie中携带 sessionid csrftoken 在header中携带X-CSRFToken 值可以在浏览器登录用户后去cookie复制
        # 用户不能退出 在服务器数据库中需要一张表 增加服务器开销

        # 默认使用basic认证 用户名密码
        # 发起请求时 可以将用户名密码 进行编码 写入Authorization中 然后发起请求
        # 将请求中携带的 类似于 Basic   进行解码处理得到对应的用户 获取用户成功，认证成功 获取失败，认证失败
        # 每次都需要用户名和密码
        # 'rest_framework.authentication.BasicAuthentication'
    ],
    # 配置全局访问频次限制 实现反扒
    'DEFAULT_THROTTLE_CLASSES': ['rest_framework.throttling.AnonRateThrottle',
                                 'rest_framework.throttling.UserRateThrottle'],
    'DEFAULT_THROTTLE_RATES': {
        'user': '200/minutes',
        'anon': '100/minutes',
    },
    # 分页功能
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 2,

    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# 应用名 模型名 推荐在没有数据库的前提去配置
AUTH_USER_MODEL = 'shop.User'

# 自定义认证类 应用名.文件名.认证类名
AUTHENTICATION_BACKENDS = ('shop.authbackend.MyLoginBackend',)

# 允许跨域
CORS_ORIGIN_ALLOW_ALL = True

