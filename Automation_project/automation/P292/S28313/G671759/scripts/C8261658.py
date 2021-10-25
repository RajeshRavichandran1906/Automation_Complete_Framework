'''
Created on March 22,2019

@author: Vpriya
Testcase Name : Test portal theme default settings with Developer
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261658
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer

class C8261658_TestClass(BaseTestCase):
    
    def test_C8261658(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj=page_designer.Design(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        caption_css=".ibx-title-bar-caption"
        tile_css=".pd-page-acc-section"
        properties_pan_css = "[title = 'Properties']"
        style_tab_css = "[class*= 'ibx-glyph-paint-brush']"
        theme_css = ".ibx-select-popup div[data-ibx-type='ibxSelectItemList'] div[class*='ibx-sm-selectable']"
        
        """
        Test case variables
        """
        expected_domain = "V5 Domain Testing"
        domains_text = 'Domains'
        expected_portal = 'v5portal1'
        portal_title='v5folder1'
        portal_subfolder_title='v5subfolder1'
        drop_down_css=".ibx-select-open-btn"
        
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        main_page_obj.select_option_from_crumb_box(domains_text)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ Step 3: Click on 'V5 Domain Testing' -> 'v5portal1' and choose Folder tile from action bar
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_portal)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'My Pages', main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option('Folder')
        util_obj.synchronize_with_visble_text(caption_css,'New Folder',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4:Enter title 'v5folder1' and click ok
        """
        main_page_obj.create_new_folder("v5folder1")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5:Right click on 'v5folder1' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, 'Publish')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_title,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6:Click on 'v5folder1' and choose Folder tile from action bar
        """
        main_page_obj.expand_repository_folder(portal_title)
        main_page_obj.select_action_bar_tabs_option('Folder')
        util_obj.synchronize_with_visble_text(caption_css,'New Folder',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7:Enter title 'v5subfolder1' and click ok
        """
        main_page_obj.enter_new_folder_title_in_popup_dialog(portal_subfolder_title)
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_subfolder_title,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8:Right click on 'v5subfolder1' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_subfolder_title, 'Publish')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, portal_subfolder_title,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 9:Click on 'V5 Domain Testing' -> v5portal1 -> v5folder1 -> v5subfolder1 and choose page tile from action bar
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_portal+'->'+portal_title+'->'+portal_subfolder_title)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(caption_css,'New Page',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10:Choose blank template
        """
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(tile_css, main_page_obj.home_page_medium_timesleep)
 
        """
        Step 11:Click on Properties panel -> Style
        """
        properties_pan = util_obj.validate_and_get_webdriver_object(properties_pan_css, 'properties_pan')
        core_utill_obj.left_click(properties_pan)
        style_tab = util_obj.validate_and_get_webdriver_object(style_tab_css, 'style_tab')
        core_utill_obj.left_click(style_tab)
 
        """
        Step 12:Click on Theme drop down
        Verify Theme drop down shows below options
        Designer 2018
        Light
        Midnight
        Custom Theme1
        
        """
        drop_down_elem=util_obj.validate_and_get_webdriver_object(drop_down_css,"Theme_dropdown")
        core_utill_obj.left_click(drop_down_elem)
        util_obj.synchronize_with_visble_text(".ibx-select-popup", "Designer", 30)
        theme_list_text = util_obj.validate_and_get_webdriver_objects(theme_css,'theme_dropdown_text')
        actual_list = [theme.text.strip() for theme in theme_list_text]
        expected_list = ['Designer 2018', 'Light', 'Midnight','Custom Theme2']
        util_obj.as_List_equal(actual_list, expected_list,"Step 12.00: Verify the theme drop down options")
        
        """
        Step 13:Click save;
        Enter 'Page Default' and click on save button
        """
        page_designer_obj.save_page_from_toolbar('Page Default')
         
        """
        Step 14:Exit designer
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 15:Right click on 'Page Default' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page Default', 'Publish')
        
        """
        Step 16:Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()