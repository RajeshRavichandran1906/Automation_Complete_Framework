'''
Created on 22-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227636
TestCase Name = Alphanumeric Filter with Attributes field - Sale,Holiday
'''
import unittest,time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties, metadata

class C2227636_TestClass(BaseTestCase):

    def test_C2227636(self):
        
        """
        CLASS OBJECTS
        """
        driver = self.driver #Driver reference object created
        visual = Visualization(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227636'
        qwery_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        utillobj.wait_for_page_loads(ribbonobj.home_page_long_timesleep)
        
        """
        Step 02: Double-click "Quantity,Sold", located under Sales Measures
        Step 03: Expand "Sales_Related" > "Transaction Date,Simple" > "Sale,Day" > "Attributes" > Double-click "Sale,Holiday"
        """
        metaobj.datatree_field_click('Quantity,Sold', 2, 1)
        visual.wait_for_visible_text(qwery_tree_css, 'Quantity,Sold')
        metadataobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(5)
        metaobj.datatree_field_click('Sale,Holiday', 2, 1)
        visual.wait_for_visible_text(qwery_tree_css, 'Sale,Holiday')       
        
        """
        Step 04: Drag and drop "Sale,Holiday" to the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Holiday', 1)
        time.sleep(5)
        
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        item_list=['[All]', 'N', 'Y']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True)
        
        """
        Step 07: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Holiday',1,"Step 07.01: Verify 'Sale,Holiday' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true", msg="Step07: Verify [All] is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['N','Y']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        xaxis_value="Sale Holiday"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07:d(ii) Verify Y-Axis Title")     
                
        """
        Step08: Click Run
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1) 
        
        """
        Step09: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227636_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 09a: Verify the total number of risers displayed on Run Chart')
        x_val_list=['N','Y']
        y_val_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 09b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 09c(i): Verify first bar color")
        xaxis_value="Sale Holiday"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09d(ii) Verify Y-Axis Title")       
        
        time.sleep(3)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true", msg="Step09: Verify [All] is checked in filter prompt")        
        time.sleep(5)
        
        """
        Step10: Close output window
        Step11: Click Save in the toolbar
        Step12: Save as "C2227636" > Click Save
        Step13: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(3)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
        
        time.sleep(2)  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 14: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227636.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        
        """
        Step15: Verify Canvas
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        utillobj.wait_for_page_loads(resultobj.home_page_long_timesleep)
        
        metaobj.verify_filter_pane_field('Sale,Holiday',1,"Step15: Verify 'Sale,Holiday' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type="true", msg="Step 15.01: Verify [All] is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 15.02: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['N','Y']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 15.03: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 15.04: Verify first bar color")
        xaxis_value="Sale Holiday"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 15.05: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 15.06: Verify Y-Axis Title")          
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()