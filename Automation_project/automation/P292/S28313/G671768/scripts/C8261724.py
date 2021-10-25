'''
Created on Nov 1, 2018

@author: Vpriya
Testcase Name : Create portal with Two-level top navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261724
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.lib import utillity,core_utility
from common.pages import portal_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C8261724_TestClass(BaseTestCase):
    
    def test_C8261724(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_title = "v5-navigation-test3"
        content_area_text = "There are no pages available"
        content_area_css = ".files-no-search-results .ibx-label-text"
        user_css = ".pvd-menu-admin .ibx-label-text"
        user_name_parsed = core_util_obj.parseinitfile('mriddev')
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        portal_title_css = "div[class*='portal-title'] .ibx-label-text"
        
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait*5)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-navigation-test3' portal and select Edit
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', 15)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-navigation-test3';
        Name input box is filled automatically as 'v5-navigation-test3'
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', Global_variables.mediumwait)
        portal_designer_obj.create_or_edit_portal('Title', 'text_box', 'v5-navigation-test3')
        portal_designer_obj.verify_portal_dialog('Title', 'text_box', 'v5-navigation-test3', 'Step 4.1: Title verification')
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', 'v5-navigation-test3', 'Step 4.1: Title verification')
        
        """
        Step 5. Select 'Two-level-top' side navigation
        """
        portal_designer_obj.create_or_edit_portal('Navigation', 'radio_button', 'check', navigation_type="Two-level-top")
        
        """
        Step 6. Check 'Show top navigation in banner' checkbox.
        """
        portal_designer_obj.create_or_edit_portal('Show top navigation in banner','checkbox','check')
        
        """
        Step 7: Click Create'
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        
        """
        Step 8. Right click on 'v5-navigation-test3' and select Run from content area..
        """
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.mediumwait)
        main_page_obj.right_click_folder_item_and_select_menu('v5-navigation-test3','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_title,30)
        util_obj.verify_current_url('portal/P292_S19901/G520448/v5-navigation-test3', 'Step 9.1: URL verification in new window')
        title_css = ".pvd-portal-title .ibx-label-text"
        title_name = util_obj.validate_and_get_webdriver_object(title_css, 'title-css').text.strip()
        util_obj.asequal(title_name,expected_title,"Step 9.2: Title verification")
        content_area_text_search = util_obj.validate_and_get_webdriver_object(content_area_css, 'content-text-css').text.strip()
        util_obj.asequal(content_area_text,content_area_text_search,"Step 9.4: Content area text verification")
        user_name = util_obj.validate_and_get_webdriver_object(user_css, 'username-text-css').text.strip()
        util_obj.asequal(user_name_parsed,user_name,"Step 9.5: Username text verification")
        
        """
        Step 9: Close portal run mode.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 10: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()