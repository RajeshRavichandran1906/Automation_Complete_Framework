'''
Created on Jul 26, 2016

@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050509
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity

class C2050509_TestClass(BaseTestCase):

    def test_C2050509(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2050509'
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
        
        """Select INTEGER, then MAX, then FILTER, then LESS THAN OR EQUAL TO, then select value of 10"""
        miscelanousobj.select_menu_items('ITableData0', "0", "Calculate","Max")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1000")
        
        miscelanousobj.select_menu_items('ITableData0', "0", "Filter", "Less than or equal to")
        filterselectionobj.create_filter(1, "Less than or equal to", "large",value1="10")
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Max 10(1%)\nTotal Max 1000", True, "Step 02: Expect to see Total Max 1000, and Filtered Max 10")
        filterselectionobj.close_filter_dialog()
        
        """Select DATE YYMD, then MAX, then FILTER, then NOT EQUAL, then select value of 1996/06/01"""
        miscelanousobj.select_menu_items('ITableData0', "2", "Calculate","Max")
        miscelanousobj.verify_calculated_value(4, 3,"Total Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1000 after adding 2nd calculate field")
        
        miscelanousobj.select_menu_items('ITableData0', "2", "Filter","Not equal")
        filterselectionobj.create_filter(1, "Not equal", "small",value1="1996/06/01")
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 3,"Filtered Max 1996/05/01\nTotal Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01, and Filtered Max 1996/05/01") 
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Max 900(90%)\nTotal Max 1000", True, "Step 02: Expect to see Total Max 1000, and Filtered Max 900(90%) after adding 2nd filter field")
        filterselectionobj.close_filter_dialog()
        
        """Select D10.2, then MAX, then FILTER, then LESS THAN, then select value of 76.00"""
        
        miscelanousobj.select_menu_items('ITableData0', "5", "Calculate","Max")
        miscelanousobj.verify_calculated_value(4, 6,"Total Max 140.00",True,"Step 02: Expect to see Total Max 140.00")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1000 after adding 3rd calculate field")
        miscelanousobj.verify_calculated_value(4, 3,"Total Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01 after adding 3rd calculate field")
         
        miscelanousobj.select_menu_items('ITableData0', "5", "Filter","Less than")
        filterselectionobj.create_filter(1, "Less than", "small",value1="76.00")
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Max 58.00(41.43%)\nTotal Max 140.00", True, "Step 02: Expect to see Total Max 140.00 and Filtered Max 58.00")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Max 1000(100%)\nTotal Max 1000", True, "Step 02: Expect to see Total Max 1000, and Filtered Max 1,000(100%) after adding 3rd filter field")
        miscelanousobj.verify_calculated_value(4, 3,"Filtered Max 1996/06/01\nTotal Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01, and Filtered Max 1996/06/01 after adding 3rd filter field")
        filterselectionobj.close_filter_dialog()
        
        """Select P9.2M, then MAX, then FILTER, then LESS THAN, then select value $30.00"""
        
        miscelanousobj.select_menu_items('ITableData0', "6", "Calculate","Max")
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00", True, "Step 02: Expect to see Total Max $1,139.00")
        miscelanousobj.verify_calculated_value(4, 6,"Total Max 140.00",True,"Step 02: Expect to see Total Max 140.00 adding 4th calculate field")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1000 after adding 4th calculate field")
        miscelanousobj.verify_calculated_value(4, 3,"Total Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01 after adding 4th calculate field")
         
        miscelanousobj.select_menu_items('ITableData0', "6", "Filter","Less than")
        filterselectionobj.create_filter(1, "Less than", "large",value1="$30.00")
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 7,"Filtered Max $25.00(2.19%)\nTotal Max $1,139.00",True,"Step 02: Expect to see Total Max $1,139.00 and Filtered Max $25.00")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Max 12(1.2%)\nTotal Max 1000", True, "Step 02: Expect to see Total Max 1000, and Filtered Max 12(1.2%) after adding 4th filter field")
        miscelanousobj.verify_calculated_value(4, 3,"Filtered Max 1996/01/01\nTotal Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01, and Filtered Max 1996/01/01 after adding 4th filter field")
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Max 13.00(9.29%)\nTotal Max 140.00", True, "Step 02: Expect to see Total Max 140.00 and Filtered Max 13.00(9.29%) after adding 4th filter field")
        filterselectionobj.close_filter_dialog()
        
        """Select DATETIME, then MAX, then FILTER, then EQUALS, then select value 2013/10/04 1:02:03AM"""
        
        miscelanousobj.select_menu_items('ITableData0', "7", "Calculate","Max")
        miscelanousobj.verify_calculated_value(4, 8,"Total Max 2013/10/04 1:02:03AM",True,"Step 02: Expect to see Total Max 2013/10/04 1:02:03AM")
        miscelanousobj.verify_calculated_value(4, 6,"Total Max 140.00",True,"Step 02: Expect to see Total Max 140.00 adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 02: Expect to see Total Max 1000 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 3,"Total Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01 after adding 5th calculate field")
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00", True, "Step 02: Expect to see Total Max $1,139.00 after adding 5th calculate field")
        
        miscelanousobj.select_menu_items('ITableData0', "7", "Filter","Equals")
        filterselectionobj.create_filter(1, "Equals", "small",value1="2013/10/04 1:02:03AM")
        filterselectionobj.filter_button_click("Filter")
        
        miscelanousobj.verify_calculated_value(4, 8,"Filtered Max 2013/10/04 1:02:03AM\nTotal Max 2013/10/04 1:02:03AM",True,"Step 02: Expect to see Total Max 2013/10/04 1:02:03AM and Filtered Max 2013/10/04 1:02:03AM")
        miscelanousobj.verify_calculated_value(4, 1, "Filtered Max 1000(100%)\nTotal Max 1000", True, "Step 02: Expect to see Total Max 1000, and Filtered Max 1,000(100%) after adding 5th filter field")
        miscelanousobj.verify_calculated_value(4, 3,"Filtered Max 1996/06/01\nTotal Max 1996/06/01",True,"Step 02: Expect to see Total Max 1996/06/01, and Filtered Max 1996/06/01 after adding 5th filter field")
        miscelanousobj.verify_calculated_value(4, 6, "Filtered Max 140.00(100%)\nTotal Max 140.00", True, "Step 02: Expect to see Total Max 140.00 and Filtered Max 140.00(100%) after adding 5th filter field")
        miscelanousobj.verify_calculated_value(4, 7,"Filtered Max $1,139.00(100%)\nTotal Max $1,139.00",True,"Step 02: Expect to see Total Max $1,139.00 and Filtered Max $1,139.00(100%) after adding 5th filter field")
        filterselectionobj.close_filter_dialog()
        
        """
            Step 03: End the Filter panel in preparation for the next field in the GROUP.
            Make sure the report is positioned at Page 1.
        """
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', 'Step 03: Expect full report to be displayed again. 1000 rows')
        
        miscelanousobj.verify_calculated_value(4, 1,"Total Max 1000",True,"Step 03: Expect to see Total Max 1000")
        miscelanousobj.verify_calculated_value(4, 3,"Total Max 1996/06/01",True,"Step 03: Expect to see Total Max 1996/06/01")
        miscelanousobj.verify_calculated_value(4, 6,"Total Max 140.00",True,"Step 03: Expect to see Total Max 140.00")
        miscelanousobj.verify_calculated_value(4, 7, "Total Max $1,139.00", True, "Step 03: Expect to see Total Max $1,139.00")
        miscelanousobj.verify_calculated_value(4, 8,"Total Max 2013/10/04 1:02:03AM",True,"Step 03: Expect to see Total Max 2013/10/04 1:02:03AM")
        
if __name__ == '__main__':
    unittest.main()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        