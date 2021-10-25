'''
Created on Oct 17, 2018

@author: Magesh

Testcase Name : Verify to restore successful with "Sales by Region Dashboard"
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419826
'''

import unittest, time
from common.wftools import visualization, chart, active_chart, active_report, report
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.lib import utillity

class C6419826_TestClass(BaseTestCase):

    def test_C6419826(self):
        
        driver = self.driver
        visual_obj = visualization.Visualization(driver)
        chart_obj = chart.Chart(driver)
        active_chart_obj=active_chart.Active_Chart(driver)
        active_report_obj=active_report.Active_Report(driver)
        report_obj=report.Report(driver)
        utillobj = utillity.UtillityMethods(driver)
        
        "-------------------------------------------------------------------Test Case Variables--------------------------------------------------------------------------"
        TestCase_ID = "C6419826"
        username= 'mradvid'
        password= 'mradvpass'
        fex_name='Sales_by_Region_Dashboard_Active'
        save_fex_name='Sales_by_Region_Dashboard1'
        edit_fex_folder_after_save="SmokeTest/~rsadv"
        folder_name='Retail_Samples/Documents'
        wait_time=90
        
        """------------------------------------------------------------------------Test Steps---------------------------------------------------------------------------"""
        """
        Step 01: Sign to Webfocus using rsadv (advanced user)
        http://machine:port/ibi_apps
        Step 02: Edit the Document using the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/Retail_Samples/Documents/Sales_by_Region_Dashboard_Active.fex&tool=Document
        """
        chart_obj.edit_fex_using_api_url(folder_name, tool='document', fex_name=fex_name, mrid=username, mrpass=password)
        riser_css1="#TableChart_1 path[class^='riser']"
        visual_obj.wait_for_number_of_element(riser_css1, expected_number=7, time_out=wait_time)
         
        """
        Step 03: Click 'Ring pie' chart on canvas
        """ 
        ringpie_locator="#TableChart_1"
        ringpie_element=utillobj.validate_and_get_webdriver_object(ringpie_locator, "Ring pie chart")
        utillobj.click_on_screen(ringpie_element, 'middle', click_type=0)
        time.sleep(Global_variables.longwait)
         
        """
        Verify the Query pane,Filter Pane, Chart and Report on canvas
        """
        riser_css1="#qbFilterBox table>tbody>tr"
        visual_obj.wait_for_number_of_element(riser_css1, expected_number=2, time_out=wait_time)
        visual_obj.verify_field_in_filterbox('Sale,Year Equal to 2013 or 2014', msg='Step 03.1')
        visual_obj.verify_field_listed_under_querytree('Measure', 'Revenue', 1,  msg='Step 03.2')
        visual_obj.verify_field_listed_under_querytree('Color', 'Product,Category', 1,  msg='Step 03.3')
        visual_obj.verify_field_listed_under_querytree('Coordinated', 'Store,Business,Region', 1,  msg='Step 03.4')
         
        """
        Verify Preview
        """
        """
        Verify ringpie chart
        """
        ringpie_parent_css="TableChart_1"
        ringpie_expected_label_list=['Revenue']
        ringpie_expected_legendlist=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        ringpie_risers="[class*='riser!s']"
        ringpie_chart_title='Sales by Product Category'
        ringpie_expected_totallabel1=['40,526']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 03.5: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 03.6: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 03.7: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 03.8: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 03.9: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 03.10: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 03.11: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title(ringpie_chart_title, 'preview', msg="Step 03.13: Verify Ringpie chart title")
           
        """
        Verify treemap chart
        """
        treemap_parent_css="TableChart_4"
        treemap_riser_css="riser!sMajor Brand-_-Sharp!g0!mnode"
        treemap_expected_legend_list=['Gross Profit %', '15.3', '25', '34.8', '44.5', '54.3']
        treemap_chart_title='Gross Profit % By Brand'
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'Samsung', 'LG', 'Pioneer', 'JVC', 'Philips', 'Canon', 'Sharp', 'Sanyo', 'Onkyo', 'T', 'BOSE', 'Yamaha']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 20, "Step 03.13: Verify number of riser segments in preview",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 03.14: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 03.15: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 03.16: Verify Treemap labels at runtime")
        chart_obj.verify_chart_title(treemap_chart_title, 'preview', msg="Step 03.17: Verify treemap chart title", preview_index=4)
           
        """
        Verify linechart 
        """
        linechart_parent_css="TableChart_2"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+linechart_parent_css+" "+linechart_no_of_risers
        linechart_x_axis_title=['Sale Month']
        linechart_expected_legend_list=['Sales (TY)', 'Sales (LY)']
        line_chart_title='Sales by Month (TY vs LY)'
        linechart_x_axis_label1=['1']
        linechart_y_axis_label1=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 03.19: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 03.20: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 03.21: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 03.22: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 03.23: Verify line color")
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 03.25: ")
        chart_obj.verify_chart_title(line_chart_title, 'preview', msg="Step 03.26: Verify line chart title", preview_index=2)
           
        """
        Active report verification in Preview
        """
        file_name=TestCase_ID+"_Ds01.xlsx"
        table_css="TableChart_3"
