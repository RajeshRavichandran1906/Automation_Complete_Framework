"""-------------------------------------------------------------------------------------------
Created on July 31, 2019
@author: AFTAB

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2330500
Test Case Title =  Error checking for same title/name save
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design 
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C2330500_TestClass(BaseTestCase):

    def test_C2330500(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        g_var = Global_variables()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Workspaces->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        retail_sample_path = "Retail Samples->Portal->Test Widgets"
        case_id = g_var.current_test_case+'~!@#$%^&*()_+=-`{}|][":;\'?><,./\\'
        

        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        node_panel_css = ".ibfs-tree-node"
        page_canvas = "div.pd-page-canvas"
        dialog_caption_css = ".pop-top .ibx-title-bar-caption .ibx-label-text"
        dialog_content_css = ".pop-top .ibx-dialog-content .ibx-label-text"
        title_css = ".sd-form-field-text-title input"
        
        """ Step 1: Login WF as domain developer;
                    Click on Content view from side bar.
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """ Step 2: Expand 'P292_S10660' domain;
                    Click on 'G192932' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """ Step 3: Choose the Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        utils.synchronize_with_visble_text(node_panel_css, group_id, main_page.home_page_long_timesleep)
        
        """ Step 4: Click on "G192932 > P292_S10660" domain to go two level up;
                    Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.collapse_content_folder("{0}->{1}_{2}".format(group_id, project_id, suite_id))
        utils.synchronize_with_visble_text(node_panel_css, 'Retail Samples', main_page.home_page_long_timesleep)
        pd_design.expand_content_folder(retail_sample_path)
        utils.synchronize_with_visble_text(node_panel_css, 'Blue', main_page.home_page_long_timesleep)
       
        """ Step 5: Drag Blue, Gray, Green and Red onto the page canvas respectively.
        """
        pd_design.drag_content_item_to_blank_canvas('Blue', 1)
        utils.synchronize_with_visble_text(page_canvas, 'Blue', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Gray', 4)
        utils.synchronize_with_visble_text(page_canvas, 'Gray', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Green', 7)
        utils.synchronize_with_visble_text(page_canvas, 'Green', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Red', 10)
        utils.synchronize_with_visble_text(page_canvas, 'Red', pd_design.home_page_long_timesleep)
        
        """ Step 6: Click the application menu and click Save.
        """
        """ Step 7: Enter "C2330500~!@#$%^&*()_+=-`{}|][":;'?><,./\" in Title box and click Save.
        """
        pd_design.save_as_page_from_application_menu(case_id)
        
        """ Step 8: Close Designer.
        """
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, case_id, pd_design.home_page_long_timesleep)
        
        """ Step 9: Edit "C2330500~!@#$%^&*()_+=-`{}|][":;'?><,./\" page.
        """
        main_page.right_click_folder_item_and_select_menu(case_id, context_menu_item_path='Edit')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(".pd-content-accordion-pane", 'Content', pd_design.home_page_long_timesleep)
        
        """ Step 10: Click the application menu and click Save as...
        """
        pd_design.select_option_from_application_menu('Save as...')
        utils.synchronize_with_visble_text(pop_top_css, 'Cancel', pd_design.home_page_long_timesleep)
        
        """ Step 11: Clear Title box;
            Enter "C2330500~!@#$%^&*()_+=-`{}|][":;'?><,./\" in Title box (the same name/title as another page) and click Save as.
            Verify that you get a message stating that the file already exists with OK and cancel button.
        """
        title_obj = utils.validate_and_get_webdriver_object(title_css, 'title_css')
        title_obj.clear()
        title_obj.send_keys(case_id)
        main_page.verify_new_folder_Name_value(g_var.current_test_case.lower()+'~!_-`_', '11.00')
        main_page.click_button_on_popup_dialog('Save as')
        utils.synchronize_with_visble_text(pop_top_css, 'exist', pd_design.home_page_long_timesleep)
        actual = utils.validate_and_get_webdriver_object(dialog_caption_css, 'dialog_caption').text.strip()
        expected = 'Confirm Save'
        utils.asequal(expected, actual, 'Step 11.01: Verify Confirm Save pop-up window appears.')
        actual = utils.validate_and_get_webdriver_object(dialog_content_css, 'dialog_content_css').text.strip()
        expected = 'File '+g_var.current_test_case.lower()+'~!_-`_ already exists. Replace it?'
        utils.asequal(expected, actual, 'Step 11.02: Verify page already exist.')
        
        """ Step 12: Click cancel to not replace
        """
        main_page.click_button_on_popup_dialog('Cancel')
        main_page.click_button_on_popup_dialog('Cancel')
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        
        """ Step 13: Close Designer and sign out WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()