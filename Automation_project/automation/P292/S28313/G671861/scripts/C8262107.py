'''
Created on May 29, 2019.

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262107
TestCase Name = Check for auto refresh of folder in PD
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview

class C8262107_TestClass(BaseTestCase):

    def test_C8262107(self):
        
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
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css = ".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        fex_name = 'Refresh Thumbnail'
        domain = 'Thumbnail Testing'
        repository_folder = 'Domains->Thumbnail Testing'
        action_tile = 'Designer'
        action_bar = 'Page'
        blank_template = 'Blank'
        folder_action_tile = 'Common'
        folder_action_bar = 'Folder'
        folder_name = "Refresh folder test"
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Click on 'Thumbnail Testing' domain and Click on Page action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """
        Step 04.00: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, blank_template, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template(blank_template)
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 05.00: Minimize page designer and invoke HOME page
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_short_timesleep)
        
        """
        Step 06.00: Click on 'Thumbnail Testing' domain and Click on Folder action tile
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, folder_action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(folder_action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, folder_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(folder_action_bar)
        
        """
        Step 07.00: Enter title as "Refresh folder test" and click ok
        """
        main_page_obj.create_new_folder(folder_name)
        
        """
        Step 08.00: Minimize HOME page and get back to page designer
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(containers_css,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 09.00: Click on Domains node to navigate up one level
        """
        page_designer_obj.collapse_content_folder(domain)
        
        """
        Step 10.00: Click on 'Thumbnail Testing' domain and expand it
        """
        page_designer_obj.expand_content_folder(domain)
        sleep(5)
        
        """
        Step 10.01: Verify "Refresh folder test" folder and its thumbnail appears as below
        """
        page_preview_obj.verify_page_domain_tree_node([folder_name], "Step 10.01: Verify 'Refresh folder test' folder and its thumbnail appears as below")
        
        """
        Step 11.00: Save page as 'Refresh Thumbnail' and close designer
        """ 
        page_designer_obj.save_page_from_toolbar(fex_name)
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 12.00: Signout WF
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, folder_action_tile, main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()