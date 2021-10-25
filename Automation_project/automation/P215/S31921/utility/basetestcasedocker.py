'''
Created on Mar 20, 2019

@author: ml12793

@Description: base test case for smoke test using selenium grid
'''

import unittest, time
from utility.selenium_utility import Selenium_Utility
from selenium import webdriver
import os
import sys

class BaseTestCaseDocker(unittest.TestCase):
   
    def setUp(self):
        se_grid_env = Selenium_Utility.parseinitfile(self,'se_grid_env')
        se_grid_url = Selenium_Utility.parseinitfile(self,'se_grid_url')
        if se_grid_env == 'NA':
            self.driver = webdriver.Chrome()
        else:
            if se_grid_env == 'Docker':
                platform = 'Linux'
            if se_grid_env == 'VMImage':
                platform = 'Windows'
            self.driver = webdriver.Remote(
                        command_executor = se_grid_url,
                        desired_capabilities = { 
                            "browserName": "chrome",
                            "platform": platform
                            }
                    )
        self.driver.maximize_window()   

    def tearDown(self):
        filename_obj = self._testMethodName 
        if sys.platform == 'linux':
            file_path = os.getcwd() + '/failure_capture/'
        else:
            file_path = os.getcwd() + '\\failure_capture\\'
        for method, error in self._outcome.errors:
            if error:
                try:
                    self.driver.save_screenshot(file_path + filename_obj + '.png')            
                except:
                    print("Exception in save_screenshot")
        try:
            self.logout_webfocus()
        except:
            pass
        time.sleep(2)
        self.driver.quit()
    
    def logout_webfocus(self): 
        try:
            Selenium_Utility.logout_wf(self)
        except:
            pass