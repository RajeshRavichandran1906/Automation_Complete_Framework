'''
Created on Feb 14, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253035
TestCase Name = Drill up on Transaction Date changes Year filter to SUM (Year) filter
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import core_metadata

class C2253035_TestClass(BaseTestCase):

    def test_C2253035(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253035'
        visual = visualization.Visualization(self.driver)
        metadataobj = core_metadata.CoreMetaData(self.driver)
        sleep_time=6
        position=1
               
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(sleep_time)
         
        
        """
        Step 02. Add Product Category to the Horizontal Axis and Quantity Sold to the Vertical Axis.
        """
        time.sleep(5)
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(5)
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 30)
        field_name="Quantity,Sold"
        visual.double_click_on_datetree_item(field_name,position)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Quantity Sold", 45)
         
        """
        Step 03. Verify label values
        """
        x_axis_title=['Product Category']
        visual.verify_x_axis_title(x_axis_title, msg='Step 3.1')
        y_axis_title=['Quantity Sold']
        visual.verify_y_axis_title(y_axis_title, msg='Step 3.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 3.3')
        expected_yaxis_label=['0', '0.3M', '0.6M', '0.9M', '1.2M']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 3.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 3.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!']", "bar_blue", msg='Step 3.6')
         
        """
        Step 04. Verify any bar riser values
        """
        time.sleep(sleep_time)   
        expected_tooltip_list=['Product Category:Accessories', 'Quantity Sold:511,667', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 4.1: Verify Tooltip') 
         
        """
        Step 05. Add Sale,Year to Rows
        """
        time.sleep(sleep_time)
        field_name='Sale,Year'
        visual.drag_field_from_data_tree_to_query_pane(field_name, position, "Rows")
        
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        visual.wait_for_visible_text(parent_css, visble_element_text='Sale,Year', time_out=50)
         
        """
        Step 06. Verify query pane
        """
        visual.verify_field_listed_under_querytree('Rows', 'Sale,Year', position, "Step 06.1:")
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Quantity,Sold', position, "Step 06.2:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, "Step 06.3:")
        
        """
        Step 07. Drag and drop Sale,Year to filter pane, accept defaults and click ok.
        """
        time.sleep(sleep_time)
        visual.drag_and_drop_from_data_tree_to_filter('Sale,Year', position)
                
        visual.close_filter_dialog('ok')
        visual.wait_for_visible_text("#qbFilterBox table>tbody>tr", 'Sale,Year', time_out=40)
        """
        Step 08. verify query added to filter pane
        """
        time.sleep(sleep_time)   
        visual.verify_field_in_filterbox('Sale,Year', position, "Step 8:")
        
         
        """
        Step 09. Move the Range from both sides 2025 to 2014(it displays only 2014)
        """
        visual.move_slider_using_page_up_or_down_key(3, parent_css='#ar_Prompt_1', drag_button='max', move_type='left', comparison_type='str')
        time.sleep(sleep_time)
        visual.move_slider_using_page_up_or_down_key(3, parent_css='#ar_Prompt_1', drag_button='min', move_type='right', comparison_type='str')
        parent_css="#MAINTABLE_wbody1 text[class^='rowLabel!r0!']"
        visual.wait_for_visible_text(parent_css, visble_element_text='2014', time_out=50)
        """
        Step 10. Verify any bar riser values
        """
        element_css="#MAINTABLE_wbody1 [class^='riser!s0']"
        visual.wait_for_number_of_element(element_css, 7, 30)
        expected_tooltip_list=['Sale Year:2014', 'Product Category:Accessories', 'Quantity Sold:63,836', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list,'Step 10.1: Verify Tooltip') 
        time.sleep(sleep_time)
        
        """
        Step 11. Hover on a bar (Media player) and select drilldown on Sale, Quarter
        """
        visual.select_tooltip('riser!s0!g3!mbar!', "Drill down to->Sale Quarter")
        
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 4, 30)
        
        """
        Step 12. Verify query added to filter pane
        """
        time.sleep(sleep_time)
        visual.verify_field_in_filterbox('Sale,Year', position, "Step 12a:")
        time.sleep(sleep_time)   
        visual.verify_field_in_filterbox('TIME_YEAR and PRODUCT_CATEGORY', position+1, "Step 12b:")
        time.sleep(sleep_time)   
         
        """
        Step 13. Verify first bar value
        """         
        expected_tooltip_list=['Sale Quarter:1', 'Product Category:Media Player', 'Quantity Sold:22,232', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip('riser!s0!g0!mbar!r0!c0!', expected_tooltip_list,'Step 13.1: Verify Tooltip') 
        time.sleep(sleep_time)
        
        """
        Step 14. Hover on second bar and select Drill Up on Sale Year
        """
        visual.select_tooltip('riser!s0!g0!mbar!r1!c0!', "Drill up to Sale Year")
        parent_css="#MAINTABLE_wbody1 [class^='riser!']"
        visual.wait_for_number_of_element(parent_css, 7, time_out=60)
        
         
        """
        Step 15. Verify query in filter dailog does not change to SUM
        """
        visual.verify_field_in_filterbox('Sale,Year', position, "Step 15.1:")
        time.sleep(sleep_time)
       
        visual.verify_field_in_filterbox('TIME_YEAR and PRODUCT_CATEGORY', position+1, "Step 15.2:")
        time.sleep(sleep_time)   
         
        
        """
        Step 16: Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        time.sleep(10)
        visual.switch_to_new_window()
        
        """
        Step 17: Verify output 
        """
        parent_css="#MAINTABLE_wbody1 text[class^='xaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Product Category', time_out=50)
        time.sleep(sleep_time)
        visual.verify_x_axis_title(['Product Category'], msg='Step 17.1')
        visual.verify_y_axis_title(['Quantity Sold'], msg='Step 17.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 17.3')
        expected_yaxis_label=['0', '40K', '80K', '120K', '160K']
        visual.verify_y_axis_label(expected_yaxis_label, msg='Step 17.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 7, msg='Step 17.5')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g3!mbar!']", "bar_blue", msg='Step 17.6')
        time.sleep(sleep_time)
        expected_tooltip_list=['Sale Year:2014', 'Product Category:Media Player', 'Quantity Sold:92,435', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_tooltip('riser!s0!g3!mbar!', expected_tooltip_list,'Step 17.7: Verify Tooltip')
        #visual.verify_slider_min_max_value_in_run_window('2011', parent_css = '#LOBJ1_cs', msg = 'Step 17', drag_button='min', comparison_type='str')
        
        visual.take_run_window_snapshot(Test_Case_ID, '17')
        
        """
        Step 18: Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 19: Click "Save" in the toolbar > Type C2141218 > Click "Save" in the Save As dialog
        """
        time.sleep(sleep_time)
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 20: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()