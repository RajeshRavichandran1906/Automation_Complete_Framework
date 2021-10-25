'''
Created on November 13, 2018

@author: varun
Testcase Name : Verify search for users/groups functionality
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261698
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C8261698_TestClass(BaseTestCase):
    
    def test_C8261698(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        domains_css = "div[title='Workspaces'] .ibx-label-text"
        folders_css = "div[data-ibxp-text=\"Folders\"] .ibx-label-text"
        share_css  = "div[title='Share']"
        drop_down_css = ".Share-with-menu-btn"
        menu_item_text_css = "div[data-ibx-type=\"ibxCheckMenuItem\"]"
        user_popup_css = ".Share-with-others-menu"
        text_to_type_css = ".ibx-widget .share-with-txt-search"
        advuser_css = ".share-with-dropdown .item-user-group .sw-item-desc"
        container_dialog_css = ".share-with-container-dialog"
        cancel_css = "div[data-ibxp-text=\"Cancel\"] .ibx-label-text"
        workspace = "Workspaces"
        
        """
        Step 1: Sign in to WebFOCUS as Developer user.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, workspace, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Workspaces->P292_S19901_G520454')
        
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        util_obj.synchronize_with_visble_text(folders_css,'Folders', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', 'Run')
        util_obj.wait_for_page_loads(10)
        core_util_obj.switch_to_new_window()
        
        """
        Step 4: Click on Share button from the personal page toolbar.
        """
        util_obj.synchronize_with_number_of_element(share_css, 1, Global_variables.mediumwait)
        share_element = util_obj.validate_and_get_webdriver_object(share_css,'Share-element')
        core_util_obj.python_left_click(share_element)
        
        """
        Step 5: Click on drop-down in the search box > Users/Groups (By default selected) in the drop-down list
        """
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, "drop_down_element")
        core_util_obj.python_left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(user_popup_css, 1, Global_variables.shortwait)
        verify_checked = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
        verify_dict = {}
        for element in verify_checked:
            verify_dict[element.text.strip()] = element.get_attribute('aria-checked')
        util_obj.asequal(verify_dict['Users/Groups'],'true',"Step 5.1: Verify Users/Groups selected")
        
        """
        Step 6: Enter 'Adv' in the 'Enter users/groups' search box.
        Verify users and groups with the name 'Adv'
        """
        util_obj.set_text_to_textbox_using_keybord('Adv', text_to_type_css)
        util_obj.synchronize_with_number_of_element(container_dialog_css, 1 , Global_variables.shortwait)
        user_elements = util_obj.validate_and_get_webdriver_objects(advuser_css,"Advanced_users")
        element_count = 0
        for element in user_elements:
            if element.text.strip().find('adv') or element.text.strip().find('Advanced Users'):
                element_count += 1
        element_present = True if element_count > 1 else False
        util_obj.asequal(element_present,True, "Step 6.1: Advanced users are present in the dropdown")
        
        """
        Step 7: Click Cancel button to close the Share with Others window.
        """
        cancel_button = util_obj.validate_and_get_webdriver_object(cancel_css, "Cancel-button")
        core_util_obj.python_left_click(cancel_button)
        util_obj.wait_for_page_loads(10)
        
        """
        Step 8: Close the portal run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main()
    