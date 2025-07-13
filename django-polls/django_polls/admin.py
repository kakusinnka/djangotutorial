from django.contrib import admin

from .models import Choice, Question

# Django 提供的一个类，用于在管理后台的模型编辑页面中内联显示相关模型。
# StackedInline 使用堆叠样式（每个字段占一行），适合字段较多的模型。
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)