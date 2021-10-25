'''
Created on Nov 20, 2018

@author: Magesh

TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7243122&group_by=cases:section_id&group_id=512444&group_order=asc
TestCase_Name : Verify to Run and Edit 'Insight - Profit versus profit margin'
'''
import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase

class C7243122_TestClass(BaseTestCase):

    def test_C7243122(self):
        
        chart_obj=chart.Chart(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C7243122"
        fex_name="Insight_-_Profit_versus_profit_margin"
        save_fex_name="Insight_-_Profit_versus_profit_margin1"
        folder_name="Retail_Samples/Charts"
        folder_name_to_edit_after_save="SmokeTest/~rsadv"
        medium_wait=10
        long_time=100
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="runbox_id"
        chart_parent_run_css_1="TableChart_1"
        RISER_CSS1="#runbox_id rect[class^='riser!']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02 : Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Insight_-_Profit_versus_profit_margin.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid="mrid", mrpass="mrpass", run_chart_css=RISER_CSS1, no_of_element=14)
          
        """ 
        Verify the following Insight Bar Chart
        """
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '25M', '50M', '75M', '100M']
        expected_y2_axis_labels=['0', '7', '14', '21', '28', '35']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 02.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 02.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 02.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 02.8: Verify chart color")
         
        """
        Step 03 : Hover over any chart riser, Verify the tooltip
        """
        css1='riser!s0!g0!ay1!mbar!'
        expected_tooltip_list=['Product Category:Accessories', 'Gross Profit:$39,854,440.53']
        chart_obj.verify_tooltip_in_run_window(css1, expected_tooltip_list, "Step 03: Verify tooltip", parent_css="#"+chart_parent_run_css)
         
        """
        Step 04 : Click + icon under Color Bucket shelf > Choose "Product Subcategory"
        """ 
        chart_obj.search_and_add_field_to_query_bucket_in_insight('Color', 'Product Subcategory') 
         
        """ 
        Verify field is added under Color bucket shelf and the following chart is displayed
        """
        chart_obj.wait_for_number_of_element(RISER_CSS1, 42, long_time)
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '15M', '30M', '45M', '60M']
        expected_y2_axis_labels=['0', '15', '30', '45', '60']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        legend_list=['Product Subcategory', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 04.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 04.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 04.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 04.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 04.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 04.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, msg="Step 04.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s4!g3!ay2!mbar!', 'brick_red', "Step 04.8: Verify chart color")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 04.9: Verify bar chart Legend List in run window')
         
        """
        Step 05 : Hover over Color bucket shelf , Click Delete icon (X)
        """
        chart_obj.delete_field_in_query_bucket_container_in_insight('Color', 'Product Subcategory')
        
        """
        Verify "Product Subcategory" field is removed
        """
        chart_obj.wait_for_number_of_element(RISER_CSS1, 14, long_time)
        chart_obj.verify_field_visible_in_query_bucket_container_in_insight('Color', 'Product Subcategory', msg='Step 05: Verify "Product Subcategory" field is removed', visible=False)
         
        """ 
        Step 06 : Click "Show Filter" icon under shelf
        Step 07 : In the search box type "Product" > Select "Product Category"
        """
        chart_obj.add_field_to_filter_container_in_insight("Product Category")
        
        """
        Step 08 : Verify the values are displayed > Select Accessories, Camcorder,Computers
        """
        item_list=['Accessories', 'Camcorder', 'Computers']
        expected_item_list = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.select_or_verify_filter_grid_values_in_insight("Product Category", item_list, verify=True, expected_item_list=expected_item_list, msg="Step 08: Verify the values are displayed in filter popup")
        
        """
        Step 09 : Click on blank area on the chart
        """
        chart_obj.click_on_blank_area_in_insight()
         
        """ 
        Verify the following filter is applied
        """
        chart_obj.wait_for_number_of_element(RISER_CSS1, 6, long_time)
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers']
        expected_y_axis_labels=['0', '15M', '30M', '45M', '60M']
        expected_y2_axis_labels=['0', '7', '14', '21', '28', '35']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 02.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 02.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 6, msg="Step 02.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 02.8: Verify chart color")
        
        """
        Step 10 : Click (X) - close on the filter shelf
        """
        chart_obj.delete_field_in_filter_panel_container_in_insight("Product Category")
        
        """
        Verify Filter condition is removed
        """
        chart_obj.wait_for_number_of_element(RISER_CSS1, 14, long_time)
        chart_obj.verify_field_visible_in_filter_panel_container_in_insight("Product Category", msg='Step 10: Verify Filter condition is removed', visible=False)
        
        """ 
        Step 11 : Click "Hide Filter" under shelf
        """
        chart_obj.select_header_option_item_in_insight(header_option_item='hide_filter')
        time.sleep(medium_wait)
         
        """ 
        Verify filter icon is not displayed
        """
        chart_obj.verify_add_filter_btn_visible_in_filter_panel_container_in_insight('Step 11: Verify filter icon is not displayed', visible=False)
         
        """ 
        Step 12 : Resize the browser window and verify it does not throws any error message
        """ 
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 14, long_time)
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 12:verify it does not throws any error message when resize the browser window")
         
        """ 
        Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        chart_obj.maximize_browser()
        chart_obj.api_logout()
        
        """ 
        Step 14 : Edit the Chart using "rsadv" user with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Insight_-_Profit_versus_profit_margin.fex&tool=Chart
        """ 
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        riser_css="#TableChart_1 rect[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 14, long_time)
        
        """ 
        Step 15 : Verify the following Query panel and Bar charts in Live Preview
        """
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Gross Profit', 1, msg="Step 15.a:")
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Gross_Margin', 2, msg="Step 15.b:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', 1, msg="Step 15.c:")
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '2,500', '5,000', '7,500', '10,000']
        expected_y2_axis_labels=['0', '9', '18', '27', '36', '45']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 15.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 15.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css_1, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 15.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 15.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 15.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css_1, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 15.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#TableChart_1 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 15.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css_1, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 15.8: Verify chart color")
        
        """ 
        Step 16 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 14, long_time)
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '25M', '50M', '75M', '100M']
        expected_y2_axis_labels=['0', '7', '14', '21', '28', '35']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 16.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 16.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 16.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 16.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 16.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 16.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 16.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 16.8: Verify chart color")
        
        """ 
        Step 17 : Click More Options > Select "Show Data Label"
        """
        chart_obj.select_or_verify_more_option_menu_item_in_insight(menu_item='Show Data Label')
        
        """ 
        Step 18 : Verify the chart with data labels
        """
        parent_css="#runbox_id [class^='dataLabels']"
        chart_obj.wait_for_number_of_element(parent_css, 14, long_time)
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '25M', '50M', '75M', '100M']
        expected_y2_axis_labels=['0', '7', '14', '21', '28', '35']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        expected_datalabel=['39.9M', '49.6M', '33.5M', '55.8M', '86.2M', '16.8M', '17.9M' ,'30.7', '32.1', '32.4', '22.7', '29.6', '21.5', '30.9']
        chart_obj.verify_data_labels(chart_parent_run_css, expected_datalabel, "Step 18: Verify the chart with data labels", custom_css="[class^='dataLabels']")
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 18.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 18.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 18.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 18.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 18.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 18.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 18.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 18.8: Verify chart color")
        chart_obj.switch_to_default_content()
        
        """
        Step 19 : Click IA > Save > Select "SmokeTest" folder > Enter title as "Insight - Profit versus profit margin1" > Click Save
        """
        chart_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
        Step 20 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 21 : Edit the saved Chart using the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/~rsadv/Insight_-_Profit_versus_profit_margin1.fex&tool=Chart
        """
        chart_obj.edit_fex_using_api_url(folder_name_to_edit_after_save, fex_name=save_fex_name, mrid="mrid", mrpass="mrpass")
        
        """ 
        Verify restore successful
        """
        riser_css="#TableChart_1 rect[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 14, long_time)
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Gross Profit', 1, msg="Step 21.a:")
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Gross_Margin', 2, msg="Step 21.b:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', 1, msg="Step 21.c:")
        expected_x_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_labels=['0', '2,500', '5,000', '7,500', '10,000']
        expected_y2_axis_labels=['0', '9', '18', '27', '36', '45']
        expected_x_axis_title_list=['Product Category']
        expected_y_axis_title_list=['Gross Profit']
        expected_y2_axis_title_list=['Gross_Margin']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 21.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 21.2: Verify y-axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y2_axis_labels, parent_css="#"+chart_parent_run_css_1, xyz_axis_label_css="svg > g text[class^='y2axis-labels']", msg="Step 21.3: Verify y2-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 21.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 21.5: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y2_axis_title_list, parent_css="#"+chart_parent_run_css_1, x_or_y_axis_title_css="text[class='y2axis-title']", msg="Step 21.6: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#TableChart_1 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 14, msg="Step 21.7: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css_1, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 21.8: Verify chart color")
        
        """
        Step 22 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()