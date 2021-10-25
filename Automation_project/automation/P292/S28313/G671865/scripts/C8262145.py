'''
Created on December 26, 2018

@author: AA14564
Testcase Name : Verify pages inside the folders are reflects in run mode
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262145
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.locators.portal_designer import Vfive_Designer
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import designer_portal

class C8262145_TestClass(BaseTestCase):
    
    def test_C8262145(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        three_level_nav_obj = designer_portal.Three_Level(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        
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
        folders_text = 'Folders'
        expected_list1=['Test page 1.1', 'Test page 1.2']
        expected_list2=['Test page 2.1', 'Test page 2.2']
        expected_list3=['Test page 3.1', 'Test page 3.2']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
                Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > G514402 folder.
        """
        main_page_obj.expand_repository_folder('Domains->{0}'.format(expand_respository))
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, context_menu_item_path='Run')
        
        """
        Step 4: Click on Folder 1 in the navigation bar.
                Verify Test Page 1.1 and Test Page 1.2 appears in the side bar.
        """
        core_util_obj.switch_to_new_window()
        three_level_nav_obj.select_a_specific_top_folder(folder_one)
        util_obj.synchronize_with_number_of_element(Vfive_Designer.LEFT_PANEL_FOLDER_CSS, 2, 90)
        three_level_nav_obj.verify_items_in_left_navigation_bar(expected_list1, "Step 4: Verify Test Page 1.1 and Test Page 1.2 appears in the side bar.")
        
        """
        Step 5: Click on Folder 2 in the navigation bar.
                Verify Test Page 2.1 and Test Page 2.2 appears in the side bar.
        """
        three_level_nav_obj.select_a_specific_top_folder(folder_two)
        util_obj.synchronize_with_number_of_element(Vfive_Designer.LEFT_PANEL_FOLDER_CSS, 2, 90)
        three_level_nav_obj.verify_items_in_left_navigation_bar(expected_list2, "Step 5: Verify Test Page 2.1 and Test Page 2.2 appears in the side bar.")
        
        """
        Step 6: Click on Folder 3 in the navigation bar.
                Verify Test Page 3.1 and Test Page 3.2 appears in the side bar.
        """
        three_level_nav_obj.select_a_specific_top_folder(folder_three)
        util_obj.synchronize_with_number_of_element(Vfive_Designer.LEFT_PANEL_FOLDER_CSS, 2, 90)
        three_level_nav_obj.verify_items_in_left_navigation_bar(expected_list3, "Step 6: Verify Test Page 3.1 and Test Page 3.2 appears in the side bar.")
        
        """
        Step 7: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()