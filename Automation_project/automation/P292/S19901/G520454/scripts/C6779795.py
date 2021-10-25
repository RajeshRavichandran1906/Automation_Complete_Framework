'''
Created on November 13, 2018

@author: varun
Testcase Name : Share the personal page to basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779795
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.pages import portal_canvas

class C6779795_TestClass(BaseTestCase):
    
    def test_C6779795(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_canvas_obj = portal_canvas.Portal_canvas(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        domains_css = "div[title='Domains'] .ibx-label-text"
        folders_css = "div[data-ibxp-text=\"Folders\"] .ibx-label-text"
        share_css  = "div[title='Share']"
        after_share_css = ".pd-header-button-share"
        dialog_content_css =".ibx-dialog-content"
        drop_down_css = ".Share-with-menu-btn"
        menu_item_text_css = "div[data-ibx-type=\"ibxCheckMenuItem\"]"
        user_popup_css = ".Share-with-others-menu"
        text_to_type_css = ".ibx-widget .share-with-txt-search"
        user_css = ".share-with-dropdown .item-user-group .sw-item-desc"
        container_dialog_css = ".share-with-container-dialog"
        shared_with_text_css = ".share-with-title .ibx-label-text"
        user_verify_top_css =".share-with-container .share-with-item .sw-item-desc"
        user_verify_bottom_css = ".share-with-container .share-with-item .sw-item-name"
        close_button_css = ".sw-close-button .item-close-icon:not([style*='none'])"
        ok_css = ".ibx-dialog-ok-button .ibx-label-text"
        
        """
        Step 1: Sign in to WebFOCUS as Developer user.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Domains',Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901_G520454')
        
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        util_obj.synchronize_with_visble_text(folders_css,'Folders', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', 'Run')
        core_util_obj.switch_to_new_window()
        
        """
        Step 4: Click on Share button from the personal page toolbar.
        """
        util_obj.synchronize_with_number_of_element(share_css, 1, Global_variables.mediumwait)
        share_element = util_obj.validate_and_get_webdriver_object(share_css,'Share-element')
        core_util_obj.python_left_click(share_element)
        
        """
        Step 5: Click on drop-down in the search box > Choose Users in the drop-down list.
        """
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, "drop_down_element")
        core_util_obj.python_left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(user_popup_css, 1, Global_variables.shortwait)
        user_items = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
        for element in user_items:
            if element.text.strip() == 'Users':
                core_util_obj.python_left_click(element)
        
        """
        Step 6: Enter 'bas' in the 'Enter users' search box > Click on 'autobasuser08' user.
        Verify under 'Shared with' it shows 'autobasuser08' name as in bold and 'autobasuser08' 
        description as in normal text with x icon and 'Enter users' search box is empty
        """
        util_obj.set_text_to_textbox_using_keybord('bas', text_to_type_css)
        util_obj.synchronize_with_number_of_element(container_dialog_css, 1 , Global_variables.shortwait)
        user_elements = util_obj.validate_and_get_webdriver_objects(user_css,"Basic_users")
        for element in user_elements:
            if element.text.strip() == 'autobasuser08':
                core_util_obj.python_left_click(element)
        util_obj.synchronize_with_visble_text(shared_with_text_css,'Shared with', Global_variables.shortwait )
        top_element = util_obj.validate_and_get_webdriver_object(user_verify_top_css,"top_css")      
        font_type = util_obj.get_element_attribute(top_element, 'style').strip("font-weight:; ")
        util_obj.asequal(font_type,'bold','Step 6.1: Verify the username at top is bold ')
        bottom_element =util_obj.validate_and_get_webdriver_object(user_verify_bottom_css,"bottom_css")
        bottom_font_type = util_obj.get_element_attribute(bottom_element, 'style')
        util_obj.asequal(bottom_font_type,'','Step 6.2: Verify the username i8n the bottom is not bold')
        util_obj.verify_object_visible(close_button_css, True, "Step 6.3: Verify close button available")
        portal_canvas_obj.search_input_in_share_with_others_dialog(verify_value='',msg = "Step 6.4: Verify the search box is empty")
        
        """
        Step 7: Click OK.
        Verify Share with Others window closed.
        Verify after sharing the page to 'autobasuser08' 
        user 'Share icon' is changed into blue color
        """
        ok_element= util_obj.validate_and_get_webdriver_object(ok_css,"ok-element")
        core_util_obj.python_left_click(ok_element)
        util_obj.synchronize_with_number_of_element(after_share_css, 1, Global_variables.mediumwait)
        util_obj.verify_object_visible(dialog_content_css, False, "Step 7.1: Verify Share with others window is closed")
        util_obj.verify_element_color_using_css_property(after_share_css, 'bright_cyan', "Step 7.2: Verify the blue color in share button",attribute='color')
        
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
        
        
            
        