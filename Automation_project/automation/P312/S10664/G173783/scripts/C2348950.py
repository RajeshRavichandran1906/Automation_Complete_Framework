'''
Created on Feb 08, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2348950
TestCase Name: Group value name in tooltip is truncated around 25 char or end of word
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348950_TestClass(BaseTestCase):

    def test_C2348950(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348950'
        Restore_fex = 'C2348950_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
            Step 01 : Restore saved fex using API
                        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348950_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6)
        
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
        Step 02 : Click on "Accessories and Camcorder" riser for the group value in preview
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
        Step 04 : Type "1234 6789 1234 6789 1234 6789"
        Step 05 : Click OK
        """
        visual.rename_grouped_riser_name(old_name='Accessories and Camcorder', new_name='1234 6789 1234 6789 1234 6789', close_button_name='OK')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6)
       
        """
        Step 06 : Verify preview updated with new group value name
        """
        expected_label_list=['1234 6789 1234 6789 1234 6789', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 6.1')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:1234 6789 1234 6789 1234 6789', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, msg='Step 6.2 : Verify tooltip values')
        
        """
        Step 07 : Click on "1234 6789 1234 6789 1234 6789" riser
        Step 08 : Verify tool tip menu group value name
        """
        elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(elem)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename 1234 6789 1234 6789 1234...', 'Ungroup 1234 6789 1234 6789 1234...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 8.1 : Verify lasso tooltip values')
        
        """
        Step 09 : Click on "1234 6789 1234 6789 1234 6789" riser > Rename 1234 6789 1234 6789 1234...
                    Tooltip shows option to rename group value and displays 24 char and then elipses (...)
        """
        visual.select_lasso_tooltip('Rename 1234 6789 1234 6789 1234...')
        
        """
        Step 10 : Highlight and Delete existing text and Type "The cow jumped over the Moon"
        Step 11 : Click OK
        """
        visual.rename_grouped_riser_name(old_name='1234 6789 1234 6789 1234 6789', new_name='The cow jumped over the Moon', close_button_name='OK')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6)
       
        """
        Step 12 : Click on "The cow jumped over the Moon" riser
        Step 13 : Verify tooltip -> Tooltip shows option to rename group value and displays "The cow jumped over the..." (23 char) with elipses
        """
        expected_label_list=['Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'The cow jumped over the Moon', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 13.1')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:The cow jumped over the Moon', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g4!mbar!', expected_tooltip_list, msg='Step 13.2 : Verify tooltip values')
        
        elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g4!mbar!']")
        visual.select_chart_component(elem)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename The cow jumped over the...', 'Ungroup The cow jumped over the...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 13.3 : Verify lasso tooltip values')
        
        """
        Step 14 : Click IA > Save as "C2348950" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 15 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 16 : Run the saved fex from Resource tree
                    http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2348950.fex
        """
        visual.run_visualization_using_api(Test_Case_ID+'.fex')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 6)
        
        """
        Step 17 : Hover on "The cow jumped over the Moon" riser and verify tool tip value
        """
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], "#MAINTABLE_wbody1_f", msg='Step 17.1')
        visual.verify_y_axis_title(['Revenue'], "#MAINTABLE_wbody1_f", msg='Step 17.2')
        expected_label_list=['Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'The cow jumped over the Moon', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 17.3')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 17.4')
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, 6, msg='Step 17.5')
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g4!mbar!']", 'bar_blue', msg='Step 17.6')
        expected_tooltip_list=['PRODUCT_CATEGORY_1:The cow jumped over the Moon', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g4!mbar!', expected_tooltip_list, msg='Step 17.7 : Verify tooltip values')
        
if __name__ == '__main__':
    unittest.main() 