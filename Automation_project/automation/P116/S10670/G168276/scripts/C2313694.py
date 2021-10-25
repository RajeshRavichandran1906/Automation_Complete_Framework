'''
Created on Nov 14, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313694
TestCase Name = AHTML: Horizontal Dual-Axis Absolute Line Chart Filter/Exclude tests.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea
from common.wftools import visualization
from common.lib import utillity

class C2313694_TestClass(BaseTestCase):

    def test_C2313694(self):
        
        Test_Case_ID="C2313694"
        """
        TESTCASE VARIABLES
        """     
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        visobj = visualization.Visualization(self.driver)

        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Absolute_Line.fex&tool=Chart
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(20)
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_visble_text(parent_css, "DEALER_COST", miscelaneousobj.chart_medium_timesleep)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K',]
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 01.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 01.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 01.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 01.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 01.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 01.8: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.9: Verify legend")

        """
        Step 02:Click the Run button.Expect to see the following Horizontal Dual-Axis Absolute Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 02.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
        Step 03:Hover over the point on the left line for Alfa Romeo.Select Exclude from Chart.
        Expect to see the following Line Chart, with Alfa Romeo removed.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', select_tooltip='Exclude from Chart', msg='Step 3.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'start')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g0!mmarker!", tooltip_css, 'Exclude from Chart', element_location='start', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 03.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 03.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 03.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 03.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 03.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 03.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 03.15 Filter Button Visible')
        
        """
        Step 04:Hover over the point on the left line for BMW.
        Select Exclude from Chart.Expect to see the following Line Chart, with Alfa Romeo & BMW removed.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g1!mmarker!', select_tooltip='Exclude from Chart', msg='Step 4.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g1!mmarker!", tooltip_css, 'Exclude from Chart', element_location='middle', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 04.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 04.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.4: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300', '350', '400', '450']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 04.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 04.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 04.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 04.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 04.15: Filter Button Visible')
         
        """
        Step 05:Hover over the point on the left line for Audi.Select Remove Filter.
        Expect to see the original Line Chart with Alfa Romeo and BMW restored.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', select_tooltip='Remove Filter', msg='Step 5.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'start')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(5)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g1!mmarker!", tooltip_css, 'Remove Filter', element_location='start', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)     
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 05.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 05.15: Filter Button Removed')
        
        """
        Step 06:Left-click and draw a box around the points for linesAlfa Romeo and Audi.
        Select Exclude from Chart.Expect to see the following Line chart with both 
        Alfa Romeo and Audi bars removed.
        """
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g1!mmarker!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g0!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        time.sleep(3)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-30,sy_offset=source_elem['y']+30,tx_offset=target_elem['x']+30,ty_offset=target_elem['y']-30)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 06.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 06.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 06.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 06.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 06.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 06.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 06.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 06.15 Filter Button Visible')
        
        """
        Step 07:Hover over the point on the left line for BMW.
        Select Remove Filter.Expect to see the original Line Chart with all lines restored.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g1!mmarker!', select_tooltip='Remove Filter', msg='Step 7.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(4)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g0!mmarker!", tooltip_css, 'Remove Filter', element_location='middle', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)         
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 07.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 07.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 07.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 07.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 07.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 07.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 07.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 07.15: Filter Button Removed')

        """
        Step 08:Left-click and draw a box around the points for lines Peugeot, Toyota & Triumph. Select Filter Chart.
        """
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s0!g7!mmarker!")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class='marker!s1!g9!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)
        time.sleep(6)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-30,sy_offset=source_elem['y']-30,tx_offset=target_elem['x']+30,ty_offset=target_elem['y']+10)
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 08.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 08.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.4: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 08.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 08.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 08.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 08.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 08.15: Filter Button Visible')

        """
        Step 09:Hover over the point on the left line for Toyota.Click Exclude Chart.
        Expect to see the following Line Chart with lines for only Peugeot & Triumph.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g1!mmarker!', select_tooltip='Exclude from Chart', msg='Step 9.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g1!mmarker!", tooltip_css, 'Exclude from Chart', element_location='middle', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)  
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 09.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 09.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 09.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['PEUGEOT', 'TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.4: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 09.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 09.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 09.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", True, 'Step 09.15 Filter Button Visible')
        
        """
        Step 10:Hover over the point on the left line for Triumph.Select Remove Filter.
        Expect to see the original Line Chart with all lines restored.        
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g1!mmarker!', select_tooltip='Remove Filter', msg='Step 10.1 : seleted marker tooltip')
#         css="#MAINTABLE_wbody0 .chartPanel"
#         move=driver.find_element_by_css_selector(css)
#         utillobj.click_on_screen(move, 'bottom_middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(4)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s1!g1!mmarker!", tooltip_css, 'Remove Filter', element_location='bottom_middle', javascript_marker_enable=True, mouse_duration=3.5)
        time.sleep(5)  
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 11.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 11.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 11.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 11.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 10.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 11.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 11.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 11.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 11.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.verify_object_visible("#MAINTABLE_0 .arChartMenuBar div[title][onclick*='Filter']", False, 'Step 11.15: Filter Button Removed')
        
        """
        Step 11:Close the chart.
        Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        utillobj.infoassist_api_logout()  
        time.sleep(5) 
         
if __name__ == '__main__':
    unittest.main()