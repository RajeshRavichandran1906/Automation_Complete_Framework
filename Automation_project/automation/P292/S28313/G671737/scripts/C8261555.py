'''
Created on October 24, 2018

@author: Robert
Testcase Name : Test Run menu using Developers
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261555
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261555_TestClass(BaseTestCase):
    
    def test_C8261555(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        project_id = util_obj.parseinitfile('project_id')
        suite_id = util_obj.parseinitfile('suite_id')
        group_id = util_obj.parseinitfile('group_id')
        crumbbox_css = ".crumb-box .ibx-label-text"
        nopage_css="#pagespane div[id^='ibx-aria-id-'] > div.ibx-label-text"
        txt_check="portal/{0}_{1}/{2}/Portal_for_Context_Menu_Testing".format(project_id, suite_id, group_id)
        ibi_logo_css="div[class^='home-banner ibx-widget'] div.banner-logo"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(ibi_logo_css, 1, 40, 1)
        """
        Step 2. Click Content View from the sidebar > Click on Domains from the resource tree
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
                
        """
        Step 3. Click on Portal View from the sidebar
        """
        main_page_obj.select_portals_from_sidebar()
        util_obj.synchronize_with_visble_text(crumbbox_css, 'Portals', 90)
        
        """
        Step 4. Right click on 'Portal for Context Menu Testing' > Click Run
        """
        main_page_obj.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Run')
        
        """
        Step 4.1. Verify that 'Portal for Context Menu Testing' portal run in a new tab and its URL as 'http://machine name:port/alias/portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(nopage_css, "There are no pages available", 30, 1)
        util_obj.verify_current_url(txt_check, 'Step 4.1 Verify the Portal for Context Menu Testing is in new tab and its URL')
        
        """
        Step 5. Close the 'Portal for Context Menu Testing' portal run window 
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6. In the banner link, click on the top right username > Click Sign Out.
        """
        
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        