'''
Created on October 26, 2018

@author: Robert
Testcase Name : Portal Menu Defaults using Advanced User 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6670307
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity

class C6670307_TestClass(BaseTestCase):
    
    def test_C6670307(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_box_css = ".crumb-box .ibx-label-text"
        ibi_logo_css="div[class^='home-banner ibx-widget'] div.banner-logo"
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_CONTEXT_MENU=['Run', 'Remove from Favorites', 'Properties']
        """
        Step 1. Sign into WebFOCUS Home Page as Developers User
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        util_obj.synchronize_with_number_of_element(ibi_logo_css, 1, 40, 1)
        
        """
        Step 2. Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(crumb_box_css, 'Domains', 30, 1)
        main_page_obj.select_option_from_crumb_box("Domains")
        
        """
        Step 3. Click on Portal View from the sidebar
        """
        util_obj.synchronize_with_number_of_element("#files-box-area", 1, 30, 1)
        
        main_page_obj.select_portals_from_sidebar()
        
        """
        Step 4. Right click on 'Portal for Context Menu Testing' > Click Add to Favorites
        """
        util_obj.synchronize_with_visble_text(crumb_box_css, 'Portals', 30, 1)
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Add to Favorites')
        
        main_page_obj.verify_favorites_notify_popup('Step 4.1. Verify favorite added popup and its color')
        
        """
        Step 5. Click on Favorite View from the sidebar
        """
        
        main_page_obj.select_favorites_from_sidebar()
        
        util_obj.synchronize_with_visble_text(crumb_box_css, 'Favorites', 30, 1)
        
        """
        Step 5.1. Verify that added 'Portal for Context Menu T...' portal appears in the favorites
        """
        main_page_obj.verify_items_in_grid_view([ITEM_NAME], 'asin', 'Step 05.01 :')
        
        """
        Step 6. 1. Right click on 'Portal for Context Menu T...'
          
        """
        main_page_obj.verify_repository_folder_item_context_menu(ITEM_NAME, EXPECTED_CONTEXT_MENU, msg = 'Step 06.01')
        
        """
        Step 7. In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        