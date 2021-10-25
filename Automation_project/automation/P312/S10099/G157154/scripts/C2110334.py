'''
Created on Feb 27, 2018

@author: Praveen Ramkumar

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2110334
TestCase Name = Lasso filter values at runtime in Visualization returns selected values correctly
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2110334_TestClass(BaseTestCase):

    def test_C2110334(self):
        """
        TESTCASE VARIABLES        
        """
        visual = visualization.Visualization(self.driver)
        driver=self.driver
        restore_fex = 'C2110334_Repro.fex'
        sleep_time=3
        time_out=45
        source_xoffset=-15
        target_xoffset=10
        source_element_location='middle_left'
        total_no_of_riser_css="#MAINTABLE_wbody1 rect[class^='riser']"
        wait_time_in_sec=120
        no_of_riser=7
        no_of_risera=3    
    
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step' + step_num + '.1:'+' Verify x-axis title')
            visual.verify_y_axis_title(y_title, msg='Step' + step_num + '.2:'+' Verify y-axis title')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.3'+' Verify x-axis label',xyz_axis_label_length=4)
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.4'+' Verify y-axis label')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step' + step_num + '.5:'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class*='"+riser+"']", 'bar_blue',  msg='Step' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser,tooltip,msg='Step' + step_num + '.7:'+' Verify riser tooltip',move_to_tooltip=True)
            
        
        """
        Step 01: Run the attached C2110334.Repro.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10099&BIP_item=C2110334.Repro.fex
        """
        visual.run_visualization_using_api(restore_fex)
        
        """
        Step 01.1: Verification
        """
        
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Media_Player_riser="riser!s0!g3!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_riser,Media_Player_riser_riser_tooltip, '03.1')  
        
        """
        Step 02: Lasso several risers (Accessories, Camcorder, Computer)
        Step 03:Click "Filter Chart"
        """     
        
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", time_out)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g2!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=source_xoffset, target_xoffset=target_xoffset, source_element_location=source_element_location)
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Filter Chart')
        
        
        """
        Step 04:Verify chart displayed on (Accessories, Camcorder, Computer) risers
        """
        
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "CostofGoods", time_out)
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_risera, wait_time_in_sec) 
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        Media_Player_riser="riser!s0!g1!mbar!"
        Media_Player_riser_riser_tooltip=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill down to Product Subcategory']
        verify_bar_chart(x_title,y_title,expected_xaxis_labels,expected_yaxis_labels,Media_Player_riser,no_of_risera,Media_Player_riser_riser_tooltip, '03.1')  
        
        """
        Step 05:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main() 