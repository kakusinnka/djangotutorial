#!/usr/bin/env python
"""Django 用于管理任务的命令行实用程序。"""
import os
import sys


def main():
    """运行管理任务。"""
    # 如果环境变量 DJANGO_SETTINGS_MODULE 已存在，则保持原来的值。
    # 如果环境变量 DJANGO_SETTINGS_MODULE 不存在，则设置为 'mysite.settings'。
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "无法导入 Django。您确定它已安装并可在您的 PYTHONPATH 环境变量中使用吗？您是否忘记激活虚拟环境了？"
        ) from exc
    # 捕获用户输入的命令行参数。
    # 解析参数并调用对应的 Django 管理命令。
    # 执行命令并返回结果。
    execute_from_command_line(sys.argv)

# 检查当前文件是否是直接运行的脚本。
# 如果是，调用 main() 函数。
# __name__：每个 Python 模块都有一个内置属性 __name__：
# 如果模块是直接运行的，__name__ 值为 '__main__'；
# 如果模块是被导入的，__name__ 值为模块名。
if __name__ == '__main__':
    main()