#         report_obj.create_acrossreport_data_set_in_preview(table_css, 3, 8, 5, 8, file_name)
        report_obj.verify_across_report_data_set_in_preview(table_css, 3, 8, 5, 8, file_name, "Step 03.26: Verify active report in preview")
           
        """
        Step 04: Click Run
        """ 
        chart_obj.run_chart_from_toptoolbar()
        time.sleep(Global_variables.longwait)
        chart_obj.switch_to_frame()
        riser_css1="#ITableData2 > tbody > tr"
        visual_obj.wait_for_number_of_element(riser_css1, expected_number=17, time_out=wait_time)
         
        """
        Verify the Output
        """
        """
        Verify ringpie chart
        """
        ringpie_parent_css="MAINTABLE_0"
        ringpie_expected_label_list=['Revenue']
        ringpie_expected_legendlist=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        ringpie_risers="[class*='riser!s']"
        ringpie_chart_title='Sales by Product Category'
        ringpie_expected_totallabel1=['70.1M']
        active_chart_toolbar_list1=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 04:01: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 04:02: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 04:03: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 04:04: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 04:05: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 04:06: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 04:07: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title_in_run_window('run_chart_title', ringpie_chart_title, msg="Step 04:08: Verify Ringpie chart title")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 04:09: Verify active chart toolbar", parent_css="#"+ringpie_parent_css)
           
        """
        Verify treemap chart
        """
        treemap_parent_css="MAINTABLE_3"
        treemap_expected_legend_list=['Gross Profit %', '20', '28.5', '37', '45.6', '54.1']
        treemap_chart_title='Gross Profit % By Brand'
        total_riser_css= "svg g [class^='riser!s']"
        treemap_riser_css="riser!sSpecialty Brand-_-Harman Kardon!g0!mnode"
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'LG', 'Pioneer', 'JVC', 'Samsung', 'Canon', 'Sharp', 'Sanyo', 'Philips', 'T', 'BOSE', 'Onkyo', 'Yamaha']
        active_chart_toolbar_list2=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Avg']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 31, "Step 04:10: Verify number of riser segments in run window",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 04:11: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 04:12: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 04.13: Verify Treemap labels at runtime")
        chart_obj.verify_number_of_risers(total_riser_css, 31, 15, "Step 04.14: Verify number of risers")
        chart_obj.verify_chart_title_in_run_window('run_chart_title1', treemap_chart_title, msg="Step 04.15: ")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list2, msg="Step 04.16: Verify active chart toolbar", parent_css="#"+treemap_parent_css)
           
        """
        Verify linechart 
        """
        linechart_parent_css="MAINTABLE_1"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+linechart_parent_css+" "+linechart_no_of_risers
        linechart_x_axis_title=['Sale Month']
        linechart_expected_legend_list=['Sales (TY)', 'Sales (LY)']
        linechart_x_axis_label1=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        linechart_y_axis_label1=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M', '4.5M']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 04.17: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 04.18: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 04.19: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 04.20: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 04.21: Verify line color")
        active_chart_obj.verify_active_chart_toolbar(active_chart_toolbar_list1, msg="Step 04.23: ", parent_css="#"+linechart_parent_css)
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 04.24: ")
           
        """
        Active report verification at runtime
        """
        file_name=TestCase_ID+"_Ds02.xlsx"
        table_css="#ITableData2"
