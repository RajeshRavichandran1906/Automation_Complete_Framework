'''
Created on 24-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2278273
TestCase Name = AHTML: CenturySales Multi-page Active Document functionality test.
'''
import unittest, time, re
from common.lib import utillity
from common.pages import ia_resultarea, active_miscelaneous, visualization_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase

class C2278273_TestClass(BaseTestCase):

    def test_C2278273(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2278273'
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        def verify_revenue_report_page(wait_css=None, wait_text=None, step_no=None, pie_expected_number=None, pie_label=None, pie_legend=None, pie_raiser_class=None,
                             pie_color=None, pie_chart_title=None, pie_filter_menu=None, pie_tooltip=None, line_expected_number=None, line_xaxis_title=None,
                             line_yaxis_title=None, line_x_lable=None, line_y_lable=None, line_raiser_class=None, line_color=None, line_chart_title=None,
                             line_filter_menu=None, line_tooltip=None, bar_expected_number=None, bar_xaxis_title=None, bar_yaxis_title=None, bar_x_lable=None, 
                             bar_y_lable=None, bar_raiser_class=None, bar_color=None, bar_chart_title=None, bar_filter_menu=None, bar_tooltip=None, 
                             century_electronics_page_summary_title=None, regional_product_sales_report_page_summary_title=None, region_drop_down_selected=None):
            
            utillobj.synchronize_with_visble_text(wait_css, wait_text, vis_resultobj.home_page_long_timesleep)
            
            '''verify  Revenue Report page title'''
            revenue_report_text = self.driver.find_element_by_css_selector("[id^='LOBJText_'][style*='block'] [id^='LOBJText'][id$='TEXT']").text.strip().replace('\n',' ')  
            utillobj.asequal('Century Electronics Regional Revenue Report', revenue_report_text, "Step "+str(step_no)+".1: Verify Revenue Report page title.")
            
            '''verify pie-chart'''
            ia_resultobj.verify_number_of_chart_segment("MAINTABLE_wbody0", pie_expected_number, "Step "+str(step_no)+".2: Verify number of riser in bar chart.")
            vis_resultobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', pie_label, "Step "+str(step_no)+".3: Verify pie label.", same_group=True)
            vis_resultobj.verify_legends(pie_legend, '#MAINTABLE_wbody0', legend_length=5, msg="Step "+str(step_no)+".4: Verify pie legends.")
            utillobj.verify_chart_color('MAINTABLE_wbody0', pie_raiser_class, pie_color, "Step "+str(step_no)+".5: Verify pie chart color.")
            utillobj.verify_element_text('#MAINTABLE_wbody1 body span', pie_chart_title, "Step "+str(step_no)+".6: Verify pie chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0 ', pie_filter_menu, "Step "+str(step_no)+".7: Verify Pie filter menu.", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step "+str(step_no)+".8: Verify pie menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody0', pie_raiser_class, pie_tooltip, "Step "+str(step_no)+".9: Verify pie tool_tip.")
            
            ''' Verify line_chart'''
            vis_resultobj.verify_number_of_riser('MAINTABLE_wbody1', 1, line_expected_number, "Step "+str(step_no)+".10: Verify number of riser in line chart.", custome_css=" svg g.risers >g>path[class^='riser']")
            vis_resultobj.verify_xaxis_title('MAINTABLE_wbody1', line_xaxis_title, "Step "+str(step_no)+".11: Verify line x-axis_title.")
            vis_resultobj.verify_yaxis_title('MAINTABLE_wbody1', line_yaxis_title, "Step "+str(step_no)+".12: Verify line y-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', line_x_lable, line_y_lable, "Step "+str(step_no)+".13: Verify line-xy-axis_Labels.")
            utillobj.verify_chart_color('MAINTABLE_wbody1', line_raiser_class, line_color, "Step "+str(step_no)+".14: Verify line chart color.", attribute_type='stroke')
            utillobj.verify_element_text('#MAINTABLE_wbody1 body span', line_chart_title, "Step "+str(step_no)+".15: Verify line chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu1 ', line_filter_menu, "Step "+str(step_no)+".16: Verify line filter menu..", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu1', ['Sum'],"Step "+str(step_no)+".17: Verify line menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            elem = self.driver.find_element_by_id("MAINTABLE_wbody1")
            utillobj.click_on_screen(elem, 'top_middle')
            elem1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g1!mmarker']")
            utillobj.click_on_screen(elem1, 'middle', javascript_marker_enable=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody1', 'marker!s0!g1!mmarker', line_tooltip, "Step "+str(step_no)+".18: Verify line tooltip.", default_move=True)
            
            '''verify bar-chart'''
            vis_resultobj.verify_number_of_riser('MAINTABLE_wbody2', 1, bar_expected_number, "Step "+str(step_no)+".19: Verify number of riser in bar chart.")
            vis_resultobj.verify_xaxis_title('MAINTABLE_wbody2', bar_xaxis_title, "Step "+str(step_no)+".20: Verify bar x-axis_title.")
            vis_resultobj.verify_yaxis_title('MAINTABLE_wbody2', bar_yaxis_title, "Step "+str(step_no)+".21: Verify bar y-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody2', bar_x_lable, bar_y_lable, "Step "+str(step_no)+".23: Verify bar-xy-axis_Labels.")
            utillobj.verify_chart_color('MAINTABLE_wbody2', bar_raiser_class, bar_color, "Step "+str(step_no)+".24: Verify bar chart color.")
            utillobj.verify_element_text('#MAINTABLE_wbody2 body span', bar_chart_title, "Step "+str(step_no)+".25: Verify bar chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu2 ', bar_filter_menu, "Step "+str(step_no)+".26: Verify bar filter menu..", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu2', ['Sum'],"Step "+str(step_no)+".27: Verify bar menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody2', bar_raiser_class, bar_tooltip, "Step "+str(step_no)+".28: Verify bar tooltip.")
            
            '''verify Century Electronics: Detailed Revenue Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody3 [id*='THEAD'] span")
            actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]]
            utillity.UtillityMethods.asequal(self, ['Century Electronics: Detailed Revenue Report'], actual_list, "Step "+str(step_no)+".29: Verify Century Electronics: Detailed Revenue Report Heading.")
            active_mis_obj.verify_page_summary(3, century_electronics_page_summary_title, "Step "+str(step_no)+".30: Verify Century Electronics: Detailed Revenue Report page summary.")
            active_mis_obj.verify_column_heading('ITableData3', ['Region', 'State', 'City', 'Revenue'], "Step "+str(step_no)+".31: Verify Century Electronics: Detailed Revenue Report page column heading.")
#             utillobj.create_table_data("table#ITableData3 tbody tr[id^='I3r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData3 tbody tr[id^='I3r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            active_mis_obj.verify_visualization('ITableData3', 'I3r', 3, 'light_gray', "Step "+str(step_no)+".33: Verify Century Electronics: Detailed Revenue Report visualization.")
            
            '''verify Regional Product Sales Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody4 [id*='THEAD'] span")
            actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]]
            utillity.UtillityMethods.asequal(self, ['Regional Product Sales'], actual_list, "Step "+str(step_no)+".34: Verify Regional Product Sales Report Heading.")
            active_mis_obj.verify_page_summary(4, regional_product_sales_report_page_summary_title, "Step "+str(step_no)+".35: Verify Regional Product Sales Report page summary.")
            active_mis_obj.verify_column_heading('ITableData4', ['Region', 'State', 'Category', 'Revenue'], "Step "+str(step_no)+".36: Verify Regional Product Sales Report page column heading.")
#             utillobj.create_table_data("table#ITableData4 tbody tr[id^='I4r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData4 tbody tr[id^='I4r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            
            '''Verify page layout'''
            expected_layout=['Layouts', 'Revenue Report', 'Regional Report', 'Product Report', 'Region', 'Middle Atlantic\nNew England\nPacific\nSouth Atlantic']
            ia_runobj.verify_active_document_page_layout_menu("table[id^='iLayTB']", expected_layout, "Step "+str(step_no)+".38: Verify revenue_report_page Layout.")
            selected_page_text = self.driver.find_element_by_css_selector("form[name='mergeform'] table[id='iLayTB$'] .arDashboardBarButtonSelected").text.strip()
            utillobj.asequal('Revenue Report', selected_page_text, "Step "+str(step_no)+".39: Verify revenue_report_page Layout 'Revenue Report' Selected.")
            utillobj.verify_dropdown_value('.arDashboardMergeDropdown', expected_default_selected_value=region_drop_down_selected, default_selection_msg="Step "+str(step_no)+".40: Verify revenue_report_page Layout 'Middle Atlantic' selected.")
            
            '''Verify three chart on the above of report two report'''
            pie_chart_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody0")
            pie_chart_height = utillobj.get_object_screen_coordinate(pie_chart_element, coordinate_type='bottom_middle')
            line_chart_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody1")
            line_chart_height = utillobj.get_object_screen_coordinate(line_chart_element, coordinate_type='bottom_middle')
            bar_chart_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody2")
            bar_chart_height = utillobj.get_object_screen_coordinate(bar_chart_element, coordinate_type='bottom_middle')
            century_electronics_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody3")
            century_electronics_height = utillobj.get_object_screen_coordinate(century_electronics_element, coordinate_type='top_middle') 
            regional_product_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody4")
            regional_product_height = utillobj.get_object_screen_coordinate(regional_product_element, coordinate_type='top_middle') 
            if century_electronics_height['y'] > pie_chart_height['y'] and century_electronics_height['y'] > line_chart_height['y'] and century_electronics_height['y'] > bar_chart_height['y'] and regional_product_height['y'] > pie_chart_height['y'] and regional_product_height['y'] > line_chart_height['y'] and regional_product_height['y'] > bar_chart_height['y']:
                status_ = True
            else:
                status_ = False
            utillobj.asequal(True, status_, "Step "+str(step_no)+".41: Verify three chart on the above of report two report.")
        
        def verify_regional_report_page(wait_css=None, wait_text=None, step_no=None, regional_product_sales_report_page_summary_title=None, century_electronics_page_summary_title=None, 
                                        line_expected_number=None, line_xaxis_title=None, line_x_lable=None, line_y_lable=None, line_raiser_class=None, line_color=None, line_chart_title=None, line_filter_menu=None,
                                        line_tooltip=None):
            
            utillobj.synchronize_with_visble_text(wait_css, wait_text, 25)
            
            '''verify  Revenue Report page title'''
            revenue_report_text = self.driver.find_element_by_css_selector("[id^='LOBJText_'][style*='block'] [id^='LOBJText'][id$='TEXT']").text.strip().replace('\n',' ')  
            utillobj.asequal('Century Electronics Regional Revenue Report', revenue_report_text, "Step "+str(step_no)+".1: Verify Revenue Report page title.")
            
            '''verify Regional Product Sales Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody5 [id*='THEAD'] span")
            actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]]
            utillity.UtillityMethods.asequal(self, ['Regional Product Sales'], actual_list, "Step "+str(step_no)+".2: Verify Regional Product Sales Report Heading.")
            active_mis_obj.verify_page_summary(5, regional_product_sales_report_page_summary_title, "Step "+str(step_no)+".3: Verify Regional Product Sales Report page summary.")
            active_mis_obj.verify_column_heading('ITableData5', ['Region', 'State', 'Product Type', 'Revenue'], "Step "+str(step_no)+".4: Verify Regional Product Sales Report page column heading.")
#             utillobj.create_table_data("table#ITableData5 tbody tr[id^='I5r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData5 tbody tr[id^='I5r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            active_mis_obj.verify_visualization('ITableData5', 'I3r', 3, 'light_gray', "Step "+str(step_no)+".6: Verify Regional Product Sales Report visualization.")
            
            '''verify Century Electronics: Detailed Revenue Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody6 [id*='THEAD'] span")
            actual_list=[re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]]
            utillity.UtillityMethods.asequal(self, ['Century Electronics: Detailed Revenue Report'], actual_list, "Step "+str(step_no)+".7: Verify Century Electronics: Detailed Revenue Report Heading.")
            active_mis_obj.verify_page_summary(6, century_electronics_page_summary_title, "Step "+str(step_no)+".8: Verify Century Electronics: Detailed Revenue Report page summary.")
            active_mis_obj.verify_column_heading('ITableData6', ['Region', 'City', 'Store Name', 'Category', 'Quarter', 'Revenue'], "Step "+str(step_no)+".9: Verify Century Electronics: Detailed Revenue Report page column heading.")
#             utillobj.create_table_data("table#ITableData6 tbody tr[id^='I6r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData6 tbody tr[id^='I6r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            
            ''' Verify line_chart'''
            vis_resultobj.verify_number_of_riser('MAINTABLE_wbody7', 1, line_expected_number, "Step "+str(step_no)+".11: Verify number of riser in line chart.", custome_css=" svg g.risers >g>path[class^='riser']")
            vis_resultobj.verify_xaxis_title('MAINTABLE_wbody7', line_xaxis_title, "Step "+str(step_no)+".12: Verify line x-axis_title.")
            vis_resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody7', line_x_lable, line_y_lable, "Step "+str(step_no)+".13: Verify line-xy-axis_Labels.")
            utillobj.verify_chart_color('MAINTABLE_wbody7', line_raiser_class, line_color, "Step "+str(step_no)+".14: Verify line chart color.", attribute_type='stroke')
            utillobj.verify_element_text('#MAINTABLE_wbody7 body span', line_chart_title, "Step "+str(step_no)+".15: Verify line chart title.")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu7 ', line_filter_menu, "Step "+str(step_no)+".16: Verify line filter menu..", custom_css="[title]")
            active_mis_obj.verify_arChartToolbar('MAINTABLE_wmenu7', ['Sum'],"Step "+str(step_no)+".17: Verify line menu sum text.", custom_css=".arChartMenuBarContainer .tabPagingText1 [id*='SUM'] td[valign]", text=True)
            elem = self.driver.find_element_by_id("MAINTABLE_wbody7")
            utillobj.click_on_screen(elem, 'top_middle')
            elem1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody7 [class*='marker!s0!g4!mmarker']")
            utillobj.click_on_screen(elem1, 'middle', javascript_marker_enable=True)
            vis_resultobj.verify_default_tooltip_values('MAINTABLE_wbody7', 'marker!s0!g4!mmarker', line_tooltip, "Step "+str(step_no)+".18: Verify line tooltip.", default_move=True)
            
            '''Verify page layout'''
            expected_layout=['Layouts', 'Revenue Report', 'Regional Report', 'Product Report', 'Region', 'Middle Atlantic\nNew England\nPacific\nSouth Atlantic']
            ia_runobj.verify_active_document_page_layout_menu("table[id^='iLayTB']", expected_layout, "Step "+str(step_no)+".19: Verify revenue_report_page Layout.")
            selected_page_text = self.driver.find_element_by_css_selector("form[name='mergeform'] table[id='iLayTB$'] .arDashboardBarButtonSelected").text.strip()
            utillobj.asequal('Regional Report', selected_page_text, "Step "+str(step_no)+".20: Verify revenue_report_page Layout 'Revenue Report' Selected.")
            utillobj.verify_dropdown_value('.arDashboardMergeDropdown', expected_default_selected_value='Middle Atlantic', default_selection_msg="Step "+str(step_no)+".21: Verify revenue_report_page Layout 'Middle Atlantic' selected.")
            
            '''Verify two report on the above of line chart'''
            regional_product_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody5")
            regional_product_height = utillobj.get_object_screen_coordinate(regional_product_element, coordinate_type='top_middle') 
            century_electronics_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody6")
            century_electronics_height = utillobj.get_object_screen_coordinate(century_electronics_element, coordinate_type='top_middle') 
            line_chart_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody7")
            line_chart_height = utillobj.get_object_screen_coordinate(line_chart_element, coordinate_type='bottom_middle')
            if line_chart_height['y'] > regional_product_height['y'] and line_chart_height['y'] > century_electronics_height['y']:
                status_ = True
            else:
                status_ = False
            utillobj.asequal(True, status_, "Step "+str(step_no)+".22: Verify two report on the above of line chart.")
        
        def verify_product_report_page(wait_css=None, wait_text=None, step_no=None, regional_product_sales_report_page_summary_title=None, century_electronics_page_summary_title=None):
            
            utillobj.synchronize_with_visble_text(wait_css, wait_text, 125)
            
            '''verify Product Category: Price and Cost Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody8 [id*='THEAD'] span")
            actual_list=[elem for elem in [re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]] if elem != '']
            utillity.UtillityMethods.as_List_equal(self, ['Product Category: Price and Cost'], actual_list, "Step "+str(step_no)+".1: Verify Product Category: Price and Cost Report Heading.")
            active_mis_obj.verify_page_summary(8, regional_product_sales_report_page_summary_title, "Step "+str(step_no)+".2: Verify Product Category: Price and Cost Report page summary.")
            active_mis_obj.verify_column_heading('ITableData8', ['Product Category', 'Product Name', 'Model', 'Price', 'Cost', 'Product Type'], "Step "+str(step_no)+".3: Verify Product Category: Price and Cost Report page column heading.")
#             utillobj.create_table_data("table#ITableData8 tbody tr[id^='I8r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData8 tbody tr[id^='I8r']", test_case_id + "_2_Ds0"+str(step_no)+".xlsx")
            active_mis_obj.verify_visualization('ITableData8', 'I8r', 4, 'light_gray', "Step "+str(step_no)+".5: Verify Product Category: Price and Cost Report visualization.")
            
            '''verify Profit By Product Category Report'''
            table_heading=self.driver.find_elements_by_css_selector("#IWindowBody9 [id*='THEAD'] span")
            actual_list=[elem for elem in [re.sub('\s+', ' ', el.strip()) for el in [el1.text for el1 in table_heading]] if elem != '']
            utillity.UtillityMethods.asequal(self, ['Profit By Product Category'], actual_list, "Step "+str(step_no)+".6: Verify Profit By Product Category Report Heading.")
            active_mis_obj.verify_page_summary(9, century_electronics_page_summary_title, "Step "+str(step_no)+".7: Verify Profit By Product Category Report page summary.")
            active_mis_obj.verify_column_heading('ITableData9', ['Product Type', 'Profit', 'Revenue', 'Shipping Cost'], "Step "+str(step_no)+".8: Verify Profit By Product Category Report page column heading.")
#             utillobj.create_table_data("table#ITableData9 tbody tr[id^='I9r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            utillobj.verify_table_data("table#ITableData9 tbody tr[id^='I9r']", test_case_id + "_1_Ds0"+str(step_no)+".xlsx")
            
            '''Verify page layout'''
            expected_layout=['Layouts', 'Revenue Report', 'Regional Report', 'Product Report', 'Region', 'Middle Atlantic\nNew England\nPacific\nSouth Atlantic']
            ia_runobj.verify_active_document_page_layout_menu("table[id^='iLayTB']", expected_layout, "Step "+str(step_no)+".10: Verify revenue_report_page Layout.")
            selected_page_text = self.driver.find_element_by_css_selector("form[name='mergeform'] table[id='iLayTB$'] .arDashboardBarButtonSelected").text.strip()
            utillobj.asequal('Product Report', selected_page_text, "Step "+str(step_no)+".11: Verify revenue_report_page Layout 'Revenue Report' Selected.")
            utillobj.verify_dropdown_value('.arDashboardMergeDropdown', expected_default_selected_value='Middle Atlantic', default_selection_msg="Step "+str(step_no)+".12: Verify product_report_page Layout 'Middle Atlantic' selected.")
            
            '''Verify Product Category: Price and Cost Report on the above of Profit By Product Category Report'''
            product_category_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody8")
            product_category_height = utillobj.get_object_screen_coordinate(product_category_element, coordinate_type='top_middle') 
            profit_by_product_category_element = self.driver.find_element_by_css_selector("div#MAINTABLE_wbody9")
            profit_by_product_category_height = utillobj.get_object_screen_coordinate(profit_by_product_category_element, coordinate_type='top_middle') 
            if profit_by_product_category_height['y'] > product_category_height['y']:
                status_ = True
            else:
                status_ = False
            utillobj.asequal(True, status_, "Step "+str(step_no)+".13: Verify Product Category: Price and Cost Report on the above of Profit By Product Category Report.")
            
        """ Step 1: Execute the attached repro - CenturySales_IA8201.fex
                    Expect to see the following layout of Page one, named Revenue Report.
                    Expect to see three charts at the top, a PIE, Line and Bar chart.
                    Also expect to see a pair of Active reports below.
                    The default value for the Coordinated field is - Middle Atlantic.
        """
        """ Step 2: Hover over a PIE slice, then a point on the Line Chart and lastly a Bar.
                    Expect to see the Tool Tip information reflect the Region of Middle Atlantic.
                    Also verify that the Reports contain only rows for Middle Atlantic.
        """
        utillobj.active_run_fex_api_login('CenturySales_IA8201.fex','S10071_2','mrid','mrpass')
        utillobj.synchronize_with_visble_text("#ITableData3 #TCOL_3_C_1", 'Region', 150)
        
        wait_css="#ITableData4 tr[id^='I4r'] td:nth-child(1)"
        wait_text="MiddleAtlantic"
        step_no=2
        pie_expected_number=5
        pie_label=['Revenue']
        pie_legend=['Category', 'Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        pie_raiser_class='riser!s0!g0!mwedge'
        pie_color='bar_blue'
        pie_chart_title='Revenue By City'
        pie_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_tooltip=['Region:Middle Atlantic', 'Category:Audio', 'Revenue:13,956.00  (22.15%)', 'Filter Chart', 'Exclude from Chart']
        line_expected_number=1
        line_xaxis_title='City'
        line_yaxis_title='Revenue'
        line_x_lable=['Albany', 'Jersey City', 'New York City', 'Philadelphia', 'Princeton', 'Syracuse']
        line_y_lable=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        line_raiser_class='riser!s0!g0!mline'
        line_color='bar_blue'
        line_chart_title='Revenue By City'
        line_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        line_tooltip=['Region:Middle Atlantic', 'City:Jersey City', 'Revenue:20,955.00', 'Filter Chart', 'Exclude from Chart']
        bar_expected_number=3
        bar_xaxis_title='State'
        bar_yaxis_title='Revenue'
        bar_x_lable=['New Jersey', 'New York', 'Pennsylvania']
        bar_y_lable=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        bar_raiser_class='riser!s0!g0!mbar'
        bar_color='bar_blue'
        bar_chart_title='Revenue By State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['Region:Middle Atlantic', 'State:New Jersey', 'Revenue:29,120.00', 'Filter Chart', 'Exclude from Chart']
        century_electronics_page_summary_title='6of16records,Page1of1'
        regional_product_sales_report_page_summary_title='15of46records,Page1of1'
        region_drop_down_selected='Middle Atlantic'
        verify_revenue_report_page(wait_css=wait_css, wait_text=wait_text, step_no=step_no, pie_expected_number=pie_expected_number, pie_label=pie_label,
                                   pie_legend=pie_legend, pie_raiser_class=pie_raiser_class, pie_color=pie_color, pie_chart_title=pie_chart_title, 
                                   pie_filter_menu=pie_filter_menu, pie_tooltip=pie_tooltip, line_expected_number=line_expected_number, line_xaxis_title=line_xaxis_title,
                                   line_yaxis_title=line_yaxis_title, line_x_lable=line_x_lable, line_y_lable=line_y_lable, line_raiser_class=line_raiser_class,
                                   line_color=line_color, line_chart_title=line_chart_title, line_filter_menu=line_filter_menu, line_tooltip=line_tooltip, 
                                   bar_expected_number=bar_expected_number, bar_xaxis_title=bar_xaxis_title, bar_yaxis_title=bar_yaxis_title, bar_x_lable=bar_x_lable, 
                                   bar_y_lable=bar_y_lable, bar_raiser_class=bar_raiser_class, bar_color=bar_color, bar_chart_title=bar_chart_title, 
                                   bar_filter_menu=bar_filter_menu, bar_tooltip=bar_tooltip, century_electronics_page_summary_title=century_electronics_page_summary_title, 
                                   regional_product_sales_report_page_summary_title=regional_product_sales_report_page_summary_title, region_drop_down_selected=region_drop_down_selected)
         
        """ Step 3: In the Coordinated Filter at the top, labelled Region, select New England.
                    Expect to see the components but now the data represents New England, in Tool Tips and on the reports.
        """
        utillobj.select_dropdown('.arDashboardMergeDropdown', 'value', 'New England')
        wait_css="#ITableData4 tr[id^='I4r'] td:nth-child(1)"
        wait_text="NewEngland"
        step_no=3
        pie_expected_number=5
        pie_label=['Revenue']
        pie_legend=['Category', 'Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        pie_raiser_class='riser!s0!g0!mwedge'
        pie_color='bar_blue'
        pie_chart_title='Revenue By City'
        pie_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_tooltip=['Region:New England', 'Category:Audio', 'Revenue:3,205.00  (19.40%)', 'Filter Chart', 'Exclude from Chart']
        line_expected_number=1
        line_xaxis_title='City'
        line_yaxis_title='Revenue'
        line_x_lable=['Hartford', 'New Haven', 'Worchester']
        line_y_lable=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000']
        line_raiser_class='riser!s0!g0!mline'
        line_color='bar_blue'
        line_chart_title='Revenue By City'
        line_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        line_tooltip=['Region:New England', 'City:New Haven', 'Revenue:2,715.00', 'Filter Chart', 'Exclude from Chart']
        bar_expected_number=2
        bar_xaxis_title='State'
        bar_yaxis_title='Revenue'
        bar_x_lable=['Connecticut', 'Massachusetts']
        bar_y_lable=['0', '2,000', '4,000', '6,000', '8,000', '10,000']
        bar_raiser_class='riser!s0!g0!mbar'
        bar_color='bar_blue'
        bar_chart_title='Revenue By State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['Region:New England', 'State:Connecticut', 'Revenue:9,095.00', 'Filter Chart', 'Exclude from Chart']
        century_electronics_page_summary_title='3of16records,Page1of1'
        regional_product_sales_report_page_summary_title='8of46records,Page1of1'
        region_drop_down_selected='New England'
        verify_revenue_report_page(wait_css=wait_css, wait_text=wait_text, step_no=step_no, pie_expected_number=pie_expected_number, pie_label=pie_label,
                                   pie_legend=pie_legend, pie_raiser_class=pie_raiser_class, pie_color=pie_color, pie_chart_title=pie_chart_title, 
                                   pie_filter_menu=pie_filter_menu, pie_tooltip=pie_tooltip, line_expected_number=line_expected_number, line_xaxis_title=line_xaxis_title,
                                   line_yaxis_title=line_yaxis_title, line_x_lable=line_x_lable, line_y_lable=line_y_lable, line_raiser_class=line_raiser_class,
                                   line_color=line_color, line_chart_title=line_chart_title, line_filter_menu=line_filter_menu, line_tooltip=line_tooltip, 
                                   bar_expected_number=bar_expected_number, bar_xaxis_title=bar_xaxis_title, bar_yaxis_title=bar_yaxis_title, bar_x_lable=bar_x_lable, 
                                   bar_y_lable=bar_y_lable, bar_raiser_class=bar_raiser_class, bar_color=bar_color, bar_chart_title=bar_chart_title, 
                                   bar_filter_menu=bar_filter_menu, bar_tooltip=bar_tooltip, century_electronics_page_summary_title=century_electronics_page_summary_title, 
                                   regional_product_sales_report_page_summary_title=regional_product_sales_report_page_summary_title, region_drop_down_selected=region_drop_down_selected)
         
        """ Step 4: Switch back to Middle Atlantic.
        """
        utillobj.select_dropdown('.arDashboardMergeDropdown', 'value', 'Middle Atlantic')
        wait_css="#ITableData4 tr[id^='I4r'] td:nth-child(1)"
        wait_text="MiddleAtlantic"
        step_no=4
        pie_expected_number=5
        pie_label=['Revenue']
        pie_legend=['Category', 'Audio', 'Camcorders', 'Cameras', 'Office', 'Video']
        pie_raiser_class='riser!s0!g0!mwedge'
        pie_color='bar_blue'
        pie_chart_title='Revenue By City'
        pie_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        pie_tooltip=['Region:Middle Atlantic', 'Category:Audio', 'Revenue:13,956.00  (22.15%)', 'Filter Chart', 'Exclude from Chart']
        line_expected_number=1
        line_xaxis_title='City'
        line_yaxis_title='Revenue'
        line_x_lable=['Albany', 'Jersey City', 'New York City', 'Philadelphia', 'Princeton', 'Syracuse']
        line_y_lable=['0', '4K', '8K', '12K', '16K', '20K', '24K']
        line_raiser_class='riser!s0!g0!mline'
        line_color='bar_blue'
        line_chart_title='Revenue By City'
        line_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        line_tooltip=['Region:Middle Atlantic', 'City:Jersey City', 'Revenue:20,955.00', 'Filter Chart', 'Exclude from Chart']
        bar_expected_number=3
        bar_xaxis_title='State'
        bar_yaxis_title='Revenue'
        bar_x_lable=['New Jersey', 'New York', 'Pennsylvania']
        bar_y_lable=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        bar_raiser_class='riser!s0!g0!mbar'
        bar_color='bar_blue'
        bar_chart_title='Revenue By State'
        bar_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        bar_tooltip=['Region:Middle Atlantic', 'State:New Jersey', 'Revenue:29,120.00', 'Filter Chart', 'Exclude from Chart']
        century_electronics_page_summary_title='6of16records,Page1of1'
        regional_product_sales_report_page_summary_title='15of46records,Page1of1'
        region_drop_down_selected='Middle Atlantic'
        verify_revenue_report_page(wait_css=wait_css, wait_text=wait_text, step_no=step_no, pie_expected_number=pie_expected_number, pie_label=pie_label,
                                   pie_legend=pie_legend, pie_raiser_class=pie_raiser_class, pie_color=pie_color, pie_chart_title=pie_chart_title, 
                                   pie_filter_menu=pie_filter_menu, pie_tooltip=pie_tooltip, line_expected_number=line_expected_number, line_xaxis_title=line_xaxis_title,
                                   line_yaxis_title=line_yaxis_title, line_x_lable=line_x_lable, line_y_lable=line_y_lable, line_raiser_class=line_raiser_class,
                                   line_color=line_color, line_chart_title=line_chart_title, line_filter_menu=line_filter_menu, line_tooltip=line_tooltip, 
                                   bar_expected_number=bar_expected_number, bar_xaxis_title=bar_xaxis_title, bar_yaxis_title=bar_yaxis_title, bar_x_lable=bar_x_lable, 
                                   bar_y_lable=bar_y_lable, bar_raiser_class=bar_raiser_class, bar_color=bar_color, bar_chart_title=bar_chart_title, 
                                   bar_filter_menu=bar_filter_menu, bar_tooltip=bar_tooltip, century_electronics_page_summary_title=century_electronics_page_summary_title, 
                                   regional_product_sales_report_page_summary_title=regional_product_sales_report_page_summary_title, region_drop_down_selected=region_drop_down_selected)
          
        """ Step 5: In the Page Layout Area, select the tab for - Regional Report.
                    Expect to see the following layout of Page two.
                    Expect to see two reports on the top and a Line chart on the bottom.
        """
        ia_runobj.select_active_document_page_layout_menu('Regional Report')
        wait_css="#ITableData6 tr[id^='I6r'] td:nth-child(1)"
        wait_text='Middle Atlantic'
        step_no=5
        regional_product_sales_report_page_summary_title='15of42records,Page1of1'
        century_electronics_page_summary_title='33of79records,Page1of1'
        line_expected_number=2
        line_xaxis_title='Product Type : Quarter'
        line_x_lable=['Audio...', 'Camc...', 'Came...', 'Office...', 'Video...']
        line_y_lable=['0', '7.5K', '15K', '22.5K', '30K']
        line_raiser_class='riser!s0!g0!mline'
        line_color='bar_blue'
        line_chart_title='Category Quarterly Revenue'
        line_filter_menu=['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation']
        line_tooltip=['Region:Middle Atlantic', 'Product Type:Video', 'Quarter:Q4', 'Revenue:16,885.00', 'Filter Chart', 'Exclude from Chart']
        verify_regional_report_page(wait_css=wait_css, wait_text=wait_text, step_no=step_no, regional_product_sales_report_page_summary_title=regional_product_sales_report_page_summary_title,
                                    century_electronics_page_summary_title=century_electronics_page_summary_title, line_expected_number=line_expected_number, line_xaxis_title=line_xaxis_title, 
                                    line_x_lable=line_x_lable, line_y_lable=line_y_lable, line_raiser_class=line_raiser_class, line_color=line_color, line_chart_title=line_chart_title, 
                                    line_filter_menu=line_filter_menu, line_tooltip=line_tooltip)
        
        """ Step 6: In the Page Layout Area, select the tab for - Product Report.
                    Expect to see the following layout of Page three.
                    Expect to see two Active Reports.
        """
        ia_runobj.select_active_document_page_layout_menu('Product Report')
        wait_css="#ITableData9 tr[id^='I9r'] td:nth-child(1)"
        wait_text="Audio"
        step_no=6
        regional_product_sales_report_page_summary_title='43of120records,Page1of1'
        century_electronics_page_summary_title='90of200records,Page1of2'
        verify_product_report_page(wait_css=wait_css, wait_text=wait_text, step_no=step_no, regional_product_sales_report_page_summary_title=regional_product_sales_report_page_summary_title, 
                                   century_electronics_page_summary_title=century_electronics_page_summary_title)
        
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()