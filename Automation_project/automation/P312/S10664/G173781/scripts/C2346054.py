'''
Created on Jan 11, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346054
TestCase Name = Tooltip shows option to group for multi select values (CTRL Key)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization


class C2346054_TestClass(BaseTestCase):

    def test_C2346054(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346054'
        Restore_fex = 'C2346054_Base'
        
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore the C2346054_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346054_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 100)
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
        Step 02: Multi select Accessories, Media player, Video production risers with Ctrl+ key in preview
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 7, 100)
        time.sleep(2)
        accessories=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        mediaplayer=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g3!mbar!']")
        video_production=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g6!mbar!']")
        visual.multi_select_chart_component([accessories, mediaplayer, video_production])
        
        """
        Step 03: Verify the tool tip values displayed
        """
        time.sleep(4)
        expected_tooltip_list=['3 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 03: Verify following tool tip values displayed')
        time.sleep(8)
        visual.take_preview_snapshot(Test_Case_ID, '03') 
        
        """
        Step 04: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()