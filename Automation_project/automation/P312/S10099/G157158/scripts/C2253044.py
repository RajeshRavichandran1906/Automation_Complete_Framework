'''
Created on Feb 23, 2018

@author: Robert

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2253044
TestCase Name = Slider Range resets to All when drill up 
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253044_TestClass(BaseTestCase):

    def test_C2253044(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253044'
        visual = visualization.Visualization(self.driver)
        sleep_time=4
        position=1
        chart_type='bar'
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS8358&tool=idis&master=baseapp/WF_RETAIL_LITE
        """
        visual.invoke_visualization_using_api('new_retail/wf_retail_lite')

        """
        Step 02. Change to chart type Heatmap
        """
        visual.change_chart_type('heatmap')
         
        """
        Step 03. Add Dimensions/Product/Product/Product,Category to Vertical axis.
        Step 04. Add Dimensions/Store/Store/Store,Business,Region to Horizontal axis
        """
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 21, 30)
        field_name="Store,Business,Region"
        visual.drag_field_from_data_tree_to_query_pane(field_name, 1, 'Horizontal Axis', 1)
        parent_css="#MAINTABLE_wbody1 text[class^='yaxisOrdinal-title']"
        visual.wait_for_visible_text(parent_css, visble_element_text='Store Business Region', time_out=50)
          
        """
        Step 05. Verify axis label values
        """
        xy_axis_title=['Store Business Region', 'Product Category']
        visual.verify_x_axis_title(xy_axis_title, msg='Step 5.1 Verify X and Y axis titles')
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 5.3')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 5.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 0, msg='Step 5.5')
        expected_legend_list=['0', '0.3', '0.5', '0.8', '1']
        visual.verify_legends(expected_legend_list, msg='Step 5.6. Verify the legends')
         
         
        """
        Step 06. Add Measures/Gross Profit to Color
        """
        visual.drag_field_from_data_tree_to_query_pane('Gross Profit', 1, 'Color', 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 28, 60)
        
        """
        Step 07. Add Dimensions/Shipments_Related/Transaction Date.Simple/Sale,Year to Row
        """
        visual.right_click_on_datetree_item('Sale,Year', 1, 'Add To Query->Rows')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 139, 60)
        
        """
        Step 08. Add Dimensions/Shipments_Related/Transaction Date.Simple/Sale,Quarter to Column
        """
        visual.right_click_on_datetree_item('Sale,Quarter', 1, 'Add To Query->Columns')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 538, 60)
        
            
        """
        Step 09. Verify query pane   
        """
        visual.verify_field_listed_under_querytree('Rows', 'Sale,Year', position, "Step 06.1:")
        visual.verify_field_listed_under_querytree('Columns', 'Sale,Quarter', position, "Step 06.2:")
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Product,Category', position, "Step 06.3:")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Store,Business,Region', position, "Step 06.4:")
        visual.verify_field_listed_under_querytree('Color', 'Gross Profit', position, "Step 06.5:")
         
        """
        Step 10. Verify 2012:Stereo systems tooltip
        Step 11. Verify 2016:NorthAmerica:Video production tooltip
        """
         
         
        expected_tooltip_list=['Sale Year:2012', 'Sale Quarter:1', 'Gross Profit:$694,748.72', 'Product Category:Stereo Systems', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip("riser!s4!g0!mbar!r1!c0!", expected_tooltip_list,'Step 10: Verify 2012:Stereo systems Tooltip')
         
        expected_tooltip_list=['Sale Year:2016', 'Sale Quarter:1', 'Gross Profit:$1,214,855.08', 'Product Category:Video Production', 'Store Business Region:North America', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        visual.verify_tooltip("riser!s6!g1!mbar!r5!c0!", expected_tooltip_list,'Step 11: Verify 2016:NorthAmerica Tooltip')
        """
        Step 12. Add Sale,Year to Filter
        """
         
        visual.drag_and_drop_from_data_tree_to_filter('Sale,Year', 1)
        visual.wait_for_number_of_element("#avFilterOkBtn", 1, 30)
        visual.close_filter_dialog('ok')
        parent_css="#qbFilterBox table>tbody>tr"
        visual.wait_for_visible_text(parent_css, visble_element_text='Sale,Year', time_out=50)
         
        """
        Step 13. Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('Sale,Year', position, "Step 13:")
         
        """
        Step 14. Drill down to Sale Month for any product category(2012:Stereo systems).
        """
        time.sleep(20)
        visual.select_tooltip("riser!s0!g0!mbar!r0!c0!", "Drill down to->Sale Month")
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 3, 60)
        
        """
        Step 15. Verify sale quarter drilldown to sale month
        """
   
        visual.verify_x_axis_title(['Product Category', 'Store Business Region', 'Store Business Region', 'Store Business Region'], msg='Step 15.1')
        
        expected_xaxis_label=['EMEA', 'EMEA', 'EMEA']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 15.3')
        expected_zaxis_label=['Accessories']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 15.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 3, msg='Step 15.5')
        expected_label_list=['Sale Year', '2011']
        visual.verify_rows_label(expected_label_list, msg='Step 15.6 Verify row labels')
        expected_label_list=['Sale Month', '1', '2', '3', 'Gross Profit', '67.6K', '73.8K', '80K', '86.2K', '92.4K']
        visual.verify_column_label(expected_label_list, msg='Step 15.7 Verify column labels')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!r0!c0!']", "golden_glow", msg='Step 15.6')
        
        """
        Step 16. Verify query added to filter pane
        """
        visual.verify_field_in_filterbox('Sale,Year', position, "Step 16:")
        visual.verify_field_in_filterbox('TIME_YEAR and TIME_QTR and BUSINESS_REGION and PRODUCT_CATEGORY', position+1, "Step 16:")
        
        """
        Step 17. Verify each bar riser tooltip
        """
        expected_tooltip_list=['Sale Year:2011', 'Sale Month:1', 'Gross Profit:$77,581.42', 'Product Category:Accessories', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        visual.verify_tooltip("riser!s0!g0!mbar!r0!c0!", expected_tooltip_list,'Step 17: Verify Tooltip')
        
        
        """
        Step 18. Drill Up on Sale, Month for any product category
        """
        visual.select_tooltip("riser!s0!g0!mbar!r0!c0!", "Drill up to Sale Quarter")
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 538, 60)
        
        """
        Step 19. Verify it should not showing any Filter Slider prompt.
        """
        #element=self.driver.find_element_by_css_selector("#Prompt_1")
        visual.verify_element_visiblty(None,"#Prompt_1", False, 'Step 19. Verify prompt not visible')
        
        
        """
        Step 20. Click Run in the toolbar 
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        """
        Step 21. Verify output
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 538, 60)
        x_axis_title=['Product Category', 'Product Category', 'Product Category', 'Product Category', 'Product Category', 'Product Category', 'Store Business Region', 'Store Business Region', 'Store Business Region', 'Store Business Region']
        visual.verify_x_axis_title(x_axis_title, msg='Step 21.1')
        
        expected_xaxis_label=['EMEA', 'North America', 'Oceania', 'South America', 'EMEA', 'North America', 'Oceania', 'South America', 'EMEA', 'North America', 'Oceania', 'South America', 'EMEA', 'North America', 'Oceania', 'South America']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 21.3')
        expected_zaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_z_axis_label(expected_zaxis_label, msg='Step 21.4')
        visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, 538, msg='Step 21.5')
        expected_label_list=['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
        visual.verify_rows_label(expected_label_list, msg='Step 21.6 Verify row labels')
        expected_label_list=['Sale Quarter', '1', '2', '3', '4', 'Gross Profit', '0M', '1.7M', '3.4M', '5M', '6.8M']
        visual.verify_column_label(expected_label_list, msg='Step 21.7 Verify column labels')
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar!r0!c0!']", "punch2", msg='Step 21.6')
        
        
        visual.take_run_window_snapshot(Test_Case_ID, '21')
        
        """
        Step 22. Close the output window
        """
        visual.switch_to_previous_window()
        
        """
        Step 23: Click "Save" in the toolbar > Type C2108833   > Click "Save" in the Save As dialog
        """
    
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 24: Logout of the IA API using the following URL: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(sleep_time)
        
if __name__ == '__main__':
    unittest.main()