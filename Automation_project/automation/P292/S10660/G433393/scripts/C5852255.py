"""-------------------------------------------------------------------------------------------
Created on June 05, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852255
Test Case Title =  Adding optional static single-select dropdown control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods as utils
from common.wftools import page_designer

class C5852255_TestClass(BaseTestCase):

    def test_C5852255(self):
        
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
        TEST_CASE_ID='C5852255'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='21 - Single Select Static Optional Other'
        FILTER_CONTRTOL_NAME='Select North America'
        FILTER_DROPDOWN_SELECTION_OPTION='North America'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Select North America']
        EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE=['EMEA']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Filter']
        EXPECTED_CONTAINERS=['21 - Single Select Static Optional Other']
        EXPECTED_SETTING_TABS=['General Settings', 'Control Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Single select', 'Tooltip=', 'Global name=']
        EXPECTED_CONTROL_TAB_PROPERTIES=['Optional=on', 'Placeholder text=Make a selection...', 'Search=off']
        EXPECTED_DATA_TAB_PROPERTIES=['Show All option=off', 'Display text=All', 'Default value=EMEA']
        EXPECTED_PARAMETER_PROPERTIES=['BUSINESS_REGION (A15V)']
        EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_QUICK_FILTER_VALUE='1'
        
        """
            STEP 01 : Login to WF as Developer. Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "21 - Single Select Static Optional Other" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
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
        pd_design.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        #pd_design.create_html_report_data_set(DATA_SET_NAME1)
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 04.07 : Verify report added to the page successfully.')
        pd_design.switch_to_default_page()
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify dropdown control bounded to the page with a default value and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify {0} filter drop down control added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify {0} drop down control bounded to the page with red dotted border around it'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify {0} drop down control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_design.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 05.04 : Verify {0} option selected as default in filter drop down'.format(EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.05 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.06 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']>div", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
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
            STEP 07.1 : Verify page loads successfully in preview with default value condition.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify {0} filter controls display in preview'.format(EXPECTED_FILTER_CONTROLS))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify {0} filter control not bounded to the page with red dotted border around it in preview'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify {0} drop down control is optional'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 07.07 : Verify {0} option selected as default in filter drop down'.format(EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.08 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.09 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.10 : Verify 1 panel display in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 07.11 : Verify page loads successfully in preview with default value condition')
        pd_preview.switch_to_default_page()
       
        """
            STEP 08 : Click dropdown control press ctrl and multi-select "North America" and "South America" value.
        """
        MULTI_OPTIONS=['North America', 'South America']
        try :
            pd_preview.select_multiple_options_from_filter_dropdown_using_ctrl(FILTER_CONTRTOL_NAME, MULTI_OPTIONS)
            multi_option=True
        except :
            multi_option=False
       
        """
           STEP 08.1 : Verify can't able to multi-select values.
        """
        utils.asequal(self, False, multi_option, 'Step 08.01 : Verify can not able to multi-select values')
        pd_preview.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, [MULTI_OPTIONS[0]], 'Step 08.02 : Verify user can select only single option from filter drop down')
       
        """
            STEP 09 : Select "North America" value in dropdown.
        """
        pd_preview.select_filter_dropdown_option(FILTER_CONTRTOL_NAME, FILTER_DROPDOWN_SELECTION_OPTION)
        
        """
            STEP 09.1 : Verify filter condition applied in the page.
        """
        pd_preview.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, [FILTER_DROPDOWN_SELECTION_OPTION], 'Step 09.01 : Verify {0} option selected in filter drop down'.format(FILTER_DROPDOWN_SELECTION_OPTION))
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='North America', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 09.02 : Verify filter condition applied in the page')
        pd_preview.switch_to_default_page()
        
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
        pd_run.wait_for_visible_text("div[class^='pd-page-title']>div", visble_element_text='Page Heading', time_out=LONG_TIME)
        
        """
            STEP 12.1 : Verify page runs successfully with default value filter condition.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 11.01 : Verify page heading  in run page')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 11.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 11.03 : Verify {0} filter controls display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_filter_dropdown_is_optional(FILTER_CONTRTOL_NAME, 'Step 11.04 : Verify {0} drop down control not bounded to the page with solid red border in run page'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_selected_value_of_filter_dropdown(FILTER_CONTRTOL_NAME, EXPECTED_DEFAULT_FILTER_DROPDOWN_VALUE, 'Step 11.05 : Verify {0} filter drop down control default text in Make a selection...'.format(FILTER_CONTRTOL_NAME))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 11.06 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 11.07 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in run page".format(CONTAINER_ITEM))
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 11.08 : Verify 1 panel display in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 11.09 : Verify page runs successfully with default value filter condition')
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