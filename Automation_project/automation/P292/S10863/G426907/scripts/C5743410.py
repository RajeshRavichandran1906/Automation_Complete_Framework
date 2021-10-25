'''
Created on Jul 13, 2019

@author: Aftab

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743410
TestCase Name =Add long container title
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.wftools.page_designer import Design
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.locators import page_designer_design
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous
import uiautomation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uisoup import uisoup
import time
from common.lib.global_variables import Global_variables
from common.lib import javascript

class C5743410_TestClass(BaseTestCase):

    def test_C5743410(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        pd_designloactaors_obj = page_designer_design.ContentTab()
        javascript_obj=javascript.JavaScript(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        containers_css=".ibx-csl-items-container [title='Containers']"
        
        """
        TESTCASE VARIABLES
        """
        project_id  = core_util_obj.parseinitfile('project_id')
        suite_id    = core_util_obj.parseinitfile('suite_id')
        group_id    = core_util_obj.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        action_tile = 'Designer'
        action_bar  = 'Page'
        
        """
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S10863' domain -> 'G426906' folder;
        Click on Page action tile from under Designer category
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab(action_tile)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option(action_bar)
        core_util_obj.switch_to_new_window()
        
        """ 
        Step 4: Choose blank template
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_until_element_is_visible(containers_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 5: Drag and drop '!@#$%^&*()_+' report from under 'G426906' folder to the page canvas
        """
        page_designer_obj.drag_content_item_to_blank_canvas('!@#$%^&*()_+', 1)
        
        """ 
        Step 6 : Drag and drop Panel container next to first panel
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        util_obj.synchronize_with_visble_text(pd_designloactaors_obj.BASIC_CONTAINER_CSS, 'Panel', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas('Panel', 4)
        
        """ 
        Step 7 : Drag and drop 'Stacked Bar - Sales by Month and Product Category stacked bar' from Retail Samples -> Charts after second panel in a 3*3 order
                Verify the tool tip should not display the full title while dragging the container.
        """
        page_designer_obj.select_option_from_carousel_items('Content')
        page_designer_obj.collapse_content_folder('G426906->P292_S10863')
#        content_folder = 'Retail Samples->Charts'
#        page_designer_obj.drag_content_item_to_blank_canvas('Stacked Bar - Sales by Month and Product Category', 7, content_folder)
        page_designer_obj.expand_content_folder('Retail Samples->Charts')
        source_file_obj = pd_miscelaneous.find_pd_content_item_and_scroll_into_view(self,'Stacked Bar - Sales by Month and Product Category')
        drop_area_obj = util_obj.validate_and_get_webdriver_object("div.pd-page-canvas div.pd-page-acc-section div[class='pd-page-section-grid-box']:nth-child(7)",'grid-box')
#        source_file_css = self.driver.find_elements_by_css_selector("div[data-ibx-type='pdTreeBrowserNode']")
#        s=javascript_obj.find_elements_by_text(source_file_css,'Stacked Bar - Sales by Month and Product Category')
#        source_file_obj = s[0]

        source_cord = core_util_obj.get_web_element_coordinate(source_file_obj)
        target_cord = core_util_obj.get_web_element_coordinate(drop_area_obj)
        
        mouse_obj=uisoup.mouse
        mouse_obj.press_button(source_cord['x'], source_cord['y'])
        time.sleep(Global_variables.longwait)
        mouse_obj.move(target_cord['x'], target_cord['y'])
        time.sleep(Global_variables.mediumwait)
        util_obj.verify_picture_using_sikuli('step_07_00.png', 'Step 07.00: Verify the tool tip should not display the full title while dragging the container.')
#         tooltip_css=".ace_tooltip"
#         raw_tooltip_list=self.driver.find_element_by_css_selector(tooltip_css).text.replace(u'\xa0\n', '').replace(u'\xa0', ' ').split('\n')
#         actual_list=util_obj.get_actual_tooltip_list(self, raw_tooltip_list)
#         expected_tooltip_list = ['']
#         util_obj.asequal(self, expected_tooltip_list, actual_list, msg='Verify tool tip')
        mouse_obj.release_button()
                
        """ 
        Step 8 : Drag and drop Panel container next to third panel
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        util_obj.synchronize_with_visble_text(pd_designloactaors_obj.BASIC_CONTAINER_CSS, 'Panel', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas('Panel', 10)
        
        """ 
        Step 08.00 : Verify container is placed as below in the fist row itself
        """
        page_designer_obj.verify_number_of_page_sections(1, 'Step 08.00 : Verify 1 page sections are displaying in page canvas')
        page_designer_obj.verify_number_of_panels(4, 'Verify 4 container in section 1:')
        
        """ 
        Step 9: Close page without saving
        """
        core_util_obj.switch_to_previous_window()
        
        """ 
        Step 10: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()