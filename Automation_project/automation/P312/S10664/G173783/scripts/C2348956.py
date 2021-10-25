'''
Created on Feb 7, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348956
TestCase Name = Ungroup All when there are 2 groups
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348956_TestClass(BaseTestCase):

    def test_C2348956(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348956'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(4)
        
        """
        Step 02: Double click "Revenue", "Product, Category"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        
        visual.double_click_on_datetree_item("Product,Category",1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        
        time.sleep(5)
        visual.verify_x_axis_title(['Product Category'], msg='Step 2.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 2.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 2.6')
        time.sleep(5)   
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Lasso Media player and Stereo systems risers in preview > Group Product, Category selection
        """
        time.sleep(5)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g3!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g4!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=-6, source_element_location='middle_left')
        time.sleep(3)
        visual.select_lasso_tooltip('Group Product,Category Selection')
        
        """
        Step 04: Drag and drop "Store,Business,Region" to Color bucket
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Region', 0, 'Color')
        time.sleep(6)
        
        """
        Step 05: Verify following preview displayed
        """
        time.sleep(5)
        parent_css="#queryTreeWindow table tr:nth-child(12) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Store,Business,Region', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 24, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 5.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 5.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 24, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 5.6')
        expected_legend_list=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_legends(expected_legend_list, msg='Step 5.7')
        time.sleep(5)  
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$51,791,709.98', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 5.8: Verify Tooltip') 
        
        """
        Step 06: Select colors for North America and South America in preview for first riser (Multi select using CTRL) > 
        """
        time.sleep(5)
        north_america=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s1!g0!mbar!']")
        south_america=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s3!g0!mbar!']")
        visual.multi_select_chart_component([north_america, south_america])
        
        """
        Step 07: Click "Group Store,Business,Region selection"
        """
        time.sleep(3)
        visual.select_lasso_tooltip('Group Store,Business,Region Selection')
        
        """
        Step 08: Verify preview updated "North America and South America" grouping
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 18, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 8.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 8.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 8.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 8.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 18, msg='Step 8.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 8.6')
        expected_legend_list=['BUSINESS_REGION_1', 'EMEA', 'North America and South America', 'Oceania']
        visual.verify_legends(expected_legend_list, msg='Step 8.7')
        time.sleep(5)  
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$51,791,709.98', 'BUSINESS_REGION_1:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 8.8: Verify Tooltip') 
        
        """
        Step 09: Click on a riser that has both groups (Media player and Stereo systems riser)
        """
        time.sleep(5)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s1!g3!mbar!']")
        visual.select_chart_component(riser_css)
        
        """
        Step 10: Click Ungroup All
        """
        time.sleep(3)
        visual.select_lasso_tooltip('Ungroup All')
        
        """
        Step 11: Verify only the Color BY group has been ungrouped
        """
        time.sleep(5)
        parent_css="#queryTreeWindow table tr:nth-child(12) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='BUSINESS_REGION_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 24, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 11.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 11.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 11.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 11.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 24, msg='Step 11.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 11.6')
        expected_legend_list=['BUSINESS_REGION_1', 'EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_legends(expected_legend_list, msg='Step 11.7')
        time.sleep(5)  
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Revenue:$51,791,709.98', 'BUSINESS_REGION_1:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 11.8: Verify Tooltip') 
        time.sleep(5)
        visual.take_preview_snapshot(Test_Case_ID ,'11')
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 12: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()