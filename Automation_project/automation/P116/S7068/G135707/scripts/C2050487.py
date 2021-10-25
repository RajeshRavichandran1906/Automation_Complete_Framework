'''
Created on Jul 22, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050487
TestCase Name = Verify Filtered Avg is displayed when filter is applied to Total Avg
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection
from common.lib import utillity


class C2050487_TestClass(BaseTestCase):

    def test_C2050487(self):
        """
            Step 01: Execute the AR-RP-001.fex
        """
#         driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001.fex','S7068','mrid','mrpass')   
        utillobj.synchronize_with_visble_text("table .arGridBar table table > tbody", "records", active_misobj.chart_long_timesleep)   
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01: Verify Page summary')
        
        """
        Step 02: Select Unit Sales > Calculate > Avg
        """
        active_misobj.select_menu_items('ITableData0', 4, 'Calculate','Avg')        
        """Verify Total Avg is applied for Unit Sales column and same is displayed under the column heading Verify the value: Total Avg 34,476"""
        active_misobj.verify_calculated_value(2, 5, "Total Avg 34476",True, "Step 02: Verify Total Avg 34,476 displayed on pagination bar")           
        
        """
        Step 03: Select Unit Sales > Filter > Less than
        Verify Filter selection pop up is opened.
        """
        active_misobj.select_menu_items('ITableData0', 4, 'Filter','Less than')
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"#wall1 .arFilterButton")))     
        active_filter.verify_filter_selection_dialog(True,'Step 03: Verify Filter selection pop up is opened.',['Unit Sales','Less than'])
        
        """
        Step 04: Click Value dropdown menu and select "22991" Click Filter option
        """
        active_filter.create_filter(1, 'Less than','large',value1='22991')
        active_filter.filter_button_click('Filter')
        
        """Verify that Unit Sales column heading shows : Filtered Avg 16,767(48.63%) Total Avg 34,476 """
        """ Move Filter Selection box"""
        active_misobj.move_active_popup("1", "600", "200")
        active_misobj.verify_calculated_value(2, 5, "Filtered Avg 16767(48.63%)\nTotal Avg 34476",True, "Step 04: Verify Filtered Avg 16,767(48.63%) Total Avg 34,476 displayed on pagination bar in Unit Sales")           
        """Pagination shows:summation, SUB/TOT See attached screenshot."""
        active_misobj.verify_summation("Step 04: Verify summation")
        WebDriverWait(self.driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"table .arGridBar table table > tbody")))        
        active_misobj.verify_page_summary('0','SUB/TOT40of107records,Page1of1', 'Step 04: Verify Page summary has SUB/TOT')
        utillobj.verify_data_set('ITableData0','I0r','C2050487_Ds01.xlsx', 'Step 04: Verify filtered data set' )
        
  
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
