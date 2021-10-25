"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Nasir

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/6670296
Test Case Title =  Portal Menu Defaults
-----------------------------------------------------------------------------------------------"""

import unittest
import pyautogui
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages.wf_mainpage import Wf_Mainpage as wf_home_page
from common.lib.utillity import UtillityMethods
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6670296_TestClass(BaseTestCase):
    
    def test_C6670296(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        wf_home_page_obj=wf_home_page(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_MAINMENU = ['Run', 'Edit', 'Customizations', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Open item location', 'Properties']
        EXPECTED_CUSTOMIZATION_SUBMENU=['Remove my customizations', 'Remove customizations for all users']
        EXPECTED_SECURITY_SUBMENU=['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...']
        CUSTOMIZATION_MENU_CSS = ".pop-top div[data-ibx-name*='miMenuItemMyCustomizations']"
        SECURITY_MENU_CSS = ".pop-top div[data-ibx-name='miMenuItemRules'][action='manageRulesOn']"
        crumbbox_css = ".crumb-box .ibx-label-text"
        
        """    1. Sign into WebFOCUS Home Page as Admin User    """
        wf_login.invoke_home_page('mrid', 'mrpass')
        
        """    2. Click Content View from the sidebar > Click on Domains from the resource tree    """
        utils.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        wf_home.select_option_from_crumb_box('Domains')
        
        """    3. Click on Portal View from the sidebar    """
        wf_home.select_portals_from_sidebar()
        utils.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
         
        """    4. Right click on 'Portal for Context Menu Testing'
        Verify that 'Portal for Context Menu Testing' context menu appears as same in the below screenshot    """
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME, EXPECTED_MAINMENU, msg="Step 4a")
        
        """    5. Hover over Customization menu
        Verify that Customization menu options appear as same in the below screenshot    """
        wf_home_page_obj.select_context_menu_item('Customizations')
        utils.synchronize_with_number_of_element(CUSTOMIZATION_MENU_CSS, 1, 5)
        wf_home_page_obj.verify_context_menu_item(EXPECTED_CUSTOMIZATION_SUBMENU, msg="Step 5a")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        
        """    6. Hover over Security Menu
        Verify that Security menu options appear as same in the below screenshot    """
        wf_home_page_obj.select_context_menu_item('Security')
        utils.synchronize_with_number_of_element(SECURITY_MENU_CSS, 1, 5)
        wf_home_page_obj.verify_context_menu_item(EXPECTED_SECURITY_SUBMENU, msg="Step 6a")
        
        """    7. In the banner link, click on the top right username > Click Sign Out.    """
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()