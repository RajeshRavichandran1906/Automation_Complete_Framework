'''
Created on Jan 10, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349050
Test_Case Name : Reuse group from data pane
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages.visualization_metadata import Visualization_Metadata
from common.wftools.visualization import Visualization

class C2349050_TestClass(BaseTestCase):

    def test_C2349050(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349050'
        visual=Visualization(self.driver)
        metadata=Visualization_Metadata(self.driver)
        
        """
            Note : Continue from C2349049 test case
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349049.fex
        """
        visual.edit_visualization_using_api('C2349049')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f svg text[class='yaxis-labels!m7!']", "350M", 120)
        time.sleep(3)
        
        """
            Step 02 : Double click "BUSINESS_REGION_1" Group
        """
        visual.double_click_on_datetree_item('Dimensions->BUSINESS_REGION_1', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "BUSINESS_REGION_1", 30)
        
        """
            Step 03 : Verify "BUSINESS_REGION_1" Group is added to horizontal Axis, group value riser displays in preview
        """
        expected_query_fields=['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Gross Profit', 'Horizontal Axis', 'BUSINESS_REGION_1', 'Marker', 'Color', 'Size', 'Tooltip']
        metadata.verify_query_panel_all_field(expected_query_fields, 'Step 03.0 : Verify "BUSINESS_REGION_1" Group is added to horizontal Axis')
        
        """
            Step 03.1 : Verify preview
        """
        visual.verify_x_axis_title(['BUSINESS_REGION_1'], msg='Step 03.1')
        visual.verify_x_axis_label(['EMEA and Oceania', 'North America', 'South America'], msg='Step 03.2')
        visual.verify_y_axis_title(['Gross Profit'], msg='Step 03.3')
        visual.verify_y_axis_label(['0', '40M', '80M', '120M', '160M', '200M'], msg='Step 03.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 3, msg='Step 03.5 ')
        visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step 03.6 ')
        expected_tooltip=['BUSINESS_REGION_1:EMEA and Oceania', 'Gross Profit:$159,673,644.62', 'Filter Chart', 'Exclude from Chart', 'Drill down to Customer Business Region']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip, 'Step 03.7 : Verify tooltip')
        visual.take_preview_snapshot(Test_Case_ID, '03')
        
        """
            Step 04 : Click IA > Save as "C2349050" > Click Save 
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 05 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()