class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY='2312453I435NDFVF22224'

class ProdConfig(Config):
    '''
    Production configuration child class
    Args: 
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args: 
        Config: The parent configuration class with general configuration settings
    '''
    DEBUG = True