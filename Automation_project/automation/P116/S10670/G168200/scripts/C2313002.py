'''
Created on Sep 18, 2017

@author: Pavithra

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313002
TestCase Name = AHTML: StreamGraph Basic chart limit tests.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous,ia_resultarea,visualization_metadata
from common.lib import utillity, core_utility


class C2313002_TestClass(BaseTestCase):

    def test_C2313002(self):
        
#         Test_Case_ID="C2313002"
        """
        TESTCASE VARIABLES
        """     
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        time_out = 90
        
        """
        Step 01:Open FEX:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamBasic.fex&tool=Chart
        Add additional Dimension(X-axis) fields:
        COUNTRY & BODYTYPE.
        Expect to see the following Active Streamgraph Preview pane.
        The limit for X-axis fields is 3.
        """
        utillobj.infoassist_api_edit("StreamBasic", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, time_out)
         
        metadataobj.datatree_field_click('COUNTRY', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='COUNTRY', expire_time=time_out)
         
        metadataobj.datatree_field_click('BODYTYPE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, visble_element_text='BODYTYPE', expire_time=time_out)
         
        resobj.verify_xaxis_title("TableChart_1", 'CAR : COUNTRY : BODYTYPE', "Step 01.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 01.02: Verify XY Label')
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('TableChart_1', expected_label_list, 'Step 01.03: Verify Legends ')
        utillobj.verify_chart_color('TableChart_1', 'riser!s1!g0!marea', 'bar_green', 'Step 01.04: Verify Color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g0!marea', 'bar_blue1', 'Step 01.05: Verify Color')
        ia_resultobj.verify_number_of_chart_segment('TableChart_1', 2, 'Step 01.06: Verify Number of riser', custom_css="path[class^='riser']")
        time.sleep(5)
           
        """
        Step 02:Click run
        Hover over the lower area(blue) for BMW.
        Expect t o see the following Tooltip information confirming that CAR, COUNTRY & BODYTYPE are shown, since all values are not visible in the chart X-axis labels.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 02.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 02.02: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 2, 'Step 02.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 02.04: Verify Color')
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST by CAR, COUNTRY, BODYTYPE', 'Step 02.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 02.09: Verify Legends ')
         
        css="#MAINTABLE_wbody0"
        elem= utillobj.validate_and_get_webdriver_object(css, 'Stream Graph runtime parent')
        core_utillobj.move_to_element(elem, element_location="bottom_right")
        expected_tooltip_list=['CAR:BMW', 'COUNTRY:W GERMANY', 'BODYTYPE:SEDAN', 'DEALER_COST:49,500', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g4!mmarker!', verify_tooltip_list=expected_tooltip_list, msg="Step 02:10: verify marker tooltip values", parent_css="#MAINTABLE_wbody0", y_offset=2)
         
        """
        Step 03:Remove Measure(Vertical axis) fields DEALER_COST & RETAIL_COST.
        Add new Measure fields:SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG & ACCEL.
        Click the Run button.
        Expect to see all 8 Vertical axis fields appear both on the chart and as entries in the chart legend.
        """
         
        short_wait=20
        utillobj.switch_to_default_content(pause=2)
        time.sleep(5)
        metadataobj.querytree_field_click('DEALER_COST', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.querytree_field_click('RETAIL_COST', 1, 1, "Delete")
        time.sleep(3)
        metadataobj.datatree_field_click('SEATS', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SEATS', short_wait)
        metadataobj.datatree_field_click('LENGTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, 'LENGTH', short_wait)
        metadataobj.datatree_field_click('WIDTH', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WIDTH', short_wait)
        metadataobj.datatree_field_click('WHEELBASE', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WHEELBASE', short_wait)
        metadataobj.datatree_field_click('FUEL_CAP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(8) td"
        utillobj.synchronize_with_visble_text(parent_css, 'FUEL_CAP', short_wait)
        metadataobj.datatree_field_click('BHP', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        utillobj.synchronize_with_visble_text(parent_css, 'BHP', short_wait)
        metadataobj.datatree_field_click('MPG', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(10) td"
        utillobj.synchronize_with_visble_text(parent_css, 'MPG', short_wait)
        metadataobj.datatree_field_click('ACCEL', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(11) td"
        utillobj.synchronize_with_visble_text(parent_css, 'ACCEL', short_wait)
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 03.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 03.02: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 8, 'Step 03.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 03.04: Verify Color')       
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by CAR, COUNTRY, BODYTYPE', 'Step 03.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['SEATS', 'LENGTH', 'WIDTH', 'WHEELBASE', 'FUEL_CAP', 'BHP', 'MPG', 'ACCEL']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 03.09: Verify Legends ')
        time.sleep(1)
        utillobj.switch_to_default_content(pause=4)
          
        metadataobj.verify_query_pane_field('Vertical Axis','SEATS',1,"Step 03.11: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','LENGTH',2,"Step 03.12: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','WIDTH',3,"Step 03.13: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','WHEELBASE',4,"Step 03.14: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','FUEL_CAP',5,"Step 03.15: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','BHP',6,"Step 03.16: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','MPG',7,"Step 03.17: Verify query pane")
        metadataobj.verify_query_pane_field('Vertical Axis','ACCEL',8,"Step 03.18: Verify query pane")
         
        """
        Step 04:Move all 8 fields from the Vertical axis area to the Tooltip area.
        Expect to see all 8 fields now under the Tooltip area in the Preview pane.
        """
         
        metadataobj.drag_and_drop_query_items("SEATS", "Tooltip")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SEATS', short_wait)
        metadataobj.drag_and_drop_query_items("LENGTH", "SEATS")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'LENGTH', short_wait)
        metadataobj.drag_and_drop_query_items("WIDTH", "LENGTH")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WIDTH', short_wait)
        metadataobj.drag_and_drop_query_items("WHEELBASE", "WIDTH")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'WHEELBASE', short_wait)
        metadataobj.drag_and_drop_query_items("FUEL_CAP", "WHEELBASE")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'FUEL_CAP', short_wait)
        metadataobj.drag_and_drop_query_items("BHP", "FUEL_CAP")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'BHP', short_wait)
        metadataobj.drag_and_drop_query_items("MPG", "BHP")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'MPG', short_wait)
        metadataobj.drag_and_drop_query_items("ACCEL", "MPG")
        parent_css="#queryTreeWindow table tr:nth-child(18) td"
        utillobj.synchronize_with_visble_text(parent_css, 'ACCEL', short_wait)
         
        metadataobj.verify_query_pane_field('Tooltip','SEATS',1,"Step 04.01: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','LENGTH',2,"Step 04.02: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WIDTH',3,"Step 04.03: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','WHEELBASE',4,"Step 04.04: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','FUEL_CAP',5,"Step 04.05: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','BHP',6,"Step 04.06: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','MPG',7,"Step 04.07: Verify query pane")
        metadataobj.verify_query_pane_field('Tooltip','ACCEL',8,"Step 04.08: Verify query pane")
        
        """
        Step 05:Add new fields DEALER_COST, RETAIL_COST, SALES & RPM to the Vertical axis area.
        Expect to see Preview pane, now with
        DEALER_COST, RETAIL_CO
        ST, SALES & RPM under the Vertical axis area.
        """
        metadataobj.datatree_field_click('DEALER_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        utillobj.synchronize_with_visble_text(parent_css, 'DEALER_COST', short_wait)
         
        metadataobj.datatree_field_click('RETAIL_COST', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        utillobj.synchronize_with_visble_text(parent_css, 'RETAIL_COST', short_wait)
        metadataobj.datatree_field_click('SALES', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        utillobj.synchronize_with_visble_text(parent_css, 'SALES', short_wait)
        metadataobj.datatree_field_click('RPM', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(7) td"
        utillobj.synchronize_with_visble_text(parent_css, 'RPM', short_wait)
         
        metadataobj.verify_query_pane_field('Vertical Axis', 'DEALER_COST', 1, "Step 05.01")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RETAIL_COST', 2, "Step 05.02")
        metadataobj.verify_query_pane_field('Vertical Axis', 'SALES', 3, "Step 05.03")
        metadataobj.verify_query_pane_field('Vertical Axis', 'RPM', 4, "Step 05.04")
          
        """
        Step 06:Click the Run button.
        Expect to see the following Streamgraph, 
        now with 4 Vertical axis and 3 Horizontal axis fields.
        """
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", 'CAR : COUNTRY : BODYTYPE', "Step 06.01: Verify X-Axis Title")
        expected_xval_list=['ALFA ROMEO : ITALY : COUPE', 'ALFA ROMEO : ITALY : ROADSTER', 'ALFA ROMEO : ITALY : SEDAN', 'AUDI : W GERMANY : SEDAN', 'BMW : W GERMANY : SEDAN', 'DATSUN : JAPAN : SEDAN', 'JAGUAR : ENGLAND : CONVERTIBLE', 'JAGUAR : ENGLAND : SEDAN', 'JENSEN : ENGLAND : SEDAN', 'MASERATI : ITALY : COUPE', 'PEUGEOT : FRANCE : SEDAN', 'TOYOTA : JAPAN : SEDAN', 'TRIUMPH : ENGLAND : HARDTOP']
        expected_yval_list=[]
        resobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 06.02: Verify XY Label')
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 06.03: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody0', 'riser!s0!g0!marea', 'bar_blue1', 'Step 06.04: Verify Color')       
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, RETAIL_COST, SALES, RPM, SEATS, LENGTH, WIDTH, WHEELBASE, FUEL_CAP, BHP, MPG, ACCEL by CAR, COUNTRY, BODYTYPE', 'Step 06.05: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.06: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.07: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.08: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_label_list=['DEALER_COST', 'RETAIL_COST', 'SALES', 'RPM']
        resobj.verify_riser_legends('MAINTABLE_wbody0', expected_label_list, 'Step 06.09: Verify Legends ')
        time.sleep(5)

        """
        Step 07:Hover over the lower area(blue) for Alfa Romeo.
        Expect to see the following Tooltip information, combining all Vertical axis fields, the applicable Horizontal fields and the 8 Tooltip fields.
        """
        elem= utillobj.validate_and_get_webdriver_object(css, 'Stream Graph runtime parent')
        core_utillobj.move_to_element(elem, element_location="bottom_left")
        
        css="marker!s0!g0!mmarker!"
        expected_tooltip_list=['CAR:ALFA ROMEO', 'COUNTRY:ITALY', 'BODYTYPE:COUPE', 'DEALER_COST:5,660', 'SEATS:2', 'LENGTH:163', 'WIDTH:62', 'WHEELBASE:92.5', 'FUEL_CAP:14.0', 'BHP:0', 'MPG:21', 'ACCEL:0', 'Filter Chart', 'Exclude from Chart']
        miscelaneousobj.select_or_verify_marker_tooltip(css, verify_tooltip_list=expected_tooltip_list, msg="Step 07.01: verify marker tooltip values", parent_css="#MAINTABLE_wbody0",y_offset=2)
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(2)
                
        """
        Step 08 Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()     