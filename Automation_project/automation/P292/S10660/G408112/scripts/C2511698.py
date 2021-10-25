'''
Created on Aug 9, 2019

@author: Aftab

Test Case Link  -  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511698
Test Case Title -  Verify the ability to navigate through the Tree
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.locators import wf_mainpage_locators
from common.lib.utillity import UtillityMethods

class C2511698_TestClass(BaseTestCase):

    def test_C2511698(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        utils = UtillityMethods(self.driver)
        
        '''
        Step 1 : Sign into WebFOCUS Home Page as Admin User.
                 Homepage will be launched properly.
        '''
        login.invoke_home_page('mridadm', 'mrpassadm')

        '''
        Step 2 : Click Content View from the sidebar >> Click on top level Domain node from the resource tree.
                 Verify the repository tree refreshes post clicking on Domain node.
        '''
        main_page.select_content_from_sidebar()
        utils.wait_for_page_loads(20)
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        main_page.click_repository_folder("Workspaces")
        utils.wait_for_page_loads(20)
        main_page.verify_action_bar_tab_all_options(['Workspace', 'Folder'], 'Step 02.01 : Verify repository refreshes by checking the action bar options')
        
        '''
        Step 3 : Click on any existing domain/folders under Repository tree. Eg: Retail_Samples >> Charts.
        '''
        main_page.expand_repository_folder('Workspaces->Retail Samples')
        main_page.expand_repository_folder('Charts',1)
        
        '''
        Step Clicking on any domain/folder will reflect on the repository tree and breadcrumbs.
        '''
        main_page.verify_selected_resource_tree_item(['Charts'], "03.01")
        main_page.verify_crumb_box('Workspaces->Retail Samples->Charts', 'Step 3.02')
        
        '''
        Step 4 : From the Breadcrumbs >> Navigate to 'Documents' folder under Retail_Samples by clicking on the arrow drop-down pointing to 'Chart's.
        '''
        main_page.select_options_form_right_arrow_in_crumb_box('Charts', 'Documents')
        
        '''
        Step 4.01: Verify Breadcrumbs display Repository Tree Node > Retail_Samples > Documents.
        '''
        main_page.verify_crumb_box('Workspaces->Retail Samples->Documents', 'Step 4.01')
        
        '''
        Step 5 : In the banner link, click on the top right username > Click Sign Out.
        '''
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()