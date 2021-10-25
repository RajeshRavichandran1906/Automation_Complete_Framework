'''
Created on October 19, 2018

@author: Varun
Testcase Name : Search Properties sections displays as capitalization standards
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261748
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools.paris_home_page import ParisHomePage

class C8261748_TestClass(BaseTestCase):
    
    def test_C8261748(self):
        
        """
        Test_case Objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        """
        Test_case variables
        """
        tab_css = "div[data-ibx-type=\"homePropertyPage\"] .ibx-tab-button"
        
        Step_01="""
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.wait_for_page_loads(30, pause_time=4)
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(20, pause_time=4)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        util_obj.capture_screenshot('01.00',Step_01)
        
        Step_02="""
        Step 2: Expand Domain > Retail Samples > click on Charts
        """
        util_obj.synchronize_with_visble_text('.crumb-box [title] .ibx-label-text', 'Workspaces', Global_variables.longwait)
        main_page_obj.select_option_from_crumb_box('Workspaces')
        util_obj.wait_for_page_loads(30, pause_time=2)
        HomePage.Workspaces.ResourcesTree.select('Retail Samples->Charts')
        util_obj.wait_for_page_loads(10, pause_time=2)
        util_obj.capture_screenshot('02.00',Step_02)
        
        Step_03="""
        Step 3: Right click on 'Bar - Highest Margin Products' > Properties > Advanced tab
        """
        main_page_obj.right_click_folder_item_and_select_menu('Bar - Highest Margin Products', 'Properties')
        util_obj.wait_for_page_loads(20, pause_time=4)
        util_obj.synchronize_with_number_of_element(tab_css, 4, Global_variables.mediumwait)
        main_page_obj.select_property_tab_value('Advanced')
        main_page_obj.verify_label_in_property_dialog('Advanced', 'Tags', '03.00')
        util_obj.capture_screenshot('03.00',Step_03)
        
        Step_04="""
        Step 4: Click Cancel to close the Properties window.
        """
        main_page_obj.close_property_dialog()
        util_obj.capture_screenshot('04.00',Step_04)
        
        Step_05="""
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        util_obj.capture_screenshot('05.00',Step_05)
        
if __name__ == '__main__':
    unittest.main()
    