'''
Created on Sep 27, 2018

@author: Magesh

Testcase Name : Verify to restore successful with "Sales by Country and Product"
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419860
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419860_TestClass(BaseTestCase):

    def test_C6419860(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419860"
        folder_name="Retail_Samples/Visualizations"
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        fex_name='Sales_by_Country_and_Product'
        save_fex_name='Sales_by_Country_and_Product1'
        menu_option_button_name_show='show_report_css'
        menu_option_button_name_reset='reset'
        parentmenuContainer_css="#MAINTABLE_menuContainer2"
        file_name=TestCase_ID+'_Ds01.xlsx'
        slider_move=1
        wait_time=90
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        preview_css1="#ar_TableChart_1 svg>g rect[class^='riser']"
        preview_css2="#ar_TableChart_2 svg>g path[class^='riser']"
        run_css1="#MAINTABLE_1 svg>g rect[class^='riser']"
        run_css2="#MAINTABLE_2 svg>g path[class^='riser']"
        app_btn_css="#applicationButtonBox"
        table_css='#MAINTABLE_wbody3 .arPivot table > tbody > tr'
        table_css1='#MAINTABLE_wbody4 .arPivot table > tbody > tr'
        table_css2='#MAINTABLE_wbodyMain5 .arPivot table > tbody > tr'
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Edit the Visualizations using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Visualizations/Sales_by_Country_and_Product.fex&tool=idis
        """
        visual_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=504, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=34, time_out=wait_time)
        
        """
        Step 03: Verify the following Chart on canvas
        """
        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_1', msg="Step 03:01:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_1', msg="Step 03:02:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 03:03:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 03:04:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017','2018']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#ar_TableChart_1', msg="Step 03:05:Verify column label in preview")
        parent_css_with_tag_name="#ar_TableChart_1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 72, msg="Step 03:06:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c5!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 03:07:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 03:08: Verify legends")
        
        "---choropleth_map---"
        parent_css_with_tag_name="#ar_TableChart_2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 34, msg="Step 03:09:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g27!mregion!']", 'elf_green', parent_css='#ar_TableChart_2', msg="Step 03:10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 03:11: Verify legends")
        
        """
        Step 04: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
        time.sleep(2*Global_variables.longwait)
         
        """
        Verify the output is displayed in new window
        """
        visual_obj.wait_for_number_of_element(run_css1, expected_number=504, time_out=wait_time)
        visual_obj.wait_for_number_of_element(run_css2, expected_number=34, time_out=wait_time)
         
        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_1', msg="Step 04.1:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_1', msg="Step 04.2:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_1', msg="Step 04.3:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_1', msg="Step 04.4:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017','2018']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_1', msg="Step 04.5:Verify column label in preview")
        parent_css_with_tag_name="#MAINTABLE_1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 72, msg="Step 04.6:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c5!']", 'lochmara_1', parent_css='#MAINTABLE_1', msg="Step 04.7:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_1", msg="Step 04.8: Verify legends")
         
        "---choropleth_map---"
        parent_css_with_tag_name="#MAINTABLE_2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 34, msg="Step 04.9:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g27!mregion!']", 'elf_green', parent_css='#MAINTABLE_2', msg="Step 04.10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_2", msg="Step 034.11: Verify legends")
         
        """
        Step 05: Click Run menu icon on Map > Click Show Data
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, parentmenuContainer_css)
         
        """
        Verify Show data output
        """
        visual_obj.wait_for_number_of_element(table_css, expected_number=35, time_out=wait_time)
#         visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 05.01:')
         
        """
        Step 06: In Sale Year filter prompt > Drag year value from 2006 to 2013
        """
        visual_obj.move_slider_using_page_up_or_down_key(slider_move, parent_css='#LOBJPrompt_44', move_type='right', comparison_type='str')
        time.sleep(Global_variables.longwait) 
        """
        Step 07: Click Restore Original
        """
        visual_obj.wait_for_number_of_element('.arPivot table > tbody > tr', expected_number=35, time_out=wait_time)
        time.sleep(Global_variables.longwait)
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_reset, parentmenuContainer_css)
        time.sleep(Global_variables.longwait)
         
        """
        Verify it should not display "No Data to Graph message"
        """
        visual_obj.wait_for_number_of_element('.arPivot table > tbody > tr', expected_number=35, time_out=wait_time)
        visual_obj.verify_visualization_tabular_report(file_name, '.arPivot table > tbody > tr', msg='Step 07.1:')
         
        """
        Step 08: Close the output window
        """
        visual_obj.switch_to_previous_window()
        time.sleep(Global_variables.longwait)
        visual_obj.wait_for_number_of_element(app_btn_css, expected_number=1, time_out=wait_time)
         
        """
        Step 09: Click IA > Save > Select "SmokeTest" folder > Enter title as "Sales by Country and Product1" > Click Save
        """
        visual_obj.save_as_from_application_menu_item(save_fex_name)
         
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
         
        """
        Step 11: Edit the saved Visualization using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Sales_by_Country_and_Product1.fex&tool=idis
        """
        visual_obj.edit_fex_using_api_url(edit_fex_folder_after_save, fex_name=save_fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=504, time_out=wait_time)
        visual_obj.wait_for_number_of_element(preview_css2, expected_number=34, time_out=wait_time)
         
        """
        Verify Restore successful
        """
        "---Stacked_bar chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_1', msg="Step 11:01:Verify x_axis label in preview")
        expected_y_axis_labels=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_1', msg="Step 11:02:Verify y-axis label in preview")
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 11:03:Verify x_axis title at preview")
        expected_y_axis_title_list=['Revenue']
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 11:04:Verify y_axis title at preview")
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017','2018']
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#ar_TableChart_1', msg="Step 11:05:Verify column label in preview")
        parent_css_with_tag_name="#ar_TableChart_1 rect"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 72, msg="Step 11:06:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g0!mbar!r0!c5!']", 'lochmara_1', parent_css='#ar_TableChart_1', msg="Step 11:07:Verify chart color")
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 11:08: Verify legends")
         
        "---choropleth_map---"
        parent_css_with_tag_name="#ar_TableChart_2 path"
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 34, msg="Step 11:09:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g27!mregion!']", 'elf_green', parent_css='#ar_TableChart_2', msg="Step 11:10:Verify chart color")
        expected_legends=['Revenue', '1.2M', '8.5M', '15.7M', '23M', '30.2M']
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 11:11: Verify legends")
        
        """
        Step 12: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()