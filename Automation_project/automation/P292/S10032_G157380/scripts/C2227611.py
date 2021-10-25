'''
Created on May 23, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227611
TestCase Name = Filter Chart - ESRI Bubble map
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227611_TestClass(BaseTestCase):

    def test_C2227611(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227611'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Change" dropdown > select ESRI Proportional (Bubble) map
        """
        ribbonobj.change_chart_type("bubble_map")
        
        """
        Step 03: Right click "Store,State,Province" > "Map As" > "US State (Name)"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Store,State,Province',1, 1, 'Map As', 'US State (Name)')
        time.sleep(4)
        
        """
        Step 04: Double click "Store,State,Province", "Revenue"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 51)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Revenue', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
        
        """
        Step 05: Click Pan and Select few points on Maps > Select Filter chart.
        """
        time.sleep(3)
        raiser="[id^='MAINTABLE_1'] [class*='riser!s0!g25!mmarker!']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        pan_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1 div[class^='SelectionButton UIButton toggleModePan']")
        utillobj.click_on_screen(pan_css, coordinate_type='middle', click_type=0)
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 36)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g25!mmarker!",expected_tooltip, "Step 05: verify the default tooltip values")       
        time.sleep(6)
        action1 = ActionChains(self.driver)
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser = utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move1, move=True)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g72!mmarker!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        time.sleep(2)
        resultobj.create_lasso('MAINTABLE_wbody1','circle', 'riser!s0!g72!mmarker!', target_tag='circle', target_riser='riser!s0!g56!mmarker!')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(5)
        
        """
        Step 06: Verify the chart preview.
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step06.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 06.a: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 06.b Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '166M', '4.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06.d Verify legend Title")
        time.sleep(5)
         
        """
        Step 07: Hover over Idaho and verify menu.
        """
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 07: verify the default tooltip values")       
         
        """
        Step 08: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step 09: Hover over bubble (Idaho) > Verify menu
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(2)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 09: verify the default tooltip values")       
        time.sleep(5)
         
        """
        Step 10: Select "Exclude from Chart"
        """
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!s0!g0!mmarker!", "Exclude from Chart", wait_time=1)
        time.sleep(5)
         
        """
        Step 11: Verify output
        """
        chart_type_css="circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 2, 'Step 11.a: Verify number of Circle displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 11.b: Verify first bar color")
        legend=['Revenue', 'Revenue', '4,478K']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:c Verify legends Title")
        time.sleep(2)
        expected_tooltip=['Store State Province:Oregon', 'Revenue:$4,169,174.83', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 11.d: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227611_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 13: Click "Save" > "C2227611" > click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 16: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.verify_filter_pane_field('Store,State,Province',1,"Step16.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 3, 'Step 16.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 16.c(i) Verify first bar color")
        legend=['Revenue', 'Revenue', '327.8M', '166M', '4.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 16.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()