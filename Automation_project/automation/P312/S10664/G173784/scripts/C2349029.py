'''
Created on Jan 05, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349029
Test_Case Name : Paperclipping in Pie chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2349029_TestClass(BaseTestCase):

    def test_C2349029(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349029'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        def verify_pie_chart(expected_legends, total_risers, step_num):
            visul_result.verify_riser_pie_labels_and_legends('MAINTABLE_wbody1_f', ['Revenue'], 'Step ' + step_num + '.1 : Verify pie chart label', same_group=True)
            visul_result.verify_riser_legends('MAINTABLE_wbody1_f', expected_legends, 'Step ' + step_num + '.2 : Verify pie chart legend values')
            visul_result.verify_number_of_pie_segments('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.3 : Verify number of pie chart risers')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mwedge!', 'lochmara', 'Step ' + step_num + '.4 : Verify pie chart riser color')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s1!g0!mwedge!', 'bar_green', 'Step ' + step_num + '.5 : Verify pie chart riser color')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s2!g0!mwedge!', 'dark_green', 'Step ' + step_num + '.6 : Verify pie chart riser color')
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        """
            Step 02 : Click Change drop down > Select Pie chart
        """
        visul_ribbon.change_chart_type('pie')
        visul_result.wait_for_property("#pfjTableChart_1 text[class='pieLabel!g0!mpieLabel!']", 1, 60, string_value='Group 0')
        
        """
            Step 03 : Double click "Revenue", "Product,Category" to add fields
        """
        metadata_obj.datatree_field_click('Revenue',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='pieLabel!g0!mpieLabel!']", 1, 80, string_value='Revenue')
        
        metadata_obj.datatree_field_click('Product,Category',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 80, string_value='Product Category')
          
        """
            Step 04 : Verify following pie chart preview displayed
        """
        expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_pie_chart(expected_legends, 7, '04')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_step_04', 'actual')
        
        """
            Step 05 : Lasso several slices
            Step 06 : Select "Group Product,Category selection"
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg path[class='riser!s2!g0!mwedge!']")
        source_cord=utillobj.get_object_screen_coordinate(source_element, 'right')
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg path[class='riser!s4!g0!mwedge!']")
        target_cord=utillobj.get_object_screen_coordinate(target_element, 'bottom_left')
        utillobj.drag_drop_on_screen(sx_offset=source_cord['x'], sy_offset=source_cord['y'],tx_offset=target_cord['x'],  ty_offset=target_cord['y'])
        expected_lasso=['3 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 05.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 07 : Verify preview,query and data pane updated with grouping
            Step 07.1 : Group is created in Color bucket "PRODUCT_CATEGORY_1", the slices selected are merged into one slice
        """
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        expected_query_pane=['Pie1', 'Matrix', 'Rows', 'Columns', 'Metric', 'Measure', 'Revenue', 'Color', 'PRODUCT_CATEGORY_1', 'Size', 'Tooltip']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1']
        expected_legends=['PRODUCT_CATEGORY_1', 'Accessories', 'Camcorder', 'Computers and Media Player and Stereo Systems', 'Televisions', 'Video Production']
        verify_pie_chart(expected_legends, 5, '07')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 07.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 07.8 : Verify query panel')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_step_07', 'actual')
        
        """
            Step 08 : Click Run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 08.1 : Verify chart output in run window
        """
        verify_pie_chart(expected_legends, 5, '08')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_08', 'actual')
        
        """
            Step 09 : Hover on value and verify tool tip values
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Computers and Media Player and Stereo Systems', 'Revenue:$640,684,475.00  (60.37%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s2!g0!mwedge!', expected_tooltip, 'Step 09.1 : Verify tool tip values')
        
        """
            Step 10 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 11 : Click Save in the toolbar > Save as "C2349029" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 12 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 13 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349029.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 13.1 : Verify preview
        """
        verify_pie_chart(expected_legends, 5, '13')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 13.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 13.8 : Verify query panel')
        
        """
            Step 14 : Click on Grouped slice and verify tooltip options
        """
        element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg path[class='riser!s2!g0!mwedge!']")
        utillobj.click_on_screen(element, 'middle', 0, pause=2)
        expected_lasso=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Computers and Media Player...', 'Ungroup Computers and Media Player...', 'Ungroup All']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 14.1 : Verify tooltip options')
        
        """
            Step 15 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()