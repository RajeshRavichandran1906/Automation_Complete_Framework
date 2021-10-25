'''
Created on Oct 19, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325620
TestCase Name = Verify Drill Down to Web Page with Choropleth ESRI Map
'''

import unittest, time
from common.wftools import visualization
from selenium.webdriver.common.by import By
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_ribbon

class C2325620_TestClass(BaseTestCase):
    
    def test_C2325620(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2325620'
        
        """
            TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """      
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass') 
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
                
        """
        Step02: Click on the "Change" button in the Home Tab ribbon > Select "Choropleth" ESRI map
        """
        ribbonobj.change_chart_type('choropleth_map')    
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)      
                 
        """
        Step03: Double-click "Revenue" from Sales Measures
        """
        metaobj.datatree_field_click("Revenue", 2,1)
        utillobj.synchronize_with_visble_text('#queryBoxColumn', 'Revenue', 30)
           
        """
        Step04: Double-click "Customer,Country", located under Customer Dimension
        """
        vis_obj.double_click_on_datetree_item('Customer,Country', 1)    
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
           
        """
        Step05: Select "Revenue" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Revenue", 1)
        parent_css="#FieldDrillDown img"
        resultobj.wait_for_property(parent_css, 1)
        ribbon_item=driver.find_element_by_css_selector("#FieldDrillDown img")
        core_utils.left_click(ribbon_item)
            
        """
        Step06: Select "Web Page"
        Step07: Type URL http://www.ibi.com
        Step08: Click "OK"
        """
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        resultobj.wait_for_property(parent_css, 1)
        iaribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com", click_ok=True)
           
        """
        Step09: Hover over United States > Verify pop up menu displays "Drill Down 1"
        """
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        utillobj.synchronize_with_number_of_element(parent_css, 6, 120)
        riser_css="#MAINTABLE_wbody1 [class*='riser!s0!g41!mregion!']"
        utillobj.synchronize_with_number_of_element(riser_css, 1, 120)
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 09.00: Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 09.01: Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',x_offset=10, y_offset=-25)
        expected_tooltip=['Customer Country:United States', 'Revenue:$333,514,945.66', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mregion!",expected_tooltip, "Step 09.02: verify the default tooltip values", default_move=True)
        time.sleep(5)
           
        """
        Step10: Select "Drill Down 1"
        """
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g24!mregion!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        vis_obj.select_tooltip("riser!s0!g24!mregion!", "Drill Down 1", "MAINTABLE_wbody1")
        time.sleep(10)
           
        """
        Step11: Verify Information Builder web page is displayed in a new window (or tab)
        """
        core_utils.switch_to_new_window(current_browser_window_title = 'Business')
        time.sleep(15)
        expected_title='Data and Analytics Company | ibi'
        drill1=(driver.title in expected_title)
        utillobj.asequal(True, drill1, "Step 11.00: Verify Information Builder web page is displayed in a new window (or tab)")
        time.sleep(8)
         
        """
        Step12: Close the output winow
        """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
           
        """
        Step13: Click "Save" in the toolbar > Save As "C2325620" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
            
        """
        Step14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2325655.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2', mrid='mrid', mrpass='mrpass')
        
        """
        Step16: Hover over Mexico > Verify pop up menu displays "Drill Down 1"
        """
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 16.00: Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 16.01: Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',x_offset=10, y_offset=-25)
        expected_tooltip=['Customer Country:United States', 'Revenue:$333,514,945.66', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mregion!",expected_tooltip, "Step 16.02: verify the default tooltip values", default_move=True)
        utillobj.synchronize_with_number_of_element("#topToolBar #runButton img", 1, 30)
        
        """
        Step17: Click "Run" in the toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run') 
        core_utils.switch_to_new_window()               
                  
        """
        Step18: Hover over Canada > Verify pop up menu displays "Drill Down 1"
        """
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 18.00: Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 18.01: Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g5!mregion!']")
        utillobj.click_on_screen(parent_elem, 'middle',x_offset=-10, y_offset=40)
        expected_tooltip=['Customer Country:Canada', 'Revenue:$89,683,027.34', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g5!mregion!",expected_tooltip, "Step 18.02: verify the default tooltip values", default_move=True)
                
        """
        Step19: Select "Drill Down 1" from the pop up menu
        """
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g5!mregion!']")
        utillobj.click_on_screen(parent_elem, 'middle', x_offset=-10, y_offset=40)   
        vis_obj.select_tooltip("riser!s0!g5!mregion!", "Drill Down 1", "MAINTABLE_wbody1",xoffset=-30,yoffset=60)
        
        """
        Step20: Verify Information Builder web page is displayed in a new window (or tab)
        """
        time.sleep(15)
        core_utils.switch_to_new_window(current_browser_window_title = 'Business')
        expected_title='Data and Analytics Company | ibi'
        drill1=(driver.title in expected_title)
        utillobj.asequal(True, drill1, "Step 20.00: Verify Information Builder web page is displayed in a new window (or tab)")
        time.sleep(5)
        core_utils.switch_to_previous_window()
          
        """
        Step21: Close the output winow
        """
        core_utils.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()  