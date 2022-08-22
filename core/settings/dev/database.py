import os

from core.settings.dev.common import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR.parent, 'db.sqlite3'),
    }
}
