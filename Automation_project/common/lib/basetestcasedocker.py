'''
Created on Jan 24, 2019

@author: Ming Li
'''

import unittest, time
from common.lib.utillity import UtillityMethods
from common.lib import global_variables 
from selenium import webdriver
import os

class BaseTestCaseDocker(unittest.TestCase):
   
    def setUp(self):
        se_grid_env = UtillityMethods.parseinitfile(self,'se_grid_env')
        se_grid_url = UtillityMethods.parseinitfile(self,'se_grid_url')
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
        global_variables.Global_variables.current_test_case=self._testMethodName.replace('test_', '').strip()  

    def tearDown(self):
        filename_obj = self._testMethodName 
        file_path = os.getcwd() + '\\failure_captures\\'
        for _, error in self._outcome.errors:
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
            UtillityMethods.switch_to_main_window(self)
            UtillityMethods.infoassist_api_logout(self)
        except:
            pass