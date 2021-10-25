'''
Created on Sep 27, 2018

@author: Magesh

Testcase Name : Verify to Interact with "Sales by Country and Product"
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2275873
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C2275871_TestClass(BaseTestCase):

    def test_C2275871(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C2275873"
        fex_name='Sales_by_Country_and_Product'
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        preview_css1="#MAINTABLE_wbody1 svg>g rect[class^='riser']"
        preview_css2="#MAINTABLE_wbody2 svg>g path[class^='riser']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Run the Chart using the below API URL
        http://machine:port/ibi_apps8/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Visualizations&BIP_item=Sales_by_Country_and_Product.fex
        """
        visual_obj.run_visualization_using_api(fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=504, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=68, time_out=wait_time)
         
        """
        Verify the following output
        """
        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017','2018']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 72, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c5!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        "---choropleth_map---"
        parent_css_with_tag_name="#MAINTABLE_wbody2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 68, msg="Step 04.9:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g27!mregion!']", 'elf_green', parent_css='#MAINTABLE_wbody2', msg="Step 04.10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 04.11: Verify legends")
        
        expected_items_list=['All', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_show_prompt_table_list(expected_items_list, parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_item_checked_status_in_show_prompt_table('All', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_slider_min_max_value_in_run_window(2006, parent_css='#LOBJPrompt_44', drag_button='min', comparison_type='integer', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(2023, parent_css='#LOBJPrompt_44', drag_button='max', comparison_type='integer', msg = 'Step 04.5:')
        
        visual_obj.verify_slider_min_max_value_in_run_window(17.99, parent_css='#LOBJPrompt_55', drag_button='min', comparison_type='floating', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(15999.4, parent_css='#LOBJPrompt_55', drag_button='max', comparison_type='floating', msg = 'Step 04.5:')
        
        """
        Step 03: Go to the Map, hover on "Store State Province: Illinois,United States" > Click Exclude from chart
        """
        riser_css='riser!s0!g8!mregion!'
        tooltip_menu='Exclude from Chart'
        parent_css="#MAINTABLE_wbody2"
        visual_obj.select_tooltip(riser_css, tooltip_menu, parent_css=parent_css,move_to_tooltip=True)
        
        """
        Verify the Result
        """
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=67, time_out=wait_time)
        parent_css_with_tag_name="#MAINTABLE_wbody2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 67, msg="Step 04.9:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g26!mregion!']", 'elf_green', parent_css='#MAINTABLE_wbody2', msg="Step 04.10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 03.11: Verify legends")
        
        """
        Step 04: Click Run menu icon on Map > Click Show Data
        """
        menu_option_button_name_show='show_report_css'
        menucontainer_css="#MAINTABLE_menuContainer2"
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, menucontainer_css)
         
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds01.xlsx'
        table_css='#MAINTABLE_wbody3 .arPivot table > tbody > tr'
        visual_obj.wait_for_number_of_element(table_css, expected_number=34, time_out=wait_time)
        visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 05.01:')
        
        """
        Step 05: Click "Show data" again to return back to Chart and click Run menu to dismiss
        """
        menucontainer_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='show_report_css'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, menucontainer_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer3", toggle_button_click='yes')
        
        """
        Step 06: In the Filter prompt > Product,Category
        Check "Accessories", "Camcorder", "Computers", "Media Player"
        """
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=67, time_out=wait_time)
        visual_obj.select_single_item_from_show_prompt_table('Accessories', parent_prompt_css='#LOBJPrompt_33')
        visual_obj.select_single_item_from_show_prompt_table('Camcorder', parent_prompt_css='#LOBJPrompt_33')
        visual_obj.select_single_item_from_show_prompt_table('Computers', parent_prompt_css='#LOBJPrompt_33')
        visual_obj.select_single_item_from_show_prompt_table('Media Player', parent_prompt_css='#LOBJPrompt_33')
        
        """
        Step 07: In the Filter prompt > Sale,Year > Change the year (from 2013 to 2016)
        (IA-4664 - Retail Samples : Visualizations slider doesn't work properly)
        """
        parent_css='#MAINTABLE_wbody1 .legend text'
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=5, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=288, time_out=wait_time)
        visual_obj.move_slider_using_page_up_or_down_key(1, parent_css='#LOBJPrompt_44', drag_button='min', move_type='right', comparison_type='str')
        time.sleep(Global_variables.mediumwait)
        visual_obj.move_slider_using_page_up_or_down_key(2, parent_css='#LOBJPrompt_44', drag_button='max', move_type='left', comparison_type='str')
        
        """
        Step 08: In the Filter prompt > Revenue > Change the revenue (17.99 to 10816.88)
        """
        time.sleep(Global_variables.mediumwait)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=42, time_out=wait_time)
        visual_obj.move_slider_using_page_up_or_down_key(2, parent_css='#LOBJPrompt_55', drag_button='max', move_type='left', comparison_type='str')
        
        """
        Step 09: In the Map, click "Pan"
        """
        time.sleep(2*Global_variables.longwait)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=42, time_out=wait_time)
        visual_obj.select_pan_or_selection_in_map('#MAINTABLE_wbody2', btn_name='Pan')
        
        """
        Verify, it changes to "Selection"
        """
        time.sleep(Global_variables.mediumwait)
        Selection_css = "#MAINTABLE_wbody2 div[class*='SelectionButton UIButton toggleModeSelection']"
        utillobj.verify_element_visiblty(Selection_css, True, msg='Step 9.1: Verify, it changes to "Selection"')
        
        """
        Step 10: Lasso 35 points, click Filter chart
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=157, time_out=wait_time)
        time.sleep(Global_variables.longwait)
        source_css_locator="#MAINTABLE_wbody2 path[class^='riser!s0!g7!mregion!']"
        target_css_locator="#MAINTABLE_wbody2 path[class^='riser!s0!g2!mregion!']"
        source_element_location='top_left'
        target_element_location='bottom_right'
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso map  path riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso map path riser")
        visual_obj.create_lasso(source_element, target_element, source_xoffset=-100, source_yoffset=-50, target_xoffset=100, target_yoffset=50, source_element_location=source_element_location, target_element_location=target_element_location)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        """
        Step 11: Verify the Result
        """
        time.sleep(Global_variables.mediumwait)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=35, time_out=wait_time)
        
        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 4, 48, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c0!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        "---choropleth_map---"
        parent_css_with_tag_name="#MAINTABLE_wbody2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 35, msg="Step 04.9:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g12!mregion!']", 'elf_green', parent_css='#MAINTABLE_wbody2', msg="Step 04.10:Verify chart color")
        expected_legends=['Revenue', '0M', '1.9M', '3.7M', '5.6M', '7.4M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 04.11: Verify legends")
        
        expected_items_list=['All', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_show_prompt_table_list(expected_items_list, parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_item_checked_status_in_show_prompt_table('Accessories', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        visual_obj.verify_item_checked_status_in_show_prompt_table('Camcorder', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        visual_obj.verify_item_checked_status_in_show_prompt_table('Computers', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        visual_obj.verify_item_checked_status_in_show_prompt_table('Media Player', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_slider_min_max_value_in_run_window(2013, parent_css='#LOBJPrompt_44', drag_button='min', comparison_type='integer', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(2016, parent_css='#LOBJPrompt_44', drag_button='max', comparison_type='integer', msg = 'Step 04.5:')
        
        visual_obj.verify_slider_min_max_value_in_run_window(17.99, parent_css='#LOBJPrompt_55', drag_button='min', comparison_type='floating', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(9606.83, parent_css='#LOBJPrompt_55', drag_button='max', comparison_type='floating', msg = 'Step 04.5:')
        
        
        """
        Step 12: Go to Bar Chart > Lasso 60 points between the Sale year 2013 and 2014 > Click Filter chart
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=192, time_out=wait_time)
        source_css_locator="#MAINTABLE_wbody1 [class*='riser!s3!g3!mbar!r0!c0!']"
        target_css_locator="#MAINTABLE_wbody1 [class*='riser!s0!g5!mbar!r0!c1!']"
        source_element_location='top_middle'
        target_element_location='bottom_middle'
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso bar riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso bar riser")
        visual_obj.create_lasso(source_element, target_element, source_yoffset=-5, target_yoffset=5, source_element_location=source_element_location, target_element_location=target_element_location)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Filter Chart')
        
        """
        Step 13: Verify the Result
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=60, time_out=wait_time)
        expected_x_axis_labels=['4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K', '450K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 4, 15, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g3!mbar!r0!c0!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
        
        """
        Step 14: Hover on any chart riser in the Sale Year : 2013 > Click "Drill down to Product Subcategory"
        """
        time.sleep(Global_variables.mediumwait)
        riser_css='riser!s3!g7!mbar!r0!c0!'
        tooltip_menu='Drill down to->Product Subcategory'
        parent_css="#MAINTABLE_wbody1"
        visual_obj.select_tooltip(riser_css, tooltip_menu, parent_css=parent_css,move_to_tooltip=False)
        
        """
        Step 15: Verify the Result
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=4, time_out=wait_time)
        expected_x_axis_labels=['8']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '40K', '80K', '120K', '160K', '200K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 4, 1, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c0!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Subcategory', 'Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        """
        Step 16: Hover over Chart riser, Click " Drill Down to Sale Quarter"
        """
        riser_css='riser!s0!g0!mbar!r0!c0!'
        tooltip_menu='Drill down to->Sale Quarter'
        parent_css="#MAINTABLE_wbody1"
        visual_obj.select_tooltip(riser_css, tooltip_menu, parent_css=parent_css,move_to_tooltip=False)
        
        """
        Verify the Result
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=1, time_out=wait_time)
        expected_x_axis_labels=['8']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','3']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c0!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Subcategory', 'Blu Ray']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        """
        Step 17: Hover over Chart riser, Click "Drill down to Model"
        """
        riser_css='riser!s0!g0!mbar!r0!c0!'
        tooltip_menu='Drill down to->Model'
        parent_css="#MAINTABLE_wbody1"
        visual_obj.select_tooltip(riser_css, tooltip_menu, parent_css=parent_css,move_to_tooltip=False)
        
        """
        Step 18: Lasso 15 points, click Exclude from chart 
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=21, time_out=wait_time)
        source_css_locator="#MAINTABLE_wbody1 [class*='riser!s18!g0!mbar!r0!c0!']"
        target_css_locator="#MAINTABLE_wbody1 [class*='riser!s4!g0!mbar!r0!c0!']"
        source_element=utillobj.validate_and_get_webdriver_object(source_css_locator, "Source Lasso bar riser")
        target_element=utillobj.validate_and_get_webdriver_object(target_css_locator, "Target Lasso bar riser")
        visual_obj.create_lasso(source_element, target_element)
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_lasso_tooltip('Exclude from Chart')
        
        """
        Step 19: Verify the Result
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=6, time_out=wait_time)
        expected_x_axis_labels=['8']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Quarter','3']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 6, 1, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c0!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Model', 'JVC XV-BP1', 'JVC XV-BP10', 'JVC XV-BP11', 'Panasonic DMP-BD30', 'Sony BDP-S470', 'Sony BDP-S570']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        """
        Step 20: Click "Run menu icon" at the bottom and Click "Show data"
        """
        menu_option_button_name_show='show_report_css'
        menucontainer_css="#MAINTABLE_menuContainer1"
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, menucontainer_css)
         
        """
        Verify Show data output
        """
        file_name=TestCase_ID+'_Ds02.xlsx'
        table_css='#MAINTABLE_wbody4 .arPivot table > tbody > tr'
        visual_obj.wait_for_number_of_element(table_css, expected_number=34, time_out=wait_time)
        visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 05.01:')
        
        """
        Step 21: Click "Run menu icon" > Click "Restore Original"
        """
        menucontainer_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='reset'
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name, menucontainer_css, toggle_button_click='no')
        time.sleep(Global_variables.mediumwait)
        
        """
        Step 22: Click "Run menu icon" > Click "Restore Original"
        """
        menucontainer_css="#MAINTABLE_menuContainer2"
        menu_option_button_name='show_report_css'
        time.sleep(Global_variables.mediumwait)
        visual_obj.select_bottom_right_run_menu_options(parent_css="#MAINTABLE_menuContainer3", toggle_button_click='yes')
        
        
        """
        Step 23: Verify the original output is restored back
        """
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=504, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=34, time_out=wait_time)

        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_wbody1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017','2018']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_wbody1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_wbody1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 72, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c5!']", 'lochmara_1', parent_css='#MAINTABLE_wbody1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody1", msg="Step 04.8: Verify legends")
         
        "---choropleth_map---"
        parent_css_with_tag_name="#MAINTABLE_wbody2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 34, msg="Step 04.9:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g27!mregion!']", 'elf_green', parent_css='#MAINTABLE_wbody2', msg="Step 04.10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_wbody2", msg="Step 04.11: Verify legends")
        
        expected_items_list=['All', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_show_prompt_table_list(expected_items_list, parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_item_checked_status_in_show_prompt_table('All', parent_prompt_css='#LOBJPrompt_33', msg="Step 04.5:")
        
        visual_obj.verify_slider_min_max_value_in_run_window(2006, parent_css='#LOBJPrompt_44', drag_button='min', comparison_type='integer', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(2023, parent_css='#LOBJPrompt_44', drag_button='max', comparison_type='integer', msg = 'Step 04.5:')
        
        visual_obj.verify_slider_min_max_value_in_run_window(17.99, parent_css='#LOBJPrompt_55', drag_button='min', comparison_type='floating', msg = 'Step 04.5:')
        visual_obj.verify_slider_min_max_value_in_run_window(15999.4, parent_css='#LOBJPrompt_55', drag_button='max', comparison_type='floating', msg = 'Step 04.5:')
        
        
        
        """
        Step 25: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()