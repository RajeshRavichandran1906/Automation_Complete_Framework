'''
Created on December 12, 2018

@author: Vpriya
Testcase Name : Verify action Bar Collaborative Portal for Dev
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6667549
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib import core_utility
from common.pages import vfour_miscelaneous
from common.pages import vfour_portal_ribbon

class C6667549_TestClass(BaseTestCase):
    
    def test_C6667549(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        vfour_misc_obj=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfour_portal_ribbon_obj=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        """
        Test case CSS
        """
        folders_text_css = "div[data-ibxp-text=\"Folders\"]"
        add_page_capion_css="#dlgTitleExplorer [class*='active'] [class*='caption']"
        navigator_css="div[id*='BipNavigatorButton']"
        
        """
        Test case variables
        """
        folders_text = 'Folders'
        Testcase_id='C6667549'
        expected_list=['C6667549']
        
        """
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the sidebar
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Other' category button > 'Collaborative Portal' action bar
        Verify 'New Portal' dialog box opens
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Collaborative Portal')
        
        """
        Step 5: Enter title 'C6667549' > Create
        Verify Add Page dialog box is displayed
        """
        main_page_obj.create_new_folder('C6667549')
        core_util_obj.switch_to_new_window()
        
        """
        Verify Add Page dialog box is displayed
        """
        util_obj.verify_object_visible(add_page_capion_css, True, "Step 5: Verify caption of Add page")
        
        """
        Step 6: Select '1 Column' > Create
        """
        vfour_misc_obj.select_page_template(page_template='1 Column', Page_title=Testcase_id, Page_name=Testcase_id, btn_name="Create")
        util_obj.synchronize_with_number_of_element(navigator_css,2,45)
        
        """
        Step 7: Click on BIP > Exit > Yes >Ok
        Verify the created 'C6667549' is displayed in content area
        """
        vfour_portal_ribbon_obj.bip_save_and_exit('Yes')
        core_util_obj.switch_to_previous_window(window_close=False)
        main_page_obj.verify_items_in_grid_view(expected_list, "asin","Step 7.1")
        
        """
        Step 7: Right Click on 'C6667549' > Delete > Ok
        Verify the created 'C6667549' is not displayed in content area
        """
        main_page_obj.right_click_folder_item_and_select_menu('C6667549','Delete')
        main_page_obj.click_button_on_popup_dialog('OK')
        main_page_obj.verify_items_in_grid_view(expected_list, "asnotin","Step 7.1")
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(folders_text_css, folders_text, base_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()