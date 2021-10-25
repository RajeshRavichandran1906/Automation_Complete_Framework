'''
Created on October 25, 2018

@author: Raghunath
Testcase Name : Portal Menu Defaults
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6670291
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6670291_TestClass(BaseTestCase):
    
    def test_C6670291(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        breadcrumb_path="Domains->P292_S19901->G513445"
        expected_folder_contentarea=['Portal for Context Menu Testing']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        main_page_obj.verify_folders_in_grid_view(expected_folder_contentarea, 'asin',"Step 3:Verify user sees 'Portal for Context Menu Testing' folder.")
        
        """
        Step 4: Right click on "Portal for Context Menu Testing" from the Resource Tree ...'. 
        """
        folder='Portal for Context Menu Testing'        
        verify_list = ['Expand', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        main_page_obj.verify_repository_folder_context_menu(folder, verify_list, msg='Step 4: Verify that following options are displayed', verification_state='collapse')
        
        """
        Step 5: Hover over Customization menu ...'. 
        """
        main_page_obj.verify_repository_folder_context_submenu('Portal for Context Menu Testing','Customizations',['Remove my customizations', 'Remove customizations for all users'], msg="Step5 : Verify that the following options are displayed under Customizations.")
        
        """
        Step 6: Hover over Security Menu ...'. 
        """ 
        main_page_obj.verify_repository_folder_context_submenu('Portal for Context Menu Testing','Security',['Rules...','Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step6 : Verify that context menu options Security appear as same in the below screenshot.")
         
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    
        