# Django settings for  project.
from os import path
from os.path import abspath, dirname, join
import private_settings

DEBUG = True

PROJECT_PATH = abspath(dirname(__file__))

# These email addresses will get all the error email for the production server
# (and any other servers with DEBUG = False )
ADMINS = (
    # ('Aptivate Intranet team', '-team@aptivate.org'),
    ('Marko Samastur', 'markos@aptivate.org'),  # this is in case the above email doesn't work
)

MANAGERS = ADMINS

# DATABASES are configured in local_settings.py.*

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# with big numbers, make 10000 into 10,000
USE_THOUSAND_SEPARATOR = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = path.join(path.dirname(__file__), 'uploads')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/uploads/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = path.join(path.dirname(__file__), 'static')


# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'


# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ('js', join(PROJECT_PATH, '..', '..', 'javascript', 'src')),
    ('dist', join(PROJECT_PATH, '..', '..', 'javascript', 'dist')),
    join(PROJECT_PATH, 'media'),
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'django_assets.finders.AssetsFinder',
)


SECRET_KEY = private_settings.SECRET_KEY


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'waffle.middleware.WaffleMiddleware',
)


TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        path.join(path.dirname(__file__), 'templates'),
        path.join(path.dirname(__file__), '..', '..', 'javascript', 'src', 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',
            'django.template.context_processors.i18n',
            'django.template.context_processors.request',
            'django.template.context_processors.media',
            'django.template.context_processors.static',
            'django.contrib.messages.context_processors.messages',
            'main.context_processors.logframe_list',
            'main.context_processors.deploy_env',
        ],
        'debug': DEBUG,
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]
    }
}]


ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
# WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'rest_framework',
    'django_tables2',  # TODO: don't need this?
    'jstemplate',
    'django_extensions',
    'django_assets',
    'floppyforms',
    'rest_framework_nested',
    # 'waffle',

    # our apps
    'main',
    'logframe',
    'contacts',
    'dashboard',
    'appconf',
    'export',
)

AUTH_USER_MODEL = 'contacts.User'
EMAIL_BOT_ADDRESS = 'blackhole@aptivate.org'
CONTACT_ADDRESS = 'kashana@aptivate.org'
SITE_HOSTNAME = 'localhost:8000'
SITE_NAME = 'Kashana'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': [],  # ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}

JSTEMPLATE_EXTS = ['handlebars']
JSTEMPLATE_DIRS = [
    join(PROJECT_PATH, '..', '..', 'javascript', 'src', 'templates'),
]

# Project Specific Settings
DEFAULT_LOGFRAME_NAME = "Log Frame"
DEFAULT_LOGFRAME_SLUG = "log_frame"

# tasks.py expects to find local_settings.py so the database stuff is there
#--------------------------------
# local settings import
# from http://djangosnippets.org/snippets/1873/
#--------------------------------
try:
    import local_settings
except ImportError:
    print """
    -------------------------------------------------------------------------
    You need to create a local_settings.py file. Run ../../deploy/tasks.py
    deploy:<whatever> to use one of the local_settings.py.* files as your
    local_settings.py, and create the database and tables mentioned in it.
    -------------------------------------------------------------------------
    """
    import sys
    sys.exit(1)
else:
    # OVERRIDE THE TEMPLATE DEBUG SETTING, now that it's been absorbed into TEMPLATES
    TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
    # Import any symbols that begin with A-Z. Append to lists any symbols that
    # begin with "EXTRA_".
    import re
    for attr in dir(local_settings):
        match = re.search(r'^EXTRA_(\w+)', attr)
        if match:
            name = match.group(1)
            value = getattr(local_settings, attr)
            try:
                globals()[name] += value
            except KeyError:
                globals()[name] = value
        elif re.search('^[A-Z]', attr):
            globals()[attr] = getattr(local_settings, attr)
