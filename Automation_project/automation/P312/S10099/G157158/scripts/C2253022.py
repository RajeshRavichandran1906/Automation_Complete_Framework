'''
Created on Feb 17, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253022
TestCase Name = IA-3764:Visualizations drill up/down/create slow due to use of FPRINT
'''

import unittest, time
from common.pages import core_metadata
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2253022_TestClass(BaseTestCase):

    def test_C2253022(self):
        
        """
        TESTCASE OBJECTS        
        """
        visual = visualization.Visualization(self.driver)
        metadataobj = core_metadata.CoreMetaData(self.driver)
        
        """
        TESTCASE VARIABLES        
        """
        Test_Case_ID = 'C2253022'
        sleep_time=4
        position=1
        riser=[7,42,4]
        time_out=200
        num=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02: Add Product Category to Horizontal axis, Quantity Sold to Vertical axis and Sale Year to Rows.
        """
        time.sleep(5)
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[0], time_out)
        
        field_name='Quantity,Sold'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxis-title']"
        visual.wait_for_number_of_element(parent_css, num, time_out)
        
        visual.right_click_on_datetree_item('Sale,Year', position, context_menu_path='Add To Query->Rows')
        query_pane="#queryTreeWindow"
        visual.wait_for_visible_text(query_pane, visble_element_text='Sale,Year', time_out=time_out)
        
        """
        Step 03: Verify label values
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[1], time_out)
        visual.verify_x_axis_title(['Product Category'], msg='Step 3.1')
        visual.verify_y_axis_title(['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold'], msg='Step 3.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '100K', '200K', '300K', '400K', '500K', '0', '100K', '200K', '300K', '400K', '500K', '0', '100K', '200K', '300K', '400K', '500K', '0', '100K', '200K', '300K', '400K', '500K', '0', '100K', '200K', '300K', '400K', '500K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', num, riser[1], msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g3!mbar!r3!c0!']", "bar_blue", msg='Step 3.6')
        expected_row_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        visual.verify_rows_label(expected_row_label_list, msg="Step 03.7:")
        expected_tooltip_list=['Sale Year:2014', 'Product Category:Media Player', 'Quantity Sold:92,435', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g3!mbar!r3!c0!', expected_tooltip_list,'Step 3.8: Verify Tooltip') 
        
        """
        Step 04: Verify query pane
        """
        visual.verify_field_listed_under_querytree('Rows', 'Sale,Year', position, "Step 04.1:")
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Quantity,Sold', position, "Step 04.2:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, "Step 04.3:")
        
        """
        Step 05: Verify 2015 Stereo systems tooltip
        """
        expected_tooltip_list=['Sale Year:2015', 'Product Category:Stereo Systems', 'Quantity Sold:302,717', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g4!mbar!r4!c0!', expected_tooltip_list,'Step 05: Verify Tooltip') 
        
        """
        Step 06: Hover over 2012 Accessories > Click Drill down > "Sale Quarter "
        """
        time.sleep(10)
        visual.select_tooltip('riser!s0!g0!mbar!r1!c0!', "Drill down to->Sale Quarter")
        
        """
        Step 07: Verify query added to fitler pane
        """
        parent_css="#qbFilterBox table>tbody>tr>td img"
        visual.wait_for_number_of_element(parent_css, position, time_out)
        visual.verify_field_in_filterbox('TIME_YEAR and PRODUCT_CATEGORY', position, "Step 07:")
        
        """
        Step 08: Hover on first bar and verify sale Year is changed to Sale Quarter in tooltip.
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[2], time_out)
        expected_tooltip_list=['Sale Quarter:1', 'Product Category:Accessories', 'Quantity Sold:7,121', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!r0!c0!', expected_tooltip_list,'Step 08: Verify Tooltip')
        
        """
        Step 09: Click Run in the tooltip
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 10: Verify output
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        visual.wait_for_number_of_element(parent_css, riser[2], time_out)
        visual.verify_x_axis_title(['Product Category'], msg='Step 10.1')
        visual.verify_y_axis_title(['Quantity Sold', 'Quantity Sold', 'Quantity Sold', 'Quantity Sold'], msg='Step 10.2')
        expected_xaxis_label=['Accessories']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 10.3')
        expected_yaxis_label=['0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000', '0', '2,000', '4,000', '6,000', '8,000', '10,000']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 10.4')
        expected_row_label_list=['Sale Quarter', '1', '2', '3', '4']
        visual.verify_rows_label(expected_row_label_list, msg="Step 10.5:")
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', num, riser[2], msg='Step 10.7')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!r0!c0!']", "bar_blue", msg='Step 10.8')
        expected_tooltip_list=['Sale Quarter:1', 'Product Category:Accessories', 'Quantity Sold:7,121', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!r0!c0!', expected_tooltip_list,'Step 10.9: Verify Tooltip')
        visual.take_run_window_snapshot(Test_Case_ID, '10')
        
        """
        Step 11: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 12: Click "Save" in the toolbar > Type C2141373 > Click "Save" in the Save As dialog
        """
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, riser[2])
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 13: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()