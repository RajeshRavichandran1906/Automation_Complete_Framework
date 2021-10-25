'''
Created on Oct 21, 2017

@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://172.19.2.180/testrail/index.php?/cases/view/2313608
TestCase Name = AHTML: Mekko Chart Color By chart using additional Buckets.
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2313608_TestClass(BaseTestCase):

    def test_C2313608(self):
               
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
            Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FVertical_Stacked_Bar.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Vertical_Stacked_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'CAR', 65)
        
        """
            step 01.1 : Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
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
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.08: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
         
        """
            Step 02 : Click the Run button.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, ribbonobj.home_page_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'CAR', 30)
        
        """
            Step 02.1  : Expect to see the following Vertical Dual-Axis Stacked Bar Chart.
        """
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 02.01: Verify chart title ")
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
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 02.11: Verify bar value")       
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#iaMetaDataBrowser", 25)
        
        """
            Step 03 : Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.
        """
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'CAR:COUNTRY', 15)
    
        metadataobj.datatree_field_click('MODEL', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'CAR:COUNTRY:MODEL', 15)
        
        """
            Step 03 : Expect to see the following Preview pane, with Car, Country & Model under the Horizontal axis bucket.
            Also expect to see the additional sort fields along the X-axis under the chart.
        """
        expected_xval_list=['ALFA ROMEO : ITALY : 2000 4 DO...', 'ALFA ROMEO : ITALY : 2000 GT...', 'ALFA ROMEO : ITALY : 2000 SPI...', 'AUDI : W GERMANY : 100 LS 2 D...', 'BMW : W GERMANY : 2002 2 DOOR', 'BMW : W GERMANY : 2002 2 DOO...', 'BMW : W GERMANY : 3.0 SI 4 DOOR', 'BMW : W GERMANY : 3.0 SI 4 DO...', 'BMW : W GERMANY : 530I 4 DOOR', 'BMW : W GERMANY : 530I 4 DOO...', 'DATSUN : JAPAN : B210 2 DOOR...', 'JAGUAR : ENGLAND : V12XKE AU...', 'JAGUAR : ENGLAND : XJ12L AUTO', 'JENSEN : ENGLAND : INTERCEPT...', 'MASERATI : ITALY : DORA 2 DOOR', 'PEUGEOT : FRANCE : 504 4 DOOR', 'TOYOTA : JAPAN : COROLLA 4 D...', 'TRIUMPH : ENGLAND : TR7']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.01: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : MODEL', "Step 03.03: Verify X-Axis Title")
        resobj.verify_number_of_riser("TableChart_1", 1, 72, 'Step 03.04: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g4!mbar!', 'bar_blue1', 'Step 03.05: Verify Color')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.06: Verify legend")
        
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 03.07: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 03.08: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','MODEL',3,"Step 03.09: Verify query pane")
          
        """
            Step 04 : Double click field BODYTYPE.
        """
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'CAR:COUNTRY:BODYTYPE', 10)
        
        """
            Step 04.1 : Expect to see the following Preview pane, with Car, Country & Bodytype under the Horizontal axis bucket.
            Bodytype replaced Model. Horizontal axis(sort) is limited to 3 fields.
        """
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTI...', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.01 : Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.02 : Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : BODYTYPE', "Step 04.03: Verify X-Axis Title")
        resobj.verify_number_of_riser("TableChart_1", 1, 52, 'Step 04.04: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g4!mbar!', 'bar_blue1', 'Step 04.05: Verify Color')
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.06: Verify legend")
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 04.07: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 04.08: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 04.09: Verify query pane")
         
        """
            Step 05 : Click the Run button.Hove over the lower left bar for the first Alfa Romeo set of bars.
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Horizontal axis bucket).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, ribbonobj.home_page_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']", 'CAR:COUNTRY:BODYTYPE', 20)
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR, COUNTRY, BODYTYPE", "Step 05.01: Verify chart title ")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADST...', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVER...', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR : COUNTRY : BODYTYPE","Step 05.04: Verify Xaxis title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 52, 'Step 05.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 05.06: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g2!ay2!mbar!", "dark_green", "Step 05.07: Verify  riser color")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.08: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.09: Verify bar value")       
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """
            Step 06 : Delete fields Car & Bodytype from the Horizontal Axis bucket.
        """
        utillobj.switch_to_default_content(pause=3)
        utillobj.synchronize_until_element_is_visible("#queryTreeWindow", 25)
        
        metadataobj.querytree_field_click("CAR",1,1,"Delete")
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY:BODYTYPE', 15)
       
        metadataobj.querytree_field_click("BODYTYPE",1,1,"Delete")
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='xaxisOrdinal-title']", 'COUNTRY', 15)
        
        """
            Step 07 : Drag field SALES to the Tooltip bucket.
            Add fields RETAIL_COST, SALES & RPM to the Vertical Axis 1 bucket.
            Add fields WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Vertical Axis 2 bucket.
        """ 
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s2!']", 'RETAIL_COST', 10)
        
        metadataobj.datatree_field_click('SALES', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s3!']", 'SALES', 10)
        
        metadataobj.datatree_field_click('RPM', 2, 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s4!']", 'RPM', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('SALES', 1, 'Tooltip', 0)
        utillobj.synchronize_with_visble_text("#queryTreeWindow", 'SALES', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH',1, 'HEIGHT', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s7!']", 'WIDTH', 10)
       
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE',1, 'WIDTH', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s8!']", 'WHEELBASE', 10)
       
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP',1, 'WHEELBASE', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s9!']", 'FUEL_CAP', 10)
       
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP',1, 'FUEL_CAP', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s10!']", 'BHP', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG',1, 'BHP', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s11!']", 'MPG', 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL',1, 'MPG', 0)
        utillobj.synchronize_with_visble_text("#pfjTableChart_1 text[class='legend-labels!s12!']", 'ACCEL', 10)
        
        """
            Expect to see the Preview pane with 5 fields in the Vertical Axis 1 bucket and 8 fields in the Vertical Axis 2 bucket.
        """
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 07.01: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 07.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 65, 'Step 07.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 07.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 07.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","COUNTRY","Step 07.06: Verify Xaxis title")
        legend=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 07.07: Verify legend")
        metadataobj.verify_query_pane_field('Vertical Axis 2','LENGTH',1,"Step 07.08: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','HEIGHT',2,"Step 07.09: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','WIDTH',3,"Step 07.10: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','WHEELBASE',4,"Step 07.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','FUEL_CAP',5,"Step 07.12: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','BHP',6,"Step 07.13: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','MPG',7,"Step 07.14: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','ACCEL',8,"Step 07.15: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','DEALER_COST',1,"Step 07.16: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','WEIGHT',2,"Step 07.17: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','RETAIL_COST',3,"Step 07.18: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','SALES',4,"Step 07.19: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','RPM',5,"Step 07.20: Verify query pane")
          
        """
            Step 08 : Click the Run button.Expect to see the following Bar chart with 13 bars for each country.
            The first 5 bars use the left-side axis for their scale. The last 8 bars use the right-side axis for their scale..
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, ribbonobj.home_page_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        utillobj.synchronize_with_visble_text("#MAINTABLE_wbody0_f text[class='legend-labels!s12!']", 'ACCEL', 20)
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, RETAIL_COST, SALES, RPM, LENGTH, HEIGHT, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL, SALES by COUNTRY", "Step 08.1 : Verify chart title ")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval1_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.01: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", [], expected_yval2_list, "Step 08.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'COUNTRY', "Step 08.03: Verify X-Axis Title")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 65, 'Step 08.04: Verify the total number of risers displayed on run')
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s2!g0!mbar!', 'dark_green', 'Step 08.05: Verify Color')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.06: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 08.09: Verify Legends ')
     
        """
            Step 09 : Hover over the bottom left(Dealer_Cost) and the bottom right(Length) bar for England.
            Expect to see values that relate to the left-side axis scale.Bottom left bar
        """
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 09.01: Verify bar value") 
        
        expected_tooltip_list=['COUNTRY:ENGLAND', 'LENGTH:741', 'SALES:12000', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g0!ay2!mbar!", expected_tooltip_list, "Step 09.02: Verify bar value") 
        
        """
            Step 10 : Hover over the bottom left(Dealer_Cost) and the bottom right(Length) for W Germany.
            Expect to see values that relate to the right-side axis scale.Bottom left bar
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'DEALER_COST:54,563', 'SALES:88190', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 10.01: Verify bar value")
    
        utillobj.switch_to_default_content(pause=2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, ribbonobj.home_page_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        
        expected_tooltip_list=['COUNTRY:W GERMANY', 'LENGTH:1,309', 'SALES:88190', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g4!ay2!mbar!", expected_tooltip_list, "Step 10.02: Verify bar value") 
       
        utillobj.switch_to_default_content(pause=2)             
        
        """
            Step 11 : Close the chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                  
if __name__ == '__main__':
    unittest.main()