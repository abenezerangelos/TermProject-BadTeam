import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app//View//static')
    TEMPLATE_FOLDER = os.path.join(basedir, 'app//View//templates')


class TestConfig(object):
    # SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(basedir, 'test.db')
    # SECRET_KEY = 'bad-bad-key'
    # ROOT_PATH = basedir
    # STATIC_FOLDER = os.path.join(basedir, 'app//View//static')
    # TEMPLATE_FOLDER = os.path.join(basedir, 'app//View//templates')
    # WTF_CSRF_ENABLED = False
    # DEBUG = True
    # TESTING = True

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app//View//static')
    TEMPLATE_FOLDER = os.path.join(basedir, 'app//View//templates')
    TESTING = True