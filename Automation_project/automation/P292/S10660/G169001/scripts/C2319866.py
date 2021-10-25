"""-------------------------------------------------------------------------------------------
Created on July 25, 2019
@author: AA14654

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/2319866
Test Case Title =  Creating an IBX Page with blank template
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2319866_TestClass(BaseTestCase):

    def test_C2319866(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        retail_sample_path = "Retail Samples->Portal->Test Widgets"
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        node_panel_css = ".ibfs-tree-node"
        page_canvas = "div.pd-page-canvas"
        content_css = "[title='Content'].checked"
        
        """ Step 1: Login WF as domain developer.
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        
        """ Step 2: Click on Content view from side bar.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """ Step 3: Expand 'P292_S10660' domain;
                    Click on 'G192932' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """ Step 4: Choose the Blank template.
                    Verify the Content tab is already highlighted and tree shows on the left.
        """
        pd_design.select_page_designer_template("Blank")
        utils.synchronize_with_visble_text(node_panel_css, group_id, main_page.home_page_long_timesleep)
        try:
            utils.validate_and_get_webdriver_object(content_css, 'content')
            status = 'highlighted'
        except:
            status = 'not_highlighted'
        utils.asequal('highlighted', status, 'Step 04.00: Verify the Content tab is already highlighted.')
        location = utils.validate_and_get_webdriver_object(node_panel_css, 'Tree node').location['x']
        utils.asequal(0, location, 'Step 04.01: Verify the Content tab is already highlighted.')
        
        
        """ Step 5: Click on "P292_S10660" domain to go one level up;
                    Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.collapse_content_folder("{0}->{1}_{2}".format(group_id, project_id, suite_id))
        pd_design.expand_content_folder(retail_sample_path)
        utils.synchronize_with_visble_text(node_panel_css, 'Blue', main_page.home_page_long_timesleep)
        
        """ Step 6: Drag Blue, Gray, Green and Red onto the page canvas respectively.
                    As you drag you should see a blue rectangle and it shows where you can drop the item.
                    Verify that they do show in a row:
        """
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Blue', 1, '06.00')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Gray', 4, '06.01')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Green', 7, '06.02')
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Red', 10, '06.03')
        utils.synchronize_with_visble_text(page_canvas, 'Green', pd_design.home_page_long_timesleep)
        pd_design.verify_containers_title(['Blue', 'Gray', 'Green', 'Red'], 'Step 06.04: Verify that they do show in a row.')
        
        """ Step 7: Click Tool bar and click Close.
        """
        """ Step 8: Click NO in the popup.
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        
        """ Step 9: Signout WF.
        """
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_long_timesleep)
        main_page.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()