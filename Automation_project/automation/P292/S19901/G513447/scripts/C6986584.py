'''
Created on October 24, 2018

@author: vpriya
Testcase Name : Test Run menu using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6986584
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6986584_TestClass(BaseTestCase):
    
    def test_C6986584(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_obj=core_utility.CoreUtillityMethods(self.driver)
        breadcrumb_path="P292_S19901->G513445"
        medium_wait=60
        drop_down_css="div.pvd-menu-btn"
        Tab_name="Portal for Context Menu Testing"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder(breadcrumb_path)
        
        
        """
        Step 4: Right click on 'Portal for Context Menu ...'. 
        Right click on 'Portal for Context Menu ...' > Click Open
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Run')
        core_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(drop_down_css,1,medium_wait)
        util_obj.verify_current_tab_name(Tab_name,'step4:verify the current tab name')
        util_obj.verify_current_url('portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing','Step 4.1:verify the current url of the portal')
        
        """
        Step 5:Close the 'Portal for Context Menu Testing' run window 
        """
        core_obj.switch_to_previous_window()
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        