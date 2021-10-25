'''
Created on 29-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227643
TestCase Name = Numeric Filter with master-based Compute field
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run,define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227643_TestClass(BaseTestCase):

    def test_C2227643(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227643'
        
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
        Step 02: Double click "Product Subcategory" and
        "Revenue Per Sq. Ft." (master-based compute field located under Measures)
        """
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue Per,Sq. Ft.', 2, 1)
        time.sleep(8)
                
        """
        Step 03: Drag and drop "Revenue Per Sq. Ft." into the Filter pane
        """
        metaobj.datatree_field_click('Revenue Per,Sq. Ft.', 1, 1, 'Filter')
        time.sleep(5)
               
        """
        Step 04: Verify Filter dialog
        Step 05: Click OK
        """
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),0,"Step07: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(float(d['float_value']),4.68,"Step07: Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
                 
        """
        Step 06: Verify Canvas
        """
        time.sleep(8)
        metaobj.verify_filter_pane_field('Revenue Per,Sq. Ft.',1,"Step06: Verify 'Revenue Per,Sq. Ft.' appears in filter pane")
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#ar_Prompt_1 span[id$='s_min']")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',0, 'int',msg="Step06: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4.68, 'float',msg="Step06: Verify filter prompt range values-max")
        time.sleep(2)
                 
        parent_css="#MAINTABLE_wbody1 [class*='riser!s0!g']"
        resultobj.wait_for_property(parent_css, 21)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step06a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step06b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step06.c(i) Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Per Sq. Ft."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step06:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step06:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Product Subcategory:Blu Ray', 'Revenue Per Sq. Ft.:$44,732.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step06e: verify the default tooltip values")      
                                  
        """
        Step07: Click Save in the toolbar
        Step08: Save as "C2158163" > Click Save
        Step09: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)          
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
           
        """
        Step10: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        Step11: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Revenue Per,Sq. Ft.',1,"Step11: Verify 'Revenue Per,Sq. Ft.' appears in filter pane")
        elem1=(By.CSS_SELECTOR, "#ar_Prompt_1 span[id$='s_min']")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',0, 'int',msg="Step11: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4.68, 'float',msg="Step11: Verify filter prompt range values-max")
         
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 [class*='riser!s0!g']"
        resultobj.wait_for_property(parent_css, 21)
               
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step11a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step11b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step11.c(i) Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Per Sq. Ft."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step11:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Product Subcategory:Blu Ray', 'Revenue Per Sq. Ft.:$44,732.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step11e: verify the default tooltip values")      
                  
        """
        Step12: Click Run
        """
        time.sleep(15)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)    
             
        """
        Step13: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)  
        browser=utillobj.parseinitfile('browser')      
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        elem1=(By.CSS_SELECTOR, "div[id*='ibi$container$inner']")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227643_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5) 
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',0,'int',msg="Step13: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',4.68,'float',msg="Step13: Verify filter prompt range values-max")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 [class*='riser!s0!g']"
        resultobj.wait_for_property(parent_css, 21)
               
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step13a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step13b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c(i) Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Per Sq. Ft."
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step13:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step13:d(ii) Verify Y Axis Title") 
        time.sleep(2)
        expected_tooltip=['Product Subcategory:Blu Ray', 'Revenue Per Sq. Ft.:$44,732.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step13e: verify the default tooltip values")      
                    
        """
        Step14: Close output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)          
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
    