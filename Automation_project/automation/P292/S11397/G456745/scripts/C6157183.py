"""-------------------------------------------------------------------------------------------
Created on September 03, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157183
Test Case Title =  Adding required date control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157183_TestClass(BaseTestCase):

    def test_C6157183(self):
        
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
        TEST_CASE_ID='C6157183'
        MONTH_TO_SELECT='Mar'
        YEAR_TO_SELECT='2016'
        DAY_TO_SELECT='17'
        DATA_SET_NAME=TEST_CASE_ID + '_DataSet_01'
        CONTAINER_ITEM='13 - Date Required'
        FILTER_CONTRTOL_NAME='Select 2016/03/17'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_SELECTED_DATE=['Mar 17, 2016']
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select 2016/03/17']
        EXPECTED_DEFAULT_DATE_FILTER_VALUE=['']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['13 - Date Required']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Date', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=off', 'Placeholder text=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['TIME_DATE_DAY_COMPONENT (YYMD)']
        
        """
            STEP 01 : Login to WF as Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "13 - Date Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
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
            STEP 05.1 : Verify date filter control bounded to the page with solid red border and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify filter date picker control added')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify date filter control bounded to the page with dotted red border around it')
        pd_design.verify_filter_date_picker_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify date filter control bounded to the page with solid red border around it')
        pd_design.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 05.04 : Verify no date selected as default in date filter control')
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.09 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.10 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Right click date control (right click over control label or date control else grid cell will be selected) and select Settings.
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
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify filter date picker control display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify solid red border removed from date filter data picker control in preview')
        pd_preview.verify_filter_date_picker_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify date filter control bounded to the page with solid red border around it')
        pd_preview.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 07.07 : Verify no date selected as default in date filter control')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.08 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.09 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.10 : Verify 1 panel display in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.verify_html_report_does_not_have_vertical_scrollbar('Step 07.11 : Verify container report does not have vertical scroll bar in preview')
        pd_preview.verify_html_report_does_not_have_horizontal_scrollbar('Step 07.12 : Verify container report does not have horizontal scroll bar in preview')
        pd_preview.switch_to_default_page()
        pd_preview.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 07.13 : Verify report display in preview')
       
        """
            STEP 08 : Select "Mar 17, 2016" using Calendar control.
        """
        pd_preview.select_date_from_single_date_picker(FILTER_CONTRTOL_NAME, month=MONTH_TO_SELECT, year=YEAR_TO_SELECT, day=DAY_TO_SELECT)
        
        """
            STEP 08.1 : Verify filter condition applied in the page and solid red border removed.
        """
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(4)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME, 'Step 08.03 : Verify filter condition applied in the page')
        pd_preview.switch_to_default_page()
        pd_preview.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 08.03 : Verify solid red border removed from date filter control')
        pd_preview.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_DATE, 'Step 08.04 : Verify {0} data selected in filter date picker'.format(EXPECTED_SELECTED_DATE))
        
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
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 11.03 : Verify filter date picker controls display in run page')
        pd_run.verify_filter_date_picker_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify date filter control bounded to the page with solid red border around it')
        pd_run.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 07.07 : Verify no date selected as default in date filter control')
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 11.06 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 11.07 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 11.07 : Verify 1 panel display in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.verify_html_report_does_not_have_vertical_scrollbar('Step 11.08 : Verify container report does not have vertical scroll bar in run page')
        pd_run.verify_html_report_does_not_have_horizontal_scrollbar('Step 11.09 : Verify container report does not have horizontal scroll bar in run page')
        pd_run.switch_to_default_page()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 11.10 : Verify report display in run page')
        pd_run.swtich_to_homepage_runwindow_frame()
           
        """
            STEP 12 : Select "Mar 17, 2016" using Calendar control.
        """    
        pd_run.select_date_from_single_date_picker(FILTER_CONTRTOL_NAME, month=MONTH_TO_SELECT, year=YEAR_TO_SELECT, day=DAY_TO_SELECT)
        
        """
            STEP 12.1 : Verify filter condition applied in the page and solid red border removed.
        """
        pd_run.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 12.01 : Verify solid red border removed from date filter control')
        pd_run.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_DATE, 'Step 12.02 : Verify {0} data selected in filter date picker'.format(EXPECTED_SELECTED_DATE))
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(4)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME, 'Step 12.03 : Verify filter condition applied in the page')
        pd_run.switch_to_default_page()
        
        """
            STEP 13 : Close run window.
        """
        pd_run.close_homepage_run_window()
        
        """
            STEP 14 : Delete the created Page.
        """
        pd_design.delete_saved_page_designer()
        
        """
            STEP 15 : Sign Out WF.
        """