"""-------------------------------------------------------------------------------------------
Created on July 16, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267148
Test Case Title =  Check Style menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main

class C5743399_TestClass(BaseTestCase):

    def test_C5743399(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        main_obj=main(self.driver)
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        align_css = "div[class^='ibx-accordion-page ibx-widget ibx-flexbox'] div[data-ibx-type='ibxRadioButton']"
        
        def right_click_on_filter_control_value():
            filter_box_elem=self.driver.find_elements_by_css_selector(".pd-filter-panel-content .pd-amper-label .ibx-label-text")
            for x in filter_box_elem:
                if x.text.strip()=="Category:":
                    core_utils.python_right_click(x)
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", main_page.home_page_medium_timesleep)
 
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
 
        """
            STEP 3 : Expand 'P292_S10863' domain -> 'G426906' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
 
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906")
        pd_design.collapse_content_folder("P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        pd_design.wait_for_number_of_element("div[class^='pd-toolbar-filter']", 1)
        
        """
            STEP 6 : Click on quick filter icon
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_is_visible('[data-ibx-type="pdFilterPanel"]',main_page.home_page_long_timesleep)
 
        """
            STEP 7 : Right click on first filter control and choose Style menu
        """
        right_click_on_filter_control_value()
        main_obj.select_context_menu_item("Format")
        utils.synchronize_with_visble_text(align_css, 'Auto', 15, pause_time=5)
        
        """
            STEP 07.01 : Verify properties pane opens and filter control style properties appears as below
        """
        utils.verify_picture_using_sikuli("C5743399_step7.01.png", "Step 07.01 : Verify properties pane opens and filter control style properties appears as below")
        utils.verify_picture_using_sikuli("C5743399_step7.02.png", "Step 07.02 : Verify properties pane opens and filter control style properties appears as below")
        utils.verify_picture_using_sikuli("C5743399_step7.03.png", "Step 07.03 : Verify properties pane opens and filter control style properties appears as below")
        
        control_obj = utils.validate_and_get_webdriver_objects(align_css, "Control css")
        actual_list = [control.text.strip() for control in control_obj]
        expected_list = ['Auto', 'Max', '20%', '25%', '33.33%', '40%', '50%', '60%', '66.66%', '75%', '80%']
        msg = "Step 07.04 : Verify properties pane opens and filter control style properties appears as below"
        utils.asequal(expected_list, actual_list, msg)
        
        """
            STEP 8 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 9 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()