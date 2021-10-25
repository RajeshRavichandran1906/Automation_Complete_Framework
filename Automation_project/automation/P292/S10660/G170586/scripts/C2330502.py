'''
Created on July 22, 2019.

@author: Niranjan_Das/Prasanth

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2330502
TestCase Name = Edit page with special characters
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.lib.global_variables import Global_variables

class C2330502_TestClass(BaseTestCase):

    def test_C2330502(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        case_id=Global_variables.current_test_case
        
        
        """
        TESTCASE VARIABLES
        """
        domain = "Workspaces"
        action_tile = 'Designer'
        action_bar  = 'Page'
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        folder_name="""P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./"""
        
        """
        Step 1: Login WF as domain developer.
        Click on Content view from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 2: Click on 'P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./' domain;
        Choose Page action tile from under Designer category.
        """
        main_page_obj.expand_repository_folder(domain)
        folder = self.driver.find_element_by_xpath("//div[contains(@class, 'ibfs-tree')]//div[contains(text(), 'P292_S10660~!@#$%^&*()_+=-`')]")
        utillity.JavaScript(self.driver).scrollIntoView(folder)
        core_util_obj.left_click(folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 3: Choose the Grid 2-1 template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Grid 2-1', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 4: Click on "P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./'" domain to one level up;
        Navigate to Retail samples --> Portal --> Test Widgets folder.l
        """
        page_designer_obj.collapse_content_folder(folder_name)
        
        """ 
        Step 5: Drag Blue, Gray and Green onto the panels respectively.
        """
        page_designer_obj.drag_content_item_to_container("Blue", "Panel 1",content_folder_path="Retail Samples->Portal->Test Widgets")
        util_obj.synchronize_with_visble_text('div[data-ibxp-title*="TITLE_1"', "Blue", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_content_item_to_container("Gray", "Panel 2",content_folder_path=None)
        util_obj.synchronize_with_visble_text('div[data-ibxp-title*="TITLE_2"', "Gray", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_content_item_to_container("Green", "Panel 3",content_folder_path=None)
        util_obj.synchronize_with_visble_text('div[data-ibxp-title*="TITLE_3"', "Green", main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 6: Click Tool bar and click Save.
        Step 7:Enter "C2330502" in Title and click Save.
        """
        page_designer_obj.save_page_from_toolbar(case_id)
        
        """ 
        Step 8: Edit "C2330502" page.
        """
        core_util_obj.switch_to_previous_window()
        main_page_obj.right_click_folder_item_and_select_menu(case_id, "Edit")
        
        """ 
        Step 8.01 Expected: Verify that it loads with no errors
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text('div[data-ibxp-title*="TITLE_1"', "Blue", main_page_obj.home_page_medium_timesleep)
        page_designer_obj.verify_page_heading_title(['Page Heading'], msg="Step 08.01 : Verify Page heading")
        page_designer_obj.verify_page_header_visible_buttons(['Refresh'], msg="Step 08.02 : Verify Page header Visible buttons")
        
        page_designer_obj.switch_to_container_frame("Blue")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: blue;',"Step 08.03 : Verify color in Panel Blue")
        page_designer_obj.switch_to_default_page()
        
        page_designer_obj.switch_to_container_frame("Gray")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: dimgray;',"Step 08.04 : Verify color in Panel Gray")
        page_designer_obj.switch_to_default_page()
        
        page_designer_obj.switch_to_container_frame("Green")
        color_attribute=self.driver.find_element_by_css_selector("body").get_attribute("Style")
        util_obj.asequal(color_attribute,'background-color: green;',"Step 08.05 : Verify color in Panel Green")
        page_designer_obj.switch_to_default_page()              
        
        """ 
        Step 9: Close designer page.
        """
        page_designer_obj.switch_to_previous_window()
        
        """ 
        Step 8: Signout WF
        """
if __name__ == '__main__':
    unittest.main()                          
                                                        