'''
Created on 26-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2228180
TestCase Name = Verify InfoMini with Format and Series Tabs (82xx)
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from selenium.common.exceptions import NoSuchElementException

class C2228180_TestClass(BaseTestCase):

    def test_C2228180(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2228180"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """ Step 1: Launch WF, New > Chart with GGSALES.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/GGSALES','P292/S10032_chart_1', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1 text", 16, expire_time=25)    
         
        """ Step 2: Select "HTML" from format group under Home tab.
        """
        ia_ribbonobj.select_or_verify_output_type(launch_point='Home',item_select_path='HTML')
        time.sleep(2)
         
        """ Step 3: Click on "Format" tab.
        """
        """ Step 4: Expand Destination group (if not already expanded).
        """
        """ Step 5: Click the dropdown arrow next to "InfoMini".
        """
        """ Step 6: Uncheck "Slicers Tab".
        """
        ia_ribbonobj.select_infomini_option(['Slicers Tab'])
         
        """ Step 7: Verify the "InfoMini" button is highlighted.
        """
        staus = False
        try:
            staus = bool(driver.find_element_by_css_selector("#FormatApplicationRibbonEnable[class*='checked']").is_displayed())
        except NoSuchElementException:
            staus = False
        utillobj.asequal(True, staus, "Step 7: Verify the 'InfoMini' button is highlighted.")
        del staus
        """ Step 8: Click the dropdown arrow next to "InfoMini".
        """
        """ Step 9: Select "Series Tab".
        """
        ia_ribbonobj.select_infomini_option(['Series Tab'])
         
        """ Step 10: Verify the following icons are displayed on the ribbon.
        """
        vis_ribbonobj.switch_ia_tab('Series')
        time.sleep(2)
        ribbon_text = driver.find_element_by_css_selector("#SeriesTab").text.strip().split('\n')
        actual_text = [elem for elem in [elem.strip() for elem in ribbon_text if elem!=''] if elem != '']
        expected_text = ['Select', 'All Series', 'Style', 'Style', 'Properties', 'Data Labels', 'Type', 'Trendline', 'Equation', 'Line', 'Smooth Line', 'Connect Lines', 'Marker']
        utillobj.asequal(actual_text, expected_text, "Step 10: Verify the following icons are displayed on the ribbon.")
        staus = False
        try:
            staus = bool(driver.find_element_by_css_selector("#SeriesLineCluster #SeriesConnectLines[class*='checked']").is_displayed())
        except NoSuchElementException:
            staus = False
        utillobj.asequal(True, staus, "Step 10.1: Verify the 'ConnectLines' button is highlighted.")
        del staus
        
        """ Step 11: Double Click on "Product", "Unit Sales", "Dollar Sales".
        """
        metaobj.datatree_field_click("Product", 2, 1)
        parent_css = "#queryTreeColumn table tr:nth-child(4)"
        resultobj.wait_for_property(parent_css, 0, expire_time=15, string_value='Product', with_regular_exprestion=True)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        parent_css = "#queryTreeColumn table tr:nth-child(3)"
        resultobj.wait_for_property(parent_css, 0, expire_time=15, string_value='UnitSales', with_regular_exprestion=True)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        parent_css = "#queryTreeColumn table tr:nth-child(4)"
        resultobj.wait_for_property(parent_css, 0, expire_time=15, string_value='DollarSales', with_regular_exprestion=True)
         
        """ Step 12: Select "Home" > "Records:" (dropdown) > "All".
        """
        vis_ribbonobj.select_ribbon_item('Home', 'Records', opt='All', custom_css="div[id*='BiComboBoxItem']")
         
        """ Step 13: Verify the following chart is displayed.
        """
        time.sleep(1)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+".png", "Step 13: Verify the following chart is displayed.")
        
        """ Step 14: Click "Run".
        """
        vis_ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """ Step 15: Verify the following chart is displayed.
        """
        utillobj.switch_to_window(1)
        time.sleep(2)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+".png", "Step 15: Verify the following chart is displayed.")
        
        """ Step 16: Dismiss the "Run" window.
        """
        driver.close()
        utillobj.switch_to_window(0)
        
        """ Step 17: Click "IA" > "Save" > "C2056388" > "Save".
        """
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """ Step 18: Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        
        """ Step 19: Highlight "C2056388" > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'Chart', 'S10032_chart_1', mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 [id*='LayoutChartObjectDrawLayer']", 1)
        time.sleep(2)
        
        """ Step 20: Verify the following chart is displayed.
        """
        time.sleep(2)
        utillobj.verify_picture_using_sikuli(Test_Case_ID+".png", "Step 15: Verify the following chart is displayed.")
        time.sleep(3)
        elem=driver.find_element_by_css_selector("#TableChart_1 [id*='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(elem, Test_Case_ID+"_Actual_Step_20")
        
        """ Step 21: Dismiss the tool window.
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()