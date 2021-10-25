'''
Created on Apr 13, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227670
Test case Name =  Filter Aggregation - Count
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227670_TestClass(BaseTestCase):

    def test_C2227670(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227670'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
     
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
             
        """
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(5)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
             
        """
        Step04: Drag and drop "Cost of Goods" to the Filter pane
        Step05: Click "Aggregation" dropdown menu > Select "Count"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods", 1, 1,"Filter")        
        time.sleep(6)
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        combo=['(None)', 'Sum', 'Average', 'Count', 'Distinct Count', 'Maximum', 'Minimum', 'Percent', 'Median']
        utillobj.select_any_combobox_item(elem,'Count',verify=True,expected_combobox_list=combo, msg="Step05: Verify list of agregation functions")
             
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Count',"Step06: Verify Aggregation in Filter dialog")
        time.sleep(5)      
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"3268","Step06: Verify From in Filter dialog")
        time.sleep(5)     
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"481547","Step06: Verify To in Filter dialog")
             
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)
              
        """
        Step 08: Verify filter in the Filter pane
        Step 09: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,"#ar_Prompt_1 span[id$='s_min']")
        resultobj._validate_page(elem)
        time.sleep(5)
        metaobj.verify_filter_pane_field('CNT (Cost of Goods)',1,"Step08: Verify 'Count(Cost of Goods)' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',3268,'int',msg="Step09: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',481547,'int',msg="Step09: Verify filter prompt range values-max")
        time.sleep(5)  
              
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Con...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09: Verify bar value")
             
        """
        Step 10: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
 
             
        """
        Step11: Verify output
        Step12: Hover over "Standard" riser
        Step13: Verify "Cost of Goods" value > $49,071,633.00
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#LOBJ1_cs")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','min',3268,'int',msg="Step11: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','max',481547,'int',msg="Step11: Verify filter prompt range values-max")
          
        time.sleep(3)  
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Con...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g17!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        bar=['Product Subcategory:Standard', 'Cost of Goods:$49,071,633.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        time.sleep(5)
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g15!mbar", bar, "Step 12: Verify bar value")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227669_Actual_Step12', image_type='actual',x=1, y=1, w=-1, h=-1) 
               
        """
        Step14: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
  
        """
        Step15: Click Save
        Step16: Click Save as "C2158200" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
              
        """
        Step17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step18: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step19: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(3)
        elem1=(By.CSS_SELECTOR, "#ar_Prompt_1")
        resultobj._validate_page(elem1)
        metaobj.verify_filter_pane_field('CNT (Cost of Goods)',1,"Step19: Verify 'CNT(Cost of Goods)' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',3268,'int',msg="Step19: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',481547,'int',msg="Step19: Verify filter prompt range values-max")
        time.sleep(5)  
          
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step19: Verify bar value")
         
        """
        Step20: Logout
        """     

        
if __name__ == '__main__':
    unittest.main()
        