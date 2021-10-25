'''
Created on Nov 9, 2017

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case= http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313601
TestCase Name =AHTML: Horizontal Dual-Axis Clustered Bar Chart Limit functionality.
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2313601_TestClass(BaseTestCase):

    def test_C2313601(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID="C2313601"
        
        """
            TESTCASE OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Cluster_Bar.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
         
        utillobj.infoassist_api_edit("Horizontal_Cluster_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 .chartPanel"
        resobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 20, 'Step 01.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "pale_green", "Step 01.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.06 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 01.07: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 01.08 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.09: Verify legend")
               
        """
            Step 02: Click the Run button.
            Expect to see the following Horizontal Dual-Axis Clustered Bar Chart.
        """
               
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR", "Step 02.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 20, 'Step 02.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!ay2!mbar!", "pale_green", "Step 02.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.07: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.08: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.09 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify legend")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 02.11: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
             
        """
            Step 03:Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.
            Expect to see the following Preview pane, with Car, Country & Model added to the Vertical axis bucket and the additional fields appearing in the 
            Y axis label area.
     
        """
             
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='COUNTRY', with_regular_exprestion=True)
        metadataobj.datatree_field_click('MODEL', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='MODEL', with_regular_exprestion=True)
        expected_xval_list=['ALFA ROMEO :...', 'ALFA ROMEO :...', 'ALFA ROMEO :...', 'AUDI : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','BMW : W GER...','DATSUN : JAP...','JAGUAR : ENG...','JAGUAR : ENG...','JENSEN : ENG...','MASERATI : IT...','PEUGEOT : FR...','TOYOTA : JAP...','TRIUMPH : EN...']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K','28K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.01: Verify XY labels",x_axis_label_length=2)
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.02: Verify XY labels",x_axis_label_length=4, y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 36, 'Step 03.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 03.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!ay2!mbar!", "bar_green", "Step 03.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : MODEL","Step 03.06 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 03.07: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 03.08 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.09: Verify legend")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 03.10: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 03.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','MODEL',3,"Step 03.12: Verify query pane")
             
        """
            Step 04: Double click field BODYTYPE.Expect to see the following Preview pane, with Car, Country & Bodytype under the Vertical axis bucket.
            Bodytype replaced Model. Vertical axis(Dimension) is limited to 3 fields.
        """   
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='BODYTYPE', with_regular_exprestion=True)
        expected_xval_list=['ALFA ROMEO :...', 'ALFA ROMEO :...', 'ALFA ROMEO :...', 'AUDI : W GER...','BMW : W GER...','DATSUN : JAP...','JAGUAR : ENG...','JAGUAR : ENG...','JENSEN : ENG...','MASERATI : IT...','PEUGEOT : FR...','TOYOTA : JAP...','TRIUMPH : EN...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.01: Verify XY labels",x_axis_label_length=2)
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.02: Verify XY labels",x_axis_label_length=2,y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 26, 'Step 04.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue1", "Step 04.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!ay2!mbar!", "bar_green", "Step 04.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : BODYTYPE","Step 04.06 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 04.07: Verify yaxis title")
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 04.08 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.09: Verify legend")
        utillobj.switch_to_default_content(pause=3)
        time.sleep(5)
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 04.10: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 04.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','BODYTYPE',3,"Step 04.12: Verify query pane")
             
        """
            Step 05:Click the Run button.Hove over the top(blue) bar for Alfa Romeo.
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Vertical axis bucket).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, LENGTH by CAR, COUNTRY, BODYTYPE", "Step 05.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO...', 'ALFA ROME...', 'ALFA ROMEO...', 'AUDI : W G...','BMW : W GE...','DATSUN : JA...','JAGUAR : E...','JAGUAR : E...','JENSEN : E...','MASERATI :...','PEUGEOT :...','TOYOTA : JA...','TRIUMPH :...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels",x_axis_label_length=2)
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.03: Verify XY labels",x_axis_label_length=2, y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 26, 'Step 05.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue1", "Step 05.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!ay2!mbar!", "bar_green", "Step 05.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR : COUNTRY : BODYTYPE","Step 05.07: Verify Xaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.08: Verify yaxis title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.09 : Verify yaxis title", custom_css="text[class='y2axis-title']")
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.10: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 05.11: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.12: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
            
        """
            Step 06: Delete fields Car & Bodytype from the Vertical Axis bucket.
            Add fields RETAIL_COST, SALES, WEIGHT & RPM to the Horizontal Axis 1 bucket.
            Add fields WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Horizontal Axis 2 bucket.
            Expect to see the additional fields in the Preview pane. The 12 bars for each set of sort fields are quite thin at this point.
        """  
        utillobj.switch_to_default_content(pause=3)
        time.sleep(10)
        metadataobj.querytree_field_click("CAR",1,1,"Delete")
        time.sleep(2)
        metadataobj.querytree_field_click("BODYTYPE",1,1,"Delete")
        time.sleep(2)
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='RETAIL_COST', with_regular_exprestion=True, expire_time=20)
        metadataobj.datatree_field_click('SALES', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='SALES', with_regular_exprestion=True, expire_time=20)
        metadataobj.datatree_field_click('WEIGHT', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='WEIGHT', with_regular_exprestion=True, expire_time=20)
        metadataobj.datatree_field_click('RPM', 2, 0)
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='RPM', with_regular_exprestion=True, expire_time=20)
        time.sleep(5)        
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='ACCEL',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='MPG',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='BHP',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='FUEL_CAP',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='WHEELBASE',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('HEIGHT',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='HEIGHT',expire_time=20)
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH',1, 'Horizontal Axis 2',0)
        parent_css='#queryTreeWindow'
        resobj.wait_for_property(parent_css, 1,string_value='WIDTH',expire_time=20)
        metadataobj.drag_and_drop_query_items("LENGTH", "Horizontal Axis 2")
        parent_css="#queryTreeWindow"
        resobj.wait_for_property(parent_css, 1, string_value='LENGTH', with_regular_exprestion=True, expire_time=20)
        time.sleep(5)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.01: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200','1,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 65, 'Step 06.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 06.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 06.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","COUNTRY","Step 06.06: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'SALES', 'WEIGHT', 'RPM', 'LENGTH', 'WIDTH', 'HEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 06.07: Verify legend") 
           
        """
            Step 07: Click the Run button.
            Expect to see the following Bar chart with 13 bars for each country.
            The first 4 bars use the bottom axis for their scale.
            The last 8 bars use the top axis for their scale.    
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, RETAIL_COST, SALES, WEIGHT, RPM, LENGTH, WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY", "Step 07.01 : Verify chart title ")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.02: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200','1,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 65, 'Step 07.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue1", "Step 07.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 07.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY","Step 07.07: Verify Xaxis title")
        legend=['DEALER_COST', 'RETAIL_COST', 'SALES', 'WEIGHT', 'RPM', 'LENGTH', 'WIDTH', 'HEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.08: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.09: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 08: Hover over the 1st bar(blue) for the England bars.
            Expect to see the value for field Dealer_Cost to relate to the bottom axis scale.   
        """
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 08.01: Verify bar value",x_offset=-2)
        time.sleep(2)
        
        """
            Step 09: Hover over the 1st bar(blue) for the England bars.
            Expect to see the value for field Dealer_Cost to relate to the bottom axis scale.   
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'ACCEL:13', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s12!g4!ay2!mbar!", expected_tooltip_list, "Step 09.01: Verify bar value",x_offset=-2)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 10: Close the chart.
        Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()