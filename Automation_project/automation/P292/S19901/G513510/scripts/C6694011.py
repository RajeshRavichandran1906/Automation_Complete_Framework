'''
Created on November 27, 2018

@author: varun
Testcase Name : Edit the Page title as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6694011
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility

class C6694011_TestClass(BaseTestCase):
    
    def test_C6694011(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Run the portal by double click on 'V5 Personal Portal'.
        Verify 'V5 Personal Portal' opens in a new tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title,45)
        observed_portal_title = util_obj.validate_and_get_webdriver_object(portal_title_css,"portal name").text.strip()
        util_obj.asequal(expected_portal_title,observed_portal_title,"Step 3.1: Verify V5 Personal page opened in new window")
        
        """
        Step 4: Double click on 'Page 1' under My Pages.
        Step 5: Type title as 'Change Page' and hit enter key.
        Verify the title has been changed.
        """
        portal_obj.rename_page_under_the_folder_in_left_sidebar('My Pages', 'Page 1', 'Change Page')
        portal_obj.verify_specific_pages_under_the_folder_in_left_sidebar('My Pages', ['Change Page'], 'Step 5.1: Verify Change page is available in the side bar')
        
        """
        Step 6: Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        util_obj.synchronize_with_number_of_element(crumb_css,1,45)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()