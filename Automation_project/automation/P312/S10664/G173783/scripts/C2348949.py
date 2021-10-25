'''
Created on Jan 31, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348949
TestCase Name: Symbols in group value name
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348949_TestClass(BaseTestCase):

    def test_C2348949(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348949'
        Restore_fex = 'C2348949_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
            Step 01 : Restore saved fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348949_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6, time_out=60)
        
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 1.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 1.2')
        expected_label_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 1.3')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 1.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, 6, msg='Step 1.5')
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g0!mbar!']", 'bar_blue', msg='Step 1.6')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, msg='Step 1.7 : Verify tooltip values')
        
        """
        Step 02 : Click on "Accessories and Camcorder" riser for the group value in preview name
        """
        elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(elem)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 2.1 : Verify lasso tooltip')
        
        """
        Step 03 : Click Rename Accessories and Camcorder
        """
        visual.select_lasso_tooltip('Rename Accessories and Camcorder...')
        
        """
        Step 04 : Type "Mix: a # of + * symbols"
        Step 05 : Click OK
        """
        visual.rename_grouped_riser_name(old_name='Accessories and Camcorder', new_name='Mix: a # of + * symbols', close_button_name='OK')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6, time_out=60)
        
        """
        Step 06 : Verify preview updated 
        """
        expected_label_list=['Computers', 'Media Player', 'Mix: a # of = * symbols', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 6.1')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:  Mix:a # of = * symbols', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g2!mbar!', expected_tooltip_list, msg='Step 6.2 : Verify tooltip values')
        
        """
        Step 07 : Click on "Mix: a # of + * symbols" riser
        Step 08 : Verify tooltip updated with new value
        """
        elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g2!mbar!']")
        visual.select_chart_component(elem)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Mix:a # of = * symbols...', 'Ungroup Mix:a # of = * symbols...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 8.1 : Verify tooltip values')
        
        """
        Step 09 : Right click "PRODUCT_CATEGORY_1" > Edit Group
        """
        visual.right_click_on_field_under_query_tree("PRODUCT_CATEGORY_1", 1, 'Edit Group...')
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        visual.wait_for_number_of_element(parent_css, 1, time_out=30)
        """
        Step 10 : Verify group value updated in group dialog
        """
        expected_grid_value_list=['Computers', 'Media Player', 'Mix: a # of = * symbols', 'Accessories', 'Camcorder', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_grid_value_list, msg='Step 10.1 : Verify group values')
        
        """
        Step 11 : Click Cancel to dismiss dialog
        """
        visual.exit_group_dialog('cancel')
        
        """
        Step 12 : Click IA > Save as "C2348949" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 13 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 14 : Run the saved fex from Resource tree
                    http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2348949.fex
        """
        visual.run_visualization_using_api(Test_Case_ID+'.fex')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6, time_out=60)
        
        """
        Step 15 : Hover on "Mix: a # of + * symbols" riser and verify tool tip value
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], "#MAINTABLE_wbody1_f", msg='Step 15.1')
        visual.verify_y_axis_title(['Revenue'], "#MAINTABLE_wbody1_f", msg='Step 15.2')
        expected_label_list=['Computers', 'Media Player', 'Mix: a # of = * symbols', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 15.3')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 15.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, 6, msg='Step 15.5')
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g2!mbar!']", 'bar_blue', msg='Step 15.6')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:  Mix:a # of = * symbols', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g2!mbar!', expected_tooltip_list, msg='Step 15.7 : Verify tooltip values')
        
if __name__ == '__main__':
    unittest.main()       