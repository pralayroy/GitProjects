import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    passWord = 'Santu@roy123'
    return passWord
