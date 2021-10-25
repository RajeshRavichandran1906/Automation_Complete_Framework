'''
Created on Nov 15, 2017

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313697
TestCase Name = AHTML: Horizontal Dual-Axis Absolute Line Chart Limit functionality.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity
from common.wftools import visualization

class C2313697_TestClass(BaseTestCase):

    def test_C2313697(self):
        
        Test_Case_ID="C2313697" 
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneous_obj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visobj = visualization.Visualization(self.driver)
        
        '''
        Step 01 : Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Absolute_Line.fex&tool=Chart
        '''
        utillobj.infoassist_api_edit("Horizontal_Absolute_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 text[class='yaxis-title']"
        utillobj.synchronize_with_visble_text(element_css, "DEALER_COST", 65)
        
        '''
        Step 01.1 : Expect to see the following Preview pane, including axis on both sides of the canvas.
        '''
        expected_xaxis_label=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_y2axis_label=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 01.1 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        resobj.verify_xaxis_title('pfjTableChart_1','CAR','Step 01.2 : Verify X Asix title')
        resobj.verify_yaxis_title('pfjTableChart_1','DEALER_COST','Step 01.3 : Verify Y Axis title')
        resobj.verify_yaxis_title('pfjTableChart_1','LENGTH','Step 01.4 : Verify Y2 Axis title',custom_css="text[class='y2axis-title']")
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1',2,'Step 01.5 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g0!mline!','bar_blue','Step 01.6 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s1!g0!mline!','pale_green','Step 01.7 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('pfjTableChart_1',['DEALER_COST','LENGTH'],'Step 01.8 : Verify chart legend labels')
        
        '''
        Step 02. : Click the Run button.
        '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 35)
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
        '''
        Step 02.1 : Expect to see the following Horizontal Dual-Axis Absolute Line Chart.
        '''  
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft','DEALER_COST, LENGTH by CAR','Step 02.1 : Verify line chart title')
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xaxis_label, expected_yaxis_label,'Step 02.2 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        resobj.verify_xaxis_title('MAINTABLE_wbody0_f','CAR','Step 02.3 : Verify X Asix title')
        resobj.verify_yaxis_title('MAINTABLE_wbody0_f','DEALER_COST','Step 02.4 : Verify Y Axis title')
        resobj.verify_yaxis_title('MAINTABLE_wbody0_f','LENGTH','Step 02.5 : Verify Y2 Axis title',custom_css="text[class='y2axis-title']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0_f',2,'Step 02.6 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s0!g0!mline!','bar_blue','Step 02.7 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s1!g0!mline!','pale_green','Step 02.8 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('MAINTABLE_wbody0_f',['DEALER_COST','LENGTH'],'Step 02.9 : Verify chart legend labels')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        utillobj.switch_to_default_content(pause=3)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element,Test_Case_ID+'_Actual_step_02', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''
        Step 03 : Double click on fields COUNTRY & MODEL to add them to the Vertical axis bucket under CAR.
        '''
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY', 10)

        metaobj.datatree_field_click('MODEL', 2, 1)
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:MODEL', 10)
        
        '''
        Step 03.1 : Expect to see the following Preview pane, with Car, Country & Model added to the Vertical axis bucket and the additional fields appearing in the Y axis label area.
        '''
        expected_xaxis_label=['ALFA ROMEO : ITALY : 2000 4 DOOR BERLINA', 'ALFA ROMEO : ITALY : 2000 GT VELOCE', 'ALFA ROMEO : ITALY : 2000 SPIDER VELOCE', 'AUDI : W GERMANY : 100 LS 2 DOOR AUTO', 'BMW : W GERMANY : 2002 2 DOOR', 'BMW : W GERMANY : 2002 2 DOOR AUTO', 'BMW : W GERMANY : 3.0 SI 4 DOOR', 'BMW : W GERMANY : 3.0 SI 4 DOOR AUTO', 'BMW : W GERMANY : 530I 4 DOOR', 'BMW : W GERMANY : 530I 4 DOOR AUTO', 'DATSUN : JAPAN : B210 2 DOOR AUTO', 'JAGUAR : ENGLAND : V12XKE AUTO', 'JAGUAR : ENGLAND : XJ12L AUTO', 'JENSEN : ENGLAND : INTERCEPTOR III', 'MASERATI : ITALY : DORA 2 DOOR', 'PEUGEOT : FRANCE : 504 4 DOOR', 'TOYOTA : JAPAN : COROLLA 4 DOOR DIX AUTO', 'TRIUMPH : ENGLAND : TR7']
        expected_yaxis_label=['0', '4K', '8K', '12K', '16K', '20K', '24K', '28K']
        expected_y2axis_label=['0', '40', '80', '120', '160', '200', '240']
        resobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 03.1 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        resobj.verify_xaxis_title('pfjTableChart_1','CAR : COUNTRY : MODEL','Step 03.2 : Verify X Asix title')
        resobj.verify_yaxis_title('pfjTableChart_1','DEALER_COST','Step 03.3 : Verify Y Axis title')
        resobj.verify_yaxis_title('pfjTableChart_1','LENGTH','Step 03.4 : Verify Y2 Axis title',custom_css="text[class='y2axis-title']")
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1',2,'Step 03.5 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g0!mline!','bar_blue','Step 03.6 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s1!g0!mline!','pale_green','Step 03.7 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('pfjTableChart_1',['DEALER_COST','LENGTH'],'Step 03.8 : Verify chart legend labels')
        metaobj.verify_query_pane_field('Vertical Axis','CAR',1,'Step 03.9')
        metaobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,'Step 03.10')
        metaobj.verify_query_pane_field('Vertical Axis','MODEL',3,'Step 03.11')
        
        '''
        Step 04 : Double click field BODYTYPE.
        '''
        metaobj.datatree_field_click('BODYTYPE', 2, 1)
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'CAR:COUNTRY:BODYTYPE', 10)
        
        '''
        Step 04.1 : Expect to see the following Preview pane, with Car, Country & Bodytype under the Vertical axis bucket.Bodytype replaced Model. 
        Vertical axis(Dimension) is limited to 3 fields.
        '''
        expected_xaxis_label=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yaxis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        expected_y2axis_label=['0', '300', '600', '900', '1,200']
        resobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 04.1 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        resobj.verify_xaxis_title('pfjTableChart_1','CAR : COUNTRY : BODYTYPE','Step 04.2 : Verify X Asix title')
        resobj.verify_yaxis_title('pfjTableChart_1','DEALER_COST','Step 04.3 : Verify Y Axis title')
        resobj.verify_yaxis_title('pfjTableChart_1','LENGTH','Step 04.4 : Verify Y2 Axis title',custom_css="text[class='y2axis-title']")
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1',2,'Step 04.5 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g0!mline!','bar_blue','Step 04.6 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s1!g0!mline!','pale_green','Step 04.7 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('pfjTableChart_1',['DEALER_COST','LENGTH'],'Step 04.8 : Verify chart legend labels')
        metaobj.verify_query_pane_field('Vertical Axis','CAR',1,'Step 04.9')
        metaobj.verify_query_pane_field('Vertical Axis','COUNTRY',2,'Step 04.10')
        metaobj.verify_query_pane_field('Vertical Axis','BODYTYPE',3,'Step 04.11')
        metaobj.verify_query_pane_field('Vertical Axis','Horizontal Axis 1',4,'Step 04.12')
        
        '''
        Step 05 : Click the Run button.
        '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 10)
        
        utillobj.switch_to_frame(pause=2)
        
        '''
        Step 05.1 : Hove over the point on the first value for Alfa Romeo.
        Expect to see that Country and Bodytype follow Car in the Tooltip, as sort fields(Vertical axis bucket).
        '''
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft','DEALER_COST, LENGTH by CAR, COUNTRY, BODYTYPE','Step 05.1 : Verify line chart title')
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xaxis_label, expected_yaxis_label,'Step 05.2 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        resobj.verify_xaxis_title('MAINTABLE_wbody0_f','CAR : COUNTRY : BODYTYPE','Step 05.3 : Verify X Asix title')
        resobj.verify_yaxis_title('MAINTABLE_wbody0_f','DEALER_COST','Step 05.4 : Verify Y Axis title')
        resobj.verify_yaxis_title('MAINTABLE_wbody0_f','LENGTH','Step 05.5 : Verify Y2 Axis title',custom_css="text[class='y2axis-title']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0_f',2,'Step 05.6 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s0!g0!mline!','bar_blue','Step 05.7 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s1!g0!mline!','pale_green','Step 05.8 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('MAINTABLE_wbody0_f',['DEALER_COST','LENGTH'],'Step 05.9 : Verify chart legend labels')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.10: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.11: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.12: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='left')
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s0!g0!mmarker', expected_tooltip_list, 'Step 02.7: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        
        utillobj.switch_to_default_content(pause=3)
        
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element,Test_Case_ID+'_Actual_step_05', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''
        Step 06 : Delete fields Car & Bodytype from the Vertical Axis bucket.
        '''
        metaobj.querytree_field_click('CAR',1,1,'Delete')
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY:BODYTYPE', 10)
        
        metaobj.querytree_field_click('BODYTYPE',1,1,'Delete')
        element_css="#pfjTableChart_1 [class='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(element_css, 'COUNTRY', 10)
         
        '''
        Step 06 : Add fields RETAIL_COST, SALES, WEIGHT & RPM to the Horizontal Axis 1 bucket.
        '''
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        element_css="#TableChart_1 text[class^='legend-labels!s1!']"
        utillobj.synchronize_with_visble_text(element_css, "RETAIL_COST", 10)
        
        metaobj.datatree_field_click('SALES', 2, 1)
        element_css="#TableChart_1 text[class^='legend-labels!s2!']"
        utillobj.synchronize_with_visble_text(element_css, "SALES", 10)
        
        metaobj.datatree_field_click('WEIGHT', 2, 1)
        element_css="#TableChart_1 text[class^='legend-labels!s3!']"
        utillobj.synchronize_with_visble_text(element_css, "WEIGHT", 10)
        
        metaobj.datatree_field_click('RPM', 2, 1)
        element_css="#TableChart_1 text[class^='legend-labels!s4!']"
        utillobj.synchronize_with_visble_text(element_css, "RPM", 10)
        
        '''
        Step 06 : Add fields WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL to the Horizontal Axis 2 bucket.
        '''
        
        metaobj.drag_drop_data_tree_items_to_query_tree('WIDTH', 1, 'LENGTH',0)
        element_css="#TableChart_1 text[class^='legend-labels!s6!']"
        utillobj.synchronize_with_visble_text(element_css, "WIDTH", 10)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('HEIGHT', 1, 'WIDTH',0)
        element_css="#TableChart_1 text[class^='legend-labels!s7!']"
        utillobj.synchronize_with_visble_text(element_css, "HEIGHT", 10)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('WHEELBASE', 1, 'HEIGHT',0)
        element_css="#TableChart_1 text[class^='legend-labels!s8!']"
        utillobj.synchronize_with_visble_text(element_css, "WHEELBASE", 10)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('FUEL_CAP', 1, 'WHEELBASE',0)
        element_css="#TableChart_1 text[class^='legend-labels!s9!']"
        utillobj.synchronize_with_visble_text(element_css, "FUEL_CAP", 10)
         
        metaobj.drag_drop_data_tree_items_to_query_tree('BHP', 1, 'FUEL_CAP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s10!']"
        utillobj.synchronize_with_visble_text(element_css, "BHP", 10)
       
        metaobj.drag_drop_data_tree_items_to_query_tree('MPG', 1, 'BHP',0)
        element_css="#TableChart_1 text[class^='legend-labels!s11!']"
        utillobj.synchronize_with_visble_text(element_css, "MPG", 10)
       
        metaobj.drag_drop_data_tree_items_to_query_tree('ACCEL', 1, 'MPG',0)
        element_css="#TableChart_1 text[class^='legend-labels!s12!']"
        utillobj.synchronize_with_visble_text(element_css, "ACCEL", 10)
        
        '''
        Step 06.1 : Expect to see the additional fields in the Preview pane. There should be 5 fields under the Horizontal Axis 1 bucket and 8 fields under the Horizontal Axis 2 bucket.
        '''
        field_names=['DEALER_COST','RETAIL_COST','SALES','WEIGHT','RPM','Horizontal Axis 2','LENGTH','WIDTH','HEIGHT','WHEELBASE','FUEL_CAP','BHP','MPG','ACCEL','Marker']
        position=1
        for field in field_names :
            metaobj.verify_query_pane_field('Horizontal Axis 1',field,position,'Step 06.1'+str(position))
            position+=1
        
        '''
        Step 6.2 : Veriy preview pane
        '''
        expected_xaxis_label=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yaxis_label=['0', '20K', '40K', '60K', '80K', '100K']
        expected_y2axis_label=['0', '300', '600', '900', '1,200', '1,500']
        resobj.verify_riser_chart_XY_labels('pfjTableChart_1', expected_xaxis_label, expected_yaxis_label,'Step 06.2.1 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        ia_resultobj.verify_number_of_chart_segment('pfjTableChart_1',13,'Step 06.2.2 : Verify number of line risers',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('pfjTableChart_1','riser!s0!g0!mline!','bar_blue','Step 06.2.3 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('pfjTableChart_1','riser!s1!g0!mline!','pale_green','Step Step 06.2.3 : Verify line chart color', attribute_type='stroke')
        expected_legends=['DEALER_COST', 'RETAIL_COST', 'SALES', 'WEIGHT', 'RPM', 'LENGTH', 'WIDTH', 'HEIGHT', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends('pfjTableChart_1',expected_legends,'Step 06.2.4 : Verify chart legend labels')
         
        '''
        Step 07 : Click the Run button.
        '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        element_css="#resultArea [id^=ReportIframe-]"
        utillobj.synchronize_with_number_of_element(element_css, 1, 20)
        
        utillobj.switch_to_frame(pause=2)
         
        '''
        Step 7.1 : Expect to see the following Bar chart with 13 lines for each country.
        The Horizontal Axis 1 fields use the bottom axis for their scale.
        The Horizontal Axis 2 fields use the top axis for their scale.
        ''' 
        expected_title="DEALER_COST, RETAIL_COST, SALES, WEIGHT, RPM, LENGTH, WIDTH, HEIGHT, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by COUNTRY"
        miscelaneous_obj.verify_chart_title('MAINTABLE_wbody0_ft',expected_title,'Step 07.1 : Verify line chart title')
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0_f', expected_xaxis_label, expected_yaxis_label,'Step 07.2 :',10,z_custom_css=" svg > g text[class^='y2axis-labels'][class*='labels']",z_expected_labels=expected_y2axis_label)
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0_f',13,'Step 07.3 : Verify Expect to see the following Bar chart with 13 lines for each country.',custom_css="g[class='risers'] path[class*='mline']")
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s0!g0!mline!','bar_blue','Step 07.4 : Verify line chart color', attribute_type='stroke')
        utillobj.verify_chart_color('MAINTABLE_wbody0_f','riser!s1!g0!mline!','pale_green','Step 07.5 : Verify line chart color', attribute_type='stroke')
        resobj.verify_riser_legends('MAINTABLE_wbody0_f',expected_legends,'Step 07.6 : Verify chart legend labels')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.8: Verify Chart toolbar")
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.9 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneous_obj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.10 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        '''
        Step 8 : Hover over the point on the first line for England.
        Expect to see the value for field Width to relate to the top axis scale.
        '''
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='start')
        expected_tooltip_list=['COUNTRY:ENGLAND', 'ACCEL:23', 'Filter Chart', 'Exclude from Chart']
        visobj.verify_tooltip('marker!s12!g0!mmarker!', expected_tooltip_list, 'Step 08.1: Verify tooltip',"MAINTABLE_wbody0", element_location='start', use_marker_enable=True)
        
        '''
        Step 9 : Hover over the point on the last line for W Germany.
        Expect to see value for field Sales relate to the bottom axis scale.
        '''
        parent_obj=self.driver.find_element_by_id("MAINTABLE_wbody0_f")
        utillobj.click_on_screen(parent_obj, coordinate_type='bottom_right')
        expected_tooltip_list=['COUNTRY:W GERMANY', 'SALES:88190', 'Filter Chart', 'Exclude from Chart']
        miscelaneous_obj.select_or_verify_marker_tooltip('marker!s2!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg='Step 05.13: Verify tooltip')
        
        utillobj.switch_to_default_content(pause=3)
        element= driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(element,Test_Case_ID+'_Actual_step_09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
if __name__=='__main__' :
    unittest.main()