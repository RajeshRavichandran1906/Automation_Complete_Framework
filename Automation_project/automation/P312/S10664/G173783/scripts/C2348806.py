'''
Created on Jan 31, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348806
TestCase Name: Edit group
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348806_TestClass(BaseTestCase):

    def test_C2348806(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348806'
        Restore_fex = 'C2348806_Base'
        
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        """
            Step 01 : Restore saved fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348806_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=20)
        
        """
            Step 02 : Verify preview chart
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 2.1:')
        visual.verify_y_axis_title(['Revenue'], msg='Step 2.2:')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3:')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 2.4:")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 2.5: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 2.6:")
        """
            Step 03 : Click Computers riser
                        Verify following tool tip options displayed
        """
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Computers', 'Revenue:$103,316,482.12', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g1!mbar', expected_tooltip_list, "Step 2.7:")
        """
            Step 04 : Right click on "PRODUCT_CATEGORY_1" in query pane > Edit group
        """
        visual.right_click_on_field_under_query_tree("PRODUCT_CATEGORY_1", 1, "Edit Group...")
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        visual.wait_for_number_of_element(parent_css, 1, time_out=30)
        """ 
            Step 05 : Verify grouping values
            Step 06 : Click Cancel
        """
        expected_grid_value_list=['Accessories and Camcorder', 'Accessories', 'Camcorder', 'Televisions', 'Computers', 'Media Player', 'Stereo Systems and Video Production', 'Stereo Systems', 'Video Production']
        visual.verify_group_grid_values(expected_grid_value_list, "Step 08:01:Verify grid values")
        visual.exit_group_dialog('cancel')
        """ 
            Step 07 : Click IA > Save as "C2348806" > Click Save
        """ 
        visual.save_as_visualization_from_menubar(Test_Case_ID) 
        """ 
            Step 08 : Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == "__main__":
    unittest.main()