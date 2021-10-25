'''
Created on 24-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227639
TestCase Name = Alphanumeric Filter with Define field
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run,define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227639_TestClass(BaseTestCase):

    def test_C2227639(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227639'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        defcomobj = define_compute.Define_Compute(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
        
        """
        Step 02: Select Calculation > Detail (Define) in the Home Tab ribbon
        Step 03: Type "Category" for Field name, change Format to A90V
        Step 04: Copy and paste following syntax in the expression area:
        WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY || (', ' | WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_SUBCATEG)
        Step 05: Click OK
        """ 
        ribbonobj.select_ribbon_item('Home', 'Calculation')
        utillobj.select_or_verify_bipop_menu('Detail (Define)')
        defcomobj.enter_define_compute_parameter('Category', 'A90V', 'Product,Category', 1)
        time.sleep(2)
        field_elem=self.driver.find_element_by_css_selector("#ftext")
        time.sleep(2)
        utillobj.set_text_field_using_actionchains(field_elem, "WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY || (', ' | WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_SUBCATEG)",pyautogui_type=True)
        defcomobj.close_define_compute_dialog('ok')
        time.sleep(5)
         
        """
        Step 06: Verify Define field "Product" appears in the Data pane
        """
        metaobj.verify_data_pane_field('Dimensions',"Category",6,"Step 06: Verify define field Category appears in data pane")
        time.sleep(2)
         
        """
        Step 07: Double click "Category" to add field to Canvas
        """
        metaobj.datatree_field_click('Category', 2, 1)
        time.sleep(5)
         
        """
        Step 08: Double-click "Cost of Goods", located under Sales Measures
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(5)         
              
        """
        Step 09: Drag and drop "Category" from Data pane into the Filter pane
        """
        metaobj.datatree_field_click('Category', 1, 1,'Filter')
        time.sleep(5)
         
        """
        Step 10: Verify Filter dialog
        Step 11: Click OK
        """
        item_list=['[All]', 'Accessories, Charger', 'Accessories, Headphones', 'Accessories, Universal Remote Controls', 'Camcorder, Handheld', 'Camcorder, Professional', 'Camcorder, Standard', 'Computers, Smartphone', 'Computers, Tablet', 'Media Player, Blu Ray', 'Media Player, DVD Players', 'Media Player, DVD Players - Portable', 'Media Player, Streaming', 'Stereo Systems, Boom Box', 'Stereo Systems, Home Theater Systems', 'Stereo Systems, Receivers', 'Stereo Systems, Speaker Kits', 'Stereo Systems, iPod Docking Station', 'Televisions, CRT TV', 'Televisions, Flat Panel TV', 'Televisions, Portable TV', 'Video Production, Video Editing']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true')
        time.sleep(2)
        metaobj.create_visualization_filters('alpha')
        time.sleep(2)
         
        """
        Step 12: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Category',1,"Step12: Verify 'Category' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step12: Verify All is checked in filter prompt")
         
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 12a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories, Charger', 'Accessories, Headphones', 'Accessories, Universal','Camcorder, Handheld', 'Camcorder, Professional', 'Camcorder, Standard']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 12.c(i) Verify first bar color")
        xaxis_value="Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 12:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Category:Accessories, Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 12e: verify the default tooltip values")      
                  
        """
        Step13: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
           
        """
        Step14: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)      
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step14: Verify All is checked in filter prompt")
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 14a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories, Charger', 'Accessories, Headphones', 'Accessories, Universal','Camcorder, Handheld', 'Camcorder, Professional', 'Camcorder, Standard']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.c(i) Verify first bar color")
        xaxis_value="Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 14:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Category:Accessories, Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 14e: verify the default tooltip values")      
           
        """
        Step15: Close output window
        Step16: Click Save in the toolbar
        Step17: Save as "C2158163" > Click Save
        Step18: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
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
        Step 19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Category',1,"Step19: Verify 'Category' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step19: Verify All is checked in filter prompt")
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 19a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories, Charger', 'Accessories, Headphones', 'Accessories, Universal','Camcorder, Handheld', 'Camcorder, Professional', 'Camcorder, Standard']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 19b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 19.c(i) Verify first bar color")
        xaxis_value="Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 19:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 19:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Category:Accessories, Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 19e: verify the default tooltip values")      
           
        """
        Step 20: Verify Canvas
        Step 21: Select values in the Filter Prompt > "Computers, Tablet" and "Media Player, Blu Ray"
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
           
        time.sleep(5)
        metaobj.verify_filter_pane_field('Category',1,"Step21: Verify 'Product' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers, Tablet', msg="Step21: Verify Accessories is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player, Blu Ray', msg="Step21: Verify Camcorder is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers, Tablet', verify=True, verify_type=True, msg="Step21: Verify 'Computers, Tablet' is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player, Blu Ray', verify=True, verify_type=True, msg="Step21: Verify 'Media Player, Blu Ray' is checked in filter prompt")
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 21a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Computers, Tablet', 'Media Player, Blu Ray']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 21b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 21:c(i) Verify first bar color")
        xaxis_value="Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 21:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Category:Media Player, Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 21e: verify the default tooltip values")                       
        time.sleep(5)
         
        """
        Step22: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
           
        """
        Step23: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(10)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227639_Actual_step23', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)        
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers, Tablet', verify=True, verify_type=True, msg="Step23: Verify 'Computers, Tablet' is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Media Player, Blu Ray', verify=True, verify_type=True, msg="Step23: Verify 'Media Player, Blu Ray' is checked in filter prompt")
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 23a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Computers, Tablet', 'Media Player, Blu Ray']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 23b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar", "bar_blue", "Step 23:c(i) Verify first bar color")
        xaxis_value="Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 23:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 23:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Category:Media Player, Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 23e: verify the default tooltip values")                       
        time.sleep(5)
           
        """
        Step24: Close output window
        Step25: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
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
    