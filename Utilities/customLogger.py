import logging
import inspect
import logging.config

class CustomLogger:
    @staticmethod
    def getCustomLogger():
        
        logging.config.fileConfig('..\\Configurations\\loggerConfigurations.ini')
        testmethod = inspect.stack()[1][3]
        logger = logging.getLogger(testmethod)
        return logger
    
