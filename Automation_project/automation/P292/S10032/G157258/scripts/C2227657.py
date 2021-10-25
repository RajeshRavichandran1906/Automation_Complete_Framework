'''
Created on Mar 24, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227657
Test case Name =  Edit Title  
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227657_TestClass(BaseTestCase):

    def test_C2227657(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227657'
        Medium_wait_time=45
        small_wait_time=30
        
        
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
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9,Medium_wait_time)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7,Medium_wait_time)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1,Medium_wait_time)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
#         metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        metaobj.create_visualization_filters("alpha")        
        time.sleep(6)
        
        """
        Step 06: Click Prompt menu in the upper right corner
        Step 07: Select "Edit Title..."
        Step 08: Change Title to "Product" > Click OK
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1,Medium_wait_time)
        propertyobj.select_or_verify_prompt_options("1", edit_title = True, old_prompt_title = "Product,Category", new_prompt_title = "Product", msg = 'Step 08')
        
        """
        Step 09: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7,Medium_wait_time)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7,Medium_wait_time)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09: Verify bar value")
        time.sleep(5)
        
        
        """
        Step 10: Click Prompt menu in the upper right corner
        Step 11: Select "Edit Title..."
        Step 12: Verify dialog > Click Cancel
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1,small_wait_time)
        propertyobj.select_or_verify_prompt_options("1", edit_title = True, old_prompt_title = "Product", msg = 'Step 12')
        
        
        """
        Step 13: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        """
        Step 14: Verify output
        """
        raiser="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 14: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227657_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1) 
        
        """
        Step 15: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 16: Click Save in the toolbar > Save as "C2227657" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 18: Reopen fex using IA API: http://machine:port/alias/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227657.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """
        Step 19: Verify Canvas
        """
        raiser="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7,Medium_wait_time)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7,Medium_wait_time)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 19: Verify bar value")
        time.sleep(5)
        
        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()

