'''
Created on Nov 13, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313693
TestCase Name = AHTML: Vertical Dual-Axis Absolute Line Chart Limit functionality.
'''
import unittest
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata

class C2313693_TestClass(BaseTestCase):

    def test_C2313693(self):
        
        """
            TESTCASE OBJECTS
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """  
            Step 01 : Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FVertical_Absolute_Line.fex&tool=Chart
            Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
        utillobj.infoassist_api_edit("Vertical_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR', 65)
        
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
            Step 02 : Click the Run button.
            Expect to see the following Vertical Dual-Axis Absolute Line Chart.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR', 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR', "Step 02.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 02.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 02.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.4: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.5: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 02.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 02.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 02.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR', 'Step 02.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
            Step 03 : Double click on fields COUNTRY & MODEL to add them to the Horizontal axis bucket under CAR.          
            Expect to see the following Preview pane, with Car, Country & Model under the Horizontal axis bucket.
        """
        utillobj.switch_to_default_content(pause=2)
        
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY', 10)
        
        metadataobj.datatree_field_click('MODEL', 2, 0)
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:MODEL', 10)
        
        expected_xval_list=['ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'AUDI : W GERMANY...', 'BMW : W GERMANY :...', 'BMW : W GERMANY :...', 'BMW : W GERMANY :...', 'BMW : W GERMANY :...', 'BMW : W GERMANY :...', 'BMW : W GERMANY :...', 'DATSUN : JAPAN :...', 'JAGUAR : ENGLAND...', 'JAGUAR : ENGLAND...', 'JENSEN : ENGLAND...', 'MASERATI : ITALY :...', 'PEUGEOT : FRANCE...', 'TOYOTA : JAPAN :...', 'TRIUMPH : ENGLAN...']
        expected_yval1_list=['0', '4K', '8K', '12K', '16K', '20K','24K', '28K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 03.1: Verify XY labels", x_axis_label_length=10)
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 03.2: Verify XY labels", x_axis_label_length=10, y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR : COUNTRY : MODEL","Step 03.3 : Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 03.4: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 03.5: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 03.6: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 03.7: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 03.8: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 03.9: Verify legend")
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 03.10: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis', 'COUNTRY',2,"Step 03.11: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','MODEL',3,"Step 03.12: Verify query pane")
  
        """
            Step 04 : Double click field BODYTYPE.Expect to see the following Preview pane, with Car, Country & Bodytype under the Horizontal axis bucket.
            Bodytype replaced Model. Horizontal axis is limited to 3 fields.
        """
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:BODYTYPE', 10)
        
        metadataobj.verify_query_pane_field('Horizontal Axis','CAR',1,"Step 04.1: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis', 'COUNTRY',2,"Step 04.2: Verify query pane")
        metadataobj.verify_query_pane_field('Horizontal Axis','BODYTYPE',3,"Step 04.3: Verify query pane")
        
        expected_xval_list=['ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'AUDI : W GERMANY...', 'BMW : W GERMANY...', 'DATSUN : JAPAN :...', 'JAGUAR : ENGLAND...', 'JAGUAR : ENGLAND...', 'JENSEN : ENGLAND...', 'MASERATI : ITALY :...', 'PEUGEOT : FRANCE...', 'TOYOTA : JAPAN : S...', 'TRIUMPH : ENGLAN...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 04.4: Verify XY labels", x_axis_label_length=10)
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 04.5: Verify XY labels", x_axis_label_length=10, y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "CAR : COUNTRY : BODYTYPE","Step 04.6: Verify Xaxis title")
        resobj.verify_yaxis_title("TableChart_1", "DEALER_COST", "Step 04.7: Verify -yAxis Title") 
        resobj.verify_yaxis_title("TableChart_1", "LENGTH", "Step 04.8: Verify -y2Axis Title", custom_css="text[class='y2axis-title']") 
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 04.9: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mline!", "bar_blue", "Step 04.10: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 04.11: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","LENGTH"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 04.12: Verify legend")
         
        """
            Step 05 : Click the Run button.
            Hove over the point on the lower line for the first Alfa Romeo set of points. 
            Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Horizontal axis bucket).
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        utillobj.switch_to_frame(pause=2)
        element_css="#MAINTABLE_wbody0_f text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:BODYTYPE', 20)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 05.1: Verify X-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "DEALER_COST", "Step 05.2: Verify Y-Axis Title")
        resobj.verify_yaxis_title("MAINTABLE_wbody0", "LENGTH", "Step 05.3: Verify Y2-Axis Title", custom_css="text[class='y2axis-title']") 
        expected_xval_list=['ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'ALFA ROMEO : ITALY...', 'AUDI : W GERMANY...', 'BMW : W GERMANY...', 'DATSUN : JAPAN :...', 'JAGUAR : ENGLAND...', 'JAGUAR : ENGLAND...', 'JENSEN : ENGLAND...', 'MASERATI : ITALY :...', 'PEUGEOT : FRANCE...', 'TOYOTA : JAPAN : S...', 'TRIUMPH : ENGLAN...']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.4: Verify XY labels", x_axis_label_length=8)
        expected_yval2_list=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.5: Verify XY labels", x_axis_label_length=5 ,y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 05.6: Verify Number of riser', custom_css="path[class^='riser']")
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='left')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 05.7: Verify tooltip')
       
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 05.8: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 05.9: Verify  2nd bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'LENGTH']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.10: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, LENGTH by CAR, COUNTRY, BODYTYPE', 'Step 05.11: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.12: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.13: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.14: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
            Step 06 : Delete fields Car & Bodytype from the Horizontal Axis bucket.
            Add fields RETAIL_COST, SALES, WEIGHT & RPM to the Vertical Axis 1 bucket.
            Add fields WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Vertical Axis 2 bucket.
            Expect to see the additional fields in the Preview pane.
        """
        utillobj.switch_to_default_content(pause=2)
        
        metadataobj.querytree_field_click('CAR', 1, 1, "Delete")
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, "COUNTRY:BODYTYPE", 10)
        
        metadataobj.querytree_field_click('BODYTYPE', 1, 1, "Delete")
        element_css="#pfjTableChart_1 text[class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, "COUNTRY", 10)
          
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(element_css, "RETAIL_COST", 10)
        
        metadataobj.datatree_field_click('SALES', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s2!']"
        utillobj.synchronize_with_visble_text(element_css, "SALES", 10)
        
        metadataobj.datatree_field_click('WEIGHT', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s3!']"
        utillobj.synchronize_with_visble_text(element_css, "WEIGHT", 10)
        
        metadataobj.datatree_field_click('RPM', 2, 0)
        element_css="#TableChart_1 text[class^='legend-labels!s4!']"
        utillobj.synchronize_with_visble_text(element_css, "RPM", 10)  
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('WIDTH', 1, 'LENGTH',0)
        element_css="#TableChart_1 text[class^='legend-labels!s6!']"
        utillobj.synchronize_with_visble_text(element_css, "WIDTH", 10)   
             
        metadataobj.drag_drop_data_tree_items_to_query_tree('HEIGHT', 1, 'WIDTH',0)
        element_css="#TableChart_1 text[class^='legend-labels!s7!']"
        utillobj.synchronize_with_visble_text(element_css, "HEIGHT", 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE', 1, 'HEIGHT',0)
        element_css="#TableChart_1 text[class^='legend-labels!s8!']"
        utillobj.synchronize_with_visble_text(element_css, "WHEELBASE", 10)
                
        metadataobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP', 1, 'WHEELBASE',0)
        element_css="#TableChart_1 text[class^='legend-labels!s9!']"
        utillobj.synchronize_with_visble_text(element_css, "FUEL_CAP", 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('BHP', 1, 'FUEL_CAP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s10!']"
        utillobj.synchronize_with_visble_text(element_css, "BHP", 10)  
              
        metadataobj.drag_drop_data_tree_items_to_query_tree('MPG', 1, 'BHP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s11!']"
        utillobj.synchronize_with_visble_text(element_css, "MPG", 10)
        
        metadataobj.drag_drop_data_tree_items_to_query_tree('ACCEL', 1, 'MPG',0)
        element_css="#TableChart_1 text[class^='legend-labels!s12!']"
        utillobj.synchronize_with_visble_text(element_css, "ACCEL", 10) 
                    
        metadataobj.verify_query_pane_field('Vertical Axis 1','DEALER_COST',1,"Step 06.1: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','RETAIL_COST',2,"Step 06.2: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','SALES',3,"Step 06.3: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','WEIGHT',4,"Step 06.4: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 1','RPM',5,"Step 06.5: Verify query pane") 
        metadataobj.verify_query_pane_field('Vertical Axis 2','LENGTH',1,"Step 06.6: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','WIDTH',2,"Step 06.7: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','HEIGHT',3,"Step 06.8: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','WHEELBASE',4,"Step 06.9: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','FUEL_CAP',5,"Step 06.10: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','BHP',6,"Step 06.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','MPG',7,"Step 06.12: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis 2','ACCEL',8,"Step 06.13: Verify query pane")
        
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval1_list, "Step 06.14: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200', '1,500']
        resobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval2_list, "Step 06.15: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        resobj.verify_xaxis_title("TableChart_1", "COUNTRY","Step 06.16 : Verify Xaxis title")
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 13, 'Step 06.17: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("TableChart_1", "riser!s5!g0!mline!", "light_brick", "Step 06.18: Verify line1 color",attribute_type='stroke')
        utillobj.verify_chart_color("TableChart_1", "riser!s1!g0!mline!", "pale_green", "Step 06.19: Verify line2 color",attribute_type='stroke')
        legend=["DEALER_COST","RETAIL_COST","SALES","WEIGHT","RPM","LENGTH","WIDTH","HEIGHT","WHEELBASE","FUEL_CAP","BHP","MPG","ACCEL"]
        resobj.verify_riser_legends("TableChart_1", legend, "Step 06.20: Verify legend")
          
        """
            Step 07 : Click the Run button.         
            Expect to see the following Line chart with 13 points on lines for each country.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 10)
        
        utillobj.switch_to_frame(pause=2)
        
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'COUNTRY', "Step 07.1: Verify X-Axis Title")
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval1_list=['0', '20K', '40K', '60K', '80K', '100K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        expected_yval2_list=['0', '300', '600', '900', '1,200', '1,500']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 13, 'Step 07.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue", "Step 07.6: Verify  1st bar color",attribute_type='stroke')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g0!mline!", "pale_green", "Step 07.7: Verify  2nd bar color",attribute_type='stroke')
        legend=["DEALER_COST","RETAIL_COST","SALES","WEIGHT","RPM","LENGTH","WIDTH","HEIGHT","WHEELBASE","FUEL_CAP","BHP","MPG","ACCEL"]
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 07.8: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES, WEIGHT, RPM, LENGTH, WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY', 'Step 07.9: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.10: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
 
        """
            Step 08 : Hover over the point on the second line from the top for England.
            Expect to see the Tooltip information for Length that related to the right-side axis scale.
            Hover over the point on the third line from the top for England.
            Expect to see the Tooltip information for Retail_Cost that related to the left-side axis scale.
        """
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='right')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'LENGTH:741', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s5!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 08.1: Verify tooltip')
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='left')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'RETAIL_COST:45,319', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s1!g0!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 08.2: Verify tooltip')
       
        """
            Step 09 : Hover over the point on the third line from the top for W GERMANY.                   
            Expect to see the Tooltip information for Retail_Cost that related to the left-side axis scale.
            Hover over the point on the bottom line for W GERMANY.
            Expect to see the Tooltip information for Accel that related to the right-side axis scale.
        """
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='right')
        expected_tooltip_list=['COUNTRY:W GERMANY', 'RETAIL_COST:64,732', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s1!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 08.1: Verify tooltip')
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='bottom_right')
        expected_tooltip_list=['COUNTRY:W GERMANY', 'ACCEL:13', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s12!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 09.2: Verify tooltip')
        
        """
            Step 10 : Close the chart.Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """  
        
if __name__ == '__main__':
    unittest.main()     