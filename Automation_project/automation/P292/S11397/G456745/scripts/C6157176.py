"""-------------------------------------------------------------------------------------------
Created on July 16, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157176
Test Case Title =  Adding optional other numeric input filter control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157176_TestClass(BaseTestCase):

    def test_C6157176(self):
        
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
        MAX_TIME=25
        TEST_CASE_ID='C6157176'
        CONTAINER_ITEM='06 - Simple Numeric Input Optional Other'
        DATA_SET_NAME=TEST_CASE_ID + '_DataSet_01'
        FILTER_CONTRTOL_NAME='Enter 5012'
        EXPECTED_TOTAL_PANELS=3
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Enter 5012']
        EXPECTED_DEFAULT_FILTER_CONTROL_VALUE=['6011']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['06 - Simple Numeric Input Optional Other', 'Panel 2', 'Panel 3']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Input', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on', 'Placeholder text=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=6011']
        EXPECTED_PARAMETER_PROPERTIES=['ID_PRODUCT (I9)']
        
        """
            STEP 01 : Login to WF as Developer.Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Grid 2-1 template.
        """
        pd_design.invoke_page_designer_and_select_template('Grid 2-1')
        
        """
            STEP 04 : Drag "06 - Simple Numeric Input Optional Other" report into the Panel 1 from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_container(CONTAINER_ITEM, 'Panel 1')
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 04.01 : Verify containers title')
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 04.02 : Verify 3 panels added in canvas')
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 04.03')
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 04.05 : Verify Refresh button only display on page header')
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 04.06 : Verify page heading')
        pd_design.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 04.07 : Verify Panel 2 is blank')
        pd_design.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 04.08 : Verify Panel 3 is blank')
        pd_design.switch_to_container_frame(CONTAINER_ITEM)
        #pd_design.create_html_report_data_set(DATA_SET_NAME)
        pd_design.verify_html_report_data_set(DATA_SET_NAME, 'Step 04.09 : Verify report display in canvas')
        pd_design.switch_to_default_page()
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Enter 5012', time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with a default value and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify Enter 5012 filter condition only added')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify filter control bounded to the page with red dotted border.')
        pd_design.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify filter control input box not selected')
        pd_design.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_CONTROL_VALUE, 'Step 05.04 : Verify filter input default value is {0}'.format(EXPECTED_DEFAULT_FILTER_CONTROL_VALUE))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.05 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.06 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify Property_tabs')
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 06.01 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 06.02 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 06.03 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 06.04 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 06.05 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify page loads successfully with default value filter condition.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window is display')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.02 : Verify containers title in preview')
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.03 : Verify 3 panels added in canvas')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify Enter 5012 filter condition display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify {0} filter control not selected in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify filter control input box not selected in preview')
        pd_preview.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_CONTROL_VALUE, 'Step 07.04 : Verify filter input default value is {0}'.format(EXPECTED_DEFAULT_FILTER_CONTROL_VALUE))
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.06 : Verify page heading')
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.07 : Verify 'Maximize', 'Options' buttons display on container tool bar in preview")
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.08 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 07.09 : Verify Panel 2 is blank in preview')
        pd_preview.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 07.10 : Verify Panel 3 is blank in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME, 'Step 07.11 : Verify report display in preview')
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
            STEP 10 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=MAX_TIME)
        
        """
            STEP 10.1 : Verify default filter condition retained at run time of the page.
        """
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 10.01 : Verify containers title in run page')
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 10.02 : Verify 3 panels added in canvas')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 10.03 : Verify Enter 5012 filter condition display in run page')
        pd_run.verify_filter_inputbox_is_optional(FILTER_CONTRTOL_NAME, 'Step 10.04 : Verify filter control input box not selected in run page')
        pd_run.verify_filter_inputbox_value(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_CONTROL_VALUE, 'Step 10.05 : Verify filter input default value is {0}'.format(EXPECTED_DEFAULT_FILTER_CONTROL_VALUE))
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 10.06 : Verify page heading in run page')
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 10.07 : Verify 'Maximize', 'Options' buttons display on container tool bar in run page")
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 10.08 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=MAX_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME, 'Step 10.09 : Verify default filter condition retained at run time of the page run page')
        pd_run.switch_to_default_page()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(EXPECTED_CONTAINERS[1], 'Step 10.10 : Verify Panel 2 is blank in run page')
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_blank_container_output(EXPECTED_CONTAINERS[2], 'Step 10.11 : Verify Panel 3 is blank in run page')
        
        """
            STEP 11 : Close run window.
        """
        pd_run.close_homepage_run_window()
        
        """
            STEP 12 : Delete the created Page.
        """
        pd_design.delete_saved_page_designer()
        
        """
            STEP 13 : Sign Out WF.
        """