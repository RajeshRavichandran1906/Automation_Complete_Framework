'''
Created on Jan 31, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348948
TestCase Name: Group value name of less than 20 char
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348948_TestClass(BaseTestCase):

    def test_C2348948(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348948'
        Restore_fex = 'C2348948_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
            Step 01 : Restore saved fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348948_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, time_out=20)      
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 1.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 1.2')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 1.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 1.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 1.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 1.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip("riser!s0!g0!mbar!", expected_tooltip_list, msg='Step 1.7 : Verify tooltip values')
        
        """
            Step 02 : Click the "Accessories and Camcorder" riser for the group value in preview name
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 2.1')
        
        """
            Step 03 : Click Rename Accessories and Camcorder
        """
        visual.select_lasso_tooltip('Rename Accessories and Camcorder...')
        """
            Step 04 : Type name of less than 20 chart or "12345678901234567890"
            Step 05 : Click OK
        """
        visual.rename_grouped_riser_name(old_name='Accessories and Camcorder',new_name='12345678901234567890', close_button_name='OK')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6)
        """
            Step 06 : Verify preview updated 
        """
        expected_label_list=['12345678901234567890', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=10, msg='Step 6.1')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 6.2")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:12345678901234567890', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip("riser!s0!g0!mbar!", expected_tooltip_list, msg='Step 6.3')
        """
            Step 07 : Click the "12345678901234567890" riser
            Step 08 : Verify tooltip menu shows full group value name
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename 12345678901234567890', 'Ungroup 12345678901234567890', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 8.1')
        visual.take_preview_snapshot(Test_Case_ID, '8')
        """
            Step 09: Click IA > Save as "C2348948" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        """
            Step 10 : Logout using API
                        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        """
            Step 11 : Reopen the fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348947.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        
        visual.wait_for_visible_text("#MAINTABLE_wbody1 text[class*='xaxisOrdinal-labels!g0!mgroupLabel!']", "12345678901234567890")
        
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 11.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 11.2')
        expected_xaxis_label=['12345678901234567890', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, xyz_axis_label_length=10, msg='Step 11.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 11.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 11.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 11.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:12345678901234567890', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip("riser!s0!g0!mbar!", expected_tooltip_list, msg='Step 11.7')
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename 12345678901234567890', 'Ungroup 12345678901234567890', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 11.8')
       
if __name__ == '__main__':
    unittest.main()