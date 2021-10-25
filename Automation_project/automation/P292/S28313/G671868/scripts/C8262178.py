'''
Created on May 31, 2019.

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262178
TestCase Name = PD Tree: At times it can be tough to tell where you are since things are grouped closed
'''

from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.locators.page_designer_design import ContentTab
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools import page_designer
from common.wftools.login import Login
import unittest

class C8262178_TestClass(BaseTestCase):

    def test_C8262178(self):
        
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
        design_locator = ContentTab()
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        
        """
        TESTCASE VARIABLES
        """
        project_id = core_utils.parseinitfile('project_id')
        suite_id = core_utils.parseinitfile('suite_id')
        group_id = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
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
        utils.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', pd_run.home_page_medium_timesleep)
        
        """
        Step 5: Choose 'Grid 2-1' template
        """
        pd_design.select_page_designer_template('Grid 2-1')
        utils.synchronize_with_visble_text(design_locator.EXPANDED_CONTENT_CSS, group_id, pd_run.home_page_medium_timesleep)
        pd_design.collapse_content_folder(group_id)
        utils.synchronize_with_visble_text(design_locator.EXPANDED_CONTENT_CSS, 'My Content', pd_run.home_page_medium_timesleep)
        
        """
        Step 6: Navigate to a 'My content' folder in the tree
                Verify No Content available message appears as below
        """
        pd_design.expand_content_folder('My Content')
        utils.synchronize_with_visble_text(design_locator.EXPANDED_CONTENT_CSS, 'No content available', pd_run.home_page_medium_timesleep)
        pd_design.verify_page_domain_tree_node(['My Content', 'No content available'], 'Step 06.00 Verify No Content available message appears as below', assert_type='asequal')
        
        """
        Step 7: Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(homepage_locators.content_area_css, 'Designer', pd_run.home_page_medium_timesleep)
       
        """
        Step 8: Sign out WF
        """
        homepage.signout_from_username_dropdown_menu()
       
if __name__ == '__main__':
    unittest.main()