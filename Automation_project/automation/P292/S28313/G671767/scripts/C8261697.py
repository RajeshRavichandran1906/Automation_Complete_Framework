'''
Created on Nov 14, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/19901&group_by=cases:section_id&group_id=520454&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261697
TestCase Name = Verify search for groups functionality 
'''
import unittest, time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261697_TestClass(BaseTestCase):

    def test_C8261697(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        folder_name_path="Workspaces->P292_S19901_G520454"
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')

        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder(folder_name_path) 
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run')
        util_obj.wait_for_page_loads(10)
        core_utility_obj.switch_to_new_window() 
        time.sleep(Global_variables.longwait)
        
        """
        Step 4: Click on Share button from the personal page toolbar.
        """
        share_css="div[class^='pd-page-header'] div[class^='pd-header-buttons'] div[class*='button-share']"
        share_button_obj=util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        share_button_obj.click()
        
        """
        Step 5: Click on drop-down in the search box > Choose Groups in the drop-down list
        """
        share_dialog_css="div[class^='share-with-others-dialog']"
        util_obj.synchronize_with_number_of_element(share_dialog_css, '1', Global_variables.longwait)
        drop_down_css="div[class^='share-with-others-dialog'] div[class^='Share-with-menu-btn'] div[class*='caret-down']"
        drop_down_obj=util_obj.validate_and_get_webdriver_object(drop_down_css,'drop_down_css')
        drop_down_obj.click()
        drop_down_menu_css="div[class^='Share-with-others-menu']"
        util_obj.synchronize_with_number_of_element(drop_down_menu_css, '1', Global_variables.longwait)
        menu_items_css="div[class^='Share-with-others-menu'] div[class='ibx-label-text']"
        item_description='menu items in the drop-down list'
        menu_items=util_obj.validate_and_get_webdriver_objects(menu_items_css, item_description)
        item=menu_items[[elem.text.strip() for elem in menu_items].index('Groups')]
        item.click()
        time.sleep(Global_variables.mediumwait)
        
        """
        Step 6: Enter 'P292_S19901' in the 'Enter groups' search box.
        """
        input_text_msg='P292_S19901'
        search_box_css = "div[class^='share-with-others-dialog'] div[class^='share-with-txt-search'] input"
        search_box_elem=util_obj.validate_and_get_webdriver_object(search_box_css,'search input box')
        search_box_elem.click()
        time.sleep(Global_variables.mediumwait)
        keyboard.write(input_text_msg, 1)
        util_obj.synchronize_with_visble_text(search_box_css, input_text_msg, 45, text_option='text_value')
        
        """
        Verify groups with 'P292_S19901' name appears.
        """
        P292_S19901_css="#shareWithDropdown div[class^='item-user-group'] div[title^='P292_S19901']"
        P292_S19901_obj=util_obj.validate_and_get_webdriver_objects(P292_S19901_css, "Groups with 'P292_S19901' name appears")
        actual_user_list=[elem.text.strip() for elem in P292_S19901_obj]
        expected_user_list=['P292_S19901', 'P292_S19901', 'P292_S19901 Advanced Users', 'P292_S19901/AdvancedUsers', 'P292_S19901 Basic Users', 'P292_S19901/BasicUsers', 'P292_S19901 Developers', 'P292_S19901/Developers', 'P292_S19901 Group Administrators', 'P292_S19901/GroupAdmins']
        util_obj.as_List_equal(actual_user_list, expected_user_list, "Step 06: Verify groups with 'P292_S19901' name appears.")
        
        """
        Step 7: Click Cancel button to close the Share with Others window.
        """
        cancel_css = "div[class*='ibx-dialog-cancel-button']"
        cancel_button_obj = util_obj.validate_and_get_webdriver_object(cancel_css, 'Cancel_button')
        core_utility_obj.python_left_click(cancel_button_obj)
        util_obj.wait_for_page_loads(10)
       
        """
        Step 8: Close the portal run window.
        """
        core_utility_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()