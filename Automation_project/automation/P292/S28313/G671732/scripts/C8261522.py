'''
Created on April 10, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8261522
TestCase Name = Fix mouse pointer when hovering over Tiles and rows in on Desktop
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages import wf_mainpage as pages_main

class C8261522_TestClass(BaseTestCase):

    def test_C8261522(self):
        """
        TESTCASE VARIABLES
        """
        main_pages_obj = pages_main.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """ 
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar.
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 4: Hover over all the Category buttons
        (Common, Data, Designer, InfoAssist, Schedule, Other)
        Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        action_bar_list = ['Data', 'Designer', 'InfoAssist', 'Schedule', 'Other']
        for index, element in enumerate(action_bar_list):
            action_obj = main_pages_obj.get_action_bar_tab_object(element)
            core_util_obj.python_move_to_element(action_obj)
            cursor_attribute = util_obj.get_element_css_propery(action_obj, 'cursor')
            util_obj.asequal('pointer', cursor_attribute, "Step 4.{0}: Verify Link select is found in {1}".format(index+1, element))
    
        """
        Step 5: Hover over ALL the action tiles
        Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        action_bar_tab_options_list = main_pages_obj.get_action_bar_tab_options_name()
        for index, element in enumerate(action_bar_tab_options_list):
            action_obj = main_pages_obj.get_action_bar_tab_option_object(element)
            core_util_obj.python_move_to_element(action_obj)
            cursor_attribute = util_obj.get_element_css_propery(action_obj, 'cursor')
            util_obj.asequal('pointer', cursor_attribute, "Step 5.{0}: Verify Link select is found in {1}".format(index+1, element))

        """
        Step 6: Hover over the minus(-) sign on Retail Samples from the resource tree
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        retail_samples_obj = main_pages_obj.get_repository_folder('Retail Samples')
        minus_symbol = util_obj.validate_and_get_webdriver_object(".ibx-label-icon", 'minus symbol', retail_samples_obj)
        core_util_obj.python_move_to_element(minus_symbol)
        cursor_attribute = util_obj.get_element_css_propery(minus_symbol, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 6.1: Verify Normal select is found in - symbol")
        
        """
        Step 7: Hover the mouse over 'Portal' folder on the content area
        """
        portal_folder_obj = main_pages_obj.get_domain_folder_item('Portal')
        core_util_obj.python_move_to_element(portal_folder_obj)
        cursor_attribute = util_obj.get_element_css_propery(portal_folder_obj, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 7.1: Verify Normal select is found in Portal")
        
        """
        Step 8: Hover over the icon for the 'Portal' folder
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        portal_folder_obj = main_pages_obj.get_domain_folder_item('Portal')
        portal_icon = util_obj.validate_and_get_webdriver_object('.ibx-label-icon', 'portal-icon', portal_folder_obj)
        core_util_obj.python_move_to_element(portal_icon)
        cursor_attribute = util_obj.get_element_css_propery(portal_icon, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 8.1: Verify Normal select is found in Portal icon")
        
        """
        Step 9: Double click on Portal > Small Widgets Folder in content area
        """
        main_page_obj.double_click_folder_item_and_select_menu('Portal')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        main_page_obj.double_click_folder_item_and_select_menu('Small Widgets')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 10: Hover over a 'Category Sales' in the content area
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        util_obj.synchronize_with_visble_text(".content-box", 'Category Sales', main_page_obj.home_page_short_timesleep)
        category_obj = main_pages_obj.get_domain_folder_item('Category Sales')
        core_util_obj.python_move_to_element(category_obj)
        cursor_attribute = util_obj.get_element_css_propery(category_obj, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 10.1: Verify Normal select is found in Category Sales")
        
        """
        Step 11: Hover over the icon for 'Category Sales' in the content area
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        category_obj = main_pages_obj.get_domain_folder_item('Category Sales')
        category_icon = util_obj.validate_and_get_webdriver_object('.ibx-label-icon', 'portal-icon', category_obj)
        core_util_obj.python_move_to_element(category_icon)
        cursor_attribute = util_obj.get_element_css_propery(category_icon, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 11.1: Verify Normal select is found in category icon")
        
        """
        Step 12: Click on 'List view' in the banner link
        """
        main_page_obj.select_list_view()
        
        """
        Step 13: Click on Portal in resource tree
        """
        main_page_obj.expand_repository_folder('Portal')
        
        """
        Step 14: Hover the mouse over 'Small Widgets' folder on the content area
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        util_obj.synchronize_with_visble_text("div[title=\"Small Widgets\"] .ibx-label-text", 'Small Widgets', main_page_obj.home_page_short_timesleep)
        small_widgets_obj = util_obj.validate_and_get_webdriver_object("div[title=\"Small Widgets\"] .ibx-label-text", 'small_widgets')
        core_util_obj.python_move_to_element(small_widgets_obj)
        cursor_attribute = util_obj.get_element_css_propery(small_widgets_obj, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 14.1: Verify Normal select is found in small widgets")
        
        """
        Step 15: Hover over a 'Retail Samples' portal
        Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        retail_samples_obj = util_obj.validate_and_get_webdriver_object(".files-box-files-area div[title=\"Retail Samples\"] .ibx-label-text", 'retail_samples')
        core_util_obj.python_move_to_element(retail_samples_obj)
        cursor_attribute = util_obj.get_element_css_propery(retail_samples_obj, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 15.1: Verify Normal select is found in small widgets")
        
        """
        Step 16: Hover over the Column titles
        Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        column_titles_obj = util_obj.validate_and_get_webdriver_objects(".files-box-files-title .grid-cell-title", 'title_name')
        for index, element in enumerate(column_titles_obj):
            core_util_obj.python_move_to_element(element)
            cursor_attribute = util_obj.get_element_css_propery(element, 'cursor')
            util_obj.asequal('pointer', cursor_attribute, "Step 16.{0}: Verify Link select is found in {1}".format(index+1, element.text.strip()))
        
        """
        Step 17: Click on minus(-) sign on Retail Samples from the resource tree
        """
        retail_samples_obj = main_pages_obj.get_repository_folder('Retail Samples')
        minus_symbol = util_obj.validate_and_get_webdriver_object(".ibx-label-icon", 'minus symbol', retail_samples_obj)
        core_util_obj.python_move_to_element(minus_symbol)
        cursor_attribute = util_obj.get_element_css_propery(minus_symbol, 'cursor')
        util_obj.asequal('default', cursor_attribute, "Step 17.1: Verify Normal select is found in - symbol")
        
        """
        Step 18: Hover over 'Charts' folder on the resource tree
        Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        charts_obj = main_pages_obj.get_repository_folder('Charts')
        core_util_obj.python_move_to_element(charts_obj)
        cursor_attribute = util_obj.get_element_css_propery(charts_obj, 'cursor')
        util_obj.asequal('pointer', cursor_attribute, "Step 18.1: Verify link select is found in charts folder")
        
        """
        Step 19: Click on 'Grid view' in the banner link
        """
        main_page_obj.select_grid_view()
        
        """
        Step 20: Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        