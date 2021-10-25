'''
Created on Nov 14, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229098
TestCase Name = Verify Show Data  
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229098_TestClass(BaseTestCase):

    def test_C2229098(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229098'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
          
        """
        Step 02: Click "Change" dropdown > "ESRI Bubble"
        """
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)

        """
        Step 03: Right click "Store,State,Province" > "Map As" > "US State (Name)"
        """
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)  
        metaobj.datatree_field_click('Store,State,Province',1, 1, 'Map As', 'US State (Name)')
        time.sleep(6)
        
        """
        Step 04: Double click "Store,State,Province", "Revenue"
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 51)
        
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 36, 'Step 04.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mmarker!", "bar_blue", "Step 04.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '164M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 04:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mmarker!",expected_tooltip, "Step 04.e: verify the default tooltip values")       
        
        """
        Step 05: Click the Show data menu dropdown
        Step 06: Click "Show Data"
        """
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step05: Verify Show data menu')
        
        """
        Step 07: Verify an Active Report is launched in a new window
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
#         iarunobj.create_table_data_set("table#ITableData0", "C2229098_1.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2229098_1.xlsx", "Step 07: Verify data set")

        """
        Step 08: Dismiss the report window
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
        Step 09: Click the Show data menu dropdown
        Step 10: Click "Show Data with Related Columns"
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data with Related Columns', verify='true', expected_popup_list=['Show Data','Show Data with Related Columns','Export Data'],msg='Step09: Verify component menu')
         
        """
        Step 11: Verify an Active Report is launched in a new window
        """
        time.sleep(15)
        utillobj.switch_to_window(1, window_title="WebFOCUS Active Report")
        time.sleep(15) 
        chart_type_css="table[id^='ITableData0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
#         iarunobj.create_table_data_set("table#ITableData0", "C2229098_2.xlsx")
        iarunobj.verify_table_data_set("table#ITableData0", "C2229098_2.xlsx", "Step 11: Verify data set")
        
        """
        Step 12: Dismiss the report window
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
        Step 13: Click "Save" icon
        Step 14: Enter Title "C2229098"
        Step 15: Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(4)
        
        """
        Step 16: Dismiss IA window
        """
        
if __name__ == '__main__':
    unittest.main()