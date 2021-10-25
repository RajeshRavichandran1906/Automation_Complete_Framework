'''
Created on Jan 08, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349041
Test_Case Name : Paperclipping in Gauge chart with field in columns bucket
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2349041_TestClass(BaseTestCase):

    def test_C2349041(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349041'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_gauge_chart(expected_column_labels, expected_total_labels, total_risers, total_lines, step_num):
            visul_result.verify_data_labels_('MAINTABLE_wbody1_f ', expected_column_labels, 'Step ' + step_num + '.1 : Verify Row labels', custom_css="svg .chartPanel text[class^='col']", data_label_length=42)
            visul_result.verify_data_labels('MAINTABLE_wbody1_f ', expected_total_labels, 'Step ' + step_num + '.2 : Verify Total labels', custom_css="svg .chartPanel text[class^='Total Label']")
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.3 : Verify number of risers', custome_css=" svg .chartPanel g>path")
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_lines, 'Step ' + step_num + '.4 : Verify number of lines', custome_css=" svg .chartPanel g>line")
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mrange!r0!c0!', 'lochmara', 'Step ' + step_num + '.5 : Verify riser color')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'gauge_secondary_ring', 'gray90', 'Step ' + step_num + '.6 : Verify riser color')
    
        """
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349040.fex
        """
        utillobj.infoassist_api_edit('C2349040', 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='rowHeader-label!']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        time.sleep(3)
        
        """
            Step 02 : Right click "PRODUCT_CATEGORY_1" in Rows > Delete
        """
        metadata_obj.querytree_field_click('PRODUCT_CATEGORY_1', 1, 1, 'Delete')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='Total Label']", 1, 80, string_value='798K')
        
        """
            Step 03 : Right click "PRODUCT_CATEGORY_1" in Data pane > Delete
        """
        metadata_obj.datatree_field_click('Dimensions->PRODUCT_CATEGORY_1', 1, 1, 'Delete')
        visul_result.wait_for_property("#iaMetaDataBrowser table[class='bi-tree-view-table']>tbody>tr:nth-child(12)>td", 1, 80, string_value='')
        
        """
            Step 04 : Drag and drop "Product,Category" to Columns
        """
        metadata_obj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Columns', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='colHeader-label!']", 1, 80, string_value='Product Category')
        
        """
            Step 05 : Verify following preview displayed
        """
        expected_column_labels=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_total_labels=['133K', '130K', '88,996', '135K', '247K', '16,516', '46,784']
        verify_gauge_chart(expected_column_labels, expected_total_labels, 14, 16, '05')
        
        """
            Step 06 : Lasso "Stereo systems to Video production" Columns
            Step 07 : Select "Group Product,Category selection"
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg path[class='riser!s0!g0!mrange!r0!c4!']")
        source_cord=utillobj.get_object_screen_coordinate(source_element, 'top_middle')
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg path[class='riser!s0!g0!mrange!r0!c6!']")
        target_cord=utillobj.get_object_screen_coordinate(target_element, 'bottom_right', x_offset=15, y_offset=12)
        utillobj.drag_drop_on_screen(sx_offset=source_cord['x'], sy_offset=source_cord['y'],tx_offset=target_cord['x'],  ty_offset=target_cord['y'])
        expected_lasso=['3 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 06.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='colHeader-label!']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 08 : Verify preview, query and data pane updated with grouping
            Group "PRODUCT_CATEGORY_1" is created in Columns bucket, the Stereo systems to Video production categories are combined in one Column.
        """
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        expected_column_labels=['PRODUCT_CATEGORY_1', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems and Televisions and Video Production']
        expected_total_labels=['133K', '130K', '88,996', '135K', '311K']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Define_1', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1']
        expected_query_pane=['Gauge1', 'Matrix', 'Rows', 'Columns', 'PRODUCT_CATEGORY_1', 'Marker', 'Measure', 'Define_1', 'Tooltip']
        verify_gauge_chart(expected_column_labels, expected_total_labels, 10, 12, '08')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 08.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 08.8 : Verify query panel')
        
        """
            Step 09 : Click Run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='colHeader-label!']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 09.1 : Verify run window
        """
        verify_gauge_chart(expected_column_labels, expected_total_labels, 10, 12, '09')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_09', 'actual')
        
        """
            Step 10 : Hover on grouped rows and verify tooltip values
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Stereo Systems and Televisions and Video Production', 'Define_1:310,644.19', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        tooltip_riser=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg .chartPanel g>path[class='riser!s0!g0!mrange!r0!c4!']")
        utillobj.click_on_screen(tooltip_riser, 'right', pause=2, x_offset=-20)
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', None, expected_tooltip, 'Step 10.1 : Verify tool tip values', default_move=True)
        
        """
            Step 11 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 12 : Click IA > Save as "C2349041" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349041.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='colHeader-label!']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        time.sleep(3)
        
        """
            Step 14.1 : Verify preview
        """
        verify_gauge_chart(expected_column_labels, expected_total_labels, 10, 12, '14')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 14.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 14.8 : Verify query panel')
        
        """
            Step 15 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()