'''
Created on December 17, 2018

@author: varun
Testcase Name : Adding folders in V5 Portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262142
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods

class C8262142_TestClass(BaseTestCase):
    
    def test_C8262142(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        action_bar_css = "[data-ibxp-text=\"Action Bar\"] .ibx-label-text"
        
        """
        Test case variables
        """
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}->{3}'.format(project,suite,group,portal_name)
        folder_one = 'Folder 1'
        folder_two = 'Folder 2'
        folder_three = 'Folder 3'
        folders_list = [folder_one,folder_two,folder_three]
        action_bar_text = 'Action Bar'
        action_bar_folder = 'Folder' 
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
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_short_timesleep)
        
        """
        Step 3: Click on folder action bar and give "Folder 1" as title > click OK.
        """
        main_page_obj.select_action_bar_tabs_option(action_bar_folder)
        main_page_obj.create_new_folder(folder_one)
        
        """
        Step 4: Click on folder action bar and give "Folder 2" as title > click OK.
        """
        main_page_obj.select_action_bar_tabs_option(action_bar_folder)
        main_page_obj.create_new_folder(folder_two)
        
        """
        Step 5: Click on folder action bar and give "Folder 3" as title > click OK.
        Verify Folder 1,2 and 3 are appears in the content area.
        """
        main_page_obj.select_action_bar_tabs_option(action_bar_folder)
        main_page_obj.create_new_folder(folder_three)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        main_page_obj.verify_folders_in_grid_view(folders_list,'asin',"Step 5.1: Verify 3 folders in the content area")
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()