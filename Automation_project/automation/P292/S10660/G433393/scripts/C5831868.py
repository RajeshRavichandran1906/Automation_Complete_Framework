"""-------------------------------------------------------------------------------------------
Created on May 24, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831868
Test Case Title =  Adding optional input filter control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C5831868_TestClass(BaseTestCase):

    def test_C5831868(self):
        
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
        TestCase_ID='C5831868'
        page_heading=['Page Heading']
        containers_title=['02 - Simple Input Optional All']
        filter_control_lables=['Business Region:']
        filter_control_name='Business Region:'
        content_item_name='02 - Simple Input Optional All'
        container_visible_buttons=['Maximize', 'Options']
        page_header_visible_buttons=['Refresh', 'Filter']
        default_filter_control_value=['']
        
        """
            STEP 01 : Login as WF Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template('Blank')
        
        """
            STEP 04 : Drag "02 - Simple Input Optional All" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_blank_canvas(content_item_name, 1)
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.switch_to_container_frame(content_item_name)
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=max_time)
        #pd_design.create_html_report_data_set(TestCase_ID + '_DataSet_01')
        pd_design.verify_html_report_data_set(TestCase_ID + '_DataSet_01', 'Step 08.1 : Verify filter condition applied in the page.')
        pd_design.switch_to_default_page()
        pd_design.verify_containers_title(containers_title, 'Step 01.2 : Verify canvas containers')
        pd_design.verify_number_of_panels(1, 'Step 01.3 : Verify only one panel has added in canvas')
        pd_design.verify_quick_filter_value('1', 'Step 01.4')
        pd_design.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 01.5 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_preview.verify_page_header_visible_buttons(['Refresh'], 'Step 01.6 : Verify Refresh button only display on page header')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Business Region:', time_out=short_timeout, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with red dotted border around the filter control.
        """
        pd_design.verify_filter_control_panel_is_selected('Business Region:', 'Step 05.1 : Verify filter control bounded to the page with red dotted border around the filter control.')
        pd_design.verify_filter_control_labels(filter_control_lables, 'Step 05.2 : Verify Business Region filter condition only added')
        pd_design.verify_page_heading_title(page_heading, 'Step 05.3 : Verify page heading')
        pd_design.verify_page_tab_groups(['Page 1'], 'Step 05.4 : Verify page tab groups')
        pd_design.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 05.5 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 05.6 : Verify Business Region filter condition default input value is None')
        
        """
            STEP 06 : Right click filter control (right click over control label or control input area else grid cell will be selected) and select Settings..
        """
        pd_design.select_filter_control_context_menu(filter_control_name, 'Settings')
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']>div", visble_element_text='Type', time_out=short_timeout)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        expected_setting_tabs=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        general_settings=['Type=Input', 'Tooltip=', 'Global name=']
        control_settings=['Optional=on', 'Placeholder text=']
        dat_settings=['Default value=_FOC_NULL']
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
            STEP 07.1 : Scroll down the report and verify all values are available in the report.
        """
        pd_preview.verify_preview_is_displayed('Step 07.1 : Verify preview window display')
        pd_design.switch_to_container_frame(content_item_name)
        pd_design.verify_html_report_data_set(TestCase_ID + '_DataSet_01', 'Step 07.2 : Verify Scroll down the report and verify all values are available in the report..')
        pd_design.switch_to_default_page()
        pd_preview.verify_filter_control_labels(filter_control_lables, 'Step 07.3 : Verify filter controls.')
        pd_preview.verify_page_heading_title(page_heading, 'Step 07.4 : Verify page heading')
        pd_preview.verify_containers_title(containers_title, 'Step 07.5 : Verify canvas containers')
        pd_preview.verify_number_of_panels(1, 'Step 07.6 : Verify only one panel has added in canvas')
        pd_preview.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 07.8 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_preview.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 07.9 : Verify Refresh and Filter button are display on page header')
        pd_design.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 7.10 : Verify Business Region filter condition input value is None')
        
    
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
            STEP 10 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_design.wait_for_visible_text("div[class^='pd-page-title']>div", visble_element_text='Page Heading', time_out=max_time)
        
        """
            STEP 10.1 : Verify page run successfully with "_FOC_NULL" filter condition (all values are available in the report).
        """
        pd_run.verify_filter_control_labels(filter_control_lables, 'Step 10.2 : Verify filter control is in required state in run page.')
        pd_run.verify_page_heading_title(page_heading, 'Step 10.3 : Verify page heading')
        pd_run.verify_containers_title(containers_title, 'Step 10.4 : Verify canvas containers')
        pd_run.verify_number_of_panels(1, 'Step 10.5 : Verify only one panel has added in canvas')
        pd_run.verify_container_title_bar_visible_buttons(content_item_name, container_visible_buttons, "Step 10.6 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_run.verify_page_header_visible_buttons(page_header_visible_buttons, 'Step 10.7 : Verify Refresh and Filter button are display on page header')
        pd_design.verify_filter_inputbox_value(filter_control_name, default_filter_control_value, 'Step 10.8 : Verify Business Region filter condition input value is None')
        pd_design.switch_to_container_frame(content_item_name)
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=max_time)
        pd_design.verify_html_report_data_set(TestCase_ID + '_DataSet_01', 'Step 10.8 : Verify page run successfully with "_FOC_NULL" filter condition (all values are available in the report)')
        pd_design.switch_to_default_page()
        
        """
            STEP 11 : Enter "EMEA" in Input control.
        """
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.enter_input_value_for_filter_control(filter_control_name, input_value_to_enter='EMEA')
        
        """
            STEP 11.1 : Verify filter condition applied in the page.
        """
        pd_design.switch_to_container_frame(content_item_name, wait_time=5)
        pd_design.wait_for_number_of_element("table[summary]>tbody>tr", expected_number=9, time_out=short_timeout)
        #pd_design.create_html_report_data_set(TestCase_ID + '_DataSet_02')
        pd_design.verify_html_report_data_set(TestCase_ID + '_DataSet_02', 'Step 11.1 : Verify filter condition applied in the page..')
        pd_design.switch_to_default_page()
        
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