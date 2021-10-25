"""-------------------------------------------------------------------------------------------
Created on October 26, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261545
Test Case Title =  Portal Menu Defaults using Developers
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261545_TestClass(BaseTestCase):

    def test_C8261545(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        wf_home_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """

        EXPECTED_CONTEXT_MENU = ['Expand', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        EXPECTED_CUSTOMIZATIONS_SUB_MENU = ['Remove my customizations', 'Remove customizations for all users']
        EXPECTED_SECURITY_SUB_MENU = ['Rules on this resource...', 'Effective policy...', 'Owner...']
        ITEM_NAME = 'Portal for Context Menu Testing'
        FOLDER_PATH = 'P292_S19901->G513445'
      
      
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developers User
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            STEP 02 : Click Content View from the sidebar > Click on Domains from the resource tree 
        """
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        wf_home.click_repository_folder('Domains')
        
        """
            STEP 03 : If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
            STEP 04 : Right click on "Portal for Context Menu Testing" from the Resource Tree
        """
        wf_home.expand_repository_folder(FOLDER_PATH)
        
        """
            STEP 04.1 : Verify that context menu appears as same in the below screenshot
        """
        wf_home_page.verify_repository_folder_context_menu(ITEM_NAME, EXPECTED_CONTEXT_MENU, msg='Step 04.1 ', verification_state='collapse')
    
        """
            STEP 05 : Hover over Customization menu
            STEP 05.1 : Verify that context menu options for Customization appear as same in the below screenshot
        """
        wf_home_page.verify_repository_folder_context_submenu(ITEM_NAME, 'Customizations', EXPECTED_CUSTOMIZATIONS_SUB_MENU, msg='Step 05.1', verification_state='collapse')
        
        """
            STEP 06 : Hover over Security Menu
            STEP 06.1 : Verify that context menu options Security appear as same in the below screenshot
        """
        wf_home_page.verify_repository_folder_context_submenu(ITEM_NAME, 'Security', EXPECTED_SECURITY_SUB_MENU, msg='Step 06.1', verification_state='collapse')
        
        """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        