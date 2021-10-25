'''
Created on December 20, 2018

@author: varun
Testcase Name : Verify folders are reflects in run mode
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262143
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.wftools import designer_portal
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C8262143_TestClass(BaseTestCase):
    
    def test_C8262143(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj = designer_portal.Three_Level(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        new_page_title_css = ".pvd-portal-title .ibx-label-text"
        
        """
        Test case variables
        """
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}'.format(project,suite,group)
        folder_one = 'Folder 1'
        folder_two = 'Folder 2'
        folder_three = 'Folder 3'
        folders_list = [folder_one,folder_two,folder_three]
        folders_text = 'Folders'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > G514402 folder > click on V5 Personal Portal_Nav-2.
        """
        main_page_obj.expand_repository_folder(expand_respository)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        Verify Folder 1 , Folder 2 and Folder 3 are appears in the navigation bar.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_title_css, portal_name, base_obj.home_page_long_timesleep)
        designer_portal_obj.verify_specific_folder_in_top_folders(folders_list, "Step 3.1: Verify 3 Folders in the navigation bar")

        """
        Step 4: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out. 
        """
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()