'''
Created on Feb 14, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327758
TestCase Name = Renaming group not allow <space> in between the group name
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327758_TestClass(BaseTestCase):

    def test_C2327758(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327758'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        sleep_time = 3
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(sleep_time)
        
        """
        Step 02: Add "Revenue", "Product,Category"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 100)
        
        visual.double_click_on_datetree_item("Product,Category",1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 100)
        
        visual.verify_x_axis_title(['Product Category'], msg='Step 2.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 2.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 2.6')
        time.sleep(sleep_time)   
        expected_tooltip_list=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Lasso first four risers from left side 
        """
        time.sleep(sleep_time)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g3!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=-15, source_element_location='middle_left')
        
        """
        Step 04: Click " Group Product,Category Selection ".
        """
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Group Product,Category Selection')

        """
        Step 05: Verify group created and updated in data pane,query pane and horizontal axis of chart
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 4, 100)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 5.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 5.2')
        expected_xaxis_label=['Accessories and Camcorder and Computers and 1 more', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 4, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 5.6')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_CATEGORY_1', 1, "Step 5.7:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 5.8:")
        time.sleep(sleep_time)
#         expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers and 1 more', 'Revenue:$633,463,582.26', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
#         visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 5.9: Verify Tooltip') 

        """
        Step 06: Click any riser 
        """
        time.sleep(sleep_time)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g1!mbar!']")
        visual.select_chart_component(riser_css)
        
        """
        Step 07: Click " Rename group PRODUCT_CATEGORY_1"
        """
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Rename group PRODUCT_CATEGORY_1')
        
        """
        Step 08: Type "Group Name Testing"
        Step 09: Click OK
        """
        visual.rename_grouped_riser_name('PRODUCT_CATEGORY_1', 'Group Name Testing', 'OK')
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='GroupNameTesting', time_out=300)

        """
        Step 10: Verify no error occurs and data pane ,querypane and horizontal axis updated with "GroupNameTesting" name.
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='GroupNameTesting', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 4, 100)
        visual.verify_x_axis_title(['GroupNameTesting'], msg='Step 10.1')
        visual.verify_y_axis_title(['Revenue'], msg='Step 10.2')
        expected_xaxis_label=['Accessories and Camcorder and Computers and 1 more', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_yaxis_label=['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 4, msg='Step 10.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 10.6')
        visual.verify_field_listed_under_datatree('Customer', 'GroupNameTesting', 1, "Step 10.7:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'GroupNameTesting', 1, "Step 10.8:")
        time.sleep(sleep_time)   
#         expected_tooltip_list=['GroupNameTesting:Accessories and Camcorder and Computers and 1 more', 'Revenue:$633,463,582.26', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
#         visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 10.9: Verify Tooltip') 
        visual.take_preview_snapshot(Test_Case_ID ,'10')
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 11: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()