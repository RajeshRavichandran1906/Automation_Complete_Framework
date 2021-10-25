'''
Created on Jun 23, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227730
TestCase Name = Dynamic Grouping with Chart
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, metadata
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227730_TestClass(BaseTestCase):

    def test_C2227730(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227730'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: In Data pane, right mouse click on "Customer,Business,Region" > "Create Group...".
        """
        time.sleep(6)
        metaobj.datatree_field_click("Customer,Business,Region", 1, 1,"Create Group...")
        time.sleep(6)
        
        """
        Step03: In Field name box, change it to "AMERICA_REGIONS".
        Step04: Multi-select "North America","South America".
        Step05: Click "Group" button and rename it to "America".
        """
        elem=(By.CSS_SELECTOR,"div[id^='QbDialog'][tabindex='0'] #dynaTextFld")
        resultobj._validate_page(elem)
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(2)
        element_list=['North America','South America']
        metaobj.create_ia_group('Group', element_list, change_field_txt='AMERICA_REGIONS')
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(2)
        element_list=['North America and South America']
        metaobj.create_ia_group('Rename', element_list, rename_field='America')
        time.sleep(10)
        
        """
        Step06: Click on "Show Other" button.
        Step07: Verify that the non-group ones have been grouped to "Other".
        Step08: Click "OK" to dismiss "Create a Group" window.
        """
        time.sleep(5)
        expected_element_list=['America', 'North America', 'South America', 'Other', 'EMEA', 'Oceania']
        metaobj.verify_fields_in_ia_groupdialog(expected_element_list, btn_name='Show Other', close_button='ok', msg='Step07: Verify that the non-group ones have been grouped to "Other".')
        time.sleep(8)
        
        """
        Step09: Verify that "AMERICA_REGIONS" is displayed under Dimension/Customer.
        """
        new_metaobj.collapse_data_field_section("Customer")
        metaobj.verify_data_pane_field('Customer',"AMERICA_REGIONS",1,"Step 09")
        time.sleep(2)
        
        """
        Step10: Locate "Customer,State,Province,Population,Range" in Data pane.
        Step11: Right mouse click > "Create Group"
        """
        time.sleep(8)
        metaobj.datatree_field_click('Customer,State,Province,Population,Range', 1, 1,"Create Group...")
        time.sleep(6)
        
        """
        Step12: In Field name box, change it to "4_StatesPopRanges".
        Step13: Select "A: 0 - 100,000" > Click "Group".
        """
        elem=(By.CSS_SELECTOR,"div[id^='QbDialog'][tabindex='0'] #dynaTextFld")
        resultobj._validate_page(elem)
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(2)
        element_list=['A: 0 - 100,000']
        metaobj.create_ia_group('Group', element_list, change_field_txt='4_StatesPopRanges')
        time.sleep(2)
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 10)
        time.sleep(6)
        
        """
        Step14: Select "B: 100,001 - 500,000", "C: 500,001 - 1,000,000" > Click "Group".
        """
        element_list1=['B: 100,001- 500,000','C: 500,001- 1,000,000']
        metaobj.create_ia_group('Group', element_list1, change_field_txt='4_StatesPopRanges')
        time.sleep(2)
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 11)
        time.sleep(6)
        
        """
        Step15: Select "D: 1,000,001 - 5,000,000", "E: 5,000,001 - 10,000,000" and "F: 10,000,001 -20,000,000" > Click "Group".
        """
        element_list2=['D: 1,000,001- 5,000,000','E: 5,000,001-10,000,000','F: 10,000,001-20,000,000']
        metaobj.create_ia_group('Group', element_list2, change_field_txt='4_StatesPopRanges')
        parent_css="div[id^='QbDialog'] [class*='active'] #dynaGrpsValuesTree[class*='tree'] table tr td[class='']"
        resultobj.wait_for_property(parent_css, 12)
        time.sleep(6)
        
        """
        Step16: Verify it created the groups as shown.
        Step17: Click "OK" to dismiss "Create a Group" window.
        """
        time.sleep(5)
        expected_element_list=['A: 0 - 100,000', 'A: 0 - 100,000', 'B: 100,001- 500,000 and C: 500,001- 1,000,000', 'B: 100,001- 500,000', 'C: 500,001- 1,000,000', 'D: 1,000,001- 5,000,000 and E: 5,000,001-10,000,000 and F: 10,000,001-20,000,000', 'D: 1,000,001- 5,000,000', 'E: 5,000,001-10,000,000', 'F: 10,000,001-20,000,000', 'G: 20,000,001-30,000,000', 'H: 30,000,001 - 40,000,000', 'MISSING']
        metaobj.verify_fields_in_ia_groupdialog(expected_element_list, close_button='ok', msg='Step16: Verify it created the groups as shown')
        
        """
        Step18: Verify that "4_StatesPopRanges" are displayed under "AMERICA_REGIONS" in Data Pane.
        """
        time.sleep(8)
        metaobj.verify_data_pane_field('AMERICA_REGIONS',"4_StatesPopRanges",1,"Step 18")
        
        """
        Step19: Drag "AMERICA_REGIONS" to Matrix - Rows.
        """
        time.sleep(8)
        metaobj.drag_drop_data_tree_items_to_query_tree('Dimensions->AMERICA_REGIONS', 1, 'Rows', 0)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        
        """
        Step20: Drag "4_StatesPopRanges" to Horizontal Axis.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree("Dimensions->4_StatesPopRanges", 1, 'Horizontal Axis', 0)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='rowLabel!']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        
        """
        Step21: Drag "Quantity,Sold" to Vertical Axis.
        """
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree("Quantity,Sold", 1, 'Vertical Axis', 0)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 12)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step22: Verify the following chart is displayed.
        """
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 12)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(2)
        xaxis_value="4_StatesPopRanges"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step22(i) Verify X-Axis Title")
        yaxis_value="Quantity Sold"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step22(ii) Verify X-Axis Title")
        expected_xval_list=['', 'A: 0 - 100,000', 'B: 100,001- 500,000 and...', 'D: 1,000,001- 5,000,000...', 'G: 20,000,001-30,000,000', 'H: 30,000,001 - 40,000,0...']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step22(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step22: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step22: Verify first bar color")
        time.sleep(5)
        expected=['America','Other']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','AMERICA_REGIONS', expected,"Step22: Verify Row header")
        time.sleep(3)
        bar=['AMERICA_REGIONS:Other', '4_StatesPopRanges:', 'Quantity Sold:1,869,259', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Region']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", bar, "Step22: Verify bar value")
        time.sleep(5)
        
        """
        Step23: Click "Run".
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(15)  
        
        """
        Step24: Verify output
        """ 
        chart_type_css="rect[class*='riser!s0!g0!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 12)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(2)
        xaxis_value="4_StatesPopRanges"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step24(i) Verify X-Axis Title")
        yaxis_value="Quantity Sold"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step24(ii) Verify X-Axis Title")
        expected_xval_list=['', 'A: 0 - 100,000', 'B: 100,001- 500,000 and...', 'D: 1,000,001- 5,000,000...', 'G: 20,000,001-30,000,000', 'H: 30,000,001 - 40,000,0...']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step24(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step24: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step24: Verify first bar color")
        time.sleep(5)
        expected=['America','Other']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','AMERICA_REGIONS', expected,"Step24: Verify Row header")
        time.sleep(3)
        bar=['AMERICA_REGIONS:Other', '4_StatesPopRanges:', 'Quantity Sold:1,869,259', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Region']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", bar, "Step24: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227730_Actual_step24', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step25: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
      
        """
        Step26: Click "IA" > "Save" > "C2160099" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                  
        """
        Step27: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step28: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158180.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                 
        """
        Step29: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar!r1!c0!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 12)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='rowHeader-label!']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(2)
        xaxis_value="4_StatesPopRanges"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step29(i) Verify X-Axis Title")
        yaxis_value="Quantity Sold"
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step29(ii) Verify X-Axis Title")
        expected_xval_list=['', 'A: 0 - 100,000', 'B: 100,001- 500,000 and...', 'D: 1,000,001- 5,000,000...', 'G: 20,000,001-30,000,000', 'H: 30,000,001 - 40,000,0...']
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step29(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step29: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", "bar_blue", "Step29: Verify first bar color")
        time.sleep(5)
        expected=['America','Other']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','AMERICA_REGIONS', expected,"Step29: Verify Row header")
        time.sleep(3)
        bar=['AMERICA_REGIONS:Other', '4_StatesPopRanges:', 'Quantity Sold:1,869,259', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Region']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r1!c0!", bar, "Step29: Verify bar value")
        time.sleep(5)
        
        """
        Step30: Logout
        """
        
if __name__ == '__main__':
    unittest.main()