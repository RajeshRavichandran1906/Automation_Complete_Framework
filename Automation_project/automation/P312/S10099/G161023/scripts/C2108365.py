'''
Created on May'3, 2016
@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357&group_by=cases:section_id&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107416&group_by=cases:section_id&group_id=146864&group_order=asc
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from common.lib import take_screenshot
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_ribbon_locators, visualization_properties_locators, visualization_resultarea_locators
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2108365_TestClass(BaseTestCase):

    def test_C2108365(self):
        driver = self.driver #Driver reference object created
        
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2108365'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
#         VisualizationRibbonLocators = visualization_ribbon_locators.VisualizationRibbonLocators(self.driver)
        #utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S8357', 'mrid02', 'mrpass02')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_4', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)    
        time.sleep(10)
        """
        Step 02: Double Click Gross Profit
        """
        metaobj.datatree_field_click('Gross Profit',2,1)
        """
        Step 03: Double Click Product,Category
        """
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category',2,1)
        """
        Step 04: Verify x and y axis labels.
        """
        time.sleep(12)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 04a: Verify the total number of risers displayed on Preview Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 04b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 04.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 04:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 04:d(ii) Verify Y-Axis Title")
        time.sleep(5)
        expected_tooltip=['Product Category:Stereo Systems', 'Gross Profit:$86,181,070.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar",expected_tooltip, "Step 04.e: verify the default tooltip values")
        time.sleep(8)
        
        """
        Step 05: Drag and Drop Sale, Year to filter.
        """
        #metaobj.datatree_field_click('Sale,Year', 1,1,'Filter')
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Year',0)
        """
        Step 06: Click "Operator" dropdown box > Select "Equal to"
        Step 07: Verify Dialog
        Step 08: Click Ok
        """
        #l = ['[All]','2', '4','5']
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'])
        #utillobj.select_combobox_item("'numericAndDateFieldPanel'] div[id*='OperatorComboBox'", "Equal to")
        #time.sleep(2)
        #driver.find_element_by_id("avFilterOkBtn").click()
        time.sleep(10)
        
        """
        Step 09: Verify Filter pane
        """
        metaobj.verify_filter_pane_field("Sale,Year", 1, "Step 09: Verify Filter pane")
        
        """
        Step 10: Verify Preview
        """
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=True, msg='Step 10a: verify the ALL is checked under Show prompt')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 10b: Verify the total number of risers displayed on Preview Chart')
        time.sleep(10)
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 10c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 10d(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 10e(ii) Verify Y-Axis Title")
        time.sleep(10)
        expected_tooltip=['Product Category:Stereo Systems', 'Gross Profit:$86,181,070.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mbar",expected_tooltip, "Step 10f: verify the default tooltip values")
        
        """
        Step 11: Click "Run" in the toolbar
        """
        time.sleep(3) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(10)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """
        Step 12: Verify Output
        """
        time.sleep(15)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=True, msg='Step 12a: verify the ALL is checked under Show prompt')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 12b: Verify the total number of risers displayed on Run Chart')
        x_val_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_val_list=['0', '20M', '40M', '60M', '80M', '100M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 12c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 12d(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 12e(ii) Verify Y-Axis Title")
        expected_tooltip=['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 12f: verify the default tooltip values")
        time.sleep(5)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2108365_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 13: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        
        """
        Step 14: Click "Save" in the toolbar > Type C2108365 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)


if __name__ == '__main__':
    unittest.main()

