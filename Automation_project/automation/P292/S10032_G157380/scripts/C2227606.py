'''
Created on Apr 26, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227606
TestCase Name = Lasso Filter using Pie chart type
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class C2227606_TestClass(BaseTestCase):

    def test_C2227606(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227606'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
          
        """
        Step 02: Click "Change" in the Home Tab > Select "Pie" chart
        """
        ribbonobj.change_chart_type("pie")
         
        """
        Step 03: Double-click "Cost of Goods" and "Gross Profit"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
         
        """
        Step 04: Double-click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 8)
         
        """
        Step 05:  Lasso top area of the Pies chart as displayed in the screen shot > Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s5!g0!mwedge!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','path', 'riser!s5!g0!mwedge', target_tag='path', target_riser='riser!s0!g1!mwedge')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
         
        """
        Step 06: Verify canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
         
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step06.a: Verify X-axis label")
         
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step06.b: Verify X-axis label")
         
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step06.c:")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 10, 'Step 06.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 06.d(i) Verify first bar color")
        legend=['Product Category', 'Accessories', 'Camcorder', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00  (17.90%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step 06e: verify the default tooltip values")       
        
        
        """
        Step07: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 08: Verify output
        """
        chart_type_css="path[class*='riser!s0!g0!mwedge']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step08.a: Verify X-axis label")
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step08.b: Verify X-axis label")
        
        time.sleep(5)
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 10, 'Step 08.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 08.d(i) Verify first bar color")
        legend=legend=['Product Category', 'Accessories', 'Camcorder', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00  (17.90%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step 08.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227606_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 09: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 10:  Lasso Pies for "Stereo Systems" and "Camcorder" > Select "Filter Chart"
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s2!g0!mwedge!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','path', 'riser!s2!g0!mwedge', target_tag='path', target_riser='riser!s1!g1!mwedge')
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step 11: Verify canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step11.a: Verify X-axis label")
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step11.b: Verify X-axis label")
        
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step11.c:")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 4, 'Step 11.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 11.d(i) Verify first bar color")
        legend=['Product Category', 'Camcorder', 'Stereo Systems']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00  (33.83%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step 11.e: verify the default tooltip values")       
        
        """
        Step 12: Click Save in the toolbar
        Step 13: Save as "C2158149" > Click Save
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
        Step 16: Verify canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step16.a: Verify X-axis label")
        
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step16.b: Verify X-axis label")
        
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step16.c:")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 4, 'Step 16.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 16.d(i) Verify first bar color")
        legend=['Product Category', 'Camcorder', 'Stereo Systems']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00  (33.83%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step 16e: verify the default tooltip values")       
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main() 