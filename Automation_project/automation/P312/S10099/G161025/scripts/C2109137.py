'''
Created on June17, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109137
TestCase Name : IA-4166:Lasso on bubble chart hangs in design mode
'''
import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2109137_TestClass(BaseTestCase):

    def test_C2109137(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2109137'
        """
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/MUTUAL_FUNDS&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/MUTUAL_FUNDS','P312/S10099_5', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        """
        Step 02: Change the chart type to bubble
        """
        time.sleep(5)
        
        ribbonobj.change_chart_type('bubble_chart')
        time.sleep(5)
        
        """
        Step 03: Add Volatility to Vertical
        """
        parent_css="#TableChart_1 svg circle[class='riser!s0!g0!mmarker!']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Measures->Volatility (%)",1, 1,"Add To Query","Vertical Axis")
        time.sleep(5)
        
        """
        Step 04: Add 3-year Performance to Horizontal axis
        """
        
        parent_css="#TableChart_1 svg text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Measures->3-Year Performance (%)", 1, 1,'Add To Query', 'Horizontal Axis')
        time.sleep(5)
        
        """
        Step 05: Add Net Assets to Size
        """
        
        parent_css="#MAINTABLE_wbody1 svg g text[class='xaxisNumeric-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Measures->Net Assets ($M)", 1, 1,"Add To Query", "Size")
        time.sleep(5)
        
        """
        Step 06: Add Fund Name to Detail
        """
        
        parent_css="#TableChart_1 svg text[class='sizeLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Dimensions->Mutual Funds->Funds->Fund Name", 1, 1,"Add To Query", "Detail")
        time.sleep(5)
        
        """
        Step 07: Add Fund Category to Color By
        """
        
        parent_css="#TableChart_1 svg text[class^='xaxisNumeric-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.datatree_field_click("Dimensions->Mutual Funds->Funds->Fund Category", 1, 1,"Add To Query", "Color")
        time.sleep(25)
        
        """
        Step 08: verify label values
        """
        parent_css="#TableChart_1 svg text[class^='legend-title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 900, 960, 'Step 8: Verify the total number of Circle displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g7!mmarker!", "bar_blue", "Step 8.1: Verify first circle color")
        xaxis_value="3-Year Performance (%)"
        yaxis_value="Volatility (%)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 8.2(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 8.2(ii) Verify Y-Axis Title")
        expected_xval_list=['-5', '0', '5', '10', '15', '20', '25', '30']
        expected_yval_list=['0', '1', '2', '3', '4', '5', '6']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 8.3: X annd Y axis Scales Values has changed or NOT')
       
        
        """
        Step 09: verify query pane
        """
        
        metaobj.verify_query_pane_field("Vertical Axis", "Volatility (%)",1, "Step 09: Verify query pane")
        
        """
        Step 10: Lasso 350+ points and select filter chart
        """        
        
        resultobj.create_lasso("MAINTABLE_wbody1", "circle", "riser!s4!g0!mmarker", target_tag="circle", target_riser="riser!s5!g64!mmarker")
        time.sleep(3)
        miscelanousobj.select_active_lasso_menu('Filter Chart')
    
        time.sleep(20)
        
        """
        Step 11: Verify query added to filter pane
        """
        parent_css="#TableChart_1 svg text[class^='xaxisNumeric-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_filter_pane_field('FUND_CATEGORY and FUND_NAME',1, 'Step 11: Verify FUND_CATEGORY and FUND_NAME query added to filter pane')
        time.sleep(3)
        
        
        """
        Step 12: verify tooltip of a bubble point (Fund category - Balanced)
        """
        bubble = "Fund Category:Balanced"
        resultobj.verify_default_circle_tooltip_values("MAINTABLE_wbody1", "riser!s0!g44!mmarker", bubble, "Step 12: verify  bubble values", x_offset=-5, y_offset=-20)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 350, 450, 'Step 12.1: Verify the total number of Circle displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g44!mmarker!", "bar_blue", "Step 12.2: Verify first bar color")
        xaxis_value="3-Year Performance (%)"
        yaxis_value="Volatility (%)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12.3(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12.3(ii) Verify Y-Axis Title")
        expected_xval_list=['0', '4', '8', '12', '16', '20']
        expected_yval_list=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12.4: X annd Y axis Scales Values has changed or NOT')
        
         
        
        """
        Step 13: Click Run in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)             # switch to run window
        
        """
        Step 14: Verify tooltip of a bubble point (Fund Category - Mortgage)
        """
        elem1=(By.CSS_SELECTOR, '[class*="riser!s"]')
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg text[class^='xaxisNumeric-labels']"
        resultobj.wait_for_property(parent_css, 6)
        
        bubble_runtime = "Fund Category:Mortgage"
        resultobj.verify_default_circle_tooltip_values("MAINTABLE_wbody1", "riser!s4!g27!mmarker", bubble_runtime, "Step 14: Verify tooltip of a bubble point", x_offset=-2, y_offset=-25)
        resultobj.verify_number_of_circle("MAINTABLE_wbody1", 350, 450, 'Step 14.1: Verify the total number of Circle displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g44!mmarker!", "bar_blue", "Step 14.2: Verify first bar color")
        xaxis_value="3-Year Performance (%)"
        yaxis_value="Volatility (%)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14.3(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 14.3(ii) Verify Y-Axis Title")
        expected_xval_list=['0', '4', '8', '12', '16', '20']
        expected_yval_list=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14.4: X annd Y axis Scales Values has changed or NOT')
        time.sleep(10)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#MAINTABLE_wbody1"),'C2109137_Actual_step14', image_type='actual')
        
        
        """
        Step 15: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)        # switch back to main window
        time.sleep(15)
        
        """
        Step 16: Click "Save" in the toolbar > Type C2109137 > Click "Save" in the Save As dialog
        """
        
        time.sleep(6)
        ribbonobj.select_top_toolbar_item("toolbar_save")
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        