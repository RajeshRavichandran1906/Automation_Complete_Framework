'''
Created on Aug 10, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050554
Description : Verify selected column inside the filter window should be autofit and move along anywhere in the browser.
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity
import unittest
import time
from selenium.webdriver import ActionChains


class C2050554_TestClass(BaseTestCase):

    def test_C2050554(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050554'
        """s
            Step 01: Execute the attached ahtmltab.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("ahtmltab.fex", "S7068", 'mrid', 'mrpass')
        innerHeight = self.driver.execute_script("return window.innerHeight")
        availHeight = self.driver.execute_script("return screen.availHeight")
        browser_height = availHeight - innerHeight
        utillity.UtillityMethods.browser_y=browser_height
        header_css="table[id='IWindowBody0'] .arGridBar table>tbody table tbody tr td:nth-child(2)"
        utillobj.synchronize_with_visble_text(header_css, "13of13records,Page1of1", 65, 1)
        
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', "Step 01: Execute the ahtmltab.fex - Top Head line verification Table 1")
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 01: Execute the ahtmltab.fex - Top Head line verification Table 2")
        miscelanousobj.verify_page_summary(2, '10of10records,Page1of1', "Step 01: Execute the ahtmltab.fex - Top Head line verification Table 3")
        miscelanousobj.verify_page_summary(3, '18of18records,Page1of1', "Step 01: Execute the ahtmltab.fex - Top Head line verification Table 4")
        
        utillobj.verify_data_set('ITableData0','I0r','ahtmltab_table1.xlsx',"Step 01: Verify table loaded data correctly table1")
        utillobj.verify_data_set('ITableData1','I1r','ahtmltab_table2.xlsx',"Step 01: Verify table loaded data correctly table2")
        utillobj.verify_data_set('ITableData2','I2r','ahtmltab_table3.xlsx',"Step 01: Verify table loaded data correctly table3")
        utillobj.verify_data_set('ITableData3','I3r','ahtmltab_table4.xlsx',"Step 01: Verify table loaded data correctly table4")
        
        #utillobj.create_data_set('ITableData0','I0r','ahtmltab_table1.xlsx')
        #utillobj.create_data_set('ITableData1','I1r','ahtmltab_table2.xlsx')
        #utillobj.create_data_set('ITableData2','I2r','ahtmltab_table3.xlsx')
        #utillobj.create_data_set('ITableData3','I3r','ahtmltab_table4.xlsx')
        

        
        """Step 02 : Click on any column dropdown menu like 'Country'"""
        """Step 03: Select Global filter option"""
        
#         miscelanousobj.select_menu_items('ITableData0', "0", "Global Filter")'
        ele=self.driver.find_element_by_css_selector("#ITableData0  #popid0_0 img")
        utillobj.default_click(ele)
        
        ele = self.driver.find_element_by_css_selector("#dt0_0_0[style*='block'] table tr#t0_0_0_3")
        utillobj.default_click(ele)
        time.sleep(4)

        """ Step 04: Click on 'Add condition', and you can see CAR option"""
       
        filterselectionobj.filter_button_click('Add Condition')
       
        time.sleep(2)
        
        #Verify Car option
        css = 'td[title="CAR"]'
        s = driver.find_element_by_css_selector(css).is_displayed()
        utillobj.asequal(True,s,'Step 04: Click on Add condition and you can see CAR option')
        
        
        """Step 05: Move the global filter window to bottom of the browser,and select 'Add Condition' """
        
        s_new = driver.find_element_by_css_selector(css)
        s = s_new.location['y']
        elm = driver.find_element_by_css_selector("#wall1 [class=arWindowBar]")
        action = ActionChains(driver)
        action.drag_and_drop_by_offset(elm,600,650).perform()
        time.sleep(5)
        filterselectionobj.filter_button_click('Add Condition')
        time.sleep(2)
        s2_new = driver.find_element_by_css_selector(css)
        s2 = s2_new.location['y']
        
        if s!=s2:
            s3 = False
        else: 
            s3= True
        utillobj.asequal(False,s3, 'Step 05: Verify selected column inside the filter window should be autofit and move along anywhere in the browser.')
        

        
if __name__ == '__main__':
    unittest.main()        
               
        
        
        
        
        
        
        
        