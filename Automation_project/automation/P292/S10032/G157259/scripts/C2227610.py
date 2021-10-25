'''
Created on Jun'01, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227610
'''
import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227610_TestClass(BaseTestCase):
    def test_C2227610(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227610'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass') 
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
             
        """
        Step02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(3)        
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)      
              
        """
        Step03: Double click "Store,Country", "Revenue"
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(5) 
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(8)
         
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
         
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        utillobj.synchronize_with_number_of_element(".colorScaleLegend-title", 1, 30)
          
        """
        Step04: Hover over United States > Verify menu
        """
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step04.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step04:d(i) Verify legend Title")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g19!mregion']")
        utillobj.click_on_screen(parent_elem, 'top_middle',javascript_marker_enable=True,mouse_duration=2.5,x_offset=0, y_offset=-15)
        time.sleep(2)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g19!mregion",expected_tooltip, "Step04.e: verify the default tooltip values",default_move=True)       
         
        """
        Step05: Select "Filter Chart"
        Step06: Verify Preview
        """ 
        utillobj.synchronize_with_number_of_element(".colorScaleLegend-title", 1, 30)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(move1, 'bottom_middle')
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g19!mregion']")
        utillobj.click_on_screen(parent_elem, 'top_middle',javascript_marker_enable=True,mouse_duration=3,x_offset=0, y_offset=-15)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g19!mregion",'Filter Chart',wait_time=1,default_move=True)
             
        parent_css2="[class*='riser!s0!g0!mregion']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step06.a: Verify number of risers displayed', custom_css="[class^='riser!s0!g0!mregion']")
        time.sleep(6)
        legend_css = "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(legend_css,6)
        legend=['Revenue', '545,792,165.4', '545,792,165.9', '545,792,166.4', '545,792,166.9', '545,792,167.4']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step06.e: verify the default tooltip values",default_move=True)       
             
        """
        Step07: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
                  
        """
        Step08: Hover over Alaska > Verify menu
        """
        parent_css2="[class*='riser!s0!g0!mregion']"
        resultobj.wait_for_property(parent_css2,1)
             
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step08.a: Verify number of risers displayed', custom_css="[class^='riser!s0!g0!mregion']")
        time.sleep(2)
        legend=['Revenue', '545,792,165.4', '545,792,165.9', '545,792,166.4', '545,792,166.9', '545,792,167.4']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step08.e: verify the default tooltip values",default_move=True)       
             
        """
        Step09: Close the output window
        Step10: Click "Save" icon > "C2227610" > click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
             
        """
        Step11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
             
        """
        Step12: Reopen fex using IA API:
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2227610.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
              
        """
        Step13: Verify canvas
        """
        parent_css2="[class*='riser!s0!g0!mregion']"
        resultobj.wait_for_property(parent_css2,1)
             
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step13.a: Verify number of risers displayed', custom_css="[class^='riser!s0!g0!mregion']")
        time.sleep(2)
        legend=['Revenue', '545,792,165.4', '545,792,165.9', '545,792,166.4', '545,792,166.9', '545,792,167.4']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step13.e: verify the default tooltip values",default_move=True)       
        time.sleep(2)
          
        """
        Step14: Right-click "Store,Country" in the Filter pane > Delete
        """
        metaobj.filter_tree_field_click('Store,Country', 1, 1,'Delete')
         
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step14.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g2!mregion']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5)
        time.sleep(1)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion",expected_tooltip, "Step14.e: verify the default tooltip values",default_move=True)       
         
        """
        Step15:Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        """
        STep16: Verify Output
        Step17: Hover over Brazil > Verify menu
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",33, 'Step17.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g2!mregion']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5)
        time.sleep(1)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion",expected_tooltip, "Step17.e: verify the default tooltip values",default_move=True)       
         
        """
        Step18: Select "Filter Chart" > Verify output
        """
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(move1, 'bottom_middle')
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g2!mregion']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=3)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g2!mregion",'Filter Chart',wait_time=1,default_move=True)
         
        parent_css2="[class*='riser!s0!g0!mregion']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step18.a: Verify number of risers displayed', custom_css="[class^='riser!s0!g0!mregion']")
        time.sleep(2)
        legend=['Revenue', '25,974,010.8', '25,974,011.3', '25,974,011.8', '25,974,012.3', '25,974,012.8']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18:d(i) Verify legend Title")
        time.sleep(5)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Brazil', 'Revenue:$25,974,011.78', 'Remove Filter', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step18.e: verify the default tooltip values",default_move=True)       
                 
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227610_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """
        Step19: Close the output window
        Step20: Logout
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        
if __name__ == '__main__':
    unittest.main()

