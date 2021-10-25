'''
Created on Aug 17, 2017

@author: em14675
'''
from selenium import webdriver
from configparser import ConfigParser
from common.lib.configfiles import settings
from os.path import os
import sys

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
        section = 'chrome'      
        option = 'docker_executables_path' if sys.platform == 'linux' else 'executables_path'
        targetPath = parser[section][option]    
        option = 'docker_executable' if sys.platform == 'linux' else 'executable'
        chromeTargetExec = parser[section][option]
        targetExec = targetPath + '/' + chromeTargetExec if sys.platform == 'linux' else targetPath + r'\\' + chromeTargetExec
        options = webdriver.ChromeOptions()
        prefs = {"download.prompt_for_download": bool(parser[section]['prompt_for_download'])}
        options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        opts=parser[section]['argument'].split(',')
        for opt in opts:
            options.add_argument(opt)
        return webdriver.Chrome(executable_path=targetExec, chrome_options=options)