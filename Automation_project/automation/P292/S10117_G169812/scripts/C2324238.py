'''
Created on Sep 14, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324238
TestCase Name = Run Mode_Run Tree : Run_Reports_frm_Resource_tree_Panel_And_Close_Portal_Run_Mode
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, wf_mainpage, ia_resultarea, active_miscelaneous, vfour_portal_run, wf_legacymainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase

class C2324238_TestClass(BaseTestCase):

    def test_C2324238(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324238'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        time.sleep(15)
        driver.implicitly_wait(1)
        elem1=WfMainPageLocators.__dict__['banner_administrator']
        resultobj._validate_page(elem1)
        time.sleep(5) 
        
        """
        Step 02: Run 'BIP_xxx_Portal123_V4' portal under P292 domain -> S10117 folder.
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1)
        
        """
        Step 03: From the Resource tree panel Panel1(located inside the panel1 in run mode); 
        Double click on P292->S10117-> 'BIP_V4_Portal' folder and run all the created reports such as Accordion report, 
        tagCloud chart, cd7, babydeer, honda_integra, bluehills and IA_Chart1.
        Verify it runs fine without any error.
        """
        time.sleep(3)
        tree_css=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.click_on_screen(tree_css, 'middle')
        time.sleep(8)
        parent_css="#treeView tbody>tr>td>img[src*='discovery_domain']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
         
        """Accordion_report"""
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->Accordion_report', 'Run', expand_resource_tree=True)
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5)
        parent_css="[ibiattr='table1']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3) 
#         vfour_runobj.create_table_data_set("[ibiattr='table1']", Test_Case_ID+ "_Ds01.xlsx") 
        vfour_runobj.verify_table_data_set("[ibiattr='table1']",  Test_Case_ID+ "_Ds01.xlsx","Step 03.1: Verify Accordion_report data set")
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
          
        """tagCloud_chart""" 
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->tagCloud_chart', 'Run')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="#jschart_HOLD_0 text[class*='riser!']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step03.2: Verify number of tagcloud labels displayed', custom_css="svg g>text[class^='riser!s']")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g0!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'ENGLAND',"Step03.3: Verify ENGLAND label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g1!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'FRANCE',"Step03.4: Verify FRANCE label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g2!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'ITALY',"Step03.5: Verify ITALY label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g3!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'JAPAN',"Step03.6: Verify JAPAN label text")
         
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='riser!s0!g4!mtag!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'W GERMANY',"Step03.7: Verify W GERMANY label text")
         
        time.sleep(3)
        expected_tooltip_list = ['(W GERMANY = 1,309)']
        active_misobj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s0!g4!mtag!", expected_tooltip_list, "Step 03: verify the default tooltip values")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g4!mtag!", "elf_green", "Step 03.8 Verify W GERMANY color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mtag!", "cumulus", "Step 03.9 Verify ENGLAND color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mtag!", "banana_mania", "Step 03.10 Verify ITALY color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g3!mtag!", "burnt_sienna_1", "Step 03.11 Verify JAPAN color") 
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mtag!", "persian_red", "Step 03.12 Verify FRANCE color")
        time.sleep(3)
        browser=utillobj.parseinitfile('browser')
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0 [class*='chartPanel']")
        utillobj.take_screenshot(ele,'C2324238_Actual_step03a', image_type='actual',x=1, y=1, w=-1, h=-1)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
         
        """cd7"""
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->cd7', 'View')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="img[src*='cd7']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        if browser == 'IE':
            utillobj.take_monitor_screenshot('C2324238_Actual_step03b_'+browser, image_type='actual', left=0, top=25, right=800, bottom=500)
        else:
            utillobj.take_monitor_screenshot('C2324238_Actual_step03b_'+browser, image_type='actual', left=100, top=100, right=100, bottom=100)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1)
          
        """babydeer"""
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->babydeer', 'View')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="img[src*='babydeer']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        if browser == 'IE':
            utillobj.take_monitor_screenshot('C2324238_Actual_step03c_'+browser, image_type='actual', left=0, top=25, right=800, bottom=500)
        else:
            utillobj.take_monitor_screenshot('C2324238_Actual_step03c_'+browser, image_type='actual', left=100, top=100, right=100, bottom=100)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
          
        """honda_integra"""
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->honda_integra', 'View')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="img[src*='honda_integra']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        if browser == 'IE':
            utillobj.take_monitor_screenshot('C2324238_Actual_step03d_'+browser, image_type='actual', left=0, top=25, right=800, bottom=500)
        else:
            utillobj.take_monitor_screenshot('C2324238_Actual_step03d_'+browser, image_type='actual', left=100, top=100, right=100, bottom=100)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
          
        """Bluehills""" 
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->Bluehills', 'View')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="img[src*='Bluehills']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        if browser == 'IE':
            utillobj.take_monitor_screenshot('C2324238_Actual_step03e_'+browser, image_type='actual', left=0, top=25, right=800, bottom=500)
        else:
            utillobj.take_monitor_screenshot('C2324238_Actual_step03e_'+browser, image_type='actual', left=100, top=100, right=100, bottom=100)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
          
        """IA_Chart1""" 
        vfour_runobj.select_portal_resource_menu('P292->S10117->BIP_V4_Portal->IA_Chart1', 'Run')
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(5) 
        parent_css="#jschart_HOLD_0 rect[class*='riser!']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 5, 'Step03.13: Verify number of risers displayed', custom_css="svg g>rect[class^='riser!s']")
        resultobj.verify_xaxis_title("jschart_HOLD_0", "COUNTRY", "Step 03.14: Verify -xAxis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "DEALER_COST", "Step 03.15: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        expected_yval_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 03.16: Verify XY labels")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 03.17: Verify first bar color")
        time.sleep(3)
        expected_tooltip=['COUNTRY:ENGLAND','DEALER_COST:37,853']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mbar",expected_tooltip, "Step 03.18: verify the default tooltip values")
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#jschart_HOLD_0 [class*='chartPanel']")
        utillobj.take_screenshot(ele,'C2324238_Actual_step03f', image_type='actual',x=1, y=1, w=-1, h=-1)
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1) 
        
        """
        Step 04: Close the portal run mode by clicking on the Close Menubar link.
        """
        vfour_runobj.select_or_verify_portal_menu_bar_item(select='Close', msg='Step 04: Close the portal run mode by clicking on the Close Menubar link.')
        time.sleep(2)
        
        """
        Step 05: Expand P292 domain ->S10117 folder.
        Verify that you are back on the main portal page and the portal is still present
        """
        driver.implicitly_wait(1)
        elem1=WfMainPageLocators.__dict__['banner_administrator']
        resultobj._validate_page(elem1)
        time.sleep(1) 
        wf_mainobj.get_repository_item_availability('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4')
        
        """
        Step 06: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
        
        
if __name__ == '__main__':
    unittest.main()