'''
Created on December 13, 2018

@author: KK14897
Testcase Name : Verify Portal action bar for dev user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/C8261619
'''
import unittest
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools import designer_portal
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase

class C8261619_TestClass(BaseTestCase):
    
    def test_C8261619(self):
        """
        Test_case objects
        """
        utils = UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        dp_obj = designer_portal.Portal(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Test case variables
        """
        domains_repository = 'Domains->Retail Samples'
        
        """
        Step 01: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 02: Click Content View from the side bar
        Step 03: Click on Retail Samples from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder(domains_repository)
        
        """
        Step 04: Click on 'Designer' category button
        """
        main_page_obj.select_action_bar_tab("Designer")
        
        """
        Step 05: Click on 'Portal' action bar
        """
        main_page_obj.select_action_bar_tabs_option("Portal")
        
        """
        Step 06: Enter title 'C6983794' > Create
        """
        dp_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value="C6983794")
        dp_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 07: Right click on 'C6983794' > Delete > Ok
        """
        utils.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu("C6983794", "Delete")
        main_page_obj.click_button_on_popup_dialog("OK")
        
        """
        Step 08: In the banner link, click on the top right username > Click Sign Out.
        """
        utils.wait_for_page_loads(main_page_obj.home_page_long_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()