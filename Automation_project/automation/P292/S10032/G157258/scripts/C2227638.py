'''
Created on 23-Mar-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227638
TestCase Name = Alphanumeric Filter with Define field
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon,visualization_properties,visualization_run,define_compute,metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227638_TestClass(BaseTestCase):

    def test_C2227638(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227638'
        
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
        defcomobj = define_compute.Define_Compute(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double-click "Days,Delayed" and "Shipment,Unit(s)", located under Shipment Measures
        """
        metaobj.datatree_field_click('Days,Delayed', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Shipment Unit(s)', 2, 1)
        time.sleep(5)  
        
        """
        Step 03: Select Calculation > Detail (Define) in the Home Tab ribbon
        Step 04: Type "Product" for Field name, change Format to A40V
        Step 05 :Expand Product Dimension > Double click "Product,Category"
        Step 06: Click OK
        """ 
        defcomobj.calculate_define_compute('Define', 'Product', 'A40V', 'Product,Category', 1, 'ok')
        time.sleep(2)
        
        """
        Step 07: Verify Define field "Product" appears in the Data pane
        """
        metaobj.verify_data_pane_field('Dimensions',"Product",6,"Step 07: Verify define field Product appears in data pane")
        time.sleep(2)
        
        """
        Step 08: Double click "Product" to add field to Canvas
        """
        new_metaobj.double_click_on_data_filed('Dimensions->Product', 2)
        time.sleep(5)
             
        """
        Step 09: Drag and drop "Product" from Data pane into the Filter pane
        """
        new_metaobj.drag_and_drop_data_field_to_filter('Dimensions->Product', 2)
        time.sleep(15)
        
        """
        Step 10: Verify Filter dialog
        Step 11: Uncheck "[All]"
        Step 12: Select "Accessories", "Camcorder", "Computers" and "Stereo Systems"
        Step 13: Click OK
        """
        item_list=['[All]', 'Accessories', 'Camcorder', 'Computers','Media Player', 'Stereo Systems','Televisions', 'Video Production']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true')
        time.sleep(2)
        l=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Stereo Systems']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(2)
        
        """
        Step 14: Verify Canvas
        """
        metaobj.verify_filter_pane_field('Product',1,"Step14: Verify 'Product' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, 'Accessories', verify=True, verify_type=True, msg="Step14: Verify Accessories is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Camcorder', verify=True, verify_type=True, msg="Step14: Verify Camcorder is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', verify=True, verify_type=True, msg="Step14: Verify Computers is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step14: Verify Stereo Systems is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 4, 'Step 14a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 14b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.c(i) Verify first bar color")
        xaxis_value="Product"
        yaxis_value=["Days Delayed","Shipment Unit(s)"]
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1_f", yaxis_value, "Step 14:d(ii) Verify Y Axis legends") 
        expected_tooltip=['Product:Accessories', 'Days Delayed:59,803', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 14e: verify the default tooltip values")      
                
        """
        Step15: Click Run
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
          
        """
        Step16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1) 
        elem1=(By.CSS_SELECTOR, "div[id*='ibi$container$inner']")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227637_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)        
        propertyobj.select_or_verify_show_prompt_item(1, 'Accessories', verify=True, verify_type=True, msg="Step16: Verify Accessories is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Camcorder', verify=True, verify_type=True, msg="Step16: Verify Camcorder is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', verify=True, verify_type=True, msg="Step16: Verify Computers is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step16: Verify Stereo Systems is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 4, 'Step 16a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c(i) Verify first bar color")
        xaxis_value="Product"
        yaxis_value=["Days Delayed","Shipment Unit(s)"]
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 16:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1_f", yaxis_value, "Step 16:d(ii) Verify Y Axis legends") 
        expected_tooltip=['Product:Accessories', 'Days Delayed:59,803', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 16e: verify the default tooltip values")      
         
        """
        Step17: Close output window
        Step18: Click Save in the toolbar
        Step19: Save as "C2227638" > Click Save
        Step20: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, '#applicationButton')
        resultobj._validate_page(elem1)
         
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
         
        """
        Step 21: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227638.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1', mrid='mrid', mrpass='mrpass')
         
        """
        Step22: Verify Canvas
        """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
         
        metaobj.verify_filter_pane_field('Product',1,"Step22: Verify 'Product' appears in filter pane")        
        propertyobj.select_or_verify_show_prompt_item(1, 'Accessories', verify=True, verify_type=True, msg="Step22: Verify Accessories is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Camcorder', verify=True, verify_type=True, msg="Step22: Verify Camcorder is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', verify=True, verify_type=True, msg="Step22: Verify Computers is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Stereo Systems', verify=True, verify_type=True, msg="Step22: Verify Stereo Systems is checked in filter prompt")
        
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 4, 'Step 22a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 22b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.c(i) Verify first bar color")
        xaxis_value="Product"
        yaxis_value=["Days Delayed","Shipment Unit(s)"]
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 22:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1_f", yaxis_value, "Step 22:d(ii) Verify Y Axis legends") 
        expected_tooltip=['Product:Accessories', 'Days Delayed:59,803', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 22e: verify the default tooltip values")                       
        time.sleep(5)
        

if __name__ == '__main__':
    unittest.main()
    