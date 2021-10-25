'''
Created on May 31, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5853146
TestCase Name = Check Info Tooltip
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_design
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5853146_TestClass(BaseTestCase):

    def test_C5853146(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        pd_locator_obj = page_designer_design.ToolBar()
        
        """
        TESTCASE VARIABLES
        """
        fex_name = 'C5853145'
        repository_folder = 'Domains->P292_S11397->G435441'
        action_tile = 'Designer'
        report_action_bar = 'Report'
        exp_tooltip_title = 'Info mode'
        sleep_time = 5
        
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
        Step 03.00: Navigate to the folder P292_S11397/G435441;
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Right click on 'C5853145' and choose Edit
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, context_menu_item_path='Edit')
        sleep(sleep_time)
        
        """
        Step 04.00: From the designer toolbar hover the mouse on Info icon. 
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_locator_obj.INFO_MODE_BUTTON_CSS, 1, main_page_obj.home_page_medium_timesleep)
        info_mode_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'info mode icon')
        core_util_obj.python_move_to_element(info_mode_obj, mouse_move_duration=2)
        sleep(sleep_time)
        
        """
        Step 04.01: Verify the tooltip shows 'info mode'.
        """
        act_tooltip_title = util_obj.get_element_attribute(info_mode_obj, 'title')
        util_obj.asequal(exp_tooltip_title, act_tooltip_title, "Step 04.01: Verify the tooltip shows 'info mode'.")
        
        """
        Step 05.00: Click on application menu and click close
        """ 
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 06.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()