'''
Created on March 29, 2019

@author: varun
Testcase Name : V5 portal: unable to navigate into My Pages folder
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261733
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_portal
from common.wftools import page_designer
import sys
from common.wftools.designer_portal import Two_Level_Side
from common.wftools.designer_portal import Three_Level
from common.locators.portal_designer import Vfive_Designer
import time
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard

class C8261733_TestClass(BaseTestCase):
    
    def test_C8261733(self):
        """
        Test case objects
        """
        three_level_side_obj = Three_Level(self.driver)
        two_level_side_obj = Two_Level_Side(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        portal_name = 'v5-Debug'
        workspace = "Workspaces"
        
        """
        Test case CSS
        """
        selected_page = Vfive_Designer.left_panel_page_folder_group_css + " .ibx-accordion-page-button"
        page_heading_title = ".pd-page-title .ibx-label-text"
        domains_css = ".toolbar"
        portal_dialog_css = ".create-pvd-dialog .ibx-title-bar-caption .ibx-label-text"
        new_page_template = ".ibx-dialog-title-box .ibx-title-bar-caption .ibx-label-text"
        
        """
        Step 1: Login WF as developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
         
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
         
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 4: Enter title as 'v5-Debug' in create portal dialog
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
        
        """
        Step 5: Click on 'Create My Pages menu' check box 
        """
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        
        """
        Step 6: Click Create
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 7: Click on 'v5-Debug' in tree and select Page tile in action bar
        """
        main_page_obj.expand_repository_folder(portal_name)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_template, 'New Page', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: Choose Grid 2-1 template and save page as 'Base Page1'
        """
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(page_heading_title, 'Page Heading', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.save_page_from_toolbar('Base Page1')
        
        """
        Step 9: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Right click on 'v5-Debug' and select Publish
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Publish')
        
        """
        Step 11: Hit F12 to invoke chrome debugger;
        Click on console
        """
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.press_key(pykeyboard.shift_key)
            pykeyboard.tap_key(character=u'\u006a')
            pykeyboard.release_key(pykeyboard.shift_key)
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.send('ctrl+shift+j')
        time.sleep(3)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.press_key(pykeyboard.shift_key)
            pykeyboard.tap_key(character=u'\u0064')
            pykeyboard.release_key(pykeyboard.shift_key)
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            keyboard.send('ctrl+shift+d')
        
        """
        Step 12: Click on Domains in breadcrumb;
        Double click on 'v5-Debug' from under P292_S19901' domain-> 'G520448' folder in content area
        Verify 'Base Page1' and 'My pages' menu appears in content area
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_medium_timesleep)
        main_page_obj.double_click_folder_item_and_select_menu(portal_name)
        main_page_obj.verify_folders_in_grid_view(["My Pages"], 'asin', "Step 12.1 Verify ")
        main_page_obj.verify_items_in_grid_view(['Base Page1'], 'asin', "Step 12.2: Verify")
        
        """
        Step 13: Double click on 'My Pages' folder in content area
        Verify no errors in F12 console
        """
        main_page_obj.double_click_folder_item_and_select_menu("My Pages")
        console_log = self.driver.get_log('browser')
        if console_log == []:
            util_obj.asequal([],console_log, "Step 13: Verify no errors in console")
        elif len(console_log) > 0:
            for index_, item in enumerate(console_log, 1):
                util_obj.asequal("WARNING",item['level'], "Step 13.{0}: Verify no errors in console".format(index_))
        else:
            raise Exception("Console has errors")
        
        """
        Step 14: Again Hit F12 to close chrome debugger;
        """
        if sys.platform == 'linux':
            pykeyboard.tap_key(pykeyboard.function_keys[12])
        else:
            keyboard.send('f12')
        
        """
        Step 15: Right click on 'v5-Debug' and select Run
        Verify 'Base Page1' is highlighted by default
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_heading_title, 'Page Heading', main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_selected_page_from_top_folder('Base Page1', "Step 14.1: Verify the Base page is selected")
        
        """
        Step 16: Click on 'My Pages' menu
        Verify only 'My Pages' menu has been highlighted now not the base page
        """
        two_level_side_obj.expand_folder_in_left_sidebar('My Pages')
        selected_page_obj = util_obj.validate_and_get_webdriver_objects(selected_page, "selected-page")
        get_selected_background = selected_page_obj[1].value_of_css_property("background-color")
        util_obj.asequal("rgba(0, 0, 0, 0.15)", get_selected_background, "Step 15.1: My Pages is selected")
        
        """
        Step 17: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 18: Right click on 'v5-Debug' and select Edit;
        Change navigation to 'Three level' and click save
        """
        core_util_obj.switch_to_default_content()
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Edit')
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 19: Right click on 'v5-Debug' and select Run
        Verify 'Base.title Page1' is highlighted by default
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_heading_title, 'Page Heading', main_page_obj.home_page_medium_timesleep)
        three_level_side_obj.verify_selected_folder_in_top_folders('Base Page1', "Step 18.1: Verify Base page1 is selected")
        
        """
        Step 20: Click on 'My Pages' menu
        Verify only 'My Pages' menu has been highlighted now not the base page
        """
        three_level_side_obj.select_a_specific_top_folder('My Pages')
        three_level_side_obj.verify_selected_folder_in_top_folders('My Pages', "Step 19.1: Verify Base page1 is selected")
        
        """
        Step 21: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", "Folders", main_page_obj.home_page_medium_timesleep)
        
        """
        Step 22: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()