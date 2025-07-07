import datetime

# Django 提供的模块，用于定义模型。
# 模型是数据库表的抽象表示，通过模型定义表的结构和字段。
from django.db import models
from django.utils import timezone

# 定义一个名为 Question 的模型类，用来表示数据库中的一个表。
# 每个模型类必须继承自 models.Model，以便 Django 的 ORM 能够识别它。
class Question(models.Model):
    # 定义一个字段，用于存储问题的文本内容。
    # models.CharField:
    # 表示一个字符串字段，适合存储短文本。
    # max_length=200:
    # 限制字符串的最大长度为 200 个字符。
    # 在数据库中，这会对应一个 VARCHAR(200) 字段。
    question_text = models.CharField(max_length=200)

    # 定义一个字段，用于存储问题的发布时间。
    # models.DateTimeField:
    # 表示一个日期时间字段，适合存储日期和时间数据。
    # "date published":
    # 一个可选的描述（verbose_name），用于表示字段的含义。
    # 这个描述会显示在 Django Admin 后台中。
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 定义模型实例的字符串表示，返回一个易读的字段值。
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # 定义一个字段，用于表示选项所属的问题。
    # models.ForeignKey:
    # 表示一个外键字段，用于建立模型之间的关联。
    # 在数据库中，这会生成一个外键约束，链接到 Question 表。
    # on_delete=models.CASCADE:
    # 指定当关联的 Question 被删除时，相关的 Choice 记录也会被删除。
    # 这是数据库的级联删除行为。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # 定义模型实例的字符串表示，返回一个易读的字段值。
    def __str__(self):
        return self.choice_text