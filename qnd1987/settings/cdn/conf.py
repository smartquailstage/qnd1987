import os

# Configuración de AWS
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")

# Verificamos de forma segura que el endpoint exista antes de limpiar la barra
_s3_endpoint = os.environ.get("AWS_S3_ENDPOINT_URL")
AWS_S3_ENDPOINT_URL = _s3_endpoint.rstrip('/') if _s3_endpoint else None

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"  # Cambia a 'private' si los archivos deben ser privados
}

# Configuración de almacenamiento (ej. 'qnd041app')
AWS_LOCATION = os.environ.get("AWS_LOCATION", "").strip('/')

# URLs seguras y limpias (evitamos duplicar 'static' si AWS_LOCATION ya lo incluye o no)
if AWS_S3_ENDPOINT_URL:
    # Si AWS_LOCATION es 'qnd041app/static', respetamos la ruta exacta sin añadir más sufijos
    if AWS_LOCATION:
        STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/'
        # Ajustamos media apuntando a la par de static o limpia
        MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION.replace("static", "media")}/'
    else:
        STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/static/'
        MEDIA_URL = f'{AWS_S3_ENDPOINT_URL}/media/'
else:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

# Almacenamiento de archivos estáticos
STATICFILES_STORAGE = os.environ.get("STATICFILES_STORAGE", "django.contrib.staticfiles.storage.StaticFilesStorage")

# Almacenamiento de archivos de medios
DEFAULT_FILE_STORAGE = os.environ.get("MEDIA_STORAGE", "django.core.files.storage.FileSystemStorage")

# Si usas DigitalOcean, añade esta configuración
AWS_S3_SIGNATURE_VERSION = 's3v4'