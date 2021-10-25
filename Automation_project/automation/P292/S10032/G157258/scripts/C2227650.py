'''
Created on Apr 13, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227650
Test case Name =  Filter with Integer field 'Quarter'
'''

import unittest, time, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from selenium.webdriver.common.by import By

class C2227650_TestClass(BaseTestCase):

    def test_C2227650(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227650_1'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Gross Profit",2,1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 2)
                
        """
        Step03: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > Double click "Sale,Year"
        Step04: Drag and drop "Sale,Quarter" into the Columns bucket in the Query pane
        """
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Quarter", 1, 'Columns', 0)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 24)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 48)        
        """
        Step05: Drag and drop "Sale,Quarter" into the Filter pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Quarter", 1)       
        time.sleep(6)
                
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """               
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"1","Step 06.01: Verify From in Filter dialog")
                
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"4","Step 06.02: Verify To in Filter dialog")
                
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)
                 
        """
        Step 08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Quarter',1,"Step08: Verify 'Sale,Quarter' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',1,'int',msg="Step 09.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4,'int',msg="Step 09.02: Verify filter prompt range values-max")
        time.sleep(5)  
                 
        xaxis_value="Sale Quarter : Sale Year"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 09.03: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 09.04: Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 48, 'Step  09.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", "bar_blue", "Step 09.07: Verify first bar color")
        time.sleep(5)
        expected=['1', '2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 09.08: Verify column header")
          
#         bar=['Sale Quarter:1', 'Sale Year:2016', 'Cost of Goods:$78,102,759.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", bar, "Step 09.09: Verify bar value")
           
        """
        Step09: Drag left slider handle to the right > Change value to 2
        Step10: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,"#ar_Prompt_1 span[id$='s_min']")
        resultobj._validate_page(elem)        
        parent_elem=self.driver.find_element_by_css_selector("#ar_Prompt_1 span[id$='s_min']")
        utillobj.click_on_screen(parent_elem, 'middle',0,x_offset=0,y_offset=10)
        time.sleep(5)
        utillobj.click_on_screen(parent_elem, 'middle',0,x_offset=50,y_offset=10)
#         propertyobj.move_slider_measure("#ar_Prompt_1",'min', 'right', 1,'int')        
        time.sleep(3)
        elem=(By.CSS_SELECTOR,"#ar_Prompt_1 span[id$='s_min']")
        resultobj._validate_page(elem)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2,'int',msg="Step 10.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4,'int',msg="Step 10.02: Verify filter prompt range values-max")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 36) 
        xaxis_value="Sale Quarter : Sale Year"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 10.03: Verify X-Axis Title", custom_css='.gVertTitle')
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10.04: Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 36, 'Step 10.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", "bar_blue", "Step 10.07: Verify first bar color")
        time.sleep(5)
        expected=['2', '3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 10.08: Verify column header")
           
#         bar=['Sale Quarter:2', 'Sale Year:2016', 'Cost of Goods:$74,450,987.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", bar, "Step 10.09: Verify bar value")
                  
        """
        Step11: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
                        
        """
        Step12: Verify output
        Step13: Drag left slider handle to the right > Change value to 3 in the output window
        Step14: Verify output window
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 36) 
        elem1=(By.CSS_SELECTOR, "#sliderPROMPT_1")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2,'int',msg="Step 12.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',4,'int',msg="Step 12.02: Verify filter prompt range values-max")
             
        time.sleep(3)  
        xaxis_value="Sale Quarter : Sale Year"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 12.03: Verify X-Axis Title",custom_css='.gVertTitle')
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 12.04: Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 36, 'Step 12.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", "bar_blue", "Step 12.07: Verify first bar color")
        time.sleep(5)
        expected=['2', '3', '4']        
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Sale Year', expected,"Step 12.08: Verify column header")
          
#         bar=['Sale Quarter:2', 'Sale Year:2016', 'Cost of Goods:$74,450,987.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", bar, "Step 12.08: Verify bar value")
         
        elem1=(By.CSS_SELECTOR, "#sliderPROMPT_1")
        resultobj._validate_page(elem1)         
        slider_obj = utillobj.validate_and_get_webdriver_object("#sliderPROMPT_1 div[id^='slider_'] [class^='ui-slider-handle']", "Slider css")
        core_utils.python_left_click(slider_obj)
        pyautogui.hotkey('ctrl', 'up')
#         propertyobj.move_slider_measure("#sliderPROMPT_1",'min', 'right', 1, 'int')    This function has issue since done script level    
        time.sleep(3)
        elem1=(By.CSS_SELECTOR, "#sliderPROMPT_1")
        resultobj._validate_page(elem1)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',3,'int',msg="Step 14.01: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',4,'int',msg="Step 14.02: Verify filter prompt range values-max")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 24)      
        time.sleep(3)  
        xaxis_value="Sale Quarter : Sale Year"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 14.03: Verify X-Axis Title",custom_css='.gVertTitle')
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 14.04: Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 24, 'Step 14.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", "bar_blue", "Step 14.07: Verify first bar color")
        time.sleep(5)
        expected=['3', '4']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter : Sale Year', expected,"Step 14.08: Verify column header")
          
#         bar=['Sale Quarter:3', 'Sale Year:2016', 'Cost of Goods:$76,459,092.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", bar, "Step 14.09: Verify bar value")
                  
        time.sleep(20)
        
                  
        """
        Step15: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
     
        """
        Step16: Click Save in the toolbar
        Step17: Save as "C2227650" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                 
        """
        Step18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step19: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227650.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
                
        """
        Step20: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 18)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 36) 
        metaobj.verify_filter_pane_field('Sale,Quarter',1,"Step20: Verify 'Sale,Quarter' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2,'int',msg="Step 20.01:Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',4,'int',msg="Step 20.02: Verify filter prompt range values-max")
    
        time.sleep(3)  
        xaxis_value="Sale Quarter : Sale Year"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 20.03: Verify X-Axis Title",custom_css='.gVertTitle')
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 20.04: Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016', '2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 36, 'Step 20.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", "bar_blue", "Step 20.07: Verify first bar color")
        time.sleep(5)
        expected=['2','3', '4']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Sale Quarter', expected,"Step 20.08: Verify column header")
          
#         bar=['Sale Quarter:2', 'Sale Year:2016', 'Cost of Goods:$74,450,987.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar!r0!c0", bar, "Step 20.09: Verify bar value")
           
        """
        Step21: Logout
        """       
if __name__ == '__main__':
    unittest.main()