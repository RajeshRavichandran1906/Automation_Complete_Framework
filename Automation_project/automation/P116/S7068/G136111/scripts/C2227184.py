'''
Created on April 10, 2017

@author: AAKhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227184
Description : AHTML:Filter Cell - Highlight Row - selects no or wrong row(Project 129369)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea
from common.lib import utillity
import unittest, time
from selenium.webdriver.common.action_chains import ActionChains


class C2227184_TestClass(BaseTestCase):

    def test_C2227184(self):
        driver = self.driver #Driver reference object created'
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        browser = utillobj.parseinitfile('browser')
        
        
        """ Step 1: Execute the attached fex. 129369.fex        """
        utillobj.active_run_fex_api_login("129369.fex", "S7068", 'mrid', 'mrpass')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        time.sleep(7)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'DEALER_COST', 'RETAIL_COST']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 01.1: Verify all columns listed on the report act-1067.fex')
        miscelanousobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.2: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227184_DS01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227184_DS01.xlsx','Step 01.3: Verify data set')
        
        
        
        """ Step 2: In the report select a cell with value SEDAN and execute 'Filter Cell'         """
        miscelanousobj.select_field_menu_items('ITableData0', 1, 3,'Filter Cell')
        time.sleep(2)
        parent_css="#MAINTABLE_wbody0 span[title='Move to Bottom'] img"
        result_obj.wait_for_property(parent_css, 1)
        column_list=['COUNTRY', 'CAR', 'MODEL', 'BODYTYPE', 'DEALER_COST', 'RETAIL_COST']
        miscelanousobj.verify_column_heading("ITableData0", column_list, 'Step 02: Verify all columns listed on the report act-1067.fex')
        miscelanousobj.verify_page_summary(0, '13of18records,Page1of1', "Step 02.1: Verify Page Summary")
#         utillobj.create_data_set('ITableData0', 'I0r', 'C2227184_DS02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2227184_DS02.xlsx','Step 02.2: Verify data set')
        
        
        """ Step 3: Now select a row and execute 'Highlight row'.        """
        miscelanousobj.select_field_menu_items('ITableData0', 1, 3,'Highlight Row')
        
        
        """ Step 4: Verify row is highlighted as expected.                """
        element=driver.find_element_by_css_selector('table[id="IWindowBody0"] .arGridBar')
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(element)
        else:
            action=ActionChains(driver)
            action.move_to_element(element).perform()
            time.sleep(2)
            del action
        time.sleep(3)
        miscelanousobj.verify_highlighted_rows('ITableData0', 1, 'Step 04: Verify row is highlighted as expected.')
        time.sleep(2)
        
        

if __name__ == "__main__":
    unittest.main()