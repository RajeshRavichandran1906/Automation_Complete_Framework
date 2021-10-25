"""-------------------------------------------------------------------------------------------
Created on May 22, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831836
Test Case Title =  Adding required input filter control to the Page
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C5831836_TestClass(BaseTestCase):

    def test_C5831836(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        TestCase_ID='C5831836'
        short_timeout=8
        max_time=25
        page_heading=['Page Heading']
        expected_containers=['01 - Simple Input Required']
        expected_filter_control=['Business Region:']
        filter_control_name='Business Region:'
        content_item_name='01 - Simple Input Required'
        container_visible_buttons=['Maximize', 'Options']
        page_header_visible_buttons=['Refresh', 'Filter']
        quick_filter_properties={'text':'1', 'background_color':'mandy', 'font_size':'12px', 'position':'absolute', 'text_align':'center'}
        
        """
            STEP 01 : Login as WF Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template('Blank')
        
        """
            STEP 04 : Drag "01 - Simple Input Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_blank_canvas(content_item_name, 1)
        
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_default_output_for_input_required_container(content_item_name, 'Step 01.1 : Verify report added to the page successfully.')
        pd_design.verify_containers_title(expected_containers, 'Step 01.2 : Verify canvas containers')
        pd_design.verify_number_of_panels(1, 'Step 01.3 : Verify only one panel has added in canvas')
        pd_design.verify_quick_filter_properties(quick_filter_properties, 'Step 01.2')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Business Region:', time_out=short_timeout, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with solid red border and red dotted border.
        """
        pd_design.verify_filter_control_panel_is_selected('Business Region:', 'Step 05.1 : Verify filter control bounded to the page with red dotted border.')
        pd_design.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 05.2 : Verify filter control bounded to the page with solid red border.')
        pd_design.verify_filter_control_labels(expected_filter_control, 'Step 05.3 : Verify filter condition')
        pd_design.verify_page_heading_title(page_heading, 'Step 05.4 : Verify page heading')
        pd_design.verify_page_tab_groups(['Page 1'], 'Step 05.5 : Verify page tab groups')
        pd_design.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 05.6 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_design.verify_filter_inputbox_value(filter_control_name, [''], 'Step 05.7 : Verify Business Region filter condition input value is None')
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']>div", visble_element_text='Type', time_out=short_timeout)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        expected_setting_tabs=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        general_settings=['Type=Input', 'Tooltip=', 'Global name=']
        control_settings=['Optional=off', 'Placeholder text=']
        dat_settings=['Default value=']
        parameter_properties=['BUSINESS_REGION (A15V)']
        pd_design.verify_property_tabs(['Settings', 'Style'], 'Step 06.1 : Verify Property_tabs')
        pd_design.verify_setting_tabs(expected_setting_tabs, 'Step 06.2 : Verify {0} tabs are display in setting tab'.format(expected_setting_tabs))
        pd_design.verify_setting_tab_properties(expected_setting_tabs[0], general_settings, 'Step 06.3 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(expected_setting_tabs[1], control_settings, 'Step 06.4 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(expected_setting_tabs[2], dat_settings, 'Step 06.5 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(parameter_properties, 'Step 06.5 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify filter control required state is retained in page preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.1 : Verify preview window display')
        pd_preview.verify_filter_control_labels(expected_filter_control, 'Step 07.1 : Verify filter control required state is retained in page preview.')
        pd_preview.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 07.3 : Verify filter control bounded to the page with solid red border.')
        pd_preview.verify_page_heading_title(page_heading, 'Step 07.4 : Verify page heading')
        pd_preview.verify_containers_title(expected_containers, 'Step 07.5 : Verify canvas containers')
        pd_preview.verify_number_of_panels(1, 'Step 07.6 : Verify only one panel has added in canvas')
        pd_preview.verify_default_output_for_input_required_container(content_item_name, 'Step 07.7 : Verify report display in preview')
        pd_preview.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 07.8 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_preview.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 07.9 : Verify Refresh and Filter button are display on page header')
        pd_design.verify_filter_inputbox_value(filter_control_name, [''], 'Step 7.10 : Verify Business Region filter condition input value is None')
        
        """
            STEP 08 : Enter "EMEA" in Input control.
        """
        pd_preview.enter_input_value_for_filter_control(filter_control_name, input_value_to_enter='EMEA')
        pd_design.switch_to_container_frame(content_item_name)
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=max_time)
        
        """
            STEP 08.1 : Verify filter condition applied in the page.
        """
        #pd_design.create_html_report_data_set(TestCase_ID)
        pd_design.verify_html_report_data_set(TestCase_ID, 'Step 08.1 : Verify filter condition applied in the page.')
        pd_design.switch_to_default_page()
        
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
        pd_design.wait_for_visible_text("div[class^='pd-page-title']>div", visble_element_text='Page Heading', time_out=max_time)
        
        """
            STEP 11.1 : Verify filter control is in required state (solid red border available over the filter control).
        """
        pd_run.verify_filter_control_labels(expected_filter_control, 'Step 11.1 : Verify filter control is in required state in run page.')
        pd_run.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 11.2 : Verify solid red border available over the filter control.')
        pd_run.verify_page_heading_title(page_heading, 'Step 11.3 : Verify page heading')
        pd_run.verify_containers_title(expected_containers, 'Step 11.4 : Verify canvas containers')
        pd_run.verify_number_of_panels(1, 'Step 11.5 : Verify only one panel has added in canvas')
        pd_run.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 11.7 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_run.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 11.8 : Verify Refresh and Filter button are display on page header')
        pd_design.verify_filter_inputbox_value(filter_control_name, [''], 'Step 11.9 : Verify Business Region filter condition input value is None')
        pd_preview.verify_default_output_for_input_required_container(content_item_name, 'Step 11.10 : Verify report display with blank output in run page', expected_output='')
        
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