'''
Created on May04, 2016
@author: Sindhuja

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/8404&group_by=cases:section_id&group_id=146864&group_order=asc
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2109132
TestCase Name : IA-4252:BUE: Filter Down/remove filter doesn't restore the chart to its original state
'''
__author__ = "Sindhuja"
__copyright__ = "IBI"

import unittest
import time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_run, metadata
from common.locators import visualization_resultarea_locators
from common.lib import utillity

class C2109132_TestClass(BaseTestCase):

    def test_C2109132(self):
        
        Test_Case_ID = 'C2109132'
        driver = self.driver #Driver reference object created
        '''Step 01. Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=retail_samples/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8404%2F'''
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10099_5', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        '''Step 02. Double click "Store Name" & "Sale Unit(s)".'''
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        metaobj.datatree_field_click('Dimensions->Store->Store->Store Name', 2, 2)
        time.sleep(5)
        metaobj.datatree_field_click('Sale Unit(s)', 2, 1)
        time.sleep(12)

        '''Step 03. Verify labels.
        Expected:
        first two riser values - Amsterdam:63,174 and Anchorage:13,448
        last two riser values - Wichita:9,984 and Zurich:30,604'''
        parent_css="#MAINTABLE_wbody1 svg g text[class='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 87, 'Step03: Verify the total number of risers displayed on liver preview Chart')
        expected_xval_list=['Amsterdam', 'Anchorage', 'Arlington', 'Athens', 'Atlanta', 'Bangalore', 'Bangkok', 'Barcelona', 'Beijing', 'Belfast', 'Berlin']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K', '800K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 03b: X annd Y axis Scales Values has changed or NOT')
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c(i) Verify first bar color")
        xaxis_value="Store Name"
        yaxis_value="Sale Unit(s)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 03:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 03:d(ii) Verify Y-Axis Title")
        time.sleep(8)
        
        '''Step 04. Verify first and last two bar riser values'''
        
        time.sleep(1)
        bar_riser=['Store Name:Amsterdam', 'Sale Unit(s):63,174', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_riser, "Step 04: Verify tooltip values")

        '''Step 05. Drag "Store,Business,Region" to color bucket'''
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(8)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region', 1, 'Color', 0)
        time.sleep(6)


        '''Step 06. Verify Legend (store business region) values'''
        parent_css="#MAINTABLE_wbody1 svg g text[class^='legend-labels']"
        resultobj.wait_for_property(parent_css, 4)
        color_val=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("MAINTABLE_wbody1",color_val, 'Step 06. Verify Legend Values')
        time.sleep(10)
        expected_xval_list=['Amsterdam', 'Anchorage', 'Arlington', 'Athens', 'Atlanta', 'Bangalore', 'Bangkok', 'Barcelona', 'Beijing', 'Belfast', 'Berlin']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K', '800K']
        
        
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 06: X annd Y axis Scales Values has changed or NOT')
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 06.c(i) Verify first bar color")
        xaxis_value="Store Name"
        yaxis_value="Sale Unit(s)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 06:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 06:d(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 87, 'Step06: Verify the total number of risers displayed on liver preview Chart')
        time.sleep(8)
        
        '''Step 07. Verify query pane'''
        
        metaobj.verify_query_pane_field('Horizontal Axis','Store Name',1,'Step 07. Verify query pane')
        
        '''Step 08: Click run in the toolbar'''
        
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_window(1)            # to switch to run window
        
        
        '''Step 09: Hover over a bar value (store name:Dayton), select drill down on region.'''
        
        parent_css="#MAINTABLE_wbody1 svg g text[class^='legend-labels']"
        elem1=(By.CSS_SELECTOR, parent_css)
        resultobj._validate_page(elem1)
        resultobj.wait_for_property(parent_css, 4)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 87, 'Step 09: Verify the total number of risers displayed on Run Chart')
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s1!g23!mbar', 'Drill down to Store Business Sub Region')
        
        '''Step 10: Verify tooltip values'''
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 10:a: Verify the total number of risers displayed on Run Chart')
        bar_riser_runtime = ['Store Name:Dayton', 'Sale Unit(s):10,700', 'Store Business Sub Region:Midwest', 'Remove Filter', 'Drill up to', 'Drill down to Store Country']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar_riser_runtime, "Step 10:b: Verify tooltip values", x_offset=0, y_offset=-7)
        xaxis_value="Store Name"
        yaxis_value="Sale Unit(s)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:c(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:c(ii) Verify Y-Axis Title")
        expected_xval_list=['Dayton']
        expected_yval_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 
                                               'Step 10:d: X annd Y axis Scales Values has changed or NOT')
        
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.e(i) Verify first bar color")
        time.sleep(5)
        
        '''Step 11: Remove filter via the arrow icon on bottom right'''
        
        runobj.select_run_menu_option("MAINTABLE_menuContainer1", "remove_filter")
        time.sleep(5)
        
        '''Step 12: Verify first and last 2 bar riser values & Step 13: Verify output''' 
        
        raiser="[id^='MAINTABLE_1'] [class*='riser!s5!g0!mbar']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 87)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 87, 'Step 12: Verify the total number of risers displayed on Run Chart')
        bar_riser_runtime1 = ['Store Name:Amsterdam', 'Sale Unit(s):63,174', 'Store Business Sub Region:Europe', 'Filter Chart', 'Exclude from Chart', 'Drill up to', 'Drill down to Store Country']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s5!g0!mbar", bar_riser_runtime1, "Step 12:a: Verify tooltip values")
        expected_xval_list=['Amsterdam', 'Anchorage', 'Arlington', 'Athens', 'Atlanta', 'Bangalore', 'Bangkok', 'Barcelona', 'Beijing', 'Belfast', 'Berlin']
        expected_yval_list=['0', '100K', '200K', '300K', '400K', '500K', '600K', '700K', '800K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 12:b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s5!g0!mbar", "orange", "Step 12.c(i) Verify first bar color")
        xaxis_value="Store Name"
        yaxis_value="Sale Unit(s)"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:d(ii) Verify Y-Axis Title")
        time.sleep(10)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2109132_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''Step 14: Close the output window'''
        
        self.driver.close()
        time.sleep(7)
        utillobj.switch_to_window(0)            # switch back to main window
        
        '''Step 15: Click "Save" in the toolbar > Type C2109132 > Click "Save" in the Save As dialog'''
        
        time.sleep(6)
        ribbonobj.select_top_toolbar_item("toolbar_save")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
        
        
        

