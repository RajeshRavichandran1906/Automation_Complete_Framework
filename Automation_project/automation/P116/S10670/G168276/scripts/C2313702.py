'''
Created on Nov 10, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10670&group_by=cases:section_id&group_id=168200&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313702
TestCase Name = AHTML: Horizontal Dual-Axis Stacked Line Chart Filter/Exclude tests.
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_resultarea,active_miscelaneous, ia_resultarea
# from common.wftools import visualization
from common.lib import utillity
# from common.lib import core_utility
from common.lib.core_utility import CoreUtillityMethods

class C2313702_TestClass(BaseTestCase):

    def test_C2313702(self):
        
        """
        TESTCASE VARIABLES
        """ 
#         Test_Case_ID = "C2313702"
            
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        coreutil=CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
#         visobj = visualization.Visualization(self.driver)
        
        """
        Step 01: Open FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FHorizontal_Stacked_Line.fex&tool=Chart
        """
        utillobj.infoassist_api_edit("Horizontal_Stacked_Line", 'chart', 'P116/S10670', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(20)
        parent_css="#pfjTableChart_1 g.chartPanel"
        utillobj.synchronize_with_visble_text(parent_css, "CAR", miscelaneousobj.chart_medium_timesleep)
        time.sleep(5)
        
        """
        Expect to see the following Preview pane, including axis on both sides of the canvas.
        """
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
        Step 02: Click the Run button.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
            
        """Expect to see the following Horizontal Dual-Axis Stacked Line Chart."""
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 g.chartPanel"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 02.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 02.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 02.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 02.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 02.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 02.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 02.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 02.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 02.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
             
        """
        Step 03: Hover over the point on the left line for Triumph. Select Exclude from Chart..
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g9!mmarker!', select_tooltip='Exclude from Chart', msg='Step 3.1 : seleted marker tooltip')
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_left')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g9!mmarker!", tooltip_css, 'Exclude from Chart', element_location='bottom_left', javascript_marker_enable=True, mouse_duration=3.5)
            
        """
        Expect to see the following Line Chart, with Triumph lines removed.
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 03.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 03.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 03.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 03.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 03.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 03.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 03.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 03.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 03.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 03.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
         
        """
        Step 04: Hover over the point on the left line for Toyota. Select Exclude from Chart.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g8!mmarker!', select_tooltip='Exclude from Chart', msg='Step 4.1 : seleted marker tooltip')
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_left')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g8!mmarker!", tooltip_css, 'Exclude from Chart', element_location='bottom_left', javascript_marker_enable=True, mouse_duration=3.5)
            
        """
        Expect to see the following Line Chart, with Triumph and Toyota lines removed.
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 04.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 04.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 04.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 04.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 04.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 04.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 04.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 04.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 04.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
            
        """
        Step 05: Hover over the point on the left line for Peugeot Select Remove Filter.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g7!mmarker!', select_tooltip='Remove Filter', msg='Step 5.1 : seleted marker tooltip')
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_left')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(5)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g7!mmarker!", tooltip_css, 'Remove Filter', element_location='bottom_left', javascript_marker_enable=True, mouse_duration=3.5)
             
        """Expect to see the original Line Chart with Triumph & Toyota lines restored."""
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 05.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 05.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 05.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 05.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 05.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 05.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 05.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 05.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 05.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
           
        """
        Step 06: Left-click and draw a box around the 8 points for Alfa Romeo & Audi at the top. Select Exclude from Chart.
        """
        
#         source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g0!mmarker!']")
#         target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s2!g3!mmarker!']")
#         visobj.create_lasso(source_element, target_element, source_xoffset=-15, target_xoffset=10, source_element_location='middle_left')
#         visobj.select_lasso_tooltip('Exclude from Chart')
        
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g1!mmarker!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s3!g0!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        time.sleep(3)
        more_option=driver.find_element_by_css_selector('div[title="More Options"]')
        coreutil.python_move_to_element(more_option)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-30,sy_offset=source_elem['y']+30,tx_offset=target_elem['x']+30,ty_offset=target_elem['y']-30)
        resobj.select_or_verify_lasso_filter(select='Exclude from Chart')
        
        
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g1!mmarker!']")
#         coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
#         sx=coord['x']-20
#         sy=coord['y']+20
#         time.sleep(2)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s3!g0!mmarker!']")
#         coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
#         tx=coord['x']+20
#         ty=coord['y']-20
#         time.sleep(2)
#         utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
#         time.sleep(3)
#         resobj.select_or_verify_lasso_filter(select='Exclude from Chart') 
         
        """
        Expect to see the following Line chart with both Alfa Romeo & Audi lines removed.
        """
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 8, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 06.1: Verify X-Axis Title")  
        expected_xval_list=['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 06.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 06.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 06.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 06.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 06.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 06.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 06.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 06.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 06.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
        Step 07: Hover over the point on the left-most line for Triumph. Select Remove Filter.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g7!mmarker!', select_tooltip='Remove Filter', msg='Step 7.1 : seleted marker tooltip')
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_left')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(4)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g7!mmarker!", tooltip_css, 'Remove Filter', element_location='bottom_left', javascript_marker_enable=True, mouse_duration=3.5)
#          
        """Expect to see the original Line Chart with Jaguar and Jensen lines restored."""
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 07.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 07.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 07.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 07.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 02.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 07.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 07.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 07.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 07.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
        Step 08: Left-click and draw a box around the 12 points for Peugeot, Toyota & Triumph. Select Filter Chart.
        """
        
        elem1=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g7!mmarker!']")
        source_elem=utillobj.enable_marker_using_javascript(elem1)
        elem2=driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s3!g9!mmarker!']")
        target_elem=utillobj.enable_marker_using_javascript(elem2)  
        time.sleep(3)
        more_option=driver.find_element_by_css_selector('div[title="More Options"]')
        coreutil.python_move_to_element(more_option)
        utillobj.drag_drop_on_screen(sx_offset=source_elem['x']-25,sy_offset=source_elem['y']-10,tx_offset=target_elem['x']+30,ty_offset=target_elem['y']+30)
        resobj.select_or_verify_lasso_filter(select='Filter Chart')
        
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s0!g7!mmarker!']")
#         coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
#         sx=coord['x']-40
#         sy=coord['y']-30
#         time.sleep(2)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0 [class*='marker!s3!g9!mmarker!']")
#         coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
#         tx=coord['x']+20
#         ty=coord['y']+20
#         time.sleep(2)
#         utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
#         time.sleep(3)
#         resobj.select_or_verify_lasso_filter(select='Filter Chart') 
         
        """Expect to see the following Line Chart with lines for Peugeot, Toyota & Triumph only.""" 
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 3, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 08.1: Verify X-Axis Title")  
        expected_xval_list=['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 08.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 08.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 08.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 08.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 08.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 08.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 08.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 08.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
        Step 09: Hover over the point on the bottom left line for Triumph. Click Exclude from Chart.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g2!mmarker!', select_tooltip='Exclude from Chart', msg='Step 9.1 : seleted marker tooltip')
#         time.sleep(5)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(3)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g2!mmarker!", tooltip_css, 'Exclude from Chart', element_location='bottom_middle', javascript_marker_enable=True, mouse_duration=3.5)
         
        """Expect to see the following Line Chart with lines for only Peugeot & Toyota."""
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 2, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 09.1: Verify X-Axis Title")  
        expected_xval_list=['PEUGEOT', 'TOYOTA']
        expected_yval1_list=['0', '1,000', '2,000', '3,000', '4,000', '5,000', '6,000', '7,000', '8,000']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 09.2: Verify XY labels")
        expected_yval2_list=['0', '40', '80', '120', '160', '200', '240', '280']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 09.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 09.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 09.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 09.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 09.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 09.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 09.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 09.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
         
        """
        Step 10: Hover over the point on the bottom left line for Toyota. Select Remove Filter.
        """
        miscelaneousobj.select_or_verify_marker_tooltip('marker!s0!g1!mmarker!', select_tooltip='Remove Filter', msg='Step 10.1 : seleted marker tooltip')
#         time.sleep(5)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody0")
#         utillobj.click_on_screen(parent_elem, 'bottom_middle')
#         time.sleep(5)
#         tooltip_css="#MAINTABLE_wbody0 span[id*='tdgchart-tooltip'][style*='visible'] [onclick^='ibiChart']:nth-child(4)"
#         visobj.select_tooltip_with_limited_search("#MAINTABLE_wbody0", "marker!s0!g1!mmarker!", tooltip_css, 'Remove Filter', element_location='bottom_middle', javascript_marker_enable=True, mouse_duration=3.5)
         
        """Expect to see the original Line Chart with all lines restored."""
        time.sleep(3)
        parent_css="#MAINTABLE_wbody0 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 10, 30)
        resobj.verify_xaxis_title("MAINTABLE_wbody0", "CAR", "Step 10.1: Verify X-Axis Title")  
        expected_xval_list=['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        expected_yval1_list=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval1_list, "Step 10.2: Verify XY labels")
        expected_yval2_list=['0', '400', '800', '1,200', '1,600']
        resobj.verify_riser_chart_XY_labels("MAINTABLE_wbody0", expected_xval_list, expected_yval2_list, "Step 10.3: Verify XY labels", y_custom_css="svg > g text[class^='y2axis-labels']")
        ia_resultobj.verify_number_of_chart_segment('MAINTABLE_wbody0', 4, 'Step 10.4: Verify Number of riser', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mline!", "bar_blue1", "Step 10.6: Verify  1st bar color",attribute_type='stroke')
        legend=['DEALER_COST', 'WEIGHT', 'LENGTH', 'HEIGHT']
        resobj.verify_riser_legends("MAINTABLE_wbody0", legend, "Step 10.7: Verify Y-Axis legend")
        miscelaneousobj.verify_chart_title('MAINTABLE_wbody0_ft', 'DEALER_COST, WEIGHT, LENGTH, HEIGHT by CAR', 'Step 10.8: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['More Options','Advanced Chart','Original Chart'],"Step 10.9: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Aggregation'],"Step 10.10: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('MAINTABLE_wmenu0', ['Sum'],"Step 10.11: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(8)
        element= driver.find_element_by_css_selector("#MAINTABLE_wbody0")
        utillobj.take_screenshot(element,'C2313702_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 11: Close the chart.
        Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(1)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()
