'''
Created on Feb 27, 2018

@author: Praveen Ramkumar

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102941
TestCase Name = Lasso Exclude cancels out a filter built into vis
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102941_TestClass(BaseTestCase):

    def test_C2102941(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        driver=self.driver
        Test_Case_ID='C2102941'
        restore_fex = 'C2102941_Repro'
        sleep_time=3
        time_out=45
        source_xoffset=-15
        target_xoffset=10
        source_element_location='middle_left'
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        wait_time_in_sec=120
        no_of_riser=7
        no_of_risera=4
        no_of_riserb=3
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label',xyz_axis_label_length=2)
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label',xyz_axis_label_length=2)
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip',move_to_tooltip=True)
                    
        """
        Step 01:Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10099%2FC2102941.Repro.fex&tool=idis
        """
        visual.edit_visualization_using_api(restore_fex)
        
        """
        Step 01.1: Verification
        """
        
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Gross Profit']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Gross Profit:$55,832,578.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '01.1')  
        
        """
        Step 02: Lasso the first 3 risers > Exclude from Chart
        """
        
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "GrossProfit", time_out)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g2!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location=source_element_location)
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Exclude from Chart')
        
        
        """
        Step 02.1:Verification
        """
        
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "GrossProfit", time_out)
        x_title=['Product Category']
        y_title=['Gross Profit']
        expected_xaxis_labels=['Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        Media_Player_riser="riser!s0!g1!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Stereo Systems', 'Gross Profit:$86,181,070.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_risera,Media_Player_riser_riser_tooltip, '02.1')  
        
        """
        Step 03:Click Run
        Step 04:Lasso the first 3 risers > Filter Chart
        Step 05:Close output window and IA window without saving.
        """
        
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_risera, wait_time_in_sec) 
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g2!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location=source_element_location)
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Filter Chart')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "GrossProfit", time_out)
        x_title=['Product Category']
        y_title=['Gross Profit']
        expected_xaxis_labels=['Media Player', 'Stereo Systems', 'Televisions']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        Media_Player_riser="riser!s0!g1!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Stereo Systems', 'Gross Profit:$86,181,070.52', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riserb,Media_Player_riser_riser_tooltip, '03.1')  
        visual.take_run_window_snapshot(Test_Case_ID, '5')
        visual.switch_to_previous_window()
        
        """
        Step 06:Logout using API(without saving)
        http://machine:port/alias/service/wf_security_logout.jsp
        """        
        
if __name__ == '__main__':
    unittest.main() 