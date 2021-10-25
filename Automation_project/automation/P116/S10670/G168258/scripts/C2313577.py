'''
Created on Oct 12, 2017

@author: Praveen Ramkumar
Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313577
TestCase Name =  AHTML: Vertical Dual-Axis Clustered Bar Chart Additional bucket functionality.

'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2313577_TestClass(BaseTestCase):

    def test_C2313577(self):
        
        Test_Case_ID="C2313577"
        """
        TESTCASE VARIABLES
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        time_out = 30
        
        """
        Step 01:Open FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FVertical_Cluster_Bar.fex&tool=Chart
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Vertical_Cluster_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 01.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.5a : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 01.5b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 01.5c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.6: Verify legend")
           
        """
        Step 02: Click the Run button.
         Expect to see the following Vertical Dual-Axis Clustered Bar Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 02.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 02.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.6b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.9:c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
           
        """
           Step 03: Drag field SALES to the Tooltip bucket.
            Expect to see the following Preview pane with SALES under the Tooltip bucket.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1,'Tooltip',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='SALES', expire_time=time_out)
        metadataobj.verify_query_pane_field('Tooltip','SALES',1,"Step 03.1: Verify query pane")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 03.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 03.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 03.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 03.5a : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 03.5b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 03.5c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify legend")
           
        """
           Step 04: Click the Run button.
            Hove over the blue bar for Audi.
            Expect to see the Sales field added to the Tooltip information for Car & Dealer_Cost.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by CAR", "Step 04.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 04.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!ay2!mbar!", "pale_green", "Step 04.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 04.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 04.6b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 04.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.7: Verify legend")
        time.sleep(5)
        expected_tooltip_list=['CAR:AUDI', 'DEALER_COST:5,063', 'SALES:7800', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g1!mbar!", expected_tooltip_list, "Step 04.8: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
           
        """
           Step 05:  Drag the field COUNTRY to the Color BY bucket.
            Expect to see the following Preview pane with COUNTRY under the Color BY bucket.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY',1, 'Color',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='COUNTRY', expire_time=time_out)
        metadataobj.verify_query_pane_field('Color BY','COUNTRY',1,"Step 05.1: Verify query pane")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 05.2a: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 05.2b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 05.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue1", "Step 05.3: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s4!g0!ay2!mbar!", "brick_red", "Step 05.3: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!ay2!mbar!", "bar_green", "Step 05.3: Verify  riser color")        
        legend=['DEALER_COST : ENGLAND', 'LENGTH : ENGLAND', 'DEALER_COST : FRANCE', 'LENGTH : FRANCE', 'DEALER_COST : ITALY', 'LENGTH : ITALY', 'DEALER_COST : JAPAN', 'LENGTH : JAPAN', 'DEALER_COST : W GERMANY', 'LENGTH : W GERMANY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 05.4: Verify legend")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 05.5a : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 05.5b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 05.5c : Verify yaxis title", custom_css="text[class='y2axis-title']")
          
        """
           Step 06:  Click the Run button. Hover over the blue bar for Jaguar.
            Expect to see the Country field added to the Tooltip information.
            Also expect to see the Country legend on the right-side of the chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by COUNTRY, CAR", "Step 06.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 06.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "lochmara", "Step 06.5: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g0!ay2!mbar!", "brick_red", "Step 06.5: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g7!ay2!mbar!", "med_green", "Step 06.5: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 06.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 06.6b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 06.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=['DEALER_COST:ENGLAND', 'LENGTH:ENGLAND', 'DEALER_COST:FRANCE', 'LENGTH:FRANCE', 'DEALER_COST:ITALY', 'LENGTH:ITALY', 'DEALER_COST:JAPAN', 'LENGTH:JAPAN', 'DEALER_COST:W GERMANY', 'LENGTH:W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.7: Verify legend")
        time.sleep(5)
        expected_tooltip_list=['CAR:JAGUAR', 'DEALER_COST:18,621', 'COUNTRY:ENGLAND', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 06.8: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.9c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
           
        """
           Step 07:  Delete the field COUNTRY from the Color BY bucket.Drag the field SEATS to the Mutli-graph bucket.
            Expect to see the following Preview pane with COUNTRY removed from the Color BY bucket and SEATS added to the Multi-graph bucket.
            Notice the order of the bars in the Preview pane, they are no longer in CAR order.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.querytree_field_click("COUNTRY",1,1,"Delete")
        time.sleep(2)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SEATS', 1,'Multi-graph',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='SEATS', expire_time=time_out)
        metadataobj.verify_query_pane_field('Multi-graph','SEATS',1,"Step 07.1: Verify query pane")
        expected_xval_list=['ALFA ROMEO','JAGUAR','MASERATI','TRIUMPH']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K','28K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 07.2a: Verify XY labels")
        expected_yval2_list=['0', '50', '100', '150', '200','250','300','350','400']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 07.2b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 07.3: Verify legend")
        resobj.verify_number_of_riser("TableChart_1", 1, 8, 'Step 07.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 07.5a: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 07.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 07.6b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 07.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
          
        """
           Step 08:  Click the Run button.Expect to see the following Bar Chart. 
            The order of the bars is no longer in CAR order but in order of SEATS.
        """
          
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by CAR", "Step 08.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH','BMW','DATSUN','JENSEN','TOYOTA','AUDI','PEUGEOT']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 08.4a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 08.4b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 08.4 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "lochmara", "Step 08.5: Verify  riser color")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.6: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.7a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.7b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.7c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 08.8: Verify the total number of risers displayed on preview')
          
        """
           Step 09:  Hover over the blue bar for Alfa Romeo.Expect to see the value of 2 for SEATS.
            The bars with 2 Seats are sorted by Car, ending with Triumph, the last Car with 2 Seats.
        """
        time.sleep(5)
        expected_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 09.1: Verify bar value")
          
        """
           Step 10:  Hover over the blue bar for BMW.Expect to see a value of 4 for SEATS.
                BMW thru Toyota all have 4 Seats.
        """
        time.sleep(5)
        expected_tooltip_list=['SEATS:4', 'CAR:BMW', 'DEALER_COST:49,500', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 10.1: Verify bar value")
          
        """
           Step 11:  Hover over the blue bar for Peugeot.Expect to see a value of 5 for SEATS.
            Both Audi & Peugeot have 5 Seats.
        """
        time.sleep(5)
        expected_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g9!mbar!", expected_tooltip_list, "Step 11.1: Verify bar value")
          
        """
           Step 12:  Delete the field SEATS from the Multi-graph bucket.Drag the field BODYTYPE to the Animate bucket.
            Expect to see the following Preview pane with a slider added for Bodytype at the top.
        """
        utillobj.switch_to_default_content(pause=3)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='SEATS', expire_time=time_out)
        metadataobj.querytree_field_click("SEATS",1,1,"Delete")
        time.sleep(5)
        metadataobj.drag_drop_data_tree_items_to_query_tree('BODYTYPE', 1,'Animate',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='BODYTYPE', expire_time=time_out)
        resobj.verify_number_of_riser("TableChart_1", 1, 2, 'Step 12.1: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "lochmara", "Step 12.2a: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 12.3a: Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 12.3b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 12.3c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        expected_xval_list=['JAGUAR']
        expected_yval1_list=['0', '2,000', '4,000', '6,000', '8,000', '10,000']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 12.4a: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 12.4b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 12.5: Verify legend")
        utillobj.verify_object_visible("#TableChart_1 rect[class='sliderBody']",True,"Step 12.6: verify slider object visible")

        """
           Step 13:  Click the Run button.Expect to see the following Bar Chart with the slider set to the default value of Convertible and only Jaguar displaying.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 2, 'Step 13.1: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue1", "Step 13.2a: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 13.3a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 13.3b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 13.3c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        expected_xval_list=['JAGUAR']
        expected_yval1_list=['0', '2,000', '4,000', '6,000', '8,000', '10,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 13.4a: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 13.4b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 13.5: Verify legend")
        utillobj.verify_object_visible("#MAINTABLE_wbody0_f rect[class='sliderBody']",True,"Step 13.6: verify slider object visible")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by BODYTYPE, CAR", "Step 13.7: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 13.8a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 13.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 13.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
     
        """
           Step 14:  Move the slider to Coupe.Hover over the blue bar for Maserati.
                Expect to see the following Bar Chart with the slider indicating a Bodytype of Coupe and only Alfa Romeo and Maserati bars appearing.
                    Also verify that the Tooltip value for Bodytype is Coupe.
        """
        time.sleep(5)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'middle', click_type=0, x_offset=-300)  
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,4, 'Step 14.1: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue1", "Step 14.2a: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 14.3a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 14.3b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 14.3c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        expected_xval_list=['ALFA ROMEO','MASERATI']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K','28K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 14.4a: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 14.4b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 14.5: Verify legend")
        utillobj.verify_object_visible("#MAINTABLE_wbody0_f rect[class='sliderBody']",True,"Step 14.6: verify slider object visible")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by BODYTYPE, CAR", "Step 14.7: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 14.8a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 14.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 14.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        expected_tooltip_list=['BODYTYPE:COUPE', 'CAR:MASERATI', 'DEALER_COST:25,000', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 14.9: Verify bar value")
                
        """
           Step 15: Move the slider all the way to Sedan.Expect to see the following Bar Chart with the slider set to the last value of Sedan.
            8 Cars have at least one Bodytype of Sedan.
        """
        time.sleep(5)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'right', click_type=0, x_offset=-15)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 16, 'Step 15.1: Verify the total number of risers displayed on run window')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!", "bar_blue1", "Step 15.2: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 15.3a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 15.3b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 15.3c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        expected_xval_list=['JAGUAR','ALFA ROMEO','AUDI','BMW','DATSUN','JENSEN','PEUGEOT','TOYOTA']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 15.4a: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 15.4b: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 15.5: Verify legend")
        utillobj.verify_object_visible("#MAINTABLE_wbody0_f rect[class='sliderBody']",True,"Step 15.6: verify slider object visible")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH, SALES by BODYTYPE, CAR", "Step 15.7: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 15.8a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 15.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 15.8c: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
           Step 16: Close chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp comment
        """
        time.sleep(3)
       
if __name__ == '__main__':
    unittest.main()