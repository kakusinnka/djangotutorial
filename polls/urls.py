# Django 提供的函数，用于定义 URL 路径和它们对应的视图。
# 它是 Django URL 配置的核心工具，允许将 URL 映射到视图函数或类。
from django.urls import path

# 导入当前应用中的 views.py 文件。
from . import views

# Django 中的 URL 配置列表。
# 这是一个 Python 列表，其中每个元素定义一个 URL 路径及其对应的处理逻辑。
# Django 会根据 urlpatterns 来匹配用户请求的 URL。
urlpatterns = [
    # "" URL 路径。
    # 空字符串表示根路径（即 /）。
    # views.index 指定处理这个 URL 的视图函数。
    # index 是在 views.py 文件中定义的视图函数。
    # name="index" 给这个 URL 路径定义一个名称。
    path("", views.index, name="index"),
]