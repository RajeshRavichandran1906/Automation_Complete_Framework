'''
Created on March 15, 2019

@author: AA14564
Testcase Name : Verify action Bar Text editor for Admin User
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8788370
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods


class C8788370_TestClass(BaseTestCase):
    
    def test_C8788370(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        content_box_css = ".content-box"
        
        """
        Test case variables
        """
        case_id = "C8788370"
        
            
        def save_in_editor_menu_icon(self,Menu):
            menu_icon=self.driver.find_element_by_css_selector('[style*="logo"]')
            core_util_obj.left_click(menu_icon)
            Menu_Path=Menu.split('->')
            for menu in Menu_Path:
                menu_obj = [menu_objs for menu_objs in self.driver.find_elements_by_css_selector(".pop-top [data-ibx-type*='ibxMenuItem']") if menu_objs.text.strip() == menu][0]
                core_util_obj.left_click(menu_obj)
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text('div.crumb-box', 'Workspaces', main_page_obj.home_page_medium_timesleep)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Domains > Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Domains->Retail Samples')
        util_obj.synchronize_with_visble_text(content_box_css, 'Other', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'Other' category button
        """
        main_page_obj.select_action_bar_tab("Other")
        """
        Step 5: Click on 'Text Editor' action bar > Select 'FOCEXEC(fex)'
        Verify Texteditor window opens with the New FOCEXEC file tab
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'Text Editor', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option("Text Editor")
        main_page_obj.select_action_bar_new_text_resource_tab("Content")
        main_page_obj.select_action_bar_new_text_resource_tab_option("FOCEXEC (fex)")
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible('[class*="ibx-tab-button"]', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Click on Application menu > Save > Enter title as 'C6667556' > Click Save
        """
        save_in_editor_menu_icon(self,"Save")
        button_row_css = ".pop-top div[class*='cancel']"
        util_obj.synchronize_with_visble_text(button_row_css, 'Cancel', 20)
        util_obj.synchronize_with_number_of_element("[role='textbox']", 6, main_page_obj.home_page_medium_timesleep)
        main_page_obj.enter_new_folder_title_in_popup_dialog(case_id)
        main_page_obj.click_button_on_popup_dialog("Save")
        
        """
        Step 7: Click on Application menu > Exit 
        Verify that 'C6667556' is displayed in the content area
        """
        util_obj.wait_for_page_loads(10)
        save_in_editor_menu_icon(self,"Exit")
        
        """
        Step 8: Right click on 'C8788370' > Delete > Click Yes in the 'Delete' dialog box
        Verify that 'C6667556' is not displayed in the content area
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(content_box_css, 'Other', main_page_obj.home_page_medium_timesleep)
        util_obj.wait_for_page_loads(10)
        main_page_obj.right_click_folder_item_and_select_menu(case_id, "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
        
        """
        Step 9 : In the banner link, Click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()