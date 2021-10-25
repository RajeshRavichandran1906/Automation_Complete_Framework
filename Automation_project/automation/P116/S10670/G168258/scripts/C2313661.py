'''
Created on Sep 15, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313661
TestCase Name=AHTML: Horizontal Dual-Axis Stacked Bar Chart Additional bucket functionality.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.pages import visualization_metadata, visualization_ribbon, visualization_resultarea, active_miscelaneous

class C2313661_TestClass(BaseTestCase):
    
    def test_C2313661(self):
        
        """
        TEST OBJECTS 
        """        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
            Step 1: Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Bar.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Bar", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')        
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 75)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 01.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 01.05: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 01.06: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 01.07: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.08 : Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
        
        """
            Step 2: Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         utillobj.synchronize_until_element_is_visible("[id^='ReportIframe']", 30)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'CAR', 20)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 02.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.04: Verify Xaxis title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 02.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.06: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 02.07: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 02.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 02.09: Verify  riser color")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.11: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.12: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.13: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
             
        """
            Step 03 : Drag field SALES to the Tooltip bucket.
        """  
        utillobj.switch_to_default_content(pause=3) 
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip',0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow", 'SALES', 20)
        metadataobj.verify_query_pane_field('Tooltip','SALES',1,"Step 03:01 :Verify Tooltip sales")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 03.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 03.05: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 03.06: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 03.07: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 03.08: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 03.09 : Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.10: Verify legend")
        
        """
            Step 04 : Click the Run button.
            Step 04:01: Hover over the lower left bar for Alfa Romeo.
            Step 04:02 :Expect to see the Sales field added to the Tooltip information for Car & Dealer_Cost.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         utillobj.synchronize_until_element_is_visible("[id^='ReportIframe']", 30)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'CAR', 20)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by CAR", "Step 04.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 04.04 : Verify Xaxis title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 04.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 04.06: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 04.07: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 04.08: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 04.09: Verify  riser color")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.10: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 04.11: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            
        """
            Step 05 : Drag the field COUNTRY to the Color BY bucket.
        """
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Color',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, 'COUNTRY', 20)
        metadataobj.verify_query_pane_field('Color BY','COUNTRY',1,"Step 05.01: Verify query pane")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue1", "Step 05.02 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g5!ay2!mbar!", "dark_green", "Step 05.03 : Verify bar color")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 05.04: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200','1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 05.05: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 05.06: Verify the total number of risers displayed on preview')
        legend=['DEALER_COST : ENGLAND', 'WEIGHT : ENGLAND', 'LENGTH : ENGLAND', 'HEIGHT : ENGLAND', 'DEALER_COST : FRANCE', 'WEIGHT : FRANCE', 'LENGTH : FRANCE', 'HEIGHT : FRANCE', 'DEALER_COST : ITALY', 'WEIGHT : ITALY', 'LENGTH : ITALY', 'HEIGHT : ITALY', 'DEALER_COST : JAPAN', 'WEIGHT : JAPAN', 'LENGTH : JAPAN', 'HEIGHT : JAPAN', 'DEALER_COST : W GERMANY', 'WEIGHT : W GERMANY', 'LENGTH : W GERMANY', 'HEIGHT : W GERMANY']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 05.07: Verify legend")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 05.08 : Verify Xaxis title")
        
        """
            Step 06 : Click the Run button. Hover over the top left bar for Audi.
            Step 06:01 : Expect to see the Country field added to the Tooltip information.
            Also expect to see the Country legend on the right-side of the chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         path_css="[id^='ReportIframe']"
#         utillobj.synchronize_with_number_of_element(path_css, 1, 30)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'CAR', 25)
        legend=['DEALER_COST : ENGLAND', 'WEIGHT : ENGLAND', 'LENGTH : ENGLAND', 'HEIGHT : ENGLAND', 'DEALER_COST : FRANCE', 'WEIGHT : FRANCE', 'LENGTH : FRANCE', 'HEIGHT : FRANCE', 'DEALER_COST : ITALY', 'WEIGHT : ITALY', 'LENGTH : ITALY', 'HEIGHT : ITALY', 'DEALER_COST : JAPAN', 'WEIGHT : JAPAN', 'LENGTH : JAPAN', 'HEIGHT : JAPAN', 'DEALER_COST : W GERMANY', 'WEIGHT : W GERMANY', 'LENGTH : W GERMANY', 'HEIGHT : W GERMANY']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.01:Verify legend")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200','1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 06.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue1", "Step 06.05 : Verify bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g5!ay2!mbar!", "dark_green", "Step 06.06 : Verify bar color")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.07: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.08: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.09: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['CAR:AUDI', 'DEALER_COST:5,063', 'COUNTRY:W GERMANY', 'SALES:7800', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s16!g1!ay2!mbar!", expected_tooltip_list, "Step 06.10: Verify bar value")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 06.11: Verify Xaxis title")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by COUNTRY, CAR", "Step 06.12: Verify chart title ")
        
        """
            Step 07 : Delete the field COUNTRY from the Color BY bucket.
            Drag the field SEATS to the Mutli-graph bucket.
        """
        
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        metadataobj.querytree_field_click("COUNTRY",1,1,"Delete")
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('SEATS', 1, 'Multi-graph',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, 'SEATS', 20)
        
        """
            Step 07:01 :Expect to see the following Preview pane with COUNTRY removed from the Color BY bucket and SEATS added to the Multi-graph bucket.
            Notice the order of the bars in the Preview pane, they are no longer in CAR order.
            Step 07:02: Verify number of preview risers
        """
        metadataobj.verify_query_pane_field('Multi-graph','SEATS',1,"Step 07.01: Verify query pane")
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH']
        expected_y1val_list=['0', '5K', '10K', '15K', '20K', '25K', '30K','35K']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 07.02:')
        expected_y2val_list=['0', '100', '200', '300', '400', '500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_y2val_list, "Step 07.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser('TableChart_1', 1, 16, 'Step 07.04: Verify number of preview risers')
        legend=['DEALER_COST','WEIGHT', 'LENGTH', 'HEIGHT' ]
        resobj.verify_riser_legends('TableChart_1',legend, 'Step 07.05: Verify chart preview legends')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar!", "bar_blue", "Step 07.06 : Verify bar color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mbar!", "bar_green", "Step 07.07 : Verify bar color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 07.08: Verify Xaxis title")

        """
            Step 08 : Click the Run button.
            Step 08:01: Expect to see the following Bar Chart.
            The order of the bars is no longer in CAR order but in order of SEATS, then Car.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         path_css="[id^='ReportIframe']"
#         utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)   
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30) 
        parent_css="#MAINTABLE_wbody0 g.chartPanel g text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(parent_css, 'CAR', 20) 
        expected_xval_list=['ALFA ROMEO','JAGUAR','MASERATI','TRIUMPH','BMW','DATSUN','JENSEN','TOYOTA','AUDI','PEUGEOT']
        expected_y1val_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_y1val_list, 'Step 08.01 :')
        expected_y2val_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_y2val_list, 'Step 08.02 :',y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 40, 'Step 08.03: Verify number of preview risers')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.04: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.05: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.06: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.07: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by CAR", "Step 08.08 : Verify chart title ")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 08.09: Verify Xaxis title")
                
        """
            Step 09: Hover over the lower left bar for Alfa Romeo.
            Expect to see the value of 2 for SEATS
            The bars with 2 Seats are sorted by Car, ending with Triumph, the last Car with 2 Seats.
        """
        expected_tooltip_list=['SEATS:2', 'CAR:ALFA ROMEO', 'LENGTH:510', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s2!g0!ay2!mbar!', expected_tooltip_list, "Step 09.01: Verify bar value")
        expected_tooltip_list=['SEATS:2', 'CAR:TRIUMPH', 'LENGTH:165', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s2!g3!ay2!mbar!', expected_tooltip_list, "Step 09.02: Verify bar value")

        """
            Step 10 : Hover over the lower left bar for BMW.
            Step 10:01 :Expect to see a value of 4 for SEATS.BMW thru Toyota all have 4 Seats.
        """
        expected_tooltip_list=['SEATS:4', 'CAR:BMW', 'LENGTH:1,122', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s2!g4!ay2!mbar!', expected_tooltip_list, "Step 10.01: Verify bar value")
        
        """
            Step 11: Hover over the lower left bar for Peugeot.
            Step 11 : 01 :Expect to see a value of 5 for SEATS.Both Audi & Peugeot have 5 Seats.
        """
        expected_tooltip_list=['SEATS:5', 'CAR:PEUGEOT', 'LENGTH:182', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s2!g9!ay2!mbar!', expected_tooltip_list, "Step 11.01: Verify bar value")        
        
        """
            Step 12 : Delete the field SEATS from the Multi-graph bucket.Drag the field BODYTYPE to the Animate bucket.
            Step 12 : 01 : Expect to see the following Preview pane 
            Step 12 : 02 : Slider added for Bodytype at the top.
        """
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        metadataobj.querytree_field_click("SEATS",1,1,"Delete")
        metadataobj.drag_drop_data_tree_items_to_query_tree('BODYTYPE', 1,'Animate',0)
        parent_css='#queryTreeWindow'
        utillobj.synchronize_with_visble_text(parent_css, 'BODYTYPE', 20)
        utillobj.verify_object_visible("#TableChart_1 rect[class='sliderBody']",True,"Step 12.01: verify slider object visible")
        utillobj.verify_chart_color("pfjTableChart_1", "riser!s0!g4!mbar!", "lochmara", "Step 12.02: 02:bar color")
        expected_xval_list=['JAGUAR']
        expected_y1val_list=['0', '2K', '4K', '6K', '8K', '10K', '12K']
        expected_y2val_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y1val_list, 'Step 12.03 :XY labels')
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_y2val_list, 'Step 12.04:', y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=['DEALER_COST','WEIGHT', 'LENGTH', 'HEIGHT' ]
        resobj.verify_riser_legends('TableChart_1',legend, 'Step 12.05: Verify chart preview legends')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue", "Step 12.06: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s2!g4!ay2!mbar!", "dark_green", "Step 12.07: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 12.08: Verify Xaxis title")
        resobj.verify_number_of_riser('TableChart_1', 1, 4, 'Step 12.09: Verify number of preview risers')
    
        """
            Step 13 : Click the Run button.
            Step 13 : 01 : Expect to see the following Bar Chart with the slider set to the default value of Convertible and only Jaguar displaying.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         path_css="[id^='ReportIframe']"
#         utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)  
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 4, 30)     
        utillobj.synchronize_with_number_of_element("#MAINTABLE_wbody0 svg > g text[class^='xaxis'][class*='labels']", 1, 20)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 4, 'Step 13.01: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!", "bar_blue", "Step 13.02: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!ay2!mbar!", "dark_green", "Step 13.03: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g0!ay2!mbar!", "pale_yellow", "Step 13.04: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mbar!", "pale_green", "Step 13.05: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 13.06: Verify Xaxis title")
        expected_xval_list=['JAGUAR']
        expected_yval1_list=['0', '2K', '4K', '6K', '8K', '10K','12K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 13.07: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240','280']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 13.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 13.09: Verify legend")
        utillobj.verify_object_visible("#MAINTABLE_wbody0_f rect[class='sliderBody']",True,"Step 13.10: verify slider object visible")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by BODYTYPE, CAR", "Step 13.11: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 13.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 13.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 13.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)

        """
            Step 14 : 01: Move the slider to Coupe.
            Hover over the lower left bar for Maserati.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        #utillobj.wait_for_page_loads(10)
#         path_css="[id^='ReportIframe']"
#         utillobj.synchronize_with_number_of_element(path_css, 1, 25)
        utillobj.switch_to_frame(pause=2)  
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 4, 30)       
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'middle', click_type=0, x_offset=-300)  
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1,8, 'Step 14.01: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 14.02: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 14.03: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g2!ay2!mbar!", "pale_yellow", "Step 14.04: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 14.05: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 14.06: Verify Xaxis title")
        expected_xval_list=['ALFA ROMEO','MASERATI']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K','30K','35K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 14.07: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 14.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 14.09: Verify legend")
        expected_tooltip_list=['BODYTYPE:COUPE', 'CAR:ALFA ROMEO', 'DEALER_COST:5,660', 'SALES:12400', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", 'riser!s0!g1!mbar!', expected_tooltip_list, "Step 14.10: Verify bar value")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by BODYTYPE, CAR", "Step 14.11: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 14.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 14.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 14.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)
        
        """
            Step 15 : Move the slider all the way to Sedan.
            Step 15:01 : Expect to see the following Bar Chart with the slider set to the last value of Sedan.
            8 Cars have at least one Bodytype of Sedan.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
   
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 4, 30) 
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0_f rect[class='sliderBody']")
        utillobj.click_on_screen(parentobj,'right', click_type=0, x_offset=-15)
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 32, 'Step 15.01: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g5!mbar!", "bar_blue", "Step 15.02: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g5!ay2!mbar!", "dark_green", "Step 15.03: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g5!ay2!mbar!", "pale_yellow", "Step 15.04 Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g5!mbar!", "pale_green", "Step 15.05: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 15.06: Verify Xaxis title")
        expected_xval_list=['JAGUAR','ALFA ROMEO','AUDI','BMW','DATSUN','JENSEN','PEUGEOT','TOYOTA']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 15.07: Verify XY labels")
        expected_yval2_list=['0', '400','800','1,200','1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 15.08: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 15.09: Verify legend")
        expected_tooltip_list=['BODYTYPE:SEDAN', 'CAR:BMW', 'DEALER_COST:49,500', 'SALES:80390', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g5!mbar!", expected_tooltip_list, "Step 15.10: Verify bar value")
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by BODYTYPE, CAR", "Step 15.11: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 15.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 15.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 15.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=2)        

        """
            Step 16 : Close the chart.
        """
        
if __name__ == "__main__":
        unittest.main()