"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986642
Test Case Title =  Portal Menu Defaults using Basic User
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.utillity import UtillityMethods

class C6986642_TestClass(BaseTestCase):

    def test_C6986642(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_CONTEXT_MENU = ['Run', 'Remove from Favorites', 'Properties']
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Basic User
        """
        wf_login.invoke_home_page('mridbas', 'mrpassbas')
        utils.synchronize_with_visble_text("div[title^='Content']", 'Content', 80)
        
        """
            STEP 02 : Click Content View from the sidebar > Click on Domains from the resource tree
        """
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_visble_text("div[title='Domains']", 'Domains', 10)
        
        """
            STEP 03 : Click on Portal View from the sidebar
        """
        wf_home.select_portals_from_sidebar()
        utils.synchronize_with_visble_text("div[title='Portals']", 'Portals', 10)
        
        """
            STEP 04 : Right click on 'Portal for Context Menu Testing' > Click Add to Favorites
        """
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME, 'Add to Favorites')
        
        """
            STEP 04.1 : Verify that Favorite added popup opens with a background transparent green layer over the popup.
        """
        wf_home.verify_favorites_notify_popup('Step 04.01 ')
        
        """
            STEP 05 : Click on Favorite View from the sidebar
        """
        wf_home.select_favorites_from_sidebar()
        utils.synchronize_with_visble_text("div[title='Favorites']", 'Favorites', 10)
        
        """
            STEP 05.1 : Verify that added 'Portal for Context Menu T...' portal appears in the favorites
        """
        wf_home.verify_items_in_grid_view([ITEM_NAME], 'asin', 'Step 05.01 :')
        
        """
            STEP 06 : Right click on 'Portal for Context Menu T...'
            STEP 06.1 : Verify that 'Run', 'Remove from Favorites', and 'Properties' context menus are displayed
        """
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME, EXPECTED_CONTEXT_MENU, msg = 'Step 06.01')
        
        """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        