#         report_obj.create_table_data_set(table_css, file_name)
        report_obj.verify_table_data_set(table_css, file_name, "Step 04.25: Verify active report at runtime")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 7, "light_gray", "Step 04.26: Verify visualization bar added in the active report")
        active_report_obj.verify_visualize_bar_added_in_activereport(table_css, 6, "red", "Step 04.27: Verify visualization bar added in the active report", expected_visual_bars=1)
        active_report_obj.verify_page_summary(2, '139of414records,Page1of10', 'Step 04.28: Verify active report page summary')
           
        """
        Verify dropdown selected value shown EMEA
        """
        dropdown_css="select[class='arDashboardMergeDropdown']"
        utillobj.verify_dropdown_value(dropdown_css, expected_default_selected_value='EMEA', default_selection_msg="Step 04.29: Verify the default selected value is EMEA")
        chart_obj.switch_to_default_content()
         
        """
        Step 05: Click IA > Save > Select "SmokeTest" folder > Enter title as "Sales by Region Dashboard1" > Click Save
        """
        chart_obj.save_as_from_application_menu_item(save_fex_name)
         
        """
        Step 06: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
        
        """
        Step 07: Edit the saved Document using "rsadv" with the below API URL
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/SmokeTest/Sales_by_Region_Dashboard1.fex&tool=Document
        """
        chart_obj.edit_fex_using_api_url(edit_fex_folder_after_save, tool='document', fex_name=save_fex_name, mrid=username, mrpass=password)
        riser_css1="#TableChart_1 path[class^='riser']"
        visual_obj.wait_for_number_of_element(riser_css1, expected_number=7, time_out=wait_time)
        riser_css2="#TableChart_3 div[class^='x']"
        visual_obj.wait_for_number_of_element(riser_css2, expected_number=520, time_out=wait_time)
        
        """
        Verify it restored successfully without any error
        """
        """
        Verify ringpie chart
        """
        ringpie_parent_css="TableChart_1"
        ringpie_expected_label_list=['Revenue']
        ringpie_expected_legendlist=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        ringpie_riser_css1="[class='riser!s4!g0!mwedge!']"
        ringpie_riser_css2="[class='riser!s0!g0!mwedge!']"
        ringpie_riser_css3="[class='riser!s3!g0!mwedge!']"
        ringpie_risers="[class*='riser!s']"
        ringpie_chart_title='Sales by Product Category'
        ringpie_expected_totallabel1=['40,526']
        chart_obj.verify_legends_in_run_window(ringpie_expected_legendlist, parent_css="#"+ringpie_parent_css, msg="Step 07.1: Verify legends")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css1, 'brick_red', parent_css="#"+ringpie_parent_css, msg="Step 07.2: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css2, 'bar_blue', parent_css="#"+ringpie_parent_css, msg="Step 07.3: Verify color")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(ringpie_riser_css3, 'pale_yellow', parent_css="#"+ringpie_parent_css, msg="Step 07.4: Verify color")
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_label_list, "Step 07.5: ",custom_css="text[class*='pieLabel']") 
        chart_obj.verify_riser_pie_labels_and_legends(ringpie_parent_css, ringpie_expected_totallabel1, "Step 07.6: Verify pie total label values in preview",custom_css="text[class^='totalLabel!']",same_group=True) 
        chart_obj.verify_number_of_chart_segment(ringpie_parent_css, 7, "Step 07.7: Verify number of pie segments in preview", custom_css=ringpie_risers)
        chart_obj.verify_chart_title(ringpie_chart_title, 'preview', msg="Step 07.8: Verify Ringpie chart title")
        
        """
        Verify treemap chart
        """
        treemap_parent_css="TableChart_4"
        total_riser_css= "svg g [class^='riser!s']"
        treemap_riser_css="riser!sMajor Brand-_-Sharp!g0!mnode"
        treemap_expected_legend_list=['Gross Profit %', '15.3', '25', '34.8', '44.5', '54.3']
        treemap_chart_title='Gross Profit % By Brand'
        treemap_x_axis_label1=['Major Brand', 'Specialty Brand', 'Sony', 'Panasonic', 'Samsung', 'LG', 'Pioneer', 'JVC', 'Philips', 'Canon', 'Sharp', 'Sanyo', 'Onkyo', 'T', 'BOSE', 'Yamaha']
        chart_obj.verify_number_of_chart_segment(treemap_parent_css, 20, "Step 07.9: Verify number of riser segments in preview",custom_css="[class^='riser!s']")
        chart_obj.verify_chart_color(treemap_parent_css, treemap_riser_css, 'persian_red', "Step 07.10: Verify Treemap chart color")
        chart_obj.verify_legends_in_run_window(treemap_expected_legend_list, parent_css="#"+treemap_parent_css, msg="Step 07.11: Verify legends in tree map at runtime")
        chart_obj.verify_x_axis_label_in_run_window(treemap_x_axis_label1, parent_css="#"+treemap_parent_css, xyz_axis_label_css="text[text-anchor='middle']", xyz_axis_label_length=1,msg="Step 07.12: Verify Treemap labels at runtime")
        chart_obj.verify_chart_title(treemap_chart_title, 'preview', msg="Step 07.13: Verify treemap chart title", preview_index=4)
        
        """
        Verify linechart 
        """
        linechart_parent_css="TableChart_2"
        linechart_no_of_risers="path[class^='riser']"
        linechart_no_of_riser_css="#"+linechart_parent_css+" "+linechart_no_of_risers
        linechart_x_axis_title=['Sale Month']
        linechart_expected_legend_list=['Sales (TY)', 'Sales (LY)']
        line_chart_title='Sales by Month (TY vs LY)'
        linechart_x_axis_label1=['1']
        linechart_y_axis_label1=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        chart_obj.verify_x_axis_title_in_run_window(linechart_x_axis_title, parent_css="#"+linechart_parent_css, msg='Step 07.15: ')
        chart_obj.verify_legends_in_run_window(linechart_expected_legend_list, parent_css="#"+linechart_parent_css, msg='Step 07.16: ')
        chart_obj.verify_x_axis_label_in_run_window(linechart_x_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 07.17: ")
        chart_obj.verify_y_axis_label_in_run_window(linechart_y_axis_label1, parent_css="#"+linechart_parent_css, msg="Step 07.18: ")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mline!']", "bar_blue1", parent_css="#"+linechart_parent_css, attribute='stroke', msg="Step 07.19: Verify line color")
        chart_obj.verify_number_of_risers(linechart_no_of_riser_css, 1, 2, msg="Step: 07.21: ")
        chart_obj.verify_chart_title(line_chart_title, 'preview', msg="Step 03.26: Verify line chart title", preview_index=2)
          
        """
        Active report verification in Preview
        """
        file_name=TestCase_ID+"_Ds01.xlsx"
        table_css="TableChart_3"
        report_obj.verify_across_report_data_set_in_preview(table_css, 3, 8, 5, 8, file_name, "Step 07.22: Verify active report in preview")
        
        """
        Step 08: Logout from WebFOCUS BI Portal using the below API Link.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(Global_variables.mediumwait)

if __name__ == "__main__":
    unittest.main()