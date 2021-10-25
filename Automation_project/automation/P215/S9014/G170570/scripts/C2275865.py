'''
Created on Sep 13, 2018

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2275865&group_by=cases:section_id&group_id=170570&group_order=asc
TestCase Name : Verify to Run and Interaction with 'Sales by Region Dashboard - Pie chart' using Co-ordinated field
'''
import unittest
from common.wftools import chart, report
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart, active_report, visualization
from common.lib import utillity

class C2275865_TestClass(BaseTestCase):

    def test_C2275865(self):
        
        driver = self.driver
        Test_Case_Id="C2275865"
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        active_report_obj=active_report.Active_Report(driver)
        report_obj=report.Report(driver)
        utillobj=utillity.UtillityMethods(driver)
        visual_obj=visualization.Visualization(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        
        medium_wait= 70
        
        username= 'mrbasid'
        password= 'mrbaspass'
        fex_name='Sales_by_Region_Dashboard_Active'
        folder_name='Retail_Samples/Documents'
        
        "----------------------------------------------------------------------------CSS--------------------------------------------------------------------------------"
        
        total_riser_css= "svg g [class^='riser!s']"
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        
        ringpie_expected_label_list=['Revenue']
        ringpie_expected_legendlist=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        ringpie_risers="[class*='riser!s']"
        ringpie_chart_title='Sales by Product Category'
        
        dropdown_css="select[class='arDashboardMergeDropdown']"
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        active_chart_toolbar_list2=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        treemap_parent_css="MAINTABLE_3"
        ringpie_parent_css="MAINTABLE_0"
        no_of_risers="rect[class^='riser']"
        treemap_no_of_riser_css="#"+treemap_parent_css+" "+no_of_risers
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        treemap_chart_title='Gross Profit % By Brand'
        
        
        linechart_parent_css="MAINTABLE_1"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+linechart_parent_css+" "+linechart_no_of_risers
        linechart_x_axis_title=['Sale Month']
        linechart_expected_legend_list=['Sales (TY)', 'Sales (LY)']
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------
            Step 01: Sign to Webfocus using rsbas (basic user)
            http://machine:port/ibi_apps
            Step 02 : Run the Document using the below API URL
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/Retail_Samples/Documents&BIP_item=Sales_by_Region_Dashboard_Active.fex
        """ 
        chart_obj.run_fex_using_api_url(folder_name, fex_name, mrid=username, mrpass=password, run_chart_css=treemap_no_of_riser_css, no_of_element=31)
        utillobj.synchronize_with_number_of_element("#MAINTABLE_0 .legend text", 8, active_chart_obj.chart_long_timesleep)
        """
            Verify ringpie chart
        """
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 02:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 02:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 02:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 02:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 02:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 02:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 02:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 02:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 02:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
          
        """
            Verify treemap chart
        """
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 02:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 02:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 02:11: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 02:12: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 02:13: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 02:14: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 02:15: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
          
        """
            Verify linechart 
        """
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 02:16: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 02:17: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 02:18: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 02:19: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 02:20: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 02:21:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 02:22: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 02:23: ")
          
        """
            Active report verification at runtime
        """
          
        file_name=Test_Case_Id+"_Ds01.xlsx"
        table_css="#ITableData2"
#         report_obj.create_table_data_set(table_css, file_name)
        report_obj.verify_table_data_set(table_css, file_name, "Step 02:24: Verify active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 7, "light_gray", "Step 02:25: Verify visualization bar added in the active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 6, "red", "Step 02:26: Verify visualization bar added in the active report", expected_visual_bars=1)
        active_report_obj.verify_page_summary(2, '139of414records,Page1of10', 'Step 02:27: Verify active report page summary')
          
        """
            Verify dropdown selected value shown EMEA
        """
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='EMEA', default_selection_msg="Step 02:28: Verify the default selected value is EMEA")
         
        """
            Step 03 : Click the "Store Business Region" Dropdown and change to "North America"
        """
        utillobj.select_dropdown(dropdown_css, 'visible_text', 'North America')
         
        """ Verify dropdown selected value """
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='North America', default_selection_msg="Step 03:00: Verify the default selected value is North America")
        row_val_css="#ITableData2 tr:nth-child(5) td:nth-child(6)"
        row_val="-55,539.19%"
        chart_obj.wait_for_visible_text(row_val_css, row_val, medium_wait)
         
        """
            Verify ringpie chart
        """
        ringpie_expected_totallabel2=['33.9M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel2, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 03:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 03:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
         
        """
            Verify treemap chart
        """
        treemap_x_axis_label2=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        treemap_expected_legend_list2=['Gross Profit %', '20', '28.5', '37', '45.5', '54']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 03:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 03:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list2, parent_css="#"+treemap_parent_css, msg="Step 03:12: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label2, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 03:13: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 03:14: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 03:15: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 03:16: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
         
        """
            Verify linechart 
        """
        linechart_x_axis_label2=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label2=['0', '0.4M', '0.8M', '1.2M', '1.6M', '2M', '2.4M']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 03:17: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 03:18: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label2, parent_css="#"+linechart_parent_css, msg="Step 03:19: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label2, parent_css="#"+linechart_parent_css, msg="Step 03:20: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 03:21: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 03:22:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 03:23: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 03:24: ")
         
        """
            Active report verification at runtime
        """
        file_name=Test_Case_Id+"_Ds02.xlsx"
        table_css="#ITableData2"
#         report_obj.create_table_data_set(table_css, file_name)
        report_obj.verify_table_data_set(table_css, file_name, "Step 03:25: Verify active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 7, "light_gray", "Step 03:26: Verify visualization bar added in the active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 6, "red", "Step 03:27: Verify visualization bar added in the active report", expected_visual_bars=1)
        active_report_obj.verify_page_summary(2, '139of414records,Page1of10', 'Step 03:28: Verify active report page summary')
         
        """
            Step 04 : Click the "Store Business Region" Dropdown and change to "South America"
        """
        utillobj.select_dropdown(dropdown_css, 'visible_text', 'South America')
         
        """ Verify dropdown selected value """
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='South America', default_selection_msg="Step 04:00: Verify the default selected value is EMEA")
        
        row_val_css="#ITableData2 tr:nth-child(5) td:nth-child(6)"
        row_val=".00%"
        chart_obj.wait_for_visible_text(row_val_css, row_val, medium_wait)
         
        """
            Verify ringpie chart
        """
        ringpie_expected_totallabel3=['6.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 03:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 03:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 03:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 03:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 03:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel3, "Step 03:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 03:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 03:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 03:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
         
        """
            Verify treemap chart
        """
        treemap_x_axis_label3=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'JVC', 'Pioneer', 'Samsung', 'Sharp', 'Canon', 'Sanyo', 'P...', 'Toshiba', 'BOSE', 'Onkyo', 'Yamaha', 'Thoms...', 'Sennheiser']
        treemap_expected_legend_list3=['Gross Profit %', '20.1', '28.7', '37.2', '45.7', '54.2']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 03:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 03:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list3, parent_css="#"+treemap_parent_css, msg="Step 03:12: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label3, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 03:13: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 03:14: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 03:15: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 03:16: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
         
        """
            Verify linechart 
        """
        linechart_x_axis_label3=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label3=['0', '50K', '100K', '150K', '200K', '250K', '300K', '350K', '400K']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 03:17: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 03:18: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label3, parent_css="#"+linechart_parent_css, msg="Step 03:19: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label3, parent_css="#"+linechart_parent_css, msg="Step 03:20: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 03:21: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 03:22:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 03:23: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 03:24: ")
         
        """
            Active report verification at runtime
        """
        file_name=Test_Case_Id+"_Ds03.xlsx"
        table_css="#ITableData2"
#         report_obj.create_table_data_set(table_css, file_name)
        report_obj.verify_table_data_set(table_css, file_name, "Step 03:25: Verify active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 7, "light_gray", "Step 03:26: Verify visualization bar added in the active report")
        active_report_obj.verify_page_summary(2, '136of414records,Page1of10', 'Step 03:27: Verify active report page summary')
         
        """
            Step 5 : Click the "Store Business Region" Dropdown and change to "EMEA"
        """
        utillobj.select_dropdown(dropdown_css, 'visible_text', 'EMEA')
         
        """ Verify dropdown selected value """
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='EMEA', default_selection_msg="Step 03:00: Verify the default selected value is EMEA")
        
        css="#MAINTABLE_0 text[class^='totalLabel!']"
        chart_obj.wait_for_visible_text(css, "70.1M", medium_wait)
         
        """
            Verify the same output as displayed in step2
            Verify ringpie chart
        """
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 05:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 05:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 05:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 05:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 05:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 05:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 05:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 05:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
         
        """
            Verify treemap chart
        """
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 05:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 05:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 05:12: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 05:13: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 05:14: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 05:15: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 05:16: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
         
        """
            Verify linechart 
        """
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 05:17: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 05:18: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 05:19: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 05:20: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 05:21: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 05:22:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 05:23: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 05:24: ")
         
        """
            Step 06 : Go to the Pie chart "Sales by Product Category
            Step 07 : Hover over on Pie for" Product Category - Accessories" > Click Filter chart
        """
        riser_css="riser!s0!g0!mwedge!"
        menu_path="Filter Chart"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=ringpie_parent_css, move_to_tooltip=True)
         
        """
            Verify the result
        """
         
        ringpie_expected_totallabel4=['8.2M']
        ringpie_expected_legendlist4=['Product Category', 'Accessories']
        ringpie_riser_css1="[class='riser!s0!g0!mwedge!']"
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist4, parent_css="#"+ringpie_parent_css, msg="Step 07:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 07:02: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 07:03: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel4, "Step 07:04: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 1, "Step 07:05: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 07:06: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 07:07: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 08 : Click Remove filter icon on top
        """
        menu_path="Remove Filter"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=ringpie_parent_css, element_location='top_middle', yoffset=1, move_to_tooltip=True)
        
        """ Verify the filter is removed """
        ringpie_expected_totallabel1=['70.1M']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 08:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 08:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 08:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 08:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 08:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 08:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 08:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 08:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 08:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 09 : Hover over on Pie for" Product Category - Televisions" > Click "Exclude From Chart"
        """
        riser_css="riser!s5!g0!mwedge!"
        menu_path="Exclude from Chart"
        visual_obj.select_tooltip(riser_css, menu_path, parent_css=ringpie_parent_css, move_to_tooltip=True)
        
        """
            Step 10 : Verify the selected value is excluded
        """
        ringpie_expected_totallabel5=['62.8M']
        ringpie_expected_legendlist5=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist5, parent_css="#"+ringpie_parent_css, msg="Step 08:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 08:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 08:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 08:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 08:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel5, "Step 08:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 6, "Step 08:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 08:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 08:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
        
        """
            Step 11 : Click the first menu icon > "Restore original"
        """
        active_chart_obj.create_new_item("MAINTABLE_0", "Restore Original")
        css="#MAINTABLE_0 text[class^='totalLabel!']"
        chart_obj.wait_for_visible_text(css, "70.1M", medium_wait)
        
        """
            Step 12 : Verify the original chart is restored back
        """
        """
            Verify ringpie chart
        """
        ringpie_expected_totallabel1=['70.1M']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 12:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 12:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 12:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 12:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 12:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 12:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 12:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 12:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 12:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
         
        """
            Verify treemap chart
        """
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 12:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 12:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 12:12: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 12:13: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 12:14: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 12:15: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 12:16: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
         
        """
            Verify linechart 
        """
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 12:17: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 12:18: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 12:19: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 12:20: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 12:21: Verify line color")
        chart_obj.verify_number_of_chart_segment(linechart_parent_css, 26, "Step 12:22:")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 12:23: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 12:24: ")
         
        """
            Active report verification at runtime
        """
         
        file_name=Test_Case_Id+"_Ds01.xlsx"
        table_css="#ITableData2"
        report_obj.verify_table_data_set(table_css, file_name, "Step 12:25 Verify active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 7, "light_gray", "Step 12:26: Verify visualization bar added in the active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 6, "red", "Step 12:27: Verify visualization bar added in the active report", expected_visual_bars=1)
        active_report_obj.verify_page_summary(2, '139of414records,Page1of10', 'Step 12:28: Verify active report page summary')
         
        """
            Verify dropdown selected value shown EMEA
        """
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='EMEA', default_selection_msg="Step 12:29: Verify the default selected value is EMEA")
        
        """
            Step 13 : Logout from WebFOCUS BI Portal using the below API Link.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()