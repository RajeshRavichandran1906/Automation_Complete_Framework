'''
Created on Feb, 05 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349075
Test_Case Name : Undo delete Group from query
Preconditions : Continue from C2349074 test case
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2349075_TestClass(BaseTestCase):

    def test_C2349075(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349075'
        Edit_Case_ID='C2349074'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(expected_xaxis_title, expected_xaxis_label, expected_yaxis_label, total_risers, step_num):
            visual.verify_x_axis_title(expected_xaxis_title, msg='Step ' + step_num + '.1')
            visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.6' )
            
        """
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349074.fex
        """
        visual.edit_visualization_using_api(Edit_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 30)
        
        """
            Step 01.1 : Restored successfully
        """
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_label, expected_yaxis_label, 6, '01')
        
        """
            Step 02 : Right click "PRODUCT_CATEGORY_1" group in query pane >
            Step 03 : Click "Delete"
        """
        visual.right_click_on_field_under_query_tree('PRODUCT_CATEGORY_1', 1, 'Delete')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-labels!m6!']", "1.2B", 30)
        
        """
            Step 04 : Verify "PRODUCT_CATEGORY_1" deleted from query pane and preview updated
        """
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_title(['Revenue'], msg='Step 04.1')
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 04.2')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 04.3')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step 04.4' )
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Marker', 1, 'Step 04.5 ')
        
        """
            Step 05 : Click Undo button in tool bar menu 
        """
        visual.select_item_in_top_toolbar('undo')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 30)
        
        """
            Step 06 : Verify Group is returned to query pane and preview returns to show group value
        """
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_label, expected_yaxis_label, 6, '06')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, 'Step 06.7 ')
        
        """
            Step 07 : Click Redo
        """
        visual.select_item_in_top_toolbar('redo')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-labels!m6!']", "1.2B", 30)
        
        """
            Step 08 : Verify "PRODUCT_CATEGORY_1" deleted from query pane and preview updated
        """
        expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
        visual.verify_y_axis_title(['Revenue'], msg='Step 08.1')
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 08.2')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 1, msg='Step 08.3')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step 08.4' )
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Marker', 1, 'Step 08.5 ')
        visual.take_preview_snapshot(Test_Case_ID, '08')
        
        """
            Step 09 : Click IA > Save as "C2349075" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 10 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()