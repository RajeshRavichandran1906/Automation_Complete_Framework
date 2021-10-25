'''
Created on October 17, 2018

@author: Varun
Testcase Name : Verify New Domain title displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261744
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C8261744_TestClass(BaseTestCase):
    
    def test_C8261744(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        verification_title = "New Workspace"
        title_css = ".ibx-dialog-title-box div[class*=caption] .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
      
        """
        Step 2: Expand Domains > Click on Domain action bar
        """
        util_obj.synchronize_with_visble_text('.crumb-box [title] .ibx-label-text', 'Workspaces',  Global_variables.longwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        main_page_obj.select_action_bar_tabs_option('Workspace')
        util_obj.synchronize_with_visble_text(title_css, verification_title, Global_variables.mediumwait)
        obtained_title = util_obj.validate_and_get_webdriver_object(title_css, 'Domain-Title')
        util_obj.asequal(obtained_title.text, verification_title,"Step 02.01 : verification of the title")
          
        """
        Step 3: Click Cancel to close the dialog box. 
        """
        cancel_css = ".ibx-dialog-cancel-button .ibx-label-text"
        cancel_button_obj = util_obj.validate_and_get_webdriver_object(cancel_css, 'Cancel_button')
        core_util_obj.left_click(cancel_button_obj)
        
        """
        Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()