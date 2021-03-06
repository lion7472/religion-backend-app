import os
from datetime import timedelta


class Config(object):
    """
    Default Configuration
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'ASDASDOWIQ!@&EQHC<XNYWGYW#!@')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 'postgres://admin:islamic9251@localhost/religion')

    INSTALLED_APPS = [
        'user',
        'video',
        'category',
        'version',
        'sound',
        'device',
        'book'
    ]

    UPLOAD_FILE = os.environ.get(
        'UPLOAD_FILE', '/home/omid/Desktop/project/religion_app/upload/')

    # MAX_DOWNLOAD_SIZE = 100 * 1024 * 1024  # 100 MB

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_HEADER_TYPE = 'JWT'


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    DEBUG = True


class DeploymentConfig(Config):
    """
    Deployment Confugartion
    """
    DEBUG = False
