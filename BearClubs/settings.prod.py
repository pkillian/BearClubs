try:
    from shared_settings import *
except ImportError:
    pass

# HEROKU
import dj_database_url
DATABASES['default'] = dj_database_url.config();
