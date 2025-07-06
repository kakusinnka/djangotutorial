# 管理后台模块
from django.contrib import admin
# Django 提供的用于定义 URL 路由的工具。
from django.urls import path

urlpatterns = [
    # 定义了一个 URL 路由，指定 /admin/ 路径映射到 Django 的管理后台。
    # 当用户访问 /admin/ 时，Django 会加载管理后台的页面。
    path('admin/', admin.site.urls),
]
