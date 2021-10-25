'''
Created on Sep 21, 2018

@author: Magesh

Testcase Name : Verify to restore successful with "Store And Product Profits over time"
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419861
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C6419861_TestClass(BaseTestCase):

    def test_C6419861(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419861"
        folder_name="Retail_Samples/Visualizations"
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        fex_name='Visualization_Store_And_Product_Profits_over_time'
        save_fex_name='Store_And_Product_Profits_over_time1'
        menu_option_button_name_show='show_report_css'
        menu_option_button_name_reset='reset'
        parentmenuContainer_css="#MAINTABLE_menuContainer1"
        file_name=TestCase_ID+'_Ds01.xlsx'
        prompt_item_name1='Accessories'
        prompt_item_name2='Camcorder'
        wait_time=400
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        preview_css1="#ar_TableChart_1 svg>g rect[class^='riser']"
        run_css1="#MAINTABLE_1 svg>g rect[class^='riser']"
        app_btn_css="#applicationButtonBox"
        table_css='#MAINTABLE_wbody3 .arPivot table > tbody > tr'
#         table_css1='#MAINTABLE_wbody4 .arPivot table > tbody > tr'
#         table_css2='#MAINTABLE_wbody5 .arPivot table > tbody > tr'
         
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Edit the Visualizations using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Visualizations/Visualization_Store_And_Product_Profits_over_time.fex&tool=idis
        """
        visual_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=244, time_out=wait_time)
        
        """
        Step 03: Verify the following Chart on canvas
        """
        "---Heatmap---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_z_axis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones']
        expected_x_axis_title_list=['Sale Month', 'Product Subcategory']
        parent_css_with_tag_name="#ar_TableChart_1 rect"
        expected_legends=['Quantity Sold', '0K', '7.6K', '15.3K', '23K', '30.5K']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_1', msg="Step 03:01:Verify x_axis label in preview")
        visual_obj.verify_y_axis_label(expected_z_axis_labels, parent_css='#ar_TableChart_1', xyz_axis_label_css="svg > g text[class^='zaxisOrdinal-labels']", msg="Step 03:02:Verify z-axis label in preview")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 03:03:Verify x_axis title at preview")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 244, msg="Step 03:04:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g11!mbar!']", 'elf_green', parent_css='#ar_TableChart_1', msg="Step 03:05:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 03:06: Verify legends")
        
        "---Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017']
        parent_css_with_tag_name="#ar_TableChart_2 path"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_2', msg="Step 03:07:Verify x_axis label in preview")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_2', msg="Step 03:08:Verify y-axis label in preview")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 03:09:Verify x_axis title at preview")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 03:10:Verify y_axis title at preview")
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#ar_TableChart_2', msg="Step 03:11:Verify column label in preview")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 35, msg="Step 03:12:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!r0!c4!']", 'lochmara_1', parent_css='#ar_TableChart_2', attribute='stroke', msg="Step 03:13:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 03:14: Verify legends")
        
        """
        Step 04: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
        
        """
        Verify the output is displayed in new window
        """
        visual_obj.wait_for_number_of_element(run_css1, expected_number=244, time_out=wait_time)
        
        "---Heatmap---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_z_axis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones']
        expected_x_axis_title_list=['Sale Month', 'Product Subcategory']
        parent_css_with_tag_name="#MAINTABLE_1 rect"
        expected_legends=['Quantity Sold', '0K', '7.6K', '15.3K', '23K', '30.5K']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_1', msg="Step 04:01:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_z_axis_labels, parent_css='#MAINTABLE_1', xyz_axis_label_css="svg > g text[class^='zaxisOrdinal-labels']", msg="Step 04:02:Verify z-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_1', msg="Step 04:03:Verify x_axis title at runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 244, msg="Step 04:04:Verify number of risers at runtime")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g11!mbar!']", 'elf_green', parent_css='#MAINTABLE_1', msg="Step 04:05:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_1", msg="Step 04:06: Verify legends")
        
        "---Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017']
        parent_css_with_tag_name="#MAINTABLE_2 path"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#MAINTABLE_2', msg="Step 04:07:Verify x_axis label in runtime")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#MAINTABLE_2', msg="Step 04:08:Verify y-axis label in runtime")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#MAINTABLE_2', msg="Step 04:09:Verify x_axis title at runtime")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#MAINTABLE_2', msg="Step 04:10:Verify y_axis title at runtime")
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#MAINTABLE_2', msg="Step 04:11:Verify column label in runtime")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 35, msg="Step 04:12:Verify number of line chart in runtime")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!r0!c4!']", 'lochmara_1', parent_css='#MAINTABLE_2', attribute='stroke', msg="Step 04:13:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#MAINTABLE_2", msg="Step 04:14: Verify legends")
        
        """
        Step 05: Click Run menu icon on Heatmap > Click Show Data
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_show, parentmenuContainer_css)
        
        """
        Verify Show data output
        """
        visual_obj.wait_for_number_of_element(table_css, expected_number=245, time_out=wait_time)
#         visual_obj.create_visualization_tabular_report(file_name, table_css)
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 05.1:')
        
        """
        Step 06: Check any two values under Product category
        """
        visual_obj.select_single_item_from_show_prompt_table(prompt_item_name1, parent_prompt_css='#LOBJPrompt_33')
        visual_obj.select_single_item_from_show_prompt_table(prompt_item_name2, parent_prompt_css='#LOBJPrompt_33')
        
        """
        Step 07: Click Restore Original
        """
        visual_obj.select_bottom_right_run_menu_options(menu_option_button_name_reset, parentmenuContainer_css,toggle_button_click='No')
        time.sleep(Global_variables.longwait)
        
        """
        Verify it should not display "No Data to Graph message"
        """
#         visual_obj.wait_for_number_of_element(table_css2, expected_number=245, time_out=wait_time)
#         visual_obj.verify_visualization_tabular_report(file_name, table_css2, msg='Step 07.1:')
        visual_obj.verify_visualization_tabular_report(file_name, table_css, msg='Step 07.1:')
        
        """
        Step 08: Close the output window
        """
        visual_obj.switch_to_previous_window()
        time.sleep(Global_variables.longwait)
        visual_obj.wait_for_number_of_element(app_btn_css, expected_number=1, time_out=wait_time)
        
        """
        Step 09: Click IA > Save > Select "SmokeTest" > Mycontent folder > Enter title as "Store and Product Profits Over Time1" > Click Save
        """
        visual_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
        Step 10: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
        
        """
        Step 11: Edit the saved Visualization using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Store_and_Product_Profits_Over_Time1.fex&tool=idis
        """
        visual_obj.edit_fex_using_api_url(edit_fex_folder_after_save, fex_name=save_fex_name, mrid='mrid', mrpass='mrpass')
        visual_obj.wait_for_number_of_element(preview_css1, expected_number=244, time_out=wait_time)
        
        """
        Verify Restore successful
        """
        "---Heatmap---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_z_axis_labels=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones']
        expected_x_axis_title_list=['Sale Month', 'Product Subcategory']
        parent_css_with_tag_name="#ar_TableChart_1 rect"
        expected_legends=['Quantity Sold', '0K', '7.6K', '15.3K', '23K', '30.5K']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_1', msg="Step 11:01:Verify x_axis label in preview")
        visual_obj.verify_y_axis_label(expected_z_axis_labels, parent_css='#ar_TableChart_1', xyz_axis_label_css="svg > g text[class^='zaxisOrdinal-labels']", msg="Step 11:02:Verify z-axis label in preview")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_1', msg="Step 11:03:Verify x_axis title at preview")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 244, msg="Step 11:04:Verify number of risers at preview")
        visual_obj.verify_chart_color_using_get_css_property("rect[class^='riser!s0!g11!mbar!']", 'elf_green', parent_css='#ar_TableChart_1', msg="Step 11:05:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_1", msg="Step 11:06: Verify legends")
        
        "---Line chart---"
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M']
        expected_x_axis_title_list=['Sale Month', 'Sale Month', 'Sale Month', 'Sale Month', 'Sale Month']
        expected_y_axis_title_list=['Gross Profit']
        expected_col_label_list=['Sale Year','2013','2014','2015','2016','2017']
        parent_css_with_tag_name="#ar_TableChart_2 path"
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        
        visual_obj.verify_x_axis_label(expected_x_axis_labels, parent_css='#ar_TableChart_2', msg="Step 11:07:Verify x_axis label in preview")
        visual_obj.verify_y_axis_label(expected_y_axis_labels, parent_css='#ar_TableChart_2', msg="Step 11:08:Verify y-axis label in preview")
        visual_obj.verify_x_axis_title(expected_x_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 11:09:Verify x_axis title at preview")
        visual_obj.verify_y_axis_title(expected_y_axis_title_list, parent_css='#ar_TableChart_2', msg="Step 11:10:Verify y_axis title at preview")
        visual_obj.verify_column_label(expected_col_label_list, parent_css='#ar_TableChart_2', msg="Step 11:11:Verify column label in preview")
        visual_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 35, msg="Step 11:12:Verify number of line chart in preview")
        visual_obj.verify_chart_color_using_get_css_property("path[class^='riser!s0!g0!mline!r0!c4!']", 'lochmara_1', parent_css='#ar_TableChart_2', attribute='stroke', msg="Step 11:13:Verify chart color")
        visual_obj.verify_legends(expected_legends, parent_css="#ar_TableChart_2", msg="Step 11:14: Verify legends")
        
        """
        Step 12: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()