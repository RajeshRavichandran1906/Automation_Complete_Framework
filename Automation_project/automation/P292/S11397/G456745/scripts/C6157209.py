"""-------------------------------------------------------------------------------------------
Created on August 20, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157209
Test Case Title =  Adding optional other static multi-select button set control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157209_TestClass(BaseTestCase):

    def test_C6157209(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        SHORT_TIME=10
        LONG_TIME=40
        TEMPLATE_NAME='Grid 2-1'
        TEST_CASE_ID='C6157209'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='27 - Multi-Select Static Optional Other'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_CONVERT_CONTROL='Button set'
        EXPECTED_TOTAL_PANELS=3
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_DEFAULT_FILTER_OPTION=['EMEA']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['27 - Multi-Select Static Optional Other', 'Panel 2', 'Panel 3']
        EXPECTED_FILTER_CONVERTER_CONTROLS=['Checkbox', 'Button set']
        EXPECTED_FILTER_BUTTONSET_OPTIONS=['South America', 'EMEA', 'North America']
        EXPECTED_PROPERTIES_TABS=['Settings', 'Format']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Multiple button set', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=EMEA']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        
        """
            STEP 01 : Login to WF as Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Grid 2-1 template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "27 - Multi-Select Static Optional Other" report into Panel 1 from P292_S10660 > G433312 > Reference Items folder.
        """
        CONTAINER_TITLE_TO_DROP_ITEM = 'Panel 1'
        pd_design.drag_content_item_to_container(CONTAINER_ITEM, CONTAINER_TITLE_TO_DROP_ITEM)
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 04.01 : Verify page heading')
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 04.02 : Verify Refresh button only display on page header')
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 04.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 04.05 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 04.06')
        pd_design.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 04.07 : Verify report display with An error has occurred', expected_output='An error has occurred')
        pd_design.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 04.08 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
        pd_design.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 04.09 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify dropdown control bounded to the page with a default value and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify {0} filter drop down control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify {0} filter drop down control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_OPTION, 'Step 05.04 : Verify {0} option selected as default in filter drop down'.format(EXPECTED_DEFAULT_FILTER_OPTION))
        
        """
            STEP 06.0 : Right click filter control (right click over filter control label or dropdown, else grid cell will be selected) and select Convert.
            STEP 06.1 : Verify Convert Control To window appears.
        """
        pd_design.verify_filter_control_converter_window(FILTER_CONTRTOL_NAME, '06.01', expected_controls_list=EXPECTED_FILTER_CONVERTER_CONTROLS)
        
        """
            STEP 07 : Select Button set in Convert Control To window.
        """
        pd_design.convert_filter_control(FILTER_CONTRTOL_NAME, FILTER_CONVERT_CONTROL)
        
        """
            STEP 07.1 : Verify dropdown control converted to button set control with default value selected.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.01 : Verify {0} filter button set control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 07.02 : Verify {0} filter button set control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_buttonset_is_optional(FILTER_CONTRTOL_NAME, 'Step 07.03 : Verify {0} filter button set control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_buttonset_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_BUTTONSET_OPTIONS, 'Step 07.04 : Verify {0} options are display in filter button set control'.format(EXPECTED_FILTER_BUTTONSET_OPTIONS))
        pd_design.verify_selected_options_in_filter_buttonset(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_OPTION, 'Step 07.05 : Verify {0} option selected as default in filter button set'.format(EXPECTED_DEFAULT_FILTER_OPTION))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.07 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 08 : Click Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 08.1 : Verify all values in Properties panel.
        """
        pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 08.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
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
            STEP 09.1 : Verify page loads successfully in preview with default value condition.
        """
        pd_preview.verify_preview_is_displayed('Step 09.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 09.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 09.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 09.04 : Verify {0} filter controls display in preview'.format(EXPECTED_FILTER_CONTROLS))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 09.05 : Verify {0} filter control not bounded to the page with red dotted border around it in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_buttonset_is_optional(FILTER_CONTRTOL_NAME, 'Step 09.06 : Verify {0} filter button set control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_buttonset_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_BUTTONSET_OPTIONS, 'Step 09.07 : Verify {0} options are display in filter button set control'.format(EXPECTED_FILTER_BUTTONSET_OPTIONS))
        pd_preview.verify_selected_options_in_filter_buttonset(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_OPTION, 'Step 09.08 : Verify {0} option selected as default in filter button set'.format(EXPECTED_DEFAULT_FILTER_OPTION))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 09.09 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 09.10 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 09.11 : Verify {0} panel display in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME1)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 09.12 : Verify report added to the page successfully')
        pd_preview.switch_to_default_page()
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 09.15 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 09.16 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
       
        """
            STEP 10 : Select "North America" and "South America" values in button set control.
        """
        FILTER_BUTTONSET_MULTI_OPTIONS_TO_SELECT=['North America', 'South America']
        pd_run.select_multiple_options_in_filter_buttonset(FILTER_CONTRTOL_NAME, FILTER_BUTTONSET_MULTI_OPTIONS_TO_SELECT)
        
        """
            STEP 10.1 : Verify selected filter condition applied in the page.
        """
        EXPECTED_FILTER_BUTTONSET_SELECTED_OPTIONS=['South America', 'EMEA', 'North America']
        pd_preview.verify_selected_options_in_filter_buttonset(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_BUTTONSET_SELECTED_OPTIONS, 'Step 10.01 : Verify {0} options are selected in filter button set'.format(EXPECTED_FILTER_BUTTONSET_SELECTED_OPTIONS))
        pd_preview.verify_filter_buttonset_is_optional(FILTER_CONTRTOL_NAME, 'Step 10.02 : Verify solid red border not display over filter the control')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_number_of_element("table[summary]>tbody>tr", 23, time_out=SHORT_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 10.03 : Verify selected filter condition applied in the page')
        pd_preview.switch_to_default_page()
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 10.04 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 10.05 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[2]))
        
        """
            STEP 11 : Return back to designer using blue arrow in preview.
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 12 : Save and Close the Designer.
        """
        pd_design.save_page_from_toolbar_with_default_name()
        pd_design.switch_to_previous_window()
        
        """
            STEP 13 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 13.1 : Verify page runs successfully with default filter condition.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 13.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 13.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 13.03 : Verify {0} filter controls display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_filter_buttonset_is_optional(FILTER_CONTRTOL_NAME, 'Step 13.04 : Verify {0} filter button set control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_filter_buttonset_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_BUTTONSET_OPTIONS, 'Step 13.05 : Verify {0} options are display in filter button set control'.format(EXPECTED_FILTER_BUTTONSET_OPTIONS))
        pd_run.verify_selected_options_in_filter_buttonset(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_OPTION, 'Step 13.06 : Verify {0} option selected as default in filter button set'.format(EXPECTED_DEFAULT_FILTER_OPTION))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 13.07 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 13.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 13.09 : Verify {0} panel display in run page'.format(EXPECTED_TOTAL_PANELS))
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 13.10 : Verify page runs successfully with default filter condition')
        pd_run.switch_to_default_page()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 13.11 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[1]))
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 13.12 : Verify {0} container is blank'.format(EXPECTED_CONTAINERS[2]))
        pd_run.swtich_to_homepage_runwindow_frame()
        
        """
            STEP 14 : Close run window.
        """
        pd_run.close_homepage_run_window()
        
        """
            STEP 15 : Delete the created Page.
        """
        pd_design.delete_saved_page_designer()
        
        """
            STEP 16 : Sign Out WF.
        """