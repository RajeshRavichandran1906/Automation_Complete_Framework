'''
Created on May04, 2016
Fixed on Sept 27, 2016
@author: gobizen
@Fixedby: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8357
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2107416
'''

__author__ = "Nasir"
__copyright__ = "IBI"

import unittest
from selenium.webdriver import ActionChains
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By
import time
from common.lib.basetestcase import BaseTestCase

class C2107416_TestClass(BaseTestCase):

    def test_C2107416(self):
        
        driver = self.driver #Driver reference object created
        defcomp=define_compute.Define_Compute(self.driver)
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2107416'
        name = 'MYDATE_MYY'
        
        """
        Step 01: Launch the IA API with ggorder    
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/ggorder&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/ggorder','P312/S10099_4', 'mrid', 'mrpass')
        element_css="#resultArea svg>g.chartPanel rect[class*='riser!']"
        utillobj.synchronize_with_number_of_element(element_css, 12, 60)
        #utillobj.infoassist_api_login('idis','baseapp/ggorder','S8357', 'mrid01', 'mrpass01')
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
 
        """
        Step 02: Create a new Calculation -> Define.
        Step 03 : In the DEFINE dialogue box, enter field name of MYDATE_MYY.
        Step 04: Click on the Format button, select "Date", and choose the format of "MYY", click OK
        Step 05: Select "Order,Date" from the field list, Click OK.
        """
        defcomp.calculate_define_compute('Define', name,'MYY', 'Order,Date', 1, 'ok')
    
        """
        Step 06 : Verify define is added to data pane.
        """
        time.sleep(3) 
        metaobj.verify_data_pane_field('Dimensions', 'MYDATE_MYY', 9, 'Step 06')
        '''define = driver.find_element_by_xpath(InfoassistLocators.common_xpath.format(name))
        if define.is_displayed() is True:
            pass #Validation will be passed to xml
        else:
            print('MYDATE_MYY not added in data pane')'''
        
        """
        Step 07: Add MYDATE_MYY to Horizontal Axis and Unit, Price to Vertical Axis.
        """
        metaobj.datatree_field_click('Dimensions->MYDATE_MYY', 2, 1)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Unit,Price', 1, 'Vertical Axis', 0)
        element_css="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Unit Price', 45, 1)
        time.sleep(10) #loads the chart details
        
        """
        Step 08 : Verify x and Y axis labels in preview.
        """
        
        time.sleep(12)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 25)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 25, 'Step 08a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['11/1990', '01/1996', '02/1996','03/1996','04/1996']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 08.c(i) Verify first bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g17!mbar!", "bar_blue", "Step 08.c(ii) Verify second bar color")
        xaxis_value="MYDATE_MYY"
        yaxis_value="Unit Price"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 08:d(ii) Verify Y-Axis Title")
        
 
        """
        Step 09:Verify first 5 and last 5 chart/grid values (tooltip values).
        First 5 values on tooltip - 11/1990:81.00 , 01/1996:10,698.00, 02/1996:10,698.00, 03/1996:10698.00, 04/1996:10,698.00,
        Last 5 values on tooltip - 08/1997:10,797.00, 09/1997:10,797.00, 10/1997:10,797.00, 11/1997:10,716.00, 12/1997:10,797.00
        Similarly verify first 5 and last 5 values.
        """
        time.sleep(5)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(5)
        expected_tooltip=['MYDATE_MYY:01/1996', 'Unit Price:10,698.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 09.a: verify the default tooltip values")
        time.sleep(5)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(5)
         
        expected_tooltip=['MYDATE_MYY:12/1997', 'Unit Price:10,797.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mbar",expected_tooltip, "Step 09.b: verify the default tooltip values")
       
        time.sleep(5)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(5)
         
        """
        Step 10: Hover over one of the bars(06/1996) and select "Filter"..
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', 'riser!s0!g6!mbar!', 'Filter Chart')
        time.sleep(10)
         
        """
        Step 11 : Verify Query is added to filter pane.
        """
        metaobj.verify_filter_pane_field(name, 1, 'Step 11: Verify Query is added to filter pane')
 
        """
        Step 12: Verify exact value got filtered.
        """
        time.sleep(5)
        parent_css1="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 12a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['06/1996']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step 12.c(i) Verify first bar color")
        xaxis_value="MYDATE_MYY"
        yaxis_value="Unit Price"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 08:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 08:d(ii) Verify Y-Axis Title")
        expected_tooltip=['MYDATE_MYY:06/1996', 'Unit Price:10,323.00']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 12.a: verify the default tooltip values")
        time.sleep(15)
        ele = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillity.UtillityMethods.click_type_using_pyautogui(self, ele, move=True)
        else:
            action = ActionChains(driver)
            action.move_to_element_with_offset(ele,1,1).perform()
        time.sleep(2)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#TableChart_1"),'C2107416_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 13 : Click "Save" in the toolbar > Type C2107416 > Click "Save" in the Save As dialog
        """
        time.sleep(2)  
        #ribbonobj.select_tool_menu_item('menu_save_as')
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
       

if __name__ == '__main__':
    unittest.main()

