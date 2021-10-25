'''
Created on Oct 19, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325620
TestCase Name = Verify Drill Down to Web Page with Choropleth ESRI Map
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2325620_TestClass(BaseTestCase):
    
    def test_C2325620(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2325620'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        iaribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass') 
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
               
        """
        Step02: Click on the "Change" button in the Home Tab ribbon > Select "Choropleth" ESRI map
        """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(3)        
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)      
                
        """
        Step03: Double-click "Revenue" from Sales Measures
        """
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(8)
          
        """
        Step04: Double-click "Customer,Country", located under Customer Dimension
        """
        metaobj.datatree_field_click("Customer,Country", 2,1)
        time.sleep(8)
           
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
           
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
          
        """
        Step05: Select "Revenue" in the Query pane > Click on "Drill Down" button in the Ribbon
        """
        metaobj.querytree_field_click("Revenue", 1)
        time.sleep(5)
        parent_css="#FieldDrillDown img"
        resultobj.wait_for_property(parent_css, 1)
        ribbon_item=driver.find_element_by_css_selector("#FieldDrillDown img")
        utillobj.default_left_click(object_locator=ribbon_item)
           
        """
        Step06: Select "Web Page"
        Step07: Type URL http://www.ibi.com
        Step08: Click "OK"
        """
        time.sleep(8)
        parent_css="div[id^='QbDialog'] div[id^='IABottomBar'] #ok"
        resultobj.wait_for_property(parent_css, 1)
        iaribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com", click_ok=True)
          
        """
        Step09: Hover over United States > Verify pop up menu displays "Drill Down 1"
        """
        time.sleep(10)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",41, 'Step 09.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 09.b Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step09.c Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',x_offset=10, y_offset=-25)
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            time.sleep(3)
        expected_tooltip=['Customer Country:United States', 'Revenue:$333,514,945.66', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mregion!",expected_tooltip, "Step 09.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
          
        """
        Step10: Select "Drill Down 1"
        """
        time.sleep(5)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g24!mregion!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',x_offset=10, y_offset=-25)   
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g24!mregion!", 'Drill Down 1', default_move=True)
        time.sleep(10)
          
        """
        Step11: Verify Information Builder web page is displayed in a new window (or tab)
        """
        utillobj.switch_to_window(1,window_title='Business')
        time.sleep(15)
        expected_title='Business Intelligence and Data Management Software | Information Builders'
        drill1=(driver.title in expected_title)
        utillobj.asequal(True, drill1, "Step11: Verify Information Builder web page is displayed in a new window (or tab)")
#         time.sleep(2)
#         elem=(By.CSS_SELECTOR,"[class*=top-bar-title] [id^='branding'] a img")
#         resultobj._validate_page(elem)
#         alternate_text=driver.find_element_by_css_selector("[class*=top-bar-title] [id^='branding'] a img").get_attribute('alt')
#         print(alternate_text)
#         utillobj.asequal('logo',alternate_text,'Step 11: Verify Information Builders Web page is displayed in a new window (or tab)')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#offCanvas")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step12: Close the output winow
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        """
        Step13: Click "Save" in the toolbar > Save As "C2325620" > Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
           
        """
        Step14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2325655.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2', mrid='mrid', mrpass='mrpass')
        time.sleep(10)
        
        """
        Step16: Hover over Mexico > Verify pop up menu displays "Drill Down 1"
        """
        time.sleep(10)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",41, 'Step 16.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 16.b Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16.c Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g24!mregion!']")
        utillobj.click_on_screen(parent_elem, 'top_middle',x_offset=10, y_offset=-25)
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            time.sleep(3)
        expected_tooltip=['Customer Country:United States', 'Revenue:$333,514,945.66', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g24!mregion!",expected_tooltip, "Step 16.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
        
        """
        Step17: Click "Run" in the toolbar
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
        time.sleep(15)
                  
        """
        Step18: Hover over Canada > Verify pop up menu displays "Drill Down 1"
        """
        chart_type_css="path[class*='riser!s0!g5!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",41, 'Step 18.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g41!mregion!", "elf_green", "Step 18.b Verify first bar color")
        legend=['Revenue', '0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18.c Verify legend Title")
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g5!mregion!']")
        utillobj.click_on_screen(parent_elem, 'middle',x_offset=-10, y_offset=40)
        browser=utillobj.parseinitfile('browser')
        if browser=='IE':
            time.sleep(3)
        expected_tooltip=['Customer Country:Canada', 'Revenue:$89,683,027.34', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer State Province', 'Drill Down 1']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g5!mregion!",expected_tooltip, "Step 18.d: verify the default tooltip values", default_move=True)
        time.sleep(5)
        
        """
        Step19: Select "Drill Down 1" from the pop up menu
        """
        time.sleep(5)
        wind_handle=driver.window_handles 
        print(wind_handle)       
        time.sleep(5)
        css=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(css, coordinate_type='start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g5!mregion!']")
        utillobj.click_on_screen(parent_elem, 'middle', x_offset=-10, y_offset=40)   
        resultobj.select_drilldown_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g5!mregion!", 'Drill Down 1', default_move=True)
        time.sleep(10)
        wind_handle1=driver.window_handles 
        time.sleep(5)
        print(wind_handle1)
        
        """
        Step20: Verify Information Builder web page is displayed in a new window (or tab)
        """
        time.sleep(10)
        utillobj.switch_to_window(2, custom_windows=wind_handle, window_title='Business')                 
        time.sleep(15)
        expected_title='Business Intelligence and Data Management Software | Information Builders'
        drill1=(driver.title in expected_title)
        utillobj.asequal(True, drill1, "Step11: Verify Information Builder web page is displayed in a new window (or tab)")
#         elem=(By.CSS_SELECTOR,"[class*=top-bar-title] [id^='branding'] a img")
#         resultobj._validate_page(elem)
#         alternate_text=driver.find_element_by_css_selector("[class*=top-bar-title] [id^='branding'] a img").get_attribute('alt')
#         print(alternate_text)
#         utillobj.asequal('logo',alternate_text,'Step 20: Verify Information Builders Web page is displayed in a new window (or tab)')
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(1,win_num=1)                 
        time.sleep(15)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step21: Close the output winow
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()  