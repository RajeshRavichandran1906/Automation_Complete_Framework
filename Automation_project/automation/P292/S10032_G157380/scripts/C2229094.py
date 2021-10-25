'''
Created on Nov 13, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229094
TestCase Name = Verify Map with Define and Compute in Visualization 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, define_compute, wf_map
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229094_TestClass(BaseTestCase):

    def test_C2229094(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229094'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
          
        """
        Step 02: Click "Change" dropdown > select ESRI Proportional (Bubble) map
        """
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
        
        """ 
        Step 03. Click "Calculation" dropdown > "Detail (Define)
        Step 04. Enter "Countries" in Field;
        Set "Format" = "A40V';
        Double click "Store,Country"
        """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Detail (Define)')
        elem=(By.CSS_SELECTOR,'#fldCreatorCancelBtn')
        resultobj._validate_page(elem)
        calculate_obj.enter_define_compute_parameter("Countries", "A40V", "Store,Country", 1)
        time.sleep(5)
        expected_field_value = '"Store,Country"'
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value").strip()
        utillobj.asequal(expected_field_value, actual_field_value, "Step 04: Verify the define field value")
        print(expected_field_value)
        print(actual_field_value)
        
        """    
        Step 05. Click "OK".   
        """
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """
        Step 06: Double click "Countries"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Countries', 2, 1)
        
        """ 
        Step 07. Select "Country" from Geographic Role dropdown
        Step 08. Set "Stored As" = "Name" > OK
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#geoRoleCancelBtn')
        resultobj._validate_page(elem)
        wfmapobj.set_geo_role(role_name='Country', store_as='Name', btn_click='Ok')
        time.sleep(3)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        
        """ 
        Step 09. Click "Calculation" > "Summary (Compute)"
        """
        ribbonobj.select_ribbon_item('Home','calculation',opt='Summary (Compute)')
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#fldCreatorCancelBtn')
        resultobj._validate_page(elem)
        
        """  
        Step 10. Double click "Revenue" > OK
        """
        calculate_obj.enter_define_compute_parameter("Compute_1", "D12.2", "Revenue", 1)
        time.sleep(5)
        expected_field_value = '"Revenue"'
        actual_field_value = self.driver.find_element_by_id("ftext").get_attribute("value").strip()
        utillobj.asequal(expected_field_value, actual_field_value, "Step 10: Verify the Compute field value")
        print(expected_field_value)
        print(actual_field_value)
        calculate_obj.close_define_compute_dialog("ok")
        
        """
        Step 11: Verify the map is updated
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_query_pane_field('Layer', 'Countries', 1, "Step11.a(i): Verify query pane Car under the Horizontal axis bucket")
        metaobj.verify_query_pane_field('Size', 'Compute_1', 1, "Step11.a(ii): Verify query pane Country under the Horizontal axis bucket")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step 11.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 11.c(i) Verify first bar color")
        legend=['Compute_1', 'Compute_1', '545.8M', '273M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Countries:United States', 'Compute_1:545,792,166.41', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g33!mmarker!",expected_tooltip, "Step 11.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 12: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 13: Verify the map is run in a new window
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step 13.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 13.c(i) Verify first bar color")
        legend=['Compute_1', 'Compute_1', '545.8M', '273M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:d(i) Verify legend Title")
        time.sleep(5)
        
        """
        Step 14: Hover over US bubble
        Step 15: Verify the tooltip is displayed correctly
        """
        expected_tooltip=['Countries:United States', 'Compute_1:545,792,166.41', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g33!mmarker!",expected_tooltip, "Step 15: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229094_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 16: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 17: Click "Save" icon
        Step 18: Enter Title "C2229094"
        Step 19: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 20: Reopen fex using IA API: http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2229094.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 21: Verify the map is restored
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_query_pane_field('Layer', 'Countries', 1, "Step21.a(i): Verify query pane Car under the Horizontal axis bucket")
        metaobj.verify_query_pane_field('Size', 'Compute_1', 1, "Step21.a(ii): Verify query pane Country under the Horizontal axis bucket")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step 21.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 21.c(i) Verify first bar color")
        legend=['Compute_1', 'Compute_1', '545.8M', '273M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step21:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Countries:United States', 'Compute_1:545,792,166.41', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g33!mmarker!",expected_tooltip, "Step 21.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 22: Dismiss IA window
        """
                
if __name__ == '__main__':
    unittest.main()