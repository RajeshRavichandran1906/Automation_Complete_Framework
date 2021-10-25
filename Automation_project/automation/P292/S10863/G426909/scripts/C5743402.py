"""-------------------------------------------------------------------------------------------
Created on July 16, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267151&group_by=cases:section_id&group_id=426909&group_order=asc
Test Case Title =  Check Convert menu
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.pages.wf_mainpage import Wf_Mainpage as main

class C5743402_TestClass(BaseTestCase):

    def test_C5743402(self):
        
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
        
        def right_click_on_filter_control_value(filter_name, default_css=".pd-filter-panel-content .pd-amper-label .ibx-label-text"):
            filter_box_elem=self.driver.find_elements_by_css_selector(default_css)
            for x in filter_box_elem:
                if x.text.strip()== filter_name:
                    core_utils.left_click(x)
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
            STEP 7 : Right click on first filter (Category) control and Convert
        """
        right_click_on_filter_control_value("Category:")
        main_obj.select_context_menu_item("Convert")
        pd_design.wait_for_visible_text("div[class*=' ibx-popup ibx-dialog']", "Convert")
        
        """
            Step 07.01 : A ibx window will appear with 'Checkbox' and 'Button set' options to convert the control to as below
        """
        convert_obj = utils.validate_and_get_webdriver_objects("div[class^='ibx-dialog-content'] div[data-ibx-type='ibxButton']", "Convert css")
        actual_list = []
        for x in convert_obj:
            actual_list.append(x.text.strip())
        msg = "Step 07.01 : A ibx window will appear with 'Checkbox' and 'Button set' options to convert the control to as below"
        utils.asequal(['', '', 'Checkbox', 'Button set', '', ''], actual_list, msg)
                
        """
            STEP 8 : Choose the checkbox option
        """
        checkbox_obj = utils.validate_and_get_webdriver_object("div[class*='pd-filter-btn-checkbox']", "check box css")
        core_utils.left_click(checkbox_obj)

        """
            Step 08.01 : Verify the control has been converted to check boxes as below
        """
        check_box_obj = utils.validate_and_get_webdriver_object("div[class*='pd-amper-radio-group pd-filter-panel-content-scroll']", "Check box css")
        a_l = check_box_obj.is_displayed()
        msg = "Step 08.01 : Verify the control has been converted to check boxes as below"
        utils.asequal(True, a_l, msg)
        
        check_box_list_obj = utils.validate_and_get_webdriver_objects("div[class*='pd-amper-radio-group pd-filter-panel-content-scroll'] div[role='checkbox']", "Check box list css")
        check_box_list = []
        for x in check_box_list_obj:
            check_box_list.append(x.text.strip())
        msg = "Step 08.02 : Verify the control has been converted to check boxes as below"
        utils.asequal(['All', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], check_box_list, msg)

        """
            STEP 9 : Right click on Region filter control and Convert
        """
        right_click_on_filter_control_value("Region:")
        main_obj.select_context_menu_item("Convert")
        pd_design.wait_for_visible_text("div[class*=' ibx-popup ibx-dialog']", "Convert")
        
        """
            Step 09.01 : A ibx window will appear with 'Radio' and 'Button set' options to convert the control to as below"
        """
        convert_obj = utils.validate_and_get_webdriver_objects("div[class^='ibx-dialog-content'] div[data-ibx-type='ibxButton']", "Convert css")
        actual_list = []
        for x in convert_obj:
            actual_list.append(x.text.strip())
        msg = "Step 09.01 : A ibx window will appear with 'Radio' and 'Button set' options to convert the control to as below"
        utils.asequal(['', 'Radio', '', 'Button set', '', ''], actual_list, msg)
        
        """
            STEP 10 : Click on 'Radio' option
        """
        Radiobutton_obj = utils.validate_and_get_webdriver_object("div[class*='pd-filter-btn-radio']", "Radio button css")
        core_utils.left_click(Radiobutton_obj)

        """
            Step 10.01 : Verify the control has been converted to radio button as below
        """
        region_radio_button_obj = utils.validate_and_get_webdriver_object("div[class*='pd-amper-radio-group fbx-block']", "Region Radio button css")
        actual_res = region_radio_button_obj.is_displayed()
        msg = "Step 10.01 : Verify the control has been converted to radio button as below"
        utils.asequal(True, actual_res, msg)
        
        all_radio_button_obj = utils.validate_and_get_webdriver_objects("div[class*='pd-amper-radio-group fbx-block'] div[role='radio']", "All radio button css")
        act_lis = []
        for x in all_radio_button_obj:
            act_lis.append(x.text.strip())
        msg = "Step 10.02 : Verify the control has been converted to radio button as below"
        utils.asequal(['All', 'EMEA', 'North America', 'Oceania', 'South America'], act_lis, msg)

        """
            STEP 11 : Right click on 'Category' filter control and Convert;
            Choose 'Button set'
        """
        right_click_on_filter_control_value("Category:\nAll\nAccessories\nCamcorder\nComputers\nMedia Player\nStereo Systems\nTelevisions\nVideo Production", default_css="div[class^='pd-filter-cell'] div[class*='ibx-widget ibx-flexbox ibx-flexbox-vertical pd-filter-panel']")
        main_obj.select_context_menu_item("Convert")
        pd_design.wait_for_visible_text("div[class*=' ibx-popup ibx-dialog']", "Convert")
        
        buttonset_obj = utils.validate_and_get_webdriver_object("div[class*='pd-filter-btn-buttonset']", "Button set css")
        core_utils.left_click(buttonset_obj)

        """
            Step 11.01 : Verify the control has been converted to button set as below
        """
        button_obj = utils.validate_and_get_webdriver_object("div[class*='pd-amper-ctrl pd-amper-button-group']", "button css")
        actual_result = button_obj.is_displayed()
        msg = "Step 11.01 : Verify the control has been converted to button set as below"
        utils.asequal(True, actual_result, msg)
        
        button_mem_obj = utils.validate_and_get_webdriver_objects("div[class*='pd-amper-ctrl pd-amper-button-group'] div[role='checkbox']", "button member")
        actual_l = []
        for x in button_mem_obj:
            actual_l.append(x.text.strip())
        msg = "Step 11.02 : Verify the control has been converted to button set as below"
        utils.asequal(['All', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], actual_l, msg)

        """
            STEP 12 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        
        """
            STEP 13 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()