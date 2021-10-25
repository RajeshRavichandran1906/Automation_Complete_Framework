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

class C2327091_TestClass(BaseTestCase):

    def test_C2327091(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327091'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        """
        Step 01: Launch the IA API with wf_retail_lite
        http://machine:port/ibi_apps/ia?tool=idis&master=s8357/CAROLAP&item=IBFS%3A%2FWFC%2FRepository%2FS8357%2F
        
        The signon screen will be displayed.
        Login as userid devuser (autodevuser01/02/03/04/05) and blank password
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        parent_css= "#TableChart_1 svg>g.chartPanel rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 12, 50) 
        """
        Step 02: Double click DEALER_COST, RETAIL_COST , SALES & CAR.
        """     
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text('#queryTreeColumn table tr:nth-child(8)', 'Product,Category', time_out=15)
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text('#queryTreeColumn table tr:nth-child(7)', 'Revenue', time_out=15)
        """
        Step 03: Verify the preview
        """
        expected_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 3.1')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 3.2')
        visual.verify_x_axis_title(['Product Category'], msg='Step 3.3')
        visual.verify_y_axis_title(['Revenue'], msg='Step 3.4')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g2!mbar']", "bar_blue", msg="Step 3.5")
        expected_tooltip_list=['Product Category:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g1!mbar', expected_tooltip_list, msg='Step 3.6 : Verify tooltip values')
        """
        Step 04: Select 2 first risers > Group Product,Category selection
        """
        source_css="#MAINTABLE_wbody1 [class='riser!s0!g0!mbar!']"
        source_element=self.driver.find_element_by_css_selector(source_css)
        target_css="#MAINTABLE_wbody1 [class*='riser!s0!g1!mbar']"
        target_element=self.driver.find_element_by_css_selector(target_css)
        visual.create_lasso(source_element,target_element)
        expected_tooltip_list=['2 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 4.1')
        """
        Step 05: Click the group value riser
        """
        visual.select_lasso_tooltip('Group Product,Category Selection')
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Accessories and Camcorder...', 'Ungroup Accessories and Camcorder...', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, msg='Step 5.1:')
        """
        Step 06: Click Rename Accessories and Camcorder...
                    Enter string length of '60' without spaces (123456789012345678901234567890123456789012345678901234567890)
                    Click OK
        """
        visual.select_lasso_tooltip('Rename Accessories and Camcorder...')
        visual.rename_grouped_riser_name(old_name='Accessories and Camcorder', new_name='123456789012345678901234567890123456789012345678901234567890', close_button_name='OK')
        """
        Step 07: Click the group value riser
                    Verify the tooltip value is truncated.
        """
        expected_tooltip_list=['PRODUCT_CATEGORY_1:123456789012345678901234567890123456789012345678901234567890', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 7.1 : Verify tooltip values')
        expected_label_list=['12345678901234567890123456789...', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_label_list, xyz_axis_label_length=5, msg='Step 7.2')
        expected_label_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_label_list, msg='Step 7.3')
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 7.4')
        visual.verify_y_axis_title(['Revenue'], msg='Step 7.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g2!mbar']", "bar_blue", msg="Step 7.6")
        """
        Step 08 : Click "Save" in the toolbar > Type 2327091 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        """ 
            Step 09 : Logout using API
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        

if __name__ == '__main__':
    unittest.main()