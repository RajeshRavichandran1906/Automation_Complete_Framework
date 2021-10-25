'''
Created on Jan, 31 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203735

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_tools
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os, subprocess
import time
from selenium.webdriver.support.color import Color

class C2203735_TestClass(BaseTestCase):

    def test_C2203735(self):
        
        """
            Step 01: Execute the AR-RP-001.fex
        """
        Test_Case_ID="C2203735"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        
        """
        Step 01: Execute each attached fex to display the three different formats AHTML/AFLEX/APDF
        """
        utillobj.active_run_fex_api_login("135782_ahtml.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(20)
        utillobj.take_screenshot(driver.find_element_by_css_selector('#orgdiv0.activeReport'), Test_Case_ID+'_Actual_step01_AHTML', image_type='actual', x=1, y=1, w=-1, h=-1)
        time.sleep(3)
        utillobj.infoassist_api_logout()
        time.sleep(2) 
        utillobj.active_run_fex_api_login("135782_apdf.fex", "S7072", 'mrid', 'mrpass')
        time.sleep(20)
        if browser == 'IE':
            utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_step01_APDF_'+browser, image_type='actual', left=20, top=90, right=30, bottom=70)
        else:
            utillobj.take_screenshot(driver.find_element_by_css_selector('html body'), Test_Case_ID+'_Actual_step01_APDF_'+browser, image_type='actual', x=1, y=1, w=-1, h=-1)
        
        time.sleep(3)
        utillobj.infoassist_api_logout()
        #AFLEX can't be done in my local computer due to Flash.
        
if __name__ == '__main__':
    unittest.main()  
            
            
            
            
        