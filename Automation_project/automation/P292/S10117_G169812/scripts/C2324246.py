'''
Created on Sep 28, 2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324246
TestCase Name = Run Mode_Run Users : Confirm_no_personalize_with_nonadmin_id_2
'''

import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.pages import visualization_resultarea, vfour_portal_ribbon, vfour_portal_run, vfour_portal_canvas
from common.lib.basetestcase import BaseTestCase

class C2324246_TestClass(BaseTestCase):

    def test_C2324246(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        parent_css="[class*='bip-page'][style*='inherit']"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_runobj = vfour_portal_run.Vfour_Portal_Run(self.driver)
        vfour_portal_canvas_obj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        
        """    1. Go to http://machine:port/alias/portal/S10032/BIP_xxx_Portal123_V4    """
        """    2. On the WF sign in page, sign in as Domain Advanced user    """
        #utillobj.run_biportal('BIP_V4_Portal/BIP_xxx_Portal123_V4','mrid02', 'mrpass02')
        utillobj.invoke_bip_portal('BIP_V4_Portal/BIP_xxx_Portal123_V4','mrid02', 'mrpass02')
        time.sleep(15)
        driver.implicitly_wait(1)
        elem1=(By.CSS_SELECTOR, "[class*='banner-top'] > div[class*='menu-bar-item'][style*='inherit']")
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(3) 
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('Test_Page', 'Step 2a: Verify Test_Page tab existi')
        
        total_panel=len(driver.find_elements_by_css_selector(parent_css+" div[id^='BiLabel'][class*='bip-title-bar pd-internal-id']"))
        actual_panel=int(total_panel)
        print(actual_panel)
        utillobj.asequal(5, actual_panel, "Step 02a(1): Verify number of panels in portal")
        
        panel_title=['Panel 1','Panel 2','Panel 3','Panel 4', 'Panel 5']
        css=parent_css+" div[id^='BiLabel'][class*='bip-title-bar pd-internal-id']"
        title_css=driver.find_elements_by_css_selector(css)
        menu_list=[el.text.strip() for el in title_css]
        print(menu_list)
        utillobj.asequal(panel_title, menu_list, "Step o2b(1): Verify panel title")
        #background_image=driver.find_element_by_css_selector(parent_css).value_of_css_property('background-image')
        #utillobj.asin('honda_integra', background_image, 'Step 02c(1): Verify background image applied')
        user_id = utillobj.parseinitfile('mrid02')
        vfour_runobj.select_or_verify_portal_menu_bar_item(verify=[user_id, 'Tools', 'Resources', 'Help', 'Close', 'Sign Out','Portals', 'Theme', 'Hidden Content'],msg='Step 02d(1): Verify portal menu bar')
        vfour_ribbonobj.verify_menu_bar_style(menu_item_font_name='Arial', menu_item_font_size=9, menu_item_bold=True, menu_item_italic=True, 
                                                     menu_item_underline=True, border_width=4, menu_item_text_color='blue',
                                                     border_color='red', border_style='solid', menubar_background='yellow')
        

        
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('1 Column', 'Step 2b: Verify that the new page added at run time page by Domain Basic user not get displayed', False)
        
        """    3. Add another page (1 Column) and drag the 'P292' domain there.    """
        vfour_portal_canvas_obj.add_page('1 Column')
        time.sleep(5)
        vfour_portal_canvas_obj.verify_page_in_navigation_bar('1 Column', 'Step 3: Verify page - 1 Column added')
        time.sleep(5)
        vfour_portal_canvas_obj.dragdrop_repository_item_to_canvas('P292', 'column', 1)
        time.sleep(2)
        
        """verify Panel 1"""
        panel_obj=vfour_portal_canvas_obj.get_panel_obj('Panel 1')
        utillobj.verify_object_visible('dummy', True, 'Step 03a: Verify P292 Folder visible in Panel 1', elem_obj=panel_obj)
        status=False
        Retail_elem=panel_obj.find_elements_by_css_selector("div[id^='BidFolderBlockTree'] table>tbody>tr")
        for elem in Retail_elem:
            if elem.text.strip() == "S10117":
                status=True
                break
        utillobj.verify_object_visible(elem, status, 'Step 03b: Verify P292 Folder listed in Panel 5', elem_obj=elem)
        
        """    3. Sign Out from WebFOCUS    """
if __name__ == '__main__':
    unittest.main()        