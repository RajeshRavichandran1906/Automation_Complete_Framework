'''
Created on Feb 01, 2018
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348803
TestCase Name: Add to existing group
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
class C2348805_TestClass(BaseTestCase):

    def test_C2348805(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348805'
        Restore_fex = 'C2348805_Base'
        
        driver = self.driver
        visual = visualization.Visualization(self.driver)
        """
            Step 01:Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348805_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, time_out=170)
        
        """
            Verify preview chart
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 01:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 01:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 01:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 01:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 5, msg="Step 01:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 01:06:")       
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, "Step 12:07:Verify tooltip values")
             
        """ 
            Step 02:Multi select "Stereo Systems" and "Video Production" in preview
        """
        Stereo_Systems_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']")
        Video_Production_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar']")
        visual.multi_select_chart_component([Stereo_Systems_elem, Video_Production_elem])
            
        """ 
            Step 03:Select "Group PRODUCT_CATEGORY_1 Selection"
        """
        expected_tooltip_list=['2 points', 'Filter Chart', 'Exclude from Chart', 'Group PRODUCT_CATEGORY_1 Selection', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 03:01: Verify tooltip values')
        visual.select_lasso_tooltip("Group PRODUCT_CATEGORY_1 Selection")
        """
           Step 04:Verify "Stereo Systems" and "Video Production" display in 1 riser in preview
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=80)
         
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 04:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 04:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 04:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M','400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 04:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 04:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 04:06:")    
        """ 
            Step 05:Hover on "Stereo Systems" and "Video Production" riser and verify tool tip values
        """
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Stereo Systems and Video Production', 'Revenue:$349,348,210.14', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g3!mbar', expected_tooltip_list, "Step 05:07:Verify tooltip values")
         
        """
            Step 06:Click run
        """
        visual.run_visualization_from_toptoolbar()
        time.sleep(10)
        visual.switch_to_new_window()
         
        """ 
            Step 07:Verify run time chart
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 4, 200)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 07:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 07:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 07:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M','400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 07:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 07:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 07:06:")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 7: Verify Tooltip')
        time.sleep(5)
        """
            Step 08:Close run window
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1)
        """ 
            Step 09:Click IA > Save as "C2348805" > Click Save
        """ 
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        """ 
            Step 10:Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
if __name__ == "__main__":
    unittest.main()