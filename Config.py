# -*- coding: utf-8 -*-
#!/usr/bin/python

import configparser

def ConfigParser():
    config = configparser.RawConfigParser()
    config.read('config.conf')
    return config

def GetTheConfig(category, item):
    config = ConfigParser()
    result = config.get(category, item)
    return result

def WriteTheConfig(category, item, value):
    config = ConfigParser()
    config.set(category, item, value)
    with open('config.conf', 'wb') as configfile:
        config.write(configfile)
