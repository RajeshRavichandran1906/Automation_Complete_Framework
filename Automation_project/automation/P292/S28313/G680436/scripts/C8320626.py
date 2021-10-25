'''
Created on May 29, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8320626
Test Case Title =  Adding required slider range control to the Page
'''

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.utillity import UtillityMethods
import time
import unittest

class C8320626_TestClass(BaseTestCase):

    def test_C8320626(self):
        
        """
        CLASS OBJECTS 
        """
        pd_design=page_designer.Design(self.driver)
        pd_preview=page_designer.Preview(self.driver)
        pd_run=page_designer.Run(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
      
        """
        COMMON TEST CASE VARIABLES 
        """
        TEST_CASE_ID='C8320626'
        TEMPLATE_NAME='Blank'
        CONTAINER_ITEM='10 - Slider Range Required'
        DATA_SET_NAME=TEST_CASE_ID + '_DataSet'
        FILTER_CONTRTOL_NAME='Move Slider'
        EXPECTED_TOTAL_PANELS=1
        EXPECTED_QUICK_FILTER_VALUE='2'
        EXPECTED_PAGE_HEADING=['Page Heading']
        EXPECTED_FILTER_CONTROLS=['Move Slider', "Move Slider"]
        EXPECTED_SLIDER_VALUES_CELL_1=['MIN=1', 'SELECTED=1', 'MAX=2']
        EXPECTED_SLIDER_VALUES_CELL_2=['MIN=3', 'SELECTED=3', 'MAX=5']
        EXPECTED_CONTAINER_BUTTONS=['Maximize', 'Options']
        EXPECTED_PAGE_HEADER_BUTTONS=['Refresh', 'Show filters']
        EXPECTED_CONTAINERS=['10 - Slider Range Required']
        #EXPECTED_PROPERTIES_TABS=['Settings', 'Style']
        EXPECTED_SETTING_TABS=['General Settings', 'Data Settings', 'Parameters']
        EXPECTED_GENERAL_TAB_PROPERTIES=['Type=Slider', 'ID=FILTERPANEL', 'Classes=', 'Tooltip=', 'Global name=']
        EXPECTED_DATA_TAB_PROPERTIES=['Default value=']
        EXPECTED_PARAMETER_PROPERTIES=['QTY_LOW (I11C)']
        
        """
            STEP 01 : Login to WF as Developer.Navigate to the folder P292_S10660/G433312.
            STEP 02 : Create new Designer Page.
            STEP 03 : Select Blank template.
        """
        pd_design.invoke_page_designer_and_select_template(TEMPLATE_NAME)
        
        """
            STEP 04 : Drag "10 - Slider Range Required" report into the page canvas from P292_S10660 > G433312 > Reference Items folder.
        """
        pd_design.drag_content_item_to_blank_canvas(CONTAINER_ITEM, 1, 'Reference Items')
       
        """
            STEP 04.1 : Verify report added to the page successfully.
        """
        pd_design.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 04.01 : Verify page heading')
        pd_design.verify_page_header_visible_buttons(['Refresh'], 'Step 04.02 : Verify Refresh button only display on page header')
        pd_design.verify_containers_title(EXPECTED_CONTAINERS, 'Step 04.03 : Verify {0} containers display in canvas'.format(EXPECTED_CONTAINERS))
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 04.04 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 04.05 : Verify 1 panel added in canvas')
        pd_design.verify_quick_filter_value(EXPECTED_QUICK_FILTER_VALUE, 'Step 04.06')
        pd_design.verify_default_output_for_input_required_container(CONTAINER_ITEM, 'Step 04.07 : Verify report added to the page successfully')
        
        """
            STEP 05 : Click Quick filter present in top right corner of the page.
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[data-ibx-type='pdFilterPanel'] div[class='ibx-label-text']", visble_element_text=FILTER_CONTRTOL_NAME, time_out=pd_design.home_page_short_timesleep, pause_time=4)
        
        """
            STEP 05.1 : Verify filter control bounded to the page with solid red border and red dotted border around it.
        """
        pd_design.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 05.01 : Verify {0} filter control only added'.format(EXPECTED_FILTER_CONTROLS))
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.02 : Verify filter control bounded to the page with red dotted border for cell 1.')
        pd_design.verify_filter_control_panel_is_selected(FILTER_CONTRTOL_NAME, 'Step 05.03 : Verify filter control bounded to the page with red dotted border for cell 2.', filter_control_position=2)
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_1, msg='Step 05.04 : Verify Slider values for cell 1')
        pd_design.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_2, msg='Step 05.05 : Verify Slider values for cell 2', filter_control_position=2)
        pd_design.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 05.06 : Verify 'Maximize', 'Options' buttons display on container tool bar")
        pd_design.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 05.07 : Verify Refresh and Filter buttons are display on page header')
        
        """
            STEP 06 : Select Properties present in top right corner of the page.
        """
        pd_design.click_property()
        pd_design.wait_for_visible_text("div[class^='pd-ps-name']", visble_element_text='Type', time_out=pd_design.home_page_short_timesleep)
        
        """
            STEP 06.1 : Verify all values in Properties panel.
        """
        #pd_design.verify_property_tabs(EXPECTED_PROPERTIES_TABS, 'Step 06.01 : Verify {0} tabs are display in Property window'.format(EXPECTED_PROPERTIES_TABS))
        pd_design.verify_setting_tabs(EXPECTED_SETTING_TABS, 'Step 06.02 : Verify {0} tabs are display in setting tab'.format(EXPECTED_SETTING_TABS))
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[0], EXPECTED_GENERAL_TAB_PROPERTIES, 'Step 06.03 : Verify General Settings properties')
        pd_design.verify_setting_tab_properties(EXPECTED_SETTING_TABS[1], EXPECTED_DATA_TAB_PROPERTIES, 'Step 06.04 : Verify Data Settings properties')
        pd_design.verify_setting_parameter_tab_properties(EXPECTED_PARAMETER_PROPERTIES, 'Step 06.05 : Verify parameter properties')
        
        """
            STEP 07 : Click Preview
        """
        pd_design.click_preview()
        
        """
            STEP 07.1 : Verify filter control required state (solid red border around the control) is retained in page preview.
        """
        pd_preview.verify_preview_is_displayed('Step 07.01 : Verify preview window is display')
        pd_preview.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 07.02 : Verify page heading')
        pd_preview.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 07.03 : Verify Refresh and Filter buttons are display on page header in preview')
        pd_preview.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 07.04 : Verify {0} filter control display in preview'.format(EXPECTED_FILTER_CONTROLS))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.05 : Verify {0} filter control not selected in preview for cell 1'.format(FILTER_CONTRTOL_NAME))
        pd_preview.verify_filter_control_panel_is_not_selected(FILTER_CONTRTOL_NAME, 'Step 07.06 : Verify {0} filter control not selected in preview for cell 2'.format(FILTER_CONTRTOL_NAME), filter_control_position=2)
        pd_preview.verify_containers_title(EXPECTED_CONTAINERS, 'Step 07.07 : Verify {0} containers display in preview'.format(EXPECTED_CONTAINERS))
        pd_preview.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 07.08 : Verify 'Maximize', 'Options' buttons display on {0} container tool bar in preview".format(CONTAINER_ITEM))
        pd_preview.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 07.09 : Verify 1 panel display in preview')
        pd_preview.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_1, msg='Step 07.10 : Verify Slider values in preview for cell 1')
        pd_preview.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_2, msg='Step 07.11 : Verify Slider valuesin preview for cell 2', filter_control_position=2)
        pd_preview.switch_to_container_frame(CONTAINER_ITEM)
        pd_preview.wait_for_visible_text("table[summary]>tbody>tr:nth-child(2)>td", visble_element_text='EMEA', time_out=pd_design.home_page_short_timesleep)
#         pd_design.create_html_report_data_set(DATA_SET_NAME)
        pd_design.verify_html_report_has_vertical_scrollbar('Step 07.11: Verify container report has vertical scroll bar')
        pd_preview.verify_html_report_data_set(DATA_SET_NAME, 'Step 07.12 : Verify report added to the page successfully.')
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
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", 60)
        
        """
            STEP 10 : Run created Designer Page.
        """
        pd_design.run_page_designer()
        time.sleep(20)
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text("div[class^='pd-page-title']", visble_element_text='Page Heading', time_out=pd_design.home_page_long_timesleep)
        
        """
            STEP 10.1 : Verify filter control is in required state (solid red border available around the filter control) at run time.
        """
        pd_run.verify_page_heading_title(EXPECTED_PAGE_HEADING, 'Step 10.01 : Verify page heading')
        pd_run.verify_page_header_visible_buttons(EXPECTED_PAGE_HEADER_BUTTONS, 'Step 10.02 : Verify Refresh and Filter buttons are display on page header in run page')
        pd_run.verify_filter_control_labels(EXPECTED_FILTER_CONTROLS, 'Step 10.03 : Verify {0} filter control display in run page'.format(EXPECTED_FILTER_CONTROLS))
        pd_run.verify_containers_title(EXPECTED_CONTAINERS, 'Step 10.04 : Verify {0} containers display in run page'.format(EXPECTED_CONTAINERS))
        pd_run.verify_container_title_bar_visible_buttons(CONTAINER_ITEM, EXPECTED_CONTAINER_BUTTONS, "Step 10.05 : Verify 'Maximize', 'Options' buttons display on container tool bar in run page")
        pd_run.verify_number_of_panels(EXPECTED_TOTAL_PANELS, 'Step 10.06 : Verify 1 panel display in run page')
        pd_run.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_1, msg='Step 10.07 : Verify Slider values in run page for cell 1')
        pd_run.verify_filter_slider_values(FILTER_CONTRTOL_NAME, EXPECTED_SLIDER_VALUES_CELL_2, msg='Step 10.08 : Verify Slider values in run page for cell 2', filter_control_position=2)
        
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

if __name__ == '__main__':
    unittest.main()