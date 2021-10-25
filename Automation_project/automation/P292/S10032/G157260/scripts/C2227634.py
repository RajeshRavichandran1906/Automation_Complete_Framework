'''
Created on May 09, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227634
Test case Name =  Verify Filter using "Values" in the Data Pane - Sale,Day - 2014
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run, metadata
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227634_TestClass(BaseTestCase):

    def test_C2227634(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227634'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
   
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
                   
        """
        Step 03: Expand Product Dimension > Double click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
           
        """
        Step04: Expand Dimension "Sales_Related" > "Transaction Date,Simple" > "Values"
        Step05: Double click year value "2014"
        """
        time.sleep(4)
        new_metaobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(6)
        metaobj.expand_field_tree('Sales_Related')
        time.sleep(2)
        metaobj.expand_field_tree('Transaction Date, Simple')
        time.sleep(2)
        metaobj.expand_field_tree('Values')
        time.sleep(2)
        metaobj.expand_field_tree('2014')
        time.sleep(5)
        metaobj.verify_data_pane_field('2014',"1",1,"Step 05.1: Verify 1 displayed  below 2014")
        metaobj.verify_data_pane_field('2014',"2",2,"Step 05.2: Verify 2 displayed  below 2014")
        metaobj.verify_data_pane_field('2014',"3",3,"Step 05.3: Verify 3 displayed  below 2014")
        metaobj.verify_data_pane_field('2014',"4",4,"Step 05.4: Verify 4 displayed  below 2014")

          
        """
        Step06: Drag and drop year value "2014" into the Filter pane
        """
        new_metaobj.drag_and_drop_data_field_to_filter('Dimensions->Sales_Related->Transaction Date, Simple->Values->2014', 1)
        time.sleep(2)      
         
        """
        Step07: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
         
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '4M','8M','12M','16M','20M','24M','28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$23,374,330.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step07: Verify bar value")
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, '2014', verify=True, verify_type=True, msg="Step07: Verify 2014 is checked in filter prompt")
                  
        """
        Step08: Right-click "Sale,Year" in the Filter pane > Edit...
        Step09: Verify Filter dialog
        Step10: Click 'Operator' dropdown > Select 'Range'
        Step11: Change "From" value to 2014, Change "To" value to 2015
        Step12: Click OK
        """
          
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.filter_tree_field_click("Sale,Year", 1, 1,"Edit...")
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        item_list=['2014']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true',msg = 'step09: Filter dialog')
        metaobj.create_visualization_filters('numeric',['Operator','Range'],['From','2014'],['To','2015'])
        time.sleep(3) 
                
        """
        Step13: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#ar_Prompt_1')
        resultobj._validate_page(elem)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step13: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2015,'int',msg="Step13: Verify filter prompt range values-max")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '20M','40M','60M','80M','100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$73,896,386.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar, "Step13: Verify bar value")
        time.sleep(5)       
         
        """
        Step14: Drag right slider handle to the right > change value from 2015 to 2016
        """
        propertyobj.move_slider_measure("#ar_Prompt_1",'max', 'right', 1,'int')        
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#ar_Prompt_1')
        resultobj._validate_page(elem)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step14: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2016,'int',msg="Step14: Verify filter prompt range values-max")
        time.sleep(2)
                 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step14:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step14.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$151,106,996.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar,"Step14: Verify bar value")
        time.sleep(5) 
         
        """
        Step15: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
              
        """
        Step16: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step16:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$151,106,996.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar,"Step16: Verify bar value")
         
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227634_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
             
        """
        Step17: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                 
        """
        Step18: Click Save in the toolbar
        Step19: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                 
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)  
         
        """
        Step21: Reopen
        Step22: Verify canvas
        """ 
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
        elem=(By.CSS_SELECTOR,'#ar_Prompt_1')
        resultobj._validate_page(elem)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step22: Verify filter prompt range values-min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2016,'int',msg="Step22: Verify filter prompt range values-max")
        time.sleep(2)
                  
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step22:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step22.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$151,106,996.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar", bar,"Step22: Verify bar value")
        time.sleep(5) 
 

if __name__ == '__main__':
    unittest.main()



    
     
        