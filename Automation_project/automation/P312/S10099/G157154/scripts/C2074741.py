'''
Created on Feb 27, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2074741
Test_Case Name : Drill down does filtering instead of next level
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2074741_TestClass(BaseTestCase):

    def test_C2074741(self):
        
        Test_Case_ID = "C2074741"
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        no_of_riser=7
        
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,riser_color_css,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser, tooltip, msg='Step' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?item=IBFS:/WFC/Repository/S10099/C2074741.Repro.fex&tool=idis
        """
        visual.edit_visualization_using_api(Test_Case_ID+"_Repro")
        
        """
        Step02: Run the Visualization.
        Step03: Hover on a bar and select "Drill down to Product Subcategory".
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
#         visual.wait_for_number_of_element(toolbar_run, 1, short_wait_time_in_sec)
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        MediaPlayer_riser_css="riser!s0!g3!mbar"
        visual.select_tooltip(MediaPlayer_riser_css, "Drill down to Product Subcategory", move_to_tooltip=True)
        
        """
        Step04: Verify the following chart.
        """
        no_of_riser=4
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['Product Subcategory']
        y_title=['Revenue']
        expected_xaxis_labels=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        BluRay_riser="riser!s0!g0!mbar"
        BluRay_tooltip=['Product Subcategory:Blu Ray', 'Revenue:$232,884,116.13', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        step_num='04'
        verify_bar_chart(x_title, y_title, expected_xaxis_labels, expected_yaxis_labels, BluRay_riser, BluRay_riser, no_of_riser, BluRay_tooltip, step_num)        
        visual.switch_to_previous_window()
                 
        """
        Step05: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        no_of_riser=7
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)

if __name__ == '__main__':
    unittest.main()        