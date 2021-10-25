'''
Created on Nov 21, 2018

TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7243123&group_by=cases:section_id&group_id=512444&group_order=asc
TestCase_Name : Verify to Run and Edit 'Insight - Revenue on product categories'
'''
import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity

class C7243123_TestClass(BaseTestCase):

    def test_C7243123(self):
        
        chart_obj=chart.Chart(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C7243123"
        fex_name="Insight_-_Revenue_on_product_categories"
        save_fex_name="Insight_-_Revenue_on_product_categories1"
        folder_name="Retail_Samples/Charts"
        folder_name_to_edit_after_save="SmokeTest/~rsadv"
        medium_wait=10
        long_wait=15
        long_time=100
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="runbox_id"
        chart_parent_run_css_1="TableChart_1"
        RISER_CSS1="#runbox_id circle[class^='riser!']"
        RISER_CSS2="#runbox_id path[class^='riser!']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02 : Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Insight_-_Revenue_on_product_categories.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid="mrid", mrpass="mrpass", run_chart_css=RISER_CSS1, no_of_element=168)
          
        """ 
        Step 03 : Verify the following "Insight Matrix Scatter chart"
        """
        expected_x_axis_labels=['1', '2', '3', '4']
        expected_y_axis_labels=['0', '12.5M', '25M', '37.5M']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css, msg="Step 03.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 03.6: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s4!g0!ax1-y1!mmarker!r0!c0!', 'brick_red', "Step 03.7: Verify scatter chart color", attribute_type='stroke', attribute='yes')
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 03.8: Verify scatter chart Legend List in run window')
        
        """
        Step 04 : Hover over any point, Verify the tooltip
        """
        css1='riser!s4!g0!ax1-y1!mmarker!r0!c0!'
        expected_tooltip_list=['Product Category:Accessories', 'Gross Profit:$39,854,440.53']
        chart_obj.verify_tooltip_in_run_window(css1, expected_tooltip_list, "Step 04: Verify tooltip", parent_css="#"+chart_parent_run_css)
        
        """ 
        Step 05 : Click Change Chart icon under bucket shelf > Select Pie Chart
        """
        chart_obj.change_chart_type_from_chart_picker_option_in_insight('Ring Pie')
         
        """ 
        Step 06 : Verify the following chart 
        """ 
        chart_obj.wait_for_number_of_element(RISER_CSS2, 42, long_time) 
        

         
        """ 
        Step 07 : Click Reset icon under bucket shelf 
        """ 
        chart_obj.select_header_option_item_in_insight(header_option_item='reset')
        time.sleep(medium_wait) 
         
        """ 
        Step 08 : Verify the chart is restored back to Scatter Chart 
        """ 
        chart_obj.wait_for_number_of_element(RISER_CSS1, 168, long_time)
        expected_x_axis_labels=['1', '2', '3', '4']
        expected_y_axis_labels=['0', '12.5M', '25M', '37.5M']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 03.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 03.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css, msg="Step 03.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 03.6: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s4!g0!ax1-y1!mmarker!r0!c0!', 'brick_red', "Step 03.7: Verify scatter chart color", attribute_type='stroke', attribute='yes')
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 03.8: Verify scatter chart Legend List in run window') 
         
        """ 
        Step 09 : Resize the browser window and verify it does not throws any error message
        """ 
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 168, long_time)
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 13:Verify number of risers at runtime")
        
        """ 
        Step 10 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        chart_obj.maximize_browser()
        chart_obj.api_logout()
        
        """ 
        Step 11 : Edit the Chart using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Insight_-_Revenue_on_product_categories.fex&tool=Chart
        """ 
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        riser_css="#TableChart_1 rect[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 1, long_time)
        
        """ 
        Step 12 : Verify the following Query panel,Filter and Scatter chart in Live Preview
        """
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', 1, msg="Step 16.a:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Sale,Month', 1, msg="Step 16.b:")
        chart_obj.verify_field_listed_under_querytree('Color BY', 'Product,Category', 1, msg="Step 16.c:")
        expected_x_axis_labels=['1']
        expected_y_axis_labels=['0', '20', '40', '60', '80', '100', '120']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        legend_list=['Product Category', 'Stereo Systems']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 16.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 16.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 16.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 16.4: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#TableChart_1 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 16.5: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css_1, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 16.6: Verify chart color")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css_1, 5, 'Step 16.7: Verify bar chart Legend List in run window')
         
        """ 
        Step 13 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 84, long_time)
        vertical_css="div[class^='query-box'] div[class^='add-bucket'][aria-label*='Vertical Axis'] div[class$='plus']"
        utillobj.verify_object_visible(vertical_css, True, "Step 17.1: Verify it restored back to Stacked bar chart")
        expected_x_axis_labels=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        expected_y_axis_labels=['0', '5M', '10M', '15M', '20M', '25M', '30M']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 17.2: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 17.3: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 17.4: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 17.5: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#runbox_id rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 7, 12, msg="Step 17.6:Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 17.7: Verify chart color")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 17.8: Verify bar chart Legend List in run window')
        
        """ 
        Step 14 : Click More Options > Select Export Data
        """
        chart_obj.select_or_verify_more_option_menu_item_in_insight(menu_item='Export Data')
        
        
        """ 
        Step 15 : Open the excel and verify output
        Step 16 : Close the excel sheet
        """
        browser = utillobj.parseinitfile('browser')
        time.sleep(long_wait)
        utillobj.save_file_from_browser(TestCase_ID+'_actual_'+browser)        
        time.sleep(medium_wait)  
        utillobj.verify_excel_sheet_dynamic_values(TestCase_ID+'_base_'+browser+'.xlsx', TestCase_ID+'_actual_'+browser+'.xlsx', 'Sheet1', 'Step 15: Open the excel and verify output', starting_row=0, no_of_rows=10)
        if browser != 'IE':
            utillobj.switch_to_main_window()           
        time.sleep(long_wait)
        chart_obj.switch_to_default_content()
        
        """
        Step 17 : Click IA > Save > Select "SmokeTest" folder > Enter title as "Insight - Revenue on product categories1" > Click Save
        """
        chart_obj.save_as_from_application_menu_item(save_fex_name)
        
        """
        Step 18 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 19 : Edit the saved Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Insight_-_Revenue_on_product_categories1.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name_to_edit_after_save, fex_name=save_fex_name, mrid="mrid", mrpass="mrpass")
        
        riser_css="#TableChart_1 rect[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 1, long_time)
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', 1, msg="Step 22.a:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Sale,Month', 1, msg="Step 22.b:")
        chart_obj.verify_field_listed_under_querytree('Color BY', 'Product,Category', 1, msg="Step 22.c:")
        expected_x_axis_labels=['1']
        expected_y_axis_labels=['0', '20', '40', '60', '80', '100', '120']
        expected_x_axis_title_list=['Sale Month']
        expected_y_axis_title_list=['Revenue']
        legend_list=['Product Category', 'Stereo Systems']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 22.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 22.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 22.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 22.4: Verify y_axis title at runtime")
        parent_css_with_tag_name = "#TableChart_1 rect"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 1, msg="Step 22.5: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css_1, 'riser!s0!g0!ay1!mbar!', 'bar_blue', "Step 22.6: Verify chart color")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css_1, 5, 'Step 22.7: Verify bar chart Legend List in run window')
        
        """
        Step 20 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()