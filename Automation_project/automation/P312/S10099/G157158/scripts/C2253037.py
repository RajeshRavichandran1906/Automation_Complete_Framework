'''
Created on Feb 21, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253037
TestCase Name = Data Visualization Drill Down returns unknown error
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2253037_TestClass(BaseTestCase):

    def test_C2253037(self):
        
        """
        Class Objects
        """
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253037'
        sleep_time=4
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
         
        """
        Step 02. Add fields 'Cost of Goods' from Sales measures and 'Product,Subcategory' from Product dimension.
        Verify vertical and horizontal axis label values:
        """
        field_name='Product,Subcategory'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s0!g20!mbar!']"
        visual.wait_for_number_of_element(parent_css, 1, 30)
        field_name="Cost of Goods"
        visual.double_click_on_datetree_item(field_name,position)
        parent_css="#MAINTABLE_wbody1 text[class*='yaxis-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Cost of Goods', time_out=50)
        visual.verify_x_axis_title(['Product Subcategory'], msg='Step 02.01')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 02.02')
        expected_xaxis_label=['Blu Ray','Boom Box','CRT TV','Charger','DVD Players']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 02.03', xyz_axis_label_length=5)
        expected_yaxis_label=['0', '40M', '80M', '120M', '160M', '200M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 02.04')
        
        """
        Step 03. Verify query pane
        """
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Cost of Goods', position, "Step 03.01:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Subcategory', position, "Step 03.02")

        """
        Step 04. Hover over "FlatPanel TV" bar.
        Verify the tool tip: 
        """
        expected_tooltip_list=['Product Subcategory:Flat Panel TV', 'Cost of Goods:$59,077,345.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        visual.verify_tooltip('riser!s0!g6!mbar!', expected_tooltip_list,'Step 04.01: Verify Tooltip') 
        
        """
        Step 05. Select Drill down to Model.
        Verify Product category drill down to model in horizontal axis:
        """
        visual.select_tooltip('riser!s0!g6!mbar!', "Drill down to Model")
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Model', time_out=50)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class*='riser']", 7, 30)
        visual.verify_x_axis_title(['Model'], msg='Step 05.01')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 05.02')
        expected_xaxis_label=['LG 19LE5300 19', 'LG 32LE5300 32']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 05.03', xyz_axis_label_length=2)
        expected_yaxis_label=['0', '3M', '6M', '9M', '12M', '15M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 05.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 05.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g1!mbar!']", "bar_blue", msg='Step 05.06')
        
        """
        Step 06. Verify query added to filter pane
        """
        
        visual.verify_field_in_filterbox('Product,Subcategory', position, "Step 06.01:")
        
        """
        Step 07. Click Run in the toolbar
        Verify the output
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Model', time_out=50)
   
        visual.verify_x_axis_title(['Model'], msg='Step 07.01')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 07.02')
        expected_xaxis_label=['LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic 58TV25BNDL', 'Panasonic TCP46G25', 'Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 07.03')
        expected_yaxis_label=['0', '3M', '6M', '9M', '12M', '15M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 07.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 07.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g1!mbar!']", "bar_blue", msg='Step 07.06')
        
        """
        Step 08. Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 09: Click "Save" in the toolbar > Type C2141626  > Click "Save" in the Save As dialog
        """
    
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 10: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()