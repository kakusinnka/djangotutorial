# 管理后台模块
from django.contrib import admin
# Django 提供的用于定义 URL 路由的工具。
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    # 用于包含其他 URL 配置文件（即将某个应用的 URL 配置嵌套到主 URL 配置中）。
    # 通过 include() 可以将应用的 URL 配置模块集成到项目的主 URL 配置中。
    path("polls/", include("django_polls.urls")),
    # 定义了一个 URL 路由，指定 /admin/ 路径映射到 Django 的管理后台。
    # 当用户访问 /admin/ 时，Django 会加载管理后台的页面。
    path('admin/', admin.site.urls),
] + debug_toolbar_urls()
