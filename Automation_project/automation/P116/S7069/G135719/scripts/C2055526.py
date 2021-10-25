
'''
Created on July 29, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7069
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055526
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,wf_legacymainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from common.lib import utillity
from common.pages import visualization_resultarea


class C2055526_TestClass(BaseTestCase):

    def test_C2055526(self):

        driver = self.driver #Driver reference object created
        
        """Step 01:  Run attached 91551.fex from text editor in adhoc page. """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
        self.driver.get(setup_url)
        utillobj.login_wf('mrid','mrpass')
        time.sleep(6)
        wf_mainobj.select_repository_menu('P116->S7069->91551', 'Edit')
        parent_css="#bipEditor #bipEditorArea"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(9)
        wf_mainobj.click_text_editor_ribbon_button('Run')
        """ Window handling"""
        time.sleep(7)
        utillobj.switch_to_window(1)
        time.sleep(12)
        driver.maximize_window()
        time.sleep(7)
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18 records')
        column=['CAR','BODYTYPE', 'DEALER_COST']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Expect to see 2 columns")
        utillobj.verify_data_set('ITableData0','I0r','91551.xlsx',"Step 01.3: Verify entire Data set of 91551.fex ran from text editor")
                 
        """
        Step 02: In report from Car field click dropdown and select calculate->Count/Distinct
        """ 
        time.sleep(5)
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#ITableData0 #popid0_0 img")))
        active_misobj.select_menu_items('ITableData0', '0', 'Calculate', 'Count',x_offset=0, y_offset=-7, browser_height=60)
        s=driver.find_element_by_css_selector(ActiveMiscelaneousLocators.Aggregation).text        
        utillobj.asequal(s,"Total Cnt 18","Step 02: Verify Total Cnt 18") 
        active_misobj.select_menu_items('ITableData0', '0', 'Calculate', 'Distinct',x_offset=0, y_offset=-7, browser_height=60)
         
        """ Step 03: Verify report gets displayed properly without throwing IE error or getting hanged"""
        time.sleep(3)
        s=driver.find_element_by_css_selector(ActiveMiscelaneousLocators.Aggregation).text        
        utillobj.asequal(s,"Total Cnt Dist 10","Step 03.1: Verify Total Cnt Dist 10")
        utillobj.verify_data_set('ITableData0','I0r','91551.xlsx',"Step 03.2: Verify entire Data set after Total")
        time.sleep(3)
        driver.close()
        time.sleep(12)
        utillobj.switch_to_window(0)
        time.sleep(7)
        self.driver.find_element_by_css_selector("#bipEditor [class*='window-close-button']").click()
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()

