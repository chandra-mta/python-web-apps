"""
Flask Application Configuration
"""

import os
from datetime import timedelta
from pathlib import Path

SQLALCHEMY_ECHO = os.getenv('SQLALCHEMY_ECHO') == 'true'
TOPOLOGY_DB_NAME = os.getenv("TOPOLOGY_DB_NAME", "test.db")
TOPOLOGY_DB_DIR = os.getenv("TOPOLOGY_DB_DIR")

if TOPOLOGY_DB_DIR is None:
    #: Relative Path
    DB_URL = f"sqlite:///{TOPOLOGY_DB_NAME}"
else:
    DB_URL = f"sqlite:///{Path(TOPOLOGY_DB_DIR, TOPOLOGY_DB_NAME)}"

class BaseConfig(object):
    #
    # --- Database and CSRF secret key
    #
    SECRET_KEY = 'secret_key_for_test'
    #
    # --- SQLAlchemy
    #
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {'echo': SQLALCHEMY_ECHO}
    #
    # --- Session Settings
    #
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_REFRESH_EACH_REQUEST = True
    SESSION_TYPE = 'sqlalchemy' #: Must set SQLAlchemy instance for session once database connection is instantiated