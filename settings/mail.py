ADMINS = (
    ('Admin', 'admin@tvoy_style.com'),
)

# # EMAIL_HOST = ''
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = ''
# EMAIL_USE_TLS = ''
# DEFAULT_FROM_EMAIL = 'robot@tvoy_style.com'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'skylifewww@gmail.com'
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'skylifewww@gmail.com'
EMAIL_HOST_PASSWORD = 'skywww123'
EMAIL_PORT = 587
