'''
Created on December 26, 2018

@author: varun
Testcase Name : Verify base pages are reflects in run mode
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262147
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

class C8262147_TestClass(BaseTestCase):
    
    def test_C8262147(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_locator_obj = portal_designer.Vfive_Designer()
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
        panel_one = 'Panel 1'
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}'.format(project,suite,group)
        folders_text = 'Folders'
        base_page_list = ['Base Page 1','Base Page 2', 'Base Page 3']
        
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
        Verify Base Page 1, Base Page 2 and Base Page 3 are appears in the navigation bar.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_title_css, portal_name, base_obj.home_page_medium_timesleep)
        designer_portal_obj.verify_specific_folder_in_top_folders(base_page_list, 'Step 3.1: Verify pages in the navigation bar')
        
        """
        Step 4: Click on Base Page 1.
        Verify Panel 1 (panel container) with a + sign inside on them.
        """
        designer_portal_obj.select_a_specific_top_folder('Base Page 1')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 1, base_obj.home_page_short_timesleep)
        designer_portal_obj.verify_specific_containers_title([panel_one], 'Step 4.1: Verify Panel 1 is present ')
        designer_portal_obj.verify_panel_add_content_displayed_in_container(panel_one, 'Step 4.2: Verify Plus sign in the Panel1')

        """
        Step 5: Click on Base Page 2.
        Verify Panel 1 (tab container) with a + sign inside on them.
        """
        designer_portal_obj.select_a_specific_top_folder('Base Page 2')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 1, base_obj.home_page_short_timesleep)
        designer_portal_obj.verify_specific_containers_title([panel_one], 'Step 5.1: Verify Panel 1 is present ')
        designer_portal_obj.verify_tab_list_in_container(panel_one, ['Tab 1'], 'Step 5.1: Verify tab 1 under panel 1')
        designer_portal_obj.verify_tab_panel_add_content_displayed_in_container(panel_one, 'Step 5.3: Verify Plus sign in the Panel1')
        
        """
        Step 6: Click on Base Page 3.
        Verify Panel 1 (carousel container) with a + sign inside on them.
        """
        designer_portal_obj.select_a_specific_top_folder('Base Page 3')
        util_obj.synchronize_with_number_of_element(portal_locator_obj.containers_css, 1, base_obj.home_page_short_timesleep)
        designer_portal_obj.verify_specific_containers_title([panel_one], 'Step 6.1: Verify Panel 1 is present ')
        designer_portal_obj.verify_carousel_panel_add_content_displayed_in_container('Panel 1', 'Step 6.2: Verify Plus sign inside carousel')
        
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