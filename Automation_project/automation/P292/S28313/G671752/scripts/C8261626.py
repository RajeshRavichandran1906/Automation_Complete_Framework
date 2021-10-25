'''
Created on April 4, 2019

@author: varun
Testcase Name : Create Page inside the portal 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261626
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C8261626_TestClass(BaseTestCase):
    
    def test_C8261626(self):
        """
        Test_case objects
        """
        page_designer_obj = Design(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        action_bar_css = "div[data-ibxp-text=\"Action Bar\"]"
        new_page_css = ".ibx-title-bar-caption"
        
        """
        Test case variables
        """
        action_bar_text = "Action Bar"
        new_page_name = 'New Page'
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on the Content Sidebar.
        """
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Click on 'v5portal1'
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1->v5folder1')
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile in Action Bar
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 5: From New Page dialog select Grid 2-1 template
        """
        page_designer_obj.select_page_designer_template('Grid 2-1')
          
        """
        Step 6: Click save;
        Enter 'Page 1' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page 1')
          
        """
        Step 7: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 1', main_page_obj.home_page_short_timesleep)
          
        """
        Step 8: Click on Page action tile in Action Bar
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 9: From New Page dialog select Grid 2-1 Side template
        """
        page_designer_obj.select_page_designer_template('Grid 2-1 Side')
          
        """
        Step 10: Click save;
        Enter 'Page 2' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page 2')
          
        """
        Step 11: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 2', main_page_obj.home_page_short_timesleep)
          
        """
        Step 12: Click on Page action tile in Action Bar
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 13: From New Page dialog select Grid 3-3-3 template
        """
        page_designer_obj.select_page_designer_template('Grid 3-3-3')
          
        """
        Step 14: Click save;
        Enter 'Page 3' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page 3')
          
        """
        Step 15: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 3', main_page_obj.home_page_short_timesleep)
          
        """
        Step 16: Click on Page action tile in Action Bar
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 17: From New Page dialog select Grid 4-2-1 template
        """
        page_designer_obj.select_page_designer_template('Grid 4-2-1')
          
        """
        Step 18: Click save;
        Enter 'Page 4' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page 4')
          
        """
        Step 19: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 4', main_page_obj.home_page_short_timesleep)
          
        """
        Step 20: Click on Page action tile in Action Bar
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_css, new_page_name, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 21: From New Page dialog select Grid InfoApp 1 template
        """
        page_designer_obj.select_page_designer_template('InfoApp 1')
          
        """
        Step 22: Click save;
        Enter 'Page 5' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page 5')
  
        """
        Step 23: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 5', main_page_obj.home_page_short_timesleep)
         
        """
        Step 24: Right click Page 1 and click Publish
        Right click Page 2 and click Publish
        Right click Page 3 and click Publish
        Right click Page 4 and click Publish
        Right click Page 5 and click Publish
        Verify Page 1,Page 2,Page 3,Page 4 and Page 5 are published.
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page 1', 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [title*='Page 1']", main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page 2', 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [Title*='Page 2']", main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page 3', 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [Title*='Page 3']", main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page 4', 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [Title*='Page 4']", main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page 5', 'Publish')
        util_obj.synchronize_until_element_is_visible("div.files-box-files .fbx-block.fbx-column .file-item-published [Title*='Page 5']", main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page 1', 'publish', "Step 24.1: Verify page 1 is published")
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page 2', 'publish', "Step 24.2: Verify page 2 is published")
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page 3', 'publish', "Step 24.3: Verify page 3 is published")
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page 4', 'publish', "Step 24.4: Verify page 4 is published")
        main_page_obj.verify_content_area_item_publish_or_unpublish('Page 5', 'publish', "Step 24.5: Verify page 5 is published")
        
        """
        Step 25: Sign out WF.
        """        
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()