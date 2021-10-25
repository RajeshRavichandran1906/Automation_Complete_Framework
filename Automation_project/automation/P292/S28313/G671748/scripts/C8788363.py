'''
Created on March 13, 2019

@author: Niranjan
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788363
Testcase Name : Verify action Bar Collaborative Portal for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.lib import core_utility
from common.pages import vfour_miscelaneous
from common.pages import vfour_portal_ribbon

class C8788363_TestClass(BaseTestCase):
    
    def test_C8788363(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        vfour_misc_obj=vfour_miscelaneous.Vfour_Miscelaneous(self.driver)
        vfour_portal_ribbon_obj=vfour_portal_ribbon.Vfour_Portal_Ribbon(self.driver)
        
        """
        Test case CSS
        """
        content_box_css = ".content-box"
        add_page_capion_css="#dlgTitleExplorer .active.window .window-caption .bi-label"
        navigator_css="div[id*='BipNavigatorButton']"
        new_portal_capion_css = "[class^='create-new-collaborative-portal'] .ibx-label-text"
        ok_btn_css=".ibx-dialog-main-box .ibx-dialog-ok-button"
        
        """
        Test case variables
        """
        Testcase_id='C8788363'
        expected_list=['C8788363']
        domain_folder='Retail Samples'
        category_btn = 'Other'
        action_bar = 'Collaborative Portal'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder('Domains') 
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Other' category button > 'Collaborative Portal' action bar
        Verify 'New Portal' dialog box opens
        """
        main_page_obj.select_action_bar_tab(category_btn)
        util_obj.synchronize_with_visble_text(content_box_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        
        """
        Verify 'New Portal' dialog box opens
        """
        util_obj.verify_object_visible(new_portal_capion_css, True, "Step 04.01: Verify caption of New Portal dialog")
        
        """
        Step 5: Enter title 'C8788363' > Create
        Verify Add Page dialog box is displayed
        """
        main_page_obj.create_new_folder(Testcase_id)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(add_page_capion_css, 'Add Page', base_obj.home_page_medium_timesleep)
        
        """
        Verify Add Page dialog box is displayed
        """
        util_obj.verify_object_visible(add_page_capion_css, True, "Step 05.01: Verify caption of Add page")
        
        """
        Step 6: Select '1 Column' > Create
        """
        vfour_misc_obj.select_page_template(page_template='1 Column', Page_title=Testcase_id, Page_name=Testcase_id, btn_name="Create")
        util_obj.synchronize_with_number_of_element(navigator_css,2,45)
        
        """
        Step 7: Click on BIP > Exit > Yes >Ok
        Verify the created 'C8788363' is displayed in content area
        """
        vfour_portal_ribbon_obj.bip_save_and_exit('Yes')
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(expected_list, "asin","Step 07.01")
        
        """
        Step 8: Right Click on 'C8788363' > Delete > Ok
        Verify the created 'C8788363' is not displayed in content area
        """
        main_page_obj.right_click_folder_item_and_select_menu(Testcase_id,'Delete')
        util_obj.synchronize_with_visble_text(ok_btn_css, 'OK', 15)
        main_page_obj.click_button_on_popup_dialog('OK')
#         util_obj.synchronize_with_visble_text(content_box_css, category_btn, main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(expected_list, "asnotin","Step 08.01")
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()