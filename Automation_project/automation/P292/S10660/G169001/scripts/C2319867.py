"""-------------------------------------------------------------------------------------------
Created on July 29, 2019
@author: AFTAB

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2319867
Test Case Title =  Testing Save As
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
from common.locators.page_designer_design import ToolBar
from common.lib.global_variables import Global_variables

class C2319867_TestClass(BaseTestCase):

    def test_C2319867(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        toolbar_locator = ToolBar
        g_var = Global_variables()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        retail_sample_path = "Retail Samples->Portal->Test Widgets"
        domain_name = repository_folder.split('->')[1]+'~!@#$%^&*()_+=-`{}|][":;\'?><,./'

        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        node_panel_css = ".ibfs-tree-node"
        page_canvas = "div.pd-page-canvas"
        crumb_css = ".pop-top .sd-crumb-box [title]"
        crumb_carat_css = ".pop-top .sd-crumb-box .sd-right-carat"
        dialog_caption_css = ".pop-top .ibx-title-bar-caption .ibx-label-text"
        dialog_content_css = ".pop-top .ibx-dialog-content .ibx-label-text"
        
        """ STEP 1: Login WF as domain developer.
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        
        """ Step 2: Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """ Step 3: Expand 'P292_S10660' domain;
                    Click on 'G192932' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """ Step 4: Choose the Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        utils.synchronize_with_visble_text(node_panel_css, group_id, main_page.home_page_long_timesleep)
        
        """ Step 5: Click on "P292_S10660" domain to go one level up;
                    Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.collapse_content_folder("{0}->{1}_{2}".format(group_id, project_id, suite_id))
        utils.synchronize_with_visble_text(node_panel_css, 'Retail Samples', main_page.home_page_long_timesleep)
        pd_design.expand_content_folder(retail_sample_path)
        utils.synchronize_with_visble_text(node_panel_css, 'Blue', main_page.home_page_long_timesleep)
       
        """ Step 6: Drag Blue, Gray, Green and Red onto the page canvas respectively.
        """
        pd_design.drag_content_item_to_blank_canvas('Blue', 1)
        utils.synchronize_with_visble_text(page_canvas, 'Blue', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Gray', 4)
        utils.synchronize_with_visble_text(page_canvas, 'Gray', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Green', 7)
        utils.synchronize_with_visble_text(page_canvas, 'Green', pd_design.home_page_long_timesleep)
        pd_design.drag_content_item_to_blank_canvas('Red', 10)
        utils.synchronize_with_visble_text(page_canvas, 'Red', pd_design.home_page_long_timesleep)
        
        """ Step 7: Click the ToolBar icon
                    Verify that you see Open, New, Save, Save as... and Close menus are available.
        """
        application_icon_ob=utils.validate_and_get_webdriver_object(toolbar_locator.APPLICATION_BUTTON_CSS, 'APPLICATION BUTTON CSS')
        core_utils.left_click(application_icon_ob)
        utils.synchronize_with_visble_text(pop_top_css, 'Save as', pd_design.home_page_long_timesleep)
        actual = utils.validate_and_get_webdriver_object(pop_top_css, 'APPLICATION BUTTON option').text.strip().split('\n')
        expected = ['Open...', 'New', 'Save', 'Save as...', 'Close']
        utils.as_List_equal(expected, actual, 'Step 07.00: Verify that you see Open, New, Save, Save as... and Close menus are available.')
        pd_design.select_container('Gray')
        utils.synchronize_until_element_disappear(pop_top_css, pd_design.home_page_short_timesleep)
        
        """ Step 8: Click the Save as... menu
                    Verify the Save as dialog appears. It should recall the (P292_S10660) domain/folder you started to create the page.
                    Verify that it says Page 1 for Title and page_1 for Name
                    Verify that the text in the Title and Name boxes are not cutoff in the save as dialog
        """
        pd_design.select_option_from_application_menu('Save as...')
        utils.synchronize_with_visble_text(pop_top_css, 'Save as', pd_design.home_page_long_timesleep)
        crumb_obj=utils.validate_and_get_webdriver_objects(crumb_css, 'crumb_css')
        actual = [opt.text.strip() for opt in crumb_obj if opt!='']
        expected = repository_folder.split('->')
        utils.as_List_equal(expected, actual, 'Step 08.00: Verify the Save as dialog appears. It should recall the (P292_S10660) domain/folder you started to create the page.')
        main_page.verify_new_folder_title_value('Page 1', '08.01')
        main_page.verify_new_folder_Name_value('page_1', '08.02')
        utils.verify_picture_using_sikuli('step_8_3.png', 'Step 08.03: Verify that the text in the Title and Name boxes are not cutoff in the save as dialog')
        
        """ Step 9: Click the Caret '>' next to Domains.
                    Verify you get a list of all the folder available under the P292_S10660 domain.
        """
        location_ = core_utils.get_web_element_coordinate(utils.validate_and_get_webdriver_object(dialog_caption_css, 'dialog_caption'))
        core_utils.left_click(utils.validate_and_get_webdriver_object(crumb_carat_css, 'crumb_carat_css'))
        utils.synchronize_with_visble_text(pop_top_css, expected[1], pd_design.home_page_long_timesleep)
        acutal = utils.validate_and_get_webdriver_object(pop_top_css, 'crumb carat option').text.strip().split('\n')
        msg = "Step 09.00: Verify you get a list of all the folder available under the P292_S10660 domain."
        utils.verify_list_values([expected[1]], acutal, msg, assert_type='asin')
        core_utils.python_click_with_offset(location_['x'], location_['y'])
        core_utils.python_click_with_offset(location_['x'], location_['y'])
        
        """ Step 10: Click the Save as button
        """
        main_page.click_button_on_popup_dialog('Save as')

        """ Step 11: Go to the Home page without closing designer.
                     Verify Page 1 is available under P292_S10660 domain.
        """
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page 1", main_page.home_page_medium_timesleep)
        
        """ Step 12: Come back to page designer and click application menu and click Save as...
        """
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(page_canvas, 'Red', pd_design.home_page_long_timesleep)
        pd_design.select_option_from_application_menu('Save as...')
        utils.synchronize_with_visble_text(pop_top_css, 'Cancel', pd_design.home_page_long_timesleep)
        
        
        """ Step 13: Don't change the title and name, click the Save as... button
                     Verify page already exist "Confirm Save" pop-up window appears.
        """
        main_page.click_button_on_popup_dialog('Save as')
        utils.synchronize_with_visble_text(pop_top_css, 'exist', pd_design.home_page_long_timesleep)
        actual = utils.validate_and_get_webdriver_object(dialog_caption_css, 'dialog_caption').text.strip()
        expected = 'Confirm Save'
        utils.asequal(expected, actual, 'Step 13.00: Verify Confirm Save pop-up window appears.')
        actual = utils.validate_and_get_webdriver_object(dialog_content_css, 'dialog_content_css').text.strip()
        expected = 'File page_1 already exists. Replace it?'
        utils.asequal(expected, actual, 'Step 13.01: Verify page already exist.')
        
        """ Step 14: Click Cancel.
        """
        main_page.click_button_on_popup_dialog('Cancel')
        
        """ Step 15: Navigate to "P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./" domain in the Save as dialog.
        """
        main_page.select_crumb_item_from_resource_dialog('Domains')
        utils.synchronize_with_visble_text(pop_top_css, domain_name, pd_design.home_page_long_timesleep)
        resource_dialog = utils.validate_and_get_webdriver_objects(".pop-top .folder-item", 'save as dialog')
        for opt in resource_dialog:
            if domain_name in opt.text.strip():
                core_utils.double_click(opt)
                break
        time.sleep(3)
        
        """ Step 16: Enter "C2319867~!@#$%^&*()_+=-`{}|][":;'?><,./" in Title box.
                     Verify some of the characters are not available in the Name box.
        """
        main_page.enter_new_folder_title_in_popup_dialog(g_var.current_test_case+'~!@#$%^&*()_+=-`{}|][":;\'?><,./')
        main_page.verify_new_folder_Name_value(g_var.current_test_case.lower()+'~!@_-`_', '08.02')
        
        """ Step 17: Click the Save as button
                     Verify page is saved.
        """
        main_page.click_button_on_popup_dialog('Save as')
        utils.synchronize_with_visble_text(".ibx-tab-position-bottom .ibx-tab-button .ibx-label-text", g_var.current_test_case, main_page.home_page_long_timesleep)
        actual = utils.validate_and_get_webdriver_object(".ibx-tab-position-bottom .ibx-tab-button .ibx-label-text", 'page').text.strip()
        expected = g_var.current_test_case+'~!@#$%^&*()_+=-`{}|][":;\'?><,./'
        utils.asequal(expected, actual, 'Step 17: Verify page is saved.')
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close=False)
        
        """ Step 18: Close Designer and logout WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()