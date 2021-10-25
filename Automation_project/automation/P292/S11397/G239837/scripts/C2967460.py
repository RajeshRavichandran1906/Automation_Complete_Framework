'''
Created on April 3, 2019

@author: AA14564
Testcase Name : Verify Shortcut Keyboard keys
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/2967460
'''
import unittest
import sys
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as system_keyboard

class C2967460_TestClass(BaseTestCase):
    
    def test_C2967460(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        pop_up_css = ".pop-top"
        
        """
        Test case variables
        """
        expected_delete_msg = "Are you sure you want to delete 'Arc - Sales by Region' ?"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.wait_for_page_loads(10)
        
        """ Step 2: Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        main_page_obj.select_option_from_crumb_box('Domains')
        util_obj.synchronize_with_visble_text(".ibfs-tree", 'Retail Samples_1', 80)
        
        """ Step 3: Right click on 'Retail Samples_1' domain from the tree
                    Verify that the context menu shows Ctrl+V after Paste option (By default disabled)
        """
        main_page_obj.verify_repository_folder_context_menu('Retail Samples_1', ['Paste Ctrl+V'], msg='Step 3', comparision_type='asin')
        main_pages_obj.verify_context_menu_item(['Paste Ctrl+V'], msg='Step 3.1', row_css="div[data-ibx-type*='MenuItem'].ibx-widget-disabled")
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        
        """ Step 4: Right click on the 'Reports' folder from the content area
                    Verify that the context menu shows the following
                    Ctrl+X after Cut option
                    Ctrl+C after Copy option
                    Ctrl+V after Paste option (By default disabled)
                    DEL after Delete option
        """
        main_page_obj.verify_repository_folder_item_context_menu('Reports', ['Paste Ctrl+V'], msg='Step 4:', comparision_type='asin')
        main_pages_obj.verify_context_menu_item(['Paste Ctrl+V'], msg='Step 4.1', row_css="div[data-ibx-type*='MenuItem'].ibx-widget-disabled")
        
        """ Step 5: Click Reports folder under Retail Sample domain in tree
                    Click on "Margin by Product Category" in content area and press "Ctrl+C" from the keyboard.
        """
        main_page_obj.expand_repository_folder('Reports')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Margin by Product Category', main_page_obj.home_page_long_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Margin by Product Category', 'Copy')
        
        """ Step 6: Click anywhere on the empty canvas then press "Ctrl+V" in keyboard
                    Verified "Margin by Product Category" is copied
        """
        core_utill_obj.python_left_click(util_obj.validate_and_get_webdriver_object(loc_obj.content_area_css, 'Content Area'), element_location='middle_right',  xoffset=-9)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.tab_key(character=u'\u0076')
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            system_keyboard.send('ctrl+v')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=2)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Margin by Product Category_1', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1'], 'asin', 'Step 6: Verified "Margin by Product Category" is copied')
        
        """ Step 7: Click on charts folder under Retail Sample domain in tree select "Arc - Sales by Region" and press "Ctrl+X" in keyboard
        """
        main_page_obj.expand_repository_folder('Charts')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Arc - Sales by Region', main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Arc - Sales by Region', context_menu_item_path='Cut')
        
        """ Step 8: Click on Reports folder under Retail Sample domain in tree and click on the content area anywhere in the empty canvas then press "Ctrl+V"
                    Verify item is being cut and pasted to new location
        """
        main_page_obj.expand_repository_folder('Reports')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Margin by Product Category_1', main_page_obj.home_page_medium_timesleep)
        core_utill_obj.python_left_click(util_obj.validate_and_get_webdriver_object(loc_obj.content_area_css, 'Content Area'), element_location='middle_right',  xoffset=-9)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.tab_key(character=u'\u0076')
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            system_keyboard.send('ctrl+v')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=2)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Arc - Sales by Region', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Arc - Sales by Region'], 'asin', 'Step 8: Verify item is being cut and pasted to new location')
        
        """ Step 9: Click Reports folder right click on "Arc - Sales by Region" and select copy
                    and click Charts folder in tree click on the content area and press "Ctrl+V"
                    Verify the chart is being pasted properly under Charts folder
        """
        main_page_obj.right_click_folder_item_and_select_menu('Arc - Sales by Region', context_menu_item_path='Copy')
        main_page_obj.expand_repository_folder('Charts')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Bar - Highest Margin Products', main_page_obj.home_page_medium_timesleep)
        core_utill_obj.python_left_click(util_obj.validate_and_get_webdriver_object(loc_obj.content_area_css, 'Content Area'), element_location='middle_right',  xoffset=-9)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.tab_key(character=u'\u0076')
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            system_keyboard.send('ctrl+v')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=2)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Bar - Highest Margin Products', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Bar - Highest Margin Products'], 'asin', 'Step 9: Verify the chart is being pasted properly under Charts folder')
        
        """ Step 10: Click on Reports folder under Retail Sample in tree and click "Arc - Sales by Region" from the keyboard press Delete key
                    Verified confirmation deletion message appearing Arc - Sales by Region chart is deleted
        """
        main_page_obj.expand_repository_folder('Reports')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Arc - Sales by Region', main_page_obj.home_page_medium_timesleep)
        core_utill_obj.python_left_click(main_pages_obj.get_domain_folder_item('Arc - Sales by Region'))
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.tab_key(character=u'\u0076')
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            system_keyboard.send('del')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=2)
        util_obj.synchronize_with_visble_text(pop_up_css, 'Arc - Sales by Region', main_page_obj.home_page_medium_timesleep)
        actual_delete_msg = util_obj.validate_and_get_webdriver_object('{0} .ibx-dialog-content'.format(pop_up_css), 'Delete dialog').text.strip()
        util_obj.asequal(expected_delete_msg, actual_delete_msg, 'Step 10: Verified confirmation deletion message appearing Arc - Sales by Region chart is deleted.')
        """ Step 11: Click Cancel.
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """ Step 12: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()