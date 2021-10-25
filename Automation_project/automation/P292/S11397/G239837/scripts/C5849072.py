'''
Created on April 3, 2019

@author: varun
Testcase Name : Verify drag and drop folder/item content area to tree
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/5849072
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators

class C5849072_TestClass(BaseTestCase):
    
    def test_C5849072(self):
        """
        Test case objects
        """
        main_pages_obj = Wf_Mainpage(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        verify_message = "Are you sure you wish to move these resources?"
        repository_css = "div[class='ibfs-tree']"
        
        def drag_fex_from_content_area_to_tree(domain_item, tree_item):
            util_obj.synchronize_with_visble_text(loc_obj.content_area_css, domain_item, main_page_obj.home_page_medium_timesleep)
            drag_obj = main_pages_obj.get_domain_folder_item(domain_item)
            core_util_obj.left_click(drag_obj)
            drag_fex = core_util_obj.get_web_element_coordinate(drag_obj)
            drop_obj = main_pages_obj.get_repository_folder(tree_item)
            drop_folder = core_util_obj.get_web_element_coordinate(drop_obj)
            core_util_obj.drag_and_drop_without_using_click(drag_fex['x'], drag_fex['y'], drop_folder['x'], drop_folder['y'])
        
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click "Portal" folder under "P292_S11397"-> G239837" domain.
        """
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Portal')
        
        """
        Step 4: Drag "Small Widgets" subfolder from content area and drop it under "Reports" folders in the Tree.
        Verify Warning message display "Are you sure you wish to move these resources".
        """
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Portal')
        drag_fex_from_content_area_to_tree('Small Widgets', 'Reports')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", "Warning", main_page_obj.home_page_short_timesleep)
        observed_warning = util_obj.validate_and_get_webdriver_object("div[data-ibx-name=\"message\"]",'message').text.strip()
        util_obj.asequal(verify_message, observed_warning, "Step 4.1: Verify the warning message")
        
        """
        Step 5: Click on Yes.
        Verify "Small Widgets" folder is in "Reports" folder.
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['Small Widgets'], 'asin', 'Step 5.1: Verify documents in the under the G239837 folder')
        
        """
        Step 6: Drag "Small Widgets" from "Reports" folder and drop it back under "Portal" folder.
        """
        drag_fex_from_content_area_to_tree('Small Widgets', 'Portal')
        
        """
        Step 7: Click Yes.
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 8: Expand "Reports" folder and from content area drag "Margin by Product Category" and drop it under "Portal" folder in the Tree.
        """
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Reports')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        drag_fex_from_content_area_to_tree('Margin by Product Category', 'Portal')
        
        """
        Step 9: Click Yes.
        Verified "Margin by Product Category" is showing under "Portal" subfolder.
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Portal')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category'], 'asin', 'Step 9.1: Verify Margin By Prodyct under Portal')
        
        """
        Step 10: Drag "Margin by Product Category" from "Portal" folder and drop it under "Reports".
        """
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Portal')
        drag_fex_from_content_area_to_tree('Margin by Product Category', 'Reports')
        
        """
        Step 11: Click Yes. 
        Verified "Margin by Product Category" is showing under "Report" folder.
        """
        yes_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok-button')
        core_util_obj.left_click(yes_button)
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Reports')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category'], 'asin', 'Step 11.1: Verify Margin By Prodyct under Portal')
        
        """
        Step 12: In the banner link, click on the top right username > Click Sign Out and sign in as Advanced user.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """
        Step 13: Click on "Reports" folder from content area drag "Margin by Product Category" and drop it to My Content area in the Tree.
        Verify Drag and drop is not allowed.
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder(folder_name+'->'+group_id+'->'+'Reports')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Folders\"]", 'Folders', main_page_obj.home_page_medium_timesleep)
        drag_fex_from_content_area_to_tree('Margin by Product Category', 'My Content')
        main_page_obj.expand_repository_folder(folder_name+'->'+'My Content')
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category'], 'asnotin', 'Step 13.1: Verify Margin By Prodyct not  under Portal')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()