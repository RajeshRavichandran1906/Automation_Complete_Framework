'''
Created on March 25,2019

@author: AA14564
Testcase Name : Create a Custom Theme(admin)
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261657
'''
import unittest
import time
import sys
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools.designer_portal import Portal
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
from common.pages.wf_mainpage import Wf_Mainpage
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as system_keybord

class C8261657_TestClass(BaseTestCase):
    
    def test_C8261657(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        portal_obj = Portal(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        pop_up_css = ".pop-top"
        
        """
        Test case variables
        """
        domains_text = 'Domains'
        expected_theme_list = ['theme', 'theme']
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content from side bar;
                Collapse Domains
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.collapse_repository_folder(domains_text)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand Global Resources ->Themes 
                Click on Custom folder and click on Folder tile
        """
        main_page_obj.expand_repository_folder('Global Resources->Themes')
        time.sleep(3)
        main_page_obj.click_repository_folder('Custom')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Folder', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Enter title 'Custom Theme1' and click ok.
        """
        main_page_obj.select_action_bar_tabs_option('Folder')
        util_obj.synchronize_with_visble_text(pop_up_css, 'Title', main_page_obj.home_page_medium_timesleep)
        main_page_obj.enter_new_folder_title_in_popup_dialog('Custom Theme1')
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Custom Theme1', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Expand Global Resources ->Themes ->Standard ->Midnight;
                Right click on theme.css and theme.sty files and copy theme
        """
        main_page_obj.expand_repository_folder('Global Resources->Themes->Standard->Midnight')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'theme', main_page_obj.home_page_medium_timesleep)
        try:
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                system_keybord.press('ctrl')
            theme_obj = main_pages_obj.get_domain_folder_item('theme')
            core_util_obj.python_left_click(theme_obj)
            theme_obj = main_pages_obj.get_domain_folder_item('theme',  item_name_index=2)
            core_util_obj.python_left_click(theme_obj)
            time.sleep(3)
            core_util_obj.python_right_click(theme_obj)
            main_pages_obj.select_context_menu_item('Copy')
        finally:
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                system_keybord.release('ctrl')
        
            
        """
        Step 6: Right click on 'Custom Theme1' and click Paste
                Verify theme.css and theme.sty files are now available under 'Custom Theme1'
        """
        main_page_obj.select_repository_folder_context_menu('Custom Theme1', 'Paste')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'theme', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(expected_theme_list, 'asin', 'Step 6: Verify theme.css and theme.sty files are now available under "Custom Theme1"')
        
        """
        Step 7: Right click on 'Custom Theme1' and click Publish
        """
        time.sleep(6)
        main_page_obj.select_repository_folder_context_menu('Custom Theme1', 'Publish')
        
        """
        Step 8: Collapse Global Resources and expand Domains
        """
        main_page_obj.collapse_repository_folder('Global Resources')
        time.sleep(6)
        
        """
        Step 9: Click on 'V5 Domain Testing' and choose Portal tile from under Designer tag from action bar
                Verify create portal dialog opens whereas 'Designer 2018' has been selected as default for Theme.
        """
        main_page_obj.expand_repository_folder('Domains')
        time.sleep(5)
        main_page_obj.expand_repository_folder('Domains->V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Portal', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(pop_up_css, 'Theme', main_page_obj.home_page_medium_timesleep)
        util_obj.validate_and_get_webdriver_object(pop_up_css, 'New portal dialog')
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='9')
        
        """
        Step 10: Click on Theme drop down
                 Verify Theme list appears as below
                 Designer 2018
                 Light
                 Midnight
                 Custom Theme1
        """
        portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(dropdown_list_value=['Designer 2018', 'Light', 'Midnight', 'Custom Theme1'], step_number='10')
        portal_obj.cancel_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 11: Sign out WF and close browser
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()