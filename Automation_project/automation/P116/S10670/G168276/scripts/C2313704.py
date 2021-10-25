'''
Created on Nov 15, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313704
TestCase Name = AHTML: Horizontal Dual-Axis Stacked Line Chart Additional bucket functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity

class C2313704_TestClass(BaseTestCase):

    def test_C2313704(self):
        
        Test_Case_ID="C2313704"
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
                
        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Line_Line.fex&tool=Chart
                    
                    Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 01.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 01.4: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 01.5: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.6: Verify Y-Axis legend")

        """
            Step 02:Click the Run button.
                    
                    Expect to see the following Horizontal Dual-Axis Stacked Line Chart.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 02.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 02.4: Verify Number of riser', custom_css="path[class^='riser']")        
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 04: Verify tooltip')          
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 02.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 02.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)

        """
            Step 03:Drag field SALES to the Tooltip bucket.
                    
                    Expect to see the following Preview pane with SALES under the Tooltip bucket.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip',0)
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True, expire_time=20)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Tooltip', 'SALES', 1, "Step 03:")

        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 03.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 03.4: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 03.5: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify Y-Axis legend")

        """
            Step 04:Click the Run button.
                    
                    Hove over the point on the lower left line for Triumph.
                Expect to see the Sales field added to the Tooltip information for Car & Dealer_Cost.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 04.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 04.4: Verify Number of riser', custom_css="path[class^='riser']")
        expected_tooltip_list=['CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'SALES:  30200', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 04.5: Verify tooltip') 
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 04.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by CAR', 'Step 04.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        
        """
            Step 05:Drag the field BODYTYPE to the Color BY bucket.
                    
                    Expect to see the following Preview pane with BODYTYPE under the Color BY bucket.
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
#         metadataobj.drag_drop_data_tree_items_to_query_tree('BODYTYPE', 1, 'Color',0)
        metadataobj.datatree_field_click('BODYTYPE', 1, 1, 'Add To Query', 'Color')
        parent_css="#queryTreeWindow table tr:nth-child(16) td"
        resobj.wait_for_property(parent_css, 1, string_value='BODYTYPE', with_regular_exprestion=True, expire_time=20)
        time.sleep(5) 
        metadataobj.verify_query_pane_field('Color BY', 'BODYTYPE', 1, "Step05a: Verify in query pane BODYTYPE under the Color BY bucket")
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 05.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 05.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 28, 'Step 05.4: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s18!g0!mline!", "periwinkle_gray", "Step 05.5: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST : CONVERTIBLE', 'WEIGHT : CONVERTIBLE', 'LENGTH : CONVERTIBLE', 'HEIGHT : CONVERTIBLE', 'DEALER_COST : COUPE', 'WEIGHT : COUPE', 'LENGTH : COUPE', 'HEIGHT : COUPE', 'DEALER_COST : HARDTOP', 'WEIGHT : HARDTOP', 'LENGTH : HARDTOP', 'HEIGHT : HARDTOP', 'DEALER_COST : ROADSTER', 'WEIGHT : ROADSTER', 'LENGTH : ROADSTER', 'HEIGHT : ROADSTER', 'DEALER_COST : SEDAN', 'WEIGHT : SEDAN', 'LENGTH : SEDAN', 'HEIGHT : SEDAN']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 05.6: Verify Y-Axis legend")

        """
            Step 06:Click the Run button. 
                    Hover over the point on the left most line for Jensen.
                    
                    Expect to see the Bodytype field added to the Tooltip information.Also expect to see the Bodytype legend on the right-side of the chart.
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 06.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 28, 'Step 06.4: Verify Number of riser', custom_css="path[class^='riser']")     
        expected_tooltip_list=['CAR:  JENSEN', 'LENGTH:  188', 'BODYTYPE:  SEDAN', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s18!g5!mmarker!', expected_tooltip_list, 'Step 06.5: Verify tooltip')   
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s18!g0!mline!", "periwinkle_gray", "Step 06.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by BODYTYPE, CAR', 'Step 06.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(1)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)

        """
            Step 07:Delete the field BODYTYPE from the Color BY bucket.
                    Drag the field SEATS to the Mutli-graph bucket.
                    
                Expect to see the following Preview pane with COUNTRY removed from the Color BY bucket and SEATS added to the Multi-graph bucket.
        """
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        metadataobj.querytree_field_click('BODYTYPE', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.datatree_field_click("SEATS", 1, 1, 'Add To Query', 'Multi-graph')
        time.sleep(2)
        metadataobj.verify_query_pane_field('Multi-graph', 'SEATS', 1, "Step 07: Verify in query pane SEATS added to the Multi-graph bucket")
        resobj.verify_xaxis_title("TableChart_1", "CAR", "Step 07.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 07.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 07.4: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue1", "Step 07.5: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 07.6: Verify Y-Axis legend")

        """
            Step 08:Click the Run button. Expect to see the following Line Chart. 
                    
                    The order of the lines is no longer in CAR order but in order of SEATS, then Car.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 08.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'JAGUAR', 'MASERATI', 'TRIUMPH', 'BMW', 'DATSUN', 'JENSEN', 'TOYOTA', 'AUDI', 'PEUGEOT']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 08.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 08.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT, SALES by CAR', 'Step 08.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)

        """
            Step 09:Hover over the point on the top left line for Alfa Romeo.
                    
                    Expect to see the value of 2 for SEATS.The lines with 2 Seats are sorted by Car, ending with Triumph,
                    the last Car with 2 Seats.Last Car with 2 Seats.
        """
        
        expected_tooltip_list=['SEATS:  2', 'CAR:  ALFA ROMEO', 'DEALER_COST:  16,235', 'SALES:  30200', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g0!mmarker!', expected_tooltip_list, 'Step 09.1: Verify tooltip') 
        time.sleep(8) 
        expected_tooltip_list=['SEATS:  2', 'CAR:  TRIUMPH', 'DEALER_COST:  4,292', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g3!mmarker!', expected_tooltip_list, 'Step 09.2: Verify tooltip') 

        """
            Step 10:Hover over the point on the right-most line for BMW.
                    
                    Expect to see a value of 4 for SEATS.BMW thru Toyota all have 4 Seats.
        """
        expected_tooltip_list=['SEATS:  4', 'CAR:  BMW', 'HEIGHT:  337', 'SALES:  80390', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s3!g4!mmarker!', expected_tooltip_list, 'Step 10.1: Verify tooltip') 
        time.sleep(8) 
        expected_tooltip_list=['SEATS:  4', 'CAR:  TOYOTA', 'DEALER_COST:  2,886', 'SALES:  35030', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g7!mmarker!', expected_tooltip_list, 'Step 10.2: Verify tooltip') 

        """
            Step 11:Hover over the point on the right-most line for Peugeot.
    
                Expect to see a value of 5 for SEATS.Both Audi & Peugeot have 5 Seats.
        """
        expected_tooltip_list=['SEATS:  5', 'CAR:  PEUGEOT', 'HEIGHT:  57', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s3!g9!mmarker!', expected_tooltip_list, 'Step 11.1: Verify tooltip')
        time.sleep(8)  
#         expected_tooltip_list=['SEATS:  5', 'CAR:  AUDI', 'HEIGHT:  54', 'SALES:  7800', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list=['SEATS:  5', 'CAR:  AUDI', 'HEIGHT:  55', 'SALES:  7800', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s3!g8!mmarker!', expected_tooltip_list, 'Step 11.2: Verify tooltip') 
     
        """
            Step 12:Delete the field SEATS from the Multi-graph bucket.
                    Drag the field COUNTRY to the Animate bucket.

                Expect to see the following Preview pane with a slider added for Country at the top.
        """
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(3)
        metadataobj.querytree_field_click('SEATS', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('COUNTRY', 1, 'Animate',0)
        parent_css="#queryTreeWindow table tr:nth-child(21) td"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True, expire_time=20)
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 12.1: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500', '600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 12.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 12.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 12.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 12.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 12.6: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('TableChart_1', expected_datalabel, "Step 12.7", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#TableChart_1 .sliderContainer", True, "Step 12.8: Slider Visible")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 12.9: Verify legend")
        time.sleep(5)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_12")
        time.sleep(1)
        

        """
            Step 13:Click the Run button.
                    
                    Expect to see the following Line Chart with the slider set to the default value of ENGLAND and only Jaguar, Jensen & Triumph lines displaying.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        expected_xval_list=['JAGUAR', 'JENSEN', 'TRIUMPH']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 13.1: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500', '600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 13.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 13.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 13.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 13.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 13.6: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 13.7: verify slider labels", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 13.8: Slider Visible")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 13.9: Verify legend")
        expected_tooltip_list=['COUNTRY:  ENGLAND', 'CAR:  TRIUMPH', 'DEALER_COST:  4,292', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s0!g2!mmarker!', expected_tooltip_list, 'Step 13.10: Verify tooltip')
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_13")
        time.sleep(1)

        """
            Step 14:Move the slider to ITALY.
                    Hover over the point for the left-most line for Maserati.
                    
                    Expect to see the following Line Chart with the slider indicating a Country of Italy and only Alfa Romeo and Maserati lines appearing.
                    Also verify that the Tooltip information includes Country from the slider and Sales form the Tooltip bucket.

        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'middle', click_type=0)
        time.sleep(5)
        expected_tooltip_list=['COUNTRY:  ITALY', 'CAR:  MASERATI', 'LENGTH:  177', 'SALES:  0', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s2!g5!mmarker!', expected_tooltip_list, 'Step 14.1 : Verify tooltip')
        time.sleep(1)
        expected_xval_list=['ALFA ROMEO', 'MASERATI']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 14.2: Verify XY labels")
        expected_yval2_list=['0', '100', '200', '300', '400', '500', '600', '700', '800']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 14.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 14.4 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 14.5: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 14.8: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 14.9: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 14.10", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 14.11: Slider Visible")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 14.13: Verify legend")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_14")
        time.sleep(1)
        
        
        """
            Step 15:Move the slider all the way to W GERMANY.
                    
                    Expect to see the following Line Chart with the slider set to the last value of W GERMANY.Audi & BMW should appear.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        time.sleep(1)
        parentobj = driver.find_element_by_css_selector("#MAINTABLE_wbody0 .sliderContainer rect[class^='sliderBody']")
        utillobj.click_on_screen(parentobj,'right', click_type=0, x_offset=-15)
        time.sleep(2)        
        expected_tooltip_list=['COUNTRY:  W GERMANY', 'CAR:  BMW', 'HEIGHT:  337', 'SALES:  80390', 'Filter Chart', 'Exclude from Chart']
        ia_resultobj.verify_marker_tooltip('MAINTABLE_wbody0', 'marker!s3!g9!mmarker!', expected_tooltip_list, 'Step 15: Verify tooltip')
        time.sleep(1)
        expected_xval_list=['AUDI', 'BMW']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 15.1: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 15.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 15.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 15.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 15.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 15.8: Verify line2 color",attribute_type='stroke')
        expected_datalabel=["ENGLAND", "FRANCE", "ITALY", "JAPAN", "W GERMANY"]
        resobj.verify_data_labels('MAINTABLE_wbody0', expected_datalabel, "Step 15.9: verify slider value", custom_css=".sliderContainer g text[class^='slider-labels!']" )
        utillobj.verify_object_visible("#MAINTABLE_wbody0 .sliderContainer", True, "Step 15.10: Slider Visible")
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 15.11: Verify legend")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element, Test_Case_ID+"_Step_15")
        time.sleep(1)        

        """
            Step 16:Close the chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
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
        