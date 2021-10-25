'''
Created on Dec 18, 2018

@author: Vpriya
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6697103
Testcase Name : Delete a personal page as basic user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import designer_portal
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C6697103_TestClass(BaseTestCase):
    
    def test_C6697103(self):
        
        """
        CLASS OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Three_Level(self.driver)
        
        
        """
            Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
            Step 2:Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G514402')
        
        """
            Step 3:Right click on 'V5 Personal Portal_Nav-2' > Click Run.
            Verify 'V5 Personal Portal' opens in a new tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal_Nav-21','Run')
        
        """
            Step 4:Click delete icon on the top of the page heading.
            Verify delete warning dialog box displays.
        """
        coreutil_obj.switch_to_new_window()
        portal_obj.delete_page()
        portal_obj.verify_page_delete_dialog_is_displayed("Step 4:")
        portal_obj.verify_page_delete_dialog_message("Are you sure you want to delete 'Change Page' ?","Step 4.1")
        
        """
            Step 5:Click OK.
            Verify 'Change Page' page is deleted.
        """
        portal_obj.click_ok_button_in_page_delete_dialog()
        
        
        """
            Step 6:Close the 'V5 Personal Portal' run window.
        """
        coreutil_obj.switch_to_previous_window()

        """
            Step 7:In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        


if __name__ == "__main__":
    unittest.main()