'''
Created on Nov 15, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313696
TestCase Name = AHTML: Horizontal Dual-Axis Absolute Line Chart Additional bucket functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity
from common.wftools import visualization

class C2313696_TestClass(BaseTestCase):

    def test_C2313696(self):
        
        Test_Case_ID="C2313696"
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
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        visobj = visualization.Visualization(self.driver)

        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Absolute_Line.fex&tool=Chart
                    
                    Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
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
            Step 02:Click the Run button.
                     
                    Expect to see the following Horizontal Dual-Axis Absolute Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
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
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g0!mmarker', expected_tooltip_list, 'Step 02.7: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
            Step 03:Drag field SALES to the Tooltip bucket.
                     
                    Expect to see the following Preview pane with SALES under the Tooltip bucket.
        """
        
        utillobj.switch_to_default_content(pause=2)
        
        metadataobj.datatree_field_click('SALES', 1, 1, 'Add To Query', 'Tooltip')
#         metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip',0)
        parent_css="#queryTreeWindow table tr:nth-child(16) td"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Tooltip', 'SALES', 1, "Step 02:")
 
        """
            Step 04:Click the Run button.
                    Hove over the point on the left line for Audi.
                 
                Expect to see the Sales field added to the Tooltip information for Car & Dealer_Cost.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 03.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 03.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 03.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 03.6: Verify Number of riser', custom_css="path[class^='riser']")
        expected_tooltip_list=['CAR:  AUDI', 'DEALER_COST:  5,063', 'SALES:  7800', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g1!mmarker!', expected_tooltip_list, 'Step 03.7: Verify tooltip')        
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 03.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 03.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH, SALES by CAR', 'Step 03.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
            Step 05:Drag the field COUNTRY to the Vertical axis above the CAR field.
                    Also drag the field COUNTRY to the Color by bucket.
     
                Expect to see the following Preview pane with COUNTRY under the Color by bucket and COUNTRY added above CAR in the Vertical axis bucket.
 
                Note: The breaks on some of the Country/Car combinations occurs because there is only one point and 2 or more are needed to make a line.
        """
        
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Vertical Axis',0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True, expire_time=20)
        
        metadataobj.verify_query_pane_field('Vertical Axis', 'COUNTRY', 1, "Step 05.1:")
        metadataobj.datatree_field_click('COUNTRY', 1, 1, 'Add To Query', 'Color')
#         metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Color',0)
        parent_css="#queryTreeWindow table tr:nth-child(15) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True,expire_time=20)
        
        metadataobj.verify_query_pane_field('Vertical Axis', 'COUNTRY', 1, "Step 05.2:")
        expected_xval_list=['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT','ITALY : ALFA ROMEO','ITALY : MASERATI','JAPAN : DATSUN','JAPAN : TOYOTA','W GERMANY : AUDI','W GERMANY : BMW']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K',]
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 05.3: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 05.4: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "COUNTRY : CAR","Step 05.5: Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 05.6: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 05.7: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 10, 'Step 05.8: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s8!g0!mline!", "moss_green", "Step 05.9: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s9!g0!mline!", "pale_yellow1", "Step 05.8: Verify line2 color",attribute_type='stroke')
        legend=['DEALER_COST : ENGLAND','LENGTH : ENGLAND','DEALER_COST : FRANCE','LENGTH : FRANCE','DEALER_COST : ITALY','LENGTH : ITALY','DEALER_COST : JAPAN','LENGTH : JAPAN','DEALER_COST : W GERMANY','LENGTH : W GERMANY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 05.9: Verify legend")
 
        """
            Step 06:Click the Run button. 
                    Hover over the left point on the line for England/Triumph.
                     
                    Expect to see the Country field added to the Tooltip information twice, once as a sort and once as a Color by field.
                    Also expect to see the Country legend on the right-side of the chart.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'COUNTRY : CAR', "Step 06.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 06.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 06.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT','ITALY : ALFA ROMEO','ITALY : MASERATI','JAPAN : DATSUN','JAPAN : TOYOTA','W GERMANY : AUDI','W GERMANY : BMW']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 10, 'Step 06.6: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
        expected_tooltip_list=['COUNTRY:  ENGLAND', 'CAR:  TRIUMPH', 'DEALER_COST:  4,292', 'COUNTRY:  ENGLAND', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g2!mmarker!', expected_tooltip_list, 'Step 06.7: Verify tooltip')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s8!g0!mline!", "moss_green", "Step 06.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s9!g0!mline!", "pale_yellow1", "Step 06.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST : ENGLAND','LENGTH : ENGLAND','DEALER_COST : FRANCE','LENGTH : FRANCE','DEALER_COST : ITALY','LENGTH : ITALY','DEALER_COST : JAPAN','LENGTH : JAPAN','DEALER_COST : W GERMANY','LENGTH : W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH, SALES by COUNTRY, COUNTRY, CAR', 'Step 06.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
 
        """
            Step 07:Delete the field COUNTRY from the Color by bucket and from the Vertical axis bucket.
                    Drag the field SEATS to the Mutli-graph bucket.
                 
                Expect to see the following Preview pane with COUNTRY removed from the Color by bucket and SEATS added to the Multi-graph bucket.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.querytree_field_click('COUNTRY', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.querytree_field_click('COUNTRY', 1, 1, "Delete")
        time.sleep(1)
        metadataobj.datatree_field_click('SEATS', 1, 1, 'Add To Query', 'Multi-graph')
#         metadataobj.drag_drop_data_tree_items_to_query_tree('SEATS', 1, 'Multi-graph',0)
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='SEATS', with_regular_exprestion=True, expire_time=20)
        
        metadataobj.verify_query_pane_field('Multi-graph', 'SEATS', 1, "Step 07:1")
        time.sleep(2)
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K','28K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 07.1: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300', '350', '400']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 07.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 07.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 07.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 07.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 07.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 07.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 07.8: Verify line2 color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 07.9: Verify legend")
         
        """
            Step 08:Click the Run button.
                     
                    Expect to see the following Line Chart. The order of the lines is no longer in CAR order but in order of SEATS. The top 4 Cars all have 2 Seats.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 08.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 08.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 08.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH', 'BMW', 'DATSUN', 'JENSEN', 'TOYOTA', 'AUDI', 'PEUGEOT']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 08.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 08.7: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 08.8: Verify  2nd bar color",attribute_type='stroke')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH, SALES by CAR', 'Step 08.9: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
 
        """
            Step 09:Hover over the point on the left line for Alfa Romeo.
                    Expect to see the value of 2 for SEATS.
                     
                    Hover over the blue bar for Triumph
                    The lines with 2 Seats are sorted by Car, ending with Triumph, the last Car with 2 Seats.
        """
        expected_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g0!mmarker', expected_tooltip_list, 'Step 09.1: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        time.sleep(5)
        expected_tooltip_list=['SEATS:2', 'CAR:TRIUMPH', 'DEALER_COST:4,292', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g3!mmarker', expected_tooltip_list, 'Step 09.1: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
 
 
        """
            Step 10:Hover over the point on the left line for BMW.
                     
                    Expect to see a value of 4 for SEATS.BMW thru Toyota all have 4 Seats.
        """
        expected_tooltip_list=['SEATS:  4', 'CAR:  BMW', 'DEALER_COST:  49,500', 'SALES:  80390', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g4!mmarker!', expected_tooltip_list, 'Step 10.1: Verify tooltip')
        time.sleep(5)
        expected_tooltip_list=['SEATS:  4', 'CAR:  TOYOTA', 'DEALER_COST:  2,886', 'SALES:  35030', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g7!mmarker!', expected_tooltip_list, 'Step 10.2: Verify tooltip')
 
 
        """
            Step 11:Hover over the point on the left line for Peugeot.
                     
                    Expect to see a value of 5 for SEATS.Both Audi & Peugeot have 5 Seats.
        """
        expected_tooltip_list=['SEATS:  5', 'CAR:  PEUGEOT', 'DEALER_COST:  4,631', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g9!mmarker!', expected_tooltip_list, 'Step 11.1: Verify tooltip')
        time.sleep(5)
        expected_tooltip_list=['SEATS:  5', 'CAR:  AUDI', 'DEALER_COST:  5,063', 'SALES:  7800', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g8!mmarker!', expected_tooltip_list, 'Step 11.2: Verify tooltip')
 
        """
            Step 12:Delete the field SEATS from the Multi-graph bucket.
                    Drag the field COUNTRY to the Animate bucket.
                 
                Expect to see the following Preview pane with a slider added for Country at the top.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.querytree_field_click('SEATS', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Animate',0)
        parent_css="#queryTreeWindow table tr:nth-child(19) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True)
        time.sleep(5)
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 12.1: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300', '350', '400', '450']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 12.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 12.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 12.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 12.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 12.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 12.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 12.8: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('TableChart_1', expected_datalabel, "Step 12.9", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#TableChart_1 .sliderContainer", True, "Step 12.10: Slider Visible")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 12.11: Verify legend")
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_12")
        time.sleep(1)


        """
            Step 13:Click the Run button.
                    
                    Expect to see the following Line Chart with the slider set to the default value of England and Cars of Jaguar, Jensen & Triumph displaying.
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 13.1: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200', '250', '300', '350', '400', '450']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 13.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 13.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 13.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 13.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 13.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 13.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 13.8: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 13.9 verify slider labels", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 13.10: Slider Visible")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 13.11: Verify legend")
        expected_tooltip_list=['COUNTRY:  ENGLAND', 'CAR:  TRIUMPH', 'DEALER_COST:  4,292', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g2!mmarker!', expected_tooltip_list, 'Step 13.12: Verify tooltip')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_13")
        time.sleep(1)

        """        
            Step 14:Move the slider to Italy.                    
                    Hover over the blue bar for Maserati.
                
                Expect to see the following Line Chart with the slider indicating a Country of Italy and only Alfa Romeo and Maserati lines appearing.
                Also verify that the Tooltip value for Country is Italy.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'middle', click_type=0)
        time.sleep(5)
        expected_tooltip_list=['COUNTRY:  ITALY', 'CAR:  MASERATI', 'LENGTH:  177', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s1!g5!mmarker!', expected_tooltip_list, 'Step 14.1 : Verify tooltip')
        time.sleep(1)
        expected_xval_list=['ALFA ROMEO', 'MASERATI']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K' ,'24K', '28K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 14.2: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500', '600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 14.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 14.4 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 14.5: Verify -yAxis Title") 
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 14.6: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 14.7: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 14.8: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 14.9: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 14.10", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 14.11: Slider Visible")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 14.13: Verify legend")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_14")
        time.sleep(1)

        """
            Step 15:Move the slider all the way to the right to W Germany.
                    
                    Expect to see the following Line Chart with the slider set to the last value of W Germany.Cars Audi & BMW should be displayed.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'right', click_type=0, x_offset=-15)
        time.sleep(2)        
        expected_tooltip_list=['COUNTRY:  W GERMANY', 'CAR:  AUDI', 'DEALER_COST:  5,063', 'SALES:  7800', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g8!mmarker!', expected_tooltip_list, 'Step 15: Verify tooltip')
        time.sleep(1)
        expected_xval_list=['AUDI', 'BMW']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 15.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 15.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 15.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 15.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 15.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 15.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 15.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 15.8: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 15.9: verify slider value", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 15.10: Slider Visible")
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 15.11: Verify legend")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_15")
        time.sleep(1)        

        """
            Step 16:Close the chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        
        """
        
        
if __name__ == '__main__':
    unittest.main()   