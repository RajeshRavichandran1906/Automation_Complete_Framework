'''
Created on 19-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251650
TestCase Name = Dashboard filtering on multiple components (ACT-434)
'''
import unittest, time
from common.lib import utillity
from common.pages import ia_resultarea, active_miscelaneous, visualization_resultarea, ia_run, active_chart_rollup
from common.lib.basetestcase import BaseTestCase


class C2251650_TestClass(BaseTestCase):

    def test_C2251650(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251650'
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        active_chartobj = active_chart_rollup.Active_Chart_Rollup(self.driver)
        
        
        def verify_dashboard(wait_css=None, wait_text=None, step_no=None, page_summary_title=None, bar_expected_number=None, xaxis_title=None, 
                             yaxis_title=None, x_lable=None, y_lable=None, bar_raiser_class=None, bar_expected_tooltip_list=None, bar_chart_title=None,
                             pie_expected_number=None, pie_raiser_class=None, pie_expected_tooltip_list=None, pie_datalable=None, pie_chart_title=None,
                             expected_legend_list=None, filter_menu_in_chart=None, pie_legend=None, bar_color=None, pie_color=None):
            utillobj.synchronize_with_visble_text(wait_css, wait_text, 65)
            '''verify check-box'''
            ia_runobj.verify_active_dashboard_prompts('checkbox', "#PROMPT_1_cs", ['[All]', 'Coffee', 'Food', 'Gifts'], "Step "+str(step_no)+".1: Verify Check Box value.", default_selected_check='[All]')
            
            '''verify report'''
            active_mis_obj.verify_page_summary(0, page_summary_title, "Step "+str(step_no)+".2: Verify page summary.")
            active_mis_obj.verify_column_heading('ITableData0', ['Category', 'Product', 'Unit Sales'], "Step "+str(step_no)+".2.1: Verify page summary.")
#             utillobj.create_table_data("table#ITableData0 tbody tr[id^='I0r']", test_case_id + "_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData0 tbody tr[id^='I0r']", test_case_id + "_Ds0"+str(step_no)+".xlsx")
            
            '''verify bar-chart'''
            vis_resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, bar_expected_number, "Step "+str(step_no)+".4: Verify number of riser in bar chart.")
            vis_resultobj.verify_xaxis_title('MAINTABLE_wbody1', xaxis_title, "Step "+str(step_no)+".5: Verify bar x-axis_title.")
            vis_resultobj.verify_yaxis_title('MAINTABLE_wbody1', yaxis_title, "Step "+str(step_no)+".6: Verify y-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', x_lable, y_lable, "Step "+str(step_no)+".7: Verify xy-axis_Labels.")
            active_mis_obj.verify_chart_title('MAINTABLE_wbody1', bar_chart_title, "Step "+str(step_no)+".8: Verify bar chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu1 ', filter_menu_in_chart, "Step "+str(step_no)+".9: Verify bar menu bar.", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step "+str(step_no)+".10: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', bar_raiser_class, bar_expected_tooltip_list, "Step "+str(step_no)+".11: Verify bar tooltip.")
            
            '''verify pie-chart'''
            ia_resultobj.verify_number_of_chart_segment("MAINTABLE_wbody2", pie_expected_number, "Step "+str(step_no)+".12: Verify number of riser in bar chart.")
            vis_resultobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody2', pie_legend, "Step "+str(step_no)+".13: Verify pie legends.")
            vis_resultobj.verify_data_labels('MAINTABLE_wbody2', pie_datalable, "Step "+str(step_no)+".14: Verify pie data lable.", custom_css=".chartPanel text[class*='mdataLabels']")
            active_mis_obj.verify_chart_title('MAINTABLE_wbody2', pie_chart_title, "Step "+str(step_no)+".15: Verify pie chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu2 ', filter_menu_in_chart, "Step "+str(step_no)+".16: Verify bar menu bar.", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step "+str(step_no)+".17: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody2', pie_raiser_class, pie_expected_tooltip_list, "Step "+str(step_no)+".18: Verify pie tooltip.")
            if expected_legend_list!=None:
                vis_resultobj.verify_legends(expected_legend_list, '#MAINTABLE_wbody2', legend_length=4, msg="Step "+str(step_no)+".19: Verify pie legends.")
            parent_elem = self.driver.find_element_by_id('IWindowBody0')
            utillobj.click_on_screen(parent_elem, 'top_middle', click_type=0)
            time.sleep(1)
            utillobj.verify_chart_color('MAINTABLE_wbody1', bar_raiser_class, bar_color, "Step "+str(step_no)+".20: Verify bar color.")
            utillobj.verify_chart_color('MAINTABLE_wbody2', pie_raiser_class, pie_color, "Step "+str(step_no)+".21: Verify pie color.")
            
            
        """ Step 1: Execute the attached repro - act434.fex
                    Expect to see the following Dashboard, with a Report, a Check Box a Bar Chart and PIE chart.
        """
        utillobj.active_run_fex_api_login('act434.fex','S10071_2','mrid','mrpass')
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 60)
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=1
        page_summary_title='10of10records,Page1of1'
        bar_expected_number=3
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Coffee', 'Food', 'Gifts']
        y_lable=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Coffee:1,376,266']
        pie_expected_number=3
        pie_legend=['Unit Sales']
        pie_datalable=['37%', '38%', '25%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s1!g0!mwedge"
        pie_expected_tooltip_list=['Food:1.4M (37.54%)']
        expected_legend_list=['Coffee', 'Food', 'Gifts']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_color='cerulean_blue'
        pie_color='gold_tips'
        verify_dashboard(wait_css, wait_text, step_no, page_summary_title, bar_expected_number, 
                         xaxis_title, yaxis_title, x_lable, y_lable, bar_raiser_class, 
                         bar_expected_tooltip_list, bar_chart_title, pie_expected_number, pie_raiser_class, 
                         pie_expected_tooltip_list, pie_datalable, pie_chart_title, expected_legend_list, filter_menu_in_chart, pie_legend=pie_legend,
                         bar_color=bar_color, pie_color=pie_color)
        
        """ Step 2: On the Bar Chart, left-click the first Bar for COFFEE.
                    Expect to see the options menu appear with Filter and Exclude options. Verify that no scroll bars appear around the Bar Chart.
        """
        """ Step 3: Click the Exclude button.
                    Expect to see the exclusion of Coffee from the Bar Chart, the PIE chart and the report at the top.
                    Verify that the filter icon is present at the top of the Bar Chart only.
        """
        time.sleep(1)
        coffee_bar_css=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 .chartPanel .risers [class='riser!s0!g0!mbar!']")
        utillobj.default_click(coffee_bar_css, click_option=0)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=3
        page_summary_title='7of10records,Page1of1'
        bar_expected_number=2
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Food', 'Gifts']
        y_lable=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Food:1,384,845']
        pie_expected_number=2
        pie_legend=['Unit Sales']
        pie_datalable=['60%', '40%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s1!g0!mwedge"
        pie_expected_tooltip_list=['Gifts:928K (40.12%)']
        expected_legend_list=['Food', 'Gifts']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        bar_color='cerulean_blue'
        pie_color='gold_tips'
        verify_dashboard(wait_css=wait_css, wait_text=wait_text, step_no=step_no, page_summary_title=page_summary_title, bar_expected_number=bar_expected_number, 
                         xaxis_title=xaxis_title, yaxis_title=yaxis_title, x_lable=x_lable, y_lable=y_lable, bar_raiser_class=bar_raiser_class, 
                         bar_expected_tooltip_list=bar_expected_tooltip_list, bar_chart_title=bar_chart_title, pie_expected_number=pie_expected_number,
                         pie_raiser_class=pie_raiser_class, pie_expected_tooltip_list=pie_expected_tooltip_list, pie_datalable=pie_datalable, 
                         pie_chart_title=pie_chart_title, expected_legend_list=expected_legend_list, filter_menu_in_chart=filter_menu_in_chart, 
                         pie_legend=pie_legend, bar_color=bar_color, pie_color=pie_color)
        
        """ Step 4: On the PIE Chart, left-click the slice for Gifts.
                    Expect to see the options menu appear with Filter and Exclude options. Verify that no scroll bars appear around the Bar Chart.
        """
        """ Step 5: Click the Exclude button.
                    Expect to see the exclusion of Gifts from the Bar Chart, the PIE chart and the report at the top.
                    Verify that filter icons now appear at the tops of both the Bar Chart and PIE chart.
        """
        pie_chart_css = self.driver.find_element_by_css_selector("#MAINTABLE_wbody2 .chartPanel [class='riser!s1!g0!mwedge!']")
        utillobj.default_click(pie_chart_css, click_option=0)
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=5
        page_summary_title='3of10records,Page1of1'
        bar_expected_number=1
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Food']
        y_lable=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Food:1,384,845']
        pie_expected_number=1
        pie_legend=['Unit Sales']
        pie_datalable=['100%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Food:1.4M (100.00%)']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        bar_color='cerulean_blue'
        pie_color='cerulean_blue'
        verify_dashboard(wait_css=wait_css, wait_text=wait_text, step_no=step_no, page_summary_title=page_summary_title, bar_expected_number=bar_expected_number, 
                         xaxis_title=xaxis_title, yaxis_title=yaxis_title, x_lable=x_lable, y_lable=y_lable, bar_raiser_class=bar_raiser_class, 
                         bar_expected_tooltip_list=bar_expected_tooltip_list, bar_chart_title=bar_chart_title, pie_expected_number=pie_expected_number,
                         pie_raiser_class=pie_raiser_class, pie_expected_tooltip_list=pie_expected_tooltip_list, pie_datalable=pie_datalable, 
                         pie_chart_title=pie_chart_title, filter_menu_in_chart=filter_menu_in_chart, 
                         pie_legend=pie_legend, bar_color=bar_color, pie_color=pie_color)
        
        """ Step 6: Click the Filter icon on top of the Bar Chart.
                    Expect to see Coffee data return to the Bar Chart, PIE Chart and report.
                    Verify that no scroll bars appear on the Bar Chart.
        """
        active_chartobj.click_pivot_menu_bar_items('MAINTABLE_wmenu1', 8)
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=6
        page_summary_title='10of10records,Page1of1'
        bar_expected_number=3
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Coffee', 'Food', 'Gifts']
        y_lable=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Coffee:1,376,266']
        pie_expected_number=3
        pie_legend=['Unit Sales']
        pie_datalable=['37%', '38%', '25%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s1!g0!mwedge"
        pie_expected_tooltip_list=['Food:1.4M (37.54%)']
        expected_legend_list=['Coffee', 'Food', 'Gifts']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_color='cerulean_blue'
        pie_color='gold_tips'
        verify_dashboard(wait_css=wait_css, wait_text=wait_text, step_no=step_no, page_summary_title=page_summary_title, bar_expected_number=bar_expected_number, 
                         xaxis_title=xaxis_title, yaxis_title=yaxis_title, x_lable=x_lable, y_lable=y_lable, bar_raiser_class=bar_raiser_class, 
                         bar_expected_tooltip_list=bar_expected_tooltip_list, bar_chart_title=bar_chart_title, pie_expected_number=pie_expected_number,
                         pie_raiser_class=pie_raiser_class, pie_expected_tooltip_list=pie_expected_tooltip_list, pie_datalable=pie_datalable, 
                         pie_chart_title=pie_chart_title, expected_legend_list=expected_legend_list, filter_menu_in_chart=filter_menu_in_chart, 
                         pie_legend=pie_legend, bar_color=bar_color, pie_color=pie_color)
        
        """ Step 7: On the Bar Chart, left-click and draw a box that touches the first two bars.
                    Expect to see the bars for Coffee and Food highlighted and the menu specify that 2 points are selected.
                    Verify that no scroll bars appear on the Bar Chart.
        """
        """ Step 8: Click the Exclude button.
                    Expect to see data for Coffee and Food removed from the Bar Chart, the PIE chart and the report.
                    Verify that no scroll bars appear on the Bar Chart.
        """
        vis_resultobj.create_lasso('MAINTABLE_wbody1', 'rect', 'riser!s0!g0!mbar', target_tag='rect', target_riser='riser!s0!g1!mbar')
        vis_resultobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=8
        page_summary_title='4of10records,Page1of1'
        bar_expected_number=1
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Gifts']
        y_lable=['0', '0.2M', '0.4M', '0.6M', '0.8M', '1M', '1.2M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Gifts:927,880']
        pie_expected_number=1
        pie_legend=['Unit Sales']
        pie_datalable=['100%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s0!g0!mwedge"
        pie_expected_tooltip_list=['Gifts:928K (100.00%)']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Remove Filter']
        bar_color='cerulean_blue'
        pie_color='cerulean_blue'
        verify_dashboard(wait_css=wait_css, wait_text=wait_text, step_no=step_no, page_summary_title=page_summary_title, bar_expected_number=bar_expected_number, 
                         xaxis_title=xaxis_title, yaxis_title=yaxis_title, x_lable=x_lable, y_lable=y_lable, bar_raiser_class=bar_raiser_class, 
                         bar_expected_tooltip_list=bar_expected_tooltip_list, bar_chart_title=bar_chart_title, pie_expected_number=pie_expected_number,
                         pie_raiser_class=pie_raiser_class, pie_expected_tooltip_list=pie_expected_tooltip_list, pie_datalable=pie_datalable, 
                         pie_chart_title=pie_chart_title, filter_menu_in_chart=filter_menu_in_chart, 
                         pie_legend=pie_legend, bar_color=bar_color, pie_color=pie_color)
        
        """ Step 9: Click the Filter button at the top of the Bar Chart.
                    Expect to see all data return to Bar Chart, PIE Chart and Report.
                    Verify that no scroll bars appear on the Bar Chart or anywhere on the Dashboard.
        """
        active_chartobj.click_pivot_menu_bar_items('MAINTABLE_wmenu1', 8)
        wait_css="#PROMPT_1_cs table tr:nth-child(2) label[for]"
        wait_text='Coffee'
        step_no=9
        page_summary_title='10of10records,Page1of1'
        bar_expected_number=3
        xaxis_title='Category'
        yaxis_title='Unit Sales'
        x_lable=['Coffee', 'Food', 'Gifts']
        y_lable=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        bar_chart_title='Unit Sales by Category'
        bar_raiser_class="riser!s0!g0!mbar"
        bar_expected_tooltip_list=['Unit Sales, Coffee:1,376,266']
        pie_expected_number=3
        pie_legend=['Unit Sales']
        pie_datalable=['37%', '38%', '25%']
        pie_chart_title='Unit Sales by Category'
        pie_raiser_class="riser!s1!g0!mwedge"
        pie_expected_tooltip_list=['Food:1.4M (37.54%)']
        expected_legend_list=['Coffee', 'Food', 'Gifts']
        filter_menu_in_chart=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_color='cerulean_blue'
        pie_color='gold_tips'
        verify_dashboard(wait_css=wait_css, wait_text=wait_text, step_no=step_no, page_summary_title=page_summary_title, bar_expected_number=bar_expected_number, 
                         xaxis_title=xaxis_title, yaxis_title=yaxis_title, x_lable=x_lable, y_lable=y_lable, bar_raiser_class=bar_raiser_class, 
                         bar_expected_tooltip_list=bar_expected_tooltip_list, bar_chart_title=bar_chart_title, pie_expected_number=pie_expected_number,
                         pie_raiser_class=pie_raiser_class, pie_expected_tooltip_list=pie_expected_tooltip_list, pie_datalable=pie_datalable, 
                         pie_chart_title=pie_chart_title, expected_legend_list=expected_legend_list, filter_menu_in_chart=filter_menu_in_chart, 
                         pie_legend=pie_legend, bar_color=bar_color, pie_color=pie_color)
        
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()