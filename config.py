class BasicConfig(object):
    DEBUG = True
    TESTING = False
    
class ProductionConfig(BasicConfig):
    DEBUG = False

class DevelopmentConfig(BasicConfig):
    DEBUG = True
    TESTING = True