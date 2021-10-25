'''
Created on Dec 13, 2018

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667550
Testcase Name : Verify action Bar Portal page option for Dev
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.global_variables import Global_variables
from common.pages import vfour_portal_canvas
from common.pages import vfour_portal_properties
from common.pages import vfour_portal_ribbon
from common.pages import vfour_miscelaneous
import time
from common.lib import core_utility


class C6667550_TestClass(BaseTestCase):

    def test_C6667550(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        vfour_portal_canvasobj=vfour_portal_canvas.Vfour_Portal_Canvas(self.driver)
        vfour_portal_properties_obj=vfour_portal_properties.Vfour_Portal_Properties(self.driver)
        vfour_portal_ribbon_obj=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        vfour_misc_obj=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        
        """
        CSS
        """
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        TESTCASE VARIABLE
        """
        Testcase_id ='C6667550'
        domain_folder='Retail Samples'
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'Other' category button
        """
        main_page_obj.select_action_bar_tab('Other')
        
        """
        Step 5: Click on 'Portal Page' action bar under 'Other' category
        """
        add_page_capion_css="#dlgTitleExplorer [class*='active'] [class*='caption']"
        main_page_obj.select_action_bar_tabs_option('Portal Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(add_page_capion_css, Global_variables.mediumwait*8)
        
        """
        Verify Add Page dialog box is displayed
        """
        util_obj.verify_object_visible(add_page_capion_css, True, "Step 5: Verify caption of Add page")
        
        """
        Step 6:Select '1 Column' page template from Add Page dialog box
        Step 7: Enter title 'C6667550' and Click 'Create'
        """
        vfour_misc_obj.select_page_template(page_template='1 Column', Page_title=Testcase_id, Page_name=Testcase_id, btn_name="Create")
        time.sleep(5)
        
        """
        Verify 'C6667550' is displayed
        """
        
        vfour_portal_properties_obj.verify_input_control('page','Title', 'textbox','Step 7: Verify Title value is shown', textbox_value=Testcase_id)
        
        """
        Step 8 : Press 'F8' and drag and drop 'Retail Samples' to page
        """
        vfour_portal_ribbon_obj.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        vfour_portal_canvasobj.dragdrop_repository_item_to_canvas('Domains->Retail Samples','column',1)
        
        """
        Step 9 : Click BIP > Exit > Yes >Ok
        """
        vfour_portal_ribbon_obj.bip_save_and_exit('Yes')
        core_utilobj.switch_to_previous_window(window_close=False)
        
        """
        Verify 'C6667550' is displayed in content area
        """
        content_files_css=".content-box.ibx-widget .files-box"
        util_obj.synchronize_with_visble_text(content_files_css, Testcase_id, 25)
        main_page_obj.verify_items_in_grid_view([Testcase_id], 'asin', "Step 9:Verify folder is displayed in the resource tree")
        
        """
        Step 10 : Right Click on 'C6667550' > Delete > Ok
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_id, context_menu_item_path='Delete', folder_path='Domains->Retail Samples')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', 15)
        main_page_obj.click_button_on_popup_dialog('OK')
        
        """
        Verify 'C6667550' is not displayed in content area
        """
        main_page_obj.expand_repository_folder('Domains->Retail Samples')
        main_page_obj.verify_items_in_grid_view([Testcase_id], 'asnotin', "Step 10:Verify folder is displayed in the resource tree")
        
        """
        Step 11: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()