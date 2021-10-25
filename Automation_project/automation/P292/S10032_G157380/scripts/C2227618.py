'''
Created on Jun 2, 2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227618
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227618_TestClass(BaseTestCase):

    def test_C2227618(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227618'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)      
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
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
        Step 05:Hover over slice for "Stereo Systems" (orange) > Verify menu > Select "Drill down to Product Subcategory"
        """        
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s4!g0!mwedge!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s4!g0!mwedge','Drill down to Product Subcategory',wait_time=1)
 
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
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step06.a: Verify X-axis label")
           
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step06.b: Verify X-axis label")
           
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step06.c: Verify filter pane")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 10, 'Step 06.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 06.d(i) Verify first bar color")
        legend=['Product Subcategory', 'Boom Box', 'Home Theater Systems', 'Receivers', 'Speaker Kits', 'iPod Docking Station']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Subcategory:Home Theater Systems', 'Cost of Goods:$56,428,589.00  (27.51%)', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s1!g0!mwedge",expected_tooltip, "Step 06e: verify the default tooltip values")       
         
        """
        Step07: Hover over slice for "Home Theater Systems" > Select "Drill down to Model"
        """
#         utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s1!g0!mwedge!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1','riser!s1!g0!mwedge','Drill down to Model',wait_time=1)

        """
        Step08: Verify canvas
        Step09: Hover over blue slice for "LG MDD72" > Verify menu
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 9)
          
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step08.a: Verify X-axis label")
          
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step08.b: Verify X-axis label")
          
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Subcategory',2,"Step08.c: Verify filter pane")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 16, 'Step 08.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step 08.d(i) Verify first bar color")
        legend=['Model', 'LG MDD72', 'LG XD63', 'Panasonic', 'Panasonic SC-PT160', 'Pioneer HTZ-170', 'Samsung HT-Z120', 'Sharp HT-CN550', 'Sony DAV-DZ30']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Model:LG MDD72', 'Cost of Goods:$6,008,739.00  (10.65%)', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step09: verify the default tooltip values")       
        
        """
        Step10: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step11: Verify output
        Step12: Hover over blue slice for "LG MDD72" in the "Gross Profit" Pie > Verify menu
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 9)
         
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step11.a: Verify X-axis label")
         
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step11.b: Verify X-axis label")
         
        time.sleep(5)
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 16, 'Step11.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step10.d(i) Verify first bar color")
        legend=['Model', 'LG MDD72', 'LG XD63', 'Panasonic', 'Panasonic SC-PT160', 'Pioneer HTZ-170', 'Samsung HT-Z120', 'Sharp HT-CN550', 'Sony DAV-DZ30']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Model:LG MDD72', 'Cost of Goods:$6,008,739.00  (10.65%)', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step12: verify the default tooltip values")       
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227618_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step14: Click Save in the toolbar
        Save as "C2158149" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
         
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
         
        """
        Step17: Verify canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='pieLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 9)
          
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Cost of Goods',"Step17.a: Verify X-axis label")
          
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 text[class^='pieLabel!g1!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step17.b: Verify X-axis label")
          
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Subcategory',2,"Step08.c: Verify filter pane")
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody1", 1, 16, 'Step17.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mwedge", "bar_blue", "Step17.d(i) Verify first bar color")
        legend=['Model', 'LG MDD72', 'LG XD63', 'Panasonic', 'Panasonic SC-PT160', 'Pioneer HTZ-170', 'Samsung HT-Z120', 'Sharp HT-CN550', 'Sony DAV-DZ30']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step17:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Model:LG MDD72', 'Cost of Goods:$6,008,739.00  (10.65%)', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mwedge",expected_tooltip, "Step17: verify the default tooltip values")       
         
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
         
if __name__ == '__main__':
    unittest.main() 