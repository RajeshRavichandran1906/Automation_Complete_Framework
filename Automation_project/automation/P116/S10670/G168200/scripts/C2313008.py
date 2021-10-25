'''
Created on January 3, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313008
TestCase Name = AHTML: StreamGraph ColorBy chart using additional Buckets.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import chart
from common.lib import base
from common.wftools import active_chart
from common.wftools import visualization


class C2313008_TestClass(BaseTestCase):

    def test_C2313008(self):
        
        """
        Test case objects
        """
        visual_obj = visualization.Visualization(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj = chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        active_chart_obj = active_chart.Active_Chart(self.driver)
        
        """
        Test case CSS
        """
        x_axis_labels = "#MAINTABLE_wbody0 text[class^='xaxis']"
        
        """
        Test case variables
        """
        alfa_romeo_tooltip = ['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        alfa_seat_tooltip = ['SEATS:2', 'CAR:ALFA ROMEO', 'RETAIL_COST:19,565', 'COUNTRY:ITALY', 'SALES:30200', 'Filter Chart', 'Exclude from Chart']
        x_label_list = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        pevgeot_tooltip = ['SEATS:5', 'CAR:PEUGEOT', 'DEALER_COST:4,631', 'COUNTRY:FRANCE', 'SALES:0', 'Filter Chart', 'Exclude from Chart']
        alfa_excluded_x_list = ['AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        alfa_audi_removed_list = ['BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        three_car_list = ['PEUGEOT', 'TOYOTA', 'TRIUMPH']
        bmw_removed_x_list = ['AUDI', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        legend_list = ['DEALER_COST:ENGLAND', 'RETAIL_COST:ENGLAND', 'DEALER_COST:FRANCE', 'RETAIL_COST:FRANCE', 'DEALER_COST:ITALY', 'RETAIL_COST:ITALY', 
                       'DEALER_COST:JAPAN', 'RETAIL_COST:JAPAN', 'DEALER_COST:W GERMANY', 'RETAIL_COST:W GERMANY']
        streamcolor_title = 'DEALER_COST, RETAIL_COST BY COUNTRY, CAR'
        alfa_tooltip = ['CAR:ALFA ROMEO', 'DEALER_COST:16,235', 'COUNTRY:ITALY', 'Filter Chart', 'Exclude from Chart']
        
        """
        Step 1:Open FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10670%2FStreamColorBy.fex&tool=Chart
        Click the Run button.
        Expect to see the following Active Streamgraph.
        """
        chart_obj.invoke_chart_in_edit_mode_using_api('StreamColorBy')
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 1.1: Verify the X axis')
        chart_obj.verify_legends_in_run_window(legend_list,parent_css='#MAINTABLE_wbody0_f', msg='Step 1.2: Verify the legends')
        active_chart_obj.verify_chart_title(streamcolor_title, 'Step 1.3: Verify title',parent_css='#MAINTABLE_wbody0_fmg')
        
        """
        Step 2: Drag the field SALES to the Tooltip area.
        Expect to see the SALES field under the Tooltip area in the Query panel.
        """
        chart_obj.switch_to_default_content()
        chart_obj.drag_field_from_data_tree_to_query_pane('SALES', 1, 'Tooltip', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(12) td", 'SALES', base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Tooltip', 'SALES', 1, 'Step 2.1: Verify Sales under Tooltip')
        
        """
        Step 3: Click the Run button.
        Hover over lower area(red) for Alfa Romeo.
        Expect to see the SALES field added to the Tooltip information.
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_tooltip_in_run_window("marker!s4!g0!mmarker!", alfa_romeo_tooltip, 'Step 3.1: Verify tooltip values',parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        """
        Step 4: Drag the field SEATS to the Multigraph area.
        Expect to see the SEATS field under the Multigraph area in the Query panel.
        """
        chart_obj.switch_to_default_content()
        chart_obj.drag_field_from_data_tree_to_query_pane('SEATS', 1, 'Multi-graph', 1)
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(14) td", 'SEATS', base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Multi-graph', 'SEATS', 1, 'Step 4.1: Verify Seats under Multi-graph')
        
        """
        Step 5: Click the Run button.
        Expect to see the data reordered, with 
        Alfa Romeo first and Peugeot last.
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 11, base_obj.chart_medium_timesleep)
        chart_obj.verify_x_axis_label_in_run_window(x_label_list, parent_css='#MAINTABLE_wbody0_f',msg='Step 5.1: Verify Alfa Romeo first and Triumph last')
        
        """
        Step 6: Hover over the lower area(red) for Alfa Romeo.
        Expect to see 2 Seats for Alfa Romeo.
        This is the lowest value of SEATS.
        """
        chart_obj.verify_tooltip_in_run_window("marker!s4!g0!mmarker!", alfa_seat_tooltip, 'Step 6.1: Verify 2 seats for Alfa Romeo',parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        """
        Step 7: Hover over the lower area(blue) for Peugeot.
        Expect to see 5 Seats for Peugeot.
        This is the highest value of SEATS.
        """
        chart_obj.verify_tooltip_in_run_window("marker!s2!g7!mmarker!", pevgeot_tooltip, 'Step 7.1: Verify 5 seats for Pevgeot',parent_css="#MAINTABLE_wbody0",initial_move_xy_dict={'x':842,'y':551}, use_marker_enable=True)
        
        """
        Step 8: Move the SEATS field from the Multigraph area to the Animate area.
        """
        chart_obj.switch_to_default_content()
        chart_obj.drag_field_within_query_pane('SEATS', 'Animate')
        chart_obj.wait_for_visible_text("#queryTreeWindow table tr:nth-child(15) td", 'SEATS', base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Animate', 'SEATS', 1, 'Step 8.1: Verify Seats under Animate')
        
        """
        Step 9: Click the Run button.
        Hover over the lower area(blue) for Jaguar.
        Expect to see the following Streamgraph, showing only CARs with 2 SEATS.
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_number_of_element(x_axis_labels, 5, base_obj.chart_medium_timesleep)
        chart_obj.verify_tooltip_in_run_window("marker!s4!g0!mmarker!", alfa_seat_tooltip, 'Step 6.1: Verify 2 seats for Alfa Romeo',parent_css="#MAINTABLE_wbody0", use_marker_enable=True)
        
        
        ## TODO: TEST CASE not completed due to issue in JIRA 