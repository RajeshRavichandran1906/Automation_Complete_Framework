'''
Created on Jan 08, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349040
Test_Case Name : Paperclipping in Gauge chart with field in Rows bucket
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon, define_compute
from common.lib import utillity

class C2349040_TestClass(BaseTestCase):

    def test_C2349040(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349040'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        define=define_compute.Define_Compute(self.driver)
        
        def verify_gauge_chart(expected_row_labels, expected_total_labels, total_risers, total_lines, step_num):
            visul_result.verify_data_labels_('MAINTABLE_wbody1_f ', expected_row_labels, 'Step ' + step_num + '.1 : Verify Row labels', custom_css="svg .chartPanel text[class^='row']")
            visul_result.verify_data_labels_('MAINTABLE_wbody1_f ', expected_total_labels, 'Step ' + step_num + '.2 : Verify Total labels', custom_css="svg .chartPanel text[class^='Total Label']")
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.3 : Verify number of risers', custome_css=" svg .chartPanel g>path")
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_lines, 'Step ' + step_num + '.4 : Verify number of lines', custome_css=" svg .chartPanel g>line")
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mrange!r0!c0!', 'lochmara', 'Step ' + step_num + '.5 : Verify riser color')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'gauge_secondary_ring', 'gray90', 'Step ' + step_num + '.6 : Verify riser color')
    
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        """
            Step 02 : Click Change drop down > Gauge chart
        """
        visul_ribbon.change_chart_type('gauge')
        visul_result.wait_for_property("#pfjTableChart_1 svg text[class='Total Label']", 1, 80, string_value='60.2')
        
        """
            Step 03 : Click Calculation drop down > Define
        """
        visul_ribbon.select_ribbon_item('Home', 'calculation', opt='Detail (Define)')
        visul_result.wait_for_property("#fldCreatorOkBtn div", 1, 40, string_value='OK')
        
        """
            Step 04 : Add "Gross Profit" / "Revenue" in text box
            Step 05 : Click ok to create define.
        """
        define.select_define_compute_field('Gross Profit', 1)
        define.select_calculation_btns('div')
        define.select_define_compute_field('Revenue', 1)
        define.close_define_compute_dialog('ok')
        visul_result.wait_for_property("#iaMetaDataBrowser table[class='bi-tree-view-table']>tbody>tr:nth-child(5)>td", 1, 30, string_value='Define_1')
        
        """
            Step 06 : Double click "Define_1" and drag and drop "Product,Category" to Rows
        """
        metadata_obj.datatree_field_click('Measures->Define_1',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='Total Label']", 1, 80, string_value='798K')
        
        metadata_obj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Rows', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='rowHeader-label!']", 1, 80, string_value='Product Category')
        
        """
            Step 07 : Verify following preview displayed
        """
        expected_row_labels=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_total_labels=['133K', '130K', '88,996', '135K', '247K', '16,516', '46,784']
        verify_gauge_chart(expected_row_labels, expected_total_labels, 14, 16, '07')
        
        """
            Step 08 : Lasso "Accessories to Media player" Rows
            Step 09 : Select "Group Product,Category selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'path', 'riser!s0!g0!mrange!r0!c0!', target_tag='path', target_riser='riser!s0!g0!mrange!r3!c0!')
        expected_lasso=['4 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 05.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='rowHeader-label!']", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 10 : Verify preview, query and data pane updated with grouping
            Group "PRODUCT_CATEGORY_1" is created in Rows bucket, the selected categories are combined in one row.
        """
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        expected_row_labels=['PRODUCT_CATEGORY_1', 'Accessories and Camcorder and Computers and 1 more', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_total_labels=['487K', '247K', '16,516', '46,784']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Define_1', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1']
        expected_query_pane=['Gauge1', 'Matrix', 'Rows', 'PRODUCT_CATEGORY_1', 'Columns', 'Marker', 'Measure', 'Define_1', 'Tooltip']
        
        verify_gauge_chart(expected_row_labels, expected_total_labels, 8, 10, '10')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 10.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 10.8 : Verify query panel')
        
        """
            Step 11 : Hover on grouped rows and verify tooltip values
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers and 1 more', 'Define_1:486,937.89', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        tooltip_riser=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg .chartPanel g>path[class='riser!s0!g0!mrange!r0!c0!']")
        utillobj.click_on_screen(tooltip_riser, 'right', pause=2, x_offset=-8)
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mrange!r0!c0!', expected_tooltip, 'Step 11.1 : Verify tool tip values', default_move=True)
        
        """
            Step 12 : Click Save in the toolbar > Save as "C2349040" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Run fex from Resource tree using API
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2349040.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='rowHeader-label!']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 14.1 : Verify output in run window
        """
        verify_gauge_chart(expected_row_labels, expected_total_labels, 8, 10, '14')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_14', 'actual')
        expected_tooltip=['PRODUCT_CATEGORY_1:Video Production', 'Define_1:46,784.14', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mrange!r3!c0!', expected_tooltip, 'Step 14.7 : Verify tool tip values')
        
        """
            Step 15 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 16 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349040.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg text[class='rowHeader-label!']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 16.1. : Verify preview
        """
        verify_gauge_chart(expected_row_labels, expected_total_labels, 8, 10, '16')
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 16.7 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 16.8 : Verify query panel')
        
        """
            Step 17 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp       
        """
        utillobj.infoassist_api_logout()

if __name__ == '__main__':
    unittest.main()