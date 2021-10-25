'''
Created on March 11, 2019

@author: Niranjan/Samuel
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8788356
Testcase Name : Verify action Bar options Chart for Admin User
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import chart
from common.locators.dialog_locators import OpenMasterFileDialog
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8788356_TestClass(BaseTestCase):


    def test_C8788356(self):
        
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
                
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        util_obj.synchronize_until_element_is_visible(WfMainPageLocators.REPOSITORY_TREE_CSS, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        util_obj.wait_for_page_loads(main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5 : Click on 'Chart' action bar under 'InfoAssist' category
        """
        util_obj.synchronize_with_number_of_element("div:not([class*='tpg-hidden'])>div>div.create-new-item[role='button']",6, main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option('Chart')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, main_page_obj.home_page_medium_timesleep)
        
        """
        Verify the Master File Dialog is displayed
        """
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 05.01: Verify open master file dialog is displayed")
        
        """
        Step 6 : Select 'wf_retail_lite.mas' > open
        """     
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_visble_text("#TableChart_1 [class='legend-labels!s0!']", 'Series 0', main_page_obj.home_page_long_timesleep)
              
        """
        Verify that the default Chart is Displayed
        """
        chart_obj.verify_number_of_chart_segment("TableChart_1", 0, "Step 06.01: Verify number of chart segment")
        chart_obj.verify_number_of_risers("#TableChart_1 rect", 1, 25, 'Step 06.02')
        
        """
        Step 7 : Click on IA Globe > Exit
        """
        chart_obj.select_ia_exit_from_application_btn()
        
        """
        Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        core_utilobj.switch_to_previous_window(window_close=False)   
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()