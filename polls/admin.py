# Django 提供的管理后台模块。
from django.contrib import admin
# 从当前应用的 models.py 文件中导入 Question 模型。
from .models import Question

# 将 Question 模型注册到 Django Admin。
admin.site.register(Question)