'''
Created on Nov 13, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313695
TestCase Name = AHTML: Horizontal Dual-Axis Absolute Line Chart Active Control icon functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity
from common.wftools import visualization

class C2313695_TestClass(BaseTestCase):

    def test_C2313695(self):
        
        Test_Case_ID="C2313695"
        """
            TESTCASE VARIABLES
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        visobj = visualization.Visualization(self.driver)
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Absolute_Line.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.

        """
        utillobj.infoassist_api_edit("Horizontal_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K',]
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 01.03 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 01.04: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 01.05: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 01.06: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 01.07: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 01.08: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")


        """
            Step 02:Click the Run button.Expect to see the following Horizontal Dual-Axis Absolute Line Chart.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 02.06: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g0!mmarker', expected_tooltip_list, 'Step 02.07: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.08: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.09: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
   
        """
            Step 03:Using the first icon at the top of the chart, select More Options, then select Chart/Rollup Tool.
            Expect to see the following Chart/Rollup Tool options.
        """
          
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Chart/Rollup Tool',0,custom_css='cpop')
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
         
        """
            Step 04:Select the Column Chart option.Click OK.
            Expect to see the Horizontal Dual-axis Absolute Line chart converted into a Vertical Dual-axis bar chart.
        """
           
        rollupobj.select_advance_chart('wall1', 'column')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 04.03: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 04.04: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.05: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.07: Verify  riser color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.08: Verify legend")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 04.09: Verify bar value")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 04.10: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
           
        """
            Step 05:Using the third icon at the top, click Original Chart.
            Expect to see the Vertical Dual-axis Column chart converted back into the original Horizontal Dual-axis Line chart.      
        """
           
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.06: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g0!mmarker', expected_tooltip_list, 'Step 05.07: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.08: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.09: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 05.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
     
        """
            Step 06:Using the second icon at the top,click Advanced Chart.
            Expect to see the following Chart/Rollup Tool options.       
        """
           
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        """
            Step 07:Select the Column Depth option.Click OK.
            Expect to see the Horizontal Line chart converted into a Column Depth bar chart.
            Verify the presence of both axis.
        """
           
        rollupobj.select_advance_chart('wall1', 'columndepth')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 07.03: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 07.04: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 07.05: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 07.06: Verify the total number of risers displayed on preview')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.07: Verify legend")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 07.08: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.09: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)

        """
            Step 08:Hover over the left(blue) bar for Alfa Romeo.
            Hover over the right(green) bar for Alfa Romeo.
            Expect to see the following Tooltip information for Dealer_Cost for Alfa Romeo.
            Expect to see the following Tooltip information for Length for Alfa Romeo.
        """
           
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.chartPanel > g:nth-child(2) g:nth-child(1) > rect")
        utillobj.click_on_screen(parent_obj,'middle')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 08.01: Verify bar value",default_move=True) 
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.chartPanel > g:nth-child(2) g:nth-child(3) > rect")
        utillobj.click_on_screen(parent_obj,'middle')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'LENGTH:510', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 08.02: Verify bar value")
           
           
        """
            Step 09:Using the second icon at the top,click Advanced Chart. 
            Scroll down and select the Curved Line option.Click OK.
            Expect to see the Column Depth Dual-axis bar chart converted into a Curved Line Chart, with Dual axis.
        """
           
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'curvedline')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 09.03: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 09.04: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 09.05: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 09.06: Verify Number of riser', custom_css="path[class^='riser']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.07: Verify legend")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 09.08: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.09: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
           
        """
            Step 10:Hover over the point in the blue line for Alfa Romeo.Hover over the point in the green line for Alfa Romeo.
            Expect to see the following Tooltip information for Dealer_Cost for Alfa Romeo.
            Expect to see the following Tooltip information for Length for Alfa Romeo.
        """
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.chartPanel > g:nth-child(2) g:nth-child(1) > rect")
        utillobj.click_on_screen(parent_obj,'middle')
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 10.01: Verify tooltip')
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'LENGTH:  510', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s1!g0!mmarker!', expected_tooltip_list, 'Step 10.02: Verify tooltip') 
           
        """
            Step 11:Using the second icon at the top,click Advanced Chart. 
            Scroll down and select the Donut(Cylinder) option.Click OK.
            Expect to see the Vertical Dual-axis bar chart converted into two PIE charts, one for Dealer_Cost and one for Length. Dual axis does not apply to PIE charts.
        """ 
         
        time.sleep(8)
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)       
        rollupobj.select_advance_chart('wall1', 'dountcylinder')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ["DEALER_COST","LENGTH"], "Step 11.01:",same_group=True)
        expected_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 11.02: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 11.03: Verify first bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 11.04: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.05: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 40, "Step 11.08: Verify number of pie", custom_css=".chartPanel path[class*='riser!s']")
        resobj.verify_data_labels('MAINTABLE_wbody0', ['144K','3,248'], "Step 11.09: verify total lable ", custom_css=".chartPanel g text[class*='totalLabel']")
        resobj.verify_data_labels('MAINTABLE_wbody0', ["DEALER_COST","LENGTH"], "Step 11.10: verify total lable ", custom_css=".chartPanel g text[class*='pieLabel']")
           
        """
           Step 12:Click the third icon at the top.Expect to see the original Vertical Dual-Axis Absolute Line Chart.
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 12.01: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 12.02: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 12.03: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 12.04: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 12.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 12.06: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 12.07: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 12.08: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 12.09: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 12.10: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.11: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
            Step 13:Using the first icon at the top of the chart, select More Options, then select Export/Excel.
            Click OK to any ActiveX messages.Open the Excel file just created.
            Expect to see the following Excel sheet appear with a summary report and a Vertical Line chart.
        """
        
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' :
            rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Export to->Excel',0,custom_css='cpop')
            time.sleep(8)
            utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step_13','actual', left=0, top=0, right=0, bottom=40)
            utillobj.saveas_excel_sheet(Test_Case_ID+'_DS11_.xlsx')
            time.sleep(4)
            utillobj.verify_excel_sheet(Test_Case_ID+'_DS11_.xlsx', Test_Case_ID+'_DS11_.xlsx', 'Sheet1', 'Step 13.01: Expect to see the Excel spreadsheet')
        else :
            print("Export option available only in IE browser")
            
        """
            Step 14:Close the Excel spreadsheet.
            Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__=='__main__' :
    unittest.main()