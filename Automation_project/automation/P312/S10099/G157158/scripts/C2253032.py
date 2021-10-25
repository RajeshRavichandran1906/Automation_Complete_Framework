'''
Created on Feb 23, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253032
TestCase Name: Legend title doesn't change upon drilldown
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2253032_TestClass(BaseTestCase):

    def test_C2253032(self):
        
        """
        Class Objects
        """
        core_meta = CoreMetaData(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253032'
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click "Cost of Goods" and "Store,Business,Sub Region".
        """
        field_name='Cost of Goods'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='yaxis-labels']"
        visual.wait_for_number_of_element(element_css, expected_number=9)
        core_meta.collapse_data_field_section('Filters and Variables')
        field_name='Store,Business,Sub Region'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=15)
        
        """
        verify label values
        """
        x_axis_title=['Store Business Sub Region']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M']
        visual.verify_x_axis_title(x_axis_title, msg='Step 02.01: Verify x_axis title')
        visual.verify_y_axis_title(y_axis_title, msg='Step 02.02: Verify x_axis title')
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step 02.03: Verify x_axis label')
        visual.verify_y_axis_label(y_axis_label, msg='Step 02.04: Verify x_axis label')
     
        """
        Step 03 : Hover over "Europe" bar.
        Verify the tool tip:
        """     
        europe_riser="riser!s0!g5!mbar!"
        tooltip_list=['Store Business Sub Region:Europe', 'Cost of Goods:$283,977,869.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to Store Country']
        visual.verify_tooltip(europe_riser, tooltip_list, msg='Step 03.01: Verify tooltip')

        
        """
        Step 04 : Click Change drop down > Select "Pie" chart.
        """
        visual.change_chart_type('pie')
        element_css="#MAINTABLE_wbody1_f svg g text[class^='legend-la']"
        visual.wait_for_number_of_element(element_css, expected_number=14)
        
        """
        Verify chart is changed to Pie
        """
        expected_legend_list=['Store Business Sub Region', 'Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        visual.verify_legends(expected_legend_list, msg='Step 04.01')
        label_list=['Cost of Goods']
        visual.verify_pie_label_in_single_group(label_list, msg='Step 04.02')
        parent_css="#MAINTABLE_wbody1_f svg g path[class^='riser']"
        total_risers=14
        visual.verify_number_of_risers(parent_css, 1, total_risers, msg='Step 04.03')
        west_css='riser!s13!g0!mwedge!'
        visual.verify_chart_color_using_get_css_property("path[class='"+west_css+"']", 'tea_green', msg='Step 04.04')
#         tooltip_list=['Store Business Sub Region:West', 'Cost of Goods:$260,321,331.00  (34.19%)', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to Store Country']
#         visual.verify_tooltip(west_css, tooltip_list, msg='Step 04.05')
        
        """
        Step 05 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='legend-la']"
        visual.wait_for_number_of_element(element_css, expected_number=14)
        
        """
        Step 06 : Hover over West > Drill down to Store Country
        """
        #MAINTABLE_wbody1
        west_css='riser!s13!g0!mwedge!'
        visual.select_tooltip(west_css, 'Drill down to Store Country')
        
        element_css="#MAINTABLE_wbody1_f svg g text[class^='legend-la']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        """
        Verify chart changes to show one color, legend value show United States.
        verify Legend title display Store, Country
        """
        expected_legend_list=['Store Country', 'United States']
        visual.verify_legends(expected_legend_list, msg='Step 06.01')
        label_list=['Cost of Goods']
        visual.verify_pie_label_in_single_group(label_list, msg='Step 06.02')
        parent_css="#MAINTABLE_wbody1_f svg g path[class^='riser']"
        total_risers=1
        visual.verify_number_of_risers(parent_css, 1, total_risers, msg='Step 06.03')
        united_states_css='riser!s0!g0!mwedge!'
        visual.verify_chart_color_using_get_css_property("path[class='"+united_states_css+"']", 'bar_blue', msg='Step 06.04')

        """
        Step 7 : Close the output window
        """
        visual.switch_to_previous_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='legend-la']"
        visual.wait_for_number_of_element(element_css, expected_number=14)
        
        """
        Step 8 : Click "Save" in the toolbar > Type C2141610 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
      
        """
        Step 9 : Logout of the IA API using the following URL.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main() 