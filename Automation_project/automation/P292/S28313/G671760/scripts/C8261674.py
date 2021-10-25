'''
Created on March 28,2019

@author: varun
Testcase Name : Login the other users for Portal/page
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261674
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.wftools.designer_portal import Two_Level_Side
from common.locators.portal_designer import Vfive_Designer

class C8261674_TestClass(BaseTestCase):
    
    def test_C8261674(self):
        """
        Test_case objects
        """
        two_level_side_obj = Two_Level_Side(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        repository_css = "div[class='ibfs-tree']"
        
        """
        Test case variables
        """
        left_sidebar_pages = ['Page Blank', 'Page Grid 2-1', 'Page Grid 2-1 Side', 'Page Grid 3-3-3', 'Page Grid 4-2-1', 'Page InfoApp 1' ]
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Right click on 'v5portal1-1' and select Run
        Verify portal appears as below
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains->V5 Domain Testing')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('v5portal1-1', 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, 'v5portal1-1', main_page_obj.home_page_medium_timesleep)
        portal_title = util_obj.validate_and_get_webdriver_object(portal_title_css, "portal title").text.strip()
        util_obj.asequal(portal_title, 'v5portal1-1', "Step 3.1: Verify the portal title")
        two_level_side_obj.verify_folders_in_left_sidebar(['Page Blank', 'Page Grid 2-1', 'Page Grid 2-1 Side', 'Page Grid 3-3-3', 'Page Grid 4-2-1', 'Page InfoApp 1', 'v5folder1', 'My Pages'], "Step 3.2: Verify the folders")
        two_level_side_obj.verify_all_pages_from_top_folder(left_sidebar_pages, "Step 3.3: Verify the pages in left side bar")
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 3.4: Verify page heading")
        
        """
        Step 4: Click on 'Page Blank'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page Blank')
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 4.1: Verify page heading")
        two_level_side_obj.verify_page_header_all_buttons(['Refresh'], "Step 4.2: Verify the refresh button")
        two_level_side_obj.verify_all_pages_from_top_folder(left_sidebar_pages, "Step 4.4: Verify the pages in left side bar")
        
        """
        Step 5: Click on 'Page Grid 2-1'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page Grid 2-1')
        util_obj.synchronize_with_number_of_element(Vfive_Designer.containers_css, 3, main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 5.1: Verify page heading")
        two_level_side_obj.verify_all_containers_title(['Panel 1','Panel 2','Panel 3'], 'Step 5.2: Verify the containers')
        two_level_side_obj.verify_page_header_all_buttons(['Refresh'], "Step 5.3: Verify the refresh button")
        
        """
        Step 6: Click on 'Page Grid 2-1 Side'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page Grid 2-1 Side')
        util_obj.synchronize_with_number_of_element(Vfive_Designer.containers_css, 3, main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 6.1: Verify page heading")
        two_level_side_obj.verify_all_containers_title(['Panel 1','Panel 3','Panel 2'], 'Step 6.2: Verify the containers')
        two_level_side_obj.verify_page_header_all_buttons(['Refresh'], "Step 6.3: Verify the refresh button")
        
        """
        Step 7: Click on 'Page Grid 3-3-3'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page Grid 3-3-3')
        util_obj.synchronize_with_number_of_element(Vfive_Designer.containers_css, 9, main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 7.1: Verify page heading")
        two_level_side_obj.verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7', 'Panel 8', 'Panel 9'], 'Step 7.2: Verify the containers')
        two_level_side_obj.verify_page_header_all_buttons(['Refresh'], "Step 7.3: Verify the refresh button")
        
        """
        Step 8: Click on 'Page Grid 4-2-1'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page Grid 4-2-1')
        util_obj.synchronize_with_number_of_element(Vfive_Designer.containers_css, 7, main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 8.1: Verify page heading")
        two_level_side_obj.verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7'], 'Step 8.2: Verify the containers')
        two_level_side_obj.verify_page_header_all_buttons(['Refresh'], "Step 8.3: Verify the refresh button")
        
        """
        Step 9: Click on 'Page infoApp 1'
        Verify portal appears as below
        """
        two_level_side_obj.select_page_from_top_folder('Page InfoApp 1')
        util_obj.synchronize_with_number_of_element("[data-ibx-type='pdPageRunner']:not([style*='none']) .pd-page-acc-section ", 2, main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_page_header_title("Page Heading", "Step 9.1: Verify page heading")
        icon_text = [element for element in util_obj.validate_and_get_webdriver_objects(".pd-page-acc-section .material-icons", "page_icon") if element.is_displayed()][0].text.strip()
        util_obj.asequal(icon_text, 'chevron_right', "Step 9.1: Verify icon on the infoapp page")
        
        """
        Step 10: Click on 'My Page' menu;
        Click the + Sign
        Verify choose template dialog appears as below
        """
        two_level_side_obj.click_on_plus_icon_under_the_folder_in_left_sidebar('My Pages')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", "New Page", main_page_obj.home_page_medium_timesleep)
        two_level_side_obj.verify_new_page_template_window_is_displayed("Step 10.1 Verify the new template is displayed")
        two_level_side_obj.verify_new_page_templates(['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1'], "Step 10.2: Verify the templates")
        
        """
        Step 11: Close template dialog
        """
        two_level_side_obj.close_new_page_template_window()
        
        """
        Step 12: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 13: Sign Out WF
        """
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()