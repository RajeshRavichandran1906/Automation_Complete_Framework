'''
Created on Feb 01, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327784
TestCase Name = Vis Paperclipping disallows grouping of duplicate values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327784_TestClass(BaseTestCase):

    def test_C2327784(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327784'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        visual.wait_for_number_of_element(parent_css, 1, 250)

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
        
        """
        Step 03: Drag and drop "Store,business,Sub Region" to rows
        """
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Sub Region', 0, 'Rows')
        time.sleep(6)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Store,Business,SubRegion', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 98, 200)
        time.sleep(5)
        visual.verify_x_axis_title(['Product Category'], msg='Step 3.1')
        visual.verify_y_axis_title(['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue'], msg='Step 3.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 98, msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g3!mbar!r3!c0!']", "bar_blue", msg='Step 3.6')
        expected_row_label_list=['Store Business Sub Region', 'Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico']
        visual.verify_rows_label(expected_row_label_list, msg="Step 03:a(iii):")
        time.sleep(5)   
        expected_tooltip_list=['Store Business Sub Region:Canada', 'Product Category:Media Player', 'Revenue:$12,324,188.57', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to']
        visual.verify_tooltip('riser!s0!g3!mbar!r3!c0!', expected_tooltip_list,'Step 3.7: Verify Tooltip') 
        
        """
        Step 04: Lasso on two riser(Media player, Stereo systems) of "Asia" row and click "Group Store,business,Sub Region selection" in tooltip
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g3!mbar!r1!c0!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g4!mbar!r1!c0!']")
        visual.create_lasso(source_element, target_element, source_yoffset=10, target_xoffset=10, source_element_location='bottom_middle')
        time.sleep(3)
        visual.select_lasso_tooltip('Group Store,Business,Sub Region Selection')
        
        """
        Step 05: Verify Group created and displaying following
        """
        time.sleep(5)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='BUSINESS_SUB_REGION_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 98, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['Product Category'], msg='Step 5.1')
        visual.verify_y_axis_title(['Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue', 'Revenue'], msg='Step 5.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M', '0', '30M', '60M', '90M', '120M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 98, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g3!mbar!r3!c0!']", "bar_blue", msg='Step 5.6')
        expected_row_label_list=['BUSINESS_SUB_REGION_1', 'Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico']
        visual.verify_rows_label(expected_row_label_list, msg="Step 05:a(iii):")
        time.sleep(5)  
        expected_tooltip_list=['BUSINESS_SUB_REGION_1:Europe', 'Product Category:Media Player', 'Revenue:$93,863,962.23', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Region', 'Drill down to']
        visual.verify_tooltip('riser!s0!g3!mbar!r5!c0!', expected_tooltip_list,'Step 5.7: Verify Tooltip') 
        
        """
        Step 06: Right click on Created "BUSINESS_SUB_REGION_1" 
        Step 07: select "Edit Group"
        """
        visual.right_click_on_field_under_query_tree("BUSINESS_SUB_REGION_1", 1, context_menu_path='Edit Group...')
        
        """
        Step 08: Verify Edit group dialog displayed following
        Step 09: Click Cancel
        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        expected_group_dialog_list=['Africa', 'Asia', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 08:01:Verify grid values")
        visual.exit_group_dialog('cancel')
        time.sleep(5)
        visual.take_preview_snapshot(Test_Case_ID ,'09')
        
        """
        Step 10: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()