'''
Created on Feb 2, 2018

@author: BM13368
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2348803
TestCase Name : Add to existing group
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348803_TestClass(BaseTestCase):

    def test_C2348803(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348803'
        Restore_fex = 'C2348803_Base'
        
        driver = self.driver
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01:Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348803_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, time_out=150)
        
        """
        Verify preview chart
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 01:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 01:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 01:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 01:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 01:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g0!mbar!']", "bar_blue", msg="Step 01:06:")       
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, "Step 01:07:Verify tooltip values")
        
        """
        Step 02:Multi select "Accessories and Camcorder"and "Televisions" risers in preview
        """
        Accessories_and_Camcorder=driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g0!mbar!']")
        televisions=driver.find_element_by_css_selector("#TableChart_1 svg>g rect[class='riser!s0!g4!mbar!']")
        visual.multi_select_chart_component([Accessories_and_Camcorder, televisions])
        """
        Step 03:Verify tooltip options, tooltip displaying group option merge with accessories and camcorder and television risers in preview
        """
        time.sleep(4)
        expected_tooltip_list=['2 points', 'Filter Chart', 'Exclude from Chart', 'Merge with Accessories and Camcorder...', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 03: Verify tooltip values')
        """
        Step 04:Select option merge with accessories and camcorder
        """
        visual.select_lasso_tooltip("Merge with Accessories and Camcorder...")
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, time_out=180) 
        """ 
        Step 05:Verify preview updated
        Preview updated with one riser grouping Accessories, Camcorder and Televisions, name of group value remains "Accessories and Camcorder"
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 05:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 05:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 05:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M','400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 05:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 5, msg="Step 05:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g0!mbar!']", "bar_blue", msg="Step 05:06:")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, "Step 05:07:Verify tooltip values")
        
        """
        Step 06:Right click on "PRODUCT_CATEGORY_1" in query pane > Edit group
        """
        visual.right_click_on_field_under_query_tree("PRODUCT_CATEGORY_1", 1, "Edit Group...")
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        visual.wait_for_number_of_element(parent_css, 1, time_out=30)
        """ 
        Step 07:Verify grouping values
        "Televisions" added into Accessories and Camcorder
        Step 08:Click Cancel
        """
        expected_grid_value_list=['Accessories and Camcorder', 'Accessories', 'Camcorder', 'Televisions', 'Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        visual.verify_group_grid_values(expected_grid_value_list, "Step 07:01:Verify grid values")
        visual.exit_group_dialog('ok')
        """
        Step 09:Hover on "Accessories and Camcorder" riser and verify tool tip values
        """
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, "Step 09:01:Verify tooltip values")
        
        """ 
        Step 10:Click IA > Save as "C2348803" > Click Save
        """ 
        visual.save_as_visualization_from_menubar(Test_Case_ID)    
        """ 
        Step 11:Logout using API
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        """ 
        Step 12:Restore saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348803.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, time_out=190) 
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 12:01: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 12:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 12:03: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 12:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 5, msg="Step 12:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg="Step 12:06:")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, "Step 12:07:Verify tooltip values")
        visual.take_preview_snapshot(Test_Case_ID, '12')
        """ 
        Step 13:Logout using API
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        

if __name__ == "__main__":
    unittest.main()