'''
Created on Feb 26, 2018
@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102946
Test_Case Name : Drilldown on 2nd hierarchy dimension if integer shows wrong dimension in tooltip
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102946_TestClass(BaseTestCase):

    def test_C2102946(self):
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        wait_time_in_sec=120
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_label, y_label,riser,total_risers,tooltip, expected_legend_list,step_num):
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.2'+' Verify x-axis label',xyz_axis_label_length=4)
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.3'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.4:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'bar_blue',  msg='Step' + step_num + '.5:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.6:'+' Verify riser tooltip',move_to_tooltip=True)
            visual.verify_legends(expected_legend_list, '#MAINTABLE_wbody1_f', 2, msg='Step' + step_num + '.7:'+' Verify Legend')
        """
        Step1:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is)
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10099&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step02: Double click Shipment Unit(s), 'Days,Delayed', 'Shipped,Year' and 'Shipped,Quarter'.
        """
        visual.double_click_on_datetree_item('Shipment Unit(s)', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "ShipmentUnit(s)", 45)
        visual.double_click_on_datetree_item('Days,Delayed', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f .legend text[class='legend-labels!s1!']",'DaysDelayed', 45)
        visual.double_click_on_datetree_item('Shipped,Year', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ShippedYear", 45)
        visual.double_click_on_datetree_item('Shipped,Quarter', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ShippedYear:ShippedQuarter", 45)
        
        no_of_riser=42
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec)
        expected_xaxis_labels=['2012 : 1', '2012 : 2', '2012 : 3', '2012 : 4', '2013 : 1', '2013 : 2', '2013 : 3', '2013 : 4', '2014 : 1', '2014 : 2', '2014 : 3', '2014 : 4', '2015 : 1', '2015 : 2', '2015 : 3', '2015 : 4', '2016 : 1', '2016 : 2', '2016 : 3', '2016 : 4', '2017 : 1']
        expected_yaxis_labels=['0', '40K', '80K', '120K', '160K', '200K']
        expected_legend_list=['Shipment Unit(s)','Days Delayed']
        Media_Player_riser="riser!s0!g17!mbar!"
        Media_Player_riser_riser_tooltip=['Shipped Year:2016', 'Shipped Quarter:2', 'Shipment Unit(s):97,377', 'Filter Chart', 'Exclude from Chart', 'Drill up to Shipped Year', 'Drill down to']
        verify_bar_chart(expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip,expected_legend_list,'02.1') 

        """
        Step03: Run the visualization
        Step04: Hover over 2016:4 (one before last on right) > Drill Down > "Shipped Month"        
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        expected_xaxis_labels=['2012 : 1', '2012 : 2', '2012 : 3', '2012 : 4', '2013 : 1', '2013 : 2', '2013 : 3', '2013 : 4', '2014 : 1', '2014 : 2', '2014 : 3', '2014 : 4', '2015 : 1', '2015 : 2', '2015 : 3', '2015 : 4', '2016 : 1', '2016 : 2', '2016 : 3', '2016 : 4', '2017 : 1']
        expected_yaxis_labels=['0', '40K', '80K', '120K', '160K', '200K']
        one_riser="riser!s0!g17!mbar!"
        one_riser_tooltip=['Shipped Year:2016', 'Shipped Quarter:2', 'Shipment Unit(s):97,377', 'Filter Chart', 'Exclude from Chart', 'Drill up to Shipped Year', 'Drill down to']
        verify_bar_chart(expected_xaxis_labels,expected_yaxis_labels,one_riser,no_of_riser,one_riser_tooltip,expected_legend_list,'04.1') 
        lastbefore_riser="riser!s0!g19!mbar!"
        visual.select_tooltip(lastbefore_riser,'Drill down to->Shipped Month')
        
        """
        Step05:Hover over each of the columns and review tooltip.
        Step06:Logout using API(without saving)
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        no_of_risera=6
        expected_xaxis_labels=['2016 : 10', '2016 : 11', '2016 : 12']
        expected_yaxis_labels=['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        first_riser="riser!s0!g0!mbar!"
        first_riser_tooltip=['Shipped Year:2016', 'Shipped Month:10', 'Shipment Unit(s):39,076', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Shipped Quarter', 'Drill down to']
        verify_bar_chart(expected_xaxis_labels,expected_yaxis_labels,first_riser,no_of_risera,first_riser_tooltip,expected_legend_list,'05.1') 
        visual.switch_to_previous_window()
        
if __name__ == '__main__':
    unittest.main()