'''
Created on Feb 21, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253021
TestCase Name = IA-3780: Visualization drill down doesn't work on Rows and columns at run time
'''
import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2253021_TestClass(BaseTestCase):

    def test_C2253021(self):
        
        """
        CLASS & OBJECTS        
        """
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES        
        """
        Test_Case_ID = 'C2253021'
        sleep_time=4
        position=1
        riser=[7,139,4]
        time_out=300
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Add Product Category to Horizontal axis and Quantity Sold to Vertical axis.
        Verify label values
        """
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[0], time_out)
        
        field_name='Quantity,Sold'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxis-title']"
        visual.wait_for_number_of_element(parent_css, 1, time_out)

        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 02.01')
        y_axis_title=['Quantity Sold']
        visual.verify_y_axis_title(y_axis_title, msg='Step 02.02')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 02.03')
        expected_yaxis_label=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 02.04')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, riser[0], msg='Step 02.05')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 02.06')
        
        """
        Step 03: Hover over "Accessories" bar.
        Verify the tool tip:
        """
        expected_tooltip_list=['Product Category:Accessories', 'Quantity Sold:511,667', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 03.01: Verify Tooltip') 
        
        """
        Step 04: Add Sale Year to Rows and Store Business Region to Columns.
        Verify query pane
        """
        visual.drag_field_from_data_tree_to_query_pane('Sale,Year', 1, 'Rows', 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Sale,Year', time_out=time_out)
        
        visual.drag_field_from_data_tree_to_query_pane('Store,Business,Region', 1, 'Columns', 1)
        parent_css="#queryTreeWindow table tr:nth-child(6) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Store,Business,Region', time_out=time_out)
        
        parent_css="#MAINTABLE_wbody1 text[class^='colHeader-label!']"
        visual.wait_for_visible_text(parent_css, visble_element_text='StoreBusinessRegion', time_out=time_out)
        visual.verify_field_listed_under_querytree('Rows', 'Sale,Year', position, "Step 04.01")
        visual.verify_field_listed_under_querytree('Columns', 'Store,Business,Region', position, "Step 04.02")
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Quantity,Sold', position, "Step 04.03")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, "Step 04.04")
        
        """
        Step 05: Verify "2011 EMEA Accessories" bar.
        Verify the tool tip:
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[1], time_out)
        expected_tooltip_list=['Sale Year:2011', 'Store Business Region:EMEA', 'Product Category:Accessories', 'Quantity Sold:13,435', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!r0!c0!', expected_tooltip_list,'Step 05.01: Verify Tooltip') 
   
        """
        Step 06: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 07: Hover over on 2012 EMEA, Media Player and click on Sale Year and Drill down.
        Verify output:
        """
        parent_css="#MAINTABLE_wbody1 text[class^='colHeader-label!']"
        visual.wait_for_visible_text(parent_css, visble_element_text='StoreBusinessRegion', time_out=time_out)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[1], time_out)
        visual.select_tooltip('riser!s0!g3!mbar!r1!c0!', "Drill down to->Sale Quarter")
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[2], time_out)

        visual.verify_y_axis_title(['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold'], msg='Step 07.01')
        expected_xaxis_label=['Media Player']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 07.02')
        expected_yaxis_label=['0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 07.03')
        expected_row_label_list=['Sale Quarter', '1', '2', '3', '4']
        visual.verify_rows_label(expected_row_label_list, msg="Step 07.04")
        expected_column_label_list=['Store Business Region : Product Category', 'EMEA']
        visual.verify_column_label(expected_column_label_list, msg="Step 07.05")
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, riser[2], msg='Step 07.06')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!r0!c0!']", "bar_blue", msg='Step 07.07')
    
        """
        Step 08: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 09: Click "Save" in the toolbar > Type C2141372 > Click "Save" in the Save As dialog
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[1])
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        
        """
        Step 10: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()