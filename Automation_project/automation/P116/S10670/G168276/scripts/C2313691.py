'''
Created on Nov 10, 2017

@author: praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313691
TestCase Name = AHTML: Vertical Dual-Axis Absolute Line Chart Active Control icon functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,active_chart_rollup
from common.lib import utillity

class C2313691_TestClass(BaseTestCase):

    def test_C2313691(self):
        
        Test_Case_ID="C2313691"
        """
            TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FVertical_Absolute_Line.fex&tool=Chart
                Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Vertical_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
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
            Step 02:Click the Run button.Expect to see the following Vertical Dual-Axis Absolute Line Chart.
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
        time.sleep(5)
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker', expected_tooltip_list, 'Step 02.7: Verify tooltip')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
   
        """
            Step 03:Using the first icon at the top of the chart, select More Options, then select Chart/Rollup Tool.Expect to see the following Chart/Rollup Tool options.
        """
          
        rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Chart/Rollup Tool',0,custom_css='cpop')
        time.sleep(3)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"Base_Step_03")
        time.sleep(1)
          
        """
            Step 04:Select the Bar Chart option.Click OK.
            Expect to see the Vertical Dual-axis Absolute Line Chart converted into a Horizontal Dual-axis Bar Chart.
        """
          
        rollupobj.select_advance_chart('wall1', 'bar')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 04.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 04.3a: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.3b: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.5: Verify  riser color")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.6: Verify legend")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 04.7: Verify bar value")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 04.8: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
   
        """
            Step 05:Using the third icon at the top, click Original Chart.
        Expect to see the Horizontal Dual-axis bar chart converted back into the original 
        Vertical Dual-axis Absolute Line chart.        
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 05.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.6: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 05.7: Verify tooltip')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
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
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_06")
          
          
        """
            Step 07:Select the Column Depth option.Click OK.
            Expect to see the Vertical Dual-axis Line chart converted into a Column Depth bar chart.
            Verify the presence of both axis.
        """
          
        rollupobj.select_advance_chart('wall1', 'columndepth')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 07.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 07.3b: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 07.3c: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 07.4: Verify the total number of risers displayed on preview')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.5: Verify legend")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 07.6: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_07', image_type='actual',x=1, y=1, w=-1, h=-1)
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
        time.sleep(2)
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 08.1: Verify bar value",default_move=True) 
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.chartPanel > g:nth-child(2) g:nth-child(3) > rect")
        utillobj.click_on_screen(parent_obj,'middle')
        time.sleep(5)  
        expected_tooltip_list=['CAR:ALFA ROMEO', 'LENGTH:510', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0", "riser!s1!g0!mbar!", expected_tooltip_list, "Step 08.2: Verify bar value")
          
        """
            Step 09:Using the second icon at the top,click Advanced Chart. 
            Scroll down and select the Currved Line Chart option.Click OK.
            Expect to see the Column Depth bar chart converted into a Curved Line Chart, with Dual axis.
        """
          
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        time.sleep(3)
        rollupobj.select_advance_chart('wall1', 'curvedline')
        time.sleep(3)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 09.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 09.3b: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 09.3c: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 07.6: Verify Number of riser', custom_css="path[class^='riser']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.5: Verify legend")
        miscelaneousobj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 09.6: Verify chart title ")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.7: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.8: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.9: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step_07', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)
          
        """
            Step 10:Hover over the point in the blue line for Audi.
                Hover over the point in the green line for Audi.
                Expect to see the following Tooltip information for Dealer_Cost for Audi.
                Expect to see the following Tooltip information for Length for Audi.
        """
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parent_obj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 g.chartPanel > g:nth-child(2) g:nth-child(1) > rect")
        utillobj.click_on_screen(parent_obj,'middle')
        time.sleep(2)
        expected_tooltip_list=['CAR:  AUDI', 'DEALER_COST:  5,063', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g1!mmarker!', expected_tooltip_list, 'Step 10.1: Verify tooltip')
        time.sleep(5)
        expected_tooltip_list=['CAR:  AUDI', 'LENGTH:  187', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s1!g1!mmarker!', expected_tooltip_list, 'Step 10.2: Verify tooltip')
         
        """
            Step 11:Using the second icon at the top,click Advanced Chart. Scroll down and select the DONUT option.
            Click OK.Expect to see the Vertical Dual-axis Curved Line chart converted into two DONUT charts, one for Dealer_Cost and one for Length. 
            Dual axis does not apply to PIE charts.
        """
         
        time.sleep(8)
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 1)
        parent_css="#wall1"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        element= driver.find_element_by_css_selector("#wall1")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_11")
        time.sleep(3)        
        rollupobj.select_advance_chart('wall1', 'donutbevel')
        time.sleep(3)
        resobj.verify_riser_pie_labels_and_legends('MAINTABLE_wbody0', ["DEALER_COST","LENGTH"], "Step 11.1:",same_group=True)
        expected_label_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 11.2: Verify pie lablesList')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mwedge!", "bar_blue", "Step 11.3: Verify first bar color")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 11.4: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 11.5: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 11.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 11.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 20, "Step 11.8: Verify number of pie", custom_css=".chartPanel path[class*='riser!s']")
        resobj.verify_data_labels('MAINTABLE_wbody0', ['144K','3,248'], "Step 11.9: verify total lable ", custom_css=".chartPanel g text[class*='totalLabel']")
        resobj.verify_data_labels('MAINTABLE_wbody0', ["DEALER_COST","LENGTH"], "Step 11.10: verify total lable ", custom_css=".chartPanel g text[class*='pieLabel']")
     
     
        """
           Step 12:Click the third icon at the top.Expect to see the original Vertical Dual-Axis Absolute Line Chart.
       """
         
        rollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 12.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 12.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 12.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 12.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 12.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 12.6: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 12.7: Verify tooltip')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 12.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 12.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 12.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 12.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 12.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 12.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 12.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
            Step 13:Using the first icon at the top of the chart, select More Options, then select Export/Excel.
            Click OK to any ActiveX messages.Open the Excel file just created.
            Expect to see the following Excel sheet appear with a summary report and a Vertical Bar chart.
        """
        
        browser=utillobj.parseinitfile('browser')
        if browser=='IE' :
            rollupobj.select_chartmenubar_option('MAINTABLE_wmenu0',0,'Export to->Excel',0,custom_css='cpop')
            time.sleep(8)
            utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step_02','actual', left=0, top=0, right=0, bottom=40)
            utillobj.saveas_excel_sheet(Test_Case_ID+'_DS11_.xlsx')
            time.sleep(4)
            utillobj.verify_excel_sheet(Test_Case_ID+'_DS11_.xlsx', Test_Case_ID+'_DS11_.xlsx', 'Sheet1', 'Step 10: Expect to see the Excel spreadsheet')
        else :
            print("Export option available only in IE browser")

        """
            Step 14:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__=='__main__' :
    unittest.main()