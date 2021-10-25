'''
Created on Nov 22, 2017

@author: AA14564
'''
from selenium import webdriver
from configparser import ConfigParser
from common.lib.configfiles import settings
from os.path import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class DriverLauncher(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def execute(self):
        configFile = 'config.ini'
        parser = ConfigParser()
        parser.read(os.path.join(settings.CONFIG_ROOT, configFile))               
        section = 'edge'
        option = 'pageLoadStrategy'
        pageLoadStrategy_ = parser[section][option]    
        cap = DesiredCapabilities.EDGE
        cap['pageLoadStrategy'] = pageLoadStrategy_
        option = 'executables_path'
        targetPath = parser[section][option]    
        option = 'executable'
        edgeTargetExec = parser[section][option]
        targetExec = targetPath + edgeTargetExec
        #return webdriver.Edge(executable_path=targetExec, capabilities=cap)
        return webdriver.Edge(capabilities=cap)