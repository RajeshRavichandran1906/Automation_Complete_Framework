'''
Created on May 28, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262105
TestCase Name = Check thumbnail for folders
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262105_TestClass(BaseTestCase):

    def test_C8262105(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        page_preview_obj = Preview(self.driver)
        workspaces ="Workspaces"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = workspaces+'->Thumbnail Testing'
        action_tile = 'Designer'
        action_bar = 'Page'
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Click on 'Thumbnail Testing' domain
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Click on Page action tile from under Designer category 
        """
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 05.00: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.01: Verify blank page canvas appears as below
        """
        page_designer_obj.verify_number_of_page_sections(expected_total_sections=1, msg="Step 05.01a: Verify blank page canvas appears as below")
        page_designer_obj.verify_number_of_panels(expected_total_panels=0, msg="Step 05.01b: Verify blank page canvas appears as below")
        
        """
        Step 05.02: Verify thumbnail for 'Thumbnail Testing' domain appears as below
        """
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing'], "Step 05.02: Verify Thumbnail Testing domain appears.")
        
        """
        Step 06.00: Click on Domains node
        """
        page_designer_obj.collapse_content_folder(folder_path='Thumbnail Testing')
        sleep(8)
        
        """
        Step 06.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below
        """
        page_preview_obj.verify_page_domain_tree_node([workspaces, 'Public', 'Thumbnail Testing'], "Step 07.01: Verify 'Thumbnail Testing' domain and 'Public' folder will have the folder thumbnail as below")
        
        """
        Step 07.00: Click the arrow next to 'Thumbnail Testing' domain
        """
        page_designer_obj.expand_content_folder("Thumbnail Testing")
        
        """
        Step 07.01: Verify thumbnail for My Content folder appears as below
        Step 07.02: Verify thumbnail for Hidden Content appears as below
        """
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing', 'My Content'], "Step 07.01: Verify thumbnail for My Content folder appears as below")
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing', 'Hidden Content'], "Step 07.02: Verify thumbnail for Hidden Content appears as below")
        
        """
        Step 08.00: Double click 'Thumbnail Testing' domain
        """
        page_designer_obj.collapse_content_folder_by_double_click("Thumbnail Testing")
        
        """
        Step 08.01: Verify the domain is collapsed
        """
        page_preview_obj.verify_page_domain_tree_node([workspaces, 'Public', 'Thumbnail Testing', 'Retail Samples'], "Step 09.01: Verify the domain is collapsed")
        
        """
        Step 09.00: Double click 'Thumbnail Testing' domain
        """
        page_designer_obj.expand_content_folder_by_double_click("Thumbnail Testing")
        
        """
        Step 09.01: Verify the domain is expanded
        """
        page_preview_obj.verify_page_domain_tree_node(['Thumbnail Testing', 'My Content', 'Hidden Content'], "Step 09.01: Verify the domain is expanded")
        
        """
        Step 10.00: Save page as 'Thumbnail defaults' and close designer
        """ 
        page_designer_obj.save_page_from_toolbar('Thumbnail defaults')
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 11.00: Signout WF
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()