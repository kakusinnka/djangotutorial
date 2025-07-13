from django.utils import timezone

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # get_queryset 的返回值 会自动赋值给 context_object_name 指定的变量名称
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    # DetailView 默认使用 pk 参数来查询对象：
    # question = Question.objects.get(pk=pk)
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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