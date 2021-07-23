import configparser

config=configparser.RawConfigParser()
config.read("..\\Configurations\\config.ini")


class ReadConfig:
    
    @staticmethod
    def getConfigData(data):
        datavalue = config.get("common info",data)
        return datavalue