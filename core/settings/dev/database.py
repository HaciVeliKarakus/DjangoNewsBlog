from core.settings.dev.common import BASE_DIR

DATABASES = {
    'default': dict(ENGINE='django.db.backends.sqlite3', NAME=BASE_DIR / 'db.sqlite3')
}
