import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Configuration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_REGISTERABLE = True
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://yuriysemesyuk:@localhost:5432/test2'
    SECRET_KEY = "mysecertkey"

    ###flask_security
    SECURITY_PASSWORD_SALT = "salt"
    SECURITY_PASSWORD_HASH = "sha512_crypt"

    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_EMAIL_SENDER = "yuriy.semesyuk@gmail.com"
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = "yuriy.semesyuk@gmail.com"
    MAIL_PASSWORD = '7777820513WUf'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
