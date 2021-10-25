'''
Created on Sep 23, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324222
TestCase Name = Portal Designer_Designer Properties : Modify_Menubar_Links_And_Save_and_Exit_Portal
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, wf_mainpage, vfour_portal_ribbon, vfour_portal_properties, wf_legacymainpage
from common.lib.basetestcase import BaseTestCase

class C2324222_TestClass(BaseTestCase):

    def test_C2324222(self):
        driver = self.driver #Driver reference object created
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        if utillobj.parseinitfile('nodeid') in ('wfinst01','wfinst02','wfinst03','wfinst05'):
            wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        else:
            wf_mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        vfour_ribbonobj = vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        portal_properties = vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        proj_id = utillobj.parseinitfile('project_id')
        suite_id = utillobj.parseinitfile('suite_id')
        parent_folder_name='BIP_V4_Portal'
        BIP_Portal_Path = str(proj_id)+'->'+str(suite_id)+'->'+parent_folder_name
        welcome_page_parent_css = "#PortalResourcevBOX table tr td"
        edit_page_parent_css = "#applicationButtonBox img[src*='bip_button']"
        
        """
        Step 01: Sign in as WF Developer
        """
        utillobj.invoke_webfocu('mrid03', 'mrpass03')
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)      

        """
        Step 02: Edit 'BIP_xxx_Portal123_V4' portal
        """
        wf_mainobj.select_repository_menu('P292->S10117->BIP_V4_Portal->BIP_xxx_Portal123_V4', 'Edit')
        utillobj.switch_to_window(1)
        utillobj.synchronize_with_number_of_element(edit_page_parent_css, 1, 50)
         
        """ 
        Step 3: Select MenuBar links area;
        """
        time.sleep(3)
        parent_css= "[class*='banner-top'] > div[class*='menu-bar']"
        resultobj.wait_for_property(parent_css, 1)
        vfour_ribbonobj.select_or_verify_menu_bar(select=True)
         
        """ 
        Step 4: From properties window, change Max items from the default 7 to 13.
        """
        time.sleep(3)
        portal_properties.edit_input_control('menu', 'Max Items', 'textbox', textbox_input=13)
         
        """ 
        Step 5: Move all items from available items to the selected items one by one. 
        """
        time.sleep(3)
        portal_properties.edit_input_control('menu', 'Language', 'menu_area', add=True)
         
        """Verify all the menubar links are available in portal design mode."""
        time.sleep(3)
        user_id = utillobj.parseinitfile('mrid03')
        print(user_id)
        browser=utillobj.parseinitfile('browser')
        if browser == 'IE':
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=[user_id, 'Tools', 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step5: Verify portal menu bar')
        else:
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=[user_id, 'Tools', 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step5: Verify portal menu bar')
        """ 
        Step 6: Modify the listing of the links by moving them around. click on each menu item and use the Blue arrows by selected to list them all as this checkpoint
        """
        time.sleep(3)
        portal_properties.edit_input_control('menu', 'Userid', 'sort_menu', down=True)
        if browser == 'IE':
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=['Tools', user_id, 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step6a: Verify portal menu bar')
        else:
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=['Tools', user_id, 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step6a: Verify portal menu bar')
         
        time.sleep(3)
        portal_properties.edit_input_control('menu', 'Tools', 'sort_menu', down=True)
        if browser == 'IE':
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=[user_id, 'Tools', 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step6b: Verify portal menu bar')
        else:
            vfour_ribbonobj.select_or_verify_menu_bar(menu_list=[user_id, 'Tools', 'Administration', 'Resources', 'Help', 'Close', 'Sign Out', 'Language', 'Portals', 'Enable Accessibility', 'Theme', 'Hidden Content'],msg='Step6b: Verify portal menu bar')
         
        """ 
        Step 7: Click Save button in toolbar; Click BIP application menu and exit the portal.
        """
        vfour_ribbonobj.bip_save_and_exit('Yes')
        utillobj.switch_to_window(0, pause=9)
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        time.sleep(1)
        
        """
        Step 08: Refresh the browser. Expand P292 domain -> S10117 folder
        Verify that the portal appears under the folder.
        """
        driver.refresh() 
        utillobj.synchronize_with_visble_text(welcome_page_parent_css, 'Domains', 50)
        time.sleep(1)
        wf_mainobj.get_repository_item_availability(BIP_Portal_Path+'->BIP_xxx_Portal123_V4')
        time.sleep(2)
        
        """ 
        Step 09: Open the resource folder. Verify that the Page_New is there.
        """
        wf_mainobj.get_repository_item_availability(BIP_Portal_Path+'->BIP_xxx_Portal123_V4 Resources->Page_New')
        time.sleep(2)
        
        """ 
        Step 10: Sign Out from WebFOCUS
        """
        
if __name__ == '__main__':
    unittest.main()