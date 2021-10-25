'''
Created on May 22, 2019

@author: Magesh

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/8262083
TestCase Name = Restore PGX for Section Theme and Grid style
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.locators import wf_mainpage_locators
from common.lib import utillity
from common.lib import core_utility
from common.wftools.page_designer import Run, Design

class C8262083_TestClass(BaseTestCase):

    def test_C8262083(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_design_obj = Design(self.driver)
        page_designer_run_obj = Run(self.driver)
        
        """
        TESTCASE CSS
        """
        pd_page_css=".pd-page-acc-section[class*='pd-style-color']"
        panel_titlebar_css=".grid-stack-item-content div[class^='pd-container-title-bar']"
        panel_label_css="div[data-ibx-type='pdContainer'] div[data-ibx-type='pdFilterPanel'] div[class*='pd-amper-label'] div[class='ibx-label-text']"
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->P292_S19901->G513470'
        fex_name = 'section theme and grid styling1'
        action_tile = 'Designer'
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Expand 'P292_S19901' domain > click on G513470 folder.
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, action_tile, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Right click on 'section theme and grid styling1' > Edit. 
        """
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Edit')
        core_util_obj.switch_to_new_window()
        
        """
        Step 03.01: Verify all the changes still exist
        """
        util_obj.synchronize_with_number_of_element(panel_label_css, 2, main_page_obj.home_page_medium_timesleep)
        page_designer_run_obj.verify_page_heading_title(['Page Heading'], 'Step 03.01 : Verify page title')
        page_designer_run_obj.verify_containers_title(["Category Sales", "Panel 2", "Panel 3"], 'Step 03.02 : Verify container titles') 
        page_designer_run_obj.verify_filter_control_labels(['Category:', 'Product Model:'], 'Step 03.03 : Verify filter panel heading labels', grid_container_title='Panel 2')
        util_obj.verify_element_color_using_css_property(pd_page_css, 'curious_blue', msg='Step 03.04 : Verify page theme', attribute='background-color')
        panel2_titlebar_css=self.driver.find_elements_by_css_selector(panel_titlebar_css)
        util_obj.verify_element_color_using_css_property(None, 'fern2', msg='Step 03.05 : Verify panel2 styling', attribute='background-color', element_obj=panel2_titlebar_css[1])
        
        """
        Step 04.00: Close the Page Designer from application menu.
        """
        page_designer_design_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 05.00: In the banner link, click on the top right username > Click Sign Out.
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()