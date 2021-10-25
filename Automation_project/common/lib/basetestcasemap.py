# Requirement1. :pip install pynput
# Requirement2.: Create a separate basetestcase_map.py, because we need separate setting for IE in maps. 

import unittest, time
from selenium import webdriver
from common.lib.utillity import UtillityMethods
from common.lib import utillity
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


class BaseTestCaseMap(unittest.TestCase):

    def setUp(self):
        UtillityMethods.asert_failure_count=0
        browser = UtillityMethods.parseinitfile(self,'browser')
        browser_driver = UtillityMethods.parseinitfile(self,'browser_driver')
        if browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'Chrome':
            options = webdriver.ChromeOptions()
            prefs = {"download.prompt_for_download": True}
            options.add_experimental_option("prefs", prefs)
            options.add_argument('--disable-print-preview')
            options.add_argument('--disable-infobars')
            self.driver = webdriver.Chrome(browser_driver,chrome_options=options)                                    
            
        elif browser == 'IE':
            cap = DesiredCapabilities.INTERNETEXPLORER
            #cap['enablePersistentHover'] = False
            cap['requireWindowFocus']=True
            #cap['nativeEvents']= True
            self.driver = webdriver.Ie(capabilities=cap)
        elif browser == 'Edge':
            cap = DesiredCapabilities.EDGE
            cap['pageLoadStrategy'] = "eager"
            self.driver = webdriver.Edge(capabilities=cap)
        elif browser == 'Safari':
            self.driver = webdriver.Safari()
        else:
            print('Verify Browser may not defined in config')
        self.driver.maximize_window()
        

    def tearDown(self):
        filename = os.getcwd() + "\\failure_captures\\"+ self._testMethodName + ".png"
        for method, error in self._outcome.errors:
            if error:
                self.driver.save_screenshot(filename)
        utillobj = utillity.UtillityMethods(self.driver)
        utillobj.infoassist_api_logout()
        #self.driver.close()
        time.sleep(2)
        self.driver.quit()
        if UtillityMethods.asert_failure_count>0:
            self.fail('Verification check point failed')


