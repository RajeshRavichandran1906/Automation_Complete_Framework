'''
Created on Apr 4, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227687
Test case Name =  Filter pane context menu - Delete
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators import visualization_resultarea_locators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class C2227687_TestClass(BaseTestCase):

    def test_C2227687(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227687'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double-click "Revenue Per,Sq. Ft." and "Sale Unit(s)" located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue Per,Sq. Ft.",2,1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Sale Unit(s)",2,1) 
         
        """
        Step 03: Expand Dimension "Sales_Related" > "Transaction Date,Simple" > Double-click "Sale,Quarter"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Quarter", 2, 1)
         
        """
        Step 04: Drag and drop "Sale,Year" to the Filter pane
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css,4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels'"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.drag_drop_data_tree_items_to_filter("Sale,Year", 1)
         
        """
        Step 05: Change "From" value to 2015
        Step 06: Click OK
        """
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric', ['From','2015'])
        time.sleep(2)
        
        """
        Step 07: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step07:")
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        expected_xval_list=['1', '2', '3', '4']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K','600K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 4, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Sale Unit(s):413,800', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar", bar, "Step 07.d: Verify bar value")
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
#         propertyobj.verify_slider_range_filter_prompts(1, [2015, 2017], "Step07: Verify filter prompt range values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2015,'int',msg="Step07: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step07: Verify filter prompt range max values")
        time.sleep(2)
        
        """
        Step 08: Right click "Sale,Year" filter in the Filter pane > Verify menu
        Step 09: Select Delete
        """
        metaobj.filter_tree_field_click('Sale,Year',1,1)
        utillobj.select_or_verify_bipop_menu('Delete',verify='true',expected_popup_list=['Edit...', 'Hide Prompt', 'Delete'],msg='Step 08: Right click "Sale,Year" filter in the Filter pane')
        time.sleep(6)
        
        """
        Step 10: Verify Filter is removed from Filter pane
        """
        metaobj.verify_filter_pane_field('Sale,Year',1,'Step:10 Verify Filter is removed from Filter pane', expected_len = 0)
        
        """
        Step 11: Verify Filter is removed from canvas and preview is refreshed
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        try:
            if self.driver.find_element_by_css_selector("div[id^='BoxLayoutFilterBox']").is_displayed():
                utillity.UtillityMethods.asequal(self, 'a', 'b', "Step 11: Verify Filter Prompts not removed from canvas")
        except NoSuchElementException:
            utillity.UtillityMethods.asequal(self, 'a', 'a', "Step 11: Verify Filter Prompts are removed from canvas")
        time.sleep(5)
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        expected_xval_list=['1', '2', '3', '4']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 4, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Sale Unit(s):602,077', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s1!g0!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227687_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Click Save in the toolbar
        Step 13: Save as "C2108489" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()