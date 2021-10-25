"""-------------------------------------------------------------------------------------------
Created on July 11, 2019
@author: Vishnu_priya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5743397
Test Case Title =  Check Edit label menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main
from common.locators import page_designer_design as DesignLocators

class C5743397_TestClass(BaseTestCase):

    def test_C5743397(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
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
        expected_title='Test Label'
         
        def right_click_on_filter_control_value():
            filter_box_elem=self.driver.find_elements_by_css_selector(".pd-filter-panel-content .pd-amper-label .ibx-label-text")
            for x in filter_box_elem:
                if x.text.strip()=="Category:":
                    core_utils.python_right_click(x)
            
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
        
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
        STEP 5: Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G426906")
        pd_design.collapse_content_folder("P292_S10863")
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        
        """
        STEP 6: Click on quick filter icon
        """
        utils.synchronize_with_number_of_element(DesignLocators.ToolBar.QUICK_FILTER_BUTTON_CSS, 1, main_page.home_page_long_timesleep)
        pd_design.click_quick_filter()
        utils.synchronize_until_element_is_visible('[data-ibx-type="pdFilterPanel"]',main_page.home_page_long_timesleep)
        
        """
        STEP 7: Right click on first filter control and choose 'Edit Label' menu
        """
        right_click_on_filter_control_value()
        main_obj.select_context_menu_item("Edit label")
        
        """
        verify Label has been selected as below
        """
        """
        STEP 8: Enter 'Test Label' and hit enter
        Verify Label has been changed as below
        """
        utils.synchronize_until_element_is_visible(".ibx-content-editing",main_page.home_page_long_timesleep)
        label_elem=self.driver.find_element_by_css_selector(".ibx-content-editing")
        core_utils.python_left_click(label_elem)
        utils.set_text_to_textbox_using_keybord("Test Label",text_box_elem=label_elem)
        actual_changed_title=self.driver.find_element_by_css_selector(".pd-filter-panel-content .pd-amper-label .ibx-label-text").text
        utils.asequal(actual_changed_title,expected_title,"Step 8:Verify Label has been changed")

        """
        STEP 9 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
        STEP 10 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()