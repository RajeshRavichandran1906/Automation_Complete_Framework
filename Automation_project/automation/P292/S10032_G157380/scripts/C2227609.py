'''
Created on May'26, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227609
'''
import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227609_TestClass(BaseTestCase):
    def test_C2227609(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227609'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
           
        """
        Step02: Select "Home" > "Visual" > "Change" (dropdown) > "Map".
        Step03: Set "Territory" = "World".
        Step04: Click "OK".
        """
        ribbonobj.change_chart_type('map')
        time.sleep(3)
        ribbonobj.select_map('choropleth',teritory='World',btn_click='ok')
        time.sleep(3) 
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css="div.leaflet-control-scale-line"
        resultobj.wait_for_property(parent_css,2)      
           
        """
        Step03: Locate and double click "Customer,Country,ISO-3166,Code", under Customer Dimension
        Step04: Verify "Location Type" dialog box displayed.
        Step05: Set "Geographic Role" = "iso_a2 (...)".
        Step06: Click "OK".
        """
        metaobj.datatree_field_click("Customer,Country,ISO-3166,Code", 2, 1)
        time.sleep(5) 
        css="#locTypeOkBtn"
        cap="div[id^='QbDialog'] [class*='active'] [class*='caption'] [class*='bi-label']"
        cap_css=self.driver.find_element_by_css_selector(cap)
        utillobj.verify_popup(css, "Step04: Verify dialog box displayed")
        print("text",cap_css.text)
        a=self.driver.find_elements_by_css_selector(cap)
        print(a[len(a)-1].text)
        utillobj.asequal(a[len(a)-1].text,"Location Type", "StepX: Verify Caption text in popup")
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"iso_a2 (AD, AE, AF)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(2)
          
        """
        Step09: Double-click "Gross Profit" from Sales
        """  
        metaobj.datatree_field_click("Gross Profit", 2,1)
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 42)
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
           
        """
        Step10: Verify Preview
        Step11: Hover over Brazil > Verify menu
        """
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",42, 'Step10.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mstate", "burnt_sienna", "Step10.c(i) Verify first bar color")
        legend=['Gross Profit', '0M', '23.5M', '47M', '70.5M', '94M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Gross Profit:$11,022,235.68', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mstate",expected_tooltip, "Step10.e: verify the default tooltip values")       
          
        """
        Step12: Select "Filter Chart" > Verify Preview
        """ 
        parent_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mstate']")
        utillobj.click_on_screen(parent_elem, 'middle')
#         time.sleep(1)
        self.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mstate",'Filter Chart',wait_time=1,default_move=True)
#         time.sleep(2)
#         resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g4!mstate",'Filter Chart',wait_time=1)
             
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step12.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step12.c(i) Verify first bar color")
        legend=['Gross Profit', '11M', '11.3M', '11.6M', '11.8M', '12.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step12:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Gross Profit:$11,022,235.68']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mstate",expected_tooltip, "Step12.e: verify the default tooltip values")       
            
        """
        Step13: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
                 
        """
        Step14: Hover over Brazil > Verify menu
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5) 
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step14.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step14.c(i) Verify first bar color")
        legend=['Gross Profit', '11M', '11.3M', '11.6M', '11.8M', '12.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step14:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Gross Profit:$11,022,235.68']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mstate",expected_tooltip, "Step14.e: verify the default tooltip values")       
           
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227609_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
            
        """
        Step15: Close the output window
        Step16: Click Save in thetoolbar, Save as "C2158150" > Click Save
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
        Step17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
            
        """
        Step19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
             
        """
        Step20: Verify canvas
        """
        parent_css2="#MAINTABLE_wbody1 [class*='riser!s']"
        resultobj.wait_for_property(parent_css2,1)
            
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",1, 'Step20.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step20.c(i) Verify first bar color")
        legend=['Gross Profit', '11M', '11.3M', '11.6M', '11.8M', '12.1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step20:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Gross Profit:$11,022,235.68']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mstate",expected_tooltip, "Step20.e: verify the default tooltip values")       
        time.sleep(4)         
        
    def select_default_tooltip_menu(self,parent_id, raiser_class, menu_path, wait_time=2, **kwargs):
        utillobj = utillity.UtillityMethods(self.driver)
        menus=menu_path.split('->')
        raiser_css="#"+ parent_id + " [class*='" + raiser_class + "']"
        tooltip_css="#"+ parent_id + " span[id='tdgchart-tooltip'] [onclick^='ibiChart']"
        browser = utillobj.parseinitfile('browser')
        if 'default_move' in kwargs:
            pass
        else:
            obj_locator=self.driver.find_element_by_css_selector(raiser_css)
            if browser == 'Firefox':
                utillobj.click_type_using_pyautogui(self, obj_locator,**kwargs)
            else:
                action1=ActionChains(self.driver)
                action1.move_to_element(obj_locator).perform()
                del action1
        if browser == 'IE':
            time.sleep(0.5)
        else:
            time.sleep(wait_time)
        tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
        tooltips[[el.text.strip() for el in tooltips].index(menus[0])].click()
        
        
        
if __name__ == '__main__':
    unittest.main()

