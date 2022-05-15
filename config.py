import os

class config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kialo:12345@localhost/persblog'

class DevConfig(config):
    DEBUG = True

class ProdConfig(config):
    pass

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}