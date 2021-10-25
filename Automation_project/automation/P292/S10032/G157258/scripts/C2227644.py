'''
Created on 29-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227644
TestCase Name = Date Filter with Attributes date field YYMD - Sale,Date
'''
import unittest,time
from datetime import datetime
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run,define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227644_TestClass(BaseTestCase):

    def test_C2227644(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227644'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        browser=utillobj.parseinitfile('browser')
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']         
        resultobj._validate_page(elem1)         
                  
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit"
        """
        time.sleep(3)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(5)
            
        """
        Step03: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > "Sale,Day" > "Attributes" > Double click "Sale,Date" to add it to the canvas
        """
        metaobj.datatree_field_click('Sale,Date', 2, 1)
        time.sleep(5)
                    
        """
        Step04: Drag and drop "Sale,Date" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Sale,Date', 1)
#         metaobj.datatree_field_click('Sale,Date', 1, 1, 'Filter')
        time.sleep(5)
                   
        """
        Step 05: Verify Filter dialog    Screenshot in testrail mismatch when edit    
        """
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Jan',"Step05.1: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'01',"Step05.1: Verify range from value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2011,"Step05.1: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step05.2: Verify range to value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step05.2: Verify range to value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step05.2: Verify range to value")
        time.sleep(2)
        
            
        """
        Step08: Change Starting Date to 01/01/2015
        Step07: Click OK                 
        """
        l1=['Jan','01','2015']
        metaobj.create_visualization_filters('numeric',['Starting Date',l1])
           
        """
        Step 08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Date',1,"Step08: Verify 'Sale,Date' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','01/01/2015','str',msg="Step08: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','03/19/2017','str',msg="Step08: Verify filter prompt range values- max")
         
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1460) 
        time.sleep(5)         
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step08a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03', '2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step08b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step08.c(i) Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step08:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(ii) Verify Y-Axis Title")
        expected_tooltip=['Sale Date:2015/01/01', 'Cost of Goods:$554,291.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step08e: verify the default tooltip values")      
                        
        """
        Step09: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                
        """
        Step10: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','01/01/2015','str',msg="Step10: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','03/19/2017','str',msg="Step10: Verify filter prompt range values- max") 
        time.sleep(2)
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step10a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03', '2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step10b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step10.c(i) Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        expected_tooltip=['Sale Date:2015/01/01', 'Cost of Goods:$554,291.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step10e: verify the default tooltip values")      
                        
        """
        Step11: Close output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)          
        time.sleep(5)      
                                       
        """
        Step12: Click Save in the toolbar
        Step13: Save as "C2158163" > Click Save
        Step14: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
             
        """
        Step15: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        Step16: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Sale,Date',1,"Step16: Verify Sale Date appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','01/01/2015','str',msg="Step16: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','03/19/2017','str',msg="Step16: Verify filter prompt range values- max")
        time.sleep(2)
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 730, 'Step16a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2015/01/01', '2015/01/02', '2015/01/03','2015/01/30', '2015/01/31', '2015/02/01']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step16b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step16.c(i) Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step16:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:d(ii) Verify Y-Axis Title")
        expected_tooltip=['Sale Date:2015/01/01', 'Cost of Goods:$554,291.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step16e: verify the default tooltip values")      
            
        """
        Step17: Drag left slider handle (in the Filter Prompt) to the right > change starting value to 12/25/15
        Step18: Verify Canvas
        """
        time.sleep(5)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str')       
        elem1=(By.CSS_SELECTOR, '#ar_Prompt_1')
        resultobj._validate_page(elem1)
          
        time.sleep(5)        
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','03/29/2016','str',msg="Step18: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','03/19/2017','str',msg="Step18: Verify filter prompt range values- max")
        time.sleep(2)
                  
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 278, 'Step18a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2016/03/29', '2016/03/30', '2016/03/31', '2016/12/29', '2016/12/30', '2016/12/31']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step16b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step18.c(i) Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step18:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18:d(ii) Verify Y-Axis Title")
        expected_tooltip=['Sale Date:2016/03/29', 'Cost of Goods:$834,400.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step18e: verify the default tooltip values")      
            
        """
        Step19: Right click "Sale,Date" filter in the Filter pane
        Step20: Verify dialog and Cancel 
        """
        time.sleep(2)
        metaobj.filter_tree_field_click('Sale,Date', 1, 1, 'Edit...')
        time.sleep(2)
           
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step20.1: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'29',"Step20.1: Verify range from value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerFrom #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2016,"Step20.1: Verify range from value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb1 input")
        d=utillobj.get_attribute_value(elem1, "text_value")
        utillobj.asequal(d['text_value'],'Mar',"Step20.2: Verify range to value")
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb2 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],'19',"Step20.2: Verify range to value")  
        elem1=driver.find_element_by_css_selector("#dateTimePickerTo #dateInputCmb3 input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),2017,"Step20.2: Verify range to value")
        time.sleep(2)
   
        metaobj.create_visualization_filters('numeric',ok='cancel')
        time.sleep(2)
        self.fail("Screenshot in testrail mismatch when edit")
        """
        Step21: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
               
        """
        Step22: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(15)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)     
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','03/29/2016','str',msg="Step22: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','03/19/2017','str',msg="Step22: Verify filter prompt range values- max")
        time.sleep(2)
                 
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 278, 'Step22a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['2016/03/29', '2016/04/29', '2016/12/29', '2016/12/30', '2016/12/31']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step22b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step22.c(i) Verify first bar color")
        xaxis_value="Sale Date"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step22:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step22:d(ii) Verify Y-Axis Title")
        expected_tooltip=['Sale Date:2016/03/29', 'Cost of Goods:$834,400.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step22e: verify the default tooltip values")      
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step22_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
                 
        """
        Step23: Close output window
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
    