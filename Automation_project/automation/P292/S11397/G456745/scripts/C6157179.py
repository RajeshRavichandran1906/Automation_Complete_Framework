"""-------------------------------------------------------------------------------------------
Created on August 30, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6157179
Test Case Title =  Adding optional other slider control to the Page
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C6157179_TestClass(BaseTestCase):

    def test_C6157179(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        SHORT_TIME=10
        LONG_TIME=40
        TEST_CASE_ID='C6157179'
        TEMPLATE_NAME='Blank'
        CONTAINER_ITEM='09 - Slider Optional Other'
        DATA_SET_NAME1=TEST_CASE_ID + '_DataSet_01'
        DATA_SET_NAME2=TEST_CASE_ID + '_DataSet_02'
        FILTER_CONTRTOL_NAME='Move Slider to 5011'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_QUICK_FILTER_VALUE='1'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Move Slider to 5011']
        EXPECTED_FILTER_SLIDER_DEFAULT_VALUES=['MIN=5000', 'SELECTED=5008', 'MAX=5020']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_CONTAINERS=['09 - Slider Optional Other']
        EXPECTED_SETTING_TABS=['General Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Slider', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=5008']
        EXPECTED_PARAMETER_PROPERTIES=['ID_PRODUCT (I9)']
        
        """
            STEP 01 : Login to WF as Developer.Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "09 - Slider Optional Other" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
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
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=SHORT_TIME, pause_time=4)
        
        """
            STEP 05.1 : Verify slider control bounded to the page with red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify filter control only added')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify slider control bounded to the page with red dotted border around it')
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_SLIDER_DEFAULT_VALUES, 'Step 05.03 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER_DEFAULT_VALUES))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.05 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Right click slider control (right click on slider control label or slider control values/pin area else grid cell will be selected) and select Settings.
        """
        filter_obj = utils.validate_and_get_webdriver_object("div[class*='pd-filter-cell'][data-grid-span='1']:nth-child(1)", "Filter Css")
        core_utils.python_right_click(filter_obj, yoffset = -35)
        utils.synchronize_with_visble_text(".pd-filter-menu", "Settings", 30)
        
        settings_obj = utils.validate_and_get_webdriver_object(".pd-filter-menu div[data-ibx-name='miSettings']", "Setting css")
        core_utils.python_left_click(settings_obj)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 06.01 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 06.02 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_DATA_TAB_PROPERTIES, 'Step 06.03 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 06.04 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify page loads successfully with slider control in preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify filter control display in preview')
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify filter control not selected in preview')
        pd_preview.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_SLIDER_DEFAULT_VALUES, 'Step 07.06 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER_DEFAULT_VALUES))
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.07 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.09 : Verify 1 panel display in preview')
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME1, 'Step 07.10 : Verify page loads successfully in preview')
        pd_preview.switch_to_default_page()
        
        """
            STEP 08 : Move slider pin to 5011 position.
        """
        pd_preview.move_filter_slider(FILTER_CONTRTOL_NAME, 5011)
        
        """
            STEP 08.1 : Verify slider condition applied in the page.
        """
        EXPECTED_FILTER_SLIDER_VALUES=['MIN=5000', 'SELECTED=5011', 'MAX=5020']
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td:nth-child(4)", visble_element_text='5011', time_out=LONG_TIME)
        #pd_preview.create_html_report_data_set(DATA_SET_NAME2)
        pd_preview.verify_html_report_data_set(DATA_SET_NAME2, 'Step 08.01 : Verify slider condition applied in the page')
        pd_preview.switch_to_default_page()
        pd_preview.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_SLIDER_VALUES, 'Step 08.02 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER_VALUES))
        
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
            STEP 11.1 : Verify page runs successfully without error.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 11.01 : Verify page heading')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 11.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 11.03 : Verify filter control display in run page')
        pd_run.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_FILTER_SLIDER_DEFAULT_VALUES, 'Step 11.04 : Verify {0} value are display in slider control'.format(EXPECTED_FILTER_SLIDER_DEFAULT_VALUES))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 11.05 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 11.06 : Verify 'Maximize', 'Options' buttons display on container tool bar in run page")
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 11.07 : Verify 1 panel display in run page')
        pd_run.switch_to_container_frame(CONTAINER_ITEM)
        pd_run.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=LONG_TIME)
        pd_run.verify_html_report_data_set(DATA_SET_NAME1, 'Step 11.08 : Verify page runs successfully without error')
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