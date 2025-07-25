# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # For development
import os
from dotenv import load_dotenv
load_dotenv()
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'bookings@solvotours.com')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

INSTALLED_APPS = [
    # ... other apps ...
    'rest_framework',
    'rest_framework_simplejwt',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3650),  # 10 years
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3650),  # 10 years
}

ALLOWED_HOSTS = [
    "api.solvotoursandsafaris.com",
    "solvotours-backend.onrender.com",
    # ...any others you need
] 