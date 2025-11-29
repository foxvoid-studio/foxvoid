import os
from dotenv import load_dotenv
from pathlib import Path
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(" ")
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(" ")


# Application definition

INSTALLED_APPS = [
    'authentication',
    'public',
    'games',

    'rosetta',
    'unfold',
    'modeltranslation',
    'django_countries',
    'timezone_field',
    'debug_toolbar',
    'tailwind',
    'theme',
    'constance',
    'constance.backends.database',
    'rest_framework',
    'rest_framework.authtoken',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

from core.constance_config import *

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'core.middleware.TimezoneMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'constance.context_processors.config',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv("DATABASE_ENGINE"),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PWD'),
        'HOST': os.getenv('DATABASE_HOST'),
        'PORT': os.getenv('DATABASE_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LANGUAGES = [
    ("en", _("English")),
    ("fr", _("French"))
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale"),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "core", "static")

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'authentication.User'

def constance_custom_style(request):
    """
    Conditionally injects CSS only for the Constance configuration page.
    """
    # Verify if request exists and if the URL matches the Constance config page
    # Adjust '/constance/config/' if your admin URL structure is customized
    if request and "/constance/config/" in request.path:
        return static("css/custom_constance_unfold.css")
    
    # Return None if we are not on the specific page (no CSS injected)
    return None

UNFOLD = {
    "SITE_TITLE": "Foxvoid",
    "SITE_HEADER": "Foxvoid",
    "SITE_LOGO": {
        "light": lambda request: static("logo.png"),
        "dark": lambda request: static("logo.png"),
    },
    "SHOW_LANGUAGES": True,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Navigation"),
                "separator": False,
                "collapsible": False,
                "items": [
                    {
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "link": reverse_lazy("admin:index")
                    }
                ]
            },
            {
                "title": _("User Management"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        # Reverse URL format: admin:<app_label>_<model_name>_changelist
                        "link": reverse_lazy("admin:authentication_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "groups",
                        "link": reverse_lazy("admin:authentication_groupproxy_changelist"),
                    },
                ],
            },
            {
                "title": _("Games"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Games"),
                        "icon": "stadia_controller",
                        "link": reverse_lazy("admin:games_game_changelist")
                    },
                    {
                        "title": _("Game Versions"),
                        "icon": "commit",
                        "link": reverse_lazy("admin:games_gameversion_changelist")
                    },
                    {
                        "title": _("Asset Files"),
                        "icon": "videogame_asset",
                        "link": reverse_lazy("admin:games_assetfile_changelist")
                    }
                ]
            },
            {
                "title": _("System"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Translations"),
                        "icon": "translate", # Material Icon name
                        # 'rosetta-home' is the name of the view provided by django-rosetta
                        "link": reverse_lazy("rosetta-old-home-redirect"), 
                    },
                    {
                        "title": _("Global Config"),
                        "icon": "tune",
                        "link": reverse_lazy("admin:constance_config_changelist"),
                        "permission": lambda request: request.user.is_superuser
                    }
                ],
            },
        ]
    },
    "STYLES": [
        constance_custom_style
    ],
}

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'

MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'fr')

TAILWIND_APP_NAME = 'theme'

INTERNAL_IPS = [
    "127.0.0.1",
]

LOGIN_REDIRECT_URL = reverse_lazy("public:index_view")

LOGOUT_REDIRECT_URL = reverse_lazy("logout_view")

LOGIN_URL = reverse_lazy("login_view")

if DEBUG:
    import socket
    
    # Standard local IPs
    INTERNAL_IPS = [
        "127.0.0.1", 
        "::1",
    ]

    # If using Docker, the IP might be dynamic. 
    # This block attempts to find the container's gateway IP.
    try:
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS += [ip[: ip.rfind(".")] + ".1" for ip in ips]
    except Exception:
        pass
    