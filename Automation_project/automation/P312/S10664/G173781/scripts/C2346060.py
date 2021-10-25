'''
Created on Jan 11, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346060
TestCase Name = Group option not available at run time (CTRL key)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2346060_TestClass(BaseTestCase):

    def test_C2346060(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346060'
        Restore_fex = 'C2346060_Base'
        
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore the C2346060_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346060_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7)
        step_num = '1'
        visual.verify_x_axis_title(['Product Category'], msg='Step ' + step_num + '.2')
        visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.1')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step ' + step_num + '.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg='Step ' + step_num + '.6')
        time.sleep(5)   
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step ' +step_num+ '.7: Verify Tooltip') 
        
        """
        Step 02: Click Run
        """
        time.sleep(5)
        visual.run_visualization_from_toptoolbar()
        time.sleep(10)
        visual.switch_to_new_window()
        time.sleep(5)
        print("Switched to run window:") 
        
        """
        Step 03: Multi select several risers with Ctrl key (Ex. Camcorder, Computers, Televisions, Video production)
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 7, 200)
        step_num = '3'
        visual.verify_x_axis_title(['Product Category'], msg='Step ' + step_num + '.2')
        visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.1')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step ' + step_num + '.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg='Step ' + step_num + '.6')
        time.sleep(5)   
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step ' +step_num+ '.7: Verify Tooltip')
        time.sleep(5)
        camcorder=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g1!mbar!']")
        computers=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g2!mbar!']")
        televisions=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g5!mbar!']")
        video_production=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g6!mbar!']")
        visual.multi_select_chart_component([camcorder, computers, televisions, video_production])
        
        """
        Step 04: Verify tool tip doesn't show option to group
        """
        time.sleep(4)
        expected_tooltip_list=['4 points', 'Filter Chart', 'Exclude from Chart']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 04: Verify tool tip doesnt show option to group')
        time.sleep(8)
        visual.take_run_window_snapshot(Test_Case_ID, '04') 
        
        """
        Step 05: Close run window
        """
        visual.switch_to_previous_window()
        time.sleep(8)
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1)
        print("Switched back to main window:")
        
        """
        Step 06: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(4)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()