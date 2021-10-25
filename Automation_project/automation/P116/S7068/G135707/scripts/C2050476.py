'''
Created on Jul 18, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050476
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,visualization_resultarea
from common.lib import utillity
from selenium import webdriver
import time

class C2050476_TestClass(BaseTestCase):

    def test_C2050476(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050476'
        """
            Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        result_obj=visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-001.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 01: Step 01: Execute the AR-RP-001.fex")
        columns1=['Category','Product ID','Product','State','Unit Sales','Dollar Sales']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')


        """
            Step 02: Click dropdown menu next to Dollar Sales and select Calculate > Sum
            Verify on Calculating Total Sum - TOT is displayed on pagination bar
        """
        miscelanousobj.select_menu_items("ITableData0", "5", "Calculate","Sum")
        miscelanousobj.verify_calculated_value(2, 6, "Total Sum 46156290",True, "Step 02: Verify on Calculating Total Sum - TOT is displayed on pagination bar")
        """
            Step 03: Now filter Dollar Sales column with option 'Equals' and select these values: 198452 208209 227482 256539 Click 'Filter' button
            
            Verify on using Filter option, Filtered Sum SUB is also displayed on pagination bar
        """
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
        filterselectionobj.create_filter(1, "Equals","large",value1="198452",value2="208209",value3="227482",value4="256539")
        filterselectionobj.filter_button_click("Filter")
        time.sleep(2)
        
        miscelanousobj.move_active_popup('1', '600', '200')
        time.sleep(2)
        miscelanousobj.verify_summation("Step 03: Verify summation")
        miscelanousobj.verify_calculated_value(2, 6, "Filtered Sum 890682(1.93%)\nTotal Sum 46156290",True, "Step 03: Verify on using Filter option, Filtered Sum SUB is also displayed on pagination bar") 
        """
            Step 04: Click Toggle icon on the pagination
            Verify Toggle Calculation type switch between SUB/TOT
        """
        self.driver.find_element_by_css_selector("[class='arGridBarCalc']").click()
        parent_css="#ITableData0 tr:nth-child(3) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        utillobj.verify_data_set('ITableData0','I0r','C2050476_Ds01.xlsx','Step 04: Verify Toggle Calculation type switch between TOT')
        miscelanousobj.verify_calculated_value(2, 6, "Total Sum 46156290",True, "Step 04.1: Verify on using Filter option, Filtered Sum TOT is also displayed on pagination bar") 
        miscelanousobj.verify_page_summary(0, 'TOT4of107records,Page1of1', "Step 04.1:Verify Page summary")
                 
        self.driver.find_element_by_css_selector("[class='arGridBarCalc']").click()
        parent_css="#ITableData0 tr:nth-child(3) td:nth-child(1)"
        result_obj.wait_for_property(parent_css, 1, string_value='Coffee', with_regular_exprestion=True)
        utillobj.verify_data_set('ITableData0','I0r','C2050476_Ds01.xlsx',"Step 04.2: Verify Toggle Calculation type switch between SUB")
        miscelanousobj.verify_calculated_value(2, 6, "Filtered Sum 890682",True, "Step 04.2: Verify on using Filter option, Filtered Sum SUB is also displayed on pagination bar") 
        miscelanousobj.verify_page_summary(0, 'SUB4of107records,Page1of1', "Step 04.2:Verify Page summary")
        
        
         
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        