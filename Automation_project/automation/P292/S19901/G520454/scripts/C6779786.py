'''
Created on October 17, 2018

@author: Varun
Testcase Name : Verify New Domain title displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779089
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility

class C6779089_TestClass(BaseTestCase):
    
    def test_C6779089(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        verification_title = "New Domain"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Expand Domains > Click on Domain action bar
        """
        main_page_obj.select_option_from_crumb_box("Domains")
        main_page_obj.select_ribbon_button('Domain', repository_section_area='Domain')
        title_css = ".ibx-dialog-title-box div[class*=caption] .ibx-label-text"
        obtained_title = util_obj.validate_and_get_webdriver_object(title_css, 'Domain-Title')
        util_obj.asequal(obtained_title.text, verification_title,"Step1 : verification of the title")
          
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
    
        