'''
Created on Oct 31, 2017
@author: Praveen Ramkumar
'''

import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_ribbon,visualization_resultarea,active_miscelaneous

class C2313664_TestClass(BaseTestCase):

    def test_C2313664(self):
        
        """
            CLASS OBJECTS
        """
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Bar.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Bar",'Chart','S10670',mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 .chartPanel"     
        utillobj.synchronize_with_number_of_element(element_css, 1, 65)
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 01.01: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 01.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 40, 'Step 01.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 01.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 01.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR","Step 01.06: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 01.07: Verify legend")
             
        """
           Step 02: Click the Run button.
            Expect to see the following Vertical Dual-Axis Clustered Bar Chart.
        """   
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]" 
        utillobj.synchronize_with_number_of_element(element_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 40, 30)    
        time.sleep(20)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR", "Step 02.01 : Verify chart title ")
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN','JAGUAR','JENSEN','MASERATI','PEUGEOT','TOYOTA','TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K','70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200','1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 02.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue", "Step 02.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 02.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR","Step 02.07: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.08: Verify legend")
        expected_tooltip_list=['CAR:BMW', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g2!mbar!", expected_tooltip_list, "Step 02.09: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
             
        """
            Step 03: Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.
            Expect to see the following Preview pane, with Car, Country & Model under the Horizontal axis bucket.
        """    
        utillobj.switch_to_default_content(pause=3)
        element_css="#queryTreeWindow"
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', 20)
        metadataobj.datatree_field_click('MODEL', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'MODEL', 20)
        expected_xval_list=['ALFA ROMEO : ITALY : 2000 4 DOOR BERLINA', 'ALFA ROMEO : ITALY : 2000 GT VELOCE', 'ALFA ROMEO : ITALY : 2000 SPIDER VELOCE', 'AUDI : W GERMANY : 100 LS 2 DOOR AUTO', 'BMW : W GERMANY : 2002 2 DOOR', 'BMW : W GERMANY : 2002 2 DOOR AUTO', 'BMW : W GERMANY : 3.0 SI 4 DOOR', 'BMW : W GERMANY : 3.0 SI 4 DOOR AUTO', 'BMW : W GERMANY : 530I 4 DOOR', 'BMW : W GERMANY : 530I 4 DOOR AUTO', 'DATSUN : JAPAN : B210 2 DOOR AUTO', 'JAGUAR : ENGLAND : V12XKE AUTO', 'JAGUAR : ENGLAND : XJ12L AUTO', 'JENSEN : ENGLAND : INTERCEPTOR III', 'MASERATI : ITALY : DORA 2 DOOR', 'PEUGEOT : FRANCE : 504 4 DOOR', 'TOYOTA : JAPAN : COROLLA 4 DOOR DIX AUTO', 'TRIUMPH : ENGLAND : TR7']
        expected_yval1_list=['0', '5K', '10K', '15K', '20K', '25K', '30K', '35K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.01: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160','200','240']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 72, 'Step 03.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue1", "Step 03.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "bar_green", "Step 03.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : MODEL","Step 03.06 : Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.07: Verify legend")
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 03.08: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 03.09: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','MODEL',3,"Step 03.10: Verify query pane")
               
        """
            Step 04: Double click field BODYTYPE.Expect to see the following Preview pane, with Car, Country & Bodytype under the Horizontal axis bucket.
            Bodytype replaced Model. Horizontal axis is limited to 3 fields.
        """    
        utillobj.switch_to_default_content(pause=3)
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        element_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(element_css, 'BODYTYPE', 20)
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.01: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 52, 'Step 04.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g4!mbar!", "bar_blue1", "Step 04.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g4!mbar!", "bar_green", "Step 04.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","CAR : COUNTRY : BODYTYPE","Step 04.06: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.07: Verify legend")
        metadataobj.verify_query_pane_field('Vertical Axis','CAR',1,"Step 04.08: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,"Step 04.09: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','BODYTYPE',3,"Step 04.10: Verify query pane")
              
              
        """
            Step 05: Click the Run button.Hove over the first blue bar.
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Horizontal axis bucket).
        """   
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        element_css="#resultArea [id^=ReportIframe-]"   
        utillobj.synchronize_with_number_of_element(element_css, 1, 45)     
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 52, 30) 
#         utillobj.synchronize_with_number_of_element(element_css, 1, 45)
        
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR, COUNTRY, BODYTYPE", "Step 05.01: Verify chart title ")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K','60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.02: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 52, 'Step 05.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g4!mbar!", "bar_blue1", "Step 05.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g4!mbar!", "bar_green", "Step 05.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","CAR : COUNTRY : BODYTYPE","Step 05.07: Verify Xaxis title")
        legend=["DEALER_COST","WEIGHT","LENGTH","HEIGHT"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.08: Verify legend")
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'LENGTH:163', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s2!g0!ay2!mbar!", expected_tooltip_list, "Step 05.09: Verify bar value")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
         
        """
            Step 06: Delete fields Car & Bodytype from the Horizontal Axis bucket.
            Add fields RETAIL_COST, SALES & RPM to the Horizontal Axis 1 bucket.
            Add fields WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Horizontal Axis 2 bucket.
            Expect to see the additional fields in the Preview pane.
        """
             
        utillobj.switch_to_default_content(pause=3)
        metadataobj.querytree_field_click("CAR",1,1,"Delete")
        time.sleep(2)
        metadataobj.querytree_field_click("BODYTYPE",1,1,"Delete")
        time.sleep(2)
        element_css="#queryTreeWindow"
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'RETAIL_COST', 20)
        
        metadataobj.datatree_field_click('SALES', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'SALES', 20)
        
        metadataobj.datatree_field_click('RPM', 2, 0)
        utillobj.synchronize_with_visble_text(element_css, 'RPM', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH',1, 'HEIGHT',0)
        utillobj.synchronize_with_visble_text(element_css, 'WIDTH', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE',1, 'WIDTH',0)
        utillobj.synchronize_with_visble_text(element_css, 'WHEELBASE', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP',1, 'WHEELBASE',0)
        utillobj.synchronize_with_visble_text(element_css, 'FUEL_CAP', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP',1, 'FUEL_CAP',0)
        utillobj.synchronize_with_visble_text(element_css, 'BHP', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG',1, 'BHP',0)
        utillobj.synchronize_with_visble_text(element_css, 'MPG', 20)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL',1, 'MPG',0)
        utillobj.synchronize_with_visble_text(element_css, 'ACCEL', 20)
        
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.01: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.02: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("TableChart_1", 1, 65, 'Step 06.03: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g2!mbar!", "bar_blue", "Step 06.04: Verify  riser color")
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g2!mbar!", "pale_green", "Step 06.05: Verify  riser color")
        resobj.verify_xaxis_title("TableChart_1","COUNTRY","Step 06.06: Verify Xaxis title")
        legend=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("TableChart_1", legend, "Step 06.07: Verify legend")
         
        """
            Step 07:Click the Run button.
            Expect to see the following Bar chart with 13 bars for each country.
            The top 5 bars use the bottom axis for their scale.
            The bottom 8 bars use the top axis for their scale.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0  svg g.risers >g>rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(element_css, 65, 30) 
        time.sleep(10)
        miscelaneous_obj.verify_chart_title("MAINTABLE_wbody0_ft","DEALER_COST, WEIGHT, RETAIL_COST, SALES, RPM, LENGTH, HEIGHT, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY", "Step 07.01: Verify chart title ")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN','W GERMANY']
        expected_yval1_list=['0','40K','80K', '120K','160K','200K','240K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.02: Verify XY labels")
        expected_yval2_list=['0', '500', '1,000', '1,500', '2,000', '2,500', '3,000', '3,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.03: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 65, 'Step 07.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mbar!", "bar_blue1", "Step 07.05: Verify  riser color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g2!mbar!", "pale_green", "Step 07.06: Verify  riser color")
        resobj.verify_xaxis_title("MAINTABLE_wbody0","COUNTRY","Step 07.07: Verify Xaxis title")
        legend=['DEALER_COST', 'WEIGHT', 'RETAIL_COST', 'SALES', 'RPM', 'LENGTH', 'HEIGHT', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.08: Verify legend")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.09: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
                
        """
            Step 08: Hover over the top left(Dealer_Cost) and the bottom left(Length) bar for England.
            Expect to see values that relate to the left-side axis scale.Bottom left bar
        """
        expected_tooltip_list=['COUNTRY:ENGLAND', 'DEALER_COST:37,853', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 08.01: Verify bar value",x_offset=-2)
        expected_tooltip_list=['COUNTRY:ENGLAND', 'LENGTH:741', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g0!ay2!mbar!", expected_tooltip_list, "Step 08.02: Verify bar value",x_offset=-2)
        
        """
            Step 09: Hover over the 6th bar(orange) and the 13th and last bar(gray) for W Germany.
                    Expect to see values that relate to the right-side axis scale.
        """
        expected_tooltip_list=['COUNTRY:W GERMANY', 'DEALER_COST:54,563', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s0!g4!mbar!", expected_tooltip_list, "Step 09.01: Verify bar value",x_offset=-2)
        expected_tooltip_list=['COUNTRY:W GERMANY', 'LENGTH:1,309', 'Filter Chart', 'Exclude from Chart']
        resobj.verify_default_tooltip_values("MAINTABLE_wbody0_f", "riser!s5!g4!ay2!mbar!", expected_tooltip_list, "Step 09.02: Verify bar value",x_offset=-2)
        utillobj.switch_to_default_content(pause=2)        
        time.sleep(2)
        
        """
            Step 10: Close the chart. Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    
if __name__ == '__main__':
    unittest.main()