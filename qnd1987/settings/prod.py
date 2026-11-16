from .base import *
from .cdn.conf import * #noqa


DEBUG = os.environ.get('DEBUG', 'False').lower() in ('true', '1', 't')

# Permitir localhost, 127.0.0.1 y el subdominio dinámico de SmartQuail
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS', 
    default='localhost,127.0.0.1,.smartquail.io', 
    cast=lambda v: [s.strip() for s in v.split(',') if s.strip()]
)

SITE_ID = 1
domain = os.environ.get('SITE_DOMAIN', 'http://localhost:8000')

# Orígenes permitidos para CORS (añadiendo desarrollo local y producción)
DOMAIN = os.environ.get("DOMAIN", f"{PROJECT_NAME}.smartquail.io")

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"https://{PROJECT_NAME}.smartquail.io",
    f"https://{DOMAIN}",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    f"https://{PROJECT_NAME}.smartquail.io",
    f"https://{DOMAIN}",
    "https://*.smartquail.io",
]

#SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"




REDIS_HOST = os.environ.get('REDIS_HOST')  # Cambia esto según tu configuración
REDIS_PORT  = os.environ.get('REDIS_PORT')        # Puerto por defecto de Redis
REDIS_DB  = os.environ.get('REDIS_DB')

EMAIL_BACKEND = config("EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend")
EMAIL_HOST = config("EMAIL_HOST", default="localhost")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=False, cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_HOST_USER_INFO = config("EMAIL_HOST_USER_INFO", default="info@tudominio.com")
EMAIL_HOST_USER_LICENCIAS = config("EMAIL_HOST_USER_LICENCIAS", default="licencias@tudominio.com")
EMAIL_HOST_USER_ACTIVOS = config("EMAIL_HOST_USER_ACTIVOS", default="licencias@tudominio.com")
EMAIL_HOST_USER_CTO = config("EMAIL_HOST_USER_CTO", default="licencias@tudominio.com")


MAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL_LICENCIAS = EMAIL_HOST_USER_LICENCIAS 
DEFAULT_FROM_EMAIL_INFO = EMAIL_HOST_USER_INFO
DEFAULT_FROM_EMAIL_ACTIVOS  = EMAIL_HOST_USER_ACTIVOS 
DEFAULT_FROM_EMAIL_CTO = EMAIL_HOST_USER_CTO 



# ==========================================
# CONFIGURACIÓN DE BASE DE DATOS (POSTGRESQL)
# ==========================================
DB_USERNAME = os.environ.get("POSTGRES_USER", "postgres")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
DB_DATABASE = os.environ.get("POSTGRES_DB", "smartquail_db")
DB_HOST = os.environ.get("POSTGRES_HOST", "localhost")
DB_PORT = os.environ.get("POSTGRES_PORT", "5432")
DB_ENGINE = os.environ.get("POSTGRES_ENGINE", "django.db.backends.postgresql")

# Forzar siempre PostgreSQL en producción si las credenciales base existen
DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_DATABASE,
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}


# ==========================================
# CONFIGURACIÓN DE ALMACENAMIENTO EN S3 (CDN)
# ==========================================

# 1. Definir un STATIC_ROOT temporal para que collectstatic los recopile antes de subirlos al S3
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build')

# 2. Clases de almacenamiento para Django (compatible con django-storages moderno)
# Si usas Django 4.2 o superior, se recomienda usar el diccionario STORAGES:
STORAGES = {
    "default": {
        "BACKEND": os.environ.get("MEDIA_STORAGE", "storages.backends.s3.S3Storage"),
    },
    "staticfiles": {
        "BACKEND": os.environ.get("STATICFILES_STORAGE", "storages.backends.s3.S3Storage"),
    },
}

# (Opcional por compatibilidad con versiones anteriores de Django)
DEFAULT_FILE_STORAGE = os.environ.get("MEDIA_STORAGE", "storages.backends.s3.S3Storage")
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE", "storages.backends.s3.S3Storage")

# Configuración de URLs del Bucket
AWS_LOCATION = os.environ.get("AWS_LOCATION", "static")
STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/static/'
MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/media/'



