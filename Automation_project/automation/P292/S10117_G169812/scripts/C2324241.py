'''
Created on Sep 18, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324241
TestCase Name = Run Mode_Run Content : Run_Portal_Verify_changes_and_Close
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_run, vfour_portal_canvas, wf_legacymainpage, vfour_portal_ribbon
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
import pyautogui

class C2324241_TestClass(BaseTestCase):

    def test_C2324241(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        v4p_ribbon=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        vfour_canvasobj = vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
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
        Step 02: Right click on portal 'BIP_xxx_Portal123_V4' and run the portal; 
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Run')
        time.sleep(4)
        elem1=(By.CSS_SELECTOR, "#BIPortalPanel")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        
        """
        Step 02.1: Verify the recent changes made in the portal edit mode is available in run mode;
        """
        vfour_canvasobj.verify_page_in_navigation_bar('Test_Page', "Step 2: Verify Test_Page in Navigation Bar.")
        vfour_runobj.verify_number_of_portal_panel(4, "Step2.a:")
        vfour_runobj.verify_portal_panel_label(['Panel 1','Panel 2','Panel 3','Panel 4'], "Step2.b:")
        user_id = utillobj.parseinitfile('mrid03')
        print(user_id)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Enable Accessibility', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        else:
            vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out', 'Portals', 'Theme', 'Hidden Content'],msg='Step2.b: Verify portal menu bar')
        
        v4p_ribbon.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        
        
        """verify Panel 1"""
        utillobj.verify_object_visible("div[id^='BidTreeBlock'][class*='bi-component']", True, 'Step 2.d: Panel1 Visible')
        utillobj.verify_object_visible("#treeView tbody>tr>td>img[src*='discovery_domain']", True, 'Step 2.e: Panel Domain tree Visible')
        """verify Panel 2"""
        utillobj.verify_object_visible("div[id^='BipContentArea'][class*='bi-component bip-panel-pane'] div[id^='BipPortalTree']", True, 'Step 2.f: Panel2 portal list Visible')
        """verify Panel 3"""
        utillobj.verify_object_visible("textarea[class*='bi-text-field text-field bip-panel-pane']", True, 'Step 2.g: Panel3 textarea Visible')
        """verify Panel 4"""
        utillobj.verify_object_visible("div[id^='BipContentArea'][class*='bi-component bip-panel-pane'] img[src*='babydeer']", True, 'Step 2.h: Panel4 babydeer Visible')
        
        """
        Step 03: Open the 'BIP_xxx_Portal123_V4' portal's resource folder.
        Step 04: Drag a page onto the page canvas
        """
        target_elem = driver.find_element_by_css_selector("#BIPortalPanel")
        self.drag_portal_resource_tree('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4 Resources->Test_Page', target_elem, ty_offset=70, mouse_duration=1)
        utillobj.click_on_screen(target_elem, 'middle', y_offset=75)
        
        """
        Verify that you get the no drop icon.
        """
        utillobj.verify_object_visible("img[id^='BiImage'][class*='bi-component'][src*='nodrop']", True, 'Step 04: Verify that you get the no drop icon')
        time.sleep(3)
        ele=driver.find_element_by_css_selector("#BIPortalPanel")
        utillobj.take_screenshot(ele,'C2324241_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        target_obj=utillobj.get_object_screen_coordinate(target_elem, coordinate_type='middle')
        target_obj_x=target_obj['x']
        target_obj_y=target_obj['y']
        pyautogui.mouseUp(target_obj_x, target_obj_y)
        time.sleep(2)
         
        """
        Step 05: Close the portal run mode.
        """
        vfour_runobj.select_or_verify_portal_menu_bar_item(select='Close')
        time.sleep(2)
        
        """
        Step 06: Sign Out from WebFOCUS
        """
    
    def drag_portal_resource_tree(self, folder_path, target_elem, **kwargs):
        driver = self.driver
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        vfour_runobj.expand_portal_resource_tree(folder_path)
        BIPtree_rows="div[id^='BipContentArea'] #treeView table>tbody>tr"
        item_name=folder_path.split('->')[-1]
        rows = driver.find_elements_by_css_selector(BIPtree_rows)
        for i in range(len(rows)):
            td_item = BIPtree_rows + ":nth-child(" + str(i+1) + ")>td"
            get_td_text=driver.find_element_by_css_selector(td_item).text
            if get_td_text == item_name:
                td_img = driver.find_element_by_css_selector(td_item + ">img.icon")
                self.driver.execute_script("arguments[0].scrollIntoView(true);", td_img)
                td_img.click()
                utillobj.click_on_screen(td_img, 'middle', click_type=0)
                time.sleep(2)
#                 utillobj.drag_to_using_pyautogui(td_img, target_elem, **kwargs)
                cord_type=kwargs['cord_type'] if 'cord_type' in kwargs else 'middle' 
                source_offset_x=kwargs['sx_offset'] if 'sx_offset' in kwargs else 0
                source_offset_y=kwargs['sy_offset'] if 'sy_offset' in kwargs else 0
                target_offset_x=kwargs['tx_offset'] if 'tx_offset' in kwargs else 0
                target_offset_y=kwargs['ty_offset'] if 'ty_offset' in kwargs else 0
                pyautogui.FAILSAFE=False  
                source_obj=utillobj.get_object_screen_coordinate(td_img, coordinate_type=cord_type, x_offset=source_offset_x, y_offset=source_offset_y)
                source_obj_x=source_obj['x']
                source_obj_y=source_obj['y']
                target_obj=utillobj.get_object_screen_coordinate(target_elem, coordinate_type=cord_type, x_offset=target_offset_x, y_offset=target_offset_y)
                target_obj_x=target_obj['x']
                target_obj_y=target_obj['y']
                time.sleep(2)
                pyautogui.mouseDown(source_obj_x,source_obj_y)
                time.sleep(15)
                pyautogui.moveTo(target_obj_x, target_obj_y)
                time.sleep(2)
        #         pyautogui.mouseUp(target_obj_x, target_obj_y)
        
                                
if __name__ == '__main__':
    unittest.main()