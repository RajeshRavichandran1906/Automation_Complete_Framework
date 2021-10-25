'''
Created on Sept 17, 2018

@author: Varun

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/11397
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6760144
TestCase Name = Add bin to horizontal axis
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C6760144_TestClass(BaseTestCase):

    def test_C6760144(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C6760144'
        visual_obj=visualization.Visualization(self.driver)
        core_obj = core_metadata.CoreMetaData(self.driver)
        expected_xval_list=['.00', '100.00', '200.00', '300.00', '400.00', '500.00', '600.00', '700.00', '800.00', '900.00', '1,100.00', '1,200.00', '1,300.00', '1,900.00', '2,200.00', '3,300.00', '3,400.00', '3,900.00']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        
        """
        Step 01: Invoke IA Visualization tool with wf_retail
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=wf_retail
        """
        visual_obj.invoke_visualization_using_api('baseapp/wf_retail')
        
        """
        Step 02: Expand Product > Model > Attributes
        """
        core_obj.expand_data_field_section("Product->Product->Model->Attributes")
              
        """
        Step03: Right click Price,Dollars > Create Bins...
        Step04: Change bin width to 100 > OK
        """       
        visual_obj.right_click_on_datetree_item("Price,Dollars",1,'Create Bins...')
        visual_obj.create_bins("PRICE_DOLLARS_BIN_1", bin_width='100', btn_click='OK')
      
        """
        Step05: Double click the bin to add to horizontal axis (can't be done right now because of IA-7034, for the time being drag the bin to horizontal axis instead)
        """ 
        visual_obj.double_click_on_datetree_item('Attributes->PRICE_DOLLARS_BIN_1', 1)
        parent_css="#MAINTABLE_wbody1_f .risers rect"
        visual_obj.wait_for_number_of_element(parent_css,18,180)
        visual_obj.verify_x_axis_title(['PRICE_DOLLARS_BIN_1'], msg="step 5a) Verify X-axis title")
        visual_obj.verify_x_axis_label(expected_xval_list, msg="Step 5b) Verify X-axis label")
        
        
        """
        Step 06: Double click Quantity,Sold
        """
        visual_obj.double_click_on_datetree_item('Sales->Quantity,Sold', 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        visual_obj.wait_for_number_of_element(parent_css, 5, 180)
        visual_obj.verify_x_axis_title(['PRICE_DOLLARS_BIN_1'], msg="step 6a) Verify X-axis title")
        visual_obj.verify_y_axis_title(['Quantity Sold'],msg="Step 6b) Verify Y-axis title")
        visual_obj.verify_x_axis_label(expected_xval_list, msg="Step 6c) Verify X-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,msg="Step 6d) Verify Y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 18, msg="Step 6e) Verify Risers")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g0!mbar\"]", "bar_blue", msg="Step 6f) Verify the bar colour")
        
        """
        Step07: Click Run
        """
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_new_window()
         
        """
        Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual_obj.wait_for_number_of_element(parent_css, 18, 180)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        visual_obj.wait_for_number_of_element(parent_css, 5, 180)
        visual_obj.verify_x_axis_title(['PRICE_DOLLARS_BIN_1'], msg="step 7a) Verify X-axis title")
        visual_obj.verify_y_axis_title(['Quantity Sold'],msg="Step 7b) Verify Y-axis title")
        visual_obj.verify_x_axis_label(expected_xval_list, msg="Step 7c) Verify X-axis label")
        visual_obj.verify_y_axis_label(expected_yval_list,msg="Step 7d) Verify Y-axis label")
        visual_obj.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 18, msg="Step 7e) Verify Risers")
        visual_obj.verify_chart_color_using_get_css_property("rect[class*=\"riser!s0!g0!mbar\"]", "bar_blue", msg="Step 7f) Verify the bar colour")

         
        """
        Step 08: Close output, save visualization with name C6760144 and close IA.
        """
        visual_obj.switch_to_previous_window()
        visual_obj.wait_for_number_of_element("#applicationButton img", 1, 120)
        visual_obj.save_as_visualization_from_menubar(Test_Case_ID)

        
if __name__ == '__main__':
    unittest.main()