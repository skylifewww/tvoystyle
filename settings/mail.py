ADMINS = (
    ('Admin', 'admin@tvoy_style.com'),
)


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'dezigner20@gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dezigner20@gmail.com'
EMAIL_HOST_PASSWORD = 'SSDD24869317SSDD**'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = 587
