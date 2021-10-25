'''
Created on Sep 8, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324221
TestCase Name = Portal Designer_Design Properties : Rename_Default_page
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, wf_legacymainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
import pyautogui

class C2324221_TestClass(BaseTestCase):

    def test_C2324221(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324221'
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
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
        Step 02: Edit 'BIP_xxx_Portal123_V4' from P292 domain->S10117 folder
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        time.sleep(5)
        utillobj.switch_to_window(1)
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        
        """ 
        Step 3: Click on Page 1
        """
        time.sleep(3)
        elem1=(By.CSS_SELECTOR, "#LayoutTab")
        resultobj._validate_page(elem1)
        page_css = driver.find_elements_by_css_selector("[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        utillobj.click_on_screen(page_css[0], 'middle', click_type=0)
        time.sleep(3)
        
        """ 
        Step 4: Enter 'Page_New' in the Title section of properties
        """
        parent_css= "#PropertiesPanelID div[id^='PropertiesPanel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        property_css = driver.find_element_by_css_selector("#idPropertiesPage div[id^='BiTabButton']")
        utillobj.click_on_screen(property_css, 'middle', click_type=0)
        time.sleep(5)
        element = driver.find_elements_by_css_selector("#PropertiesPanelID [id^='BiVBox'] input[id^='BiTextField']")
        utillobj.click_on_screen(element[0], 'middle', click_type=0)
        time.sleep(3)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(3)
        pyautogui.press('backspace', pause=2)
        time.sleep(3)
        pyautogui.typewrite('Page_New', interval=0.5)
        time.sleep(3)
        
        
        """Verify that the title got changed on the page tab and also in the properties section"""
        page_css = driver.find_elements_by_css_selector("[id^='BipNavigatorTop'] div[id^='BipNavigatorButton']")
        actual_pagetitle = page_css[0].text.strip()
        print(actual_pagetitle)
        expected_pagetitle = 'Page_New'
        utillobj.asequal(expected_pagetitle,actual_pagetitle,'Step 4: Verify that the title got changed on the page tab and also in the properties section')
        
        """ 
        Step 5: Save and exit portal
        """
        time.sleep(2)
        vfour_ribbonobj.select_tool_menu_item('menu_Save')
        time.sleep(3)
        vfour_ribbonobj.select_tool_menu_item('menu_Exit')
        time.sleep(2)
        utillobj.switch_to_window(0)
        time.sleep(3)
        elem1=WfMainPageLocators.__dict__['banner_administrator']
        resultobj._validate_page(elem1)
        
        """ 
        Step 6: Sign Out from WebFOCUS
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()