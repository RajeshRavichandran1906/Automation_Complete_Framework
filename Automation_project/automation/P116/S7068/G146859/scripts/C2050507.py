'''
Created on Jul 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050507
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity
from selenium import webdriver
import time

class C2050507_TestClass(BaseTestCase):

    def test_C2050507(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050507'
        """
            Step 01: Execute the AR-RP-141CA.fex
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login("AR-RP-141CA.fex", "S7068", 'mrid', 'mrpass')
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 01: Step 01: Execute the AR-RP-141CA.fex")
        columns1=['Order Number INTEGER','ALPHA Store Code','Date YYMD','Date MDYY','Date DMYY','D10.2 Unit Price','P9.2M Unit Price', 'DATETIME HYYMDSA']
        miscelanousobj.verify_column_heading("ITableData0", columns1, 'Step 01: Verify all columns listed on the report')

        
        """
            Step 02: Expect to see options Clear, Clear All, Sum, Avg, Min, Max, Count, Distinct, % of Total.
        """
        option = ['Clear','Clear All','Sum','Avg','Min','Max','Count','Distinct','% of Total']
        miscelanousobj.verify_menu_items('ITableData0', 0, "Calculate", option,"Step 02: Step 02: Expect to see all options")
         
        """ Select INTEGER, then MIN, then FILTER, then GREATER THAN OR EQUAL TO, then select value of 25."""
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Min")
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1")
         
        miscelanousobj.select_menu_items('ITableData0', "0", "Filter","Greater than or equal to")
        filterselectionobj.create_filter(1, 'Greater than or equal to', 'large',value1='25')
        filterselectionobj.filter_button_click("Filter")
         
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Min 25(2500%)\nTotal Min 1", True, "Step 02: Expect to see Total Min 1, and Filtered Min 25")
        filterselectionobj.close_filter_dialog()
         
        """Select DATE, then MIN, then FILTER, then NOT EQUAL, then select value of 19960101"""
        miscelanousobj.select_menu_items('ITableData0', "2", "Calculate","Min")
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see 1996/01/01")
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1 after adding 2nd calculate field")
          
        miscelanousobj.select_menu_items('ITableData0', "2", "Filter","Not equal")
        filterselectionobj.create_filter(1, 'Not equal', 'small',value1='1996/01/01')
        filterselectionobj.filter_button_click("Filter")
         
        miscelanousobj.verify_calculated_value(4, 3, "Filtered Min 1996/02/01\nTotal Min 1996/01/01", True, "Step 02: Expect to see Total Min 19960101, and Filtered Min 19960201")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Min 181(18100%)\nTotal Min 1", True, "Step 02: Expect to see the Integer field changes after adding 2nd filtered field")
        filterselectionobj.close_filter_dialog()
         
        """Select D10.2, then MIN, then FILTER, then GREATER THAN, then select value of 76.00"""
         
        miscelanousobj.select_menu_items('ITableData0', "5", "Calculate","Min")
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00")
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1 after adding 3rd calculate field") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see 1996/01/01 after adding 3rd calculate field")
         
        miscelanousobj.select_menu_items('ITableData0', "5", "Filter","Greater than")
        filterselectionobj.create_filter(1, 'Greater than', 'small',value1='76.00')
        filterselectionobj.filter_button_click("Filter")
         
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Min 81.00(623.08%)\nTotal Min 13.00", True, "Step 02: Expect to see Total Min 13.00 and Filtered Min 81.00")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Min 3(300%)\nTotal Min 1", True, "Step 02: Expect to see the Integer field changes after adding 3rd filtered field")
        miscelanousobj.verify_calculated_value(4, 3, "Filtered Min 1996/01/01\nTotal Min 1996/01/01", True, "Step 02: Expect to see Date field changes after adding 3rd filtered field")
        filterselectionobj.close_filter_dialog()
         
        """Select P9.2M, then MIN, then FILTER, then GREATER THAN, then select value $63.00"""
         
        miscelanousobj.select_menu_items('ITableData0', "6", "Calculate","Min")
        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", True, "Step 02: Expect to see Total Min $24.00")
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1 after adding 4th calculate field") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see 1996/01/01 after adding 4th calculate field")
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00 after adding 4th calculate field") 
         
        miscelanousobj.select_menu_items('ITableData0', "6", "Filter","Greater than")
        filterselectionobj.create_filter(1, 'Greater than', 'large',value1='$63.00')
        filterselectionobj.filter_button_click("Filter")
         
        miscelanousobj.verify_calculated_value(4, 7,"Filtered Min $69.00(287.5%)\nTotal Min $24.00",True,"Step 02: Expect to see Total Min $24.00 and Filtered Min $69.00")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Min 3(300%)\nTotal Min 1", True, "Step 02: Expect to see the Integer field changes after adding 4th filtered field")
        miscelanousobj.verify_calculated_value(4, 3, "Filtered Min 1996/01/01\nTotal Min 1996/01/01", True, "Step 02: Expect to see Date field changes after adding 4th filtered field")
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Min 13.00(100%)\nTotal Min 13.00", True, "Step 02: Expect to see D10.2 field changes after adding 4th filtered field")
        filterselectionobj.close_filter_dialog()
         
        """Select DATETIME, then MIN, then FILTER, then EQUALS, then select value 2013/10/04 1:02:03AM"""
        miscelanousobj.select_menu_items('ITableData0', "7", "Calculate","Min")
        miscelanousobj.verify_calculated_value(4, 8, "Total Min 2002/12/31 11:59:59PM", True, "Step 02: Expect to see Total Min 2002/12/31 11:59:59PM")
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 02: Expect to see Total Min 1 after adding 5th calculate field") 
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 02: Expect to see 1996/01/01 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00 after adding 5th calculate field") 
        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", True, "Step 02: Expect to see Total Min $24.00 after adding 5th calculate field")
         
        miscelanousobj.select_menu_items('ITableData0', "7", "Filter","Equals")
        filterselectionobj.create_filter(1, 'Equals', 'small',value1='2013/10/04 1:02:03AM')
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 8, "Filtered Min 2013/10/04 1:02:03AM\nTotal Min 2002/12/31 11:59:59PM",True,"Step 02: Expect to see Total Min 2002/12/31 11:59:59PM andFiltered Min 2013/10/04 1:02:03AM")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Min 16(1600%)\nTotal Min 1", True, "Step 02: Expect to see the Integer field changes after adding 5th filtered field")
        miscelanousobj.verify_calculated_value(4, 3, "Filtered Min 1996/01/01\nTotal Min 1996/01/01", True, "Step 02: Expect to see Date field changes after adding 5th filtered field")
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Min 13.00(100%)\nTotal Min 13.00", True, "Step 02: Expect to see D10.2 field changes after adding 5th filtered field")
        miscelanousobj.verify_calculated_value(4, 7,"Filtered Min $39.00(162.5%)\nTotal Min $24.00",True,  "Step 02: Expect to see P9.2M field changes after adding 5th filtered field")
        filterselectionobj.close_filter_dialog()

        """
            Step 03: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03: Expect full report to be displayed again. 1000 rows')
        
        miscelanousobj.verify_calculated_value(4, 1, "Total Min 1", True, "Step 03: Expect to see Total Min 1")
        miscelanousobj.verify_calculated_value(4, 3, "Total Min 1996/01/01", True, "Step 03: Expect to see 1996/01/01")
        miscelanousobj.verify_calculated_value(4, 6, "Total Min 13.00", True, "Step 02: Expect to see Total Min 13.00")
        miscelanousobj.verify_calculated_value(4, 7, "Total Min $24.00", True, "Step 02: Expect to see Total Min $24.00")
        miscelanousobj.verify_calculated_value(4, 8, "Total Min 2002/12/31 11:59:59PM", True, "Step 02: Expect to see Total Min 2002/12/31 11:59:59PM")
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        