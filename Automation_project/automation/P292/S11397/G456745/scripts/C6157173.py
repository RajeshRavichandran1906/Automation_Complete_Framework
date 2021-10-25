"""-------------------------------------------------------------------------------------------
Created on July 12, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157173
Test Case Title =  Adding optional other input filter control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157173_TestClass(BaseTestCase):

    def test_C6157173(self):
        
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
        TEST_CASE_ID='C6157173'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='03 - Simple Input Optional Other'
        FILTER_CONTRTOL_NAME='Business Region:'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Business Region:']
        EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE=['Oceania']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_CONTAINERS=['03 - Simple Input Optional Other']
        EXPECTED_PROPERTIES_TABS=['Settings', 'Format']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Input', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on', 'Placeholder text=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=Oceania']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        
        """
            STEP 01 : Login as WF Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "03 - Simple Input Optional Other" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1)
        
        """
            STEP 04.1 : Verify report added to the page successfully.
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
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 04.07 : Verify filter condition applied in the page')
        pd_design.switch_to_default_page()
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Business Region:', time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with red dotted border around the filter control.
        """
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.01 : Verify {0} button are display on page header'.format(EXPECTED_PAGE_HEADER_BUTTONS))
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.02 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify filter input box control bounded to the page with red dotted border around it')
        pd_design.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 05.04 : Verify filter input box control is optional')
        pd_design.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 05.05 : Verify {0} filter input box default value is {1}'.format(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE))
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are available in Properties panel'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 06.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 06.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 06.04 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 06.05 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 06.06 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview.
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify default filter condition applied in the page.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter button are display on page header')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify filter control required state is retained in page preview.')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify filter not bounded to the page with red dotted border around it in preview')
        pd_preview.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify filter input box control is optional')
        pd_preview.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 07.07 : Verify {0} filter input box default value is {1}'.format(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.08 : Verify canvas containers')
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.09 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.10 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='Oceania', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 07.11 : Verify default filter condition applied in the page')
        pd_preview.switch_to_default_page()
        
        """
            STEP 08 : Return back to designer using blue arrow in preview.
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 09 : Save and Close the Designer.
        """
        pd_design.save_page_from_toolbar_with_default_name()
        pd_design.switch_to_previous_window()
        
        """
            STEP 10 : Run created Designer page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 10.1 : Verify page run successfully with "Oceania" filter condition.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 10.01 : Verify page heading')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 10.02 : Verify Refresh and Filter button are display on page header')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 10.02 : Verify filter control required state is retained in run.')
        pd_run.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 10.04 : Verify filter input box control is optional')
        pd_run.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 10.05 : Verify {0} filter input box default value is {1}'.format(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 10.06 : Verify canvas containers')
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 10.07 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 10.08 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='Oceania', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 10.09 : Verify page run successfully with "Oceania" filter condition')
        pd_run.switch_to_default_page()
        
        """
            STEP 11 : Enter "_FOC_NULL" in Input control.
        """
        INPUT_VALUE_TO_ENTER='_FOC_NULL'
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.enter_input_value_for_filter_control(FILTER_CONTRTOL_NAME, INPUT_VALUE_TO_ENTER)
        pd_run.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, [INPUT_VALUE_TO_ENTER], 'Step 11.05 : Verify {0} filter input box value is {1}'.format(FILTER_CONTRTOL_NAME, INPUT_VALUE_TO_ENTER))
        
        """
            STEP 11.1 : Verify filter condition applied in the page.
        """
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        #pd_run.create_html_report_data_set(DATA_SET_NAME2)
        pd_run.verify_html_report_data_set(DATA_SET_NAME2, 'Step 11.01 : Verify filter condition applied in the page')
        pd_run.switch_to_default_page()
        
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