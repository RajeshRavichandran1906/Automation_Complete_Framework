'''
Created on Jan 4, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6667254&group_by=cases:section_id&group_order=asc&group_id=512308
Testcase Name : Verify that user can insert a chart in a document
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.wftools.active_chart import Active_Chart
from common.wftools.report import Report
from common.wftools.chart import Chart
from common.wftools.document import Document
from common.lib import utillity

import keyboard

class C6667254_TestClass(BaseTestCase):

    def test_C6667254(self):
        
        """ TESTCASE VARIABLES """
        
        Test_Case_ID = 'C6667254'
        
        """ CLASS OBJECTS """
        
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj=Report(self.driver)
        active_report_obj=Active_Report(self.driver)
        active_chart_obj=Active_Chart(self.driver)
        document_obj=Document(self.driver)
        chart_obj=Chart(self.driver)
        
        """ CSS """
        PREVIEW_PARENT_CSS1="TableChart_1"
        PREVIEW_PARENT_CSS2="TableChart_2"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        """
        Step 1:Launch IA Document with GGSales.Mas
        """
        document_obj.invoke_ia_tool_using_api(master='ibisamp/ggsales', mrid='mrid', mrpass='mrpass')

        """
        Step 2:Execute following URL to create Document
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116_S18157%2FG435171%2F
        """
         
        """
        Step 3:Change output format as Active report
        """
        chart_obj.change_output_format_type('active_report')
 
        """
        Step 4:Double click on fields Category, Product ID, Region and Unit Sales
        """
        chart_obj.double_click_on_datetree_item('Category', 1)
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS1+" div[class^='x']", 2, time_out=20)
        
        chart_obj.double_click_on_datetree_item('Product ID', 1)
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS1+" div[class^='x']", 5, time_out=20)
        
        chart_obj.double_click_on_datetree_item('Region', 1)
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS1+" div[class^='x']", 13, time_out=20)
        
        chart_obj.double_click_on_datetree_item('Unit Sales', 1)
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS1+" div[class^='x']", 21, time_out=20)
        
        coln_list = ['Category', 'Product ID', 'Region', 'Unit Sales']
        report_obj.verify_report_titles_on_preview(4, 4, PREVIEW_PARENT_CSS1, coln_list, "Step 04:01: Verify column titles")
#         report_obj.create_report_data_set_in_preview(PREVIEW_PARENT_CSS1, 7, 4, Test_Case_ID+'_Ds01.xlsx')
        report_obj.verify_report_data_set_in_preview(PREVIEW_PARENT_CSS1, 7, 4, Test_Case_ID+'_Ds01.xlsx', 'Step 04:02: Verify Preview report dataset')
        
        """
        Step 5:Click Insert tab > select Chart
        """
        chart_obj.select_ia_ribbon_item('Insert','Chart')
        chart_obj.wait_for_number_of_element("#"+PREVIEW_PARENT_CSS2, 1, time_out=30)
        
        document_obj.drag_drop_document_component("#"+PREVIEW_PARENT_CSS2, "#"+PREVIEW_PARENT_CSS1, 260, 0)
 
        """
        Step 6:Double click on fields Category and Budget Units
        """
        chart_obj.double_click_on_datetree_item('Category', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS2+" [class='xaxisOrdinal-title']", visble_element_text="Category", time_out=20)
        
        chart_obj.double_click_on_datetree_item('Budget Units', 1)
        chart_obj.wait_for_visible_text("#"+PREVIEW_PARENT_CSS2+" [class='yaxis-title']", visble_element_text="Budget Units", time_out=20)
        
        preview_expected_xaxis_label_list=['Coffee']
        preview_expected_yaxis_label_list=['0', '100K', '200K', '300K', '400K', '500K', '600K']
        preview_parent_css_with_tagname1="#"+PREVIEW_PARENT_CSS2+" rect"
        
        chart_obj.verify_x_axis_label_in_preview(preview_expected_xaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS2, msg="Step 6:01:")
        chart_obj.verify_y_axis_label_in_preview(preview_expected_yaxis_label_list, parent_css="#"+PREVIEW_PARENT_CSS2, msg="Step 6:02:")
        chart_obj.verify_number_of_risers(preview_parent_css_with_tagname1, 1, 1, msg="Step 6:04:")
        chart_obj.verify_chart_color_using_get_css_property_in_preview(RISER_CSS, "bar_blue", parent_css="#"+PREVIEW_PARENT_CSS2, msg="Step 6:05:")
        chart_obj.verify_number_of_chart_segment(PREVIEW_PARENT_CSS2, 1, "Step 6:06:Verify chart segments", custom_css="rect[class^='riser']")
        
        """
        Step 7:Click on Insert tab > select Text box.
        """
        chart_obj.select_ia_ribbon_item('Insert','Text')
        TEXT_CSS="#Prompt_1"
        chart_obj.wait_for_number_of_element(TEXT_CSS, 1, time_out=15)
        document_obj.drag_drop_document_component(TEXT_CSS,"#"+PREVIEW_PARENT_CSS1, 0,50, target_drop_point='bottom_middle')
        
        """
        Step 8:Right Click on Text box > Select Properties
        """
        document_obj.choose_right_click_menu_item_for_prompt(TEXT_CSS, 'Properties')
        
        """
        Step 9:Click Report drop down > select Chart1 and assign Budget Units for field value.
        """
        source_dict={'select_report':'Chart1','select_field':'Budget Units'}
        document_obj.customize_active_dashboard_properties(source=source_dict)
    
        """
        Step 10:Run the report
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        RUN_TABLE_CSS='ITableData0'
        
#         utillobj.create_data_set(RUN_TABLE_CSS, 'I0r', Test_Case_ID+'_Ds02.xlsx')
        utillobj.verify_data_set(RUN_TABLE_CSS, 'I0r', Test_Case_ID+'_Ds02.xlsx', 'Step 11:01: Verify data.')
        active_report_obj.verify_page_summary(0, '39of39records,Page1of1', 'Step 11:02: Verify the Report Heading')
        
        RUN_CHART_CSS="MAINTABLE_1"
        RUN_PARENT_CSS_WITH_TAGNAME="#" + RUN_CHART_CSS + " rect"
        ACTIVE_MENUBAR_CSS="#MAINTABLE_wmenu1"
        run_exp_chart_title="Budget Units BY Category"
        RISER_CSS="[class='riser!s0!g0!mbar!']"
        
        run_exp_xaxis_label_list=['Coffee', 'Food', 'Gifts']
        run_exp_yaxis_label_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_toolbar_menu_list=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        exp_yaxis_title_list=['Budget Units']
        exp_xaxis_title_list=['Category']
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 10:01:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 10:02:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 3, msg="Step 10:03:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 10:04:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 10:05:", parent_css="#MAINTABLE_wbody1_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_CHART_CSS, msg="Step 10:06:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 3, "Step 10:08: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 11:11:")
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+RUN_CHART_CSS,msg="Step 11:12:")
 
        """
        Step 11: Give input as "1385923" in text box and press enter key in keyboard.
        Verify the chart displayed on the preview on the report canvas.
        Bar chart should display with Measure (Sum) as Budget Units value and Category as X axis with out any error in the document output for all the three format verify that chart tool bar icon present in the chart output windows.
        """
        element=self.driver.find_element_by_css_selector('#PROMPT_1_cs input')
        exec("element.clear()")
        exec("element.send_keys('1385923')")
        keyboard.send('enter')
        time.sleep(5)
        
#         utillobj.create_data_set(RUN_TABLE_CSS, 'I0r', Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set(RUN_TABLE_CSS, 'I0r', Test_Case_ID+'_Ds03.xlsx', 'Step 11:01: Verify data.')
        active_report_obj.verify_page_summary(0, '39of39records,Page1of1', 'Step 11:02: Verify the Report Heading')
        
        run_exp_xaxis_label_list=['Coffee']
        run_exp_yaxis_label_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        
        chart_obj.verify_y_axis_label_in_run_window(run_exp_yaxis_label_list, parent_css="#"+RUN_CHART_CSS, msg="Step 11:03:")
        chart_obj.verify_x_axis_label_in_run_window(run_exp_xaxis_label_list, parent_css="#"+RUN_CHART_CSS, xyz_axis_label_length=1, msg="Step 11:04:")
        chart_obj.verify_number_of_risers(RUN_PARENT_CSS_WITH_TAGNAME, 1, 1, msg="Step 11:05:")
        active_chart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 11:06:", parent_css=ACTIVE_MENUBAR_CSS)
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step 11:07:", parent_css="#MAINTABLE_wbody1_ft")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window(RISER_CSS, 'bar_blue', parent_css="#"+RUN_CHART_CSS, msg="Step 11:08:")
        chart_obj.verify_number_of_chart_segment(RUN_CHART_CSS, 1, "Step 11:09: Verify chart segments", custom_css="rect[class^='riser']")
        chart_obj.verify_x_axis_title_in_run_window(exp_xaxis_title_list,parent_css="#"+RUN_CHART_CSS,msg="Step 11:11:")
        chart_obj.verify_y_axis_title_in_run_window(exp_yaxis_title_list, parent_css="#"+RUN_CHART_CSS,msg="Step 11:12:")
        
        """
        Step 12: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()