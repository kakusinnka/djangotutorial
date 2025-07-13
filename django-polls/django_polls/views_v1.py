# Django 提供的一个类，用于构建 HTTP 响应。
# 它可以返回 HTML、纯文本或其他类型的内容作为响应。
# 在这个例子中，HttpResponse 用于返回一个简单的文本响应。
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

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
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    # 确保用户提交的 question_id 对应的问题存在。
    question = get_object_or_404(Question, pk=question_id)
    try:
        # 使用 Django 的反向查询机制从问题的选项集合（choice_set）中获取用户选择的选项。
        selected_choice = question.choice_set.get(pk=request.POST["choice"])

        # 如果用户未选择任何选项，表单中没有 choice 参数。
        # 访问 request.POST["choice"] 时会抛出 KeyError。
        # 如果用户选择了一个不存在的选项（例如，选项被删除），查询 choice_set.get(pk=...) 会抛出 Choice.DoesNotExist。
    except (KeyError, Choice.DoesNotExist):
        # 重新渲染投票页面，并显示错误信息。
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        # Django 的 F 对象，用于在数据库层面进行字段操作。
        selected_choice.votes = F("votes") + 1
        # 保存更新后的选项到数据库。
        selected_choice.save()

        # Django 提供的类，用于返回 HTTP 重定向响应。
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))