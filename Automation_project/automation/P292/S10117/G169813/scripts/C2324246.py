'''
Created on Sep 28, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324246
TestCase Name = Run Mode_Run Users : Confirm_no_personalize_with_nonadmin_id_2
'''

import unittest, time
from common.lib import utillity
from common.pages import vfour_portal_ribbon, vfour_portal_run, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324246_TestClass(BaseTestCase):

    def test_C2324246(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """

        utillobj = utillity.UtillityMethods(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        user_id = utillobj.parseinitfile('mrid02')
        project_id = utillobj.parseinitfile('project_id')
        
        
        
        """    1. Go to http://machine:port/alias/portal/S10032/BIP_xxx_Portal123_V4    """
        """    2. On the WF sign in page, sign in as Domain Advanced user    """
        utillobj.invoke_bip_portal('BIP_V4_Portal/BIP_xxx_Portal123_V4','mrid02', 'mrpass02')
        time.sleep(1)
        element_css="[class*='banner-top'] > div[class*='menu-bar-item'][style*='inherit']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 190)
        time.sleep(3) 
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('Test_Page', 'Step 2a: Verify Test_Page tab existi')
        vfour_runobj.verify_number_of_portal_panel(5, "Step 02a(1): Verify number of panels in portal")
        
        panel_title=['Panel 1','Panel 2','Panel 3','Panel 4', 'Panel 5']
        css="div[id^='BiLabel'][class*='bip-title-bar pd-internal-id']"
        active_page=vfour_portal_canvas_obj.get_current_page()
        title_css=active_page.find_elements_by_css_selector(css)
        menu_list=[el.text.strip() for el in title_css]
        utillobj.asequal(panel_title, menu_list, "Step o2b(1): Verify panel title")
        vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out','Portals', 'Theme', 'Hidden Content'],msg='Step 02d(1): Verify portal menu bar')
        vfour_ribbonobj.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        

        
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('1 Column', 'Step 2b: Verify that the new page added at run time page by Domain Basic user not get displayed', False)
        
        """    2. Add another page (1 Column) and drag the 'P292' domain there.    """
        vfour_portal_canvas_obj.add_page('1 Column')
        time.sleep(5)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('1 Column', 'Step 3: Verify page - 1 Column added')
        time.sleep(5)
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas(project_id, 'column', 1)
        time.sleep(2)
        
        """verify Panel 1"""
        panel_obj=vfour_portal_canvas_obj.get_panel_obj('Panel 1')
        item_path="P292_S10117_G169813"
        panel_1_text_list = panel_obj.find_element_by_css_selector("table").text.strip().split('\n')
        utillobj.asin(item_path, panel_1_text_list, "Step 13.1: Verify that the folder is there with its contents")

        """    3. Sign Out from WebFOCUS    """
if __name__ == '__main__':
    unittest.main()        