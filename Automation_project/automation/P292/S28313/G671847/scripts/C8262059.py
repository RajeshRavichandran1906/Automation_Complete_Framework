'''
Created on May 11, 2019

@author: varun
Test case Name : Properties: Remove Load in iframe from Page advanced tab
Test case ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262059
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import page_designer
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators


class C8262059_TestClass(BaseTestCase):
    
    def test_C8262059(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        pd_obj = page_designer.Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        pop_up_dialog_css = ".pop-top"
        page_designer_content_tab_css = "[class*='pd-content-tab-pag'].tpg-selected .ibx-accordion-page-button"
        
        """
        Test case variables
        """
        folder_name = 'HOME-1702'
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
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        pd_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(page_designer_content_tab_css, main_page_obj.home_page_medium_timesleep)

        """
        Step 6: Save page as 'HOME-1702' and close designer
        """
        pd_obj.save_page_from_toolbar(folder_name)
        pd_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 7: Right click on 'HOME-1702' and select properties
        """
        main_page_obj.right_click_folder_item_and_select_menu(folder_name, 'Properties')
        
        """
        Step 8: Click on advanced tab
        Verify Load in iframe property is not available
        """
        util_obj.synchronize_with_visble_text(".properties-page-label", folder_name, main_page_obj.home_page_short_timesleep)
        main_page_obj.select_property_tab_value('Advanced')
        advanced_pane_text = util_obj.validate_and_get_webdriver_object('.properties-advanced-item-fex', 'advanced-tab').text.strip()
        try:
            main_page_obj.verify_label_in_property_dialog('Advanced', 'Load in iframe', '8.1')
            util_obj.as_notin('Load in iframe', advanced_pane_text, "Step 8.1: Verify load in iframe not present")
        except IndexError:
            util_obj.as_notin('Load in iframe', advanced_pane_text, "Step 8.1: Verify load in iframe not present")
        
        """
        Step 9: Click cancel
        """
        main_page_obj.select_property_dialog_save_cancel_button('Cancel')
        
        """
        Step 10: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()