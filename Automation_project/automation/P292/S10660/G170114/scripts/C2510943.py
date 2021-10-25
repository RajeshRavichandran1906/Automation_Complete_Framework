"""-------------------------------------------------------------------------------------------
Created on October 23, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2510943
Test Case Title =  Verify Open item location for Portals W/ Dev user
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C2510943_TestClass(BaseTestCase):

    def test_C2510943(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        ITEM_NAME1 = 'Retail Samples'
        ITEM_NAME2 = 'Demo Videos'
        EXPECTED_ITEM_CONTEXT_MENU = ['Open item location']
        EXPECTED_CRUMB_BOX_TEXT = 'Domains->Retail Samples->Portal'
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            STEP 02 : Click Portals from the sidebar. 
        """
        wf_home.select_portals_from_sidebar()
        
        """
            STEP 03 : Right click on 'Retail Samples' V3 Portal
            STEP 03.1 : Verify 'Open item location' is not available. 
        """
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME1, EXPECTED_ITEM_CONTEXT_MENU, msg='Step 03', comparision_type='asnotin')
        element_obj = self.driver.find_element_by_css_selector(".files-box-files .content-title-label")
        core_utils.left_click(element_obj)
        
        """
            STEP 04 : Right click on 'Retail Samples' V4 portal.
            STEP 04.1 : Verify 'Open item location' is available.
        """
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME1, EXPECTED_ITEM_CONTEXT_MENU, msg='Step 03', comparision_type='asin', item_name_index=2)
        
        """
            STEP 05 : Click 'Open item location' 
        """
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME1, 'Open item location', item_name_index=2)
        utils.synchronize_with_visble_text(".files-box-files [data-ibxp-text^='Items']", 'Items', 10)
        
        """
            STEP 05.1 : Verify that you are on the content view and in the folder where the portal resides.
        """
        wf_home.verify_crumb_box(EXPECTED_CRUMB_BOX_TEXT, 'Step 05.1 ')
        wf_home.verify_repository_folder_icon_plus_minus('Portal', 'collapse', 'Step 05.2 : Verify that you are on the content view and in the folder where the portal resides')
        
        """
            STEP 06 : Click Content from the sidebar and click on 'Retail Samples' under Domains.
            STEP 07 : Right click on 'Demo Videos' > Add to Favorites and again right click on 'Demo Videos' > Add to Mobile Favorites. 
        """
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME2, context_menu_item_path='Add to Favorites', folder_path='Retail Samples')
        wf_home.right_click_folder_item_and_select_menu(ITEM_NAME2, context_menu_item_path='Add to Mobile Favorites')
        
        """
            STEP 08 : Click Favorites from the sidebar.Right click on 'Demo Videos'.
            STEP 08.1 : Verify that 'Open item location' is not available.
        """
        wf_home.select_favorites_from_sidebar()
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME2, EXPECTED_ITEM_CONTEXT_MENU, msg='Step 08', comparision_type='asnotin')
        
        """
            STEP 09 : Click Mobile Favorites from the sidebar.Right click on 'Demo Videos'.
            STEP 09.1 : Verify that 'Open item location' is not available.
        """
        wf_home.select_mobilefavorites_from_sidebar()
        wf_home.verify_repository_folder_item_context_menu(ITEM_NAME2, EXPECTED_ITEM_CONTEXT_MENU, msg='Step 09', comparision_type='asnotin')
        
        """
            STEP 10 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        