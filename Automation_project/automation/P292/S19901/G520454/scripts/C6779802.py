'''
Created on November 15, 2018

@author: varun
Testcase Name : Verify able to share personal pages using Link to an existing page for multiple users
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779802
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.pages import portal_canvas,portal_sidebar

class C6779802_TestClass(BaseTestCase):
    
    def test_C6779802(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        portal_canvas_obj = portal_canvas.Portal_canvas(self.driver)
        portal_sidebar_object = portal_sidebar.Two_Level_SideBar(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        domains_css = "div[title='Domains'] .ibx-label-text"
        pd_title_css = ".pd-page-title .ibx-label-text"
        after_share_css = ".pd-header-button-share"
        dialog_content_css =".ibx-dialog-content"
        drop_down_css = ".Share-with-menu-btn"
        menu_item_text_css = "div[data-ibx-type=\"ibxCheckMenuItem\"]"
        user_popup_css = ".Share-with-others-menu"
        folders_css = ".content-title-label .ibx-label-text"
        text_to_type_css = ".ibx-widget .share-with-txt-search"
        user_css = ".share-with-dropdown .item-user-group .sw-item-desc"
        container_dialog_css = ".share-with-container-dialog"
        shared_with_text_css = ".share-with-title .ibx-label-text"
        user_verify_top_css =".share-with-container .share-with-item .sw-item-desc"
        ok_css = ".ibx-dialog-ok-button .ibx-label-text"
        dev_user = core_util_obj.parseinitfile('mriddev')
        basic_user = 'autobasuser08'
        expected_user_list = [basic_user,dev_user]
        containers_title=['Category Sales','Regional Sales Trend','Discount by Region','Regional Profit by Category',
                          'Example of a Tab Container','Example of a Carousel Container']
        
        """
        Step 1: Sign in to WebFOCUS as Admin user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
         
        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Domains',Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901_G520454')
         
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        Verify 'Sales Dashboard (Filtere...' appears in the sidebar and 'Retail Sales Dashboard' appears in the canvas
        """
        util_obj.synchronize_with_visble_text(folders_css,'Folders', Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share', 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pd_title_css, 'Retail Sales Dashboard',60)
        portal_sidebar_object.verify_pages_in_folder('My Pages',['Sales Dashboard (Filtered)'], msg="Step 3.1: Verify Sales dashboard in side bar", assert_type='asin')
        portal_canvas_obj.verify_page_header_title("Retail Sales Dashboard", "Step 3.2: Verify Title matches")
        portal_canvas_obj.verify_containers_title(containers_title,"Step 16.2: Verify container's title")
        
        """
        Step 4: Click on Share button from the personal page toolbar
        Verify 'Share with Others' dialog opens with already shared with 'autodevuser82' user
        """
        util_obj.synchronize_with_number_of_element("div[title='Stop sharing']", 1, Global_variables.longwait)
        portal_canvas_obj.click_on_page_header_button('Stop sharing')
        util_obj.synchronize_with_visble_text(shared_with_text_css,'Shared with', Global_variables.shortwait )
        util_obj.verify_object_visible(dialog_content_css, True, "Step 4.1: Verify Share with others window is open")
        user_name_text = util_obj.validate_and_get_webdriver_object(user_verify_top_css,"user-name").text.strip()
        util_obj.asequal(user_name_text,dev_user,"Step 4.2: Verify autodevuser82 is available")
        
        """
        Step 5: Click on drop-down in the search box > Choose Users in the drop-down list
        """
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, "drop_down_element")
        core_util_obj.python_left_click(drop_down_button)
        util_obj.synchronize_with_number_of_element(user_popup_css, 1, Global_variables.shortwait)
        user_items = util_obj.validate_and_get_webdriver_objects(menu_item_text_css, "menu_item")
        for element in user_items:
            if element.text.strip() == 'Users':
                core_util_obj.python_left_click(element)
                
        """
        Step 6: Enter 'autobasuser08' user in the 'Enter user' search box > Select 'autobasuser08' user
        Verify multiple users (autodevuser82 and autobasuser08 users) are selected and appears under 'Shared with'
        """
        input_element = util_obj.validate_and_get_webdriver_object(text_to_type_css,'text-css')
        core_util_obj.python_left_click(input_element)
        input_element.send_keys(basic_user) 
        util_obj.synchronize_with_number_of_element(container_dialog_css, 1 , Global_variables.shortwait)
        user_elements = util_obj.validate_and_get_webdriver_objects(user_css,"Basic_users")
        for element in user_elements:
            if element.text.strip() == basic_user:
                core_util_obj.python_left_click(element)
        util_obj.synchronize_with_visble_text(shared_with_text_css,'Shared with', Global_variables.shortwait )
        total_users = util_obj.validate_and_get_webdriver_objects(user_verify_top_css,"user-name")
        observed_users = []
        for user in total_users:
            observed_users.append(user.text.strip())
        util_obj.asequal(expected_user_list,observed_users,"Step 6.1: Verify the basic and dev user under share with ")
        
        """
        Step 7: Click the Ok button to close the 'Share with Others' dialog box
        Verify after sharing the personal page with multiple users (autodevuser82 and autobaseuser08 users) 
        still 'Share icon' appears in the blue color 
        """
        ok_element= util_obj.validate_and_get_webdriver_object(ok_css,"ok-element")
        core_util_obj.python_left_click(ok_element)
        util_obj.synchronize_with_number_of_element(after_share_css, 1, Global_variables.mediumwait)
        util_obj.verify_element_color_using_css_property(after_share_css, 'bright_cyan', "Step 7.1: Verify share button is still in blue color",attribute='color')
        
        """
        Step 8: Close the portal run window
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
        
        
        
        
        