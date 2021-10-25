'''
Created on Sep 11, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324244
TestCase Name = Run Mode : Run_the_Portal
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, vfour_portal_ribbon, vfour_portal_run, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324244_TestClass(BaseTestCase):

    def test_C2324244(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2324244'
        parent_css="[class*='bip-page'][style*='inherit']"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
        """    1. Go to http://machine:port/alias/portal/S10032/BIP_xxx_Portal123_V4    """
        """    2. On the sign in page, sign in as Domain Basic user    """
        utillobj.invoke_bip_portal('BIP_V4_Portal/BIP_xxx_Portal123_V4','mrid01', 'mrpass01')
        time.sleep(15)
        driver.implicitly_wait(1)
        elem1=(By.CSS_SELECTOR, "[class*='banner-top'] > div[class*='menu-bar-item'][style*='inherit']")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(3)
        
        """    Verify the portal appears with no errors.   """
        total_panel=len(driver.find_elements_by_css_selector(parent_css+" div[id^='BiLabel'][class*='bip-title-bar pd-internal-id']"))
        actual_panel=int(total_panel)
        print(actual_panel)
        utillobj.asequal(5, actual_panel, "Step 02a: Verify number of panels in portal")
        
        panel_title=['Panel 1','Panel 2','Panel 3','Panel 4', 'Panel 5']
        css=parent_css+" div[id^='BiLabel'][class*='bip-title-bar pd-internal-id']"
        title_css=driver.find_elements_by_css_selector(css)
        menu_list=[el.text.strip() for el in title_css]
        print(menu_list)
        utillobj.asequal(panel_title, menu_list, "Step o2b: Verify panel title")
        #background_image=driver.find_element_by_css_selector(parent_css).value_of_css_property('background-image')
        #print(background_image)
        #utillobj.asin('honda_integra', background_image, 'Step 02c: Verify background image applied')
        user_id = utillobj.parseinitfile('mrid01')
        vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out','Portals', 'Theme', 'Hidden Content'],msg='Step 02d: Verify portal menu bar')
        vfour_ribbonobj.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        
        """verify Panel 1"""
        panel_obj=vfour_portal_canvas_obj.get_panel_obj('Panel 1')
        panel_elem=panel_obj.find_element_by_css_selector("#treeView tbody>tr>td>img[src*='discovery_domain']")
        utillobj.verify_object_visible('dummy', True, 'Step 02e: Verify Resouce Tree visible in Panel 1', elem_obj=panel_elem)
        
        """verify Panel 2"""
        vfour_portal_canvas_obj.verify_panel_portal_list('Panel 2', 'BIP_xxx_Portal123_V4', "Step 02f: Verify Portal list visible")
        
        """verify Panel 3"""
        vfour_portal_canvas_obj.verify_panel_text('Panel 3', 'testing text panel area', 'Step 02g: Verify text input in Panel 3')
        
        """verify Panel 4"""
        vfour_portal_canvas_obj.verify_panel_image('Panel 4', 'babydeer', 'Step 02h: Verify image in Panel 4')
        
        """verify Panel 5"""
        panel_obj=vfour_portal_canvas_obj.get_panel_obj('Panel 5')
        panel_elem_list=panel_obj.find_elements_by_css_selector("div[id^='BidFolderBlockTree'] table>tbody>tr")
        status=False
        for item in panel_elem_list:
            if item.text.strip() == "Portal":
                status=True
                break
        utillobj.verify_object_visible(item, status, 'Step 02i: Verify Retail Samples Folder visible in Panel 5', elem_obj=item)
        utillity.UtillityMethods.asequal(self, True, status, 'Step 021: Verify Retail Samples Folder in Panel 5')
        
if __name__ == '__main__':
    unittest.main()        