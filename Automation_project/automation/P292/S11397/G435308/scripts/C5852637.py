'''
Created on June 11, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852637
TestCase Name = Show on ToolTip
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as miscellaneous_obj
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5852637_TestClass(BaseTestCase):

    def test_C5852637(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        pd_locator_obj = page_designer_locators.PageDesigner()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        
        """
        TESTCASE CSS
        """
        container_settings_pane_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings']"
        label_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings'] div[data-ibx-type='ibxLabel']"
        show_on_prop_css = "div[class^='container-settings'] div[data-ibxp-btn-options*='Container Settings'] div[data-ibx-row='{0}'].pd-container-device"
        desktop_icon_css = container_settings_pane_css+" .pd-container-device div[data-ibx-type='ibxRadioButton'][class*='desktop']"
        tablet_icon_css = container_settings_pane_css+" .pd-container-device div[data-ibx-type='ibxRadioButton'][class*='tablet']"
        mobile_icon_css = container_settings_pane_css+" .pd-container-device div[data-ibx-type='ibxRadioButton'][class*='mobile']"
        panel5_css = ".grid-stack-item-content div[data-ibxp-type='grid'] .pd-container-title-bar"
        panel6_css = ".grid-stack-item-content [data-ibx-type='pdContent'][data-ibxp-type*='explorer']"
        link_tile_css = ".grid-stack-item-content [data-ibx-type='pdContent'][data-ibxp-type='link_tile']"
        
        """
        TESTCASE VARIABLES
        """
        edit_fex_name = 'C5852637'
        domain = 'P292_S11397'
        repository_folder = 'Domains->'+domain+'->G435308'
        report_action_bar = 'Report'
        property_label = 'Show On'
        expected_list = ['Desktop', 'Tablet', 'Mobile']
        sleep_time = 9
        
        """
        Step 01.00: Login WF as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 02.00: Click on content view from side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Expand 'P292_S11397' domain -> 'G435308' folder
        """
        main_page_obj.expand_repository_folder(repository_folder)
        
        """
        Right click on 'C5852636' and click on Edit menu
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(edit_fex_name, context_menu_item_path='Edit')
        sleep(sleep_time)
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_locator_obj.PD_CONTAINER_CSS, 7, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 04.00: Right click on 'Panel 1' in canvas and choose Settings menu
        """
        page_designer_obj.select_container_context_menu('Panel 1', context_menu='Settings')
        
        """
        Step 04.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        labels = util_obj.validate_and_get_webdriver_objects(label_css, 'Container Settings labels')
        label_list = [el.text.strip() for el in labels if el.text.strip() != '']
        util_obj.asin(property_label, label_list, "Step 04.01a: Verify show on properties label appears")
        
        show_on_prop_obj = util_obj.validate_and_get_webdriver_object(show_on_prop_css.format(label_list.index(property_label)+1), 'Show on properties')
        prop_list = show_on_prop_obj.find_elements_by_css_selector("div[data-ibx-type='ibxRadioButton']")
        actual_list = [el.get_attribute('title') for el in prop_list]
        util_obj.as_List_equal(actual_list, expected_list, "Step 04.01b: Verify show on properties appear as below")
        
        """
        Step 05.00: Hover over the 3 icons under Show On section one by one
        Step 05.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        desktop_icon = util_obj.validate_and_get_webdriver_object(desktop_icon_css, 'desktop icon')
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        
        desktop_tooltip_title = util_obj.get_element_attribute(desktop_icon, 'title')
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 05.01a: Verify the Desktop appears as tool tip respectively")
        
        tablet_icon = util_obj.validate_and_get_webdriver_object(tablet_icon_css, 'tablet icon')
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        
        tablet_tooltip_title = util_obj.get_element_attribute(tablet_icon, 'title')
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 05.01b: Verify the Tablet appears as tool tip respectively")
        
        mobile_icon = util_obj.validate_and_get_webdriver_object(mobile_icon_css, 'mobile icon')
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        
        mobile_tooltip_title = util_obj.get_element_attribute(mobile_icon, 'title')
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 05.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 06.00: Right click on 'Panel 2' in canvas and choose Settings menu
        """
        page_designer_obj.select_container_context_menu('Panel 2', context_menu='Settings')
        
        """
        Step 06.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 06.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 06.01b: Verify show on properties appear as below")
        
        """
        Step 07.00: Hover over the 3 icons under Show On section one by one
        Step 07.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 07.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 07.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 07.01c: Verify the Mobile appears as tool tip respectively")
        
        
        """
        Step 08.00: Right click on 'Panel 3' in canvas and choose Settings menu
        """
        page_designer_obj.select_container_context_menu('Panel 3', context_menu='Settings')
        
        """
        Step 08.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 08.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 08.01b: Verify show on properties appear as below")
        
        """
        Step 09.00: Hover over the 3 icons under Show On section one by one
        Step 09.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 09.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 09.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 09.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 10.00: Right click on 'Panel 4' in canvas and choose Settings menu
        """
        page_designer_obj.select_container_context_menu('Panel 4', context_menu='Settings')
        
        """
        Step 10.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 10.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 10.01b: Verify show on properties appear as below")
        
        """
        Step 11.00: Hover over the 3 icons under Show On section one by one
        Step 11.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 11.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 11.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 11.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 12.00: Right click on 'Panel 5' in canvas and choose Settings menu
        """
        panel5_obj = util_obj.validate_and_get_webdriver_object(panel5_css, 'panel 5')
        core_util_obj.right_click(panel5_obj)
        miscellaneous_obj.select_page_designer_context_menu(self, 'Settings')
        
        """
        Step 12.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 12.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 12.01b: Verify show on properties appear as below")
        
        """
        Step 13.00: Hover over the 3 icons under Show On section one by one
        Step 13.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 13.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 13.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 13.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 14.00: Right click on 'Panel 6' in canvas and choose Settings menu
        """
        panel6_obj = util_obj.validate_and_get_webdriver_object(panel6_css, 'panel 6')
        core_util_obj.right_click(panel6_obj,  element_location='top_middle')
        miscellaneous_obj.select_page_designer_context_menu(self, 'Settings')
        
        """
        Step 14.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 14.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 14.01b: Verify show on properties appear as below")
        
        """
        Step 15.00: Hover over the 3 icons under Show On section one by one
        Step 15.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 15.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 15.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 15.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 16.00: Right click on Link tile widget in canvas and choose Settings menu
        """
        link_tile_obj = util_obj.validate_and_get_webdriver_object(link_tile_css, 'link tile widget')
        core_util_obj.right_click(link_tile_obj)
        miscellaneous_obj.select_page_designer_context_menu(self, 'Settings')
        
        """
        Step 16.01: Verify show on properties appear as below
        """
        util_obj.synchronize_with_number_of_element(container_settings_pane_css,1, main_page_obj.home_page_medium_timesleep)
        util_obj.asin(property_label, label_list, "Step 16.01a: Verify show on properties label appears")
        util_obj.as_List_equal(actual_list, expected_list, "Step 16.01b: Verify show on properties appear as below")
        
        """
        Step 17.00: Hover over the 3 icons under Show On section one by one
        Step 17.01: Verify Desktop, Tablet and Mobile appears as tool tip respectively
        """
        core_util_obj.python_move_to_element(desktop_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(desktop_tooltip_title, expected_list[0], "Step 17.01a: Verify the Desktop appears as tool tip respectively")
        core_util_obj.python_move_to_element(tablet_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(tablet_tooltip_title, expected_list[1], "Step 17.01b: Verify the Tablet appears as tool tip respectively")
        core_util_obj.python_move_to_element(mobile_icon, mouse_move_duration=2)
        sleep(sleep_time)
        util_obj.asequal(mobile_tooltip_title, expected_list[2], "Step 17.01c: Verify the Mobile appears as tool tip respectively")
        
        """
        Step 18.00: Close designer without saving
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 19.00: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()