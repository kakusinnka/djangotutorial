# pathlib.Path: Python 的标准库模块，用于处理文件路径。
# 相比传统的字符串路径，Path 提供了更方便的方法来处理跨平台路径
from pathlib import Path

# 项目的根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# Django 项目中用于加密的密钥
SECRET_KEY = 'django-insecure-pnveeg=y2btz#a1o3jd^70+c-mum##f-+xr(lj=l!bh@bo%g!)'

# 是否启用调试模式。
DEBUG = True

# 定义允许访问此 Django 项目的主机名或 IP 地址。
ALLOWED_HOSTS = []

# 定义项目中启用的应用程序列表。
# 默认包含 Django 提供的内置应用（如 admin、auth 等）。
# 自定义应用需要手动添加到此列表中。
INSTALLED_APPS = [
    # 包含 polls 应用程序
    "polls.apps.PollsConfig",

    # 管理站点。
    'django.contrib.admin',
    # 身份验证系统。
    'django.contrib.auth',
    # 内容类型框架。
    'django.contrib.contenttypes',
    # 会话框架。
    'django.contrib.sessions',
    # 消息传送框架。
    'django.contrib.messages',
    # 用于管理静态文件的框架。
    'django.contrib.staticfiles',

    # Debug Toolbar
    'debug_toolbar',
]

# 定义中间件的列表。
# 中间件是处理请求和响应的钩子，可以在请求到达视图或响应返回之前执行操作。
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #  Debug Toolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# 定义了 Django 项目的主 URL 配置文件路径。
ROOT_URLCONF = 'mysite.urls'

# INTERNAL_IPS 用于定义“内部 IP”，通常用来限制调试工具的显示范围。
# 只有来自这些 IP 地址的请求才能访问某些调试功能。
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# 配置模板引擎的选项。
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"], # 项目全局模板目录
        'APP_DIRS': True, # 自动查找应用中的 templates 文件夹
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 指定项目的 WSGI 应用入口点。
WSGI_APPLICATION = 'mysite.wsgi.application'

# 配置数据库连接信息。
# 默认使用 SQLite 数据库。
# ENGINE: 数据库引擎。
# NAME: 数据库文件路径。
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 定义密码验证规则。
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 项目默认语言
LANGUAGE_CODE = 'en-us'

# 项目默认时区
TIME_ZONE = 'UTC'

# 是否启用国际化支持。
USE_I18N = True

# 是否启用时区支持。
USE_TZ = True

# 定义静态文件的 URL 前缀
STATIC_URL = 'static/'

# Django 模型中自动生成主键的字段类型。
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
