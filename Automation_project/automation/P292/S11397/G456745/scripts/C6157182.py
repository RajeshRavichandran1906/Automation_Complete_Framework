"""-------------------------------------------------------------------------------------------
Created on August 30, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157182
Test Case Title =  Adding optional other slider range control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C6157182_TestClass(BaseTestCase):

    def test_C6157182(self):
        
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
        TEST_CASE_ID='C6157182'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        CONTAINER_ITEM='12 - Slider Range Optional Other'
        FILTER_CONTRTOL_NAME1='Move Sliders to 3 and 5'
        FILTER_CONTRTOL_NAME2='Move Slider to 5'
        EXPECTED_FILTER_SLIDER1_DEFAULT_VALUES=['MIN=1', 'SELECTED=2', 'MAX=2']
        EXPECTED_FILTER_SLIDER2_DEFAULT_VALUES=['MIN=3', 'SELECTED=4', 'MAX=5']
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_QUICK_FILTER_VALUE='2'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Move Sliders to 3 and 5', 'Move Slider to 5']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['12 - Slider Range Optional Other']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Numeric range', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=2', 'Default value=4']
        EXPECTED_PARAMETER_PROPERTIES=['QTY_LOW (I11C)', 'QTY_HIGH (I11C)']
        
        """
            STEP 01 : Login to WF as Developer.Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "12 - Slider Range Optional Other" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
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
        pd_design.verify_html_report_data_set(DATA_SET_NAME1, 'Step 04.07 : Verify report added to the page successfully')
        pd_design.switch_to_default_page()
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME1, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify slider controls bounded to the page with red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify two filter slider controls added')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME1, 'Step 05.02 : Verify first filter slider control bounded to the page with red dotted border around it')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME2, 'Step 05.03 : Verify second filter slider control bounded to the page with red dotted border around it')
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME1, EXPECTED_FILTER_SLIDER1_DEFAULT_VALUES, 'Step 05.04 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER1_DEFAULT_VALUES))
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME2, EXPECTED_FILTER_SLIDER2_DEFAULT_VALUES, 'Step 05.05 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER2_DEFAULT_VALUES))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.07 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Right click right side slider control (right click on slider control label or slider control values/pin area else grid cell will be selected) and select Combine.
        """
        pd_design.select_filter_control_context_menu(FILTER_CONTRTOL_NAME1, 'Combine')
        
        """
            STEP 06.1 : Verify slider range control created.
        """
        EXPECTED_FILTER_CONTROLS=['Move Sliders to 3 and 5']
        EXPECTED_FILTER_SLIDER1_VALUES=['MIN=1', 'SELECTED=2 : 4', 'MAX=5']
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 06.01 : Verify slider range control created')
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME1, EXPECTED_FILTER_SLIDER1_VALUES, 'Step 06.02 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER1_VALUES))
        pd_design.verify_filter_slider_range_line_color(FILTER_CONTRTOL_NAME1, 'Step 06.03 : Verify filter slider range line display with blue color')
        
        """
            STEP 07 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=SHORT_TIME)
        
        """
            STEP 07.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 07.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 07.01 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 07.02 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_DATA_TAB_PROPERTIES, 'Step 07.03 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 07.04 : Verify parameter properties')
        
        """
            STEP 08 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 08.1 : Verify page loads successfully with slider range control in preview.
        """
        pd_preview.verify_preview_is_displayed('Step 08.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 08.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 08.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 08.04 : Verify filter slider controls display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME1, 'Step 08.05 : Verify filter slider control not bounded to the page with red dotted border around it')
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME1, EXPECTED_FILTER_SLIDER1_VALUES, 'Step 08.06 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER1_VALUES))
        pd_design.verify_filter_slider_range_line_color(FILTER_CONTRTOL_NAME1, 'Step 08.07 : Verify filter slider range line display with blue color')
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 08.08 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 08.09 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 08.10 : Verify 1 panel display in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 08.11 : Verify Page loads successfully in preview')
        pd_preview.switch_to_default_page()
        
        """
            STEP 09 : Move first slider pin to 3 and second slider pin to 5.
        """
        pd_preview.move_filter_slider_range(FILTER_CONTRTOL_NAME1, range_value1=3, range_value2=5)
        
        """
            STEP 09.1 : Verify slider condition applied in the page.
        """
        EXPECTED_FILTER_SLIDER_VALUES=['MIN=1', 'SELECTED=3 : 5', 'MAX=5']
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(4)", visble_element_text='6,308', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 09.01 : Verify slider condition applied in the page')
        pd_preview.switch_to_default_page()
        pd_preview.verify_filter_slider_values(FILTER_CONTRTOL_NAME1, EXPECTED_FILTER_SLIDER_VALUES, 'Step 09.02 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER_VALUES))
        pd_design.verify_filter_slider_range_line_color(FILTER_CONTRTOL_NAME1, 'Step 09.03 : Verify filter slider range line display with blue color')
         
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
            STEP 12.1 : Verify page runs successfully without error.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 12.01 : Verify page heading')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 12.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 12.03 : Verify filter slider control display in run page')
        pd_run.verify_filter_slider_values(FILTER_CONTRTOL_NAME1, EXPECTED_FILTER_SLIDER1_VALUES, 'Step 12.04 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER1_VALUES))
        pd_run.verify_filter_slider_range_line_color(FILTER_CONTRTOL_NAME1, 'Step 12.05 : Verify filter slider range line display with blue color')
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 12.06 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 12.07 : Verify 'Maximize', 'Options' buttons display on container tool bar in run page")
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 12.08 : Verify 1 panel display in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 12.09 : Verify page runs successfully without error in run page')
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