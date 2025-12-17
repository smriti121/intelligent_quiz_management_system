"""
Django settings for quiz_system project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# ------------------------
# BASIC SETTINGS
# ------------------------
SECRET_KEY = 'django-insecure-vz8s#7cpf4u*o+xu2521m130!=2!()&3devbk@ouk1az-0mede'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ------------------------
# LOGIN/LOGOUT REDIRECTS
# ------------------------
LOGIN_REDIRECT_URL = 'home'   # update with your URL name
LOGOUT_REDIRECT_URL = 'login'

# ------------------------
# INTERNATIONALIZATION
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'  # optional, set your local timezone
USE_I18N = True
USE_TZ = True


# ------------------------
# INSTALLED APPS
# ------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'users',
    'quiz.apps.QuizConfig',
]


# ------------------------
# MIDDLEWARE
# ------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'quiz_system.urls'


# ------------------------
# TEMPLATES
# ------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # ✅ REQUIRED: tell Django where your global templates folder is
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # <-- added
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'quiz_system.wsgi.application'


# ------------------------
# DATABASE
# ------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ------------------------
# PASSWORD VALIDATION
# ------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ------------------------
# INTERNATIONALIZATION
# ------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ------------------------
# STATIC & MEDIA FILES
# ------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ------------------------
# PASSWORD RESET EMAIL CONFIG
# ------------------------
# Emails will print to terminal (console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@example.com'


# ------------------------
# DEFAULT PRIMARY KEY TYPE
# ------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
