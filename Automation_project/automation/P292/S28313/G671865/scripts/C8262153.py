'''
Created on December 21, 2018

@author: KK14897
Testcase Name : Edit the Page title as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262153
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility

class C8262153_TestClass(BaseTestCase):
    
    def test_C8262153(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj_2 = designer_portal.Three_Level(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal_Nav-2'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path='Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        items_css = 'div[data-ibxp-text="Items "] .ibx-label-text'
        pd_window_css = ".pd-filter-window .ibx-title-bar-caption .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_path)
        util_obj.synchronize_with_visble_text(items_css,'Items', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Run the portal by double click on 'V5 Personal Portal_Nav-2'.
        Verify 'V5 Personal Portal_Nav-2' opens in a new tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal_Nav-2','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title, main_page_obj.home_page_medium_timesleep)
        observed_portal_title = util_obj.validate_and_get_webdriver_object(portal_title_css,"portal name").text.strip()
        util_obj.asequal(expected_portal_title,observed_portal_title,"Step 3.1: Verify V5 Personal page opened in new window")
        
        """
        Step 4: Double click on 'Page 1' under My Pages.
        Step 5: Type title as 'Change Page' and hit enter key.
        Verify the title has been changed.
        """
        util_obj.synchronize_with_visble_text(pd_window_css, 'Selections', main_page_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog("Close")
        portal_obj_2.rename_page_from_left_navigation_bar('Page 1', 'Change Page base')
        portal_obj_2.verify_specific_item_in_left_navigation_bar(['Change Page base'], 'Step 5.1: Verify Change page is available in the side bar')
        
        """
        Step 6: Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(items_css,'Items', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()