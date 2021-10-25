'''
Created on Aug 26, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7076&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2055544

'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_chart_rollup, visualization_resultarea
from common.lib import utillity
from common.locators.active_miscelaneous_locators import ActiveMiscelaneousLocators
from common.pages.visualization_resultarea import Visualization_Resultarea


class C2055544_TestClass(BaseTestCase):

    def test_C2055544(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2055544'
        """
        Step 01: Execute the attached repro - act406.fex.
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(25) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        utillobj.active_run_fex_api_login('act406.fex','S7076','mrid','mrpass') 
        time.sleep(10)     
        active_misobj.verify_page_summary('0','2488361of2488361records,Page1of43656', 'Step 01.1: Verify Page summary 2488361of2488361')
        column=['ID Sales','Revenue','Quantity Sold']
        active_misobj.verify_column_heading('ITableData0', column, "Step 01.2: Verify Column heading of act406.fex")
        utillobj.verify_data_set('ITableData0','I0r','act406.xlsx',"Step 01.3: Verify act406.fex dataset")        
        
        """
        Step 02: Click the down arrow by Revenue and create a Less Than or Equal To filter for 179.99 to reduce the records.
        """
        time.sleep(10)
        active_misobj.select_menu_items('ITableData0', 1, 'Filter','Less than or equal to')
        time.sleep(8)
        active_filter.create_filter(1, 'Less than or equal to','large','wall1',4,value1='$179.99')
        active_filter.filter_button_click('Filter')
        active_misobj.move_active_popup("1", "600", "200")
        time.sleep(5)
        active_filter.verify_filter_selection_dialog(True,'Step 02.1: Verify filter row.',['Revenue', 'Less than or equal to', '$179.99'])
        active_misobj.verify_page_summary('0','641778of2488361records,Page1of11260', 'Step 02.2: Verify Page summary 641778of2488361')
        
        """
        Step 03: Click the down arrow on Quantity_Sold and do ROLLUP on Revenue.
        """
        active_misobj.select_menu_items('ITableData0', 2, 'Rollup','Revenue')
        time.sleep(8)
        column=['Revenue','Quantity Sold']
        active_misobj.verify_column_heading('ITableData1', column, "Step 03.1: Verify Column heading after rollup")
        active_misobj.verify_page_summary('1','245of245records,Page1of5', 'Step 03.2: Verify Page summary 245of245')
        utillobj.verify_data_set('ITableData1','I1r','C2055544_Ds01.xlsx',"Step 03.3:Verify dataset for ROLLUP on Revenue")
        
        """
        Step 04: On the ROLLUP report, sort ascending on QUANTITY_SOLD.
        """
        time.sleep(8)
        active_misobj.select_menu_items('ITableData1', 1, 'Sort Ascending')
        time.sleep(8)
        utillobj.verify_data_set('ITableData1','I1r','C2055544_Ds02.xlsx',"Step 04.1:Verify sort ascending on QUANTITY_SOLD")
        
        """
        Step 05: Change the ROLLUP to a bar chart by clicking BAR chart icon.
        """
        time.sleep(8)
        rollobj.click_chart_menu_bar_items('wall2',1)
        """ Verify values are arranged in ascending order."""
        #screenshot
        time.sleep(5)
        element = self.driver.find_element_by_css_selector("#wall2")
        utillobj.take_screenshot(element, 'C2055544_Actual_Step05.png', image_type='actual')
        #menu
        rollobj.verify_arChartMenu('wall2',"Step 05.1: Verify chart menu")
        #Title
        r_title=driver.find_element_by_css_selector('#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle').text
        r_cond=r_title.strip()=='Quantity Sold BY Revenue'
        utillity.UtillityMethods.asequal(self,True, r_cond, 'Step 05.2: Verifying the rollup dialog title')
        
        #Tooltip
        time.sleep(5)
        if utillobj.parseinitfile('browser')=='Chrome':
            expected=['Quantity Sold: 1,574', 'X: 107.99']
            raiser="riser!s0!g106!mbar"
        else:
            raiser="riser!s0!g110!mbar"
            expected=['Quantity Sold: 15,577', 'X: 109.99']
        active_misobj.verify_active_chart_tooltip('wall2',raiser,expected,"Step 05.3: Verify the bar riser tooltip and color - 'ACT-406'")
        utillobj.verify_chart_color('wall2',"riser!s0!g110!mbar",'cerulean_blue',"Step 05.3: Verify Color - 'ACT-406'")
        time.sleep(5)
        #XY Labels        
        yval_list=['0', '10K', '20K', '30K', '40K', '50K']        
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' or 'Chrome' or 'Edge':
            xval_list=['104.29', '90.3', '167.98', '84.15']
        else:
            xval_list=['104.29','158.4','96.75']
        resobj.verify_riser_chart_XY_labels('wall2', xval_list, yval_list, "Step 05.4 Verify Chart XY labels- 'ACT-406'") 
        
        print("Issue still exists where values are not arranged in ascending order. - 'ACT-406'")

if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
