'''
Created on Jun 16, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227720
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227720_TestClass(BaseTestCase):

    def test_C2227720(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227720'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
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
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """
        Step 02: Double click "Gross Profit", "Product,Category".
        """
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
                 
        """
        Step03: Drag "Store Type" to Matrix - Columns.
        Step04: Verify the following chart is displayed.
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Store Type", 1, 1,"Add To Query", 'Columns')
         
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step04:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step04:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step04.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step04: Verify Column header")
            
        bar=['Store Type:Store Front', 'Product Category:Accessories', 'Gross Profit:$27,674,694.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step04: Verify bar value")
                 
        """
        Step05: Drag "Store Type" to the Filter pane.
        Step06: Click "OK" on "Filter for Store Type".
        Step07: Verify "Store Type" filter has been placed into the Filter pane.
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 14)
        metaobj.datatree_field_click("Store Type", 1, 1,"Filter")        
        time.sleep(6)
        metaobj.create_visualization_filters('alpha')
        time.sleep(2) 
        metaobj.verify_filter_pane_field('Store Type',1,"Step07: Verify 'Store Type' appears in filter pane")        
         
        """
        Step08: Verify Filter Prompts appears on the canvas (rightmost area) with [All] checkbox checked.
        """
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step08: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=False,msg="Step08: Verify Store Front unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=False,msg="Step08: Verify Web unchecked in prompt")
         
        """
        Step09: Enable "Store Front" checkbox.
        """
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=False,msg="Step09: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step09: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=False,msg="Step09: Verify Web unchecked in prompt")
         
        """
        Step10: Verify the following chart is displayed.
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
         
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step10:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step10: Verify Column header")
            
        bar=['Store Type:Store Front', 'Product Category:Accessories', 'Gross Profit:$27,674,694.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step10: Verify bar value")
         
        """
        Step11: Disable "Store Front" checkbox.
        Step12: Verify that [All] checkbox has been selected.
        Step13: Enable "Web" checkbox.
        Step14: Verify the following chart is displayed.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=True,msg="Step12: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=False,msg="Step12: Verify Store Front unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step12: Verify Web checked in prompt")
         
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
         
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step14:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step14:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step14.c: Verify first bar color")
        time.sleep(5)
        expected=['Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step14: Verify Column header")
            
        bar=['Store Type:Web', 'Product Category:Accessories', 'Gross Profit:$12,179,745.81', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step14: Verify bar value")
         
        """
        Step15: Enable "Store Front" checkbox.
        Step16: Verify the following chart is displayed.
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=False)
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step16: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step16: Verify Web checked in prompt")
         
        parent_css= "#MAINTABLE_wbody1 g.scrollColTitle"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step16:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", "Gross Profit", "Step16:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 14, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step16.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step16: Verify Column header")
            
        bar=['Store Type:Store Front', 'Product Category:Accessories', 'Gross Profit:$27,674,694.72', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step16: Verify bar value")
         
        """
        Step17: Drag "Product,Category" to the Filter pane.
        Step18: Click "OK" on "Filter for Product,Category".
        Step19: Verify "Product,Category" filter has been placed into the Filter pane.
        Step20: Verify Filter Prompts appears on the canvas (rightmost area) with [All] checkbox checked.
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 14)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")        
        time.sleep(6)
        metaobj.create_visualization_filters('alpha')
        time.sleep(2) 
        metaobj.verify_filter_pane_field('Store Type',1,"Step19: Verify 'Store Type' appears in filter pane")        
        metaobj.verify_filter_pane_field('Product,Category',2,"Step19: Verify 'Product,Category' appears in filter pane")        
        
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterWindow']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('2', '[All]',verify=True, verify_type=True,msg="Step20: Verify All checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step20: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step20: Verify Web checked in prompt")
        
        """
        Step21: Enable "Computers" checkbox.
        Step22: Verify only "Computers" product is displayed.
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=True, verify_type=True,msg="Step22: Verify Computers checked in prompt")
                
        time.sleep(3)
        expected_xval_list=['Computers']
        time.sleep(2)
        expected_yval_list=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step22.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step22: Verify Column header")
        time.sleep(2)   
        bar=['Store Type:Store Front', 'Product Category:Computers', 'Gross Profit:$21,984,070.23', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step22: Verify bar value")
        time.sleep(5)
        
        """
        Step23: Enable "Video Production" checkbox.
        Step24: Verify the following chart is displayed.
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('2', 'Video Production',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Video Production',verify=True, verify_type=True,msg="Step24: Verify Video Production checked in prompt")
                
        time.sleep(3)
        expected_xval_list=['Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','4M','8M','12M','16M','20M','24M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,4, 'Step24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step24.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step24: Verify Column header")
           
        bar=['Store Type:Store Front', 'Product Category:Computers', 'Gross Profit:$21,984,070.23', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step24: Verify bar value")
        time.sleep(5)
        
        """
        Step25: Enable "Camcorder" check box.
        Step26: Verify the following chart is displayed.
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('2', 'Camcorder',verify=False,scroll_down=True)
        propertyobj.select_or_verify_show_prompt_item('2', 'Camcorder',verify=True, verify_type=True,msg="Step26: Verify Camcorder checked in prompt")
                
        time.sleep(3)
        expected_xval_list=['Camcorder','Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M','35M','40M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step26:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,6, 'Step26.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step26.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step26: Verify Column header")
           
        bar=['Store Type:Store Front', 'Product Category:Camcorder', 'Gross Profit:$34,471,375.27', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step26: Verify bar value")
        time.sleep(5)
        
        time.sleep(10)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227720_Actual_step26', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
       
        """
        Step27: Click Save as "C2158200" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                   
        """
        Step28: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()