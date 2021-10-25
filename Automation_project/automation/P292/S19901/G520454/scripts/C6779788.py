'''
Created on December 06, 2018
@author: Prabhakaran
Testcase Name : Verify Share button on the personal page toolbar
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779788
'''

import unittest
from common.wftools.login import Login
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.designer_portal import Two_Level_Side

class C6779788_TestClass(BaseTestCase):
    
    def test_C6779788(self):
        
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
        MIDIUM_WAIT_TIME = 30
        SHORT_WAIT_TIME = 10
        EXPECTED_PAGE_TEMPLATES = ['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        PORTAL_NAME = 'V5 Portal Share'
        EXPECTED_PANELS_TITLE = ['Panel 1', 'Panel 2', 'Panel 3']
        PAGE_FOLDER = 'My Pages'
        
        """
            STEP 01 : Sign in to WebFOCUS as Developer user
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(".left-main-panel .left-main-panel-content-button", 'Content', LONG_WAIT_TIME)
        
        """
            STEP 02 : Click on Content View from the sidebar and Click on Domain from the resource tree
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 03 : Expand the domain from the tree > click on 'P292_S19901_G520454'
            STEP 04 : Right click on 'V5 Portal Share' from the content area > Run
        """
        wf_home.right_click_folder_item_and_select_menu(PORTAL_NAME, 'Run', 'P292_S19901_G520454')
        coreutils.switch_to_new_window()
        coreutils.update_current_working_area_browser_specification()
        utils.synchronize_with_visble_text("div.pvd-canvas-container", 'There are no pages available', MIDIUM_WAIT_TIME)
        
        """
            STEP 04.1 : Verify 'V5 Portal Share' run in a new window and you see a sidebar with My Pages and a + sign under it.
        """
        two_level_portal.verify_folders_in_left_sidebar([PAGE_FOLDER], 'Step 04.01 : Verify new portal open with My Pages folder')
        two_level_portal.verify_pages_under_the_folder_in_left_sidebar(PAGE_FOLDER, ['+'], "Step 04.02 : Verify 'V5 Portal Share' run in a new window and you see a sidebar with My Pages and a + sign under it")
        
        """
            STEP 05 : Click the + sign
        """
        two_level_portal.click_on_plus_icon_under_the_folder_in_left_sidebar(PAGE_FOLDER)
        utils.synchronize_with_visble_text("div.new-page-from-template", 'New Page', SHORT_WAIT_TIME)
        
        """
            STEP 05.1 : Verify you see 4-page templates (Grid 2-1, Grid 2-1 side, Grid 3-3-3, and Grid 4-2-1)
        """
        two_level_portal.verify_new_page_templates(EXPECTED_PAGE_TEMPLATES, 'Step 05.01 : Verify you see 4-page templates (Grid 2-1, Grid 2-1 side, Grid 3-3-3, and Grid 4-2-1)')
        
        """
            Step 06 : Choose Grid 2-1 template 
        """
        two_level_portal.select_new_page_template('Grid 2-1')
        utils.synchronize_with_visble_text(".pd-container-title", 'Panel 1', SHORT_WAIT_TIME)
        
        """
            STEP 06.1 : Verify the page is loaded with 3 panels and each has a + sign inside of them and 
            the personal page toolbar has Share (By default it is in grey color), refresh and delete buttons
        """
        two_level_portal.verify_page_header_title('Page Heading', 'Step 06.01 : Verify page heading')
        two_level_portal.verify_all_containers_title(EXPECTED_PANELS_TITLE, 'Step 06.02 : Verify the page is loaded with 3 panels')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[0], 'Step 06.03 : Verify Panel 1 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[1], 'Step 06.04 : Verify Panel 2 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[2], 'Step 06.05 : Verify Panel 3 has a + sign')
        two_level_portal.verify_page_header_all_buttons(['Share', 'Refresh', 'Delete'], "Step 06.06 : Verify page toolbar has 'Share', 'Refresh', 'Delete' buttons")
        two_level_portal.verify_page_header_button_color('Share', 'Step 06.07 : Verify Share button displayed in grey color')
        
        """
            STEP 07 : Close the portal run window
        """
        coreutils.switch_to_previous_window()
        
        """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()