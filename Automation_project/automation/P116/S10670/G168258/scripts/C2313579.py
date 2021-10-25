'''
Created on Oct 14, 2017

@author: Praveen Ramkumar
Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/7074&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313579
TestCase Name =  AHTML: Vertical Dual-Axis Clustered Bar Chart Limit functionality.
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous
from common.lib import utillity

class C2313579_TestClass(BaseTestCase):

    def test_C2313579(self):
        
        Test_Case_ID="C2313579"
        query_css="#queryTreeWindow"
        
        """
            TESTCASE OBJECTS
        """
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        time_out = 30
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FVertical_Cluster_Bar.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Vertical_Cluster_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "pale_green", "Step 01.4b: Verify  riser color")
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
        time.sleep(5)
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
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!", "pale_green", "Step 02.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.6b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify legend")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 02.8: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.9:c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
             
        """
            Step 03: Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.
            Expect to see the following Preview pane, with Car, Country & Model under the Horizontal axis bucket.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(12) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='COUNTRY', expire_time=time_out)
        metadataobj.datatree_field_click('MODEL', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(13) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='MODEL', expire_time=time_out)
        expected_xval_list=['ALFA ROMEO :...', 'ALFA ROMEO :...', 'ALFA ROMEO :...', 'AUDI : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','DATSUN : JAP...','JAGUAR : ENG...','JAGUAR : ENG...','JENSEN : ENG...','MASERATI : IT...','PEUGEOT : FR...','TOYOTA : JAP...','TRIUMPH : EN...']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K','28K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.1: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 36, 'Step 03.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 03.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 03.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : MODEL","Step 03.5a : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 03.5b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 03.5c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.6: Verify legend")
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 03.12: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 03.13: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','MODEL',3,"Step 03.14: Verify query pane")
            
        """
            Step 04: Double click field BODYTYPE.Expect to see the following Preview pane, with Car, Country & Bodytype under the Horizontal axis bucket.
            Bodytype replaced Model. Horizontal axis is limited to 3 fields.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(13) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='BODYTYPE', expire_time=time_out)
        expected_xval_list=['ALFA ROMEO :...', 'ALFA ROMEO :...', 'ALFA ROMEO :...', 'AUDI : W GER...','BMW : W GER...','DATSUN : JAP...','JAGUAR : ENG...','JAGUAR : ENG...','JENSEN : ENG...','MASERATI : IT...','PEUGEOT : FR...','TOYOTA : JAP...','TRIUMPH : EN...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 26, 'Step 04.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue1", "Step 04.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!ay2!mbar!", "bar_green", "Step 04.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : BODYTYPE","Step 04.5a : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 04.5b: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 04.5c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.6: Verify legend")
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 04.7a: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','COUNTRY',2,"Step 04.7b: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 04.7c: Verify query pane")
            
        """
            Step 05: Click the Run button.Hove over the first blue bar.
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Horizontal axis bucket).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR, COUNTRY, BODYTYPE", "Step 05.1 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO...', 'ALFA ROME...', 'ALFA ROMEO...', 'AUDI : W G...','BMW : W GE...','DATSUN : JA...','JAGUAR : E...','JAGUAR : E...','JENSEN : E...','MASERATI :...','PEUGEOT :...','TOYOTA : JA...','TRIUMPH :...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 05.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue1", "Step 05.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!ay2!mbar!", "bar_green", "Step 05.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR : COUNTRY : BODYTYPE","Step 05.6a: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.6b: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.6c : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.7: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.8: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.9a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.9b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.9:c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
             
        """
            Step 06: Delete fields Car & Bodytype from the Horizontal Axis bucket.
            Add fields RETAIL_COST, SALES, WEIGHT & RPM to the Vertical Axis 1 bucket.
            Add fields WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Vertical Axis 2 bucket.
            Expect to see the additional fields in the Preview pane.
        """
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.querytree_field_click("CAR",1,1,"Delete")
        time.sleep(2)
        metadataobj.querytree_field_click("BODYTYPE",1,1,"Delete")
        time.sleep(2)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='RETAIL_COST', expire_time=time_out)
        metadataobj.datatree_field_click('SALES', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='SALES', expire_time=time_out)
        metadataobj.datatree_field_click('WEIGHT', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='WEIGHT', expire_time=time_out)
        metadataobj.datatree_field_click('RPM', 2, 0)
#         parent_css="#queryTreeWindow table tr:nth-child(11) td"
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='RPM', expire_time=time_out)
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH',1, 'LENGTH',0)
#         parent_css='#queryTreeWindow tr:nth-child(14) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='WIDTH', expire_time=time_out)
        metadataobj.drag_drop_data_tree_items_to_query_tree('HEIGHT',1, 'WIDTH',0)
#         parent_css='#queryTreeWindow tr:nth-child(15) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='HEIGHT', expire_time=time_out)
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE',1, 'HEIGHT',0)
#         parent_css='#queryTreeWindow tr:nth-child(16) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='WHEELBASE', expire_time=time_out)
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP',1, 'WHEELBASE',0)
#         parent_css='#queryTreeWindow tr:nth-child(17) td'query_css
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='FUEL_CAP', expire_time=time_out)
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP',1, 'FUEL_CAP',0)
#         parent_css='#queryTreeWindow tr:nth-child(18) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='BHP', expire_time=time_out)
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG',1, 'BHP',0)
#         parent_css='#queryTreeWindow tr:nth-child(19) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='MPG', expire_time=time_out)
        time.sleep(3)
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL',1, 'MPG',0)
#         parent_css='#queryTreeWindow tr:nth-child(20) td'
        utillobj.synchronize_with_visble_text(query_css, visble_element_text='ACCEL', expire_time=time_out)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.1: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200','1,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.2: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 65, 'Step 06.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 06.4a: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 06.4b: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","COUNTRY","Step 06.5a : Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'SALES', 'WEIGHT', 'RPM', 'LENGTH', 'WIDTH', 'HEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 06.6: Verify legend")
         
        """
            Step 07: Click the Run button.
                    Expect to see the following Bar chart with 13 bars for each country.
                    The first 5 bars use the left-side axis for their scale.
                    The last 8 bars use the right-side axis for their scale.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES, WEIGHT, RPM, LENGTH, WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY", "Step 07.1 : Verify chart title ")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200','1,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 65, 'Step 07.4: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue1", "Step 07.5a: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 07.5b: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY","Step 07.6: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'SALES', 'WEIGHT', 'RPM', 'LENGTH', 'WIDTH', 'HEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.7: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.8a: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.8b: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.8c Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 08: Hover over the 1st bar(blue) and the 5th bar(red) for England.
                    Expect to see values that relate to the left-side axis scale.
        """
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 08.1: Verify bar value",x_offset=-2)
        expected_tooltip_list=['COUNTRY:ENGLAND', 'RPM:21200', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s4!g0!mbar!", expected_tooltip_list, "Step 08.1: Verify bar value",x_offset=-2)
        
        """
            Step 09: Hover over the 6th bar(orange) and the 13th and last bar(gray) for W Germany.
                    Expect to see values that relate to the right-side axis scale.
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'LENGTH:1,309', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g4!ay2!mbar!", expected_tooltip_list, "Step 09.1: Verify bar value",x_offset=-2)
        expected_tooltip_list=['COUNTRY:W GERMANY', 'ACCEL:13', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s12!g4!ay2!mbar!", expected_tooltip_list, "Step 09.2: Verify bar value",x_offset=-2)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)        
#         ele=driver.find_element_by_css_selector("#resultArea")
#         utillobj.take_screenshot(ele,Test_Case_ID + '_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
#         time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 10: Close the chart. Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()