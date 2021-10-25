'''
Created on November 13, 2018
@author: Prabhakaran
Testcase Name : Check Share Tooltip before sharing personal pages
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779089
'''

import unittest
from common.wftools.login import Login
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.designer_portal import Two_Level_Side

class C6779789_TestClass(BaseTestCase):
    
    def test_C6779789(self):
        
        """
        CLASS OBJECTS
        """
        wf_login = Login(self.driver)
        wf_home = Wf_Mainpage(self.driver)
        two_level_portal = Two_Level_Side(self.driver)
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """
        COMMAND VARIABLES
        """
        LONG_WAIT_TIME = 120
        PORTAL_NAME = 'V5 Portal Share'
        EXPECTED_PANELS_TITLE = ['Panel 1', 'Panel 2', 'Panel 3']
        
        """
            STEP 01 : Sign in to WebFOCUS as Developer user.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(".left-main-panel .left-main-panel-content-button", 'Content', LONG_WAIT_TIME)
        
        """
            STEP 02 : Click on Content View from the sidebar and Click on Domain from the resource tree
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 03 : Expand the domain from the tree and click on 'P292_S19901_G520454'.
            STEP 04 : Right click on 'V5 Portal Share' from the content area > Run.
        """
        wf_home.right_click_folder_item_and_select_menu(PORTAL_NAME, 'Run', 'P292_S19901_G520454')
        coreutils.switch_to_new_window()
        utils.synchronize_with_visble_text(".pd-container-title", 'Panel 1', LONG_WAIT_TIME)
        
        """
            STEP 04.1 : Verify the page is loaded with 3 panels and each has a + sign inside of them 
            and the personal page toolbar has Share (By default it is in grey color),refresh and delete buttons.
        """
        two_level_portal.verify_page_header_title('Page Heading', 'Step 04.01 : Verify page heading')
        two_level_portal.verify_all_containers_title(EXPECTED_PANELS_TITLE, 'Step 04.02 : Verify the page is loaded with 3 panels')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[0], 'Step 04.03 : Verify Panel 1 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[1], 'Step 04.04 : Verify Panel 2 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[2], 'Step 04.05 : Verify Panel 3 has a + sign')
        two_level_portal.verify_page_header_all_buttons(['Share', 'Refresh', 'Delete'], "Step 04.06 : Verify page toolbar has 'Share', 'Refresh', 'Delete' buttons")
        two_level_portal.verify_page_header_button_color('Share', 'Step 04.07 : Verify Share button displayed in grey color')
        
        """
            STEP 05 : Hover the mouse to the Share button in the personal page toolbar.
            STEP 05.1 : Verify the tooltip shows 'Share'.
        """
        two_level_portal.verify_page_header_button_tooltip("Share", "Step 05.01 : Verify the tooltip shows 'Share'")
        
        """
            STEP 06 : Close the portal run window.
        """
        coreutils.switch_to_previous_window()
        
        """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()