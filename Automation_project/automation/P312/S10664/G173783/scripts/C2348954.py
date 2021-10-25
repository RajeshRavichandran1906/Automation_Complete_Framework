'''
Created on Feb 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348954
TestCase Name = Ungroup All after restore
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348954_TestClass(BaseTestCase):

    def test_C2348954(self):
        """
        TESTCASE VARIABLES
        """
        Restore_fex = 'C2348954_Base'
        Test_Case_ID = 'C2348954'
        driver=self.driver
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348954_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 01.1: Verify x-axis title')
        visual.verify_y_axis_title(['Revenue'], msg='Step 01.2:Verify Yaxis title')
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 01.3: Verify x-axis label')
        expected_y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M','400M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 01.4:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 4, msg="Step 01.5: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 01.6:")
        time.sleep(4)
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$362,455,173.58', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list,'Step 1.7: Verify Tooltip')

        """
        Step 02: Click any riser in preview (Ex., Computers)
        """
        time.sleep(5)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g1!mbar!']")
        visual.select_chart_component(riser_css)
        
        """
        Step 03: Select Ungroup All
        """
        time.sleep(3)
        visual.select_lasso_tooltip('Ungroup All')
        
        """
        Step 04: Verify preview updated
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 4.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 4.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 4.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 4.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 4.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 4.6')
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 4.7: Verify Tooltip') 
        
        """
        Step 05: Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 06: Hover on run time riser and verify tool tip values
        """
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 6.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 6.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 6.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 6.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 6.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 6.6')
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 6.7: Verify Tooltip') 
        visual.take_run_window_snapshot(Test_Case_ID, '06')
        
        """
        Step 07: Close run window
        """
        visual.switch_to_previous_window()
        
        """
        Step 08 : Click IA > Save as "C2348954" > Click Save
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 09 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 10 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348954.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        time.sleep(5)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 10.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 10.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 10.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 10.6')
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 10.7: Verify Tooltip') 
        
        """
        Step 11: Right click on "PRODUCT_CATEGORY_1" query or data pane > Edit group
        """
        visual.right_click_on_field_under_query_tree("PRODUCT_CATEGORY_1", 1, context_menu_path='Edit Group...')
        
        """
        Step 12: Verify there are no group values in the group
        Step 13: Click Cancel
        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        expected_group_dialog_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 12: Verify there are no group values in the group")
        visual.exit_group_dialog('cancel')
        
        """
        Step 14: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()