'''
Created on Dec 12, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667542
Testcase Name : Verify action Bar options Chart for Dev User
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.wftools import chart
from common.locators.dialog_locators import OpenMasterFileDialog

class C6667542_TestClass(BaseTestCase):


    def test_C6667542(self):
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
        Step 1: Sign into WebFOCUS Home Page as dev User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4: Click on 'InfoAssist' category button
        """
        main_page_obj.select_action_bar_tab('InfoAssist')
        
        """
        Step 5 : Click on 'Chart' action bar under 'InfoAssist' category
        """
        main_page_obj.select_action_bar_tabs_option('Chart')
        core_utilobj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(OpenMasterFileDialog.PARENT_CSS, Global_variables.mediumwait*5)
        
        """
        Verify the Master File Dialog is displayed
        """
        util_obj.verify_object_visible(OpenMasterFileDialog.PARENT_CSS, True, "Step 5:1 Verify open master file dialog is displayed")
        
        """
        Step 6 : Select 'wf_retail_lite.mas' > open
        """
        
        util_obj.select_masterfile_in_open_dialog('baseapp', 'wf_retail_lite')
        util_obj.synchronize_with_visble_text("#TableChart_1 [class='legend-labels!s0!']", 'Series 0', 30)
        
        
        """
        Verify that the default Chart is Displayed
        """
        chart_obj.verify_number_of_chart_segment("TableChart_1", 0, "Step 6:1: Verify number of chart segment")
        chart_obj.verify_number_of_risers("#TableChart_1 rect", 1, 25, 'Step 6:2: Verify number of risers')
        
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