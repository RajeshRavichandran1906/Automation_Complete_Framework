'''
Created on Jan 31, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348947
TestCase Name: Rename group value to old name
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348947_TestClass(BaseTestCase):

    def test_C2348947(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348947'
        Restore_fex = 'C2348947_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        """
            Step 01 : Restore the "C2348947_Base.fex" using the API.
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348947_Base.fex
            Step 02 :   Click riser "Accessories, Camcorder & TV"
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=20)        
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 2.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 2.2')
        expected_xaxis_label=['Accessories, Camcorders & TV', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, xyz_axis_label_length=10, msg='Step 2.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 2.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 2.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 2.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories, Camcorders & TV', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 2.7 : Verify tooltip values')
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories, Camcorders...', 'Ungroup Accessories, Camcorders...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 2.8')
        """
            Step 02 : Select Rename Accessories, Camcorders from tooltip
        """
        visual.select_lasso_tooltip('Rename Accessories, Camcorders...')
        """
            Step 03 : Type "Accessories and Camcorder"
            Step 04 : Click OK
        """
        visual.rename_grouped_riser_name(old_name='Accessories, Camcorders & TV', new_name='Accessories and Camcorder', close_button_name='OK')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, time_out=20)
        """
            Step 05 : Verify Preview updates with new group value name.
        """
        expected_label_list=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=10,  msg='Step 5.1')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 5.2")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 5.3')
        visual.take_preview_snapshot(Test_Case_ID, '7')
        """
            Step 06 : Click the "Accessories and Camcorder" riser
            Step 07 : Verify Tooltip shows option: Rename Accessories and Camc...
        """
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 7.1')
        """
            Step 08 : Click IA > Save as "C2348947" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        """
            Step 09 : Logout using API
                        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        """
            Step 10 : Reopen the fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348947.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 10.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 10.2')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, xyz_axis_label_length=10, msg='Step 10.3')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 10.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 10.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 10.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 10.7')
        """
            Step 11 : Logout using API
                        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
       
if __name__ == '__main__':
    unittest.main()