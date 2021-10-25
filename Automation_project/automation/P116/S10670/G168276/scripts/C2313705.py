'''
Created on Nov 15, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313705
TestCase Name = AHTML: Horizontal Dual-Axis Stacked Line Chart Limit functionality.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity

class C2313705_TestClass(BaseTestCase):

    def test_C2313705(self):
        
        """
            TESTCASE OBJECTS
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """   
            Step 01 : Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Line_Line.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(element_css, 1, 65)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR","Step 01.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 01.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 01.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 01.6: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.7: Verify legend")
  
        """
            Step 02 : Click the Run button.
            Expect to see the following Horizontal Dual-Axis Stacked Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.1: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR","Step 02.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 02.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.6: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify legend")
         
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='start')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 02.8: Verify tooltip')
          
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 02.9: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
          
        """   
            Step 03 : Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.
            Expect to see the following Preview pane, with Car, Country & Model under the Vertical axis bucket.
            Also expect to see the additional sort fields along the Y-axis on the left the chart.
        """
 
        utillobj.switch_to_default_content(pause=3)
          
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY', 20)
          
        metadataobj.datatree_field_click('MODEL', 2, 0)
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:MODEL', 20)
         
        expected_xval_list=['ALFA ROMEO : ITALY : 2000 4 DOOR BERLINA', 'ALFA ROMEO : ITALY : 2000 GT VELOCE', 'ALFA ROMEO : ITALY : 2000 SPIDER VELOCE', 'AUDI : W GERMANY : 100 LS 2 DOOR AUTO', 'BMW : W GERMANY : 2002 2 DOOR', 'BMW : W GERMANY : 2002 2 DOOR AUTO', 'BMW : W GERMANY : 3.0 SI 4 DOOR', 'BMW : W GERMANY : 3.0 SI 4 DOOR AUTO', 'BMW : W GERMANY : 530I 4 DOOR', 'BMW : W GERMANY : 530I 4 DOOR AUTO', 'DATSUN : JAPAN : B210 2 DOOR AUTO', 'JAGUAR : ENGLAND : V12XKE AUTO', 'JAGUAR : ENGLAND : XJ12L AUTO', 'JENSEN : ENGLAND : INTERCEPTOR III', 'MASERATI : ITALY : DORA 2 DOOR', 'PEUGEOT : FRANCE : 504 4 DOOR', 'TOYOTA : JAPAN : COROLLA 4 DOOR DIX AUTO', 'TRIUMPH : ENGLAND : TR7']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.1: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR : COUNTRY : MODEL","Step 03.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 03.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 03.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 03.6: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.7: Verify legend")
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 03.8: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 03.9: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','MODEL',3,"Step 03.10: Verify query pane")
           
        """   
            Step 04 : Double click field BODYTYPE.Expect to see the following Preview pane, with Car, Country & Bodytype under the Horizontal axis bucket.
            Bodytype replaced Model. Vertical axis(sort) is limited to 3 fields.
        """
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        element_text="CAR : COUNTRY : BODYTYPE"
        utillobj.synchronize_with_visble_text(element_css, element_text, 20)
          
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.1: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR : COUNTRY : BODYTYPE","Step 04.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 4, 'Step 04.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 04.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 04.6: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.7: Verify legend")
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 04.8: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 04.9: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','BODYTYPE',3,"Step 04.10: Verify query pane")
            
        """   
            Step 05 : Click the Run button.Hove over the point on the left-most line for the first Alfa Romeo line.
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Vertical axis bucket).
        """
          
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        utillobj.switch_to_frame(pause=2)
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.1: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR : COUNTRY : BODYTYPE","Step 05.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 05.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.6: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.7: Verify legend")
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='start')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 05.9 Verify tooltip')
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR, COUNTRY, BODYTYPE", "Step 05.9: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """   
            Step 06 : Delete fields Car & Bodytype from the Horizontal Axis bucket.
            Add fields RETAIL_COST, SALES & RPM to the Horizontal Axis 1 bucket.
            Add fields WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Horizontal Axis 2 bucket.
            Expect to see the Preview pane with 5 fields in the Horizontal Axis 1 bucket and 8 fields in the Horizontal Axis 2 bucket.        
        """
          
        utillobj.switch_to_default_content(pause=3)
           
        metadataobj.querytree_field_click("CAR",1,1,"Delete")
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY:BODYTYPE', 10)
           
        metadataobj.querytree_field_click("BODYTYPE",1,1,"Delete")
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', 10)
           
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s2!']"
        utillobj.synchronize_with_visble_text(element_css, "RETAIL_COST", 10)
           
        metadataobj.datatree_field_click('SALES', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s3!']"
        utillobj.synchronize_with_visble_text(element_css, "SALES", 10)
           
        metadataobj.datatree_field_click('RPM', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s4!']"
        utillobj.synchronize_with_visble_text(element_css, "RPM", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH',1, 'HEIGHT',0)
        element_css="#TableChart_1 text[class^='legend-labels!s7!']"
        utillobj.synchronize_with_visble_text(element_css, "WIDTH", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE',1, 'WIDTH',0)
        element_css="#TableChart_1 text[class^='legend-labels!s8!']"
        utillobj.synchronize_with_visble_text(element_css, "WHEELBASE", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP',1, 'WHEELBASE',0)
        element_css="#TableChart_1 text[class^='legend-labels!s9!']"
        utillobj.synchronize_with_visble_text(element_css, "FUEL_CAP", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP',1, 'FUEL_CAP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s10!']"
        utillobj.synchronize_with_visble_text(element_css, "BHP", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG',1, 'BHP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s11!']"
        utillobj.synchronize_with_visble_text(element_css, "MPG", 10)
           
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL',1, 'MPG',0)
        element_css="#TableChart_1 text[class^='legend-labels!s12!']"
        utillobj.synchronize_with_visble_text(element_css, "ACCEL", 10)
          
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval1_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.1: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "COUNTRY","Step 06.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 13, 'Step 06.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 06.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 06.6: Verify line2 color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 06.7: Verify legend")

        """   
            Step 07 : Click the Run button.Expect to see the following Bar chart with 13 bars for each country.        
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 35)
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval1_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.1: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "COUNTRY","Step 07.3 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, 'Step 07.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 07.5: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 07.6: Verify line2 color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.7: Verify legend")
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='start')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 07.8: Verify tooltip')
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, RETAIL_COST, SALES, RPM, LENGTH, HEIGHT, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY", "Step 07.9: Verify chart title ")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """   
            Step 08 : Hover over the points in the top left line(Dealer_Cost) and the top right(Accel) line for England.
            Top left line for Dealer_Cost relates to the bottom axis scale.
            Top right line for Accel relates to the top axis scale.
        """
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='start')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 08.1: Verify tooltip')
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='right')
#         expected_tooltip_list=['COUNTRY:ENGLAND', 'ACCEL:22', 'Filter Chart', 'Exclude from Chart']
        expected_tooltip_list=['COUNTRY:ENGLAND', 'ACCEL:23', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s12!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 08.2: Verify tooltip')
        
        """   
            Step 09 : Hover over the points in the bottom left line(Dealer_Cost) and the bottom right(Rpm) line for W Germany.
            Bottom left line for Dealer_Cost relates to the bottom axis scale.Top right line for Rpm relates to the top axis scale.
        """
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='bottom_middle')
        expected_tooltip_list=['COUNTRY:W GERMANY', 'DEALER_COST:54,563', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s0!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 09.1: Verify tooltip')
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='bottom_right')
        expected_tooltip_list=['COUNTRY:W GERMANY', 'RPM:5500', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s4!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 09.2: Verify tooltip')
        
        """   
            Step 10:Close the chart.
            Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.switch_to_default_content(pause=2)  
              

if __name__=='__main__' :
    unittest.main()       