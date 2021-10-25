'''
Created on March 12, 2019

@author: Niranjan
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788357
Testcase Name : Verify action Bar Visualization option for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.locators.dialog_locators import OpenMasterFileDialog

class C8788357_TestClass(BaseTestCase):

    def test_C8788357(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        
        """
        CSS
        """
        repository_css = "div[class='ibfs-tree']"
        content_box_css = ".content-box"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
#         util_obj.synchronize_with_visble_text(repository_css, domain_folder, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder(domain_folder)
        util_obj.synchronize_with_visble_text(content_box_css, 'InfoAssist', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5 : Click on 'Visualization' action bar under 'InfoAssist' category
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'Visualization', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Visualization')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, main_page_obj.home_page_long_timesleep)
        
        """
        Verify the Master File Dialog is displayed
        """
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 5.1: Verify open master file dialog is displayed")
        
        """
        Step 6 : Select 'wf_retail_lite.mas' > open
        """
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_number_of_element("#TableChart_1 rect[class*='riser']", 12, main_page_obj.home_page_long_timesleep)
        
        """
        Verify that default Visualization Chart is Displayed
        """
        chart_obj.verify_number_of_risers("#TableChart_1 rect", 3, 4, 'Step 6.1: Verify number of risers')
        
        """
        Step 7 : Click on IA Globe > Exit
        """
        chart_obj.select_ia_exit_from_application_btn()
        core_utilobj.switch_to_previous_window(window_close=False)
        
        """
        Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        util_obj.synchronize_with_visble_text(content_box_css, 'InfoAssist', main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()