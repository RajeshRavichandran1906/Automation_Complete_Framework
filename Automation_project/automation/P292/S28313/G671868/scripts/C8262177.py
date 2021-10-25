'''
Created on May 31, 2019.

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262177
TestCase Name = UC:Save Dialog: Navigating to another folder/domain removes the title and name entries
'''

import unittest
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators.page_designer_design import ToolBar
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer

class C8262177_TestClass(BaseTestCase):

    def test_C8262177(self):
        
        """
        TESTCASE OBJECTS
        """
        pd_design = page_designer.Design(self.driver)
        pd_run = page_designer.Run(self.driver)
        wf_login = Login(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        homepage = Wf_Mainpage(self.driver)
        homepage_locators = WfMainPageLocators()
        design_locator = ToolBar()
        workspaces ="Workspaces"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".pd-page-canvas"
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        group_id = core_utils.parseinitfile('group_id')
        reference_folder = core_utils.parseinitfile('reference_folder').split('->')[0]
        repository_folder = workspaces+'->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        
        """
        Step 1: Login WF as domain developer
        """
        wf_login.invoke_home_page("mrid", "mrpass")
        
        """
        Step 2: Click on Content view from side bar
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(homepage_locators.REPOSITORY_TREE_CSS, 1, pd_run.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'P292_S28313' domain -> G671868 folder
        """
        homepage.click_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Designer', pd_run.home_page_medium_timesleep)
       
        """
        Step 4: Click on Page action tile from under Designer category
        """
        homepage.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Page', pd_run.home_page_medium_timesleep)
        homepage.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Grid 2-1 Side', pd_run.home_page_medium_timesleep)
        
        """
        Step 5: Choose 'Grid 2-1 Side' template
        """
        pd_design.select_page_designer_template('Grid 2-1 Side')
        utils.synchronize_with_visble_text(containers_css, 'Panel 1', pd_run.home_page_medium_timesleep)
        utils.synchronize_until_element_is_visible(design_locator.SAVE_BUTTON_CSS, pd_run.home_page_medium_timesleep)
        
        """
        Step 6: Click on save button
                Verify 'Page 1' appears for title and name by default
        """
        pd_design.click_toolbar_save()
        homepage.verify_new_domain_title_value('Page 1', "Step 06:00 Verify 'Page 1' appears for title by default.")
        homepage.verify_new_domain_name_value('page_1', "Step 06:01 Verify 'Page 1' appears for name by default.")
        
        """
        Step 7: Navigate to Retail Samples domain and double click on it.
                Verify 'Page 1' still appears for title and name, shguldn't be blank
        """
        homepage.select_crumb_item_from_resource_dialog(workspaces)
        homepage.select_file_or_folder_from_resource_dialog(reference_folder, selection_type='double', view_type="grid_view")
        homepage.verify_new_domain_title_value('Page 1', "Step 07:00 Verify 'Page 1' appears for title by default.")
        homepage.verify_new_domain_name_value('page_1', "Step 07:01 Verify 'Page 1' appears for name by default.")
        
        """
        Step 8: Click Cancel
        """
        homepage.click_button_on_popup_dialog('Cancel')
        
        """
        Step 9: Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Designer', pd_run.home_page_medium_timesleep)
       
        """
        Step 10: Signout WF
        """
        homepage.signout_from_username_dropdown_menu()
       
      
if __name__ == '__main__':
    unittest.main()