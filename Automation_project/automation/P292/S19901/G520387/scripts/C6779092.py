'''
Created on October 17, 2018

@author: Varun
Testcase Name : Verify Role names title displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779092
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779092_TestClass(BaseTestCase):
    
    def test_C6779092(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        role_name_verification = ['WebFOCUSManagerDomainRestrictions', 'DomainAdvancedUser', 'DomainBasicUser', 'DomainDeveloperRestrictions', 'DomainDeveloper', 'DomainGroupAdminRestrictions', 'DomainGroupAdmin']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 2: Expand Domain > right click on Retail Samples > Security > Rules on this Resources
        """
        main_page_obj.select_option_from_crumb_box('Domains')
        main_page_obj.select_repository_folder_context_menu('Domains->Retail Samples','Security->Rules on this resource...')
        core_util_obj.switch_to_new_window()
        roles_css = ".col-2"
        role_values = util_obj.validate_and_get_webdriver_objects(roles_css,"roles-css")
        role_list = [elem.text.strip() for elem in role_values]
        util_obj.asequal(role_name_verification, role_list,"Step2 : verification of the Roles")
        
        """
        Step 3: Close the Rules window
        """
        core_util_obj.switch_to_previous_window()

        """
        Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
         
