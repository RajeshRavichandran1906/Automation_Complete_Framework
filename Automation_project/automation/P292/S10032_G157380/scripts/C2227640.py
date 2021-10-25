'''
Created on 24-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227640
TestCase Name = Numeric Filter format D20.2M
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run,define_compute
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227640_TestClass(BaseTestCase):

    def test_C2227640(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227640'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
               
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(5)
               
        """
        Step 04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Year" into the Rows bucket (Matrix in Query pane)
        """
        metaobj.datatree_field_click('Sale,Year', 1, 1, 'Add To Query', 'Rows')
        time.sleep(5)
               
        """
        Step 05: Drag and drop "Cost of Goods" into the Filter pane
        """
        metaobj.datatree_field_click('Cost of Goods', 1, 1, 'Filter')
        time.sleep(5)
               
        """
        Step 06: Verify Filter dialog
        Step 07: Type 5000 in the "From" value input box
        Step 08: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        metaobj._validate_page(elem)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),16,"Step06: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),13000,"Step06: Verify range to value")  
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',['From',5000])
        time.sleep(2)
                
        """
        Step 09: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step09: Verify 'Cost of Goods' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5000,'int',msg="Step09: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step09: Verify filter prompt range values-max")
        time.sleep(2)
                
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step09a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'Firefox':
#             expected_yval_list=['0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M']
#         else:
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 09.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09:d(ii) Verify Y Axis Title") 
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 09: Verify column header")
        expected_tooltip=['Sale Year:2013', 'Product Category:Camcorder', 'Cost of Goods:$1,482,108.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r2!c0",expected_tooltip, "Step 09e: verify the default tooltip values")      
                 
        """
        Step10: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                  
        """
        Step11: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)    
         
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',5000, 'int',msg="Step11: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',13000,'int',msg="Step11: Verify filter prompt range values-max") 
        time.sleep(2)
                
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step11a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 11.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 11:d(ii) Verify Y Axis Title") 
    
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 11: Verify column header")
              
        expected_tooltip=['Sale Year:2013', 'Product Category:Camcorder', 'Cost of Goods:$1,482,108.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r2!c0",expected_tooltip, "Step 11e: verify the default tooltip values")      
                  
        """
        Step12: Close output window
        Step13: Click Save in the toolbar
        Step14: Save as "C2158163" > Click Save
        Step15: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
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
        Step 16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158163.fex&tool=idis
        Ste4p 17: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step16: Verify 'Cost of Goods' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5000,'int',msg="Step16: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step16: Verify filter prompt range values-max")
        time.sleep(2)
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 12, 'Step16a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
#         browser=utillobj.parseinitfile('browser')
#         if browser == 'Firefox':
#             expected_yval_list=['0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M', '0', '1.4M', '2.8M', '4.2M', '5.6M', '7M']
#         else:
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 16.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16:d(ii) Verify Y Axis Title") 
        expected=['2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 16: Verify column header")
        expected_tooltip=['Sale Year:2013', 'Product Category:Camcorder', 'Cost of Goods:$1,482,108.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r2!c0",expected_tooltip, "Step 16e: verify the default tooltip values")      
            
        """
        Step18: Edit the Prompt value > Drag slider handle to the right, at value 10061.81 (or approximate)
        """
        browser=utillobj.parseinitfile('browser')
        if browser =='Firefox':
            propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 2, 'float')#actual value as in testrail is 10061.81
        if browser in ['IE', 'Chrome']:
            propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 2, 'float')
         
        """
        Step19: Verify Canvas and Prompt 
        """
        if browser == 'Firefox':
            ran=10209
        if browser in ['IE', 'Chrome']:
            ran=10193
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',ran,'float',msg="Step19: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step19: Verify filter prompt range values-max")
        time.sleep(2)
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 9, 'Step19a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 19b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 19.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 19:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 19:d(ii) Verify Y Axis Title") 
        expected=['2012', '2013', '2014', '2015', '2016']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 19: Verify column header")
        expected_tooltip=['Sale Year:2014', 'Product Category:Camcorder', 'Cost of Goods:$81,400.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r2!c0",expected_tooltip, "Step 19e: verify the default tooltip values")      
          
        """
        Step20: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)    
            
        """
        Step21: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(15)        
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227640_Actual_step21_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)        
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 9, 'Step21a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Camcorder','Televisions']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '0', '50K', '100K', '150K', '200K', '250K', '300K', '350K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 21b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r2!c0", "bar_blue", "Step 21.c(i) Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 21:d(ii) Verify Y Axis Title") 
        expected=['2012', '2013', '2014', '2015', '2016']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year', expected,"Step 21: Verify column header")
        expected_tooltip=['Sale Year:2014', 'Product Category:Camcorder', 'Cost of Goods:$81,400.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar!r2!c0",expected_tooltip, "Step 21e: verify the default tooltip values")      
        time.sleep(5)
            
        """
        Step22: Close output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)          
        time.sleep(5) 
         
        """
        Step23: Right click "Cost of Goods" filter in the Filter pane > Edit
        """
        metaobj.filter_tree_field_click('Cost of Goods',1,1, 'Edit...')
        time.sleep(2)
         
        """
        Step24: Verify Filter dialog
        """
        if browser == 'Firefox':
            ran=10209
        if browser in ['IE', 'Chrome']:
            ran=10193
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(int(float(d['float_value'])),ran,"Step24: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),13000,"Step24: Verify range to value")  
        time.sleep(2)
         
        """
        Step25: Click Cancel
        """
        metaobj.create_visualization_filters('numeric',ok='Cancel')
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
    