'''
Created on May'31, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2108835&group_by=cases:section_id&group_id=146864&group_order=asc
TestCase Name : IA-4430:Vis: Lasso filter on Vis with 2 or more By (dimension) in Query Panel, throws error message
'''
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, metadata
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.wftools import visualization

class C2108835_TestClass(BaseTestCase):

    def test_C2108835(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108835'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visual = visualization.Visualization(self.driver)
        browser = utillobj.parseinitfile('browser')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "Revenue" and "Product,SubCategory"
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Dimensions->Product->Product->Product,Subcategory", 2, 1)
        time.sleep(5)
        """
        Step 03: Verify x and y axis labels.
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory",'Step 03: Verify X title Product Subcategory')
        resultobj.verify_yaxis_title('MAINTABLE_wbody1', "Revenue",'Step 03: Verify Y title Revenue')
        """
        Step 04: Verify first and last 3 bar riser values..
        """
        WebDriverWait(self.driver, 70).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class,"riser!s0!g0!mbar")]')))
        a=['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 04: Verify Preview 1st bar value")
        
        """
        Step 05: Add "Product,Category" to Horizontal axis.
        """
        time.sleep(8)
        metaobj.datatree_field_click('Dimensions->Product->Product->Product,Category',1,1,'Add To Query','Horizontal Axis')
        
        """
        Step 06: Verify x-axis label value
        """
        resultobj.verify_xaxis_title('MAINTABLE_wbody1', "Product Subcategory : Product Category",'Step 06.a: Verify X title')
        xaxis = self.driver.find_element_by_css_selector("g > text[class='xaxisOrdinal-title']")
        utillity.UtillityMethods.asequal(self, 'Product Subcategory : Product Category',xaxis.text, "Step 06.b: Verify x-axis label value has Product Subcategory : Product Category")
        time.sleep(8)
        expected_xval_list=['Blu Ray : Media Player', 'Boom Box : Stereo Systems', 'CRT TV : Televisions', 'Charger : Accessories', 'DVD Players : Media Player', 'DVD Players - Portable : Media Player', 'Flat Panel TV : Televisions', 'Handheld : Camcorder', 'Headphones : Accessories', 'Home Theater Systems : Stereo Systems', 'Portable TV : Televisions', 'Professional : Camcorder', 'Receivers : Stereo Systems', 'Smartphone : Computers', 'Speaker Kits : Stereo Systems', 'Standard : Camcorder', 'Streaming : Media Player', 'Tablet : Computers', 'Universal Remote Controls : Accessories', 'Video Editing : Video Production', 'iPod Docking Station : Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 06.c: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 06.d: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 06.e(i) Verify first bar color")
        xaxis_value="Product Subcategory : Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 06.f: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 06.g: Verify Y-Axis Title")
        expected_tooltip=['Product Subcategory:Blu Ray', 'Product Category:Media Player', 'Revenue:$232,884,116.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 06.h: verify the default tooltip values")
        time.sleep(8)
         
        """
        Step 07: Lasso 4 points and Click Filter Chart
        """
        visual.create_lasso_using_action_chain("rect[class='riser!s0!g6!mbar!']", "rect[class='riser!s0!g9!mbar!']")
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        utillobj.wait_for_page_loads(10)
#         WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class,"riser!s0!g0!mbar")]')))
#         action = ActionChains(driver)
#         move1 = driver.find_element_by_css_selector("#orgdiv0")
#         if browser=='Firefox':
#             utillobj.click_type_using_pyautogui(move1, move=True)
#         else:
#             action.move_to_element_with_offset(move1,1,1).perform()
#         time.sleep(8)
#         action = ActionChains(driver)
#         raiser="#MAINTABLE_wbody1 [class*='riser!s0!g6!mbar']"
#         move_riser = driver.find_element_by_css_selector(raiser)
#         if browser=='Firefox':
#             utillobj.click_type_using_pyautogui(move_riser)
#         else:
#             action.move_to_element(move_riser).perform()
#         resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g6!mbar!', target_tag='rect', target_riser='riser!s0!g9!mbar')
#         time.sleep(3)
    
         
         
        """
        Step 08: Verify uneditable query is added to filter pane.
        """   
        time.sleep(5)
        parent_css="#qbFilterWindow #qbFilterBox img"
        resultobj.wait_for_property(parent_css, 1) 
        metaobj.verify_filter_pane_field("PRODUCT_SUBCATEG and PRODUCT_CATEGORY", 1, "Step 08.1: verify query added to filter pane")
        time.sleep(5)
        metaobj.filter_tree_field_click('PRODUCT_SUBCATEG and PRODUCT_CATEGORY', 1, 1)
        time.sleep(5)
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Delete'],msg='Step 8.2: Verify Edit not in bi-popup menu')
  
        """
        Step 09: Verify filtered bar riser values
        """
        WebDriverWait(self.driver, 70).until(EC.visibility_of_element_located((By.XPATH,'//*[contains(@class,"riser!s0!g0!mbar")]')))
        a=['Product Subcategory:Flat Panel TV', 'Product Category:Televisions', 'Revenue:$74,962,843.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 09: Verify filtered 1st bar value")
        time.sleep(8)
        expected_xval_list=['Flat Panel TV : Televisions', 'Handheld : Camcorder', 'Headphones : Accessories', 'Home Theater Systems : Stereo Systems']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 9: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 7: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 9: Verify first bar color")
        xaxis_value="Product Subcategory : Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09: Verify Y-Axis Title")
        time.sleep(8)
         
        """
        Step 10: Click "Run" in the toolbar.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(15)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        """
        Step 11: Verify output
        """
        WebDriverWait(self.driver, 70).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,"[id*='MAINTABLE_wbody1'] [class*='riser!s0!g0!mbar']")))
        time.sleep(8)
        expected_xval_list=['Flat Panel TV : Televisions', 'Handheld : Camcorder', 'Headphones : Accessories', 'Home Theater Systems : Stereo Systems']
        expected_yval_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 11: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 11: Verify first bar color")
        xaxis_value="Product Subcategory : Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 11: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11: Verify Y-Axis Title")
        time.sleep(10)
        a=['Product Subcategory:Flat Panel TV', 'Product Category:Televisions', 'Revenue:$74,962,843.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody1','riser!s0!g0!mbar',a,"Step 11: Verify filtered 1st bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108835_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
        Step 12: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 13: Click "Save" in the toolbar > Type C2108835 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)



if __name__ == '__main__':
    unittest.main()