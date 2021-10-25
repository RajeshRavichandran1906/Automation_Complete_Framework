"""
Created on Jun 27, 2016

@author: Sindhuja
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2140687
TestCase Name : IA-4375:selecting a value with "&" in filter prompt is not reflecting in canvas.
"""

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators

class C2140687_TestClass(BaseTestCase):

    def test_C2140687(self):
        driver = self.driver #Driver reference object created
        """
         TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2140687'
        """
        Step 01: Launch the IA API with EMPDATA http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/EMPDATA&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F

        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','ibisamp/empdata','P312/S10099_5', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Add fields DEPT, SALARY.
        """
        metaobj.datatree_field_click("DEPT", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 8)
        
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 03: Verify label values
        """
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 8, 'Step 03a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['ACCOUNTING', 'ADMIN SERVICES', 'CONSULTING', 'CUSTOMER SUPPORT', 'MARKETING', 'PERSONNEL', 'PROGRAMMING & DVLPMT', 'SALES']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        time.sleep(5)
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="DEPT"
        yaxis_value="SALARY"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        
        """
        Step 04: Verify query pane
        """
        metaobj.verify_query_pane_field("Horizontal Axis", "DEPT", 1, "Step 04a: Verify query pane - DEPT- Horizontal Axis")
        metaobj.verify_query_pane_field('Vertical Axis', "SALARY", 1, "Step 04b: Verify query pane - SALARY- Vertical Axis")
        time.sleep(10)
        
        """
        Step 05: Verify all bar riser values (DEPT:SALARY)
        """
        expected_tooltip=['DEPT:ACCOUNTING','SALARY:$283,300.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 05.a: Verify bar riser values (DEPT:SALARY)")
        
        """
        Step 06: Drag/drop DEPT to Filter pane, uncheck "All", then select values ACCOUNTING, CONSULTING, click ok.
        """
        time.sleep(5)
        metaobj.datatree_field_click("DEPT", 1, 1,"Filter")
        time.sleep(5)
        l=['[All]','ACCOUNTING','CONSULTING']
        loc=("#alphaFieldPanel #avAlphaOperatorComboBox div[id^='BiButton']")
        elem1=(By.CSS_SELECTOR, loc)
        resultobj._validate_page(elem1)
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(10)
        
        """
        Step 07: Verify filtered (accounting and consulting) DEPT:SALARY values
        """
        prompt_css = "div[id*='Prompt_1'] table[style*=hidden] tr"
        elem1=(By.CSS_SELECTOR, prompt_css)
        resultobj._validate_page(elem1)
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=False, msg='Step 07a(i): verify the ALL is unchecked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'ACCOUNTING', True, verify_type=True, msg='Step 07a(ii): verify the ACCOUNTING is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'CONSULTING', True, verify_type=True, msg='Step 07a(iii): verify the CONSULTING is checked under Show prompt')
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07b: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ACCOUNTING', 'CONSULTING']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07c: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 07d(i): Verify first bar color")
        xaxis_value="DEPT"
        yaxis_value="SALARY"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07e(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07e(ii) Verify Y-Axis Title")
        expected_tooltip=['DEPT:CONSULTING','SALARY:$126,300.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g1!mbar",expected_tooltip, "Step 07f: verify the default tooltip values")
        time.sleep(3)
        resultobj._validate_page(elem1)
        
        """
        Step 08: Select value PROGRAMMING & DVLPMT in the Filter Prompt
        """
        propertyobj.select_or_verify_show_prompt_item(1, "PROGRAMMING & DVLPMT")
        propertyobj.select_or_verify_show_prompt_item(1,'[All]', True, verify_type=False, msg='Step 08a(i): verify the ALL is unchecked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'ACCOUNTING', True, verify_type=True, msg='Step 08a(ii): verify the ACCOUNTING is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'CONSULTING', True, verify_type=True, msg='Step 08a(iii): verify the CONSULTING is checked under Show prompt')
        propertyobj.select_or_verify_show_prompt_item(1,'PROGRAMMING & DVLPMT', True, verify_type=True, msg='Step 08a(iv): verify the PROGRAMMING & DVLPMT is checked under Show prompt')
        time.sleep(15)
        
        """
        Step 09: Verify chart values in preview
        """
        time.sleep(4)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 09a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['ACCOUNTING', 'CONSULTING', 'PROGRAMMING & DVLPMT']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 09b: X annd Y axis Scales Values has changed or NOT')
        expected_tooltip=['DEPT:PROGRAMMING & DVLPMT','SALARY:$182,300.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mbar",expected_tooltip, "Step 09c: verify the default tooltip values")
         
        """
        Step 10 : Click Run in the toolbar
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        
        """
        Step 11: Verify output
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        time.sleep(8)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 11a: Verify the total number of risers displayed on Run Chart')
        x_val_list=['ACCOUNTING', 'CONSULTING', 'PROGRAMMING & DVLPMT']
        y_val_list=['0', '50K', '100K', '150K', '200K', '250K', '300K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_val_list, y_val_list, 'Step 11b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g1!mbar!", "bar_blue", "Step 11c(i): Verify first bar color")
        xaxis_value="DEPT"
        yaxis_value="SALARY"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11d(ii) Verify Y-Axis Title")
        expected_tooltip=['DEPT:PROGRAMMING & DVLPMT','SALARY:$182,300.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mbar",expected_tooltip, "Step 11e: verify the default tooltip values")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2140687_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Close the output window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 13: Click "Save" in the toolbar > Type C2140687 > Click "Save" in the Save As dialog
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()
        
        
    