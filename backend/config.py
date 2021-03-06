from datetime import timedelta
import os


PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))


class Config:
    DEBUG = False
    SECRET_KEY = 'iQfPvB6sZaNHqVFI5CJa9rM1xOEVHKIM0LwifT04yLsPlZhSSvaDuZXOgJFSpJVq'
    SECURITY_TRACKABLE = False
    JWT_EXPIRATION_DELTA = timedelta(days=7)
    DATABASE = {
        'name': 'database.db',
        'engine': 'peewee.SqliteDatabase',
    }

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    DEBUG = True
    SECURITY_PASSWORD_SALT = 'tilda'
    CORS_RESOURCES = {r"/api/*": {"origins": "*"}}
    SECURITY_SEND_REGISTER_EMAIL = False


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass


configs = {
    'dev': DevConfig,
    'testing': TestConfig,
    'prod': ProdConfig,
    'default': Config
}
