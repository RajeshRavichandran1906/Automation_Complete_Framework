'''
Created on June 04, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5853145
TestCase Name = Check Defaults
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_design, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5853145_TestClass(BaseTestCase):

    def test_C5853145(self):
        
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
        page_designer_locator_obj = page_designer_locators.PageDesigner()
        
        """
        TESTCASE VARIABLES
        """
        fex_name = 'C5853145'
        repository_folder = 'Domains->P292_S11397->G435441'
        report_action_bar = 'Report'
        expected_resource_label_value_list = ['Reference Path', 'Not set']
        expected_parameters_label_value_list = ['Parameters/Filters', 'None']
        sleep_time = 5
        
        """
        TESTCASE CSS
        """
        info_mode_css = "div[title='Info mode'].ibxtool-toolbar-button"
        resource_css = "div[class*='pdcnt-resource']"
        parameters_css = "div[class*='pdcnt-parameters']"
        
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
        
        """
        Step 04.00: Right click on 'C5853145' and choose Edit
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, context_menu_item_path='Edit')
        sleep(sleep_time)
        
        """
        Step 05.00: From the designer toolbar click on info mode button. 
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_locator_obj.INFO_MODE_BUTTON_CSS, 1, main_page_obj.home_page_medium_timesleep)
        info_mode_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'info mode icon')
        core_util_obj.left_click(info_mode_obj)
        sleep(sleep_time)
        
        """
        Step 05.01: Verify blue background appears after clicking info mode button.
        """
        util_obj.verify_element_color_using_css_property(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'summer_sky1', msg='Step 05.01: Verify blue background appears after clicking info mode button.', attribute='background-color')
        
        """
        Step 05.02: Verify Resource 'Not set' and Parameters 'None' for all the panels.
        """
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_PANEL_CSS, 7, main_page_obj.home_page_medium_timesleep)
        for i in range(1,8):
            page_designer_obj.verify_resource_label_value(i, expected_resource_label_value_list, step_num="05.02a.0"+str(i))
            page_designer_obj.verify_parameters_label_value(i, expected_parameters_label_value_list, step_num="05.02b.0"+str(i))
            
        """
        Step 06.00: Click info mode button. 
        """
        core_util_obj.left_click(info_mode_obj)
        #Once after clicking the infomode button, moving mouse cursor away from it, inorder to verify the background color.
        help_btn_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.HELP_BUTTON_CSS, 'help button')
        core_util_obj.move_to_element(help_btn_obj)
        sleep(sleep_time)

        """
        Step 06.01: Verify blue background disappears.
        """
        util_obj.verify_element_color_using_css_property(info_mode_css, 'nero', msg='Step 06.01: Verify blue background disappears.', attribute='background-color')
        
        """
        Step 06.02: Verify that all the panels back to its default state.
        """
        for i in range(1,8):
            resource_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+resource_css
            parameters_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+parameters_css
            for j, k in zip([resource_element_css, parameters_element_css], ['resource label value', 'parameters_element label value']):
                util_obj.verify_element_visiblty(element_css=j, visible=False, msg="Step 06.02.0"+str(i)+": Verify that all the panels back to its default state and "+k+" is disabled.")
        
        """
        Step 07.00: Close the Page Designer from application menu.
        """ 
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 08.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()