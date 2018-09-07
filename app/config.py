class Config:
    '''
    General configuration parent class - this is where configurations that are common across all encironments are
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

#     app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }