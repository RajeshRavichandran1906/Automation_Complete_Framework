'''
Created on Feb 21, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253036
TestCase Name = IA-3781:Visualization default tool tip is wrong after drill down at run time
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253036_TestClass(BaseTestCase):

    def test_C2253036(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253036'
        visual = visualization.Visualization(self.driver)
        sleep_time=4
        position=1
             
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(sleep_time)
             
        """
        Step 02. Double click "Quantity,Sold" and "Product,Category".
        Verify vertical and horizontal axis labels:
        """
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class*='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 30)
        field_name="Quantity,Sold"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 30)
        x_axis_title=['Product Category']
        y_axis_title=['Quantity Sold']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual.verify_x_axis_title(x_axis_title, msg='Step 02.01')
        visual.verify_y_axis_title(y_axis_title, msg='Step 02.02')
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=8, msg='Step 02.03')
        visual.verify_y_axis_label(y_axis_label, msg='Step 02.04')
        
        """
        Step 03. Verify query pane
        """
        
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Quantity,Sold', position, "Step 03.01")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, "Step 03.02")
         
        """
        Step 04. Hover on "Media Player" bar.
        Verify the tool tip:
        """  
        expected_tooltip_list=['Product Category:Media Player', 'Quantity Sold:771,934', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g3!mbar!', expected_tooltip_list,'Step 04.01: Verify Tooltip') 
        time.sleep(sleep_time)   
        
        
        """
        Step 05: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 06. Hover over "Accessories" bar and Select "Drill down to Product Subcategory".
        Verify vertical and horizontal axis label values:
        """
        visual.select_tooltip('riser!s0!g0!mbar!', "Drill down to Product Subcategory")
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 3, 30)
        x_axis_title=['Product Subcategory']
        y_axis_title=['Quantity Sold']
        x_axis_label=['Charger', 'Headphones', 'Universal Remote Controls']
        y_axis_label=['0', '40K', '80K', '120K', '160K', '200K', '240K']
        visual.verify_x_axis_title(x_axis_title, msg='Step 06.01')
        visual.verify_y_axis_title(y_axis_title, msg='Step 06.02')
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=8, msg='Step 06.03')
        visual.verify_y_axis_label(y_axis_label, msg='Step 06.04')
        
        """
        Step 07. Hover on "Headphones" bar.
        Verify the tool tip:
        """
        expected_tooltip_list=['Product Subcategory:Headphones', 'Quantity Sold:228,349', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip('riser!s0!g1!mbar!', expected_tooltip_list,'Step 07.01: Verify Tooltip')
        time.sleep(sleep_time)
          
        """
        Step 08. Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 09: Click "Save" in the toolbar > Type C2141625 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 10: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()