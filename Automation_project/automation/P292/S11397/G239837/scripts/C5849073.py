'''
Created on April 3, 2019

@author: varun
Testcase Name : Verify drag and Drop folder tree to content area
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5849073
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators

class C5849073_TestClass(BaseTestCase):
    
    def test_C5849073(self):
        """
        Test case objects
        """
        main_pages_obj = Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        verify_message = "Are you sure you wish to move these resources?"
        
        """
        Test case CSS
        """
        
        def drag_fex_from_content_area_to_tree(domain_item, tree_item):
            util_obj.synchronize_with_visble_text(loc_obj.content_area_css, domain_item, main_page_obj.home_page_medium_timesleep)
            drag_obj = main_pages_obj.get_domain_folder_item(domain_item)
            core_util_obj.left_click(drag_obj)
            drag_fex = core_util_obj.get_web_element_coordinate(drag_obj)
            drop_obj = main_pages_obj.get_repository_folder(tree_item)
            drop_folder = core_util_obj.get_web_element_coordinate(drop_obj)
            core_util_obj.drag_and_drop_without_using_click(drag_fex['x'], drag_fex['y'], drop_folder['x'], drop_folder['y'])
            
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree.
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains')
        
        """
        Step 3: Expand "Retail Sample_1" domain in resource tree..
        """
        main_page_obj.expand_repository_folder('Retail Samples_1')
        
        """
        Step 4: Drag "Documents" folder from tree and drop it on "P292_S11397"-> G239837 domain.
        Verify Warning message display "Are you sure you wish to move these resources".
        """
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id)
        main_page_obj.expand_repository_folder('Retail Samples_1')
        drag_fex_from_content_area_to_tree('Documents', group_id)
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", "Warning", main_page_obj.home_page_short_timesleep)
        observed_warning = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"message\"]",'message').text.strip()
        util_obj.asequal(verify_message, observed_warning, "Step 4.1: Verify the warning message")
        
        """
        Step 5: Click on Yes.
        Verify "Document" folder is under "P292_S11397"-> G239837
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id)
        main_page_obj.verify_folders_in_grid_view(['Documents'], 'asin', 'Step 5.1: Verify documents in the under the G239837 folder')
        
        """
        Step 6: Drag "Document" from "P292_S11397"-> G239837 from content area back to "Retail samples_1" domain in the tree.
        """
        drag_fex_from_content_area_to_tree('Documents', 'Retail Samples_1')
        
        """
        Step 7: Click Yes.
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign O
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
    