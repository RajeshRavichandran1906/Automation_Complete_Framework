'''
Created on April 5, 2018

@author: Niranjan/Samuel
Testcase Name : Test Link Pages
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261630
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer
from common.wftools.designer_portal import Two_Level_Side

class C8261630_TestClass(BaseTestCase):
    
    def test_C8261630(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        two_level_side_obj = Two_Level_Side(self.driver)
        
        """
        Test case CSS
        """
        portal_title_css = "[class*='pvd-portal-title']"
        close_css = ".pop-top  [class*='close-button']"
        pop_up_css = ".pop-top .ibx-dialog-content"
        
        """
        Test case variables
        """
        portal = 'v5portal1'
        page2_containers_title = ['Panel 1', 'Panel 3', 'Panel 2']
        page3_containers_title = ['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7', 'Panel 8', 'Panel 9']
        page4_containers_title = ['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7']
        actual_pop_up = "Are you sure you want to delete 'Page 2' ?"
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'V5 Domain Testing';
        """
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Designer', base_obj.home_page_medium_timesleep)
         
        """
        Step 4: Right click on V5 portal1 and click Run
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal,'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, portal, base_obj.home_page_medium_timesleep)
         
        """
        Step 5: Click on Page 2
        Verify Page 2
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar('v5folder1','Page 2')
        page_designer_obj.verify_containers_title(page2_containers_title, 'Step 5.1: Verify Page 1 containers title')
         
        """
        Step 6: Click on Page 3
        Verify Page 3
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar('v5folder1','Page 3')
        page_designer_obj.verify_containers_title(page3_containers_title, 'Step 6.1: Verify Page 1 containers title')
         
        """
        Step 7: Click on Page 4
        Verify Page 4
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar('v5folder1','Page 4')
        page_designer_obj.verify_containers_title(page4_containers_title, 'Step 7.1: Verify Page 1 containers title')
         
        """
        Step 8: Click on Page 5
        Verify Page 5
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar('v5folder1','Page 5')
        util_obj.verify_picture_using_sikuli('Page_5', msg='Step 8.1: Verify Page 5')
             
        """
        Step 9: Close portal run window
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 10: Right click on Page 1 and click Delete
        Verify warning message is displayed.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_long_timesleep)
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1->v5folder1')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page 2', main_page_obj.home_page_long_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page 2', 'Delete')
        util_obj.synchronize_with_visble_text('.pop-top', 'Page 2', main_page_obj.home_page_long_timesleep)
        util_obj.verify_element_text(pop_up_css, actual_pop_up, 'Step 10.1: Verify warning message is displayed')
        
        """
        Step 11: Close the warning
        """
        close_btn = util_obj.validate_and_get_webdriver_object(close_css, "close button")
        core_utill_obj.python_left_click(close_btn)
        util_obj.synchronize_until_element_disappear('.pop-top', main_page_obj.home_page_long_timesleep)
        
        """
        Step 12:Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()