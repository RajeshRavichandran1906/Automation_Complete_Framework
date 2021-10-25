'''
Created on October 24, 2018

@author: Raghunath
Testcase Name : Portal Menu Defaults using Basic User
Testcase ID : 172.19.2.180/testrail/index.php?/cases/view/6670304
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators


class C6670304_TestClass(BaseTestCase):
    
    def test_C6670304(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        breadcrumb_path="P292_S19901->G513445"
        expected_folder_contentarea=['Portal for Context Menu Testing']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        
        main_page_obj.expand_repository_folder(breadcrumb_path)
        main_page_obj.verify_items_in_grid_view(expected_folder_contentarea, 'asin',"Step 3:Verify user sees 'Portal for Context Menu Testing' folder.")
        util_obj.verify_picture_using_sikuli("portal_item.png", "Step03: Verify that 'Portal for Context Menu Testing' displayed as an item and NOT a folder from the content area")  
        
        
        """
        Step 4: Right click on 'Portal for Context Menu ...'. 
        """
        verify_list = [ 'Run', 'Remove my customizations', 'Add to Favorites', 'Properties']
        main_page_obj.verify_repository_folder_item_context_menu('Portal for Context Menu Testing', verify_list, msg='Step 4:Verify the options are displayed')  

        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

        
if __name__ == '__main__':
    unittest.main()
    
        