"""-------------------------------------------------------------------------------------------
Created on July 12, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157171
Test Case Title =  Adding required input filter control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.lib import utillity

class C6157171_TestClass(BaseTestCase):

    def test_C6157171(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        SHORT_TIME=10
        LONG_TIME=40
        TEMPLATE_NAME='Blank'
        TEST_CASE_ID='C6157171'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        CONTAINER_ITEM='01 - Simple Input Required'
        FILTER_CONTRTOL_NAME='Business Region:'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Business Region:']
        EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE=['']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['01 - Simple Input Required']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Input', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=off', 'Placeholder text=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        EXPECTED_QUICK_FILTER_PRORERTIES={'text':'1', 'background_color':'mandy', 'font_size':'12px', 'position':'absolute', 'text_align':'center'}
        
        """
            STEP 01 : Login as WF Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "01 - Simple Input Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
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
        pd_design.verify_quick_filter_properties(EXPECTED_QUICK_FILTER_PRORERTIES, 'Step 04.06')
        pd_design.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 04.07 : Verify report added to the page successfully')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Business Region:', time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with solid red border and red dotted border.
        """
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.01 : Verify {0} button are display on page header'.format(EXPECTED_PAGE_HEADER_BUTTONS))
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.02 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify {0} filter drop down control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_inputbox_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 05.04 : Verify filter control bounded to the page with solid red border.')
        pd_design.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 05.05 : Verify Business Region filter condition input value is None')
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are available in Properties panel'.format(EXPECTED_PROPERTIES_TABS))
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
            STEP 07.1 : Verify filter control required state is retained in page preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter button are display on page header')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify filter control required state is retained in page preview.')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify {0} filter drop down control not bounded to the page with red dotted border around it in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_inputbox_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify filter control bounded to the page with solid red border.')
        pd_preview.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 07.07 : Verify Business Region filter condition input value is None')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.08 : Verify canvas containers')
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.09 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.10 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_preview.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 07.11 : Verify report display in preview')
        
        """
            STEP 08 : Enter "EMEA" in Input control.
        """
        pd_preview.enter_input_value_for_filter_control(FILTER_CONTRTOL_NAME, input_value_to_enter='EMEA')
        pd_design.switch_to_container_frame("01 - Simple Input Required")
        util_obj.synchronize_with_number_of_element("table[summary]>tbody>tr:nth-child(2)>td", 3, 50)
        
        """
            STEP 08.1 : Verify filter condition applied in the page.
        """
        #pd_design.create_html_report_data_set(DATA_SET_NAME1)
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 08.01 : Verify filter condition applied in the page.')
        pd_design.switch_to_default_page()
        pd_preview.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 08.02 : Verify solid red border removed from filter inputbox')
        
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
            STEP 11.1 : Verify filter control is in required state (solid red border available over the filter control).
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 11.01 : Verify page heading')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 11.02 : Verify Refresh and Filter button are display on page header')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 11.02 : Verify filter control required state is retained in run.')
        pd_run.verify_filter_inputbox_is_not_optional(FILTER_CONTRTOL_NAME, 'Step 11.04 : Verify filter control bounded to the page with solid red border.')
        pd_run.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_INPUTBOX_VALUE, 'Step 11.05 : Verify Business Region filter condition input value is None')
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 11.06 : Verify canvas containers')
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 11.07 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 11.08 : Verify ['Maximize', 'Options'] buttons display on container tool bar")
        pd_run.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 11.09 : Verify report display in preview')
        
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