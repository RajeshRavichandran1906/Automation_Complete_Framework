"""-------------------------------------------------------------------------------------------
Created on July 23, 2019
@author: Vishnu_priya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334373
Test Case Title =  Testing Save As with special characters
-----------------------------------------------------------------------------------------------"""
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2334373_TestClass(BaseTestCase):

    def test_C2334373(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        
        """
            STEP 1 : Login WF as domain developer.
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        
        """
            STEP 2 : Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Expand 'P292_S10660' domain;
            Click on 'G192932' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        
        """
            STEP 4 : Choose the Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        
        """
            STEP 5 : Click on "G192932 > P292_S10660" domain to go two level up;
            Navigate to Retail samples --> Portal --> Test Widgets folder..
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G192932")
        pd_design.collapse_content_folder("P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 6 : Drag Blue, Gray, Green and Red onto the panels respectively.
        """
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Blue', 1, '06.00')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Gray', 4, '06.01')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Green', 7, '06.02')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Red', 10, '06.03')
        
        
        
        """
            STEP 7 : Click the application menu and click Save as.....
        """
        """
            
            STEP 8 : Enter "C2334373~!@#$%^&*()_+=-`{}|][":;'?><,./\" in Title box..
            Verify some of the characters are not available in the Name box.
        """
        """
            STEP 9: Click the Save as... button.
        """

        name_to_save='''C2334373~!@#$%^&*()_+=-`{}|][":;'?><,./\ '''
        name_value="c2334373~!@_-`_"
        pd_design.select_option_from_application_menu("Save as...")
        utils.synchronize_until_element_is_visible(".open-dialog-resources",main_page.chart_long_timesleep)
        main_page.enter_new_domain_title_value(name_to_save)
        time.sleep(2)
        main_page.verify_new_folder_name_in_popup_dialog(name_value,"Step 08:Verify some of the characters are not available in the Name box.")
        main_page.click_button_on_popup_dialog("Save as")
        
        """
            STEP 10: Close Designer page.
            Verify created page visible in the home page under P292_S10660/G192932 domain.
        """
        core_utils.switch_to_previous_window()
        
        """
            STEP 11: Run the page.
            Verify the page run and no issue appears.
        """
        time.sleep(2)
        name_to_open='''C2334373~!@#$%^&*()_+=-`{}|][":;\'?><,./\\'''
        main_page.right_click_folder_item_and_select_menu(name_to_open,"Run in new window")
        core_utils.switch_to_new_window()
        utils.verify_object_visible('.pop-top', False,"Step:11 Verify the page run and no issue appears.")
        
        
        """
            STEP 12 : Close run window and sign out WF.
        """
        core_utils.switch_to_previous_window()
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()