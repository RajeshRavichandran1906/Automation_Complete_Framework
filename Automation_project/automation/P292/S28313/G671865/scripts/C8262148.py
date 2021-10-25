'''
Created on December 26, 2018

@author: varun
Testcase Name :Add personal pages in run mode
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262148
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
from common.locators import portal_designer

class C8262148_TestClass(BaseTestCase):
    
    def test_C8262148(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        two_level_designer_obj=designer_portal.Two_Level_Side(self.driver)
        portal_locator_obj = portal_designer.Vfive_Designer()
        designer_portal_obj = designer_portal.Three_Level(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        page_template_css = ".ibx-title-bar-caption .ibx-label-text"
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        new_page_title_css = ".pvd-portal-title .ibx-label-text"
        new_page_css = '{0} {1} {2}'.format(portal_locator_obj.left_panel_page_folders_container_css, 
                                            portal_locator_obj.ADD_NEW_PAGE_CSS, portal_locator_obj.LABEL_TEXT_CSS)
        
        """
        Test case variables
        """
        new_page_text = 'New Page'
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}'.format(project,suite,group)
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
        Step 2: Expand 'P292_S19901' domain > G514402 folder.
        """
        main_page_obj.expand_repository_folder(expand_respository)
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_title_css, portal_name, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on My Pages > click + sign > choose 'Grid2-1' template
        """
        designer_portal_obj.select_a_specific_top_folder('My Pages')
        util_obj.synchronize_with_number_of_element(new_page_css, 1 , base_obj.home_page_short_timesleep)
        designer_portal_obj.click_new_page_from_left_navigation_bar()
        util_obj.synchronize_with_visble_text(page_template_css, new_page_text, base_obj.home_page_medium_timesleep)
        two_level_designer_obj.select_new_page_template('Grid 2-1')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 3, base_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click + sign > choose 'Grid 3-3-3' template.
        """
        designer_portal_obj.click_new_page_from_left_navigation_bar()
        util_obj.synchronize_with_visble_text(page_template_css, new_page_text, base_obj.home_page_medium_timesleep)
        two_level_designer_obj.select_new_page_template('Grid 3-3-3')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 9, base_obj.home_page_medium_timesleep)
        
        """
        Step 6: Click +sign > choose 'Grid 4-2-1' template.
        Verify that the personal pages(Page 1,2 and 3) are appears at the end of the list
        """
        designer_portal_obj.click_new_page_from_left_navigation_bar()
        util_obj.synchronize_with_visble_text(page_template_css, new_page_text, base_obj.home_page_medium_timesleep)
        two_level_designer_obj.select_new_page_template('Grid 4-2-1')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 7, base_obj.home_page_medium_timesleep)
        designer_portal_obj.verify_specific_item_in_left_navigation_bar(['Page 1','Page 2','Page 3'], 'Step 6.1: Verify 3 pages in the left navigation bar')
        
        """
        Step 7: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_short_timesleep)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()