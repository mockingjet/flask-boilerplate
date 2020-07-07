import os
from datetime import timedelta

getenv = os.environ.get

DEFAULT_DBURI = 'postgresql+psycopg2://postgres:ciPs1618@192.168.66.65:5432/petertsai'


class Config(object):
    """Base configuration."""

    SECRET = getenv('SECRET', 'secret')
    DATABASE_URI = getenv('DATABASE_URI', DEFAULT_DBURI)


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    """Test configuration."""

    ENV = 'test'
    DEBUG = True
    TESTING = True


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    TESTING = False
