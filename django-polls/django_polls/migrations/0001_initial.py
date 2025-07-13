# 用于处理外键的删除行为（例如 on_delete=models.CASCADE）。
# 在迁移文件中，外键的删除规则需要显式导入。
import django.db.models.deletion

# django.db.migrations: Django 提供的模块，用于定义迁移操作。
# 迁移文件是 Django 用来记录数据库结构变更的文件。
# django.db.models: Django 提供的模块，用于定义字段类型（例如 CharField、IntegerField）。
from django.db import migrations, models

# 定义一个迁移类，表示这次迁移的内容。
# 每个迁移文件都会生成一个继承自 migrations.Migration 的类。
class Migration(migrations.Migration):

    # 表示这是一个初始迁移文件，用于创建模型对应的数据库表。
    # 初始迁移通常是项目开始时生成的第一批迁移文件。
    initial = True

    # 定义这次迁移依赖的其他迁移文件。
    # 空列表表示没有依赖，通常用于初始迁移。
    dependencies = [
    ]

    # 定义迁移操作的列表。
    # 每个迁移操作描述具体的数据库变更，例如创建表、修改字段、添加索引等。
    operations = [

        # 表示创建一个数据库表, 与模型类名一致。
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),

        # 表示创建一个数据库表, 与模型类名一致。
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.question')),
            ],
        ),
    ]
