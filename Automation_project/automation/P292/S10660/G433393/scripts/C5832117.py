"""-------------------------------------------------------------------------------------------
Created on May 25, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5832117
Test Case Title =  Adding required numeric input filter control to the Page
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C5832117_TestClass(BaseTestCase):

    def test_C5832117(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        short_timeout=10
        max_time=25
        TestCase_ID='C5832117'
        page_heading=['Page Heading']
        containers=['04 - Simple Numeric Input Required', 'Panel 2', 'Panel 3']
        filter_controls=['Enter 5012']
        filter_control_name='Enter 5012'
        content_item_name='04 - Simple Numeric Input Required'
        container_visible_buttons=['Maximize', 'Options']
        page_header_visible_buttons=['Refresh', 'Filter']
        default_filter_control_value=['']
        total_panels=3
        
        """
            STEP 01 : Login to WF as Developer.Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Grid 2-1 template.
        """
        pd_design.invoke_page_designer_and_select_template('Grid 2-1')
        
        """
            STEP 04 : Drag "04 - Simple Numeric Input Required" report into the Panel 1 from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_container(content_item_name, 'Panel 1')
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_default_output_for_input_required_container(content_item_name, 'Step 04.1 : Verify 04 - Simple Numeric Input Required container display "A required parameter is missing"')
        pd_design.verify_containers_title(containers, 'Step 04.2 : Verify canvas containers')
        pd_design.verify_number_of_panels(total_panels, 'Step 04.3 : Verify 3 panels added in canvas')
        pd_design.verify_quick_filter_value('1', 'Step 04.4')
        pd_design.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 04.5 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_preview.verify_page_header_visible_buttons(['Refresh'], 'Step 04.6 : Verify Refresh button only display on page header')
        pd_design.verify_blank_container_output(containers[1], 'Step 04.4 : Verify Panel 2 is blank')
        pd_design.verify_blank_container_output(containers[1], 'Step 04.4 : Verify Panel 3 is blank')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Enter 5012', time_out=short_timeout, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with solid red border and red dotted border.
        """
        pd_design.verify_filter_control_panel_is_selected(filter_control_name, 'Step 05.1 : Verify filter control bounded to the page with red dotted border.')
        pd_design.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 05.2 : Verify filter control bounded to the page with solid red border.')
        pd_design.verify_filter_control_labels(filter_controls, 'Step 05.3 : Verify Enter 5012 filter condition only added')
        pd_design.verify_page_heading_title(page_heading, 'Step 05.4 : Verify page heading')
        pd_design.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 05.5 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 05.6 : Verify Enter 5012 filter condition default input value is None')
        
        """
            STEP 06 : Right click over the filter control (right click over filter control label or control input area else grid cell will be selected) and select Settings.
        """
        pd_design.select_filter_control_context_menu(filter_control_name, 'Settings')
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']>div", visble_element_text='Type', time_out=short_timeout)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        expected_setting_tabs=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        general_settings=['Type=Input', 'Tooltip=', 'Global name=']
        control_settings=['Optional=off', 'Placeholder text=']
        dat_settings=['Default value=']
        parameter_properties=['ID_PRODUCT (I9)']
        pd_design.verify_property_tabs(['Settings', 'Style'], 'Step 06.1 : Verify Property_tabs')
        pd_design.verify_setting_tabs(expected_setting_tabs, 'Step 06.2 : Verify {0} tabs are display in setting tab'.format(expected_setting_tabs))
        pd_design.verify_setting_tab_properties(expected_setting_tabs[0], general_settings, 'Step 06.3 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(expected_setting_tabs[1], control_settings, 'Step 06.4 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(expected_setting_tabs[2], dat_settings, 'Step 06.5 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(parameter_properties, 'Step 06.6 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify filter control required state (solid red border over the filter control) is retained in page preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.1 : Verify preview window display')
        pd_design.verify_default_output_for_input_required_container(content_item_name, 'Step 01.1 : Verify 04 - Simple Numeric Input Required container display "A required parameter is missing"')
        pd_preview.verify_filter_control_labels(filter_controls, 'Step 07.2 : Verify filter control required state is retained in page preview.')
        pd_design.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 07.3 : Verify filter control bounded to the page with solid red border.')
        pd_design.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 07.4 : Verify Enter 5012 filter condition input value is None')
        pd_preview.verify_page_heading_title(page_heading, 'Step 07.5 : Verify page heading')
        pd_preview.verify_containers_title(containers, 'Step 07.6 : Verify canvas containers')
        pd_preview.verify_number_of_panels(total_panels, 'Step 07.7 : Verify 3 panels display in preview')
        pd_preview.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 07.8 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_preview.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 07.9 : Verify Refresh and Filter button are display on page header')
        pd_preview.verify_number_of_panels(total_panels, 'Step 7.10 : Verify 3 panels display in preview')
        
        """    
            STEP 08 : Enter "5012" in Input control.
        """
        pd_preview.enter_input_value_for_filter_control(filter_control_name, input_value_to_enter='5012')
        
        """
            STEP 08.1 : Verify filter condition applied in the page.
        """
        pd_design.switch_to_container_frame(content_item_name, wait_time=2)
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=max_time)
        #pd_preview.create_html_report_data_set(TestCase_ID + '_DataSet_01')
        pd_preview.verify_html_report_data_set(TestCase_ID + '_DataSet_01', 'Step 08.1 : Verify filter condition applied in the page.')
        pd_preview.switch_to_default_page()
        pd_design.verify_blank_container_output(containers[1], 'Step 08.2 : Verify Panel 2 is blank')
        pd_design.verify_blank_container_output(containers[1], 'Step 08.3 : Verify Panel 3 is blank')
        
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
        pd_run.verify_filter_control_labels(filter_controls, 'Step 11.2 : Verify filter control required state is retained in page preview.')
        pd_run.verify_filter_inputbox_is_not_optional(filter_control_name, 'Step 11.3 : Verify filter control bounded to the page with solid red border.')
        pd_run.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 11.4 : Verify Enter 5012 filter condition input value is None')
        pd_run.verify_page_heading_title(page_heading, 'Step 11.5 : Verify page heading')
        pd_run.verify_containers_title(containers, 'Step 11.6 : Verify canvas containers')
        pd_run.verify_number_of_panels(total_panels, 'Step 11.7 : Verify 2 panels display in run page')
        pd_run.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 11.8 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_run.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 11.9 : Verify Refresh and Filter button are display on page header')
        pd_preview.verify_number_of_panels(total_panels, 'Step 11.10 : Verify 3 panels display in run page')
        pd_run.verify_default_output_for_input_required_container(content_item_name, 'Step 11.12 : Verify 04 - Simple Numeric Input Required container display "A required parameter is missing"', expected_output='')
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(containers[1], 'Step 11.11 : Verify Panel 2 is blank')
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(containers[1], 'Step 11.12 : Verify Panel 3 is blank')
        
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