"""-------------------------------------------------------------------------------------------
Created on July 18, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267161&group_by=cases:section_id&group_id=426907&group_order=asc
Test Case Title =  Check Settings Menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators

class C5743412_TestClass(BaseTestCase):

    def test_C5743412(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
    
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        quick_filter_css = "[title='Quick filter']"
        north_red_line_css = "div[class*='ibx-selection-manager'] div[class='pd-selection north']"
        south_red_line_css = "div[class*='ibx-selection-manager'] div[class='pd-selection south']"
        east_red_line_css = "div[class*='ibx-selection-manager'] div[class='pd-selection east']"
        west_red_line_css = "div[class*='ibx-selection-manager'] div[class='pd-selection west']"
        
        def right_click_on_filter_control_value():
            filter_box_elem=self.driver.find_elements_by_css_selector(".pd-filter-panel-content .pd-amper-label .ibx-label-text")
            for x in filter_box_elem:
                if x.text.strip()=="Category:":
                    core_utils.python_left_click(x)
                    
        def verify_red_dotted_line_surrounding(line_css, msg):
            border_obj = utils.validate_and_get_webdriver_object(line_css,"border css")
            actual_res = border_obj.get_attribute('class')
            utils.as_notin('hide', actual_res, msg)
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mrid', 'mrpass')
     
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
 
        """
            STEP 3 : Expand 'P292_S10863' domain -> 'G426906' folder; 
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Drag and drop 'Category Sales' from Retail Samples -> Portal -> Small widgets to the page canvas
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("{0}->{1}_{2}".format(group_id, project_id, suite_id))
        pd_design.drag_content_item_to_blank_canvas("Category Sales", 1, content_folder_path="Retail Samples->Portal->Small Widgets")
        utils.synchronize_until_element_is_visible(quick_filter_css, main_page.home_page_long_timesleep)
    
        """
            STEP 6 : Click on quick filter icon
        """
        pd_design.click_quick_filter()
        utils.synchronize_until_element_disappear(quick_filter_css, main_page.home_page_long_timesleep)
 
        """
            STEP 7 : Click on the Page
        """
        page_obj = utils.validate_and_get_webdriver_object(".pd-page-header", "Page css")
        core_utils.python_left_click(page_obj)

        """
            STEP 7.01 : Verify there is a red dotted line surrounding the whole page
        """
        verify_red_dotted_line_surrounding(north_red_line_css, "Step 7.01 : Verify there is a red dotted line surrounding the whole page")
        verify_red_dotted_line_surrounding(south_red_line_css, "Step 7.02 : Verify there is a red dotted line surrounding the whole page")
        verify_red_dotted_line_surrounding(east_red_line_css, "Step 7.03 : Verify there is a red dotted line surrounding the whole page")
        verify_red_dotted_line_surrounding(west_red_line_css, "Step 7.04 : Verify there is a red dotted line surrounding the whole page")

        """
            STEP 8 : Click open properties pane -> Settings tab
        """
        pd_design.click_property()

        """
            STEP 8.01 : Verify setting menus appears as below
        """
        pd_design.verify_setting_tab_properties("Page Settings", ['ID=PAGE', 'Classes=', 'Title=on', 'Toolbar=on'], "Step 8.01 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("Embedded Resources", ['CSS=off', 'Javascript=off'], "Step 8.02 : Verify setting menus appears as below")
        pd_design.click_property()
        
        """
            STEP 9 : Click on the first filter control of the filter tool bar
        """
        right_click_on_filter_control_value()

        """
            STEP 9.01 : Verify there is a red dotted line surrounding the whole filter control
        """
        verify_red_dotted_line_surrounding(north_red_line_css, "Step 9.01 : Verify there is a red dotted line surrounding the whole filter control")
        verify_red_dotted_line_surrounding(south_red_line_css, "Step 9.02 : Verify there is a red dotted line surrounding the whole filter control")
        verify_red_dotted_line_surrounding(east_red_line_css, "Step 9.03 : Verify there is a red dotted line surrounding the whole filter control")
        verify_red_dotted_line_surrounding(west_red_line_css, "Step 9.04 : Verify there is a red dotted line surrounding the whole filter control")
        
        """
            STEP 10 : Click open properties pane -> Settings tab
        """
        pd_design.click_property()
        
        """
            STEP 10.01 : Verify setting menus appears as below
        """
        pd_design.verify_setting_tabs(['General Settings', 'Control Settings', 'Data Settings', 'Parameters'], "Step 10.01 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("General Settings", ['Type=Multiple select', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name='], "Step 10.02 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("Control Settings", ['Optional=on', 'Placeholder text=Make a selection...', 'Search=off', 'Selection controls=off'], "Step 10.03 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("Data Settings", ['Show All option=on', 'Display text=All', 'Default value=_FOC_NULL'], "Step 10.04 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("Parameters", [], "Step 10.05 : Verify setting menus appears as below")
        
        parameter_obj = utils.validate_and_get_webdriver_object("div[class*='pd-ps-value pd-ps-parameters'] input", "Parameter css")
        actual_output = parameter_obj.get_attribute('aria-label').strip()
        msg = "Step 10.06 : Verify setting menus appears as below"
        utils.asequal("PRODUCT_CATEGORY (A40V)", actual_output, msg)
        pd_design.click_property()
        
        """
            STEP 11 : Click on category sales panel
        """
        category_sales_obj = utils.validate_and_get_webdriver_object('.pd-container-title-bar', "Category Sales css")
        core_utils.python_left_click(category_sales_obj)
        
        """
            STEP 11.01 : Verify there is a red dotted line surrounding the whole container
        """
        verify_red_dotted_line_surrounding(north_red_line_css, "Step 11.01 : Verify there is a red dotted line surrounding the whole container")
        verify_red_dotted_line_surrounding(south_red_line_css, "Step 11.02 : Verify there is a red dotted line surrounding the whole container")
        verify_red_dotted_line_surrounding(east_red_line_css, "Step 11.03 : Verify there is a red dotted line surrounding the whole container")
        verify_red_dotted_line_surrounding(west_red_line_css, "Step 11.04 : Verify there is a red dotted line surrounding the whole container")
        
        """
            STEP 12 : Click open properties pane -> Settings tab
        """
        pd_design.click_property()
        
        """
            STEP 12.01 : Verify setting menus appears as below
        """
        pd_design.verify_setting_tabs(['Container Settings', 'Content Customization', 'Content'], "Step 11.01 : Verify there is a red dotted line surrounding the whole container")
        pd_design.verify_setting_tab_properties("Container Settings", ['ID=CONTAINER', 'Classes=', 'Title=on', 'Toolbar=on', 'Show On=off'], "Step 11.02 : Verify there is a red dotted line surrounding the whole container")
        pd_design.verify_setting_tab_properties("Content Customization", ['Lock content=on', 'Path=Not selected', 'Lock path=on', 'Flatten list=off', 'Hide tags=off', 'Initial view=off'], "Step 11.03 : Verify there is a red dotted line surrounding the whole container")
        pd_design.verify_setting_tab_properties("Content", ['ID=CONTENT', 'Classes='], "Step 11.04 : Verify there is a red dotted line surrounding the whole container")
        pd_design.click_property()
        
        """
            STEP 13 : Click on the section
        """
        pd_design.select_page_section(1)
        
        """
            STEP 13.01 : Verify there is a red dotted line surrounding the whole section
        """
        verify_red_dotted_line_surrounding(north_red_line_css, "Step 13.01 : Verify there is a red dotted line surrounding the whole section")
        verify_red_dotted_line_surrounding(south_red_line_css, "Step 13.02 : Verify there is a red dotted line surrounding the whole section")
        verify_red_dotted_line_surrounding(east_red_line_css, "Step 13.03 : Verify there is a red dotted line surrounding the whole section")
        verify_red_dotted_line_surrounding(west_red_line_css, "Step 13.04 : Verify there is a red dotted line surrounding the whole section")
        
        """
            STEP 14 : Click open properties pane -> Settings tab
        """
        pd_design.click_property()
        
        """
            STEP 14.01 : Verify setting menus appears as below
        """
        pd_design.verify_setting_tabs(['Section Settings'], "STEP 14.01 : Verify setting menus appears as below")
        pd_design.verify_setting_tab_properties("Section Settings", ['ID=SECTION', 'Classes=', 'Collapsible=off', 'Row height=off'], "Step 14.02 : Verify setting menus appears as below")

        """
            STEP 15 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 16 : Sign out WF
        """
        main_page.signout_from_username_dropdown_menu()      
 
if __name__ == '__main__':
    unittest.main()