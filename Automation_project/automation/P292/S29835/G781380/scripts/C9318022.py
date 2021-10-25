'''
Created on May 11, 2019

@author: Niranjan
Testcase Name : Adding required dynamic radio button control to the Page
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318022
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity,core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer

class C9318022_TestClass(BaseTestCase):
    
    def test_C9318022(self):
        """
        Test case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        page_obj=page_designer.Design(self.driver)
        page_preview_obj=page_designer.Preview(self.driver)
        page_run_obj=page_designer.Run(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->P292_S29835->G781380'
        TEST_CASE_ID='C9318022'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        CONTAINER_ITEM='22 - Single Select Dynamic Required'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_CONVERT_CONTROL='Radio'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE=['Make a selection...']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['22 - Single Select Dynamic Required']
        EXPECTED_FILTER_CONVERTER_CONTROLS=['Radio', 'Button set']
        EXPECTED_FILTER_RADIOGROUP_OPTIONS=['EMEA', 'North America', 'Oceania', 'South America']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Radio group', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=off', 'Search=off']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        
        """
        Test case CSS
        """
        domains_css = ".toolbar"
        pop_top_css = ".pop-top"
        
        """
        Step 01:01: Login WF as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02:01: Click on the Content View from the sidebar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text(domains_css, 'Workspaces', main_page_obj.home_page_short_timesleep)
        
        """
        Step 03:01: Navigate to 'P292_S29835' domain;
        Click on 'G781380' folder and choose 'Page' action tile from under designer tab
        """
        main_page_obj.click_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_utill_obj.switch_to_new_window()
        
        """
        Step 04:01: Select Blank template.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        page_obj.select_page_designer_template("Blank")
        
        """
        Step 05:01: Drag "22 - Single Select Dynamic Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        page_obj.collapse_content_folder('G781380->P292_S29835')
        page_obj.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1, 'P292_S10660->G433312->Reference Items')
        
        """
            STEP 05.01 : Verify report added to the page successfully.
        """
        page_obj.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 05.01 : Verify page heading')
        page_obj.verify_page_header_visible_buttons(['Refresh'], 'Step 05.02 : Verify Refresh button only display on page header')
        page_obj.verify_containers_title(EXPECTED_CONTAINERS, 'Step 05.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        page_obj.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        page_obj.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 05.05 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        page_obj.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 05.06')
        page_obj.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 05.07 : Verify report added to the page successfully')
        
        """
            STEP 06 : Click Quick filter present in top right corner of the page.
        """
        page_obj.click_quick_filter()
        util_obj.synchronize_with_visble_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']",FILTER_CONTRTOL_NAME, main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 06.1 : Verify dropdown control bounded to the page with solid red border and red dotted border around it.
        """
        page_obj.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 06.01 : Verify filter drop down control added')
        page_obj.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 06.02 : Verify filter drop down control bounded to the page with red dotted border around it')
        page_obj.verify_filter_dropdown_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 06.03 : Verify filter drop down control bounded to the page with solid red border around it')
        page_obj.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 06.04 : Verify {0} text display in filter drop down'.format(EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE))
        
        """
            STEP 07.0 : Right click filter control (right click over filter control label or dropdown, else grid cell will be selected) and select Convert.
            STEP 07.1 : Verify Convert Control To window appears.
        """
        page_obj.verify_filter_control_converter_window(FILTER_CONTRTOL_NAME, '06.01', expected_controls_list=EXPECTED_FILTER_CONVERTER_CONTROLS)
        
        """
            STEP 08 : Select Radio in Convert Control To window.
        """
        page_obj.convert_filter_control(FILTER_CONTRTOL_NAME, FILTER_CONVERT_CONTROL)
        
        """
            STEP 08.1 : Verify dropdown control converted to radio button control and solid red border retained over the control.
        """
        page_obj.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 08.01 : Verify {0} filter button set control added'.format(EXPECTED_FILTER_CONTROLS))
        page_obj.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 08.02 : Verify filter button set control bounded to the page with red dotted border around it')
        page_obj.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 08.03 : Verify filter radio group control bounded to the page with solid red border around it')
        page_obj.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 08.04 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        page_obj.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 08.05 : Verify no one option selected as default in filter radio group control')
        page_obj.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 08.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        page_obj.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 08.07 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 09 : Click Properties present in top right corner of the page.
        """
        page_obj.click_property()
        util_obj.synchronize_with_visble_text("div[class^='pd-ps-name']",'Type', main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 09.1 : Verify all values in Properties panel.
        """
        #page_obj.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 09.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        page_obj.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 09.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        page_obj.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 09.03 : Verify General Settings properties')
        page_obj.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 09.04 : Verify Control Settings properties')
        page_obj.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 09.05 : Verify Data Settings properties')
        page_obj.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 09.06 : Verify parameter properties')
        
        """
            STEP 10 : Click Preview
        """
        page_obj.click_preview()
        
        """
            STEP 10.1 : Verify page loads successfully in preview with required radio button control.
        """
        page_preview_obj.verify_preview_is_displayed('Step 10.01 : Verify preview window is display')
        page_preview_obj.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 10.02 : Verify page heading')
        page_preview_obj.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 10.03 : Verify Refresh and Filter buttons are display on page header in preview')
        page_preview_obj.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 10.04 : Verify filter controls display in preview')
        page_preview_obj.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 10.05 : Verify filter control not bounded to the page with red dotted border around it in preview')
        page_preview_obj.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 10.06 : Verify filter radio group control bounded to the page with solid red border around it')
        page_preview_obj.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 10.07 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        page_preview_obj.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 10.08 : Verify no one option selected as default in filter radio group control')
        page_preview_obj.verify_containers_title(EXPECTED_CONTAINERS, 'Step 10.09 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        page_preview_obj.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 10.10 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        page_preview_obj.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 10.11 : Verify {0} panel display in preview'.format(EXPECTED_TOTAL_PANELS))
        page_preview_obj.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 10.12 : Verify report loads successfully in preview')
       
        """
            STEP 11 : Select "Oceania" radio button.
        """
        FILTER_RADIOGROUP_OPTIONS_TO_SELECT = 'Oceania'
        page_preview_obj.select_filter_radio_group_option(FILTER_CONTRTOL_NAME, FILTER_RADIOGROUP_OPTIONS_TO_SELECT)
        
        """
            STEP 11.1 : Verify solid red border over filter the control removed and selected condition applied in the page.
        """
        EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP = [FILTER_RADIOGROUP_OPTIONS_TO_SELECT]
        page_preview_obj.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP, 'Step 10.01 : Verify {0} option selected in filter radio group'.format(EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP))
        page_preview_obj.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 10.02 : Verify solid red border over filter the control removed')
        page_preview_obj.switch_to_container_frame(CONTAINER_ITEM)
        util_obj.synchronize_with_visble_text("table[summary]>tbody>tr:nth-child(2)>td",'Oceania', main_page_obj.home_page_medium_timesleep)
        page_preview_obj.verify_html_report_data_set(DATA_SET_NAME1, 'Step 10.03 : Verify selected condition applied in the page')
        page_preview_obj.switch_to_default_page()
        
        """
            STEP 12 : Return back to designer using blue arrow in preview.
        """
        page_preview_obj.go_back_to_design_from_preview()
        
        """
            STEP 13.01 : Click on save button;
            Enter page title as 'C9318022' and click on save button
        """
        page_obj.save_page_from_toolbar(page_name_to_save=TEST_CASE_ID)
        
        """
            STEP 14.01 : Close designer
        """
        page_obj.switch_to_previous_window()
        
        """
            STEP 15 : Double click on created page to run created Designer Page.
        """
        page_obj.run_page_designer_by_double_click(page_name_to_run=TEST_CASE_ID)
        page_run_obj.swtich_to_homepage_runwindow_frame()
        util_obj.synchronize_with_visble_text("div[class^='pd-page-title']","Page Heading", main_page_obj.home_page_medium_timesleep)
        
        """
            STEP 15.1 : Verify page runs successfully with required (solid red border around the control) radio button control.
        """
        page_run_obj.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 15.01 : Verify page heading  in run page')
        page_run_obj.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 15.02 : Verify Refresh and Filter buttons are display on page header in run page')
        page_run_obj.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 15.03 : Verify filter controls display in run page')
        page_run_obj.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 15.04 : Verify filter radio group control bounded to the page with solid red border around it')
        page_run_obj.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 15.05 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        page_run_obj.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 15.06 : Verify no one option selected as default in filter radio group control')
        page_run_obj.verify_containers_title(EXPECTED_CONTAINERS, 'Step 16.07 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        page_run_obj.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 16.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        page_run_obj.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 16.09 : Verify {0} panel display in run page'.format(EXPECTED_TOTAL_PANELS))
        page_run_obj.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 16.10 : Verify report loads successfully in run page')
        page_run_obj.swtich_to_homepage_runwindow_frame()
        
        """
            STEP 16 : Close run window.
        """
        page_run_obj.close_homepage_run_window()
        
       
        """
            STEP 16 : Sign Out WF.
        """
        
if __name__ == '__main__':
    unittest.main()