# Django 提供的一个类，用于构建 HTTP 响应。
# 它可以返回 HTML、纯文本或其他类型的内容作为响应。
# 在这个例子中，HttpResponse 用于返回一个简单的文本响应。
from django.http import HttpResponse
from django.template import loader

from .models import Question

# Django 中的视图函数负责处理用户的 HTTP 请求。
# 它接收一个参数 request，这是 Django 自动传入的请求对象，包含请求的所有信息（如方法、URL、头部数据等）。
def index(request):
    # 结果是一个包含最近发布的 5 个问题的 QuerySet 对象。
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # 加载名为 polls/index.html 的模板文件。
    template = loader.get_template("polls/index.html")
    # 将获取到的问题列表传递给模板，渲染出 HTML 页面。
    context = {"latest_question_list": latest_question_list}
    # 返回渲染后的 HTML 页面作为 HTTP 响应。
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)