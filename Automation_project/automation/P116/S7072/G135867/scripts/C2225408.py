'''
Created on Jan31, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7072&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2225408

'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.lib.global_variables import Global_variables


class C2225408_TestClass(BaseTestCase):

    def test_C2225408(self):

        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        browser = Global_variables.browser_name
        
        """
        Step 1. Execute the AR-RP-001.fex
        
        """
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7072", 'mrid', 'mrpass')
        utillobj._validate_page((By.ID,'ITableData0'))
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 01.01: Verified the Page Summary')
        column_list=['Category', 'Product','Product ID','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.02: Verified Column Heading')
        utillobj.verify_data_set('ITableData0','I0r','AR-RP-001.xlsx','Step 01.03: Data set verified')
        
        """"
        Step 2 :Right click on the report.
        
        Verify Context menu pop up is opened. That shows these sub menus: 
        - Comments 
        - Highlight Value 
        - Highlight Row 
        - Unhighlight All 
        - Filter Cell.
        
        """
        miscelanousobj.verify_field_menu_items("ITableData0", 5, 3, ['Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell'], "Step 02.01: Verified Context menu pop up is opened and sub menus are shown as expected")
        
        """
        Step 3. Click Highlight Row option on a particular row
        
        Verify user can highlight particular row in the report and user can highlight more than one row in the report.
            
        """
        miscelanousobj.select_field_menu_items('ITableData0', 5, 3,'Highlight Row')
        miscelanousobj.select_field_menu_items('ITableData0', 8, 2,'Highlight Row')
        
        
        element=driver.find_element_by_css_selector('table[id="IWindowBody0"] .arGridBar')
        if browser == 'firefox':
            utillobj.click_type_using_pyautogui(element)
        else:
            action=ActionChains(driver)
            action.move_to_element(element).perform()
            time.sleep(2)
            del action
        time.sleep(5)
        miscelanousobj.verify_highlighted_rows('ITableData0', 2, 'Step 03.01: Verified user can highlight particular row in the report and user can highlight more than one row in the report.')
        

if __name__=='__main__' :
    unittest.main()