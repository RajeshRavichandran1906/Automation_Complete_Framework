'''
Created on 28-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227642
TestCase Name = Numeric Filter format I11C
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227642_TestClass(BaseTestCase):

    def test_C2227642(self):
        
        """
        CLASS & OBJECTS
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227642'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        time.sleep(5)        
                
        """
        Step 02: Double-click "Quantity,Sold", located under Sales Measures
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        metaobj.datatree_field_click('Quantity,Sold', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(8)
                
        """
        Step04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Quarter" into the Columns bucket (Matrix in Query pane)
        Step05: Drag and drop "Sale,Quarter" into the Color bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Columns', 0)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Quarter', 1, 'Color', 0)
        time.sleep(5)
           
        """
        Step 06: Drag and drop "Quantity,Sold" into the Filter pane
        """
        metaobj.drag_drop_data_tree_items_to_filter('Quantity,Sold', 1)
        time.sleep(5)
               
        """
        Step 07: Verify Filter dialog
        Step 08: Click OK
        """
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),1,"Step 07.01: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),4,"Step 07.02: Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
                 
        """
        Step 09: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Quantity,Sold',1,"Step09: Verify 'Quantity,Sold' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',1, 'int',msg="Step 09.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4, 'int',msg="Step 09.02: Verify filter prompt range values-max")
        time.sleep(2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "QuantitySold", 45)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 83, 60)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 83, 'Step 09.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Cont...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 09.05: Verify first bar color")
        xaxis_value="Sale Quarter : Product Subcategory"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09.06: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 09.07: Verify Y Axis Title") 
        time.sleep(2)
        resultobj.verify_riser_legends('MAINTABLE_wbody1', ['Sale Quarter', '1', '2', '3', '4'],"Step 09.08: Verify Chart Legend")
        expected=['1', '2', '3']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 09.09: Verify column header")
         
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!r0!c1", "pale_green", "Step 09.10: Verify first bar color")
                               
        """
        Step10: Click Save in the toolbar
        Step11: Save as "C2227642" > Click Save
        Step12: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
          
        """
        Step13: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2227642.fex&tool=idis
        Step14: Verify Canvas
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('Quantity,Sold',1,"Step14: Verify 'Quantity,Sold' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',1, 'int',msg="Step 14.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4, 'int',msg="Step 14.02: Verify filter prompt range values-max")
        time.sleep(2)
              
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 83, 'Step 14.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Cont...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 14.05: Verify first bar color")
        xaxis_value="Sale Quarter : Product Subcategory"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14.06: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 14.07: Verify Y Axis Title") 
        time.sleep(2)
        resultobj.verify_riser_legends('MAINTABLE_wbody1', ['Sale Quarter', '1', '2', '3', '4'],"Step 14.08: Verify Chart Legend")
        expected=['1', '2', '3']
        resultobj.wait_for_property("#MAINTABLE_wbody1 g.scrollColLbl > g text", 4)
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Subcategory', expected,"Step 14.09: Verify column header")
       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!r0!c1", "pale_green", "Step 14.10: Verify first bar color")
       
          
        """
        Step15: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
             
        """
        Step16: Verify output
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "div[id*='ibi$container$inner']")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227642_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',1, 'int',msg="Step 16.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',4, 'int',msg="Step 16.02: Verify filter prompt range values-max")
        time.sleep(2)
               
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 83, 'Step 16.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Cont...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step 16.05: Verify first bar color")
        xaxis_value="Sale Quarter : Product Subcategory"
        yaxis_value="Quantity Sold"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16.06: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 16.07: Verify Y Axis Title") 
        time.sleep(2)
        resultobj.verify_riser_legends('MAINTABLE_wbody1', ['Sale Quarter', '1', '2', '3', '4'],"Step 16.08: Verify Chart Legend")
        expected=['1', '2', '3', '4']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Product Subcategory', expected,"Step 16.09: Verify column header")
       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s1!g0!mbar!r0!c1", "pale_green", "Step 16.10: Verify first bar color")
       
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s2!g0!mbar!r0!c2", "dark_green", "Step 16.11: Verify first bar color")
                 
        """
        Step17: Close output window
        """
        

if __name__ == '__main__':
    unittest.main()