'''
Created on Feb 13, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327844
TestCase Name = Unable to rename group to its base field 
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2327844_TestClass(BaseTestCase):

    def test_C2327844(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2327844'
        sleep_time = 3
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(sleep_time)
        
        """
        Step 02: Double Click "Cost of Goods" and "Product,Category" to add fields
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 1, 100)
        
        visual.double_click_on_datetree_item("Product,Category",1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 100)
        
        visual.verify_x_axis_title(['Product Category'], msg='Step 2.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 2.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 2.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 2.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 2.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 2.6')
        time.sleep(sleep_time)   
        expected_tooltip_list=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 2.7: Verify Tooltip') 
        
        """
        Step 03: Lasso on last two risers
        """
        time.sleep(sleep_time)
        source_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g6!mbar!']")
        target_element=driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g5!mbar!']")
        visual.create_lasso(source_element, target_element, source_xoffset=10, source_element_location='middle_right')
        
        """
        Step 04: Click " Group Product,Category Selection ".
        """
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Group Product,Category Selection')
        
        """
        Step 05: Verify the preview updated
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 6, 100)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 5.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 5.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 5.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 5.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 5.7:")
        time.sleep(sleep_time)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 5.8: Verify Tooltip') 
        
        """
        Step 06: Click any riser (First riser)
        """
        time.sleep(sleep_time)
        riser_css=driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        visual.select_chart_component(riser_css)
        
        """
        Step 07: Click "Rename group PRODUCT_CATEGORY_1"
        """
        time.sleep(sleep_time)
        visual.select_lasso_tooltip('Rename group PRODUCT_CATEGORY_1')
        
        """
        Step 08: Type "PRODUCT_CATEGORY" in input box
        Step 09: Click OK
        """
        visual.rename_grouped_riser_name('PRODUCT_CATEGORY_1', 'PRODUCT_CATEGORY', 'OK')
        
        """
        Step 10: Verify following message displayed
        """
        visual.verify_popup_or_dialog_caption_text("[id^='BiDialog'] div[class^='bi-window-caption']", 'Message', 'Step 10.1')
        visual.verify_dialogs_and_popups_text("div[id^='BiOptionPane']>div[class='bi-label']", "Name already in use, select a new name.", 'Step 10.2')
        
        """
        Step 11: Click OK to dismiss
        """
        visual.click_any_bibutton_in_dialog()
        
        """
        Step 12: Verify preview not changed
        """
        parent_css="#queryTreeWindow table tr:nth-child(9) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='PRODUCT_CATEGORY_1', time_out=300)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, 6, 100)
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 12.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 12.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 12.3')
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 12.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 6, msg='Step 12.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 12.6')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_CATEGORY_1', 1, "Step 12.7:")
        time.sleep(sleep_time)   
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 12.8: Verify Tooltip') 
        visual.take_preview_snapshot(Test_Case_ID ,'12')
        
        """
        Step 13: Click Save in the toolbar > Save as "C2327844" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 14: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()