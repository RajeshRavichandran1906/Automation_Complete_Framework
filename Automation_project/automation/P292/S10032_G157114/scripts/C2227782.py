'''
Created on Dec 16, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227782
TestCase Name : Chart:Verify basic chart production for Column, PIE, Line chart and Scatter diagram.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, visualization_resultarea,ia_resultarea,visualization_metadata,visualization_ribbon
from common.lib import utillity
from common.wftools import active_chart
from pywinauto.handleprops import parent

class C2227782_TestClass(BaseTestCase):

    def test_C2227782(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227782'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        actchart_obj=active_chart.Active_Chart(self.driver)
        expected_default_x_axis_label_list=['Group 0', 'Group 1', 'Group 2', 'Group 3','Group 4']
        expected_default_y_axis_label_list=['0', '10', '20', '30', '40', '50']
        expected_y_axis_title_list=['Gross Profit']
        expected_x_axis_title_list=['Product Category']
        expected_x_axis_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_y_axis_label_list=['0', '20M', '40M', '60M', '80M', '100M']
        runtime_bar_chart_riser_css="riser!s0!g0!mbar!"
        runtime_barchart_expected_tooltip_list=['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart']
        expected_toolbar_menu_list=['More Options','Advanced Chart','Original Chart']
        run_parent_css="#jschart_HOLD_0"
        expected_piechart_preview_title_list=['Gross Profit']
        expected_piechart_preview_legends=['Accessories']
        
        """
        Step 01:Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 02:Navigate to folder: P292_S10032_G157266
        Execute the following URL:
        http://machine:port/{alias}/ia?tool=chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10032_G157266%2F
        Change the Output type to Active Report.
        """
        
        actchart_obj.invoke_chart_tool_using_api("new_retail/wf_retail_lite", mrid="autodevuser01")
        actchart_obj.verify_x_axis_label_in_preview(expected_default_x_axis_label_list, msg="Step 01:01:")
        actchart_obj.verify_y_axis_label_in_preview(expected_default_y_axis_label_list, msg="Step 01:02:")
#         ribbonobj.change_output_format_type('active_report', location='Home')
        
        """
        Step 03:From the Measures group, select the Sales sub-group of fields, then select the Gross_Profit field.
        From the Dimensions group, select the Product sub-group, then select the Product,Category field.
        """
        actchart_obj.double_click_on_datetree_item('Gross Profit', 1)
        actchart_obj.wait_for_number_of_element("#TableChart_1 text[class^='yaxis'][class$='title']", 1, 35)
        actchart_obj.double_click_on_datetree_item('Product,Category', 1)
        actchart_obj.wait_for_number_of_element("#TableChart_1 text[class^='xaxis'][class$='title']", 1, 35)
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, msg="Step 01:02: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 01:03: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 01:04:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 01:05:")
        actchart_obj.verify_number_of_risers_in_preview('rect', 1, 7, msg='Step 03:01')
        
        """
        Step 04:Click the Run button
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#MAINTABLE_wbody0", msg="Step 04:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list,parent_css="#MAINTABLE_wbody0", msg="Step 04:04:")
        actchart_obj.verify_number_of_risers_in_run_window('rect', 1, 7, parent_css="#MAINTABLE_wbody0",msg='Step 04:06:')
        actchart_obj.verify_tooltip_in_run_window(runtime_bar_chart_riser_css, runtime_barchart_expected_tooltip_list, "Step 04:07:Verify tooltip value at runtime for bar chart", parent_css="#MAINTABLE_wbody0")
        actchart_obj.verify_active_chart_toolbar(expected_toolbar_menu_list, msg="Step 04:07:Verify chart title", parent_css="#MAINTABLE_wmenu0")
        
        """
        Step 05:Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the PIE icon.
        """
        actchart_obj.switch_to_default_content()
        actchart_obj.select_chart_type('pie')
        actchart_obj.wait_for_number_of_element("#TableChart_1 .chartPanel text", expected_number=1)
        actchart_obj.verify_x_axis_title_in_preview(expected_piechart_preview_title_list, msg="Step 05:01:")
        actchart_obj.verify_legends_in_preview(expected_piechart_preview_legends, msg='Step 05:02')
        pie_riser_css=["riser!s4!g0!mwedge!"]
        actchart_obj.verify_chart_color_using_get_attribute_in_preview(pie_riser_css, 'brick_red', msg='Step 05:03:Verify chart')
        actchart_obj.verify_number_of_risers_in_preview('path', 1, 7, msg='Step 03:01')
        
        """
        Step 06: Click the Run button.
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 06:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 06:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, msg="Step 06:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, msg="Step 06:04:")
        actchart_obj.verify_number_of_risers_in_run_window('rect', 1, 7, msg='Step 06:05:')
        actchart_obj.verify_tooltip_in_run_window(runtime_bar_chart_riser_css, runtime_barchart_expected_tooltip_list, "Step 06:06:Verify tooltip value at runtime for bar chart")
        expected_toolbar_menu_list=['Gross Profit BY Product Category']
        actchart_obj.verify_active_chart_toolbar(run_parent_css, expected_toolbar_menu_list, msg="Step 06:07:Verify chart title" )
        
        """
        Step 07: Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the LINE icon.
        """
        actchart_obj.switch_to_default_content()
        #select formattab line chart
        actchart_obj.wait_for_number_of_element("#TableChart_1 path[class='riser!s0!g0!mline!']", expected_number=1)
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, msg="Step 07:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 07:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 07:03:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 07:04:")
        actchart_obj.verify_number_of_risers_in_preview('path', 1, 7, msg='Step 07:05:')
        
        """
        Step 08: Click the Run button.
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        line_riser_css="marker!s0!g5!mmarker!"
        expected_tooltip_list=['Camcorder']
        msg="Verify Line chart tooltip valu"
        actchart_obj.verify_tooltip_in_run_window(line_riser_css, expected_tooltip_list, msg, use_marker_enable=True)
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, msg="Step 08:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, msg="Step 08:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, msg="Step 08:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, msg="Step 08:04:")
        actchart_obj.verify_active_chart_toolbar(run_parent_css, expected_toolbar_menu_list, "Step 08:05:Verify chart title")
        
        """
        Step 09: Click the Format button in the control area at the top of the chart.
        Select the Chart Types icon and select the SCATTER icon.
        """
        actchart_obj.switch_to_default_content()
        #add scatter chart
        actchart_obj.wait_for_number_of_element("#TableChart_1 circle[class^='riser']", expected_number=7)
        actchart_obj.verify_x_axis_title_in_preview(expected_x_axis_title_list, msg="Step 09:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_preview(expected_y_axis_title_list, msg="Step 09:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_preview(expected_x_axis_label_list, msg="Step 09:03:")
        actchart_obj.verify_y_axis_label_in_preview(expected_y_axis_label_list, msg="Step 09:04:")
        actchart_obj.verify_number_of_risers_in_preview('circle', 1, 7, msg='Step 09:05')
        
        """
        Step 10: Click run button
        """
        actchart_obj.run_chart_from_toptoolbar()
        frame_css="[id^='ReportIframe']"
        actchart_obj.wait_for_number_of_element(frame_css, expected_number=1)
        actchart_obj.switch_to_frame(frame_css)
        scatter_riser_css="riser!s0!g0!mmarker!"
        expected_tooltip_list=['Camcorder']
        msg="Verify Line chart tooltip valu"
        actchart_obj.verify_tooltip_in_run_window(line_riser_css, expected_tooltip_list, msg, use_marker_enable=True)
        actchart_obj.verify_x_axis_title_in_run_window(expected_x_axis_title_list, parent_css="#MAINTABLE_wbody0",msg="Step 08:01: Verify x-axis title")
        actchart_obj.verify_y_axis_title_in_run_window(expected_y_axis_title_list, parent_css="#MAINTABLE_wbody0",msg="Step 08:02: Verify y-axis title")
        actchart_obj.verify_x_axis_label_in_run_window(expected_x_axis_label_list, parent_css="#MAINTABLE_wbody0", msg="Step 08:03:")
        actchart_obj.verify_y_axis_label_in_run_window(expected_y_axis_label_list, parent_css="#MAINTABLE_wbody0",msg="Step 08:04:")
        actchart_obj.verify_active_chart_toolbar(run_parent_css, expected_toolbar_menu_list, "Step 08:05:Verify chart title", parent_css="#MAINTABLE_wbody0")
        actchart_obj.verify_chart_color_using_get_attribute_in_run_window(scatter_riser_css, "bar_blue", "Step 08.5: Verify line1 color", parent_css="#MAINTABLE_wbody0", attribute_type='stroke')
        
          
#         """
#         Step 03:Click the Run button.Expect to see the following Chart, displaying a 7 bar vertical Column chart.
#         """
#           
#         ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(5)
#         parent_css="#resultArea [id^=ReportIframe-]"
#         resobj.wait_for_property(parent_css, 1)
#         utillobj.switch_to_frame(pause=2)
#         time.sleep(5)
#         miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Gross Profit BY Product Category", "Step 03.1 : Verify chart title ")
#         expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         expected_yval1_list=['0', '20M', '40M', '60M', '80M', '100M']
#         resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
#         resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 7, 'Step 03.3: Verify the total number of risers displayed on preview')
#         utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g1!mbar!", "bar_blue", "Step 03.4: Verify  riser color")
#         resobj.verify_xaxis_title("MAINTABLE_wbody0","Product Category","Step 03.5: Verify Xaxis title")
#         resobj.verify_yaxis_title("MAINTABLE_wbody0", "Gross Profit", "Step 03.6 Verify yaxis title")
#         expected_tooltip_list=['Product Category:Camcorder', 'Gross Profit:$49,598,845.23', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g1!mbar!", expected_tooltip_list, "Step 03.7: Verify bar value")
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.8a: Verify Chart toolbar")
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.8c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         
#         """
#         Step 04:Click the Format button in the control area at the top of the chart.
#             Select the Chart Types icon and select the PIE icon.
#             Expect to see a new Live Preview canvas showing the PIE chart option.
#         """
#         utillobj.switch_to_default_content(pause=2)
#         time.sleep(5)
#         ribbonobj.select_ribbon_item('Format', 'Pie')
#         time.sleep(5)
#         utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 04.1: Verify Color')
#         utillobj.verify_chart_color('TableChart_1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 04.2: Verify Color')
#         resobj.verify_riser_pie_labels_and_legends('TableChart_1', ['Gross Profit'], "Step 04.3:",custom_css="text[class*='pieLabel']",same_group=True) 
#         ia_resultobj.verify_number_of_chart_segment('TableChart_1', 7, "Step 04.4: Verify number of pie",custom_css="path[class^='riser']")
#         expected_label_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 04.5: Verify Legends ')
#            
#         """
#         Step 05:Click the Run button.Expect to see the following Chart, displaying a 7 slice PIE chart.
#         """
#         ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(5)
#         parent_css="#resultArea [id^=ReportIframe-]"
#         resobj.wait_for_property(parent_css, 1)
#         utillobj.switch_to_frame(pause=2)
#         time.sleep(5)
#         miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","Gross Profit BY Product Category", "Step 05.1 : Verify chart title ")
#         utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 05.2: Verify Color')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.3: Verify Chart toolbar")
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         expected_label_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 05.6: Verify Legends ')
#         expected_tooltip_list=['Product Category:Computers', 'Gross Profit:$33,508,818.12  (11.18%)', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0_f', 'riser!s2!g0!mwedge!', expected_tooltip_list, 'Step 05.7: verify the default tooltip values')
#         time.sleep(2)
#         resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ['Gross Profit'], "Step 05.8:",custom_css="text[class*='pieLabel']",same_group=True) 
#         ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 7, "Step 05.9: Verify number of pie",custom_css="path[class^='riser']")
#           
#         """
#         Step 06:Click the Format button in the control area at the top of the chart.
#         Select the Chart Types icon and select the LINE icon.
#         Expect to see a new Live Preview canvas showing the Line chart option.
#         """
#           
#         utillobj.switch_to_default_content(pause=2)
#         time.sleep(5)
#         ribbonobj.select_ribbon_item('Format', 'line')
#         time.sleep(5)
#         expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         expected_yval1_list=['0', '20M', '40M', '60M', '80M', '100M']
#         resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.1: Verify XY labels")
#         resobj.verify_xaxis_title("TableChart_1", "Product Category","Step 06.2: Verify Xaxis title")
#         resobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 06.2: Verify -yAxis Title") 
#         ia_resultobj.verify_number_of_chart_segment('TableChart_1', 1, 'Step 06.3: Verify Number of riser', custom_css="path[class^='riser']")
#         utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 06.4: Verify line1 color",attribute_type='stroke')
#           
#         """
#         Step 07:Click the Run button.Expect to see the following Chart, displaying a 7 point Line Chart.
#         """
#         ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(5)
#         parent_css="#resultArea [id^=ReportIframe-]"
#         resobj.wait_for_property(parent_css, 1)
#         utillobj.switch_to_frame(pause=2)
#         time.sleep(5)
#         resobj.verify_xaxis_title("MAINTABLE_wbody0", 'Product Category', "Step 07.1: Verify X-Axis Title")
#         resobj.verify_yaxis_title("MAINTABLE_wbody0", "Gross Profit", "Step 07.2: Verify Y-Axis Title")
#         expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         expected_yval1_list=['0', '20M', '40M', '60M', '80M', '100M']
#         resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.3: Verify XY labels")
#         ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 1, 'Step 07.4: Verify Number of riser', custom_css="path[class^='riser']")
#         expected_tooltip_list=['Product Category:  Camcorder', 'Gross Profit:  $49,598,845.23', 'Filter Chart', 'Exclude from Chart']
#         ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g1!mmarker!', expected_tooltip_list, 'Step 07.5: Verify tooltip')
#         utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 07.6: Verify  1st bar color",attribute_type='stroke')
#         miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Gross Profit BY Product Category', 'Step 07.7: Verify Chart Title')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.8a: Verify Chart toolbar")
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
#         """
#         Step 08:Click the Format button in the control area at the top of the chart.
#         Select the Chart Types icon and select the SCATTER icon.
#         Expect to see a new Live Preview canvas showing the Scatter Diagram option.
#         """
#         utillobj.switch_to_default_content(pause=2)
#         time.sleep(5)
#         ribbonobj.select_ribbon_item('Format', 'scatter')
#         time.sleep(5)
#         expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         expected_yval1_list=['0', '20M', '40M', '60M', '80M', '100M']
#         resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 08.1: Verify XY labels")
#         resobj.verify_xaxis_title("TableChart_1", "Product Category","Step 08.2: Verify Xaxis title")
#         resobj.verify_yaxis_title("TableChart_1", "Gross Profit", "Step 08.3: Verify -yAxis Title") 
#         utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mmarker!", "bar_blue", "Step 08.4: Verify line1 color",attribute_type='stroke')
#         
#         """
#         Step 09:Click the Run button.Expect to see the following Chart, displaying a 7 point Scatter Diagram.
#         """
#         
#         ribbonobj.select_top_toolbar_item('toolbar_run')
#         time.sleep(5)
#         parent_css="#resultArea [id^=ReportIframe-]"
#         resobj.wait_for_property(parent_css, 1)
#         utillobj.switch_to_frame(pause=2)
#         time.sleep(5)
#         resobj.verify_xaxis_title("MAINTABLE_wbody0", 'Product Category', "Step 09.1: Verify X-Axis Title")
#         resobj.verify_yaxis_title("MAINTABLE_wbody0", "Gross Profit", "Step 09.2: Verify Y-Axis Title")
#         expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
#         expected_yval1_list=['0', '20M', '40M', '60M', '80M', '100M']
#         resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.3: Verify XY labels")
#         expected_tooltip_list=['Product Category:Accessories', 'Gross Profit:$39,854,440.52', 'Filter Chart', 'Exclude from Chart']
#         resobj.verify_default_tooltip_values('MAINTABLE_wbody0', 'riser!s0!g0!mmarker!', expected_tooltip_list, 'Step 09.5: verify the default tooltip values',attribute_type='stroke')
#         utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mmarker!", "bar_blue", "Step 09.6: Verify  1st bar color",attribute_type='stroke')
#         miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft', 'Gross Profit BY Product Category', 'Step 09.7: Verify Chart Title')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.8a: Verify Chart toolbar")
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
#         miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
#         time.sleep(5)
#         utillobj.switch_to_default_content(pause=2)   
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
#         time.sleep(2)
#         ribbonobj.select_tool_menu_item('menu_save_as')
#         time.sleep(2)
#         utillobj.ibfs_save_as(Test_Case_ID)
#         time.sleep(3)
if __name__ == '__main__':
    unittest.main()