"""-------------------------------------------------------------------------------------------
Created on May 11, 2018
@author: Vpriya

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9318025
Test Case Title =  Adding optional other dynamic radio button control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity,core_utility
from common.locators import wf_mainpage_locators

class C9318025_TestClass(BaseTestCase):

    def test_C9318025(self):
        
        """
            CLASS OBJECTS 
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        SHORT_TIME=10
        LONG_TIME=40
        TEMPLATE_NAME='Blank'
        TEST_CASE_ID='C9318025'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='24 - Single Select Dynamic Optional Other'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_CONVERT_CONTROL='Radio'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_DEFAULT_FILTER_VALUE=['Oceania']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['24 - Single Select Dynamic Optional Other']
        EXPECTED_FILTER_CONVERTER_CONTROLS=['Radio', 'Button set']
        EXPECTED_FILTER_RADIOGROUP_OPTIONS=['EMEA', 'North America', 'Oceania', 'South America']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Radio group', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on', 'Search=off']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=Oceania']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        domains_css = ".toolbar"
        repository_folder = 'Domains->P292_S29835->G781380'
        pop_top_css = ".pop-top"
        
        
        """
            STEP 01 : Login to WF as Developer. 
            
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
        
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_utill_obj.switch_to_new_window()
        
        """
        Step 04:01: Select Blank template.
        """
        util_obj.synchronize_with_visble_text(pop_top_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        pd_design.select_page_designer_template(TEMPLATE_NAME)
        
        """
            STEP 05 : Drag "24 - Single Select Dynamic Optional Other" report into the page canvas from P292_S29835->G781380 > Reference Items folder.
        """
        pd_design.collapse_content_folder('G781380->P292_S29835')
        pd_design.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1,'P292_S10660->G433312->Reference Items')
       
        """
            STEP 05.1 : Verify report added to the page successfully.
        """
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 04.01 : Verify page heading')
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 04.02 : Verify Refresh button only display on page header')
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 04.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 04.05 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 04.06')
        pd_design.switch_to_container_frame(CONTAINER_ITEM)
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='Oceania', time_out=LONG_TIME)
        #pd_design.create_html_report_data_set(DATA_SET_NAME1)
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 04.07 : Verify selected condition applied in the page')
        pd_design.switch_to_default_page()
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify dropdown control bounded to the page with default value and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify filter drop down control bounded to the page with red dotted border around it')
        pd_design.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify filter drop down control is optional')
        pd_design.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_VALUE, 'Step 05.04 : Verify {0} option selected as default in filter drop down'.format(EXPECTED_DEFAULT_FILTER_VALUE))
        
        """
            STEP 06.0 : Right click filter control (right click over filter control label or dropdown, else grid cell will be selected) and select Convert.
            STEP 06.1 : Verify Convert Control To window appears.
        """
        pd_design.verify_filter_control_converter_window(FILTER_CONTRTOL_NAME, '06.01', expected_controls_list=EXPECTED_FILTER_CONVERTER_CONTROLS)
        
        """
            STEP 07 : Select Radio in Convert Control To window.
        """
        pd_design.convert_filter_control(FILTER_CONTRTOL_NAME, FILTER_CONVERT_CONTROL)
        
        """
            STEP 07.1 : Verify dropdown control converted to radio button control and default value radio button is selected.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.01 : Verify filter button set control added')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 07.02 : Verify filter button set control bounded to the page with red dotted border around it')
        pd_design.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 07.03 : Verify filter radio group control is optional')
        pd_design.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 07.04 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_design.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_VALUE, 'Step 07.05 : Verify {0} option selected as default in filter radio group control'.format(EXPECTED_DEFAULT_FILTER_VALUE))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.07 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 08 : Right click filter control (right click over filter control label or radio button group, else grid cell will be selected) and select Settings.
        """
        pd_design.select_filter_control_context_menu(FILTER_CONTRTOL_NAME, 'Settings')
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 08.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 08.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 08.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 08.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 08.04 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 08.05 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 08.06 : Verify parameter properties')
        
        """
            STEP 09 : Click Preview.
        """
        pd_design.click_preview()
        
        """
            STEP 09.1 : Verify page loads successfully in preview with default value filter condition.
        """
        pd_preview.verify_preview_is_displayed('Step 09.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 09.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 09.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 09.04 : Verify filter button set controls display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 09.05 : Verify filter control not bounded to the page with red dotted border around it in preview')
        pd_preview.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 09.06 : Verify filter radio group control is optional')
        pd_preview.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 09.07 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_preview.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_VALUE, 'Step 09.08 : Verify {0} option selected as default in filter radio group control'.format(EXPECTED_DEFAULT_FILTER_VALUE))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 09.09 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 09.10 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 09.11 : Verify {0} panel display in preview'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='Oceania', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 09.12 : Verify page loads successfully in preview with default value filter condition')
        pd_preview.switch_to_default_page()
       
        """
            STEP 10 : Select "North America" radio button.
        """
        FILTER_RADIOGROUP_OPTIONS_TO_SELECT = 'North America'
        pd_preview.select_filter_radio_group_option(FILTER_CONTRTOL_NAME, FILTER_RADIOGROUP_OPTIONS_TO_SELECT)
        
        """
            STEP 10.1 : Verify only "North America" values available in the page.
        """
        EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP = [FILTER_RADIOGROUP_OPTIONS_TO_SELECT]
        pd_preview.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP, 'Step 10.01 : Verify {0} option selected in filter radio group'.format(EXPECTED_SELECTED_OPTION_IN_FILTER_RADIOFROUP))
        pd_preview.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 10.02 : Verify solid red border not over filter the control')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='North America', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 10.03 : Verify only "North America" values available in the page')
        pd_preview.switch_to_default_page()
        
        """
            STEP 11 : Return back to designer using blue arrow in preview.
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 12 : Click on save button;
            Enter page title as 'C9318025' and click on save button
        """
        pd_design.save_page_from_toolbar('C9318025')
        core_utill_obj.switch_to_previous_window(window_close=True)
    
        
        """
            STEP 13 : Right click created Page and select Run in New Window.
        """
        pd_design.run_page_designer_in_new_window('C9318025')
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 13.1 : Verify page runs successfully with default filter condition.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 13.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 13.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 13.03 : Verify {0} filter button set controls display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_filter_radio_group_is_optional(FILTER_CONTRTOL_NAME, 'Step 13.04 : Verify filter radio group control is optional')
        pd_run.verify_filter_radio_group_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_RADIOGROUP_OPTIONS, 'Step 13.05 : Verify {0} options are display in filter radio group control'.format(EXPECTED_FILTER_RADIOGROUP_OPTIONS))
        pd_run.verify_selected_options_in_filter_radio_group(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_VALUE, 'Step 13.06 : Verify {0} option selected as default in filter radio group control'.format(EXPECTED_DEFAULT_FILTER_VALUE))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 13.07 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 13.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 13.09 : Verify {0} panel display in run page'.format(EXPECTED_TOTAL_PANELS))
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
#         pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(1)", visble_element_text='Oceania', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 13.10 : Verify page runs successfully with default filter condition')
        pd_run.switch_to_default_page()
        
        """
            STEP 14 : Close run window.
        """
        pd_design.switch_to_previous_window()
        
        """
            STEP 15 : Delete the created Page.
        """
        pd_design.delete_saved_page_designer('C9318025')
        
        """
            STEP 16 : Sign Out WF.
        """