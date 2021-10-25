"""-------------------------------------------------------------------------------------------
Created on September 14, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157187
Test Case Title =  Adding optional date range control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157187_TestClass(BaseTestCase):

    def test_C6157187(self):
        
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
        TEMPLATE_NAME='Grid 3-3-3'
        TEST_CASE_ID='C6157187'
        START_DATE_TO_SELECT='Mar-10-2016'
        END_DATE_TO_SELECT='Mar-17-2016'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='17 - Date Range Optional'
        FILTER_CONTRTOL_NAME='Select 2016/03/10 through 2016/03/17'
        EXPECTED_TOTAL_PANELS=9
        EXPECTED_QUICK_FILTER_VALUE='2'
        EXPECTED_SELECTED_DATE=['Mar 10, 2016 - Mar 17, 2016']
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_DEFAULT_DATE_FILTER_VALUE=['']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['17 - Date Range Optional', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7', 'Panel 8', 'Panel 9']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Date range', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on', 'Placeholder text=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=_FOC_NULL', 'Default value=_FOC_NULL']
        EXPECTED_PARAMETER_PROPERTIES=['START_DAY (YYMD)', 'END_DAY (YYMD)']
        
        """
            STEP 01 : Login to WF as Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Grid 3-3-3 template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "17 - Date Range Optional" report into Panel 1 from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_container(CONTAINER_ITEM, 'Panel 1')
       
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
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        #pd_design.create_html_report_data_set(DATA_SET_NAME1)
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 04.07 : Verify report added to the page successfully')
        pd_design.switch_to_default_page()
    
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text='Select 2016/03/10 through 2016/03/17', time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify date filter controls bounded to the page with red dotted border.
        """
        STEP5_EXPECTED_FILTER_CONTROLS=['Select 2016/03/10 through 2016/03/17', 'Select 2016/03/10 through 2016/03/17']
        pd_design.verify_filter_control_labels(STEP5_EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify two filter date picker controls added')
        pd_design.verify_filter_control_panel_is_selected(STEP5_EXPECTED_FILTER_CONTROLS[0], 'Step 05.02 : Verify first date filter control bounded to the page with dotted red border around it')
        pd_design.verify_filter_control_panel_is_selected(STEP5_EXPECTED_FILTER_CONTROLS[1], 'Step 05.03 : Verify second date filter control bounded to the page with dotted red border around it')
        pd_design.verify_filter_date_picker_is_optional(STEP5_EXPECTED_FILTER_CONTROLS[0], 'Step 05.04 : Verify first date filter control is optional')
        pd_design.verify_filter_date_picker_is_optional(STEP5_EXPECTED_FILTER_CONTROLS[1], 'Step 05.05 : Verify second date filter control is optional')
        pd_design.verify_selected_date_in_filter_date_picker(STEP5_EXPECTED_FILTER_CONTROLS[0], EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 05.06 : Verify no date selected in first date picker control')
        pd_design.verify_selected_date_in_filter_date_picker(STEP5_EXPECTED_FILTER_CONTROLS[1], EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 05.07 : Verify no date selected in second date picker control')
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.08 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.09 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Right click second date control (right click over filter control label or calendar control area else grid cell will be selected) and select Combine.
        """
        pd_design.select_filter_control_context_menu(STEP5_EXPECTED_FILTER_CONTROLS[0], 'Combine')
        
        """
            STEP 06.1 : Verify date range control created successfully.
        """
        EXPECTED_FILTER_CONTROLS=['Select 2016/03/10 through 2016/03/17']
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 06.01 : Verify date range control created successfully')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 06.02 : Verify filter date range control bounded to the page with dotted red border around it')
        pd_design.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 06.03 : Verify date range filter control is optional')
        pd_design.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 06.04 : Verify no date selected in date range picker control')
        
        """
            STEP 07 : Right click date range control (right click over filter control label or calendar control area else grid cell will be selected) and select Settings.
        """
        pd_design.select_filter_control_context_menu(FILTER_CONTRTOL_NAME, 'Settings')
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 07.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 07.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 07.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 07.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_CONTROL_TAB_PROPERTIES, 'Step 07.04 : Verify Control Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[2], EXPECTED_DATA_TAB_PROPERTIES, 'Step 07.05 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 07.06 : Verify parameter properties')
        
        """
            STEP 08 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 08.1 : Verify page loads successfully with date range filter control.
        """
        pd_preview.verify_preview_is_displayed('Step 08.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 08.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 08.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 08.04 : Verify filter date range picker control display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 08.05 : Verify solid red border removed from date filter data range picker control in preview')
        pd_preview.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 08.06 : Verify filter date range picker control is optional')
        pd_preview.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 08.07 : Verify no date selected in filter date range picker control')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 08.08 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 08.09 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 08.10 : Verify {0} panel added in canvas'.format(EXPECTED_TOTAL_PANELS))
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 08.11 : Verify page loads successfully with date range filter control')
        pd_preview.switch_to_default_page()
        
        """
            STEP 09 : Select "Mar 10, 2016 - Mar 17, 2016" using date range calendar control.
        """
        pd_preview.select_date_from_date_range_picker(FILTER_CONTRTOL_NAME, START_DATE_TO_SELECT, END_DATE_TO_SELECT)
        
        """
            STEP 09.1 : Verify selected filter condition applied in the page.
        """
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(3)", visble_element_text='2,093', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 09.01 : Verify selected filter condition applied in the page')
        pd_preview.switch_to_default_page()
        pd_preview.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 09.02 : Verify solid red border removed from date filter control')
        pd_preview.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_DATE, 'Step 09.03 : Verify {0} data selected in filter date range picker'.format(EXPECTED_SELECTED_DATE))
        
        """
            STEP 10 : Return back to designer using blue arrow in preview. 
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 11 : Save and Close the Designer.
        """
        pd_design.save_page_from_toolbar_with_default_name()
        pd_design.switch_to_previous_window()
        
        """
            STEP 12 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 12.1 : Verify page runs successfully with Date Range filter control.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 12.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 12.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 12.03 : Verify filter date range picker controls display in run page')
        pd_run.verify_filter_date_picker_is_optional(FILTER_CONTRTOL_NAME, 'Step 12.04 : Verify date filter control is optional')
        pd_run.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_DATE_FILTER_VALUE, 'Step 12.05 : Verify no date selected in date filter control'.format(EXPECTED_DEFAULT_DATE_FILTER_VALUE))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 12.06 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 12.07 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 12.08 : Verify {0} panels display in run page'.format(EXPECTED_TOTAL_PANELS))
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 12.09 : Verify page runs successfully with Date Range filter control')
        pd_run.switch_to_default_page()
        pd_run.swtich_to_homepage_runwindow_frame()
           
        """
            STEP 13 : Select "Mar 10, 2016 - Mar 17, 2016" using date range calendar control.
        """    
        pd_run.select_date_from_date_range_picker(FILTER_CONTRTOL_NAME, START_DATE_TO_SELECT, END_DATE_TO_SELECT)
        
        """
            STEP 13.1 : Verify selected filter condition applied in the page.
        """
        pd_run.verify_selected_date_in_filter_date_picker(FILTER_CONTRTOL_NAME, EXPECTED_SELECTED_DATE, 'Step 13.01 : Verify {0} data selected in filter date range picker'.format(EXPECTED_SELECTED_DATE))
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(3)", visble_element_text='2,093', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME2, 'Step 13.02 : Verify selected filter condition applied in the page.')
        pd_run.switch_to_default_page()
        
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