'''
Created on October 24, 2018

@author: vpriya
Testcase Name : Portal Menu Defaults using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261532
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261532_TestClass(BaseTestCase):
    
    def test_C8261532(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        breadcrumb_path="P292_S19901->G513445"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.click_repository_folder('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, "Portal for Context Menu Testing", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Right click on 'Portal for Context Menu ...'. 
        """
        verify_list = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        main_page_obj.verify_repository_folder_item_context_menu('Portal for Context Menu Testing', verify_list, msg='Step 4: Verify that following options are displayed')
        
        """
        Step 5: Hover over Customization menu ...'. 
        Verify that Customization options are displayed as per in the screenshot
        
        Step 6:Hover over Security Menu
        Verify that Security options are displayed as per in the screenshot
        """
        main_page_obj.verify_repository_folder_item_context_submenu('Portal for Context Menu Testing','Customizations',['Remove my customizations', 'Remove customizations for all users'],msg="Step6.1 : Verify that the following options are displayed under Customizations.")
        main_page_obj.verify_repository_folder_item_context_submenu('Portal for Context Menu Testing','Security', ['Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step6.2 : Verify that the following options are displayed under Security.")
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        