
'''
Created on Aug 12, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050550
Test CaseName = AHTML:Cache:Rpt:Apply filter,create chart throws webpg error(Project 148561)
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,wf_mainpage
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.lib import utillity


class C2050550_TestClass(BaseTestCase):

    def test_C2050550(self):

        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(50) #Intializing common implicit wait for throughout the test
        Test_Case_ID = 'C2050550'
        
        """
        Step 01: Execute the attached repro - 148561.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj = active_filter_selection.Active_Filter_Selection(self.driver)
        mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj.active_run_fex_api_login('148561.fex','S7068','mrid','mrpass')
        active_misobj.verify_page_summary('0','18of18records,Page1of1', 'Step 01.1: Verify Page summary 18of18 records')
        column=['COUNTRY','CAR','DEALER_COST','RETAIL_COST','SALES']
        active_misobj.verify_column_heading('ITableData0',column, "Step 01.2: Verify Column heading")
        utillobj.verify_data_set('ITableData0','I0r','148561.xlsx',"Step 01.3: Verify entire Data set of 148561.fex ran from text editor")
        
        """
        Step 02: From Country dropdown, Apply filter equal to ENGLAND, FRANCE.
        Click Filter
        """ 
        time.sleep(5)
        active_misobj.select_menu_items('ITableData0', '0', 'Filter', 'Equals')       
        time.sleep(5)
        filterobj.create_filter(1, 'Equals',value1='ENGLAND',value2='FRANCE')
        filterobj.verify_filter_selection_dialog(True,'Step 02.1: Verify filter menu MODEL appears','COUNTRY')
        time.sleep(5)
        filterobj.verify_value_selection(1, ['ENGLAND','FRANCE'], "Step 02.2: Verify value is selected")
        filterobj.filter_button_click('Filter')
        active_misobj.verify_page_summary('0','5of18records,Page1of1', 'Step 02.3: Verify Page summary 5of18 records')
        utillobj.verify_data_set('ITableData0','I0r','C2050550_Ds01.xlsx',"Step 02.4: Verify entire Data set of 148561.fex ran from text editor")
        
        """
        Step 03: From Retail_Cost dropdown, Chart--> PIE-->COUNTRY.
        """
        active_misobj.move_active_popup("1", "600", "200")
        time.sleep(3)
        active_misobj.select_menu_items('ITableData0', '3', 'Chart', 'Pie','COUNTRY')
        
        """
        Step 04: Verify value is shown as expected.
        """
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2050550_Actual_Step04.png', image_type='actual_images')
        active_misobj.verify_active_popup_chart_tooltip('wall2', 'pie', 'FRANCE', 'FRANCE=5610(11%)','Pomegranate', "Step 04.1: Verify tooltip FRANCE=5610(11%) and its color")
        time.sleep(5)
        # verify legends
        expected_lgnds_list=['ENGLAND 89%', 'FRANCE 11%']
        if utillobj.parseinitfile('browser')=='IE':
            raiser_css = "#Pie2>div>div[style*='align: left']"
        else:
            raiser_css = "#Pie2>div>div[style*='align:left']"
        lgnds = driver.find_elements_by_css_selector(raiser_css)
        actual_lgnds_list=[]
        for i in range(len(lgnds)):
            actual_lgnds_list.append((lgnds[i].text).strip())
        utillity.UtillityMethods.asequal(self,actual_lgnds_list, expected_lgnds_list,'Step 04.2: Expect to see a legend entry for the PIE chart')
     
        
                        
if __name__ == '__main__':
    unittest.main()
    
