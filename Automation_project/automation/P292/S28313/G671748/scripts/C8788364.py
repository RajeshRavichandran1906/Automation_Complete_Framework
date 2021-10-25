'''
Created on March 20, 2019

@author: Niranjan
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788364
Testcase Name : Verify action Bar Portal page option for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.pages import vfour_portal_canvas
from common.pages import vfour_portal_properties
from common.pages import vfour_portal_ribbon
from common.pages import vfour_miscelaneous
from common.lib import core_utility
from common.locators import wf_mainpage_locators

class C8788364_TestClass(BaseTestCase):

    def test_C8788364(self):
        
        """
        TESTCASE OBJECTS
        """
        workspace = "Workspaces"
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        vfour_portal_canvasobj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        vfour_portal_properties_obj=vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        vfour_portal_ribbon_obj=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_misc_obj=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        CSS
        """
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        add_page_capion_css="#dlgTitleExplorer [class*='active'] [class*='caption']"
        panel_content_css = "[id*='BidFolderBlockTree']"
        
        """
        TESTCASE VARIABLE
        """
        Testcase_id ='C8788364'
        domain_folder=workspace+'->Retail Samples'
        category_btn = 'Other'
        action_bar = 'Portal Page'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'Other' category button
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(category_btn)
        
        """
        Step 5: Click on 'Portal Page' action bar under 'Other' category
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(add_page_capion_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Verify Add Page dialog box is displayed
        """
        util_obj.verify_object_visible(add_page_capion_css, True, "Step 5: Verify caption of Add page")
        
        """
        Step 6:Select '1 Column' page template from Add Page dialog box
        Step 7: Enter title 'C8788364' and Click 'Create'
        """
        vfour_misc_obj.select_page_template(page_template='1 Column', Page_title=Testcase_id, Page_name=Testcase_id, btn_name="Create")
        
        """
        Verify 'C8788364' is displayed
        """
        vfour_portal_properties_obj.verify_input_control('page','Title', 'textbox', 'Step 7: Verify Title value is shown', textbox_value=Testcase_id)
        
        
        """
        Step 8 : Press 'F8' and drag and drop 'Retail Samples' to page
        """
        vfour_portal_ribbon_obj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        vfour_portal_canvasobj.dragdrop_repository_item_to_canvas(workspace+'->Retail Samples','column', 1)
        util_obj.synchronize_with_visble_text(panel_content_css, 'Retail Samples', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9 : Click BIP > Exit > Yes >Ok
        """
        vfour_portal_ribbon_obj.bip_save_and_exit('Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        
        """
        Verify 'C8788364' is displayed in content area
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, Testcase_id, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([Testcase_id], 'asin', "Step 9:Verify folder is displayed in the resource tree")
        
        """
        Step 10 : Right Click on 'C8788364' > Delete > Ok
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_id, context_menu_item_path='Delete', folder_path=workspace+'->Retail Samples')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, category_btn, main_page_obj.home_page_medium_timesleep)
        
        """
        Verify 'C8788364' is not displayed in content area
        """
        main_page_obj.expand_repository_folder(workspace+'->Retail Samples')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view([Testcase_id], 'asnotin', "Step 10:Verify folder is displayed in the resource tree")
        
        """
        Step 11: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()