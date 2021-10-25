'''
Created on Sept 26, 2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7068&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2203697
TestCase Name = AHTML: Verify original chart and filtering 
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,  active_chart_rollup, visualization_resultarea
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators

class C2203697_TestClass(BaseTestCase):

    def test_C2203697(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2203697'
        """
            Step 01:Execute the attached fex.
        """
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollupobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('148116.fex','S7068','mrid','mrpass')      
        time.sleep(8)      
        active_misobj.verify_page_summary('0','5of5records,Page1of1', 'Step 01: Verify Page summary')
        
        """Step 02:Click on Dealer_Cost dropdown and select Chart-->Pie-->Country """
        
        utillobj.verify_data_set('ITableData0','I0r','148116.xlsx',"Step 01: 148116 fex data verification")
        
        #utillobj.create_data_set('ITableData0','I0r','148116.xlsx')
        
        active_misobj.select_menu_items('ITableData0', 1, 'Chart','Pie','COUNTRY')
        time.sleep(5)
        
        #screenshot
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2203697_Actual_Step02', image_type='actual')
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['ENGLAND', 'DEALER_COST: 37,853', '26.3% of 144K'], "Step 02.1: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue_1',"Step 02.2: Verify Chart piebevel Color ")
        
        active_misobj.verify_popup_title('wall1', 'DEALER_COST BY COUNTRY', 'Step 02.3: Verify that State By Product pop up window for the chart is displayed')
        
  
        """Step 03: Click on 'Line' chart and Click on "original chart" button from chart window toolbar and close it."""
        #Line chart changinn
        rollupobj.click_chart_menu_bar_items('wall1',3 )
        time.sleep(5)
        
        #screenshot
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2203697_Actual_Step03', image_type='actual')
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"marker!s0!g0!mmarker", ['DEALER_COST: 37,853', 'X: ENGLAND'], "Step 02.1: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'marker!s0!g0!mmarker','white',"Step 03.2: Verify Chart piebevel Color ")
        
        active_misobj.verify_popup_title('wall1', 'DEALER_COST BY COUNTRY', 'Step 03.3: Verify that State By Product pop up window for the chart is displayed')
        x_val = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_val= ['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels('wall1', x_val, y_val, 'Step 03.3: Line Chart x and y label verification')
        
        #Click original chart 
        rollupobj.click_chart_menu_bar_items('wall1',7)
        time.sleep(5)
        
        #Tooltip & Color
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['ENGLAND', 'DEALER_COST: 37,853', '26.3% of 144K'], "Step 03.4: Verify Chart piebevel tooltip for Unit Sales")
        time.sleep(5)
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue_1',"Step 03.5: Verify Chart piebevel Color ")
        
        active_misobj.verify_popup_title('wall1', 'DEALER_COST BY COUNTRY', 'Step 03.6: Verify that State By Product pop up window for the chart is displayed')
         
        active_filter.close_filter_dialog('wall1')
        """Step 04: Now click on COUNTRY dropdown select Filter-->Equals-->ENGLAND and then click filter. """
        active_misobj.select_menu_items("ITableData0", "0", "Filter","Equals")
        time.sleep(3)
        active_filter.create_filter(1, 'Equals',value1='ENGLAND')
        time.sleep(4)
        active_filter.filter_button_click('Filter')
        time.sleep(4)
        
        """Step 05: Verify values are displayed as expected."""
        
        utillobj.verify_data_set('ITableData0','I0r','C2203697_Ds01.xlsx',"Step 01: 148116 fex data verification")
        active_misobj.verify_page_summary('0','1of5records,Page1of1', 'Step 01: Verify Page summary')
        #utillobj.create_data_set('ITableData0','I0r','C2203697_Ds01.xlsx')
        
        
        

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
