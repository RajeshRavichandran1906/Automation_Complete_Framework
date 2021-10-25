'''
Created on Apr 20, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227652
Test case Name =  Filter with Integer field 'Day'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227652_TestClass(BaseTestCase):

    def test_C2227652(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227652'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
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
        Step03: Expand Product Dimension > Double click "Product,Subcategory"
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > Drag and drop "Sale,Day" into the Rows bucket in the Query pane
        """
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 42)
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Day", 1, 'Rows', 0)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 186)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 1302)        
        """
        Step05: Drag and drop "Sale,Day" into the Filter pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Day", 1)        
        time.sleep(6)
                
        """
        Step06: Verify Filter dialog
        Step07: Click "Operators" dropdown box > select "Greater than or equal to"
        Step08: Change "From" value to 15
        Step09: Click OK
        """               
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"1","Step06: Verify From in Filter dialog")
                
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"31","Step06: Verify To in Filter dialog")
 
        metaobj.create_visualization_filters('numeric',['Operator','Greater than or equal to'],['From','15'])
                  
        """
        Step10: Verify Canvas
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 102)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 714)
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step10: Verify 'Sale,Day' appears in filter pane")
          
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',15,'int',msg="Step10: Verify minimum Slider range is 15")
        time.sleep(5)  
                   
        xaxis_value="Product Subcategory"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 714, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        expected=['15','16','17','18','19','20']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Day', expected,"Step10: Verify Row header")
                 
        """
        Step11: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)
                 
        """
        Step12: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 102)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 714) 
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',15,'int',msg="Step12: Verify minimum Slider range is 15")
        time.sleep(5)
                  
        xaxis_value="Product Subcategory"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step12:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step12:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 714, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        expected=['15','16','17','18','19','20','21','22']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Day', expected,"Step12: Verify Row header")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227652_Actual_Step12', image_type='actual',x=1, y=1, w=-1, h=-1)
                           
        """
        Step13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
      
        """
        Step14: Click Save in the toolbar
        Step15: Save as "C2227652" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                  
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227652.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
                 
        """
        Step18: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 102)
        parent_css= "#MAINTABLE_wbody1 rect[class*='riser']"
        resultobj.wait_for_property(parent_css, 714)  
        metaobj.verify_filter_pane_field('Sale,Day',1,"Step18: Verify 'Sale,Day' appears in filter pane")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',15,'int',msg="Step18: Verify minimum Slider range is 15") 
        time.sleep(5)  
                  
        xaxis_value="Product Subcategory"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step18:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 714, 'Step18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step18.c: Verify first bar color")
        time.sleep(5)
        expected=['15','16','17','18','19','20']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Day', expected,"Step18: Verify Row header")
           
        """
        Step19: Logout
        """
        
if __name__ == '__main__':
    unittest.main()