'''
Created on April 2, 2019

@author: varun
Testcase Name : Check navigations with % setting
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261736
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_portal
import time

class C8261736_TestClass(BaseTestCase):
    
    def padding_verification(self, input_list, msg):
        container_css = ".pvd-container"
        padding_sides = ['left','right','top','bottom']
        util_obj = utillity.UtillityMethods(self.driver)
        container_obj = util_obj.validate_and_get_webdriver_object(container_css, "container")
        padding_list = []
        for side in padding_sides:
            padding_list.append(util_obj.get_element_css_propery(container_obj,'padding-{0}'.format(side)).strip())
        util_obj.as_List_equal(input_list, padding_list, msg)
    
    def test_C8261736(self):
        """
        Test case objects
        """
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
        portal_name = 'Portal with 100% Two side nav'
        three_level_portal = 'Portal with 100% Three level nav'
        two_level_top = 'Portal with 100% Two Top level nav'
        workspace = "Workspaces"
        
        """
        Test case CSS
        """
        domains_css = ".toolbar"
        portal_dialog_css = ".create-pvd-dialog .ibx-title-bar-caption .ibx-label-text"
        portal_title_css = ".pvd-portal-title"
            
        """
        Step 1: Login WF as domain advanced user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        util_obj.synchronize_with_visble_text(domains_css, workspace, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 4: Enter title as 'Portal with 100% Two side nav';
        Click on 'Create My pages menu' check box;
        Click create
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
         
        """
        Step 5: Right click on 'Portal with 100% Two side nav' and select Publish
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, portal_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Publish')
        util_obj.wait_for_page_loads(5)
         
        """
        Step 6: Right click on 'Portal with 100% Two side nav' and select Run
        Verify that the portal appears in maximum width (full screen)
        """
        
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, portal_name, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['0px', '0px', '0px', '0px'], "Step 6.1: Portal appears in maximum width")
         
        """
        Step 7: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
         
        """
        Step 8: Right click on 'Portal with 100% Two side nav' and select Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Edit')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Edit Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 9: Enter 75% on maximum width and click save
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
         
        """
        Step 10: Right click on 'Portal with 100% Two side nav' and select Run
        Verify portal appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, portal_name, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['210px', '210px', '0px', '0px'], "Step 10.1: Portal appears with 75% width")
         
        """
        Step 11: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
         
        """
        Step 12: Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 13: Enter title as 'Portal with 100% Three level nav';
        Click on Three level nav
        Click on 'Create My pages menu' check box;
        Click create.
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=three_level_portal)
        portal_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
         
        """
        Step 14: Right click on 'Portal with 100% Three level nav' and select Publish
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, three_level_portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(three_level_portal,'Publish')
        time.sleep(3)
        util_obj.wait_for_page_loads(5)
         
        """
        Step 15: Right click on 'Portal with 100% Three level nav' and select Run
        Verify that the portal appears in maximum width (full screen)
        """
        main_page_obj.right_click_folder_item_and_select_menu(three_level_portal,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, three_level_portal, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['0px', '0px', '0px', '0px'], "Step 15.1: Portal appears in maximum width")
         
        """
        Step 16: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
         
        """
        Step 17: Right click on 'Portal with 100% Three level nav' and select Edit
        """
        util_obj.wait_for_page_loads(10)
        main_page_obj.right_click_folder_item_and_select_menu(three_level_portal,'Edit')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Edit Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 18: Enter 75% on maximum width and click save
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
         
        """
        Step 19: Right click on 'Portal with 100% Three level nav' and select Run
        """
        main_page_obj.right_click_folder_item_and_select_menu(three_level_portal,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, three_level_portal, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['210px', '210px', '0px', '0px'], "Step 19.1: Portal appears in 75% width")
         
        """
        Step 20: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
         
        """
        Step 21: Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 22: Enter title as 'Portal with 100% Two Top level nav';
        Click on Two Top level nav
        Click on 'Create My pages menu' check box;
        Click create.
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=two_level_top)
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        portal_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check')
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
         
        """
        Step 23: Right click on 'Portal with 100% Two Top level nav' and select Publish
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, two_level_top, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(two_level_top,'Publish')
        time.sleep(3)
        util_obj.wait_for_page_loads(5)
         
        """
        Step 24: Right click on 'Portal with 100% Two Top level nav' and select Run
        Verify that the portal appears in maximum width (full screen)
        """
        main_page_obj.right_click_folder_item_and_select_menu(two_level_top,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, two_level_top, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['0px', '0px', '0px', '0px'], "Step 23.1: Portal appears in maximum width")
         
        """
        Step 25: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
         
        """
        Step 26: Right click on 'Portal with 100% Two Top level nav' and select Edit
        """
        main_page_obj.right_click_folder_item_and_select_menu(two_level_top,'Edit')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Edit Portal', main_page_obj.home_page_short_timesleep )
         
        """
        Step 27: Enter 75% on maximum width and click save
        """
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='75%')
        portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
        
        """
        Step 28: Right click on 'Portal with 100% Two Top level nav' and select Run
        Verify portal appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(two_level_top,'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, two_level_top, main_page_obj.home_page_medium_timesleep)
        self.padding_verification(['0px', '0px', '0px', '0px'], "Step 28.1: Portal appears in 75% width")
        
        """
        Step 29: Close portal
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_short_timesleep)
        
        """
        Step 30: Click on 'G671769' folder;
        Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
        
        """
        Step 31: Enter title as 'Portal with 50 % Three level nav (50 space %)';
        Enter maximum width value as '50' space '%'
        Verify maximum width text box ignores the space and value appears as 50%
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value='Portal with 50 % Three level nav (50 space %)')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(edit_value='50 %')
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(click_on_label=True)
        util_obj.wait_for_page_loads(10)
        portal_obj.maximum_width_textbox_in_new_or_edit_portal_dialog(verify_value='50%', step_number='31.1')
        
        """
        Step 32: Click cancel
        """
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
        
        """
        Step 33: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()