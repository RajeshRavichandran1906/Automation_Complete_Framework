'''
Created on Nov 15, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229095
TestCase Name = Verify Map with Define and Compute in Visualization 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229095_TestClass(BaseTestCase):

    def test_C2229095(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229095'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10028&tool=idis&master=wfretail82/dimensions/wf_retail_geography
        """
        utillobj.infoassist_api_login('idis','new_retail/dimensions/wf_retail_geography','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
        
        """    
        Step02: Click "Join".    
        """
        ribbonobj.select_ribbon_item('Home', 'Join')
        
        """
        step03: Verify the Join dialog    
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#dlgJoin_btnOK img')
        resultobj._validate_page(elem)
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        source_tds=tables[0].find_elements_by_css_selector("td")
        actual_list=[]
        for i in range(5):
            temp=source_tds[i].text.strip()
            actual_list.append(temp)
        print(actual_list)
        expected_list=['ADDRESS_LINE_1', 'ADDRESS_LINE_2', 'BUSINESS_REGION', 'BUSINESS_SUB_REGION', 'CITY_NAME']
        utillobj.asequal(expected_list, actual_list, "Step 03: Verify 'empdata' fields list is showing on the 'Join' window")
        
        """
        step04: Click "Add New"    
        step05: Select new_retail/dimesntions/wf_retail_store.mas > "Open"
        """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_store", new_join=False)
        time.sleep(3)
        
        """
        step06: Drag "ID_GEOGRAPHY" from the first pane to "ID_GEOGRAPHY" in the second pane
        """
        ia_ribbonobj.create_join_link(0, "ID_GEOGRAPHY", 1, "ID_GEOGRAPHY", source_scroll_down=12, target_scroll_down=3)
        time.sleep(3)
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 06a: Verify join created successfully")
        
        """
        step07: Click "Add New"    
        step08: Select new_retail/facts/wf_retail_sales.mas > "Open"
        """
        ia_ribbonobj.create_join("new_retail->facts->wf_retail_sales", new_join=False)
        time.sleep(3)
        
        """
        step09: Drag "ID_STORE" from the second pane to "ID_STORE" in the third pane
        """
        ia_ribbonobj.create_additional_join_link(1, "ID_STORE", 2, "ID_STORE")
        time.sleep(3)
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 09a: Verify join created successfully")
        
        """
        step10:  Click "OK".    
        """
        join_btn=driver.find_element_by_css_selector("#dlgJoin_btnOK img")
        utillobj.default_left_click(object_locator=join_btn)
        time.sleep(5)
        
        """
        Step11: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(3)        
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)   
        
        """
        Step12: Double click "Country", "Revenue"
        """
        metaobj.datatree_field_click("Country", 2, 1)
        time.sleep(4) 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        
        """
        Step13: Verify the map is displayed
        """
        parent_css2="[class*='riser!s0!g0!mregion']"
        resultobj.wait_for_property(parent_css2,1)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step13.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 13.c(i) Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step13.e: verify the default tooltip values",default_move=True)       
         
        """
        Step14: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)  
         
        """
        Step15: Verify the map is run in a new window
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 33) 
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step15.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 15.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step15:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step15.e: verify the default tooltip values",default_move=True)       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229095_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
         
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
        Step 18: Enter Title "C2229095"
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
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step21.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 21.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 21:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step21.e: verify the default tooltip values",default_move=True)       
        
        """
        Step 22: Dismiss IA window
        """
        time.sleep(5) 
               
if __name__ == '__main__':
    unittest.main()