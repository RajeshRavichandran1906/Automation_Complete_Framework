'''
Created on Jun'13 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227608'''
import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227608_TestClass(BaseTestCase):
    def test_C2227608(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227608'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step02: Click "Change" dropdown > "Map"
        Step03: Select "Leaflet Bubble" > OK
        """
        ribbonobj.change_chart_type('map')
        time.sleep(3)
        ribbonobj.select_map('bubble')
        time.sleep(2)
        ribbonobj.select_map('bubble',btn_click='ok')
        time.sleep(3)
        parent_css="div.leaflet-control-scale-line"
        resultobj.wait_for_property(parent_css,2)
        time.sleep(5)
           
        """
        Step04: Double click "Store,State,Province"
        Step05: Select "state_name" from Geographic Role dropdown > OK
        Step06: Double click "Gross Profit"
        """
        metaobj.datatree_field_click("Store,State,Province", 2, 1)
        time.sleep(5)
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"state_name (Alabama, Alaska, Arizona)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)       
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
         
        """
        Step07: Click "Pan" in the map canvas
        """        
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1 button[class^='data-selection-button leaflet-control']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(3)
          
        """
        Step08: Lasso "Maine", "New York", "Massachusetts" bubbles (as shown in the screenshot)
        Step09: Verify Lasso Menu
        Step10: Select "Exclude from Chart"
        Step11: Verify the map is updated
        """
        riser=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g50!mstate']")
        utillobj._validate_page(riser)
         
        time.sleep(2)
        source=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g50!mstate']")
        target=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g41!mstate']")
        
        utillobj.drag_to_using_pyautogui(source, target,sx_offset=-15,tx_offset=25,sy_offset=6)
#         resultobj.create_lasso('MAINTABLE_wbody1','path', 'riser!s0!g50!mstate!',pyautogui=True,sy_offset=15,target_tag='path', target_riser='riser!s0!g41!mstate!')
        menu=['3 points', 'Filter Chart', 'Exclude from Chart', 'Group Store,State,Province Selection']
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart',verify=menu,msg="Step11: Verify menu")
        time.sleep(5)
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        
        
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step11.a:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step11.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step 11.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:c Verify legends Title")
        
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mstate",expected_tooltip, "Step11: verify the default tooltip values")       
        
        """
        Step12:Click "Run"
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        
        """
        Step13: Verify the map runs in a new window
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step13.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step13.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:c Verify legends Title")
        
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mstate",expected_tooltip, "Step13: verify the default tooltip values")       
        
        """
        Step14: Click "Pan" in the map canvas
        Step15: Lasso all bubbles except Alaska and Hawaii
        Step16: Select "Filter Chart"
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        time.sleep(2)
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1 button[class^='data-selection-button leaflet-control']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(3)
        riser=(By.CSS_SELECTOR,"#MAINTABLE_wbody1 [class*='riser!s0!g69!mstate']")
        utillobj._validate_page(riser)
        time.sleep(2)
        source=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g69!mstate']")
        coord=utillobj.get_object_screen_coordinate(source, 'middle')
        sx=coord['x']-30
        sy=coord['y']-30
        time.sleep(2)
        target=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 path[class*='riser!s0!g19!mstate']")
        coord1=utillobj.get_object_screen_coordinate(target, 'middle')
        tx=coord1['x']+70
        ty=coord1['y']+30
        time.sleep(5)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5) 
        
        """
        Step17: Verify the map is updated
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 31)
        
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 31, 'Step17.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g7!mstate", "bar_blue", "Step 17.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.3M', '0.3M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:c Verify legends Title")
        
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g7!mstate",expected_tooltip, "Step17: verify the default tooltip values")       
         
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227608_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step19: Click Save in the toolbar
        Step19: Save as "C2158150" > Click Save
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
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
         
        """
        Step21: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_2',mrid='mrid',mrpass='mrpass')
          
        """
        Step22: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step22.a:Verify Filter pane")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step22.a: Verify number of bubble displayed', custom_css="svg g>path[class^='riser!s']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g25!mstate", "bar_blue", "Step22.b: Verify first bar color")
        legend=['Gross Profit', 'Gross Profit', '92.2M', '46.1M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step22:c Verify legends Title")
        
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Gross Profit:$92,237,787.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mstate",expected_tooltip, "Step22: verify the default tooltip values")       
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()

