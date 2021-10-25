'''
Created on Sept'08

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197659
TestCase Name =Noticed color of chart tool bar doesn't extend to the width of the chart window.
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,  active_chart_rollup,active_tools, visualization_resultarea
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2197659_TestClass(BaseTestCase):

    def test_C2197659(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2197659'
        """
            Step 01: Run the attached 139757.fex from text editor
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_toolsobj = active_tools.Active_Tools(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('139757.fex','S7074','mrid','mrpass')      
        time.sleep(8)      
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbodyMain0', expected_xval_list, expected_yval_list, 'Step 01: Verify x and y labels')
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('MAINTABLE_wbodyMain0',"riser!s0!g0!mbar", ['SALES, ENGLAND: 12,000'],"Step 04.3: Verify Chart piebevel tooltip for Unit Sales")
        
        utillobj.verify_chart_color('MAINTABLE_wbodyMain0', 'riser!s0!g0!mbar','cerulean_blue_1',"Step 04.4: Verify Chart piebevel Color ")
        
        
        """Step 02:Verify that the color of chart tool bar extended to the width of the chart window"""
        menu_color = driver.find_element_by_css_selector(".arChartMenuBar  td.arChartMenuBarContainer").value_of_css_property('background-color')
        extended_menucolor = driver.find_element_by_css_selector(".arChartMenuBar  td[width='*']").value_of_css_property('background-color')
        validate = menu_color==extended_menucolor
        utillobj.asequal(True, validate, 'Step 02:Verify that the color of chart tool bar extended to the width of the chart window')
        
        
 
       
 
        

if __name__ == '__main__':
    unittest.main()


