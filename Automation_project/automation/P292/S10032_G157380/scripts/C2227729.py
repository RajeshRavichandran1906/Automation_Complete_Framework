'''
Created on Jun 21, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227729
TestCase Name = Preview component menu
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties, ia_run, active_miscelaneous
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227729_TestClass(BaseTestCase):

    def test_C2227729(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227729'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double click "Cost of Goods" and "Product,Category".
        """
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(2)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step02:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step02:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step02.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!", "bar_blue", "Step02.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!", bar,"Step02: Verify bar value")
        time.sleep(5) 
        
        """
        Step03: Drag "Product,Category" to Filter pane.
        """
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        time.sleep(2)
        
        """
        Step 04: Click "All" to clear all checkboxes.
        Step 05: Select "Camcorder","Computers" in the filter window.
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        l=['[All]','Camcorder','Computers']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(5)
        
        """
        Step 07: Verify the following chart is displayed.
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Computers']
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step07: Verify bar value")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, 'Camcorder', verify=True, verify_type=True, msg="Step07.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, 'Computers', verify=True, verify_type=True, msg="Step07.2: Verify values is checked in filter prompt")
        time.sleep(5)
        
        """
        Step08: Select "Show Data" menu in the upper right corner
        """
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step08: Verify component menu')
         
        """
        Step09: Verify only the filtered values are displayed in the Active output
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '2of2records,Page1of1', "Step 09.a: Verify Page Summary")
        time.sleep(2)
#         iarunobj.create_table_data_set("table#ITableData0", "C2227729_1.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2227729_1.xlsx", "Step 09.b: Verify data set")
        
        """
        Step10: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """
        Step11: Select "Show Data with Related Columns" menu in the upper right corner
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data with Related Columns', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step11: Verify component menu')
         
        """
        Step12: Verify output with all Columns from Product hierarchy and Sales Measures (data for Camcorder and Computers only)
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        miscelanousobj.verify_page_summary(0, '35of35records,Page1of1', "Step 12.a: Verify Page Summary")
        time.sleep(2)
#         iarunobj.create_table_data_set("table#ITableData0", "C2227729_2.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2227729_2.xlsx", "Step 12.b: Verify data set")
        
        """
        Step13: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """
        Step 14: Hover over "Camcorder" and select "Drill Down to Product Subcategory".
        """
        time.sleep(3)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(3)        
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g0!mbar!", "Drill down to Product Subcategory")
        time.sleep(5)
        
        """
        Step 15: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step15:")
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step15:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Handheld', 'Professional', 'Standard']
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar!", "bar_blue", "Step15.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Standard', 'Cost of Goods:$49,071,633.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar!", bar,"Step15: Verify bar value")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, 'Camcorder', verify=True, verify_type=True, msg="Step15.1: Verify values is checked in filter prompt")
        time.sleep(5)
        
        
        """
        Step16: Select "Show Data" menu in the upper right corner
        """
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step16: Verify component menu')
         
        """
        Step17: Verify output
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        miscelanousobj.verify_page_summary(0, '3of3records,Page1of1', "Step 17.a: Verify Page Summary")
        time.sleep(2)
#         iarunobj.create_table_data_set("table#ITableData0", "C2227729_3.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2227729_3.xlsx", "Step 17.b: Verify data set")
        
        """
        Step18: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """
        Step19: Select "Show Data with Related Columns" menu in the upper right corner
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data with Related Columns', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step19: Verify component menu')
         
        """
        Step20: Verify output
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        miscelanousobj.verify_page_summary(0, '15of15records,Page1of1', "Step 20.a: Verify Page Summary")
        time.sleep(2)
#         iarunobj.create_table_data_set("table#ITableData0", "C2227729_4.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2227729_4.xlsx", "Step 20.b: Verify data set")
        
        """
        Step21: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()