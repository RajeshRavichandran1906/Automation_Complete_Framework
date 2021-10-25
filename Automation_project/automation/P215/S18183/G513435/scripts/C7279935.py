'''
Created on Dec 18, 2018
@author: BM13368

TestCase_ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7279935&group_by=cases:section_id&group_id=513435&group_order=asc
TestCase_Name : Verify to Run and Edit 'Insight - Revenue on product categories'
'''
import unittest, time
from common.wftools import chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods

class C7279935_TestClass(BaseTestCase):

    def test_C7279935(self):
        
        chart_obj=chart.Chart(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        core_util_obj=CoreUtillityMethods(self.driver)
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C7279935"
        fex_name="Insight_-_Revenue_on_product_categories"
        save_fex_name="Insight_-_Revenue_on_product_categories1"
        folder_name="Retail_Samples/Charts"
        folder_name_to_edit_after_save="SmokeTest/~rsadv"
        medium_wait=20
        long_wait=35
        long_time=300
        username='mrid'
        password='mrpass'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        chart_parent_run_css="runbox_id"
        chart_parent_run_css_1="TableChart_1"
        pie_label_css="text[class^='totalLabel']"
        RISER_CSS1="#runbox_id circle[class^='riser!']"
        RISER_CSS2="#runbox_id path[class^='riser!']"
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        
        """
        Step 01 : Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02 : Run the Chart using the below API URL
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Charts&BIP_item=Insight_-_Revenue_on_product_categories.fex
        """
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=RISER_CSS1, no_of_element=168)
            
        """ 
        Verify the following "Insight Matrix Scatter chart"
        """
        expected_x_axis_labels=['1', '2', '3', '4']
        expected_y_axis_labels=['0', '12.5M', '25M', '37.5M']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 02.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 02.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css, msg="Step 02.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 02.6: Verify number of risers at runtime")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 02.7: Verify scatter chart Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s4!g0!ax1-y1!mmarker!r0!c0!']", "brick_red", parent_css="#"+chart_parent_run_css, attribute='stroke', msg="Step 02:8: Verify scatter color")
          
        """
        Step 03 : Hover over any point, Verify the tooltip
        """
        css1='riser!s4!g0!ax1-y1!mmarker!r0!c0!'
        expected_tooltip_list=['Store Country:United States', 'Sale Quarter:1', 'Revenue:$36,525,385.88', 'Product Category:Stereo Systems']
        chart_obj.verify_tooltip_in_run_window(css1, expected_tooltip_list, "Step 03: Verify tooltip", parent_css="#"+chart_parent_run_css)
          
        """ 
        Step 04 : Click Change Chart icon under bucket shelf > Select Pie Chart
        """
        chart_obj.change_chart_type_from_chart_picker_option_in_insight('Ring Pie')
           
        """ 
        Verify the following chart 
        """ 
        chart_obj.wait_for_number_of_element(RISER_CSS2, 42, long_time) 
        expected_pie_label_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        expected_total_label_list=['545.8M', '51.5M', '27.4M', '51.9M', '39.0M', '8.4M']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        parent_css_with_tag_name = "#runbox_id path"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 42, msg="Step 04.1: Verify number of risers at runtime")
        chart_obj.verify_chart_color(chart_parent_run_css, 'riser!s0!g0!mwedge!r0!c0!', 'bar_blue', "Step 04.2: Verify ring pie chart color")
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_pie_label_list, parent_css="#"+chart_parent_run_css, msg='Step 04.3: Verify ring pie labels')
        chart_obj.verify_pie_label_in_single_group_in_run_window(expected_total_label_list, parent_css="#"+chart_parent_run_css, label_css=pie_label_css, msg="Step 04.4: Verify ring pie total labels")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 04.5: Verify ring pie chart Legend List in run window')
           
        """ 
        Step 05 : Click Reset icon under bucket shelf 
        """ 
        chart_obj.select_header_option_item_in_insight(header_option_item='reset')
        time.sleep(medium_wait) 
           
        """ 
        Step 06 : Verify the chart is restored back to Scatter Chart 
        """ 
        chart_obj.wait_for_number_of_element(RISER_CSS1, 168, long_time)
        expected_x_axis_labels=['1', '2', '3', '4']
        expected_y_axis_labels=['0', '12.5M', '25M', '37.5M']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 06.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 06.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 06.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 06.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css, msg="Step 06.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 06.6: Verify number of risers at runtime")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 06.7: Verify scatter chart Legend List in run window') 
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s4!g0!ax1-y1!mmarker!r0!c0!']", "brick_red", parent_css="#"+chart_parent_run_css, attribute='stroke', msg="Step 06:8: Verify scatter color")
           
        """ 
        Step 07 : Resize the browser window and verify it does not throws any error message
        """ 
        chart_obj.set_browser_window_size()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 168, long_time)
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 07: verify it does not throws any error message after resize the browser window")
          
        """ 
        Step 08 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        chart_obj.maximize_browser()
        chart_obj.api_logout()
         
        """ 
        Step 09 : Edit the Chart using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Charts/Insight_-_Revenue_on_product_categories.fex&tool=Chart
        """ 
        chart_obj.edit_fex_using_api_url(folder_name, fex_name=fex_name, mrid="mrid", mrpass="mrpass")
        riser_css="#TableChart_1 circle[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 7, long_time)
         
        """ 
        Step 10 : Verify the following Query panel,Filter and Scatter chart in Live Preview
        """
        chart_obj.verify_field_listed_under_querytree('Rows', 'Store,Country', 1, msg="Step 10.a:")
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', 1, msg="Step 10.b:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Sale,Quarter', 1, msg="Step 10.c:")
        chart_obj.verify_field_in_filterbox('Store,Country Equal to United States or United Kingdom or Spain or ...', 1, msg="Step 10.d:")
        chart_obj.verify_field_in_filterbox('Product,Category Equal to Optional Multiselect Dynamic Parameter (Name: PRODUCT_CATEGORY, Field: PRODUCT_CATEGORY in retail_samples/WF_RETAIL_LITE) Sort Ascending', 2, msg="Step 10.e:")
        expected_x_axis_labels=['1']
        expected_y_axis_labels=['0', '3.8K', '7.5K', '11.3K']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 10.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 10.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 10.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 10.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css_1, msg="Step 10.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#TableChart_1 circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 10.6: Verify number of risers at runtime")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css_1, 5, 'Step 10.7: Verify scatter chart Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s4!g0!ax1-y1!mmarker!r0!c0!']", "brick_red", parent_css="#"+chart_parent_run_css_1, attribute='stroke', msg="Step 10:8: Verify scatter color") 
         
        """ 
        Step 11 : Click Run, Verify the output
        """
        chart_obj.run_chart_from_toptoolbar()
        parent_css="#resultArea [id^=ReportIframe-]"
        chart_obj.wait_for_number_of_element(parent_css, 1, medium_wait)
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(RISER_CSS1, 168, long_time)
        expected_x_axis_labels=['1', '2', '3', '4']
        expected_y_axis_labels=['0', '12.5M', '25M', '37.5M']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States', 'United Kingdom', 'Spain', 'Italy', 'Germany', 'France']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 11.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css, msg="Step 11.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 11.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css, msg="Step 11.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css, msg="Step 11.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#runbox_id circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 168, msg="Step 11.6: Verify number of risers at runtime")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css, 5, 'Step 11.7: Verify scatter chart Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s4!g0!ax1-y1!mmarker!r0!c0!']", "brick_red", parent_css="#"+chart_parent_run_css, attribute='stroke', msg="Step 11:8: Verify scatter color")
         
        """ 
        Step 12 : Click More Options > Select Export Data
        """
        chart_obj.select_header_option_item_in_insight('more_options')
        export_data_css="div[class*='exportData'] div[class*='menu-item-label']"
        utillobj.synchronize_with_number_of_element(export_data_css, 1, long_wait)
        export_data=utillobj.validate_and_get_webdriver_object(export_data_css, "Export Data menu option")
        export_data.click()
         
        """ 
        Step 13 : Open the excel and verify output
        Step 14 : Close the excel sheet
        """
        browser = utillobj.parseinitfile('browser')
        time.sleep(long_wait)
        utillobj.save_file_from_browser(TestCase_ID+'_actual_'+browser)        
        time.sleep(medium_wait)  
        utillobj.verify_excel_sheet_dynamic_values(TestCase_ID+'_base_'+browser+'.xlsx', TestCase_ID+'_actual_'+browser+'.xlsx', 'Sheet1', 'Step 13: Open the excel and verify output', starting_row=0, no_of_rows=10)
        time.sleep(long_wait)
        chart_obj.switch_to_default_content()
         
        """
        Step 15 : Click IA > Save > Select "SmokeTest" folder > Enter title as "Insight - Revenue on product categories1" > Click Save
        """
        chart_obj.save_as_from_application_menu_item(save_fex_name)
        save_button_elem=utillobj.validate_and_get_webdriver_object("[id='IbfsOpenFileDialog7_btnOK']", 'Save Button')
        core_util_obj.left_click(save_button_elem)
        """
        Step 16 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 17 : Edit the saved Chart using "rsadv" with the below API URL
        http://machine:port/{alias}/ia?item=IBFS:/WFC/Repository/SmokeTest/Insight_-_Revenue_on_product_categories1.fex
        """
        chart_obj.edit_fex_using_api_url(folder_name_to_edit_after_save, fex_name=save_fex_name, mrid="mrid", mrpass="mrpass")
        
        riser_css="#TableChart_1 circle[class*='riser']"
        chart_obj.wait_for_number_of_element(riser_css, 7, long_time)
        chart_obj.verify_field_listed_under_querytree('Rows', 'Store,Country', 1, msg="Step 17.a:")
        chart_obj.verify_field_listed_under_querytree('Vertical Axis', 'Revenue', 1, msg="Step 17.b:")
        chart_obj.verify_field_listed_under_querytree('Horizontal Axis', 'Sale,Quarter', 1, msg="Step 17.c:")
        expected_x_axis_labels=['1']
        expected_y_axis_labels=['0', '3.8K', '7.5K', '11.3K']
        expected_x_axis_title_list=['Sale Quarter']
        expected_y_axis_title_list=['Revenue']
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_label_list=['Store Country', 'United States']
        chart_obj.verify_x_axis_label_in_run_window(expected_x_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 17.1: Verify x_axis label in runtime")
        chart_obj.verify_y_axis_label_in_run_window(expected_y_axis_labels, parent_css="#"+chart_parent_run_css_1, msg="Step 17.2: Verify y-axis label in runtime")
        chart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 17.3: Verify y_axis title at runtime")
        chart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#"+chart_parent_run_css_1, msg="Step 17.4: Verify y_axis title at runtime")
        chart_obj.verify_rows_label_in_run_window(expected_row_label_list, parent_css="#"+chart_parent_run_css_1, msg="Step 17.5: Verify row header and labels at runtime")
        parent_css_with_tag_name = "#TableChart_1 circle"
        chart_obj.verify_number_of_risers(parent_css_with_tag_name, 1, 7, msg="Step 17.6: Verify number of risers at runtime")
        chart_obj.verify_legends_in_run_window(legend_list, "#"+chart_parent_run_css_1, 5, 'Step 17.7: Verify scatter chart Legend List in run window')
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s4!g0!ax1-y1!mmarker!r0!c0!']", "brick_red", parent_css="#"+chart_parent_run_css_1, attribute='stroke', msg="Step 17:8: Verify scatter color")
        
        """
        Step 18 : Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()