'''
Created on May 10, 2019

@author: varun
Testcase Name : Adding required static radio button control to the Page
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9318019
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import page_designer

class C9318019_TestClass(BaseTestCase):
    
    def test_C9318019(self):
        """
        Test case objects
        """
        pd_run = page_designer.Run(self.driver)
        pd_design = page_designer.Design(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile("project_id")
        suite_id = core_util_obj.parseinitfile("suite_id")
        group_id = core_util_obj.parseinitfile("group_id")
        folder_path = "Domains->{0}_{1}->{2}".format(project_id, suite_id, group_id)
        TEST_CASE_ID='C9318019'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        CONTAINER_ITEM='19 - Single Select Static Required'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_CONVERT_CONTROL='Radio'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE=['Make a selection...']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['19 - Single Select Static Required']
        EXPECTED_FILTER_CONVERTER_CONTROLS=['Radio', 'Button set']
        EXPECTED_FILTER_RADIOGROUP_OPTIONS=['South America', 'EMEA', 'North America']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Radio group', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=off', 'Search=off']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        
        """
        Step 1: Login WF as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Navigate to 'P292_S29835' domain;
        Click on 'G781380' folder and choose 'Page' action tile from under designer tab
        """
        main_page_obj.expand_repository_folder(folder_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Page', main_page_obj.home_page_long_timesleep)
         
        """
        Step 4: Select Blank template
        """
        pd_design.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text("div[class*='pd-page-header'] div[class*='ibx-label-text']", 'Page Heading', main_page_obj.home_page_long_timesleep)
         
        """
        Step 5: Drag "19 - Single Select Static Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        Verify report has been added to the page successfully.
        """
        pd_design.collapse_content_folder('G781380->P292_S29835')
        pd_design.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1, 'P292_S10660->G433312->Reference Items')
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 05.01 : Verify page heading')
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 05.02 : Verify Refresh button only display on page header')
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 05.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 05.05 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 05.06')
        pd_design.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 05.07 : Verify report added to the page successfully')
         
        """
        Step 6: Click Quick filter present in top right corner of the page.
        Verify dropdown control bounded to the page with solid red border and red dotted border around it.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=main_page_obj.home_page_short_timesleep, pause_time=4)
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 06.01 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 06.02 : Verify {0} filter drop down control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_dropdown_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 06.03 : Verify {0} filter drop down control bounded to the page with solid red border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 06.04 : Verify {0} text display in filter drop down'.format(EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE))
         
        """
        Step 7: Right click filter control (right click over filter control label or dropdown, else grid cell will be selected) and select Convert.
        Verify Convert Control To window appears.
        """
        pd_design.verify_filter_control_converter_window(FILTER_CONTRTOL_NAME, '07.01', expected_controls_list=EXPECTED_FILTER_CONVERTER_CONTROLS)
         
        """
        Step 8: Select Radio in Convert Control To window.
        Verify dropdown control converted to radio button control and solid red border retained over the control.
        """
        pd_design.convert_filter_control(FILTER_CONTRTOL_NAME, FILTER_CONVERT_CONTROL)
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 08.01 : Verify {0} filter button set control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 08.02 : Verify {0} filter button set control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 08.03 : Verify {0} filter radio group control bounded to the page with solid red border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 08.04 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_design.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 08.05 : Verify no one option selected as default in filter radio group control')
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 08.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 08.07 : Verify Refresh and Filter buttons are display on page header')
         
        """
        Step 9: Click on Properties pane present in top right corner of the page.
        Verify all values in Properties panel appears as below
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=main_page_obj.home_page_short_timesleep)
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 09.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 09.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 09.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 09.04 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 09.05 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 09.06 : Verify parameter properties')
         
        """
        Step 10: Click Preview.
        Verify page loads successfully in preview with required radio button control.
        """
        pd_design.click_preview()
        pd_preview.verify_preview_is_displayed('Step 10.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 10.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 10.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 10.04 : Verify {0} filter controls display in preview'.format(EXPECTED_FILTER_CONTROLS))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 10.05 : Verify {0} filter control not bounded to the page with red dotted border around it in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 10.06 : Verify {0} filter radio group control bounded to the page with solid red border around it'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 10.07 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_preview.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 10.08 : Verify no one option selected as default in filter radio group control')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 10.09 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 10.10 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 10.11 : Verify {0} panel display in preview'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 10.12 : Verify report loads successfully in preview')
         
        """
        Step 11: Select "EMEA" radio button
        Verify solid red border over filter the control removed and selected condition applied in the page.
        """
        FILTER_RADIOGROUP_OPTIONS_TO_SELECT = 'EMEA'
        pd_preview.select_filter_radio_group_option(FILTER_CONTRTOL_NAME, FILTER_RADIOGROUP_OPTIONS_TO_SELECT)
        EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP = [FILTER_RADIOGROUP_OPTIONS_TO_SELECT]
        pd_preview.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP, 'Step 11.01 : Verify {0} option selected in filter radio group'.format(EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP))
        pd_preview.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 11.02 : Verify solid red border over filter the control removed')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=main_page_obj.home_page_long_timesleep)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 11.03 : Verify selected condition applied in the page')
        pd_preview.switch_to_default_page()
         
        """
        Step 12: Return back to designer using blue arrow in preview.
        """
        pd_preview.go_back_to_design_from_preview()
         
        """
        Step 13: Click on save button;
        Enter page title as 'C9318019' and click on save button
        """
        pd_design.save_page_from_toolbar(TEST_CASE_ID)
         
        """
        Step 14: Close designer
        """
        pd_design.switch_to_previous_window()
        
        """
        Step 15: Double click on created page to run created Designer Page.
        Verify page runs successfully with required (solid red border around the control) radio button control.
        """
        pd_design.run_page_designer_by_double_click(page_name_to_run=TEST_CASE_ID)
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=main_page_obj.home_page_long_timesleep)
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 15.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 15.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 15.03 : Verify {0} filter controls display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_filter_radio_group_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 15.04 : Verify {0} filter radio group control bounded to the page with solid red border around it'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 15.05 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_run.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, [], 'Step 15.06 : Verify no one option selected as default in filter radio group control')
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 15.07 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 15.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 15.09 : Verify {0} panel display in run page'.format(EXPECTED_TOTAL_PANELS))
        pd_run.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 15.10 : Verify report loads successfully in run page')
        pd_run.swtich_to_homepage_runwindow_frame()
        
        """
        Step 16: Close run window
        """
        pd_run.close_homepage_run_window()
        
        """
        Step 17: Sign Out WF.
        """
       
if __name__ == '__main__':
    unittest.main()