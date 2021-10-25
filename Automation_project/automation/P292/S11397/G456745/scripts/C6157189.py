"""-------------------------------------------------------------------------------------------
Created on July 23, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157189
Test Case Title =  Adding required static single-select dropdown control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157189_TestClass(BaseTestCase):

    def test_C6157189(self):
        
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
        TEMPLATE_NAME='Blank'
        TEST_CASE_ID='C6157189'
        DATA_SET_NAME=TEST_CASE_ID + '_DataSet_01'
        CONTAINER_ITEM='19 - Single Select Static Required'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_DROPDOWN_SELECTION_OPTION='North America'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE=['Make a selection...']
        EXPECTED_FILTER_DROPDOWN_OPTIONS=['South America', 'EMEA', 'North America']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['19 - Single Select Static Required']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Single select', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=off', 'Placeholder text=Make a selection...', 'Search=off']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        
        """
            STEP 01 : Login to WF as Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "19 - Single Select Static Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1)
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 04.01 : Verify page heading')
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 04.02 : Verify Refresh button only display on page header')
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 04.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 04.05 : Verify 1 panel added in canvas')
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 04.06')
        pd_design.switch_to_container_frame(CONTAINER_ITEM)
        pd_design.verify_html_report_does_not_have_vertical_scrollbar('Step 04.07 : Verify container report does not have vertical scroll bar')
        pd_design.verify_html_report_does_not_have_horizontal_scrollbar('Step 04.08 : Verify container report does not have horizontal scroll bar')
        pd_design.switch_to_default_page()
        pd_design.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 04.09 : Verify report added to the page successfully')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify drop down control bounded to the page with solid red border and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify {0} drop down control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_dropdown_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify {0} drop down control bounded to the page with solid red border'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 05.04 : Verify {0} filter drop down control default text is Make a selection...'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.09 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.10 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Right click dropdown control and select Settings.
        """
        pd_design.select_filter_control_context_menu(FILTER_CONTRTOL_NAME, 'Settings')
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 06.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 06.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 06.04 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 06.05 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 06.06 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify filter control required state (solid red border around the control) is retained in page preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify {0} filter controls display in preview'.format(EXPECTED_FILTER_CONTROLS))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify {0} filter control not bounded to the page with red dotted border around it in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_dropdown_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify {0} drop down control bounded to the page with solid red border in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 07.07 : Verify {0} filter drop down control default text is Make a selection...'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.08 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.09 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.10 : Verify 1 panel display in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.verify_html_report_does_not_have_vertical_scrollbar('Step 07.11 : Verify container report does not have vertical scroll bar in preview')
        pd_preview.verify_html_report_does_not_have_horizontal_scrollbar('Step 07.12 : Verify container report does not have horizontal scroll bar in preview')
        pd_preview.switch_to_default_page()
        pd_preview.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 07.13 : Verify report display in preview')
       
        """
            STEP 08 : Click drop down control and select "North America" value.
        """
        pd_preview.verify_filter_dropdown_options(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_DROPDOWN_OPTIONS, 'Step 08.01 : Verify {0} options are display in filter drop down'.format(EXPECTED_FILTER_DROPDOWN_OPTIONS))
        pd_preview.select_filter_dropdown_option(FILTER_CONTRTOL_NAME, FILTER_DROPDOWN_SELECTION_OPTION)
        
        """
            STEP 08.1 : Verify solid red border not available over the filter control and filter condition applied in the page.
        """
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='North America', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME, 'Step 08.03 : Verify filter appied in report')
        pd_preview.switch_to_default_page()
        pd_preview.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 08.03 : Verify solid red border not available over the filter control and filter condition applied in the page')
        pd_preview.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, [FILTER_DROPDOWN_SELECTION_OPTION], 'Step 08.04 : Verify {0} option selected in filter drop down'.format(FILTER_DROPDOWN_SELECTION_OPTION))
        
        """
            STEP 09 : Return back to designer using blue arrow in preview. 
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 10 : Save and Close the Designer.
        """
        pd_design.save_page_from_toolbar_with_default_name()
        pd_design.switch_to_previous_window()
        
        """
            STEP 11 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 11.1 : Verify filter control is in required state (solid red border available around the filter control) at run time.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 11.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 11.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 11.03 : Verify {0} filter controls display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_filter_dropdown_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 11.04 : Verify {0} drop down control bounded to the page with solid red border in run page'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 11.05 : Verify {0} filter drop down control default text is Make a selection...'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 11.06 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 11.07 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 11.07 : Verify 1 panel display in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.verify_html_report_does_not_have_vertical_scrollbar('Step 11.08 : Verify container report does not have vertical scroll bar in run page')
        pd_run.verify_html_report_does_not_have_horizontal_scrollbar('Step 11.09 : Verify container report does not have horizontal scroll bar in run page')
        pd_run.switch_to_default_page()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 11.10 : Verify report display in run page', expected_output='')
               
        """
            STEP 12 : Close run window.
        """
        pd_run.close_homepage_run_window()
        
        """
            STEP 13 : Delete the created Page.
        """
        pd_design.delete_saved_page_designer()
        
        """
            STEP 14 : Sign Out WF.
        """