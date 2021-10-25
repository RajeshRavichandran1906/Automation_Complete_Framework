'''
Created on Sep 11, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324237
TestCase Name = Run Mode : Run_the_Portal
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, wf_mainpage, ia_resultarea, vfour_portal_run, wf_legacymainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from pynput.keyboard import Key, Controller

class C2324237_TestClass(BaseTestCase):

    def test_C2324237(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        time.sleep(10)
        driver.implicitly_wait(1)
        elem1=WfMainPageLocators.__dict__['banner_administrator']
        resultobj._validate_page(elem1)
        time.sleep(5)        

        """
        Step 02: Double click the portal 'BIP_xxx_Portal123_V4' under P292 domain ->S10117 folder to run it
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        print('pass')
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel']",frame_height_value=0)
        time.sleep(8)
        print('Inside frame')
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resultobj.wait_for_property(parent_css, 7)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        """
        Step 02.1: Verify the changes that we made in the portal design mode are available in run mode;
        """
        total_panel=len(driver.find_elements_by_css_selector("[id^='BipInnerBox'] div[id^='BiLabel'][class*='bi-label bip-title-bar pd-internal-id']"))
        actual_panel=int(total_panel)
        print(actual_panel)
        utillobj.asequal(4, actual_panel, "Step2.a: Verify number of panels in portal")
        
        panel_title=['Panel 1','Category Sales','Panel 3','Panel 4']
        css="[id^='BipInnerBox'] div[id^='BiLabel'][class*='bi-label bip-title-bar pd-internal-id']"
        title_css=driver.find_elements_by_css_selector(css)
        menu_list=[el.text.strip() for el in title_css]
        print(menu_list)
        utillobj.asequal(panel_title, menu_list, "Step2.b: Verify panel title")
        
        user_id = utillobj.parseinitfile('mrid03')
        print(user_id)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        else:
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        
        """verify Panel 1"""
        utillobj.verify_object_visible("div[id^='BidTreeBlock'][class*='bi-component']", True, 'Step 2.c: Panel1 Visible')
        utillobj.verify_object_visible("#treeView tbody>tr>td>img[src*='discovery_domain']", True, 'Step 2.d: Domain tree Visible')
        
        """verify Panel 2"""
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Panel']",frame_height_value=0)
        time.sleep(8)
        print('Inside panel2 frame')
        
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0",7, 'Step02.e: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Revenue',"Step02.f: Verify X-axis label")
        
        elem=self.driver.find_element_by_css_selector("#jschart_HOLD_0 text[class^='totalLabel!g0!mtotalLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'1.1B',"Step02.g: Verify total label")
        
        legend=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step02.h Verify legend Title")
        
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "bar_blue1", "Step 02.i Verify first bar color")
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        """verify Panel 3"""
        utillobj.verify_object_visible("div[id^='BipAccordionPane'][class*='bi-component accordion-pane']", True, 'Step 2.j: Panel3 Visible')
        accordian_title=['Regional Sales Trend','Accordion_report']
        css="div[id^='BipAccordionButton'] div[class*='bi-button-label']"
        title_css=driver.find_elements_by_css_selector(css)
        accordian_list=[el.text.strip() for el in title_css]
        print(accordian_list)
        utillobj.asequal(accordian_title, accordian_list, "Step2.k: Verify accordian title")
        
        utillobj.switch_to_frame(pause=2,frame_css="[class*='bi-iframe iframe '][name^='Area_1']",frame_height_value=0)
        time.sleep(8)
        print('Inside panel3 frame')
        
        parent_css="#jschart_HOLD_0 path[class*='riser!']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("jschart_HOLD_0", 4, 'Step02.l: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        
        legend=['EMEA', 'North America', 'Oceania', 'South America']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend, "Step02.m Verify legend Title")
        
        resultobj.verify_xaxis_title("jschart_HOLD_0", "Month", "Step 02.n: Verify -xAxis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", "Revenue", "Step 02.o: Verify -yAxis Title")
        time.sleep(2)
        expected_xval_list=['1','2','3','4','5','6','7','8','9','10','11','12']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resultobj.verify_riser_chart_XY_labels("jschart_HOLD_0", expected_xval_list, expected_yval_list, "Step 02.p: Verify XY labels")
        
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mline!", "bar_blue1", "Step 02.q Verify first bar color", attribute_type='stroke')
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        
        """verify Panel 4"""
        utillobj.verify_object_visible("div[id^='BipTabPane']", True, 'Step 2.r: Panel4 Visible')
        tab_bar_title=['Demo Videos', 'babydeer', 'Discount by Region', 'Tab 4']
        css="div[id^='BipTabButton'] div[class*='bi-button-label']"
        title_css=driver.find_elements_by_css_selector(css)
        title_list=[el.text.strip() for el in title_css]
        print(title_list)
        utillobj.asequal(tab_bar_title, title_list, "Step2.s: Verify accordian title")
        
        """
        Step 02.2: Verify the URL is correct. the machine name might be different for your testing. make sure its softcontext/portal/parent folder/portal name
        """
        current_url = driver.current_url
        print(current_url)
        portal_url = "/portal/P292/S10117/BIP_V4_Portal/BIP_xxx_Portal123_V4"
        utillobj.asin(portal_url, current_url, "Step 02.2: Verify the portal URL is correct")
        
        """
        Step 03: Bring up the F8 tree and scroll to the right
        Verify that white spaces appear
        """
        tree_css=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.click_on_screen(tree_css, 'middle')
        time.sleep(3)
        keyboard = Controller()
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        time.sleep(1)
        elem1=(By.CSS_SELECTOR, "#treeContainer")
        resultobj._validate_page(elem1)
        utillobj.verify_object_visible("#treeContainer", True, 'Step 03: Resource tree Visible')
        time.sleep(1)
        tree_css=driver.find_element_by_css_selector("#treeContainer")
        utillobj.click_on_screen(tree_css, 'bottom_middle')
        time.sleep(2)
        utillobj.click_on_screen(tree_css, 'bottom_middle', click_type=0, y_offset=-7, mouse_duration=1.5)
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#treeContainer")
        utillobj.take_screenshot(ele,'C2324237_Actual_step03', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 04: Close the F8 resource tree
        """
        time.sleep(3)
        keyboard = Controller()
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        time.sleep(3)
        utillobj.verify_object_visible("#treeContainer", False, 'Step 04: Resource tree closed')
        
        """
        Step 05: Press F8 to bring the tree back
        Verify that it shows the original state.
        """
        time.sleep(3)
        keyboard = Controller()
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        elem1=(By.CSS_SELECTOR, "#treeContainer")
        resultobj._validate_page(elem1)
        utillobj.verify_object_visible("#treeContainer", True, 'Step 05: Verify Resource tree shows the original state')
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#treeContainer")
        utillobj.take_screenshot(ele,'C2324237_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 06: Close the resource tree.
        Close portal
        """
        time.sleep(3)
        keyboard = Controller()
        keyboard.press(Key.f8)
        keyboard.release(Key.f8)
        time.sleep(3)
        utillobj.verify_object_visible("#treeContainer", False, 'Step 06: Close the resource tree')
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.take_screenshot(ele,'C2324237_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 07: Sign Out from WebFOCUS
        """
        
        
        
if __name__ == '__main__':
    unittest.main()        