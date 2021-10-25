'''
Created on April 16, 2019

@author: AA14564
Test case Name : V5 portals/Embedded Content section should not appear in Page designer but only in Workbook
Test case ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262057
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools.page_designer import Design
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
from common.locators.page_designer_design import ContentTab

class C8262057_TestClass(BaseTestCase):
    
    def test_C8262057(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        pd_obj = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        content_obj = ContentTab()
        
        """
        Test case CSS
        """
        pop_up_dialog_css = ".pop-top"
        page_designer_content_tree_css = ".pd-tree"
        page_designer_content_tab_css = "[class*='pd-content-tab-pag'].tpg-selected .ibx-accordion-page-button"
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'P292_S28313' domain -> G671847 folder
        """
        main_page_obj.click_repository_folder('{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under Designer category
        """
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        
        """
        Step 5: Choose 'Grid 2-1' template
                Verify that you don't see the embedded Content section on the tree;
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        pd_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(page_designer_content_tab_css, main_page_obj.home_page_medium_timesleep)
        content_option_objs = util_obj.validate_and_get_webdriver_objects(page_designer_content_tab_css, 'Page designer content section')
        actual_content_list_value = [elem.text.strip() for elem in content_option_objs if elem.text.strip()!='']
        util_obj.verify_list_values(['Embedded Content'], actual_content_list_value,  "Step 5: Verify that you don't see the embedded Content section on the tree.", assert_type='asnotin')
        
        """
        Step 6: Expand 'P292_S28313' domain
                Verify 'v5-mypages-test1' portal doesn't appear in the tree for selection
        """
        pd_obj.collapse_content_folder('{0}'.format(group_id))
        util_obj.synchronize_until_element_is_visible(page_designer_content_tree_css, main_page_obj.home_page_medium_timesleep)
        item_elements = util_obj.validate_and_get_webdriver_objects(content_obj.EXPANDED_CONTENT_ITEMS_CSS, 'Page designer content items')
        actual_content_list_value = [elem.text.strip() for elem in item_elements if elem.text.strip()!='']
        util_obj.verify_list_values(['v5-mypages-test1'], actual_content_list_value,  "Step 6: Verify 'v5-mypages-test1' portal doesn't appear in the tree for selection.", assert_type='asnotin')
        
        """
        Step 7: Close page without saving
        """
        pd_obj.close_page_designer_without_save_page()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 8: Sign out WF 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()