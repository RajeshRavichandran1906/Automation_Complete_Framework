'''
Created on April 4,2019

@author: Niranjan/Samuel
Testcase Name : Verify drag and drop folder/item content area to content area
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/5849071
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators
import sys
import time
if sys.platform == 'linux':
    from pykeyboard import PyKeyboard
    pykeyboard = PyKeyboard()
else:
    import keyboard as system_keybord

class C5849071_TestClass(BaseTestCase):
    
    def test_C5849071(self):
        
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
        ok_button_css = ".pop-top [class*='ibx-dialog-ok-button']"
        pop_up_css = ".pop-top .ibx-dialog-content"
        
        """
        Test case variables
        """
        expected_domain = "P292_S11397"
        expected_folder = 'G239837'
        actual_pop_up = 'Are you sure you wish to move these resources?'
        
        """
        This local function is used to drag contents from content area to repsitory tree
        """
        def drag_fex_from_content_area_to_tree(domain_item, tree_item):
            util_obj.synchronize_with_visble_text(loc_obj.content_area_css, domain_item, main_page_obj.home_page_medium_timesleep)
            drag_obj = main_pages_obj.get_domain_folder_item(domain_item)
            core_utill_obj.left_click(drag_obj)
            drag_fex = core_utill_obj.get_web_element_coordinate(drag_obj)
            drop_obj = main_pages_obj.get_repository_folder(tree_item)
            drop_folder = core_utill_obj.get_web_element_coordinate(drop_obj)
            core_utill_obj.drag_and_drop_without_using_click(drag_fex['x'], drag_fex['y'], drop_folder['x'], drop_folder['y'])
            
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
         
        """ 
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
         
        """ 
        Step 3: Expand "Retail Sample_1" folder and copy "Reports", "Portal" folder to this domain folder "P292_S11397"-> G239837 
                Publish the folders.
        """
        main_page_obj.expand_repository_folder('Retail Samples_1')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        try:
            if sys.platform == 'linux':
                pykeyboard.press_key(pykeyboard.control_key)
            else:
                system_keybord.press('ctrl')
            pages_obj = main_pages_obj.get_domain_folder_item('Reports')
            core_utill_obj.python_left_click(pages_obj)
            pages_obj = main_pages_obj.get_domain_folder_item('Portal')
            core_utill_obj.python_left_click(pages_obj)
            time.sleep(5)
            main_page_obj.right_click_folder_item_and_select_menu('Reports', 'Copy')
        finally:
            if sys.platform == 'linux':
                pykeyboard.release_key(pykeyboard.control_key)
            else:
                system_keybord.release('ctrl')
             
        main_page_obj.collapse_repository_folder('Retail Samples_1')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        core_utill_obj.left_click(util_obj.validate_and_get_webdriver_object(loc_obj.content_area_css, 'Content Area'), element_location='middle_right',  xoffset=-9)
        if sys.platform == 'linux':
            pykeyboard.press_key(pykeyboard.control_key)
            pykeyboard.tab_key(character=u'\u0076')
            pykeyboard.release_key(pykeyboard.control_key)
        else:
            system_keybord.send('ctrl+v')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Reports', 'Publish')
        main_page_obj.verify_content_area_folder_publish_or_unpublish('Reports', 'publish', 'Step 03.00: Verify Reports is Publish')
        main_page_obj.right_click_folder_item_and_select_menu('Portal', 'Publish')
        main_page_obj.verify_content_area_folder_publish_or_unpublish('Portal', 'publish', 'Step 03.01: Verify Portal is Publish')
         
        """
        Step 4: Click on "P292_S11397"-> G239837" domain folder and drag Reports folder from content area then drop it under 
                Portals folder in content area.
        Verify Warning message display "Are you sure you wish to move these resources".
        """
        drag_obj = main_pages_obj.get_domain_folder_item('Reports')
        drag_folder = core_utill_obj.get_web_element_coordinate(drag_obj)
        drop_obj = main_pages_obj.get_domain_folder_item('Portal')
        drop_folder = core_utill_obj.get_web_element_coordinate(drop_obj)
        util_obj.drag_drop_on_screen(sx_offset=drag_folder['x'], sy_offset=drag_folder['y'], tx_offset=drop_folder['x'], ty_offset=drop_folder['y'])
        util_obj.verify_element_text(pop_up_css, actual_pop_up, 'Step 4.1: Verify Warning message displays as Are you sure you wish to move these resources')
         
        """
        Step 5: Click on Yes 
        Verify Reports folder is showing under Portals folder.
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Portal')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['Reports'], 'asin', 'Step 5.1: Verify Reports folder is showing under Portals folder')
         
        """
        Step 6: Click on Portals folder and from content area drag "Retail Sales Data" and drop it on "Reports" subfolder
        """
        drag_obj = main_pages_obj.get_domain_folder_item('Retail Sales Data')
        drag_fex = core_utill_obj.get_web_element_coordinate(drag_obj)
        drop_obj = main_pages_obj.get_domain_folder_item('Reports')
        drop_folder = core_utill_obj.get_web_element_coordinate(drop_obj)
        util_obj.drag_drop_on_screen(sx_offset=drag_fex['x'], sy_offset=drag_fex['y'], tx_offset=drop_folder['x'], ty_offset=drop_folder['y'])
         
        """
        Step 7: Click Yes
        Verified "Retail Sales Data" is showing under a "Reports" subfolder
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Portal'+'->'+'Reports')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Retail Sales Data', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Retail Sales Data'], 'asin', 'Step 7.1: Verified Retail Sales Data is showing under a Reports subfolder')
         
        """
        Step 8: Drag "Reports" folders under "Portal" folders in content area andl drop it on "P292_S11397"-> G239837 folder in the tree
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Portal')
        drag_fex_from_content_area_to_tree('Reports', expected_folder)
         
        """
        Step 9: Click Yes
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
         
        """
        Step 10: Drag "Margin by Product Category" from "Reports" folder in content area and drop it under portal folder in the tree.
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Reports')
        drag_fex_from_content_area_to_tree('Margin by Product Category', 'Portal')
         
        """
        Step 11: Click Yes
        Verified "Margin by Product Category" is showing under a "Portal" subfolder.
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Portal')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category'], 'asin', 'Step 11.1: Verified Margin by Product Category is showing under a Portal subfolder')
        drag_fex_from_content_area_to_tree('Margin by Product Category', 'Reports')
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        
        """
        Step 12: In the banner link, click on the top right username > Click Sign Out and sign in as Advanced user
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """
        Step 13: From content area drag items under "Reports" and drop it under My Content folder in the Tree
        Verify Drag and drop is not allowed.
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Reports')
        drag_fex_from_content_area_to_tree('Sales Metrics YTD', 'My Content')
        main_page_obj.expand_repository_folder(expected_domain+'->'+'My Content')
        util_obj.synchronize_until_element_is_visible(loc_obj.content_area_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Sales Metrics YTD'], 'asnotin', 'Step 13.1: Verify Drag and drop is not allowed')
        
        """
        Step 14: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()