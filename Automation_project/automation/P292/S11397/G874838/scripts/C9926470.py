'''
Created on Sep 23, 2019

@author: Robert
Testcase Name : Content Menu:Verify Multi Select items and actions such as duplicate/copy/delete/add to favorites.
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/9926470
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages.wf_mainpage import Wf_Mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators import wf_mainpage_locators
import keyboard

class C9926470_TestClass(BaseTestCase):
    
    def test_C9926470(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        home_page = Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        locatorsobj = wf_mainpage_locators.WfMainPageLocators()
        
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        folder_name_path="Domains->Retail Samples->Reports"
        
        
        Step1 = """
        Step 1: Launch WF_Home Page as Developer user.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
#         util_obj.synchronize_with_visble_text(".toolbar", "Workspaces", 120)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.longwait)
        util_obj.capture_screenshot("01.00", Step1)
        
        Step2 = """
        Step 2: Under Domain tree >> Navigate to Retail_Samples domain >> Click on 'Reports' folder.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(crumb_css, 1, Global_variables.longwait)
        util_obj.capture_screenshot("02.00", Step2)
        
        Step3 = """
        Step 3: Multi Select reports Margin by Product Category & Quantity Sold by Stores >> Right click.
        Step 03.00: Verify context menu,

        Duplicate.
        Cut.
        Copy.
        Delete.
        Add to Favorites.
        Publish.
        Hide.
        """
        util_obj.synchronize_with_visble_text(locatorsobj.content_area_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_visble_text(locatorsobj.content_area_css, 'Quantity Sold By Stores', main_page_obj.home_page_medium_timesleep)
        retun_obj = home_page.get_domain_folder_item('Margin by Product Category')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        retun_obj1 = home_page.get_domain_folder_item('Quantity Sold By Stores')
        keyboard.press('ctrl')
        core_util_obj.python_left_click(retun_obj1)
        core_util_obj.python_left_click(retun_obj)
        core_util_obj.right_click(retun_obj1)
        expected_list = ['Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide']
        home_page.verify_context_menu_item(expected_list, msg='Step 03.00')
        util_obj.capture_screenshot("03.00", Step3)
        
        Step4 = """
        Step 4: Select 'Duplicate' from the context menu.
        Step 04.00: Items will be duplicated with _1 for each name of the duplicated items.
        Margin by Product Category_1 & Quantity Sold by Stores_1
        """
        
        home_page.select_context_menu_item('Duplicate')
        keyboard.release('ctrl')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1', 'Quantity Sold By Stores_1'], 'asin', 'Step 04.00: ')
        util_obj.capture_screenshot("04.00", Step4)
              
        Step5 = """
        Step 5: Multi Select reports Margin by Product Category_1 & Quantity Sold by Stores_1 >> Right click >> Select 'Copy' from the context menu >> Paste to Retail_Samples/MyContent folder.
        Step 05.00: Verify reports were copied to My Content folder.
        """
        retun_obj = home_page.get_domain_folder_item('Margin by Product Category_1')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        retun_obj1 = home_page.get_domain_folder_item('Quantity Sold By Stores_1')
        core_util_obj.python_left_click(retun_obj1)
        keyboard.press('ctrl')
        core_util_obj.python_left_click(retun_obj)
        core_util_obj.right_click(retun_obj1)
        home_page.select_context_menu_item('Copy')
        keyboard.release('ctrl')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        folder_name_path="Domains->Retail Samples->My Content"
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(crumb_css, 'My Content', main_page_obj.home_page_long_timesleep)
        keyboard.press_and_release('ctrl+v')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1', 'Quantity Sold By Stores_1'], 'asin', 'Step 05.00: ')
        util_obj.capture_screenshot("05.00", Step5)
        
        Step6 = """
        Step 6: Multi Select reports Margin by Product Category_1 & Quantity Sold by Stores_1 >> Right click >> Select 'Add to Favorites' from the context menu.
        Step 06.00: Verify,
        """
        retun_obj = home_page.get_domain_folder_item('Margin by Product Category_1')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        retun_obj1 = home_page.get_domain_folder_item('Quantity Sold By Stores_1')
        keyboard.press('ctrl')
        core_util_obj.python_left_click(retun_obj1)
        core_util_obj.python_left_click(retun_obj)
        core_util_obj.right_click(retun_obj1)
        home_page.select_context_menu_item('Add to Favorites')
        util_obj.verify_notify_popup(notify_text="Favorites added", msg='Step 06.00')
        util_obj.wait_for_page_loads(10)
        util_obj.capture_screenshot("06.00", Step6)
        
        
        Step7 = """
        Step 7: Multi Select reports Margin by Product Category_1 & Quantity Sold by Stores_1 >> Right click >> Select 'Delete' from the context menu> Click OK.
        Step 07.00 : Verify duplicated items were deleted.
        """
        core_util_obj.right_click(retun_obj1)
        home_page.select_context_menu_item('Delete')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        util_obj.synchronize_with_number_of_element("div[class*='dialog-ok-button']",1, main_page_obj.home_page_long_timesleep)
        ok_element = util_obj.validate_and_get_webdriver_object("div[class*='dialog-ok-button']", 'ok button')
        core_util_obj.python_left_click(ok_element)
        keyboard.release('ctrl')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1', 'Quantity Sold By Stores_1'], 'asnotin', 'Step 07.00: ')
        util_obj.capture_screenshot("07.00", Step7)
        
        Step8 = """
        Step 8: From Side menu >> Select Add to Favorites
        Step 08.00 : Verify duplicated items were present under Favorites,
        """
        main_page_obj.select_favorites_from_sidebar()
        util_obj.synchronize_with_visble_text(locatorsobj.content_area_css, 'Margin by Product Category_1', main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1', 'Quantity Sold By Stores_1'], 'asin', 'Step 08.00: ')
        util_obj.capture_screenshot("08.00", Step8)
        
        Step9 = """
        Step 9: Multi-select Margin by Product Category_1 & Quantity Sold by Stores_1 > Remove from Favorites
        Step 09.00 : Verify items were removed.
        """
        retun_obj = home_page.get_domain_folder_item('Margin by Product Category_1')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        retun_obj1 = home_page.get_domain_folder_item('Quantity Sold By Stores_1')
        keyboard.press('ctrl')
        core_util_obj.python_left_click(retun_obj1)
        core_util_obj.python_left_click(retun_obj)
        core_util_obj.right_click(retun_obj1)
        home_page.select_context_menu_item('Remove from Favorites')
        keyboard.release('ctrl')
        util_obj.wait_for_page_loads(60, sleep_interval=1, pause_time=5)
        main_page_obj.verify_items_in_grid_view(['Margin by Product Category_1', 'Quantity Sold By Stores_1'], 'asnotin', 'Step 09.00: ')
        util_obj.capture_screenshot("09.00", Step9)
        
        Step10 = """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        util_obj.capture_screenshot("10.00", Step10)
        
if __name__ == '__main__':
    unittest.main()