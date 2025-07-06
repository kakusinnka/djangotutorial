# Django 提供的一个类，用于构建 HTTP 响应。
# 它可以返回 HTML、纯文本或其他类型的内容作为响应。
# 在这个例子中，HttpResponse 用于返回一个简单的文本响应。
from django.http import HttpResponse

# Django 中的视图函数负责处理用户的 HTTP 请求。
# 它接收一个参数 request，这是 Django 自动传入的请求对象，包含请求的所有信息（如方法、URL、头部数据等）。
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")