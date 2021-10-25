'''
Created on Aug 17, 2017

@author: em14675
'''
from selenium import webdriver
from configparser import ConfigParser
from common.lib.configfiles import settings
from os.path import os
import sys
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
        option = 'executables_path'
        section = 'ie'
        targetPath = parser.get(section, option)
        sys.path.append(targetPath)
        cap = DesiredCapabilities.INTERNETEXPLORER
        cap['requireWindowFocus']=bool(parser[section]['requireWindowFocus'])
        option = 'executables_path'
        targetPath = parser[section][option]    
        option = 'executable'
        ieTargetExec = parser[section][option]
        targetExec = targetPath + ieTargetExec
        return webdriver.Ie(executable_path=targetExec, capabilities=cap)
