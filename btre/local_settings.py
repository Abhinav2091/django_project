# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a+v-x3)9z$%+r+hcmyui82uvjjf!s7=e(7su-sv$*)&l-+-0cfal('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['139.59.15.101']

DATABASES = {
            'default': {
                        'ENGINE': 'django.db.backends.postgresql',
                                'NAME': 'btre_prod',
                                        'USER':'dbadmin',
                                                'PASSWORD':'1234!',
                                                        'HOST':'localhost'
                                                            }
            }
#Email config
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='YourFrom email'
EMAIL_HOST_PASSWORD='password'
EMAIL_USE_TLS=True
