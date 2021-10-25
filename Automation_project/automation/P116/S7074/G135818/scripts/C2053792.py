'''
Created on Sep 6, 2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2053792

'''
import unittest
import time
from selenium import webdriver
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, active_filter_selection,\
    active_pivot_comment, active_chart_rollup, visualization_resultarea,\
    active_tools
from common.lib import utillity


class C2053792_TestClass(BaseTestCase):

    def test_C2053792(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2053792'
        """
        Step 01: Execute the AR-RP-001.fex
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_filter = active_filter_selection.Active_Filter_Selection(self.driver)
        rollobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        resobj= visualization_resultarea.Visualization_Resultarea(self.driver)
        toolobj= active_tools.Active_Tools(self.driver)
        pivobj = active_pivot_comment.Active_Pivot_Comment(self.driver)
        utillobj.active_run_fex_api_login('AR-RP-001A.fex','S7074','mrid','mrpass') 
        active_misobj.verify_page_summary('0','107of107records,Page1of2', 'Step 01.1: Verify Page summary 107of107')
        
        """
        Step 02: Select State > Chart > Pie > Category
        Verify that 'State By Category' pop up window for the Bar chart is displayed. 
        Verify that chart toolbar is present with all the options.
        """
        time.sleep(8)
        active_misobj.select_menu_items('ITableData0', 3, 'Chart','Pie','Category')        
        
        """
        Step 03: Click Scatter chart icon
        Verify Scatter chart is displayed.
        """
        rollobj.click_chart_menu_bar_items('wall1', 4)
        time.sleep(4)
        scatter=self.driver.find_element_by_css_selector('#wbody1_f circle[class*="riser!s0!g2!mmarker"]')
        if scatter.is_displayed()==True:
            utillobj.asequal(True,True,"Step 03: Scatter Chart is displayed")
        else: 
            utillobj.asequal(False,True,"Step 03: Scatter Chart is not displayed")
        
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053792_Actual_Step02', image_type='actual')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g2!mmarker", ['State','X: Gifts','Y: 44'],"Step 02.1a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g2!mmarker','white',"Step 02.1b: Verify Chart piebevel Color ", attribute=True)
        time.sleep(5)
        #XY Labels
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval_list=['0', '10','20','30','40','50']
        resobj.verify_riser_chart_XY_labels('wall1', expected_xval_list, expected_yval_list, 'Step 02.1b: Verify XY Labels')
        #Title
        active_misobj.verify_popup_title('wall1', 'State BY Category', 'Step 02.1c: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 02.1d: Verify the chart Menu")        
        
        """
        Step 04:Click Original Chart icon from the toolbar
        Verify that Origianl chart icon shows original chart on a chart window.
        """
        rollobj.click_chart_menu_bar_items('wall1', 7)
         
        chart=self.driver.find_element_by_css_selector('#wbody1_f [class*="riser!s0!g0!mwedge"]')
        if chart.is_displayed()==True:
            utillobj.asequal(True,True,"Step 03: Chart is displayed")
        else: 
            utillobj.asequal(False,True,"Step 03: Chart is not displayed")
        #screenshot
        time.sleep(8)
        element = self.driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, 'C2053792_Actual_Step04', image_type='actual_images')
        #Tooltip & Color
        time.sleep(5)
        active_misobj.verify_active_chart_tooltip('wall1',"riser!s0!g0!mwedge", ['Coffee','State: 30','28.0% of 107'],"Step 03.1a: Verify Chart tooltip and color")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge','cerulean_blue',"Step 03.1b: Verify Chart piebevel Color ")
        time.sleep(5)
        #Pie Label
        resobj.verify_riser_pie_labels_and_legends('wall1', ['State'],"Step 03.1b: Verify Chart Label")
        #Pie Legend
        resobj.verify_riser_legends('wall1', ['Coffee','Food','Gifts'], "Step 03.1c: Verify Chart Legends")
        #Title
        active_misobj.verify_popup_title('wall1', 'State BY Category', 'Step 03.1d: Verify the dialog title')
        #Menu
        rollobj.verify_arChartMenu('wall1',"Step 03.1e: Verify the chart Menu")
        
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
