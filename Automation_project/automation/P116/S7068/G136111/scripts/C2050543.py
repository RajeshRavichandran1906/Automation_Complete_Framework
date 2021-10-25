'''
Created on Aug 8, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050543
Test case Name = AHTML:Accordian:Expanded/Filter Values Not Calculated (proj 162526)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection, active_pivot_comment
from common.lib import utillity
import unittest,time
from selenium.webdriver import ActionChains

class C2050543_TestClass(BaseTestCase):

    def test_C2050543(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050543'
        """
        Step 01: Execute the attached repro - 162526.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        active_piv=active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login("162526.fex", "S7068", 'mrid', 'mrpass')
        active_misobj.verify_page_summary(0, '18of18records,Page1of1', "Step 01.1: Execute 162526.fex verify Page Summary 18of18")
        active_misobj.verify_column_heading('ITableData0', ['COUNTRY'], "Step 01.2: Verify Column heading of 162526.fex")
        utillobj.verify_data_set('ITableData0','I0r', "162526.xlsx","Step 01.3: Verify 162526.fex dataset")
         
        """
        Step 02: expand England ->Jaguar
        """
        active_misobj.expand_or_colapse_accordian_field('ITableData0', 0, 0)
        active_misobj.expand_or_colapse_accordian_field('ITableData0', 0, 1)
        """Verify Dataset"""
        utillobj.verify_data_set('ITableData0','I0r', "C2050543_Ds01.xlsx","Step 02: Verify dataset after expanding Accordion report")
        
        """
        Step 03: Click on dropdown of DEALER_COST---> Select "CALCULATE"--->SELECT "SUM"
        """
        column_heading_css = "#ITableData0 .arGridColumnHeading > td"
        columns=self.driver.find_elements_by_css_selector(column_heading_css)
        columns[int(3)].click()
        active_misobj.select_menu_items('ITableData0', 3, 'Calculate','Sum')
        """Verify calculated value"""
        active_misobj.verify_calculated_value(2, 4, "Expanded Sum 37,853(26.32%)\nFiltered Sum 143,794(100%)\nTotal Sum 143,794",True, "Step 03: Verify calculated value of DEALER_COST")
        
        """
        Step 04: Click on dropdown of CAR---> Select "CALCULATE"--->SELECT "COUNT"
        """ 
        active_misobj.select_menu_items('ITableData0', 1, 'Calculate','Count')
        """Verify calculated value"""
        active_misobj.verify_calculated_value(2, 2, "Expanded Cnt 4\nFiltered Cnt 18\nTotal Cnt 18",True,"Step 04: Verify Calculated value of CAR")  
         
        """
        Step 05: Verify that Expanded and Filtered values are displayed for calculate functions like as in base they are present.
        """
        utillobj.verify_data_set('ITableData0','I0r', "C2050543_Ds01.xlsx","Step 05: Verify dataset")
        

if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        