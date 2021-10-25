'''
Created on Nov 27, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6694012
Testcase Name : Delete a personal page as basic user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import designer_portal

class C6694012_TestClass(BaseTestCase):
    
    def test_C6694012(self):
        
        """
        CLASS OBJECTS
        """
        login_o = login.Login(self.driver)
        main_page_o = wf_mainpage.Wf_Mainpage(self.driver)
        util_o = utillity.UtillityMethods(self.driver)
        coreutil_o = core_utility.CoreUtillityMethods(self.driver)
        portal_o = designer_portal.Two_Level_Side(self.driver)
        
        """
        TESTCASE VARIBALE
        """
        
        """
        CSS
        """
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        
        """
            Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_o.invoke_home_page('mridbas', 'mrpassbas')
        
        """
            Step 2:Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_o.select_content_from_sidebar()
        util_o.synchronize_with_number_of_element(crumb_css, 1, 20)
        main_page_o.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
            Step 3:Right click on 'V5 Personal Portal' > Click Run.
            Verify 'V5 Personal Portal' opens in a new tab.
        """
        main_page_o.right_click_folder_item_and_select_menu('V5 Personal Portal','Run')
        
        """
            Step 4:Click delete icon on the top of the page heading.
            Verify delete warning dialog box displays.
        """
        coreutil_o.switch_to_new_window()
        portal_o.delete_page()
        portal_o.verify_page_delete_dialog_is_displayed("Step 4:")
        portal_o.verify_page_delete_dialog_message("Are you sure you want to delete 'Change Page' ?","Step 4.1")
        
        """
            Step 5:Click OK.
            Verify 'Change Page' page is deleted.
        """
        portal_o.click_ok_button_in_page_delete_dialog()
        portal_o.verify_pages_not_displayed_under_the_folder_in_left_sidebar('My Pages','Change Page','Step 5')
        
        """
            Step 6:Close the 'V5 Personal Portal' run window.
        """
        coreutil_o.switch_to_previous_window()

        """
            Step 7:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_o.signout_from_username_dropdown_menu()
        


if __name__ == "__main__":
    unittest.main()