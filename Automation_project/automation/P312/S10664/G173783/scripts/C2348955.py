'''
Created on Feb 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348955
TestCase Name = Ungroup All with 2 group values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348955_TestClass(BaseTestCase):

    def test_C2348955(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348955'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(4)
        
        """
        Step 02: Double click "Gross Profit", Product, Category"
        """
        visual.double_click_on_datetree_item('Gross Profit', 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 300)
        
        visual.double_click_on_datetree_item("Product,Category",1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        
        time.sleep(5)
        visual.verify_x_axis_title(['Product Category'], msg='Step 2.1')
        visual.verify_y_axis_title(['Gross Profit'], msg='Step 2.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '20M', '40M', '60M', '80M', '100M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 2.6')
        
        """
        Step 03: Lasso Camcorder and Computer riser > Group Product, Category selection
        """
        time.sleep(5)
        camcorder_riser=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g1!mbar!']")
        computer_riser=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g2!mbar!']")
        visual.create_lasso(camcorder_riser, computer_riser, source_xoffset=-6, source_element_location='middle_left')
        time.sleep(3)
        visual.select_lasso_tooltip('Group Product,Category Selection')
        
        """
        Step 04: Multi select "Stereo systems and Video production" > Group PRODUCT_CATEGORY_1 selection
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, 300)
        stereo_systems=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g3!mbar!']")
        video_production=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g5!mbar!']")
        visual.multi_select_chart_component([stereo_systems, video_production])
        time.sleep(2)
        visual.select_lasso_tooltip('Group PRODUCT_CATEGORY_1 Selection')
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 5, 300)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 4.1')
        visual.verify_y_axis_title(['Gross Profit'], msg='Step 4.2')
        expected_xaxis_label=['Accessories', 'Camcorder and Computers', 'Media Player', 'Stereo Systems and Video Production', 'Televisions']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 4.3')
        expected_yaxis_label=['0', '20M', '40M', '60M', '80M', '100M', '120M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 4.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 5, msg='Step 4.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 4.6')
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 4.7: Verify Tooltip') 
        
        """
        Step 05: Click on any riser > Ungroup All
        """
        time.sleep(5)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        time.sleep(2)
        visual.select_lasso_tooltip('Ungroup All')
        
        """
        Step 06: Verify preview updated to ungrouped all grouped values
        """
        time.sleep(5)
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        time.sleep(5)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 6.1')
        visual.verify_y_axis_title(['Gross Profit'], msg='Step 6.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 6.3')
        expected_yaxis_label=['0', '20M', '40M', '60M', '80M', '100M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 6.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 6.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 6.6')
        time.sleep(5)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 6.7: Verify Tooltip') 
        
        """
        Step 07: Right click on "PRODUCT_CATEGORY_1" query or data pane > Edit group
        """
        visual.right_click_on_field_under_query_tree("PRODUCT_CATEGORY_1", 1, context_menu_path='Edit Group...')
        
        """
        Step 08: Verify there are no group values in the group
        Step 09: Click Cancel
        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        expected_group_dialog_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 08:01:Verify grid values")
        visual.exit_group_dialog('cancel')
        time.sleep(5)
        visual.take_preview_snapshot(Test_Case_ID ,'09')
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 10: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()