import os

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATION = True

    

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hezzy:kialo@localhost/persblog'
    DEBUG = True

class ProdConfig(Config):
    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}