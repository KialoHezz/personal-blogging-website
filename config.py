class config:
    pass

class DevConfig(config):
    DEBUG = True

class ProdConfig(config):
    pass

config_options = {
    'development': Devconfig,
    'production': ProdConfig
}