'''
Created on 22-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227635
TestCase Name = Alphanumeric Filter format A40V
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227635_TestClass(BaseTestCase):

    def test_C2227635(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227635'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")  
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 03e: verify the default tooltip values")       
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        """
        metaobj.datatree_field_click('Product,Category',1,1,'Filter')
        time.sleep(5)
        
        """
        Step 05 :Verify Filter dialog
        Step 06: Click OK
        """
        item_list=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True)
        
        """
        Step 07: Verify Filter appears in the Filter pane
        """
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07: Verify 'Product Category' appears in filter pane")
        
        """
        Step08: Verify Filter Prompt is displayed on preview canvas
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step08: Verify [All] is checked in filter prompt")
        
        """
        Step09: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)    
        
        """
        Step10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227635_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10a: Verify the total number of risers displayed on Run Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 10b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 10c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10d(ii) Verify Y-Axis Title")
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 10e: verify the default tooltip values")        
        
        time.sleep(3)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step10: Verify [All] is checked in filter prompt")        
        time.sleep(5)
        
        """
        Step11: Close output window
        Step12: Click Save in the toolbar
        Step13: Save as "C2158163" > Click Save
        Step14: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
        
        time.sleep(2)  
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """
        Step 15: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        
        """
        Step16: Verify Canvas
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 16a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 16.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16:d(ii) Verify Y-Axis Title")  
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 16e: verify the default tooltip values")
        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True,msg="Step16: Verify [All] is checked in filter prompt")        
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()
    