# Django 提供的类，用于定义应用的配置。
# 每个 Django 应用都可以有一个配置类，负责管理应用的元信息（如名称、默认字段类型等）。
from django.apps import AppConfig

# 定义一个名为 PollsConfig 的配置类。
# 每个 Django 应用都需要一个配置类，通常命名为 <应用名>Config。
# 配置类必须继承自 AppConfig。
class PollsConfig(AppConfig):
    # 定义模型中自动生成主键字段的默认类型。
    # Django 默认会为每个模型添加一个自动生成的主键字段（通常是 id）。
    # 'django.db.models.BigAutoField':
    # 表示主键字段的类型为 BigAutoField。
    # BigAutoField 是一个 64 位整数类型，适合存储较大的数据量。
    # 如果不设置，Django 默认使用 AutoField（32 位整数类型）。
    default_auto_field = 'django.db.models.BigAutoField'

    # 定义应用的名称，通常与应用的目录名称一致。
    # 'polls':
    # 表示这个应用的名称是 polls。
    # Django 使用这个名称来标识应用，并在 INSTALLED_APPS 中引用它。
    name = 'django_polls'
    label = "polls"
