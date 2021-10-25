'''
Created on Feb 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348953
TestCase Name = Ungroup group values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348953_TestClass(BaseTestCase):

    def test_C2348953(self):
        """
        TESTCASE VARIABLES
        """
        Restore_fex = 'C2348953_Base'
        Test_Case_ID = 'C2348953'
        driver=self.driver
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348953_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 01.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 01.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 01.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 01.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 01.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 01.6:")
        time.sleep(4)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 1.7: Verify Tooltip')
        
        """
        Step 02: Click on "Televisions and Video Production" riser in preview 
        """
        time.sleep(5)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g5!mbar!']")
        visual.select_chart_component(riser_css)
        
        """
        Step 03: Click "Ungroup Televisions and Video Production"
        """
        time.sleep(3)
        visual.select_lasso_tooltip('Ungroup Televisions and Video...')
        
        """
        Step 04: Verify preview updated 
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 04.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 04.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 04.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 04.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 7, msg="Step 04.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 04.6:")
        time.sleep(4)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 04.7: Verify Tooltip')
        
        """
        Step 05: Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 06: Verify run time chart with ungrouped values
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 06.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 06.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 06.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 06.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 7, msg="Step 06.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 06.6:")
        time.sleep(4)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 06.7: Verify Tooltip')
        visual.take_run_window_snapshot(Test_Case_ID, '06')
        
        """
        Step 07: Dismiss run window
        """
        visual.switch_to_previous_window()
        
        """
        Step 08: Click IA > Save as "C2348953" > Click Save
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 09: Logout using API: http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 10: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348953.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 10.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 10.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 10.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 7, msg="Step 10.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 10.6:")
        time.sleep(4)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 10.7: Verify Tooltip')
        
        """
        Step 11: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()